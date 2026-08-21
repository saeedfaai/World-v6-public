#!/usr/bin/env python3
"""Offline, no-token conformance demo for the portable Secretary Brain Pack."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "candidate-v6.2" / "runtime"))

from core.brain_gateway import BrainInputSegment, BrainRequest  # noqa: E402
from core.portable_brain import (  # noqa: E402
    PortableSecretaryRunner,
    ScriptedPortableAdapter,
    load_portable_pack,
)
from core.resolution import load_profile_file  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", choices=("chatgpt", "gemini", "grok"), default="chatgpt")
    parser.add_argument("--title", default="ارسال پیش‌نویس قرارداد")
    args = parser.parse_args()

    candidate = ROOT / "candidate-v6.2"
    pack_dir = candidate / "brain-packs" / "secretary-001"
    profiles = [
        load_profile_file(path) for path in sorted((candidate / "profiles").glob("*v0.2.json"))
    ]
    task_profile = next(item for item in profiles if item.profile_id == "secretary.task")
    fixture = json.loads(
        (pack_dir / "fixtures" / f"{args.provider}.task-proposal.json").read_text(encoding="utf-8")
    )
    fixture["slots"]["title"] = args.title
    adapter = ScriptedPortableAdapter(
        f"{args.provider}-offline-fixture",
        {(task_profile.profile_id, task_profile.version, task_profile.profile_hash): "R1"},
        fixture,
        task_types=("secretary.task",),
    )
    runner = PortableSecretaryRunner(
        load_portable_pack(pack_dir / "portable-brain-pack.v1.0.0.json"),
        [adapter],
        profiles,
    )
    segment = BrainInputSegment(
        "task",
        {
            "task_id": "demo-task",
            "title": args.title,
            "status": "OPEN",
            "next_action": "DRAFT",
            "due_at": None,
            "priority": "NORMAL",
            "domain": "general",
            "goal_id": None,
            "created_at": "2026-08-20T00:00:00Z"
        },
        task_profile.profile_id,
        task_profile.version,
        task_profile.profile_hash,
        "task:demo-task",
        0,
        "R0",
        "R0",
        "TASK_PROPOSAL",
    )
    result = runner.run(
        BrainRequest("world-v6.brain-request.v2", "secretary.task", (segment,))
    )
    print(json.dumps({
        "provider": result.provider,
        "pack_hash": result.pack_hash,
        "semantic_hash": result.decision.semantic_hash,
        "rendered_text": result.rendered_text,
        "api_token_used": False,
        "network_used": False,
        "proposal_only": True,
    }, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
