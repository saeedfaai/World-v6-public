"""Fractal, fail-closed execution primitives for World v6.2 RC2.

The runtime keeps complexity local to a node.  A node starts coarse and only
expands when a handler explicitly asks for more detail.  Handlers can be code,
manual host sessions, local models, remote brains, or councils, but every
result remains a non-authoritative proposal.

This module performs no network I/O and executes no external effect.
"""
from __future__ import annotations

from dataclasses import dataclass, field, replace
from enum import Enum
import re
from typing import Any, Mapping, Protocol, Sequence

from .resolution import canonical_hash, canonical_json, resolution_rank


class FractalContractError(ValueError):
    """A versioned fractal execution contract is invalid."""


class FractalExecutionError(RuntimeError):
    """No safe execution path could satisfy the capsule."""


class HandlerStatus(str, Enum):
    SUCCESS = "SUCCESS"
    NEEDS_DETAIL = "NEEDS_DETAIL"
    ABSTAIN = "ABSTAIN"
    FAILED = "FAILED"


class OutcomeStatus(str, Enum):
    PROPOSED = "PROPOSED"
    EXPANDED = "EXPANDED"
    DEFERRED = "DEFERRED"


_LEVEL_BOUNDS: dict[str, tuple[int, int]] = {
    "X": (0, 9),   # execution granularity
    "B": (0, 4),   # B5 (World ownership) is constitutionally forbidden
    "D": (0, 5),   # deliberation depth
    "C": (0, 6),   # compilation maturity
    "A": (0, 5),   # authority remains independently policy-gated
    "E": (0, 5),   # evidence ladder
    "M": (0, 9),   # model capability class; profile-specific semantics
}


def _level_rank(value: str, prefix: str) -> int:
    if not isinstance(value, str) or re.fullmatch(fr"{prefix}(0|[1-9][0-9]*)", value) is None:
        raise FractalContractError(f"{prefix} level must look like {prefix}0")
    rank = int(value[1:])
    lower, upper = _LEVEL_BOUNDS[prefix]
    if rank < lower or rank > upper:
        raise FractalContractError(f"{prefix} level outside supported bounds: {value}")
    return rank


def _token(value: str, label: str) -> None:
    if not isinstance(value, str) or not value or len(value) > 160:
        raise FractalContractError(f"{label} must be a non-empty bounded string")
    if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:/@#-]*", value) is None:
        raise FractalContractError(f"{label} contains forbidden characters")


@dataclass(frozen=True)
class ExecutionVector:
    """Orthogonal execution axes; never collapse these into one global level."""

    resolutions: tuple[tuple[str, str], ...]
    granularity: str = "X0"
    brain_delegation: str = "B0"
    deliberation: str = "D0"
    compilation: str = "C0"
    authority: str = "A0"
    evidence: str = "E0"
    model_capability: str = "M0"

    def __post_init__(self) -> None:
        if not self.resolutions:
            raise FractalContractError("ExecutionVector requires at least one Resolution domain")
        domain_names = [name for name, _ in self.resolutions]
        if len(domain_names) != len(set(domain_names)):
            raise FractalContractError("duplicate Resolution domain")
        for domain, level in self.resolutions:
            _token(domain, "Resolution domain")
            resolution_rank(level)
        _level_rank(self.granularity, "X")
        _level_rank(self.brain_delegation, "B")
        _level_rank(self.deliberation, "D")
        _level_rank(self.compilation, "C")
        _level_rank(self.authority, "A")
        _level_rank(self.evidence, "E")
        _level_rank(self.model_capability, "M")

    def to_document(self) -> dict[str, Any]:
        return {
            "resolutions": {key: value for key, value in sorted(self.resolutions)},
            "granularity": self.granularity,
            "brain_delegation": self.brain_delegation,
            "deliberation": self.deliberation,
            "compilation": self.compilation,
            "authority": self.authority,
            "evidence": self.evidence,
            "model_capability": self.model_capability,
        }


