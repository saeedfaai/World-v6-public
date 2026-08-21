from __future__ import annotations
from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True)
class NormalizedInbound:
    channel: str
    channel_actor_id: str
    principal_id: str
    text: str
    authenticated: bool
    conversation_id: str = "human-root:secretary-001"
    message_id: str = ""

    def __post_init__(self):
        if not self.message_id:
            object.__setattr__(self, "message_id", f"msg_{uuid4().hex}")


def normalize_chatgpt(actor_id: str, text: str, *, principal_id: str = "human-root",
                      conversation_id: str = "human-root:secretary-001") -> NormalizedInbound:
    return NormalizedInbound(
        channel="chatgpt",
        channel_actor_id=str(actor_id),
        principal_id=principal_id,
        text=text.strip(),
        authenticated=True,
        conversation_id=conversation_id,
    )


def normalize_telegram(actor_id: str, text: str, verified_webhook: bool, *,
                       principal_id: str = "unbound",
                       conversation_id: str = "human-root:secretary-001",
                       message_id: str | None = None) -> NormalizedInbound:
    # Transport verification is mandatory; message text itself is data, never authority.
    return NormalizedInbound(
        channel="telegram",
        channel_actor_id=str(actor_id),
        principal_id=principal_id,
        text=text.strip(),
        authenticated=bool(verified_webhook),
        conversation_id=conversation_id,
        message_id=message_id or "",
    )
