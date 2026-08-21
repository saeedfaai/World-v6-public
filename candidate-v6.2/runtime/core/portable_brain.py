"""Portable, provider-neutral Brain Pack support for World v6.2 RC2.

The module deliberately contains no vendor SDK and performs no network I/O.
It turns model output into a narrow Secretary Decision proposal, then renders
standard replies deterministically.  ChatGPT, Gemini, Grok, a local model, a
manual host session, and deterministic code can therefore share one identity,
state boundary, policy contract, and observable output contract.
"""
from __future__ import annotations

from dataclasses import dataclass
import re
import json
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from .brain_gateway import (
    BrainAdapter,
    BrainGateway,
    BrainRequest,
    BrainRequestDescriptor,
    BrainResponse,
    ProjectedBrainRequest,
)
from .resolution import ProjectionProfile, canonical_hash


class PortableBrainError(ValueError):
    """A portable pack, model output, or offline binding is invalid."""


_TOKEN_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/@#-]{0,191}$")
_HASH_RE = re.compile(r"^[0-9a-f]{64}$")
_ALLOWED_INTENTS = {
    "GREET",
    "TASK_CAPTURE",
    "TASK_LIST",
    "DRAFT",
    "PRICE_LOOKUP",
    "CLARIFY",
    "UNKNOWN",
}
_ALLOWED_RESPONSE_KINDS = {
    "ACKNOWLEDGE",
    "TASK_PROPOSAL",
    "TASK_LIST",
    "DRAFT_READY",
    "PRICE_RESULT",
    "CLARIFICATION_REQUEST",
    "SAFE_DEFER",
}
_ALLOWED_ACTIONS = {
    "NONE",
    "PROPOSE_TASK",
    "PROPOSE_DRAFT",
    "PROPOSE_PRICE_LOOKUP",
    "PROPOSE_EXTERNAL_EFFECT",
}
_FORBIDDEN_OUTPUT_KEYS = {
    "execute",
    "execute_now",
    "effect_executed",
    "approval_granted",
    "authority_granted",
    "canonical_write",
    "send_now",
}
_DECISION_KEYS = {
    "schema_version",
    "intent",
    "response_kind",
    "template_id",
    "slots",
    "proposed_actions",
    "requires_approval",
    "confidence_millis",
    "evidence_refs",
    "uncertainties",
}


def _token(value: str, label: str) -> None:
    if not isinstance(value, str) or _TOKEN_RE.fullmatch(value) is None:
        raise PortableBrainError(f"invalid {label}: {value!r}")


def _hash(value: str, label: str) -> None:
    if not isinstance(value, str) or _HASH_RE.fullmatch(value) is None:
        raise PortableBrainError(f"{label} must be a lowercase SHA-256")


def _scalar(value: Any, label: str) -> None:
    if value is None or isinstance(value, bool):
        return
    if isinstance(value, str):
        if len(value) > 4_000:
            raise PortableBrainError(f"{label} exceeds the bounded string limit")
        return
    if isinstance(value, int) and not isinstance(value, bool):
        if abs(value) > 9_007_199_254_740_991:
            raise PortableBrainError(f"{label} exceeds the canonical safe integer range")
        return
    raise PortableBrainError(f"{label} must be a canonical scalar")


