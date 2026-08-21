from decimal import Decimal

import pytest

from core.resolution import ResolutionError
from src.channels import normalize_chatgpt
from src.models import PriceKey, PriceRecord
from src.secretary import DirectExternalIOForbidden, Secretary001


def values(envelopes):
    return [envelope["value"] for envelope in envelopes]


def test_r0_conversation_is_same_source_with_coarse_fields_and_provenance():
    secretary = Secretary001(execution_resolution="R0")
    secretary.ingest_message(normalize_chatgpt("human-root", "نامه را آماده کن"))
    secretary.record_reply("آماده شد", provider="openai", channel="chatgpt")
    r0 = secretary.brain_context(resolution="R0")
    r1 = secretary.brain_context(resolution="R1")
    assert [item["text"] for item in values(r0)] == [item["text"] for item in values(r1)]
    assert set(r0[0]["value"]) == {"direction", "text"}
    assert "message_id" in r1[0]["value"]
    assert r0[0]["source_ref"] == r1[0]["source_ref"]
    assert r0[0]["canonical_hash"] == r1[0]["canonical_hash"]
    assert r0[0]["projection_authoritative"] is False


def test_r0_task_keeps_backbone_and_r1_only_adds_fine_wires():
    secretary = Secretary001(execution_resolution="R0")
    task = secretary.add_task(
        title="پیگیری مشتری",
        priority="HIGH",
        due_at="2026-08-21T09:00:00+03:30",
        domain="sales",
        next_action="call",
    )
    r0 = secretary.task_view(task.task_id, "R0")
    r1 = secretary.task_view(task.task_id, "R1")
    assert r0["value"]["task_id"] == r1["value"]["task_id"] == task.task_id
    assert r0["value"]["title"] == r1["value"]["title"]
    assert "priority" not in r0["value"]
    assert r1["value"]["priority"] == "HIGH"


def test_r0_price_never_exposes_amount_or_approval_details():
    secretary = Secretary001(execution_resolution="R0")
    secretary.store.put_price(PriceRecord(PriceKey("c1", "p1", "m2"), Decimal("460000")))
    r0 = secretary.price_view("c1", "p1", "m2", "R0")
    r1 = secretary.price_view("c1", "p1", "m2", "R1")
    assert r0["data_class"] == "CONFIDENTIAL"
    assert r0["value"] == {
        "customer_id": "c1", "product_key": "p1", "unit": "m2", "active": True
    }
    assert r1["value"]["unit_price_irr"] == "460000"
    assert "approved_by" not in r0["value"]


def test_proforma_is_blocked_at_r0_even_when_price_exists():
    secretary = Secretary001(execution_resolution="R0")
    secretary.store.put_price(PriceRecord(PriceKey("c1", "p1", "m2"), Decimal("460000")))
    with pytest.raises(PermissionError, match="Resolution gate"):
        secretary.make_proforma_from_known_price(
            customer_id="c1", customer_name="x", customer_phone="1",
            product_key="p1", description="p", quantity=Decimal("1"), unit="m2",
            document_no="1", document_date="1", output_pdf="/tmp/never.pdf",
        )


def test_r1_proforma_uses_exact_profile_bound_price(tmp_path):
    secretary = Secretary001(execution_resolution="R1")
    secretary.store.put_price(PriceRecord(PriceKey("c1", "p1", "m2"), Decimal("460000")))
    output = tmp_path / "pi.pdf"
    result = secretary.make_proforma_from_known_price(
        customer_id="c1", customer_name="x", customer_phone="1",
        product_key="p1", description="p", quantity=Decimal("1"), unit="m2",
        document_no="1", document_date="1", output_pdf=output,
    )
    assert result["status"] == "DRAFT_READY"
    assert output.exists()
    assert result["price_projection"]["profile_id"] == "secretary.price"


def test_no_silent_legacy_resolution_bypass():
    with pytest.raises(ResolutionError, match="mandatory"):
        Secretary001(execution_resolution=None)


def test_external_send_method_cannot_reach_adapter_even_with_yes_boolean(tmp_path):
    secretary = Secretary001(execution_resolution="R1")
    pdf = tmp_path / "x.pdf"
    pdf.write_bytes(b"%PDF-1.7")
    with pytest.raises(DirectExternalIOForbidden, match="Outbox"):
        secretary.send_pdf_to_root_telegram(pdf, root_approved=True)


def test_r1_can_only_prepare_a_bound_non_authoritative_effect_proposal(tmp_path):
    secretary = Secretary001(execution_resolution="R1")
    pdf = tmp_path / "letter.pdf"
    pdf.write_bytes(b"%PDF-1.7 exact document")
    proposal = secretary.propose_pdf_delivery(
        pdf,
        command_id="cmd-77",
        recipient_ref="telegram-chat:123",
        expected_version=8,
        control_epoch=2,
        idempotency_key="letter-77",
    )
    assert proposal.payload_hash != proposal.effect_hash
    assert proposal.recipient_ref == "telegram-chat:123"
    assert proposal.control_epoch == 2


def test_r0_cannot_even_prepare_external_effect_proposal(tmp_path):
    secretary = Secretary001(execution_resolution="R0")
    pdf = tmp_path / "letter.pdf"
    pdf.write_bytes(b"%PDF-1.7 exact document")
    with pytest.raises(PermissionError, match="Resolution gate"):
        secretary.propose_pdf_delivery(
            pdf,
            command_id="cmd-77",
            recipient_ref="telegram-chat:123",
            expected_version=8,
            control_epoch=2,
            idempotency_key="letter-77",
        )
