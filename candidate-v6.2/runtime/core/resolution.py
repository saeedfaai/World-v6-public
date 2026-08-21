"""Deterministic Resolution primitives for the World v6.2 RC1.

Resolution is a compatibility/view mechanism. It never grants authority,
changes identity, lowers data classification, or replaces canonical state.
Canonical state is always hashed as strict World Canonical JSON v1; projected
views are derived and non-authoritative.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
import re
from typing import Any, Iterable, Literal, Mapping


DowngradePolicy = Literal["SAFE_TO_PROJECT", "READ_ONLY_WHEN_PROJECTED", "NO_DOWNGRADE"]
JsonType = Literal["string", "integer", "boolean", "null", "array", "object"]

_RES_RE = re.compile(r"^R(0|[1-9][0-9]*)$")
_TOKEN_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/-]{0,191}$")
_CLASS_RANK = {"PUBLIC": 0, "INTERNAL": 1, "CONFIDENTIAL": 2, "RESTRICTED": 3}
_MAX_SAFE_INTEGER = 9_007_199_254_740_991
_MAX_DOCUMENT_DEPTH = 64
_MAX_DOCUMENT_NODES = 100_000
_MAX_PROFILE_FIELDS = 4_096
_MAX_PATCH_OPERATIONS = 128

COMPILER_ID = "world-v6.structural-resolution-compiler"
COMPILER_VERSION = "0.2.0"
_COMPILER_CONTRACT = (
    "strict-json-v1|json-pointer-leaves|fail-closed-unknown|monotonic-fields|"
    "projection-derived-non-authoritative|bounded-existing-scalar-patch|"
    "canonical-reload-for-up-resolution"
)
COMPILER_HASH = hashlib.sha256(_COMPILER_CONTRACT.encode("utf-8")).hexdigest()


class ResolutionError(ValueError):
    pass


class CanonicalJSONError(ResolutionError):
    pass


class ResolutionMismatch(ResolutionError):
    pass


class ProjectionError(ResolutionError):
    pass


class PatchRejected(ResolutionError):
    pass


def _validate_canonical_json(value: Any, *, _depth: int = 0, _counter: list[int] | None = None) -> None:
    """Validate the restricted, cross-language World Canonical JSON v1 domain.

    Floats and implicit stringification are forbidden. Decimal, datetime and
    other domain values must be normalized by their schema adapter first (for
    example a monetary Decimal becomes an exact decimal string).
    """
    if _counter is None:
        _counter = [0]
    _counter[0] += 1
    if _counter[0] > _MAX_DOCUMENT_NODES:
        raise CanonicalJSONError("canonical document exceeds node limit")
    if _depth > _MAX_DOCUMENT_DEPTH:
        raise CanonicalJSONError("canonical document exceeds depth limit")

    if value is None or isinstance(value, (str, bool)):
        return
    if isinstance(value, int) and not isinstance(value, bool):
        if abs(value) > _MAX_SAFE_INTEGER:
            raise CanonicalJSONError("integer exceeds World Canonical JSON safe range")
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise CanonicalJSONError("non-finite number is forbidden")
        raise CanonicalJSONError("floats are forbidden; normalize exact values before hashing")
    if isinstance(value, list):
        for child in value:
            _validate_canonical_json(child, _depth=_depth + 1, _counter=_counter)
        return
    if isinstance(value, Mapping):
        for key, child in value.items():
            if not isinstance(key, str):
                raise CanonicalJSONError("canonical object keys must be strings")
            _validate_canonical_json(child, _depth=_depth + 1, _counter=_counter)
        return
    raise CanonicalJSONError(f"unsupported canonical JSON type: {type(value).__name__}")


def canonical_json(value: Any) -> str:
    _validate_canonical_json(value)
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def resolution_rank(level: str) -> int:
    if not isinstance(level, str):
        raise ResolutionError("resolution must be a string such as R0")
    match = _RES_RE.fullmatch(level)
    if not match:
        raise ResolutionError(f"invalid resolution: {level!r}")
    return int(match.group(1))


def lower_or_equal(a: str, b: str) -> bool:
    return resolution_rank(a) <= resolution_rank(b)


def negotiate_resolution(
    *, desired: str, minimum: str, brain_max: str, canonical_resolution: str | None = None
) -> str:
    """Select the highest supported resolution without weakening the minimum."""
    desired_rank, minimum_rank, brain_rank = map(
        resolution_rank, (desired, minimum, brain_max)
    )
    if desired_rank < minimum_rank:
        raise ResolutionMismatch("desired resolution is below task minimum")
    if canonical_resolution is not None:
        canonical_rank = resolution_rank(canonical_resolution)
        if desired_rank > canonical_rank or minimum_rank > canonical_rank:
            raise ResolutionMismatch("request exceeds the profile canonical resolution")
        brain_rank = min(brain_rank, canonical_rank)
    effective_rank = min(desired_rank, brain_rank)
    if effective_rank < minimum_rank:
        raise ResolutionMismatch(
            f"brain supports only R{brain_rank}, but task requires at least R{minimum_rank}"
        )
    return f"R{effective_rank}"


def _validate_token(value: str, label: str) -> None:
    if not isinstance(value, str) or not _TOKEN_RE.fullmatch(value):
        raise ResolutionError(f"invalid {label}: {value!r}")


def _decode_pointer(path: str) -> tuple[str, ...]:
    if not isinstance(path, str) or not path.startswith("/") or len(path) > 512:
        raise ResolutionError(f"path must be a bounded JSON Pointer: {path!r}")
    raw_parts = path[1:].split("/")
    if not raw_parts or any(part == "" for part in raw_parts):
        raise ResolutionError(f"empty JSON Pointer segment is forbidden: {path!r}")
    parts: list[str] = []
    for raw in raw_parts:
        index = 0
        decoded: list[str] = []
        while index < len(raw):
            if raw[index] != "~":
                decoded.append(raw[index])
                index += 1
                continue
            if index + 1 >= len(raw) or raw[index + 1] not in {"0", "1"}:
                raise ResolutionError(f"invalid JSON Pointer escape: {path!r}")
            decoded.append("~" if raw[index + 1] == "0" else "/")
            index += 2
        parts.append("".join(decoded))
    return tuple(parts)


def _encode_pointer(parts: Iterable[str]) -> str:
    return "/" + "/".join(part.replace("~", "~0").replace("/", "~1") for part in parts)


def _json_type(value: Any) -> JsonType:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, Mapping):
        return "object"
    raise CanonicalJSONError(f"unsupported canonical JSON type: {type(value).__name__}")


def _profile_data_class(profile: "ProjectionProfile") -> str:
    return max(
        (field.data_class for field in profile.fields),
        key=lambda item: _CLASS_RANK[item],
    )


@dataclass(frozen=True)
class FieldRule:
    path: str
    introduced_at: str = "R0"
    write_min_resolution: str | None = None
    downgrade_policy: DowngradePolicy = "SAFE_TO_PROJECT"
    cable_id: str = "GENERAL"
    semantic_contract_id: str = "world-v6.semantic.general.v1"
    data_class: str = "INTERNAL"
    expected_type: JsonType | None = None
    required_for_actions: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        _decode_pointer(self.path)
        introduced = resolution_rank(self.introduced_at)
        write_min = resolution_rank(self.write_min)
        if write_min < introduced:
            raise ResolutionError("write_min_resolution cannot be below introduced_at")
        if self.downgrade_policy not in {
            "SAFE_TO_PROJECT", "READ_ONLY_WHEN_PROJECTED", "NO_DOWNGRADE"
        }:
            raise ResolutionError(f"invalid downgrade policy: {self.downgrade_policy}")
        _validate_token(self.cable_id, "cable_id")
        _validate_token(self.semantic_contract_id, "semantic_contract_id")
        if self.data_class not in _CLASS_RANK:
            raise ResolutionError(f"invalid data_class: {self.data_class}")
        if self.expected_type not in {None, "string", "integer", "boolean", "null", "array", "object"}:
            raise ResolutionError(f"invalid expected_type: {self.expected_type}")
        for action in self.required_for_actions:
            _validate_token(action, "action")

    @property
    def write_min(self) -> str:
        return self.write_min_resolution or self.introduced_at

    def to_document(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "introduced_at": self.introduced_at,
            "write_min_resolution": self.write_min_resolution,
            "downgrade_policy": self.downgrade_policy,
            "cable_id": self.cable_id,
            "semantic_contract_id": self.semantic_contract_id,
            "data_class": self.data_class,
            "expected_type": self.expected_type,
            "required_for_actions": list(sorted(self.required_for_actions)),
        }


@dataclass(frozen=True)
class ActionRule:
    action: str
    minimum_resolution: str
    required_paths: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        _validate_token(self.action, "action")
        resolution_rank(self.minimum_resolution)
        for path in self.required_paths:
            _decode_pointer(path)

    def to_document(self) -> dict[str, Any]:
        return {
            "action": self.action,
            "minimum_resolution": self.minimum_resolution,
            "required_paths": list(sorted(self.required_paths)),
        }


@dataclass(frozen=True)
class ProjectionProfile:
    profile_id: str
    version: str
    canonical_resolution: str
    fields: tuple[FieldRule, ...]
    allow_unspecified: bool = False
    required_backbone_paths: tuple[str, ...] = ()
    actions: tuple[ActionRule, ...] = ()

    def __post_init__(self) -> None:
        _validate_token(self.profile_id, "profile_id")
        _validate_token(self.version, "profile version")
        canonical_rank = resolution_rank(self.canonical_resolution)
        if self.allow_unspecified:
            raise ResolutionError("allow_unspecified=true is unsafe and unsupported in RC1")
        if not self.fields or len(self.fields) > _MAX_PROFILE_FIELDS:
            raise ResolutionError("profile field count is outside allowed bounds")

        seen: set[str] = set()
        decoded: dict[str, tuple[str, ...]] = {}
        for rule in self.fields:
            if rule.path in seen:
                raise ResolutionError(f"duplicate projection rule: {rule.path}")
            if resolution_rank(rule.introduced_at) > canonical_rank:
                raise ResolutionError(f"field introduced above canonical resolution: {rule.path}")
            if resolution_rank(rule.write_min) > canonical_rank:
                raise ResolutionError(f"field write minimum above canonical resolution: {rule.path}")
            seen.add(rule.path)
            decoded[rule.path] = _decode_pointer(rule.path)

        paths = list(decoded)
        for index, left in enumerate(paths):
            left_parts = decoded[left]
            for right in paths[index + 1:]:
                right_parts = decoded[right]
                shorter = min(len(left_parts), len(right_parts))
                if left_parts[:shorter] == right_parts[:shorter]:
                    raise ResolutionError(f"ancestor/descendant field rules overlap: {left} / {right}")

        rules = self.rule_map()
        for path in self.required_backbone_paths:
            _decode_pointer(path)
            rule = rules.get(path)
            if rule is None or rule.introduced_at != "R0":
                raise ResolutionError(f"required backbone path must be an R0 field: {path}")

        action_names: set[str] = set()
        for action in self.actions:
            if action.action in action_names:
                raise ResolutionError(f"duplicate action rule: {action.action}")
            action_names.add(action.action)
            if resolution_rank(action.minimum_resolution) > canonical_rank:
                raise ResolutionError(f"action minimum exceeds canonical resolution: {action.action}")
            for path in action.required_paths:
                if path not in seen:
                    raise ResolutionError(f"action requires undeclared field: {action.action} -> {path}")

    def rule_map(self) -> dict[str, FieldRule]:
        return {field.path: field for field in self.fields}

    def action_rule_map(self) -> dict[str, ActionRule]:
        return {action.action: action for action in self.actions}

    def to_document(self) -> dict[str, Any]:
        return {
            "profile_id": self.profile_id,
            "version": self.version,
            "canonical_resolution": self.canonical_resolution,
            "allow_unspecified": False,
            "required_backbone_paths": list(sorted(self.required_backbone_paths)),
            "fields": [field.to_document() for field in sorted(self.fields, key=lambda item: item.path)],
            "actions": [action.to_document() for action in sorted(self.actions, key=lambda item: item.action)],
        }

    @property
    def profile_hash(self) -> str:
        return canonical_hash(self.to_document())


def profile_from_document(document: Mapping[str, Any]) -> ProjectionProfile:
    try:
        fields = tuple(
            FieldRule(
                path=item["path"],
                introduced_at=item["introduced_at"],
                write_min_resolution=item.get("write_min_resolution"),
                downgrade_policy=item["downgrade_policy"],
                cable_id=item["cable_id"],
                semantic_contract_id=item["semantic_contract_id"],
                data_class=item["data_class"],
                expected_type=item.get("expected_type"),
                required_for_actions=tuple(item.get("required_for_actions", ())),
            )
            for item in document["fields"]
        )
        actions = tuple(
            ActionRule(
                action=item["action"],
                minimum_resolution=item["minimum_resolution"],
                required_paths=tuple(item.get("required_paths", ())),
            )
            for item in document.get("actions", ())
        )
        return ProjectionProfile(
            profile_id=document["profile_id"],
            version=document["version"],
            canonical_resolution=document["canonical_resolution"],
            fields=fields,
            allow_unspecified=document.get("allow_unspecified", False),
            required_backbone_paths=tuple(document.get("required_backbone_paths", ())),
            actions=actions,
        )
    except (KeyError, TypeError) as exc:
        raise ResolutionError(f"invalid profile document: {exc}") from exc


def load_profile_file(path: str | Path) -> ProjectionProfile:
    try:
        document = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ResolutionError(f"cannot load resolution profile {path}: {exc}") from exc
    if not isinstance(document, Mapping):
        raise ResolutionError("resolution profile root must be an object")
    return profile_from_document(document)


@dataclass(frozen=True)
class ProjectionResult:
    profile_id: str
    profile_version: str
    profile_hash: str
    canonical_hash: str
    canonical_resolution: str
    target_resolution: str
    projection_hash: str
    source_ref: str
    source_version: int
    purpose: str
    data_class: str
    freshness: str
    value: dict[str, Any]
    included_paths: tuple[str, ...]
    omitted_paths: tuple[str, ...]
    read_only_paths: tuple[str, ...]
    no_downgrade_paths: tuple[str, ...]
    compiler_id: str = COMPILER_ID
    compiler_version: str = COMPILER_VERSION
    compiler_hash: str = COMPILER_HASH
    derived: bool = True
    authoritative: bool = False

    def consumer_envelope(self) -> dict[str, Any]:
        """Return the provider-safe envelope; omitted field names stay audit-internal."""
        return {
            "profile_id": self.profile_id,
            "profile_version": self.profile_version,
            "profile_hash": self.profile_hash,
            "source_ref": self.source_ref,
            "source_version": self.source_version,
            "canonical_hash": self.canonical_hash,
            "canonical_resolution": self.canonical_resolution,
            "effective_resolution": self.target_resolution,
            "projection_hash": self.projection_hash,
            "compiler_id": self.compiler_id,
            "compiler_version": self.compiler_version,
            "compiler_hash": self.compiler_hash,
            "purpose": self.purpose,
            "data_class": self.data_class,
            "freshness": self.freshness,
            "projection_derived": True,
            "projection_authoritative": False,
            "value": deepcopy(self.value),
        }

    def audit_metadata(self) -> dict[str, Any]:
        metadata = self.consumer_envelope()
        metadata.pop("value")
        metadata.update({
            "included_paths": list(self.included_paths),
            "omitted_paths": list(self.omitted_paths),
            "read_only_paths": list(self.read_only_paths),
            "no_downgrade_paths": list(self.no_downgrade_paths),
        })
        return metadata


@dataclass(frozen=True)
class PatchOperation:
    path: str
    value: Any

    def __post_init__(self) -> None:
        _decode_pointer(self.path)
        _validate_canonical_json(self.value)


@dataclass(frozen=True)
class ResolutionPatch:
    actor_resolution: str
    expected_canonical_hash: str
    expected_projection_hash: str
    expected_version: int
    source_ref: str
    operations: tuple[PatchOperation, ...]
    projection_profile_id: str
    projection_profile_version: str
    projection_profile_hash: str

    def __post_init__(self) -> None:
        resolution_rank(self.actor_resolution)
        for label, digest in {
            "expected_canonical_hash": self.expected_canonical_hash,
            "expected_projection_hash": self.expected_projection_hash,
            "projection_profile_hash": self.projection_profile_hash,
        }.items():
            if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                raise ResolutionError(f"invalid {label}")
        if not isinstance(self.expected_version, int) or self.expected_version < 0:
            raise ResolutionError("expected_version must be a non-negative integer")
        _validate_token(self.source_ref, "source_ref")
        if not self.operations or len(self.operations) > _MAX_PATCH_OPERATIONS:
            raise ResolutionError("patch operation count is outside allowed bounds")


def _leaf_paths(value: Any, prefix: tuple[str, ...] = ()) -> Iterable[tuple[str, Any]]:
    if isinstance(value, Mapping):
        if not value and prefix:
            yield _encode_pointer(prefix), {}
        for key, child in value.items():
            yield from _leaf_paths(child, prefix + (key,))
        return
    if prefix:
        yield _encode_pointer(prefix), value


def _set_projection_path(target: dict[str, Any], path: str, value: Any) -> None:
    parts = _decode_pointer(path)
    current = target
    for part in parts[:-1]:
        existing = current.get(part)
        if existing is None:
            existing = {}
            current[part] = existing
        if not isinstance(existing, dict):
            raise ProjectionError(f"projection path collision at {path}")
        current = existing
    current[parts[-1]] = deepcopy(value)


def _get_existing_path(target: Mapping[str, Any], path: str) -> Any:
    current: Any = target
    for part in _decode_pointer(path):
        if not isinstance(current, Mapping) or part not in current:
            raise PatchRejected(f"patch path does not exist in canonical state: {path}")
        current = current[part]
    return current


def _set_existing_scalar_path(target: dict[str, Any], path: str, value: Any) -> None:
    parts = _decode_pointer(path)
    current: Any = target
    for part in parts[:-1]:
        if not isinstance(current, dict) or part not in current or not isinstance(current[part], dict):
            raise PatchRejected(f"patch ancestor is missing or non-object: {path}")
        current = current[part]
    if not isinstance(current, dict) or parts[-1] not in current:
        raise PatchRejected(f"patch path does not exist in canonical state: {path}")
    current[parts[-1]] = deepcopy(value)


def project(
    canonical: Mapping[str, Any],
    *,
    profile: ProjectionProfile,
    target_resolution: str,
    source_ref: str = "unbound-source",
    source_version: int = 0,
    purpose: str = "UNSPECIFIED",
    data_class: str = "INTERNAL",
    freshness: str = "CURRENT",
) -> ProjectionResult:
    """Create a deterministic, non-destructive, provenance-bound projection."""
    _validate_canonical_json(canonical)
    _validate_token(source_ref, "source_ref")
    _validate_token(purpose, "purpose")
    _validate_token(freshness, "freshness")
    if not isinstance(source_version, int) or source_version < 0:
        raise ProjectionError("source_version must be a non-negative integer")
    if data_class not in _CLASS_RANK:
        raise ProjectionError(f"invalid data_class: {data_class}")

    target_rank = resolution_rank(target_resolution)
    canonical_rank = resolution_rank(profile.canonical_resolution)
    if target_rank > canonical_rank:
        raise ProjectionError("cannot synthesize a resolution above canonical data")

    rules = profile.rule_map()
    out: dict[str, Any] = {}
    included: list[str] = []
    omitted: list[str] = []
    readonly: list[str] = []
    no_downgrade: list[str] = []

    for path, value in _leaf_paths(canonical):
        rule = rules.get(path)
        if rule is None:
            raise ProjectionError(f"no projection rule for canonical field: {path}")
        actual_type = _json_type(value)
        if rule.expected_type is not None and actual_type != rule.expected_type:
            raise ProjectionError(
                f"canonical field type mismatch at {path}: expected {rule.expected_type}, got {actual_type}"
            )
        if _CLASS_RANK[rule.data_class] > _CLASS_RANK[data_class]:
            raise ProjectionError(
                f"envelope data_class understates field classification at {path}"
            )

        if resolution_rank(rule.introduced_at) <= target_rank:
            _set_projection_path(out, path, value)
            included.append(path)
            if (
                resolution_rank(rule.write_min) > target_rank
                or rule.downgrade_policy in {"READ_ONLY_WHEN_PROJECTED", "NO_DOWNGRADE"}
            ):
                readonly.append(path)
        else:
            omitted.append(path)
            if rule.downgrade_policy == "READ_ONLY_WHEN_PROJECTED":
                readonly.append(path)
            elif rule.downgrade_policy == "NO_DOWNGRADE":
                no_downgrade.append(path)

    missing_backbone = sorted(set(profile.required_backbone_paths) - set(included))
    if missing_backbone:
        raise ProjectionError(f"projection lost required R0 backbone paths: {missing_backbone}")

    return ProjectionResult(
        profile_id=profile.profile_id,
        profile_version=profile.version,
        profile_hash=profile.profile_hash,
        canonical_hash=canonical_hash(canonical),
        canonical_resolution=profile.canonical_resolution,
        target_resolution=target_resolution,
        projection_hash=canonical_hash(out),
        source_ref=source_ref,
        source_version=source_version,
        purpose=purpose,
        data_class=data_class,
        freshness=freshness,
        value=out,
        included_paths=tuple(sorted(included)),
        omitted_paths=tuple(sorted(omitted)),
        read_only_paths=tuple(sorted(set(readonly))),
        no_downgrade_paths=tuple(sorted(set(no_downgrade))),
    )


def apply_patch(
    canonical: Mapping[str, Any],
    *,
    profile: ProjectionProfile,
    patch: ResolutionPatch,
    current_version: int,
    source_ref: str,
) -> dict[str, Any]:
    """Apply an existing scalar-leaf patch while preserving all hidden state."""
    _validate_canonical_json(canonical)
    if (
        patch.projection_profile_id != profile.profile_id
        or patch.projection_profile_version != profile.version
        or patch.projection_profile_hash != profile.profile_hash
    ):
        raise PatchRejected("projection profile identity/hash mismatch")
    if patch.source_ref != source_ref:
        raise PatchRejected("canonical source_ref mismatch")
    if patch.expected_version != current_version:
        raise PatchRejected("stale expected_version")
    if canonical_hash(canonical) != patch.expected_canonical_hash:
        raise PatchRejected("stale canonical hash")

    try:
        current_projection = project(
            canonical,
            profile=profile,
            target_resolution=patch.actor_resolution,
            source_ref=source_ref,
            source_version=current_version,
            data_class=_profile_data_class(profile),
        )
    except ProjectionError as exc:
        raise PatchRejected(f"canonical state no longer conforms to projection profile: {exc}") from exc
    if current_projection.projection_hash != patch.expected_projection_hash:
        raise PatchRejected("stale or mismatched projection hash")

    actor_rank = resolution_rank(patch.actor_resolution)
    if actor_rank > resolution_rank(profile.canonical_resolution):
        raise PatchRejected("actor resolution exceeds canonical resolution")

    rules = profile.rule_map()
    updated = deepcopy(dict(canonical))
    seen: set[str] = set()
    for operation in patch.operations:
        if operation.path in seen:
            raise PatchRejected(f"duplicate patch path: {operation.path}")
        seen.add(operation.path)
        rule = rules.get(operation.path)
        if rule is None:
            raise PatchRejected(f"field is not writable under projection profile: {operation.path}")
        if actor_rank < resolution_rank(rule.introduced_at):
            raise PatchRejected(f"field is not visible at {patch.actor_resolution}: {operation.path}")
        if actor_rank < resolution_rank(rule.write_min):
            raise PatchRejected(f"field requires {rule.write_min} to write: {operation.path}")
        if (
            rule.downgrade_policy in {"READ_ONLY_WHEN_PROJECTED", "NO_DOWNGRADE"}
            and actor_rank < resolution_rank(profile.canonical_resolution)
        ):
            raise PatchRejected(f"field is read-only/no-downgrade in projected execution: {operation.path}")

        existing = _get_existing_path(canonical, operation.path)
        if isinstance(existing, (Mapping, list)) or isinstance(operation.value, (Mapping, list)):
            raise PatchRejected(f"collection replacement is forbidden: {operation.path}")
        existing_type = _json_type(existing)
        new_type = _json_type(operation.value)
        if existing_type != new_type:
            raise PatchRejected(
                f"patch type mismatch at {operation.path}: {existing_type} -> {new_type}"
            )
        if rule.expected_type is not None and new_type != rule.expected_type:
            raise PatchRejected(f"patch violates declared type at {operation.path}")
        _set_existing_scalar_path(updated, operation.path, operation.value)

    _validate_canonical_json(updated)
    return updated


def require_action_resolution(*, effective_resolution: str, minimum_required: str) -> None:
    if resolution_rank(effective_resolution) < resolution_rank(minimum_required):
        raise ResolutionMismatch(
            f"action requires {minimum_required}, effective view is {effective_resolution}"
        )


def require_action_compatibility(
    *, profile: ProjectionProfile, action: str, projection: ProjectionResult
) -> None:
    """Bind an action to both its minimum level and its required fine wires."""
    if (
        projection.profile_id != profile.profile_id
        or projection.profile_version != profile.version
        or projection.profile_hash != profile.profile_hash
    ):
        raise ResolutionMismatch("action projection/profile mismatch")
    action_rule = profile.action_rule_map().get(action)
    if action_rule is None:
        raise ResolutionMismatch(f"action is not declared by profile: {action}")
    require_action_resolution(
        effective_resolution=projection.target_resolution,
        minimum_required=action_rule.minimum_resolution,
    )
    missing = sorted(set(action_rule.required_paths) - set(projection.included_paths))
    if missing:
        raise ResolutionMismatch(f"action-required fields are absent from projection: {missing}")


def assert_monotonic_projection(
    canonical: Mapping[str, Any], *, profile: ProjectionProfile, lower: str, higher: str
) -> None:
    """Property helper: a finer view may add fields but cannot alter coarse values."""
    if resolution_rank(lower) > resolution_rank(higher):
        raise ResolutionError("lower must not exceed higher")
    data_class = _profile_data_class(profile)
    low = project(canonical, profile=profile, target_resolution=lower, data_class=data_class)
    high = project(canonical, profile=profile, target_resolution=higher, data_class=data_class)
    reprojection = project(high.value, profile=profile, target_resolution=lower, data_class=data_class)
    if low.value != reprojection.value:
        raise ProjectionError("projection is not compositional/monotonic")