@dataclass(frozen=True)
class PortableBrainPack:
    pack_id: str
    version: str
    world_id: str
    entity_id: str
    identity_ref: str
    dna_ref: str
    dna_hash: str
    root_constitution_ref: str
    prompt_contract_ref: str
    prompt_contract_hash: str
    output_contract_ref: str
    output_contract_hash: str
    templates: tuple[tuple[str, str], ...]
    allowed_task_types: tuple[str, ...]
    required_profile_bindings: tuple[tuple[str, str, str], ...]
    proposal_only: bool = True
    api_optional: bool = True

    def __post_init__(self) -> None:
        for value, label in (
            (self.pack_id, "pack_id"),
            (self.version, "version"),
            (self.world_id, "world_id"),
            (self.entity_id, "entity_id"),
            (self.identity_ref, "identity_ref"),
            (self.dna_ref, "dna_ref"),
            (self.root_constitution_ref, "root_constitution_ref"),
            (self.prompt_contract_ref, "prompt_contract_ref"),
            (self.output_contract_ref, "output_contract_ref"),
        ):
            _token(value, label)
        for value, label in (
            (self.dna_hash, "dna_hash"),
            (self.prompt_contract_hash, "prompt_contract_hash"),
            (self.output_contract_hash, "output_contract_hash"),
        ):
            _hash(value, label)
        if self.proposal_only is not True:
            raise PortableBrainError("RC2 Brain Packs must be proposal-only")
        if self.api_optional is not True:
            raise PortableBrainError("RC2 reference pack must remain usable without an API")
        template_ids = [key for key, _ in self.templates]
        if not template_ids or len(template_ids) != len(set(template_ids)):
            raise PortableBrainError("template ids must be non-empty and unique")
        for key, template in self.templates:
            _token(key, "template_id")
            if not isinstance(template, str) or not template or len(template) > 4_000:
                raise PortableBrainError("template must be a bounded non-empty string")
        if not self.allowed_task_types:
            raise PortableBrainError("pack requires at least one task type")
        if len(self.allowed_task_types) != len(set(self.allowed_task_types)):
            raise PortableBrainError("duplicate allowed task type")
        for task_type in self.allowed_task_types:
            _token(task_type, "task_type")
        profile_keys: set[tuple[str, str]] = set()
        for profile_id, version, digest in self.required_profile_bindings:
            _token(profile_id, "profile_id")
            _token(version, "profile_version")
            _hash(digest, "profile_hash")
            key = (profile_id, version)
            if key in profile_keys:
                raise PortableBrainError("duplicate profile binding")
            profile_keys.add(key)

    def to_document(self) -> dict[str, Any]:
        return {
            "pack_id": self.pack_id,
            "version": self.version,
            "world_id": self.world_id,
            "entity_id": self.entity_id,
            "identity_ref": self.identity_ref,
            "dna_ref": self.dna_ref,
            "dna_hash": self.dna_hash,
            "root_constitution_ref": self.root_constitution_ref,
            "prompt_contract_ref": self.prompt_contract_ref,
            "prompt_contract_hash": self.prompt_contract_hash,
            "output_contract_ref": self.output_contract_ref,
            "output_contract_hash": self.output_contract_hash,
            "templates": {key: value for key, value in sorted(self.templates)},
            "allowed_task_types": list(self.allowed_task_types),
            "required_profile_bindings": [
                {"profile_id": item[0], "version": item[1], "sha256": item[2]}
                for item in sorted(self.required_profile_bindings)
            ],
            "proposal_only": self.proposal_only,
            "api_optional": self.api_optional,
        }

    @property
    def pack_hash(self) -> str:
        return canonical_hash(self.to_document())

    def template(self, template_id: str) -> str:
        try:
            return dict(self.templates)[template_id]
        except KeyError as exc:
            raise PortableBrainError(f"unknown template_id: {template_id}") from exc


