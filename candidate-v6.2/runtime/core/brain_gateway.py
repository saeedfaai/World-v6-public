"""Provider-neutral cognition gateway with profile-scoped Resolution negotiation.

Providers receive only derived projection envelopes. Canonical input, omitted
field names, identity authority and Policy state never cross the adapter edge.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Protocol

from .resolution import (
    ProjectionProfile,
    ResolutionError,
    ResolutionMismatch,
    negotiate_resolution,
    project,
)


class BrainUnavailable(RuntimeError):
    pass


class BrainIncompatible(RuntimeError):
    pass


@dataclass(frozen=True)
class BrainInputSegment:
    """One canonical input domain with its own Resolution Profile.

    A request can carry several segments (for example task + conversation +
    price). This prevents a global ``R1`` from pretending to mean the same
    thing across unrelated domains.
    """

    segment_id: str
    canonical: dict[str, Any]
    profile_id: str
    profile_version: str
    profile_hash: str
    source_ref: str
    source_version: int
    desired_resolution: str
    minimum_resolution: str
    purpose: str
    data_class: str = "INTERNAL"
    freshness: str = "CURRENT"


@dataclass(frozen=True)
class BrainRequest:
    contract_version: str
    task_type: str
    inputs: tuple[BrainInputSegment, ...]
    world_id: str = "world-v6"
    entity_id: str = "secretary-001"
    principal_id: str = "human-root"
    conversation_id: str = "human-root:secretary-001"

    def __post_init__(self) -> None:
        if not self.inputs:
            raise BrainIncompatible("BrainRequest requires at least one input segment")
        segment_ids = [segment.segment_id for segment in self.inputs]
        if len(segment_ids) != len(set(segment_ids)):
            raise BrainIncompatible("duplicate Brain input segment_id")


@dataclass(frozen=True)
class BrainRequestDescriptor:
    """Value-free metadata used by a provider's compatibility gate."""

    contract_version: str
    task_type: str
    world_id: str
    entity_id: str
    principal_id: str
    conversation_id: str
    segments: tuple[dict[str, Any], ...]


@dataclass(frozen=True)
class ProjectedBrainInput:
    segment_id: str
    envelope: dict[str, Any]


@dataclass(frozen=True)
class ProjectedBrainRequest:
    contract_version: str
    task_type: str
    inputs: tuple[ProjectedBrainInput, ...]
    world_id: str
    entity_id: str
    principal_id: str
    conversation_id: str


@dataclass(frozen=True)
class BrainResponse:
    provider: str
    output: dict[str, Any]
    effective_resolutions: tuple[tuple[str, str], ...]

    @property
    def effective_resolution(self) -> str:
        if len(self.effective_resolutions) != 1:
            raise BrainIncompatible("request has a Resolution vector, not one scalar level")
        return self.effective_resolutions[0][1]


class BrainAdapter(Protocol):
    name: str

    def compatible(self, request: BrainRequestDescriptor) -> bool: ...

    def max_resolution_for(
        self, profile_id: str, profile_version: str, profile_hash: str
    ) -> str | None: ...

    def invoke(self, request: ProjectedBrainRequest) -> dict[str, Any]: ...


