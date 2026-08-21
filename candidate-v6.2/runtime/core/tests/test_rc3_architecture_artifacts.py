from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

from core.portable_brain import PortableBrainError, normalize_secretary_decision
from core.resolution import load_profile_file


CANDIDATE = Path(__file__).resolve().parents[3]
RELEASE_ROOT = CANDIDATE.parent
SCHEMAS = CANDIDATE / "schemas"
PACK_DIR = CANDIDATE / "brain-packs" / "secretary-001"
ARCHITECTURE_PATH = (
    CANDIDATE
    / "docs"
    / "WORLD_V6_2_FRACTAL_MULTI_BRAIN_ARCHITECTURE_v1.1_FA.md"
)
ARCHITECTURE_MANIFEST_PATH = (
    CANDIDATE / "architecture" / "ARCHITECTURE_MANIFEST_v1.1.0-rc3.json"
)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def universal_bridge():
    path = RELEASE_ROOT / "tools" / "universal_model_bridge.py"
    spec = importlib.util.spec_from_file_location("world_v6_universal_model_bridge", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(schema_name: str, document) -> None:
    schema = load(SCHEMAS / schema_name)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(document)


def validate_bundle_schema(bundle) -> None:
    manual_schema = load(SCHEMAS / "manual-brain-exchange.schema.json")
    bundle_schema = load(SCHEMAS / "portable-model-bundle.schema.json")
    registry = Registry().with_resource(
        manual_schema["$id"], Resource.from_contents(manual_schema)
    )
    Draft202012Validator(bundle_schema, registry=registry).validate(bundle)


def test_architecture_manifest_is_bound_to_the_complete_document():
    manifest = load(ARCHITECTURE_MANIFEST_PATH)
    release = load(RELEASE_ROOT / "RELEASE_MANIFEST.json")
    validate("architecture-manifest.schema.json", manifest)
    assert manifest["document"]["sha256"] == sha256(ARCHITECTURE_PATH)
    assert release["architecture"]["document_sha256"] == sha256(ARCHITECTURE_PATH)
    assert release["architecture"]["manifest_sha256"] == sha256(
        ARCHITECTURE_MANIFEST_PATH
    )
    assert manifest["immutable_foundation"]["parent_release"] == (
        "World v6.2 Fractal Multi-Brain RC2"
    )
    assert manifest["evidence_boundary"] == {
        "current": "E2",
        "production_claim_minimum": "E4",
        "live_provider_verified": False,
        "postgresql_integration_verified": False,
        "restore_verified": False,
    }


def test_complete_architecture_contains_every_required_operational_domain():
    text = ARCHITECTURE_PATH.read_text(encoding="utf-8")
    assert len(text.splitlines()) >= 1_400
    required = (
        "## ۳. قوانین تغییرناپذیر",
        "## ۶. مدل فراکتالی سادگی تا پیچیدگی",
        "## ۸. Resolution به‌عنوان کابل داده",
        "## ۹. معماری Multi-Brain و قابلیت حمل میان همهٔ مدل‌ها",
        "## ۱۲. Context Compiler و معماری حافظه",
        "## ۱۴. Brain Council؛ تالار مشورت محدود",
        "## ۱۵. Hot Path، Shadow Path و ستون عدم‌انقراض",
        "## ۱۶. Governance، Policy و External Effect",
        "## ۲۱. Observability، Evidence و SLO",
        "## ۲۲. Threat Model",
        "## ۲۶. Test Architecture و معیار ابطال",
        "## ۲۸. مسیر پیاده‌سازی از امروز",
    )
    assert all(item in text for item in required)
    assert "RATIFICATION_CANDIDATE_NOT_CANONICAL_NOT_DEPLOYED" in text


def test_universal_model_card_is_schema_valid_and_exactly_profile_bound():
    card_path = PACK_DIR / "model-cards" / "universal-manual-host.v1.json"
    overlay_path = PACK_DIR / "provider-overlays" / "universal-manual.v1.json"
    bridge_path = RELEASE_ROOT / "tools" / "universal_model_bridge.py"
    card = load(card_path)
    release = load(RELEASE_ROOT / "RELEASE_MANIFEST.json")
    validate("model-capability-card.schema.json", card)
    observed = {
        item["profile_id"]: item["profile_hash"]
        for item in card["capabilities"]["resolution_bindings"]
    }
    expected = {
        profile.profile_id: profile.profile_hash
        for profile in (
            load_profile_file(path)
            for path in sorted((CANDIDATE / "profiles").glob("*v0.2.json"))
        )
    }
    assert observed == expected
    assert card["provider_family"] == "ANY_CONFORMING_MODEL"
    assert card["governance"]["network_required_by_runtime"] is False
    assert card["governance"]["api_token_required_by_runtime"] is False
    assert card["governance"]["proposal_only"] is True
    universal = release["universal_model_path"]
    assert universal["model_card_sha256"] == sha256(card_path)
    assert universal["provider_overlay_sha256"] == sha256(overlay_path)
    assert universal["bridge_sha256"] == sha256(bridge_path)
    assert universal["schemas"] == {
        "model_capability_card_sha256": sha256(
            SCHEMAS / "model-capability-card.schema.json"
        ),
        "manual_exchange_sha256": sha256(
            SCHEMAS / "manual-brain-exchange.schema.json"
        ),
        "portable_model_bundle_sha256": sha256(
            SCHEMAS / "portable-model-bundle.schema.json"
        ),
        "architecture_manifest_sha256": sha256(
            SCHEMAS / "architecture-manifest.schema.json"
        ),
    }


def test_arbitrary_model_gets_a_self_contained_schema_valid_zero_api_bundle():
    bridge = universal_bridge()
    bundle = bridge.build_task_bundle(
        PACK_DIR / "examples" / "task-input.example.json",
        "arbitrary-model-xyz",
    )
    validate_bundle_schema(bundle)
    assert bridge.validate_bundle(bundle) == bundle["integrity"]["bundle_payload_hash"]
    assert bundle["exchange"]["provider_hint"] == "arbitrary-model-xyz"
    assert bundle["runtime_claims"] == {
        "network_used": False,
        "api_token_used": False,
        "authoritative": False,
        "external_effect_enabled": False,
    }
    assert bundle["exchange"]["proposal_only"] is True
    assert "priority" not in bundle["exchange"]["request"]["inputs"][0]["envelope"]["value"]


def test_portable_bundle_integrity_fails_closed_after_projection_tampering():
    bridge = universal_bridge()
    bundle = bridge.build_task_bundle(
        PACK_DIR / "examples" / "task-input.example.json",
        "any-conforming-model",
    )
    bundle["exchange"]["request"]["inputs"][0]["envelope"]["value"]["title"] = (
        "tampered"
    )
    with pytest.raises(PortableBrainError, match="payload hash mismatch"):
        bridge.validate_bundle(bundle)


def test_any_conforming_model_response_has_the_same_semantics_and_rendering():
    bridge = universal_bridge()
    semantic_hashes = set()
    rendered = set()
    for name in (
        "chatgpt.task-proposal.json",
        "gemini.task-proposal.json",
        "grok.task-proposal.json",
    ):
        result = bridge.validate_and_render(PACK_DIR / "fixtures" / name)
        semantic_hashes.add(result["semantic_hash"])
        rendered.add(result["rendered_text"])
        assert result["proposal_only"] is True
        assert result["network_used"] is False
        assert result["api_token_used"] is False
    assert len(semantic_hashes) == 1
    assert rendered == {"کار «ارسال پیش‌نویس قرارداد» به‌صورت پیشنهاد آماده شد."}


def test_model_output_cannot_smuggle_authority_through_the_universal_path():
    response = load(PACK_DIR / "fixtures" / "chatgpt.task-proposal.json")
    with pytest.raises(PortableBrainError, match="forbidden"):
        normalize_secretary_decision({**response, "canonical_write": True})
    with pytest.raises(PortableBrainError, match="forbidden proposed action"):
        normalize_secretary_decision(
            {**response, "proposed_actions": ["EXECUTE_EXTERNAL"]}
        )