def portable_pack_from_document(document: Mapping[str, Any]) -> PortableBrainPack:
    required = {
        "pack_id",
        "version",
        "world_id",
        "entity_id",
        "identity_ref",
        "dna_ref",
        "dna_hash",
        "root_constitution_ref",
        "prompt_contract_ref",
        "prompt_contract_hash",
        "output_contract_ref",
        "output_contract_hash",
        "templates",
        "allowed_task_types",
        "required_profile_bindings",
        "proposal_only",
        "api_optional",
    }
    if set(document) != required:
        raise PortableBrainError("Portable Brain Pack key set mismatch")
    templates = document["templates"]
    bindings = document["required_profile_bindings"]
    if not isinstance(templates, Mapping) or not isinstance(bindings, list):
        raise PortableBrainError("invalid templates/profile bindings")
    parsed_bindings: list[tuple[str, str, str]] = []
    for item in bindings:
        if not isinstance(item, Mapping) or set(item) != {"profile_id", "version", "sha256"}:
            raise PortableBrainError("invalid profile binding")
        parsed_bindings.append((item["profile_id"], item["version"], item["sha256"]))
    task_types = document["allowed_task_types"]
    if not isinstance(task_types, list):
        raise PortableBrainError("allowed_task_types must be an array")
    return PortableBrainPack(
        pack_id=document["pack_id"],
        version=document["version"],
        world_id=document["world_id"],
        entity_id=document["entity_id"],
        identity_ref=document["identity_ref"],
        dna_ref=document["dna_ref"],
        dna_hash=document["dna_hash"],
        root_constitution_ref=document["root_constitution_ref"],
        prompt_contract_ref=document["prompt_contract_ref"],
        prompt_contract_hash=document["prompt_contract_hash"],
        output_contract_ref=document["output_contract_ref"],
        output_contract_hash=document["output_contract_hash"],
        templates=tuple(sorted(templates.items())),
        allowed_task_types=tuple(task_types),
        required_profile_bindings=tuple(parsed_bindings),
        proposal_only=document["proposal_only"],
        api_optional=document["api_optional"],
    )


def load_portable_pack(path: str | Path) -> PortableBrainPack:
    document = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(document, Mapping):
        raise PortableBrainError("Portable Brain Pack must be a JSON object")
    return portable_pack_from_document(document)


@dataclass(frozen=True)
class SecretaryDecision:
    schema_version: str
    intent: str
    response_kind: str
    template_id: str
    slots: tuple[tuple[str, Any], ...]
    proposed_actions: tuple[str, ...]
    requires_approval: bool
    confidence_millis: int
    evidence_refs: tuple[str, ...]
    uncertainties: tuple[str, ...]

    def __post_init__(self) -> None:
        if self.schema_version != "world-v6.secretary-decision.v1":
            raise PortableBrainError("unsupported Secretary Decision schema")
        if self.intent not in _ALLOWED_INTENTS:
            raise PortableBrainError("unsupported intent")
        if self.response_kind not in _ALLOWED_RESPONSE_KINDS:
            raise PortableBrainError("unsupported response_kind")
        _token(self.template_id, "template_id")
        slot_keys = [key for key, _ in self.slots]
        if len(slot_keys) != len(set(slot_keys)):
            raise PortableBrainError("duplicate decision slot")
        for key, value in self.slots:
            _token(key, "slot name")
            _scalar(value, f"slot {key}")
        if not self.proposed_actions:
            raise PortableBrainError("proposed_actions cannot be empty")
        if len(self.proposed_actions) != len(set(self.proposed_actions)):
            raise PortableBrainError("duplicate proposed action")
        for action in self.proposed_actions:
            if action not in _ALLOWED_ACTIONS:
                raise PortableBrainError(f"forbidden proposed action: {action}")
        if "PROPOSE_EXTERNAL_EFFECT" in self.proposed_actions and not self.requires_approval:
            raise PortableBrainError("external-effect proposal must require approval")
        if not isinstance(self.requires_approval, bool):
            raise PortableBrainError("requires_approval must be boolean")
        if not isinstance(self.confidence_millis, int) or isinstance(self.confidence_millis, bool):
            raise PortableBrainError("confidence_millis must be an integer")
        if not 0 <= self.confidence_millis <= 1000:
            raise PortableBrainError("confidence_millis outside 0..1000")
        for ref in self.evidence_refs:
            _token(ref, "evidence_ref")
        for item in self.uncertainties:
            if not isinstance(item, str) or len(item) > 500:
                raise PortableBrainError("uncertainty must be a bounded string")

    def semantic_document(self) -> dict[str, Any]:
        """Provider-independent fields that determine the observable answer."""
        return {
            "schema_version": self.schema_version,
            "intent": self.intent,
            "response_kind": self.response_kind,
            "template_id": self.template_id,
            "slots": {key: value for key, value in sorted(self.slots)},
            "proposed_actions": list(self.proposed_actions),
            "requires_approval": self.requires_approval,
        }

    def to_document(self) -> dict[str, Any]:
        return {
            **self.semantic_document(),
            "decision_id": self.decision_id,
            "confidence_millis": self.confidence_millis,
            "evidence_refs": list(self.evidence_refs),
            "uncertainties": list(self.uncertainties),
            "proposal_only": True,
        }

    @property
    def semantic_hash(self) -> str:
        return canonical_hash(self.semantic_document())

    @property
    def decision_id(self) -> str:
        return f"decision:{self.semantic_hash}"