@dataclass(frozen=True)
class ExecutionBudget:
    """Hard budgets keep recursive refinement bounded and predictable."""

    max_input_tokens: int = 4_000
    max_cost_micros: int = 0
    max_latency_ms: int = 30_000
    max_depth: int = 3
    max_attempts: int = 4
    max_council_rounds: int = 2

    def __post_init__(self) -> None:
        values = (
            self.max_input_tokens,
            self.max_cost_micros,
            self.max_latency_ms,
            self.max_depth,
            self.max_attempts,
            self.max_council_rounds,
        )
        if any(not isinstance(value, int) or value < 0 for value in values):
            raise FractalContractError("execution budgets must be non-negative integers")
        if self.max_attempts == 0:
            raise FractalContractError("max_attempts cannot be zero")
        if self.max_depth > 12:
            raise FractalContractError("max_depth exceeds the bounded fractal limit")

    def to_document(self) -> dict[str, int]:
        return {
            "max_input_tokens": self.max_input_tokens,
            "max_cost_micros": self.max_cost_micros,
            "max_latency_ms": self.max_latency_ms,
            "max_depth": self.max_depth,
            "max_attempts": self.max_attempts,
            "max_council_rounds": self.max_council_rounds,
        }


@dataclass(frozen=True)
class FractalNode:
    node_id: str
    version: str
    purpose: str
    input_contract_ref: str
    output_contract_ref: str
    handler_ids: tuple[str, ...]
    fallback_handler_ids: tuple[str, ...] = ()
    parent_id: str | None = None
    child_ids: tuple[str, ...] = ()
    expandable: bool = False
    risk_class: str = "LOW"
    minimum_vector: ExecutionVector = field(
        default_factory=lambda: ExecutionVector((("task", "R0"),))
    )

    def __post_init__(self) -> None:
        _token(self.node_id, "node_id")
        _token(self.version, "node version")
        _token(self.input_contract_ref, "input contract ref")
        _token(self.output_contract_ref, "output contract ref")
        if not isinstance(self.purpose, str) or not self.purpose or len(self.purpose) > 1_000:
            raise FractalContractError("node purpose must be a bounded non-empty string")
        if self.parent_id is not None:
            _token(self.parent_id, "parent_id")
        if self.risk_class not in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
            raise FractalContractError("invalid node risk_class")
        ordered = self.handler_ids + self.fallback_handler_ids
        if not ordered:
            raise FractalContractError("node requires at least one handler")
        if len(ordered) != len(set(ordered)):
            raise FractalContractError("handler and fallback chains must be unique")
        if len(self.child_ids) != len(set(self.child_ids)):
            raise FractalContractError("duplicate child node")
        if self.child_ids and not self.expandable:
            raise FractalContractError("node with children must be expandable")
        for identifier in ordered + self.child_ids:
            _token(identifier, "node reference")

    def to_document(self) -> dict[str, Any]:
        return {
            "node_id": self.node_id,
            "version": self.version,
            "purpose": self.purpose,
            "input_contract_ref": self.input_contract_ref,
            "output_contract_ref": self.output_contract_ref,
            "handler_ids": list(self.handler_ids),
            "fallback_handler_ids": list(self.fallback_handler_ids),
            "parent_id": self.parent_id,
            "child_ids": list(self.child_ids),
            "expandable": self.expandable,
            "risk_class": self.risk_class,
            "minimum_vector": self.minimum_vector.to_document(),
        }

    @property
    def node_hash(self) -> str:
        return canonical_hash(self.to_document())


