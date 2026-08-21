from __future__ import annotations
from decimal import Decimal
from pathlib import Path
from .models import LetterRequest, ProformaItem, ProformaRequest, TaskRecord, PriceKey, ConversationMessage
from .store import InMemorySecretaryStore
from .policy import classify_action
from .letters import render_letter_pdf
from .proforma import render_proforma_pdf


class Secretary001:
    DEFAULT_CONVERSATION_ID = "human-root:secretary-001"

    def __init__(self, store=None, base_dir: str | Path | None = None):
        self.store = store or InMemorySecretaryStore()
        self.base_dir = Path(base_dir or Path(__file__).resolve().parents[1])

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

    def record_reply(self, text: str, *, provider: str, channel: str,
                     principal_id: str = "human-root",
                     conversation_id: str = DEFAULT_CONVERSATION_ID):
        return self.store.append_conversation_message(ConversationMessage(
            principal_id=principal_id,
            conversation_id=conversation_id,
            direction="OUTBOUND",
            channel=channel,
            text=text,
            brain_provider=provider,
        ))

    def brain_context(self, *, principal_id: str = "human-root",
                      conversation_id: str = DEFAULT_CONVERSATION_ID,
                      limit: int = 50) -> list[dict]:
        """Same context is loaded whether the next Brain is OpenAI, Google or another compatible provider."""
        return [
            {
                "direction": m.direction,
                "channel": m.channel,
                "text": m.text,
                "brain_provider": m.brain_provider,
                "created_at": m.created_at,
                "message_id": m.message_id,
            }
            for m in self.store.conversation_context(principal_id, conversation_id, limit)
        ]

    def make_letter(self, req: LetterRequest, output_pdf: str | Path):
        d = classify_action("RENDER_LETTER_PDF")
        if not d.allowed: raise PermissionError(d.reason)
        return render_letter_pdf(req, self.base_dir / "assets" / "letterhead_template.pptx", output_pdf)


    def send_pdf_to_root_telegram(self, pdf_path: str | Path, *, root_approved: bool, caption: str | None = None, config=None, opener=None):
        """Deliver an already-rendered PDF to the verified Human Root Telegram chat.

        This is an external effect. It requires explicit Human Root approval and never
        derives authority from username or document content.
        """
        d = classify_action("SEND_DOCUMENT_TO_ROOT_TELEGRAM", root_approved=root_approved)
        if not d.allowed:
            raise PermissionError(d.reason)
        from .telegram_adapter import TelegramRuntimeConfig, TelegramBotClient
        cfg = config or TelegramRuntimeConfig.from_env()
        client = TelegramBotClient(cfg, opener=opener)
        result = client.send_document(pdf_path, caption=caption)
        self.record_reply(
            f"PDF delivered to Human Root via Telegram: {Path(pdf_path).name}",
            provider="TRANSPORT", channel="telegram"
        )
        return result


    def send_latest_archived_letter_to_telegram(
        self, *, root_approved: bool, chat_id: str | None = None,
        expected_filename: str | None = None, caption: str | None = None,
        drive_client=None, telegram_config=None, telegram_opener=None,
    ):
        """Fetch the newest PDF from the canonical Drive letters archive and send it to Telegram.

        Safety rules:
        - explicit Human Root approval is mandatory;
        - only PDFs are accepted;
        - expected_filename, when supplied, must match exactly before any send;
        - recipient chat_id may be Root or a customer, but the send is still Root-authorized.
        """
        d = classify_action("SEND_ARCHIVED_PDF_TO_TELEGRAM", root_approved=root_approved)
        if not d.allowed:
            raise PermissionError(d.reason)

        from .drive_archive import DriveArchiveClient, DriveArchiveConfig
        from .telegram_adapter import TelegramRuntimeConfig, TelegramBotClient

        archive = drive_client or DriveArchiveClient(DriveArchiveConfig.from_env())
        document = archive.latest_pdf()
        if expected_filename is not None and document.name != expected_filename:
            raise RuntimeError(
                f"Latest archived letter mismatch: expected={expected_filename!r}, actual={document.name!r}"
            )
        if document.mime_type != "application/pdf" and not document.name.lower().endswith(".pdf"):
            raise RuntimeError(f"Latest archive object is not a PDF: {document.name}")

        payload = archive.download_bytes(document)
        cfg = telegram_config or TelegramRuntimeConfig.from_env()
        client = TelegramBotClient(cfg, opener=telegram_opener)
        result = client.send_document_bytes(
            payload, filename=document.name, caption=(caption or document.name), chat_id=chat_id,
            mime_type="application/pdf",
        )
        self.record_reply(
            f"Archived PDF delivered via Telegram: {document.name} (drive:{document.file_id})",
            provider="TRANSPORT", channel="telegram"
        )
        return {
            "status": "SENT",
            "drive_file_id": document.file_id,
            "filename": document.name,
            "telegram": result,
        }

    def add_task(self, **kwargs):
        d = classify_action("ADD_TASK")
        if not d.allowed: raise PermissionError(d.reason)
        return self.store.add_task(TaskRecord(**kwargs))

    def resolve_price_or_ask_root(self, customer_id: str, product_key: str, unit: str, quantity: Decimal):
        key = PriceKey(customer_id, product_key, unit)
        price = self.store.get_active_price(key)
        if price:
            return {"status": "PRICE_FOUND", "unit_price_irr": price.unit_price_irr, "approved_by": price.approved_by}
        inquiry = self.store.create_price_inquiry(customer_id, product_key, unit, quantity)
        return {"status": "ASK_ROOT", "inquiry": inquiry}

    def make_proforma_from_known_price(self, *, customer_id: str, customer_name: str, customer_phone: str,
                                      product_key: str, description: str, quantity: Decimal, unit: str,
                                      document_no: str, document_date: str, output_pdf: str | Path):
        found = self.resolve_price_or_ask_root(customer_id, product_key, unit, quantity)
        if found["status"] != "PRICE_FOUND":
            return found
        d = classify_action("BUILD_PROFORMA_DRAFT", price_is_exact_active_match=True)
        if not d.allowed: raise PermissionError(d.reason)
        req = ProformaRequest(customer_name, customer_phone,
            (ProformaItem(description, quantity, unit, found["unit_price_irr"]),), document_no, document_date,
            notes=("هزینه حمل بر عهده خریدار است مگر خلاف آن صراحتاً تأیید شود.",))
        pdf = render_proforma_pdf(req, output_pdf)
        return {"status": "DRAFT_READY", "pdf": str(pdf)}