def normalize_secretary_decision(raw: Mapping[str, Any]) -> SecretaryDecision:
    if not isinstance(raw, Mapping):
        raise PortableBrainError("model output must be an object")
    keys = set(raw)
    forbidden = keys & _FORBIDDEN_OUTPUT_KEYS
    if forbidden:
        raise PortableBrainError(f"authoritative/effect key forbidden: {sorted(forbidden)}")
    if keys != _DECISION_KEYS:
        missing = sorted(_DECISION_KEYS - keys)
        extra = sorted(keys - _DECISION_KEYS)
        raise PortableBrainError(f"decision key mismatch; missing={missing}, extra={extra}")
    slots = raw["slots"]
    if not isinstance(slots, Mapping):
        raise PortableBrainError("slots must be an object")
    actions = raw["proposed_actions"]
    evidence = raw["evidence_refs"]
    uncertainties = raw["uncertainties"]
    if not isinstance(actions, list) or not all(isinstance(item, str) for item in actions):
        raise PortableBrainError("proposed_actions must be a string array")
    if not isinstance(evidence, list) or not all(isinstance(item, str) for item in evidence):
        raise PortableBrainError("evidence_refs must be a string array")
    if not isinstance(uncertainties, list) or not all(
        isinstance(item, str) for item in uncertainties
    ):
        raise PortableBrainError("uncertainties must be a string array")
    return SecretaryDecision(
        schema_version=raw["schema_version"],
        intent=raw["intent"],
        response_kind=raw["response_kind"],
        template_id=raw["template_id"],
        slots=tuple(sorted(slots.items())),
        proposed_actions=tuple(actions),
        requires_approval=raw["requires_approval"],
        confidence_millis=raw["confidence_millis"],
        evidence_refs=tuple(evidence),
        uncertainties=tuple(uncertainties),
    )


class _StrictSlots(dict[str, Any]):
    def __missing__(self, key: str) -> Any:
        raise PortableBrainError(f"template requires missing slot: {key}")


def render_secretary_decision(pack: PortableBrainPack, decision: SecretaryDecision) -> str:
    template = pack.template(decision.template_id)
    try:
        rendered = template.format_map(_StrictSlots(dict(decision.slots)))
    except PortableBrainError:
        raise
    except (ValueError, KeyError) as exc:
        raise PortableBrainError("invalid template/slot binding") from exc
    if len(rendered) > 8_000:
        raise PortableBrainError("rendered reply exceeds bounded output")
    return rendered


class ScriptedPortableAdapter:
    """Offline deterministic adapter used for code fallback, fixtures, and tests."""

    network_required = False
    api_token_required = False

    def __init__(
        self,
        name: str,
        capabilities: Mapping[tuple[str, str, str], str],
        responder: Mapping[str, Any] | Callable[[ProjectedBrainRequest], Mapping[str, Any]],
        *,
        task_types: Sequence[str] = (),
    ) -> None:
        _token(name, "adapter name")
        self.name = name
        self._capabilities = dict(capabilities)
        self._responder = dict(responder) if isinstance(responder, Mapping) else responder
        self._task_types = frozenset(task_types)
        self.last_request: ProjectedBrainRequest | None = None

    def compatible(self, request: BrainRequestDescriptor) -> bool:
        return not self._task_types or request.task_type in self._task_types

    def max_resolution_for(
        self, profile_id: str, profile_version: str, profile_hash: str
    ) -> str | None:
        return self._capabilities.get((profile_id, profile_version, profile_hash))

    def invoke(self, request: ProjectedBrainRequest) -> dict[str, Any]:
        self.last_request = request
        response = self._responder(request) if callable(self._responder) else self._responder
        if not isinstance(response, Mapping):
            raise PortableBrainError("scripted response must be an object")
        return dict(response)


