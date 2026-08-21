from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Decision:
    allowed: bool
    reason: str
    approval_required: bool = False


def classify_action(action: str, *, price_is_exact_active_match: bool = False,
                    root_approved: bool = False) -> Decision:
    if action in {"DRAFT_LETTER", "RENDER_LETTER_PDF", "ADD_TASK", "LIST_TASKS"}:
        return Decision(True, "L0 internal action")
    if action == "BUILD_PROFORMA_DRAFT":
        if price_is_exact_active_match:
            return Decision(True, "Uses exact active Human-Root-approved price")
        return Decision(False, "Missing/unapproved/changed price", approval_required=True)
    if action in {"SEND_DOCUMENT_TO_ROOT_TELEGRAM", "SEND_ARCHIVED_PDF_TO_TELEGRAM"}:
        if root_approved:
            return Decision(True, "Explicit Human Root request/approval to deliver the exact PDF to Telegram")
        return Decision(False, "Human Root approval required", approval_required=True)
    if action in {"SEND_EXTERNAL", "COMMIT_PRICE", "LEGAL_FINANCIAL_COMMITMENT"}:
        return Decision(False, "Human Root approval required", approval_required=True)
    return Decision(False, "Unknown action: fail closed")
