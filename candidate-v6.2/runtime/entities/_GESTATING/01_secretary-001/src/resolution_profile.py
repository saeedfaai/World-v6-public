"""Secretary-001 bindings to the single versioned Resolution Profile artifacts."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from core.resolution import (
    ProjectionResult,
    load_profile_file,
    project,
    require_action_compatibility,
    require_action_resolution,
)


_PROFILE_DIR = Path(__file__).resolve().parents[5] / "profiles"

CONVERSATION_PROFILE = load_profile_file(
    _PROFILE_DIR / "secretary-conversation-profile.v0.2.json"
)
TASK_PROFILE = load_profile_file(_PROFILE_DIR / "secretary-task-profile.v0.2.json")
PRICE_PROFILE = load_profile_file(_PROFILE_DIR / "secretary-price-profile.v0.2.json")
EFFECT_PROFILE = load_profile_file(_PROFILE_DIR / "secretary-effect-profile.v0.2.json")


ACTION_MINIMUM_RESOLUTION: dict[str, str] = {
    "DRAFT_LETTER": "R0",
    "RENDER_LETTER_PDF": "R0",
    "ADD_TASK": "R0",
    "LIST_TASKS": "R0",
    "BUILD_PROFORMA_DRAFT": "R1",
    "PRICE_LOOKUP": "R1",
    "PROPOSE_EXTERNAL_EFFECT": "R1",
    "EXECUTE_EXTERNAL": "R1",
    "COMMIT_PRICE": "R2",
    "LEGAL_FINANCIAL_COMMITMENT": "R2",
}


def minimum_for_action(action: str) -> str:
    # Unknown actions are denied by Policy; R2 also prevents accidental coarse execution.
    return ACTION_MINIMUM_RESOLUTION.get(action, "R2")


def check_action_resolution(action: str, effective_resolution: str) -> None:
    require_action_resolution(
        effective_resolution=effective_resolution,
        minimum_required=minimum_for_action(action),
    )


def check_price_action(action: str, projection: ProjectionResult) -> None:
    require_action_compatibility(profile=PRICE_PROFILE, action=action, projection=projection)


def conversation_dict(message) -> dict[str, Any]:
    return {
        "direction": message.direction,
        "text": message.text,
        "channel": message.channel,
        "brain_provider": message.brain_provider,
        "created_at": message.created_at,
        "message_id": message.message_id,
    }


def project_conversation_message(message, target_resolution: str) -> ProjectionResult:
    return project(
        conversation_dict(message),
        profile=CONVERSATION_PROFILE,
        target_resolution=target_resolution,
        source_ref=f"conversation-message:{message.message_id}",
        source_version=0,
        purpose="BRAIN_CONTEXT",
        data_class="INTERNAL",
        freshness="APPEND_ONLY",
    )


def task_dict(task) -> dict[str, Any]:
    return {
        "task_id": task.task_id,
        "title": task.title,
        "status": task.status,
        "next_action": task.next_action,
        "due_at": task.due_at,
        "priority": task.priority,
        "domain": task.domain,
        "goal_id": task.goal_id,
        "created_at": task.created_at,
    }


def project_task(task, target_resolution: str) -> ProjectionResult:
    return project(
        task_dict(task),
        profile=TASK_PROFILE,
        target_resolution=target_resolution,
        source_ref=f"task:{task.task_id}",
        source_version=0,
        purpose="TASK_VIEW",
        data_class="INTERNAL",
        freshness="CURRENT",
    )


def price_dict(price) -> dict[str, Any]:
    return {
        "customer_id": price.key.customer_id,
        "product_key": price.key.product_key,
        "unit": price.key.unit,
        "active": price.active,
        "unit_price_irr": str(price.unit_price_irr),
        "valid_until": price.valid_until,
        "approved_by": price.approved_by,
        "approved_at": price.approved_at,
    }


def project_price(price, target_resolution: str) -> ProjectionResult:
    source_ref = f"price:{price.key.customer_id}:{price.key.product_key}:{price.key.unit}"
    return project(
        price_dict(price),
        profile=PRICE_PROFILE,
        target_resolution=target_resolution,
        source_ref=source_ref,
        source_version=0,
        purpose="PRICE_DECISION",
        data_class="CONFIDENTIAL",
        freshness="VALIDITY_BOUND",
    )