class ManualHostAdapter(ScriptedPortableAdapter):
    """No-token bridge: paste/export a pack to any model and import strict JSON."""

    def export_exchange(
        self,
        request: ProjectedBrainRequest,
        pack: PortableBrainPack,
    ) -> dict[str, Any]:
        return {
            "exchange_contract": "world-v6.manual-brain-exchange.v1",
            "pack_id": pack.pack_id,
            "pack_version": pack.version,
            "pack_hash": pack.pack_hash,
            "provider_hint": self.name,
            "request": {
                "contract_version": request.contract_version,
                "task_type": request.task_type,
                "world_id": request.world_id,
                "entity_id": request.entity_id,
                "principal_id": request.principal_id,
                "conversation_id": request.conversation_id,
                "inputs": [
                    {"segment_id": item.segment_id, "envelope": item.envelope}
                    for item in request.inputs
                ],
            },
            "response_contract_ref": pack.output_contract_ref,
            "proposal_only": True,
            "network_performed_by_runtime": False,
            "api_token_used_by_runtime": False,
        }

    def import_response(self, document: Mapping[str, Any]) -> SecretaryDecision:
        """Validate and stage a pasted host response for a later Gateway run."""
        decision = normalize_secretary_decision(document)
        self._responder = dict(document)
        return decision


@dataclass(frozen=True)
class PortableSecretaryResult:
    provider: str
    decision: SecretaryDecision
    rendered_text: str
    effective_resolutions: tuple[tuple[str, str], ...]
    pack_hash: str


class PortableSecretaryRunner:
    """One stable Secretary contract over interchangeable offline/live adapters."""

    def __init__(
        self,
        pack: PortableBrainPack,
        adapters: Sequence[BrainAdapter],
        profiles: Sequence[ProjectionProfile],
        *,
        allow_network: bool = False,
        allow_api_tokens: bool = False,
    ) -> None:
        if not adapters:
            raise PortableBrainError("at least one adapter is required")
        for adapter in adapters:
            if getattr(adapter, "network_required", False) and not allow_network:
                raise PortableBrainError(f"network adapter disabled: {adapter.name}")
            if getattr(adapter, "api_token_required", False) and not allow_api_tokens:
                raise PortableBrainError(f"API-token adapter disabled: {adapter.name}")
        actual = {(profile.profile_id, profile.version): profile.profile_hash for profile in profiles}
        for profile_id, version, digest in pack.required_profile_bindings:
            if actual.get((profile_id, version)) != digest:
                raise PortableBrainError(
                    f"pack/profile binding mismatch: {profile_id}@{version}"
                )
        self.pack = pack
        self.gateway = BrainGateway(list(adapters), list(profiles))

    def _validate_request(self, request: BrainRequest) -> None:
        if request.task_type not in self.pack.allowed_task_types:
            raise PortableBrainError(f"task type not allowed by pack: {request.task_type}")
        if request.world_id != self.pack.world_id or request.entity_id != self.pack.entity_id:
            raise PortableBrainError("request identity differs from the immutable pack binding")

    def prepare_manual_exchange(
        self, request: BrainRequest, adapter: ManualHostAdapter
    ) -> dict[str, Any]:
        self._validate_request(request)
        if adapter not in self.gateway.providers:
            raise PortableBrainError("manual adapter is not registered in this runner")
        projected, effective = self.gateway.prepare_for_provider(request, adapter)
        exchange = adapter.export_exchange(projected, self.pack)
        exchange["effective_resolutions"] = {
            segment_id: level for segment_id, level in effective
        }
        return exchange

    def run(self, request: BrainRequest) -> PortableSecretaryResult:
        self._validate_request(request)
        response: BrainResponse = self.gateway.invoke(request)
        decision = normalize_secretary_decision(response.output)
        return PortableSecretaryResult(
            provider=response.provider,
            decision=decision,
            rendered_text=render_secretary_decision(self.pack, decision),
            effective_resolutions=response.effective_resolutions,
            pack_hash=self.pack.pack_hash,
        )
