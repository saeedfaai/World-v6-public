from __future__ import annotations

import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator

from core.portable_brain import load_portable_pack, normalize_secretary_decision


CANDIDATE = Path(__file__).resolve().parents[3]
SCHEMAS = CANDIDATE / "schemas"
PACK = CANDIDATE / "brain-packs" / "secretary-001"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(schema_name, artifact):
    schema = load(SCHEMAS / schema_name)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(load(artifact))


def test_all_rc2_schemas_are_valid_draft_2020_12():
    for path in sorted(SCHEMAS.glob("*.schema.json")):
        Draft202012Validator.check_schema(load(path))


def test_machine_readable_nodes_handlers_council_maturity_pack_and_fixtures_conform():
    for path in sorted((CANDIDATE / "fractal" / "nodes").glob("*.json")):
        validate("fractal-node.schema.json", path)
    for path in sorted((CANDIDATE / "fractal" / "handlers").glob("*.json")):
        validate("brain-handler-profile.schema.json", path)
    validate(
        "council-session.schema.json",
        CANDIDATE / "fractal" / "council" / "secretary-high-risk-council.v1.json",
    )
    validate(
        "compilation-maturity.schema.json",
        CANDIDATE / "fractal" / "maturity" / "secretary-code-fallback.v1.json",
    )
    validate("portable-brain-pack.schema.json", PACK / "portable-brain-pack.v1.0.0.json")
    for path in sorted((PACK / "fixtures").glob("*.json")):
        validate("secretary-decision.schema.json", path)


def test_pack_hash_bindings_match_exact_bytes_and_provider_fixtures_are_semantically_equal():
    artifact = load(PACK / "portable-brain-pack.v1.0.0.json")
    assert artifact["dna_hash"] == sha256(PACK / "secretary-dna-overlay.v1.3-rc2.json")
    assert artifact["prompt_contract_hash"] == sha256(PACK / "PROMPT_CONTRACT_v1.0_FA.md")
    assert artifact["output_contract_hash"] == sha256(SCHEMAS / "secretary-decision.schema.json")
    loaded = load_portable_pack(PACK / "portable-brain-pack.v1.0.0.json")
    assert len(loaded.pack_hash) == 64
    manifest = load(CANDIDATE.parent / "RELEASE_MANIFEST.json")
    assert manifest["version"] == "6.2.0-rc.3"
    assert manifest["parent_release"]["release"] == "World v6.2 Fractal Multi-Brain RC2"
    assert manifest["portable_brain_pack"]["file_sha256"] == sha256(
        PACK / "portable-brain-pack.v1.0.0.json"
    )
    assert manifest["portable_brain_pack"]["canonical_sha256"] == loaded.pack_hash
    assert manifest["candidate"]["runtime_api_tokens_enabled"] is False
    semantic = {
        normalize_secretary_decision(load(path)).semantic_hash
        for path in sorted((PACK / "fixtures").glob("*.json"))
    }
    assert len(semantic) == 1


def test_provider_overlays_are_no_token_no_runtime_network_and_non_authoritative():
    for path in sorted((PACK / "provider-overlays").glob("*.json")):
        overlay = load(path)
        assert overlay["network_required_by_runtime"] is False
        assert overlay["api_token_required_by_runtime"] is False
        assert overlay["identity_authority_memory"] is False
        assert overlay["proposal_only"] is True
        assert "LIVE_API_VERIFIED" not in overlay["integration_status"]


def test_release_tree_contains_no_obvious_api_credentials_or_compiled_cache():
    forbidden_fragments = (
        "sk" + "-proj-",
        "AIza" + "Sy",
        "BEGIN PRIVATE" + " KEY",
        "xoxb" + "-",
    )
    for path in CANDIDATE.rglob("*"):
        if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        if path.suffix.lower() not in {".py", ".json", ".md", ".txt", ".yaml", ".yml", ".sql"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        assert not any(fragment in text for fragment in forbidden_fragments), path
