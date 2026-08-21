from __future__ import annotations

from decimal import Decimal
from pathlib import Path

from core.effects import ExternalEffectProposal, sha256_bytes
from core.resolution import ResolutionError, resolution_rank

from .letters import render_letter_pdf
from .models import (
    ConversationMessage,
    LetterRequest,
    PriceKey,
    ProformaItem,
    ProformaRequest,
    TaskRecord,
)
from .policy import classify_action
from .proforma import render_proforma_pdf
from .resolution_profile import (
    check_price_action,
    project_conversation_message,
    project_price,
    project_task,
)
from .store import InMemorySecretaryStore


class DirectExternalIOForbidden(PermissionError):
    pass


class Secretary001:
    DEFAULT_CONVERSATION_ID = "human-root:secretary-001"

    def __init__(
        self,
        store=None,
        base_dir: str | Path | None = None,
        execution_resolution: str = "R0",
    ):
        if execution_resolution is None:
            raise ResolutionError("execution_resolution is mandatory; legacy bypass is removed")
        if resolution_rank(execution_resolution) > 1:
            raise ResolutionError("secretary-001 RC1 supports only R0 and R1")
        self.store = store or InMemorySecretaryStore()
        self.base_dir = Path(base_dir or Path(__file__).resolve().parents[1])
        self.execution_resolution = execution_resolution

    def _policy(self, action: str, **kwargs):
        return classify_action(action, effective_resolution=self.execution_resolution, **kwargs)

    def ingest_message(self, inbound):
        """Persist channel-neutral conversation before any Brain is selected."""
        if not inbound.authenticated:
            raise PermissionError("unauthenticated transport cannot enter the trusted conversation spine")
        return self.store.append_conversation_message(ConversationMessage(
            principal_id=inbound.principal_id,
            conversation_id=inbound.conversation_id,
            direction="INBOUND",
            channel=inbound.channel,
            channel_actor_id=inbound.channel_actor_id,
            text=inbound.text,
            message_id=inbound.message_id,
        ))

    def record_reply(
        self,
        text: str,
        *,
        provider: str,
        channel: str,
        principal_id: str = "human-root",
        conversation_id: str = DEFAULT_CONVERSATION_ID,
    ):
        return self.store.append_conversation_message(ConversationMessage(
            principal_id=principal_id,
            conversation_id=conversation_id,
            direction="OUTBOUND",
            channel=channel,
            text=text,
            brain_provider=provider,
        ))

    def brain_context(
        self,
        *,
        principal_id: str = "human-root",
        conversation_id: str = DEFAULT_CONVERSATION_ID,
        limit: int = 50,
        resolution: str | None = None,
    ) -> list[dict]:
        """Return provider-safe envelopes, never provenance-free raw views."""
        target = resolution or self.execution_resolution
        rows = self.store.conversation_context(principal_id, conversation_id, limit)
        return [project_conversation_message(message, target).consumer_envelope() for message in rows]

    def task_view(self, task_id: str, resolution: str | None = None) -> dict:
        projection = project_task(self.store.tasks[task_id], resolution or self.execution_resolution)
        return projection.consumer_envelope()

    def price_view(
        self,
        customer_id: str,
        product_key: str,
        unit: str,
        resolution: str | None = None,
    ) -> dict | None:
        price = self.store.get_active_price(PriceKey(customer_id, product_key, unit))
        if price is None:
            return None
        return project_price(price, resolution or self.execution_resolution).consumer_envelope()

    def make_letter(self, request: LetterRequest, output_pdf: str | Path):
        decision = self._policy("RENDER_LETTER_PDF")
        if not decision.allowed:
            raise PermissionError(decision.reason)
        return render_letter_pdf(
            request,
            self.base_dir / "assets" / "letterhead_template.pptx",
            output_pdf,
        )

    def add_task(self, **kwargs):
        decision = self._policy("ADD_TASK")
        if not decision.allowed:
            raise PermissionError(decision.reason)
        return self.store.add_task(TaskRecord(**kwargs))

    def resolve_price_or_ask_root(
        self,
        customer_id: str,
        product_key: str,
        unit: str,
        quantity: Decimal,
    ) -> dict:
        price = self.store.get_active_price(PriceKey(customer_id, product_key, unit))
        if price is not None:
            projection = project_price(price, self.execution_resolution)
            if self.execution_resolution == "R1":
                check_price_action("PRICE_LOOKUP", projection)
            return {"status": "PRICE_FOUND", "projection": projection.consumer_envelope()}
        inquiry = self.store.create_price_inquiry(customer_id, product_key, unit, quantity)
        return {"status": "ASK_ROOT", "inquiry": inquiry}

    def make_proforma_from_known_price(
        self,
        *,
        customer_id: str,
        customer_name: str,
        customer_phone: str,
        product_key: str,
        description: str,
        quantity: Decimal,
        unit: str,
        document_no: str,
        document_date: str,
        output_pdf: str | Path,
    ):
        decision = self._policy("BUILD_PROFORMA_DRAFT", price_is_exact_active_match=True)
        if not decision.allowed:
            raise PermissionError(decision.reason)
        price = self.store.get_active_price(PriceKey(customer_id, product_key, unit))
        if price is None:
            inquiry = self.store.create_price_inquiry(customer_id, product_key, unit, quantity)
            return {"status": "ASK_ROOT", "inquiry": inquiry}

        projection = project_price(price, self.execution_resolution)
        check_price_action("BUILD_PROFORMA_DRAFT", projection)
        exact = projection.value
        request = ProformaRequest(
            customer_name,
            customer_phone,
            (ProformaItem(description, quantity, unit, Decimal(exact["unit_price_irr"])),),
            document_no,
            document_date,
            notes=("هزینه حمل بر عهده خریدار است مگر خلاف آن صراحتاً تأیید شود.",),
        )
        pdf = render_proforma_pdf(request, output_pdf)
        return {
            "status": "DRAFT_READY",
            "pdf": str(pdf),
            "price_projection": projection.consumer_envelope(),
        }

    def propose_pdf_delivery(
        self,
        pdf_path: str | Path,
        *,
        command_id: str,
        recipient_ref: str,
        expected_version: int,
        control_epoch: int,
        idempotency_key: str,
        policy_version: str = "1.2.0",
    ) -> ExternalEffectProposal:
        """Prepare a bound proposal; no network call and no authority are created."""
        decision = self._policy("PROPOSE_EXTERNAL_EFFECT")
        if not decision.allowed:
            raise PermissionError(decision.reason)
        path = Path(pdf_path)
        if not path.is_file() or path.suffix.lower() != ".pdf":
            raise ValueError("only an existing PDF may be proposed for delivery")
        payload_hash = sha256_bytes(path.read_bytes())
        return ExternalEffectProposal(
            world_id="world-v6",
            entity_id="secretary-001",
            command_id=command_id,
            destination="telegram",
            action="SEND_DOCUMENT",
            resource_ref=f"artifact:{path.name}",
            recipient_ref=recipient_ref,
            payload_ref=f"sha256:{payload_hash}",
            payload_hash=payload_hash,
            policy_version=policy_version,
            expected_version=expected_version,
            control_epoch=control_epoch,
            idempotency_scope="secretary-001:telegram-document",
            idempotency_key=idempotency_key,
            effect_semantics="RECONCILABLE",
        )

    def send_pdf_to_root_telegram(self, *args, **kwargs):
        raise DirectExternalIOForbidden(
            "Direct send was removed in RC1; propose the effect, bind Human Root approval, "
            "commit Command/Event/Outbox atomically, then let the registered Executor deliver it"
        )

    def send_latest_archived_letter_to_telegram(self, *args, **kwargs):
        raise DirectExternalIOForbidden(
            "Entity-local Drive/Telegram chaining is forbidden; use registered read and effect Executors"
        )
