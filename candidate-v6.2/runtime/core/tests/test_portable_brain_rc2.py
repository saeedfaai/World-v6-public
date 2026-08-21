from __future__ import annotations

import json
from pathlib import Path

import pytest

from core.brain_gateway import BrainInputSegment, BrainRequest
from core.portable_brain import (
    ManualHostAdapter,
    PortableBrainError,
    PortableSecretaryRunner,
    ScriptedPortableAdapter,
    load_portable_pack,
    normalize_secretary_decision,
    render_secretary_decision,
)
from core.resolution import load_profile_file


CANDIDATE = Path(__file__).resolve().parents[3]
PACK_DIR = CANDIDATE / "brain-packs" / "secretary-001"
PROFILE_DIR = CANDIDATE / "profiles"


def profiles():
    return [load_profile_file(path) for path in sorted(PROFILE_DIR.glob("*v0.2.json"))]


def task_profile():
    return next(profile for profile in profiles() if profile.profile_id == "secretary.task")


def pack():
    return load_portable_pack(PACK_DIR / "portable-brain-pack.v1.0.0.json")


def fixture(name):
    return json.loads((PACK_DIR / "fixtures" / name).read_text(encoding="utf-8"))


def request():
    profile = task_profile()
    canonical = {
        "task_id": "task-001",
        "title": "ارسال پیش‌نویس قرارداد",
        "status": "OPEN",
        "next_action": "DRAFT",
        "due_at": None,
        "priority": "NORMAL",
        "domain": "general",
        "goal_id": None,
        "created_at": "2026-08-20T00:00:00Z",
    }
    segment = BrainInputSegment(
        segment_id="task",
        canonical=canonical,
        profile_id=profile.profile_id,
        profile_version=profile.version,
        profile_hash=profile.profile_hash,
        source_ref="task:task-001",
        source_version=0,
        desired_resolution="R0",
        minimum_resolution="R0",
        purpose="TASK_PROPOSAL",
    )
    return BrainRequest("world-v6.brain-request.v2", "secretary.task", (segment,))


def adapter(name, response):
    profile = task_profile()
    capabilities = {(profile.profile_id, profile.version, profile.profile_hash): "R1"}
    return ScriptedPortableAdapter(name, capabilities, response, task_types=("secretary.task",))


def test_chatgpt_gemini_and_grok_fixtures_render_exact_same_standard_answer():
    outputs = []
    decisions = []
    for provider, filename in (
        ("chatgpt", "chatgpt.task-proposal.json"),
        ("gemini", "gemini.task-proposal.json"),
        ("grok", "grok.task-proposal.json"),
    ):
        runner = PortableSecretaryRunner(pack(), [adapter(provider, fixture(filename))], profiles())
        result = runner.run(request())
        outputs.append(result.rendered_text)
        decisions.append(result.decision.semantic_hash)
        assert result.provider == provider
        assert dict(result.effective_resolutions) == {"task": "R0"}
    assert len(set(outputs)) == 1
    assert len(set(decisions)) == 1
    assert outputs[0] == "کار «ارسال پیش‌نویس قرارداد» به‌صورت پیشنهاد آماده شد."


def test_provider_failover_preserves_request_identity_and_projection_hash():
    profile = task_profile()
    capabilities = {(profile.profile_id, profile.version, profile.profile_hash): "R1"}

    def fail(_request):
        raise RuntimeError("offline provider unavailable")

    first = ScriptedPortableAdapter("first", capabilities, fail)
    second = adapter("code-fallback", fixture("chatgpt.task-proposal.json"))
    result = PortableSecretaryRunner(pack(), [first, second], profiles()).run(request())
    assert result.provider == "code-fallback"
    assert first.last_request is not None
    assert second.last_request.entity_id == "secretary-001"
    assert first.last_request.inputs[0].envelope["projection_hash"] == second.last_request.inputs[0].envelope["projection_hash"]


def test_offline_runner_rejects_network_or_api_token_adapter_at_construction():
    remote = adapter("remote", fixture("chatgpt.task-proposal.json"))
    remote.network_required = True
    remote.api_token_required = True
    with pytest.raises(PortableBrainError, match="network adapter disabled"):
        PortableSecretaryRunner(pack(), [remote], profiles())


def test_model_output_is_strict_proposal_only_and_fail_closed():
    raw = fixture("chatgpt.task-proposal.json")
    invalid = {**raw, "send_now": True}
    with pytest.raises(PortableBrainError, match="forbidden"):
        normalize_secretary_decision(invalid)
    invalid = {**raw, "proposed_actions": ["EXECUTE_EXTERNAL"]}
    with pytest.raises(PortableBrainError, match="forbidden proposed action"):
        normalize_secretary_decision(invalid)
    invalid = {
        **raw,
        "proposed_actions": ["PROPOSE_EXTERNAL_EFFECT"],
        "requires_approval": False,
    }
    with pytest.raises(PortableBrainError, match="must require approval"):
        normalize_secretary_decision(invalid)
    with pytest.raises(PortableBrainError, match="duplicate proposed action"):
        normalize_secretary_decision({**raw, "proposed_actions": ["NONE", "NONE"]})
    with pytest.raises(PortableBrainError, match="safe integer"):
        normalize_secretary_decision({**raw, "slots": {"value": 9_007_199_254_740_992}})


def test_pack_profile_and_entity_bindings_cannot_be_silently_swapped():
    mismatched = profiles()[:-1]
    with pytest.raises(PortableBrainError, match="pack/profile binding mismatch"):
        PortableSecretaryRunner(pack(), [adapter("code", fixture("chatgpt.task-proposal.json"))], mismatched)
    bad = request()
    bad = BrainRequest(
        bad.contract_version,
        bad.task_type,
        bad.inputs,
        world_id=bad.world_id,
        entity_id="other-entity",
    )
    runner = PortableSecretaryRunner(pack(), [adapter("code", fixture("chatgpt.task-proposal.json"))], profiles())
    with pytest.raises(PortableBrainError, match="identity differs"):
        runner.run(bad)


def test_manual_exchange_contains_projected_envelope_and_no_runtime_token_requirement():
    response = fixture("chatgpt.task-proposal.json")
    profile = task_profile()
    manual = ManualHostAdapter(
        "chatgpt-manual",
        {(profile.profile_id, profile.version, profile.profile_hash): "R1"},
        {},
        task_types=("secretary.task",),
    )
    runner = PortableSecretaryRunner(pack(), [manual], profiles())
    exchange = runner.prepare_manual_exchange(request(), manual)
    assert exchange["api_token_used_by_runtime"] is False
    assert exchange["network_performed_by_runtime"] is False
    assert exchange["effective_resolutions"] == {"task": "R0"}
    assert exchange["request"]["inputs"][0]["envelope"]["value"]["title"] == "ارسال پیش‌نویس قرارداد"
    assert "priority" not in exchange["request"]["inputs"][0]["envelope"]["value"]
    assert "API_KEY" not in repr(exchange)
    imported = manual.import_response(response)
    result = runner.run(request())
    assert result.decision.semantic_hash == imported.semantic_hash
    assert result.provider == "chatgpt-manual"


def test_template_binding_is_strict_and_deterministic():
    decision = normalize_secretary_decision(fixture("chatgpt.task-proposal.json"))
    assert render_secretary_decision(pack(), decision) == render_secretary_decision(pack(), decision)
    broken = normalize_secretary_decision(
        {**fixture("chatgpt.task-proposal.json"), "slots": {"wrong": "x"}}
    )
    with pytest.raises(PortableBrainError, match="missing slot"):
        render_secretary_decision(pack(), broken)