@dataclass(frozen=True)
class ExecutionCapsule:
    capsule_id: str
    world_id: str
    entity_id: str
    principal_id: str
    conversation_id: str
    node_id: str
    node_version: str
    node_hash: str
    canonical_input_hash: str
    state_refs: tuple[str, ...]
    vector: ExecutionVector
    budget: ExecutionBudget
    purpose: str
    expected_version: int
    data_class: str = "INTERNAL"
    freshness: str = "CURRENT"
    parent_capsule_id: str | None = None

    def __post_init__(self) -> None:
        for value, label in (
            (self.capsule_id, "capsule_id"),
            (self.world_id, "world_id"),
            (self.entity_id, "entity_id"),
            (self.principal_id, "principal_id"),
            (self.conversation_id, "conversation_id"),
            (self.node_id, "node_id"),
            (self.node_version, "node_version"),
        ):
            _token(value, label)
        if self.parent_capsule_id is not None:
            _token(self.parent_capsule_id, "parent_capsule_id")
        for digest, label in (
            (self.node_hash, "node_hash"),
            (self.canonical_input_hash, "canonical_input_hash"),
        ):
            if re.fullmatch(r"[0-9a-f]{64}", digest) is None:
                raise FractalContractError(f"{label} must be a lowercase SHA-256")
        if not isinstance(self.expected_version, int) or self.expected_version < 0:
            raise FractalContractError("expected_version must be a non-negative integer")
        if self.data_class not in {"PUBLIC", "INTERNAL", "RESTRICTED", "SECRET"}:
            raise FractalContractError("invalid data_class")
        if self.freshness not in {"CURRENT", "STALE", "UNKNOWN"}:
            raise FractalContractError("invalid freshness")
        for ref in self.state_refs:
            _token(ref, "state_ref")

    def to_document(self) -> dict[str, Any]:
        return {
            "capsule_id": self.capsule_id,
            "world_id": self.world_id,
            "entity_id": self.entity_id,
            "principal_id": self.principal_id,
            "conversation_id": self.conversation_id,
            "node_id": self.node_id,
            "node_version": self.node_version,
            "node_hash": self.node_hash,
            "canonical_input_hash": self.canonical_input_hash,
            "state_refs": list(self.state_refs),
            "vector": self.vector.to_document(),
            "budget": self.budget.to_document(),
            "purpose": self.purpose,
            "expected_version": self.expected_version,
            "data_class": self.data_class,
            "freshness": self.freshness,
            "parent_capsule_id": self.parent_capsule_id,
        }

    @property
    def capsule_hash(self) -> str:
        return canonical_hash(self.to_document())


@dataclass(frozen=True)
class HandlerProfile:
    handler_id: str
    version: str
    kind: str
    maturity: str
    evidence: str
    supported_node_ids: tuple[str, ...]
    deterministic: bool
    network_required: bool = False
    api_token_required: bool = False
    proposal_only: bool = True
    provider_family: str = "NONE"

    def __post_init__(self) -> None:
        _token(self.handler_id, "handler_id")
        _token(self.version, "handler version")
        _token(self.provider_family, "provider_family")
        if self.kind not in {"CODE", "BRAIN", "MANUAL_HOST", "LOCAL_MODEL", "COUNCIL"}:
            raise FractalContractError("invalid handler kind")
        _level_rank(self.maturity, "C")
        _level_rank(self.evidence, "E")
        if not self.supported_node_ids:
            raise FractalContractError("handler must support at least one node")
        for node_id in self.supported_node_ids:
            _token(node_id, "supported node_id")
        if not self.proposal_only:
            raise FractalContractError("Phase 0/RC2 handlers must be proposal-only")

    def to_document(self) -> dict[str, Any]:
        return {
            "handler_id": self.handler_id,
            "version": self.version,
            "kind": self.kind,
            "maturity": self.maturity,
            "evidence": self.evidence,
            "supported_node_ids": list(self.supported_node_ids),
            "deterministic": self.deterministic,
            "network_required": self.network_required,
            "api_token_required": self.api_token_required,
            "proposal_only": self.proposal_only,
            "provider_family": self.provider_family,
        }

    @property
    def profile_hash(self) -> str:
        return canonical_hash(self.to_document())


@dataclass(frozen=True)
class HandlerResult:
    handler_id: str
    handler_version: str
    status: HandlerStatus
    output: dict[str, Any]
    confidence_millis: int = 0
    trace_summary: str = ""
    proposal_only: bool = True

    def __post_init__(self) -> None:
        _token(self.handler_id, "result handler_id")
        _token(self.handler_version, "result handler_version")
        if not isinstance(self.status, HandlerStatus):
            raise FractalContractError("handler status must be a HandlerStatus")
        if not isinstance(self.output, dict):
            raise FractalContractError("handler output must be a JSON object")
        if not 0 <= self.confidence_millis <= 1000:
            raise FractalContractError("confidence_millis outside 0..1000")
        if not self.proposal_only:
            raise FractalContractError("handler attempted an authoritative result")

    @property
    def output_hash(self) -> str:
        return canonical_hash(self.output)


class FractalHandler(Protocol):
    profile: HandlerProfile

    def invoke(self, capsule: ExecutionCapsule, payload: Mapping[str, Any]) -> HandlerResult: ...


@dataclass(frozen=True)
class AttemptRecord:
    node_id: str
    handler_id: str
    handler_version: str
    status: str
    input_hash: str
    output_hash: str | None
    reason: str


