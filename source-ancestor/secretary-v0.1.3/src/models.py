from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional, Literal
import hashlib, json, uuid


def utcnow_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex}"


def canonical_hash(payload: object) -> str:
    raw = json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"), default=str)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class ConversationMessage:
    principal_id: str
    conversation_id: str
    direction: Literal["INBOUND", "OUTBOUND"]
    channel: str
    text: str
    channel_actor_id: Optional[str] = None
    brain_provider: Optional[str] = None
    message_id: str = field(default_factory=lambda: new_id("msg"))
    created_at: str = field(default_factory=utcnow_iso)


@dataclass(frozen=True)
class LetterRequest:
    recipient: str
    subject: str
    body: str
    document_no: str
    document_date: str
    signatory: str = "فرخی - مدیرعامل"
    company: str = "شرکت فلات پارس"


@dataclass(frozen=True)
class ProformaItem:
    description: str
    quantity: Decimal
    unit: str
    unit_price_irr: Decimal

    @property
    def total_irr(self) -> Decimal:
        return self.quantity * self.unit_price_irr


@dataclass(frozen=True)
class ProformaRequest:
    customer_name: str
    customer_phone: str
    items: tuple[ProformaItem, ...]
    document_no: str
    document_date: str
    validity_hours: int = 24
    tax_rate: Decimal = Decimal("0")
    notes: tuple[str, ...] = ()


@dataclass
class TaskRecord:
    title: str
    due_at: Optional[str] = None
    priority: Literal["LOW", "NORMAL", "HIGH", "URGENT"] = "NORMAL"
    domain: str = "general"
    goal_id: Optional[str] = None
    next_action: Optional[str] = None
    task_id: str = field(default_factory=lambda: new_id("task"))
    status: Literal["OPEN", "DONE", "CANCELLED"] = "OPEN"
    created_at: str = field(default_factory=utcnow_iso)


@dataclass(frozen=True)
class PriceKey:
    customer_id: str
    product_key: str
    unit: str


@dataclass
class PriceRecord:
    key: PriceKey
    unit_price_irr: Decimal
    valid_until: Optional[str] = None
    approved_by: str = "human-root"
    approved_at: str = field(default_factory=utcnow_iso)
    active: bool = True


@dataclass(frozen=True)
class OwnerInquiry:
    inquiry_id: str
    customer_id: str
    product_key: str
    unit: str
    requested_quantity: Decimal
    message: str
