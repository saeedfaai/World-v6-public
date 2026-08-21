"""Deterministic external-effect proposal and approval binding primitives.

This module performs no I/O and writes no database rows.  It prepares a value
that the canonical Kernel may insert into Command/Event/Outbox in one
PostgreSQL transaction after Policy and version/control-epoch rechecks.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import hashlib
import re
from typing import Any, Literal

from .resolution import canonical_hash


EffectSemantics = Literal["NATIVE_IDEMPOTENT", "RECONCILABLE", "NON_IDEMPOTENT"]
_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


class EffectBindingError(ValueError):
    pass


def sha256_bytes(payload: bytes) -> str:
    if not isinstance(payload, bytes) or not payload:
        raise EffectBindingError("effect payload must be non-empty bytes")
    return hashlib.sha256(payload).hexdigest()


def _require_text(value: str, label: str) -> None:
    if not isinstance(value, str) or not value.strip() or len(value) > 512:
        raise EffectBindingError(f"invalid {label}")


def _require_hash(value: str, label: str) -> None:
    if not isinstance(value, str) or not _HASH_RE.fullmatch(value):
        raise EffectBindingError(f"invalid {label}")


@dataclass(frozen=True)
class ExternalEffectProposal:
    world_id: str
    entity_id: str
    command_id: str
    destination: str
    action: str
    resource_ref: str
    recipient_ref: str
    payload_ref: str
    payload_hash: str
    policy_version: str
    expected_version: int
    control_epoch: int
    idempotency_scope: str
    idempotency_key: str
    effect_semantics: EffectSemantics = "RECONCILABLE"

    def __post_init__(self) -> None:
        for label in (
            "world_id", "entity_id", "command_id", "destination", "action",
            "resource_ref", "recipient_ref", "payload_ref", "policy_version",
            "idempotency_scope", "idempotency_key",
        ):
            _require_text(getattr(self, label), label)
        _require_hash(self.payload_hash, "payload_hash")
        if not isinstance(self.expected_version, int) or self.expected_version < 0:
            raise EffectBindingError("expected_version must be non-negative")
        if not isinstance(self.control_epoch, int) or self.control_epoch < 1:
            raise EffectBindingError("control_epoch must be positive")
        if self.effect_semantics not in {
            "NATIVE_IDEMPOTENT", "RECONCILABLE", "NON_IDEMPOTENT"
        }:
            raise EffectBindingError("invalid effect_semantics")

    def binding_document(self) -> dict[str, Any]:
        return {
            "world_id": self.world_id,
            "entity_id": self.entity_id,
            "command_id": self.command_id,
            "destination": self.destination,
            "action": self.action,
            "resource_ref": self.resource_ref,
            "recipient_ref": self.recipient_ref,
            "payload_ref": self.payload_ref,
            "payload_hash": self.payload_hash,
            "policy_version": self.policy_version,
            "expected_version": self.expected_version,
            "control_epoch": self.control_epoch,
            "idempotency_scope": self.idempotency_scope,
            "idempotency_key": self.idempotency_key,
            "effect_semantics": self.effect_semantics,
        }

    @property
    def effect_hash(self) -> str:
        return canonical_hash(self.binding_document())


@dataclass(frozen=True)
class ApprovalBinding:
    approval_ref: str
    approver_ref: str
    decision: Literal["APPROVE"]
    command_id: str
    action: str
    recipient_ref: str
    payload_hash: str
    effect_hash: str
    policy_version: str
    expected_version: int
    control_epoch: int
    issued_at: str
    expires_at: str | None = None

    def __post_init__(self) -> None:
        for label in (
            "approval_ref", "approver_ref", "command_id", "action",
            "recipient_ref", "policy_version", "issued_at",
        ):
            _require_text(getattr(self, label), label)
        if self.decision != "APPROVE":
            raise EffectBindingError("only an explicit APPROVE binding can authorize an effect")
        _require_hash(self.payload_hash, "payload_hash")
        _require_hash(self.effect_hash, "effect_hash")
        if not isinstance(self.expected_version, int) or self.expected_version < 0:
            raise EffectBindingError("expected_version must be non-negative")
        if not isinstance(self.control_epoch, int) or self.control_epoch < 1:
            raise EffectBindingError("control_epoch must be positive")


@dataclass(frozen=True)
class PreparedOutboxIntent:
    proposal: ExternalEffectProposal
    approval_ref: str
    policy_decision_ref: str
    effect_hash: str
    status: Literal["PREPARED_NOT_COMMITTED"] = "PREPARED_NOT_COMMITTED"
    authoritative: bool = False

    def to_document(self) -> dict[str, Any]:
        return {
            **self.proposal.binding_document(),
            "effect_hash": self.effect_hash,
            "approval_ref": self.approval_ref,
            "policy_decision_ref": self.policy_decision_ref,
            "status": self.status,
            "authoritative": False,
        }


def validate_approval_binding(
    proposal: ExternalEffectProposal,
    approval: ApprovalBinding,
    *,
    evaluated_at: str,
) -> None:
    if approval.approver_ref != "human-root":
        raise EffectBindingError("approval must be issued by stable human-root role")
    expected = {
        "command_id": proposal.command_id,
        "action": proposal.action,
        "recipient_ref": proposal.recipient_ref,
        "payload_hash": proposal.payload_hash,
        "effect_hash": proposal.effect_hash,
        "policy_version": proposal.policy_version,
        "expected_version": proposal.expected_version,
        "control_epoch": proposal.control_epoch,
    }
    actual = {field: getattr(approval, field) for field in expected}
    mismatches = sorted(field for field, value in expected.items() if actual[field] != value)
    if mismatches:
        raise EffectBindingError(f"approval binding mismatch: {mismatches}")
    try:
        evaluated = datetime.fromisoformat(evaluated_at.replace("Z", "+00:00"))
        issued = datetime.fromisoformat(approval.issued_at.replace("Z", "+00:00"))
        expires = (
            datetime.fromisoformat(approval.expires_at.replace("Z", "+00:00"))
            if approval.expires_at else None
        )
    except ValueError as exc:
        raise EffectBindingError("approval timestamps must be ISO-8601") from exc
    if evaluated < issued:
        raise EffectBindingError("approval is not yet valid")
    if expires is not None and evaluated >= expires:
        raise EffectBindingError("approval has expired")


def prepare_outbox_intent(
    proposal: ExternalEffectProposal,
    approval: ApprovalBinding,
    *,
    policy_decision_ref: str,
    evaluated_at: str,
) -> PreparedOutboxIntent:
    _require_text(policy_decision_ref, "policy_decision_ref")
    validate_approval_binding(proposal, approval, evaluated_at=evaluated_at)
    return PreparedOutboxIntent(
        proposal=proposal,
        approval_ref=approval.approval_ref,
        policy_decision_ref=policy_decision_ref,
        effect_hash=proposal.effect_hash,
    )