class BrainGateway:
    def __init__(self, providers: list[BrainAdapter], profiles: list[ProjectionProfile]):
        self.providers = providers
        self._profiles: dict[tuple[str, str], ProjectionProfile] = {}
        for profile in profiles:
            key = (profile.profile_id, profile.version)
            if key in self._profiles:
                raise BrainIncompatible(f"duplicate registered Resolution Profile: {key}")
            self._profiles[key] = profile

    def _profile_for(self, segment: BrainInputSegment) -> ProjectionProfile:
        profile = self._profiles.get((segment.profile_id, segment.profile_version))
        if profile is None:
            raise BrainIncompatible(
                f"unregistered Resolution Profile: {segment.profile_id}@{segment.profile_version}"
            )
        if segment.profile_hash != profile.profile_hash:
            raise BrainIncompatible(
                f"Resolution Profile hash mismatch: {segment.profile_id}@{segment.profile_version}"
            )
        return profile

    def _descriptor(self, request: BrainRequest) -> BrainRequestDescriptor:
        return BrainRequestDescriptor(
            contract_version=request.contract_version,
            task_type=request.task_type,
            world_id=request.world_id,
            entity_id=request.entity_id,
            principal_id=request.principal_id,
            conversation_id=request.conversation_id,
            segments=tuple(
                {
                    "segment_id": segment.segment_id,
                    "profile_id": segment.profile_id,
                    "profile_version": segment.profile_version,
                    "profile_hash": segment.profile_hash,
                    "source_ref": segment.source_ref,
                    "source_version": segment.source_version,
                    "desired_resolution": segment.desired_resolution,
                    "minimum_resolution": segment.minimum_resolution,
                    "purpose": segment.purpose,
                    "data_class": segment.data_class,
                    "freshness": segment.freshness,
                }
                for segment in request.inputs
            ),
        )

    @staticmethod
    def _provider_max(provider: BrainAdapter, segment: BrainInputSegment) -> str | None:
        capability = getattr(provider, "max_resolution_for", None)
        if callable(capability):
            return capability(segment.profile_id, segment.profile_version, segment.profile_hash)

        capabilities = getattr(provider, "resolution_capabilities", None)
        if isinstance(capabilities, Mapping):
            exact_key = f"{segment.profile_id}@{segment.profile_version}#{segment.profile_hash}"
            version_key = f"{segment.profile_id}@{segment.profile_version}"
            return capabilities.get(exact_key) or capabilities.get(version_key)
        return None

    def prepare_for_provider(
        self, request: BrainRequest, provider: BrainAdapter
    ) -> tuple[ProjectedBrainRequest, tuple[tuple[str, str], ...]]:
        """Project a request for one exact provider without invoking it.

        RC2 Manual Host workflows use this method to export the same safe
        envelope that a live adapter would receive.  It grants no authority and
        performs no provider/network operation.
        """
        profiles = {segment.segment_id: self._profile_for(segment) for segment in request.inputs}
        descriptor = self._descriptor(request)
        if not provider.compatible(descriptor):
            raise BrainIncompatible(f"provider is incompatible: {provider.name}")
        projected_inputs: list[ProjectedBrainInput] = []
        effective: list[tuple[str, str]] = []
        for segment in request.inputs:
            profile = profiles[segment.segment_id]
            provider_max = self._provider_max(provider, segment)
            if provider_max is None:
                raise ResolutionMismatch(
                    f"provider has no capability for {segment.profile_id}@{segment.profile_version}"
                )
            target = negotiate_resolution(
                desired=segment.desired_resolution,
                minimum=segment.minimum_resolution,
                brain_max=provider_max,
                canonical_resolution=profile.canonical_resolution,
            )
            projection = project(
                segment.canonical,
                profile=profile,
                target_resolution=target,
                source_ref=segment.source_ref,
                source_version=segment.source_version,
                purpose=segment.purpose,
                data_class=segment.data_class,
                freshness=segment.freshness,
            )
            projected_inputs.append(
                ProjectedBrainInput(segment.segment_id, projection.consumer_envelope())
            )
            effective.append((segment.segment_id, target))
        return (
            ProjectedBrainRequest(
                contract_version=request.contract_version,
                task_type=request.task_type,
                inputs=tuple(projected_inputs),
                world_id=request.world_id,
                entity_id=request.entity_id,
                principal_id=request.principal_id,
                conversation_id=request.conversation_id,
            ),
            tuple(effective),
        )

    def invoke(self, request: BrainRequest) -> BrainResponse:
        # Validate all profile bindings before any provider is considered.
        for segment in request.inputs:
            self._profile_for(segment)
        attempted: list[str] = []

        for provider in self.providers:
            try:
                projected_request, effective = self.prepare_for_provider(request, provider)
                attempted.append(provider.name)
                output = provider.invoke(projected_request)
                if not isinstance(output, dict):
                    raise BrainIncompatible("provider returned non-structured output")
                return BrainResponse(provider.name, output, effective)
            except (ResolutionError, BrainIncompatible):
                continue
            except Exception:
                # Provider failure may trigger failover, but no request invariant changes.
                continue
        raise BrainUnavailable(f"no compatible brain succeeded; attempted={attempted}")
