from __future__ import annotations
from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional
from .models import TaskRecord, PriceKey, PriceRecord, OwnerInquiry, ConversationMessage, new_id


class InMemorySecretaryStore:
    """Test/dev repository. Canonical production adapter is PostgreSQL, not this class."""
    def __init__(self) -> None:
        self.tasks: dict[str, TaskRecord] = {}
        self.prices: dict[tuple[str, str, str], PriceRecord] = {}
        self.inquiries: dict[str, OwnerInquiry] = {}
        self.events: list[dict] = []
        self.conversation_messages: list[ConversationMessage] = []

    def append_conversation_message(self, msg: ConversationMessage) -> ConversationMessage:
        self.conversation_messages.append(msg)
        self.events.append({
            "type": "CONVERSATION.MESSAGE_RECORDED",
            "message_id": msg.message_id,
            "principal_id": msg.principal_id,
            "conversation_id": msg.conversation_id,
            "channel": msg.channel,
            "direction": msg.direction,
            "brain_provider": msg.brain_provider,
        })
        return msg

    def conversation_context(self, principal_id: str, conversation_id: str, limit: int = 50) -> list[ConversationMessage]:
        rows = [m for m in self.conversation_messages
                if m.principal_id == principal_id and m.conversation_id == conversation_id]
        return rows[-limit:]

    def add_task(self, task: TaskRecord) -> TaskRecord:
        self.tasks[task.task_id] = task
        self.events.append({"type": "TASK.CREATED", "task_id": task.task_id})
        return task

    def complete_task(self, task_id: str) -> TaskRecord:
        task = self.tasks[task_id]
        task.status = "DONE"
        self.events.append({"type": "TASK.COMPLETED", "task_id": task_id})
        return task

    def put_price(self, price: PriceRecord) -> None:
        key = (price.key.customer_id, price.key.product_key, price.key.unit)
        self.prices[key] = price
        self.events.append({"type": "PRICE.APPROVED", "key": key, "approved_by": price.approved_by})

    def get_active_price(self, key: PriceKey) -> Optional[PriceRecord]:
        rec = self.prices.get((key.customer_id, key.product_key, key.unit))
        if not rec or not rec.active:
            return None
        if rec.valid_until:
            try:
                expiry = datetime.fromisoformat(rec.valid_until.replace("Z", "+00:00"))
                if expiry < datetime.now(timezone.utc):
                    return None
            except ValueError:
                return None
        return rec

    def create_price_inquiry(self, customer_id: str, product_key: str, unit: str, qty: Decimal) -> OwnerInquiry:
        inquiry = OwnerInquiry(
            inquiry_id=new_id("priceq"), customer_id=customer_id, product_key=product_key,
            unit=unit, requested_quantity=qty,
            message=f"مشتری {customer_id} برای {qty} {unit} از {product_key} قیمت می‌خواهد؛ قیمت فعال/معتبر پیدا نشد. لطفاً قیمت را اعلام و تأیید کنید."
        )
        self.inquiries[inquiry.inquiry_id] = inquiry
        self.events.append({"type": "PRICE.ROOT_INQUIRY_CREATED", "inquiry_id": inquiry.inquiry_id})
        return inquiry
