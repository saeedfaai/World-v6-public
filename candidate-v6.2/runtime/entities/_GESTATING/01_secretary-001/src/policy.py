from __future__ import annotations

from dataclasses import dataclass

from core.resolution import ResolutionMismatch
from .resolution_profile import check_action_resolution


@dataclass(frozen=True)
class Decision:
    allowed: bool
    reason: str
    approval_required: bool = False


def classify_action(
    action: str,
    *,
    effective_resolution: str,
    price_is_exact_active_match: bool = False,
) -> Decision:
    """Secretary-local classification inside the canonical Policy path.

    There is no legacy bypass: every runtime binding carries an explicit
    Resolution.  This function may permit preparation of an effect proposal,
    but Entity code never receives permission to perform external I/O.
    """
    try:
        check_action_resolution(action, effective_resolution)
    except ResolutionMismatch as exc:
        return Decision(False, f"Resolution gate: {exc}")

    if action in {"DRAFT_LETTER", "RENDER_LETTER_PDF", "ADD_TASK", "LIST_TASKS"}:
        return Decision(True, "L0 internal action")
    if action == "PRICE_LOOKUP":
        return Decision(True, "Read-only price lookup; field dependencies still apply")
    if action == "BUILD_PROFORMA_DRAFT":
        if price_is_exact_active_match:
            return Decision(True, "Uses exact active Human-Root-approved price")
        return Decision(False, "Missing/unapproved/changed price", approval_required=True)
    if action == "PROPOSE_EXTERNAL_EFFECT":
        return Decision(True, "May prepare a non-authoritative effect proposal only")
    if action == "EXECUTE_EXTERNAL":
        return Decision(
            False,
            "Entity-direct external I/O is forbidden; use Policy + bound approval + atomic Outbox + Executor",
            approval_required=True,
        )
    if action in {"COMMIT_PRICE", "LEGAL_FINANCIAL_COMMITMENT"}:
        return Decision(False, "Human Root approval and canonical execution path required", True)
    return Decision(False, "Unknown action: fail closed")
