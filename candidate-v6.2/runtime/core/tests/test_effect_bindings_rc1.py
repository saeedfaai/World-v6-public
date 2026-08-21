import pytest

from core.effects import (
    ApprovalBinding,
    EffectBindingError,
    ExternalEffectProposal,
    prepare_outbox_intent,
    sha256_bytes,
)


def proposal():
    return ExternalEffectProposal(
        world_id="world-v6",
        entity_id="secretary-001",
        command_id="cmd-1",
        destination="telegram",
        action="SEND_DOCUMENT",
        resource_ref="artifact:letter.pdf",
        recipient_ref="telegram-chat:123",
        payload_ref="blob:abc",
        payload_hash=sha256_bytes(b"%PDF-1.7 exact bytes"),
        policy_version="1.2.0",
        expected_version=9,
        control_epoch=4,
        idempotency_scope="secretary:telegram",
        idempotency_key="letter-1-to-123",
    )


def approval(effect=None, **overrides):
    effect = effect or proposal()
    values = {
        "approval_ref": "approval-1",
        "approver_ref": "human-root",
        "decision": "APPROVE",
        "command_id": effect.command_id,
        "action": effect.action,
        "recipient_ref": effect.recipient_ref,
        "payload_hash": effect.payload_hash,
        "effect_hash": effect.effect_hash,
        "policy_version": effect.policy_version,
        "expected_version": effect.expected_version,
        "control_epoch": effect.control_epoch,
        "issued_at": "2026-08-20T10:00:00+00:00",
        "expires_at": "2026-08-20T11:00:00+00:00",
    }
    values.update(overrides)
    return ApprovalBinding(**values)


def test_exact_human_root_binding_prepares_non_authoritative_outbox_value():
    effect = proposal()
    prepared = prepare_outbox_intent(
        effect,
        approval(effect),
        policy_decision_ref="policy-decision-1",
        evaluated_at="2026-08-20T10:30:00+00:00",
    )
    assert prepared.effect_hash == effect.effect_hash
    assert prepared.status == "PREPARED_NOT_COMMITTED"
    assert prepared.authoritative is False
    assert prepared.to_document()["recipient_ref"] == "telegram-chat:123"


@pytest.mark.parametrize(
    "override",
    [
        {"approver_ref": "brain"},
        {"recipient_ref": "telegram-chat:999"},
        {"payload_hash": "0" * 64},
        {"effect_hash": "0" * 64},
        {"expected_version": 8},
        {"control_epoch": 3},
    ],
)
def test_approval_is_not_a_reusable_yes_token(override):
    effect = proposal()
    with pytest.raises(EffectBindingError):
        prepare_outbox_intent(
            effect,
            approval(effect, **override),
            policy_decision_ref="policy-decision-1",
            evaluated_at="2026-08-20T10:30:00+00:00",
        )


def test_expired_approval_fails_closed():
    effect = proposal()
    with pytest.raises(EffectBindingError, match="expired"):
        prepare_outbox_intent(
            effect,
            approval(effect),
            policy_decision_ref="policy-decision-1",
            evaluated_at="2026-08-20T12:00:00+00:00",
        )
