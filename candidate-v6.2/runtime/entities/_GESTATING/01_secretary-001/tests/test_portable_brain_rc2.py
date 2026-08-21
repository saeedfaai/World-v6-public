from __future__ import annotations

import json
from pathlib import Path

from core.portable_brain import PortableSecretaryRunner, ScriptedPortableAdapter, load_portable_pack
from core.resolution import load_profile_file
from src.brain_portability import PortableSecretaryService
from src.secretary import Secretary001


CANDIDATE = Path(__file__).resolve().parents[5]
PACK_DIR = CANDIDATE / "brain-packs" / "secretary-001"
PROFILE_DIR = CANDIDATE / "profiles"


def load_profiles():
    return [load_profile_file(path) for path in sorted(PROFILE_DIR.glob("*v0.2.json"))]


def task_fixture():
    return json.loads(
        (PACK_DIR / "fixtures" / "chatgpt.task-proposal.json").read_text(encoding="utf-8")
    )


def runner(provider_name):
    profiles = load_profiles()
    task = next(profile for profile in profiles if profile.profile_id == "secretary.task")
    adapter = ScriptedPortableAdapter(
        provider_name,
        {(task.profile_id, task.version, task.profile_hash): "R1"},
        task_fixture(),
        task_types=("secretary.task",),
    )
    return PortableSecretaryRunner(
        load_portable_pack(PACK_DIR / "portable-brain-pack.v1.0.0.json"),
        [adapter],
        profiles,
    )


def test_real_secretary_state_can_use_any_provider_without_provider_owned_state():
    secretary = Secretary001(execution_resolution="R0")
    task = secretary.add_task(title="ارسال پیش‌نویس قرارداد", next_action="DRAFT")
    before = dict(secretary.store.tasks)
    results = [
        PortableSecretaryService(secretary, runner(provider)).decide_task(task.task_id)
        for provider in ("chatgpt-manual", "gemini-manual", "grok-manual", "code")
    ]
    assert {result.rendered_text for result in results} == {
        "کار «ارسال پیش‌نویس قرارداد» به‌صورت پیشنهاد آماده شد."
    }
    assert {result.decision.semantic_hash for result in results}.__len__() == 1
    assert secretary.store.tasks == before
    assert all(result.decision.to_document()["proposal_only"] for result in results)