@dataclass(frozen=True)
class ExecutionOutcome:
    status: OutcomeStatus
    capsule: ExecutionCapsule
    result: HandlerResult | None
    attempts: tuple[AttemptRecord, ...]
    child_outcomes: tuple["ExecutionOutcome", ...] = ()

    @property
    def proposal(self) -> dict[str, Any] | None:
        return None if self.result is None else self.result.output


class HandlerRegistry:
    def __init__(self, handlers: Sequence[FractalHandler] = ()) -> None:
        self._handlers: dict[str, FractalHandler] = {}
        for handler in handlers:
            self.register(handler)

    def register(self, handler: FractalHandler) -> None:
        identifier = handler.profile.handler_id
        if identifier in self._handlers:
            raise FractalContractError(f"duplicate handler_id: {identifier}")
        self._handlers[identifier] = handler

    def get(self, handler_id: str) -> FractalHandler:
        try:
            return self._handlers[handler_id]
        except KeyError as exc:
            raise FractalContractError(f"unregistered handler: {handler_id}") from exc

    def profile_documents(self) -> tuple[dict[str, Any], ...]:
        return tuple(
            self._handlers[key].profile.to_document() for key in sorted(self._handlers)
        )


class FractalOrchestrator:
    """Minimal-cost, bounded-depth coordinator with no external-effect authority."""

    def __init__(
        self,
        nodes: Sequence[FractalNode],
        registry: HandlerRegistry,
        *,
        allow_network: bool = False,
        allow_api_tokens: bool = False,
    ) -> None:
        self.nodes: dict[str, FractalNode] = {}
        for node in nodes:
            if node.node_id in self.nodes:
                raise FractalContractError(f"duplicate node_id: {node.node_id}")
            self.nodes[node.node_id] = node
        self.registry = registry
        self.allow_network = allow_network
        self.allow_api_tokens = allow_api_tokens
        self._validate_tree()

    def _validate_tree(self) -> None:
        for node in self.nodes.values():
            for child_id in node.child_ids:
                child = self.nodes.get(child_id)
                if child is None:
                    raise FractalContractError(f"missing child node: {child_id}")
                if child.parent_id != node.node_id:
                    raise FractalContractError("child parent binding mismatch")
            for handler_id in node.handler_ids + node.fallback_handler_ids:
                handler = self.registry.get(handler_id)
                if node.node_id not in handler.profile.supported_node_ids:
                    raise FractalContractError(
                        f"handler {handler_id} does not declare node {node.node_id}"
                    )

        # A fractal graph is a bounded tree/DAG, never a recursive call loop.
        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(node_id: str) -> None:
            if node_id in visiting:
                raise FractalContractError(f"cycle detected at node: {node_id}")
            if node_id in visited:
                return
            visiting.add(node_id)
            for child_id in self.nodes[node_id].child_ids:
                visit(child_id)
            visiting.remove(node_id)
            visited.add(node_id)

        for node_id in sorted(self.nodes):
            visit(node_id)

    @staticmethod
    def build_capsule(
        node: FractalNode,
        payload: Mapping[str, Any],
        *,
        capsule_id: str,
        vector: ExecutionVector,
        budget: ExecutionBudget | None = None,
        world_id: str = "world-v6",
        entity_id: str = "secretary-001",
        principal_id: str = "human-root",
        conversation_id: str = "human-root:secretary-001",
        state_refs: tuple[str, ...] = (),
        expected_version: int = 0,
        purpose: str | None = None,
        data_class: str = "INTERNAL",
        freshness: str = "CURRENT",
    ) -> ExecutionCapsule:
        return ExecutionCapsule(
            capsule_id=capsule_id,
            world_id=world_id,
            entity_id=entity_id,
            principal_id=principal_id,
            conversation_id=conversation_id,
            node_id=node.node_id,
            node_version=node.version,
            node_hash=node.node_hash,
            canonical_input_hash=canonical_hash(dict(payload)),
            state_refs=state_refs,
            vector=vector,
            budget=budget or ExecutionBudget(),
            purpose=purpose or node.purpose,
            expected_version=expected_version,
            data_class=data_class,
            freshness=freshness,
        )

    @staticmethod
    def _validate_capsule(node: FractalNode, capsule: ExecutionCapsule, payload: Mapping[str, Any]) -> None:
        if (capsule.node_id, capsule.node_version, capsule.node_hash) != (
            node.node_id,
            node.version,
            node.node_hash,
        ):
            raise FractalExecutionError("capsule is not bound to the selected node version/hash")
        if capsule.canonical_input_hash != canonical_hash(dict(payload)):
            raise FractalExecutionError("capsule input hash mismatch")
        # This is deliberately a conservative byte ceiling.  Provider-specific
        # tokenizers may reject an input earlier, but may never raise this cap.
        if len(canonical_json(dict(payload)).encode("utf-8")) > capsule.budget.max_input_tokens * 8:
            raise FractalExecutionError("capsule input exceeds bounded token approximation")
        requested = dict(capsule.vector.resolutions)
        required = dict(node.minimum_vector.resolutions)
        for domain, minimum in required.items():
            actual = requested.get(domain)
            if actual is None or resolution_rank(actual) < resolution_rank(minimum):
                raise FractalExecutionError(
                    f"capsule Resolution below node minimum for domain {domain}"
                )
        for prefix, actual, minimum in (
            ("X", capsule.vector.granularity, node.minimum_vector.granularity),
            ("B", capsule.vector.brain_delegation, node.minimum_vector.brain_delegation),
            ("D", capsule.vector.deliberation, node.minimum_vector.deliberation),
            ("C", capsule.vector.compilation, node.minimum_vector.compilation),
            ("A", capsule.vector.authority, node.minimum_vector.authority),
            ("E", capsule.vector.evidence, node.minimum_vector.evidence),
            ("M", capsule.vector.model_capability, node.minimum_vector.model_capability),
        ):
            if _level_rank(actual, prefix) < _level_rank(minimum, prefix):
                raise FractalExecutionError(f"capsule {prefix} below node minimum")

    def execute(
        self, node_id: str, capsule: ExecutionCapsule, payload: Mapping[str, Any]
    ) -> ExecutionOutcome:
        node = self.nodes.get(node_id)
        if node is None:
            raise FractalExecutionError(f"unknown node: {node_id}")
        return self._execute(node, capsule, payload, depth=0, consumed_attempts=0)

    def _execute(
        self,
        node: FractalNode,
        capsule: ExecutionCapsule,
        payload: Mapping[str, Any],
        *,
        depth: int,
        consumed_attempts: int,
    ) -> ExecutionOutcome:
        self._validate_capsule(node, capsule, payload)
        attempts: list[AttemptRecord] = []
        wants_detail = False
        ordered_handlers = node.handler_ids + node.fallback_handler_ids

        for offset, handler_id in enumerate(ordered_handlers, start=1):
            if consumed_attempts + offset > capsule.budget.max_attempts:
                break
            handler = self.registry.get(handler_id)
            profile = handler.profile
            if _level_rank(profile.maturity, "C") < _level_rank(
                capsule.vector.compilation, "C"
            ):
                attempts.append(
                    AttemptRecord(
                        node.node_id,
                        profile.handler_id,
                        profile.version,
                        "SKIPPED",
                        capsule.canonical_input_hash,
                        None,
                        "MATURITY_BELOW_NODE_MINIMUM",
                    )
                )
                continue
            if _level_rank(profile.evidence, "E") < _level_rank(
                capsule.vector.evidence, "E"
            ):
                attempts.append(
                    AttemptRecord(
                        node.node_id,
                        profile.handler_id,
                        profile.version,
                        "SKIPPED",
                        capsule.canonical_input_hash,
                        None,
                        "EVIDENCE_BELOW_NODE_MINIMUM",
                    )
                )
                continue
            delegation_rank = _level_rank(capsule.vector.brain_delegation, "B")
            deliberation_rank = _level_rank(capsule.vector.deliberation, "D")
            if profile.kind != "CODE" and delegation_rank == 0:
                attempts.append(
                    AttemptRecord(
                        node.node_id,
                        profile.handler_id,
                        profile.version,
                        "SKIPPED",
                        capsule.canonical_input_hash,
                        None,
                        "BRAIN_DELEGATION_DISABLED",
                    )
                )
                continue
            if profile.kind == "COUNCIL" and (delegation_rank < 3 or deliberation_rank < 3):
                attempts.append(
                    AttemptRecord(
                        node.node_id,
                        profile.handler_id,
                        profile.version,
                        "SKIPPED",
                        capsule.canonical_input_hash,
                        None,
                        "COUNCIL_LEVEL_REQUIRES_B3_D3",
                    )
                )
                continue
            if profile.network_required and not self.allow_network:
                attempts.append(
                    AttemptRecord(
                        node.node_id,
                        profile.handler_id,
                        profile.version,
                        "SKIPPED",
                        capsule.canonical_input_hash,
                        None,
                        "NETWORK_DISABLED",
                    )
                )
                continue
            if profile.api_token_required and not self.allow_api_tokens:
                attempts.append(
                    AttemptRecord(
                        node.node_id,
                        profile.handler_id,
                        profile.version,
                        "SKIPPED",
                        capsule.canonical_input_hash,
                        None,
                        "API_TOKEN_DISABLED",
                    )
                )
                continue
            try:
                result = handler.invoke(capsule, payload)
                if result.handler_id != profile.handler_id or result.handler_version != profile.version:
                    raise FractalExecutionError("handler result identity/version mismatch")
                if not result.proposal_only:
                    raise FractalExecutionError("handler attempted an authoritative effect")
                attempts.append(
                    AttemptRecord(
                        node.node_id,
                        profile.handler_id,
                        profile.version,
                        result.status.value,
                        capsule.canonical_input_hash,
                        result.output_hash,
                        result.trace_summary,
                    )
                )
                if result.status is HandlerStatus.SUCCESS:
                    return ExecutionOutcome(
                        OutcomeStatus.PROPOSED, capsule, result, tuple(attempts)
                    )
                if result.status is HandlerStatus.NEEDS_DETAIL:
                    wants_detail = True
            except Exception as exc:  # failover records type only, never secret payload
                attempts.append(
                    AttemptRecord(
                        node.node_id,
                        profile.handler_id,
                        profile.version,
                        "FAILED",
                        capsule.canonical_input_hash,
                        None,
                        type(exc).__name__,
                    )
                )

        can_expand = (
            wants_detail
            and node.expandable
            and node.child_ids
            and depth < capsule.budget.max_depth
        )
        if can_expand:
            child_outcomes: list[ExecutionOutcome] = []
            for index, child_id in enumerate(node.child_ids):
                child = self.nodes[child_id]
                child_capsule = replace(
                    capsule,
                    capsule_id=f"{capsule.capsule_id}.x{depth + 1}.{index}",
                    node_id=child.node_id,
                    node_version=child.version,
                    node_hash=child.node_hash,
                    parent_capsule_id=capsule.capsule_id,
                    vector=replace(
                        capsule.vector,
                        granularity=f"X{min(_level_rank(capsule.vector.granularity, 'X') + 1, 9)}",
                    ),
                )
                child_outcomes.append(
                    self._execute(
                        child,
                        child_capsule,
                        payload,
                        depth=depth + 1,
                        consumed_attempts=(
                            consumed_attempts
                            + len(attempts)
                            + sum(self._attempt_count(item) for item in child_outcomes)
                        ),
                    )
                )
            if child_outcomes and all(
                outcome.status in {OutcomeStatus.PROPOSED, OutcomeStatus.EXPANDED}
                for outcome in child_outcomes
            ):
                combined = HandlerResult(
                    handler_id="world-v6.fractal-expander",
                    handler_version="0.1.0",
                    status=HandlerStatus.SUCCESS,
                    output={
                        "proposal_type": "FRACTAL_COMPOSITE",
                        "children": {
                            outcome.capsule.node_id: outcome.proposal
                            for outcome in child_outcomes
                        },
                    },
                    trace_summary="BOUNDED_CHILD_COMPOSITION",
                )
                return ExecutionOutcome(
                    OutcomeStatus.EXPANDED,
                    capsule,
                    combined,
                    tuple(attempts),
                    tuple(child_outcomes),
                )

        return ExecutionOutcome(OutcomeStatus.DEFERRED, capsule, None, tuple(attempts))

    @staticmethod
    def _attempt_count(outcome: ExecutionOutcome) -> int:
        return len(outcome.attempts) + sum(
            FractalOrchestrator._attempt_count(child) for child in outcome.child_outcomes
        )
