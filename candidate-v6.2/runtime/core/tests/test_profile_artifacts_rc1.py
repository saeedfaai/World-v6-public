import json
from pathlib import Path

from core.resolution import canonical_hash, load_profile_file


PROFILE_DIR = Path(__file__).resolve().parents[3] / "profiles"


def test_every_active_profile_is_runtime_loadable_and_hash_stable():
    active = sorted(PROFILE_DIR.glob("*.v0.2.json"))
    assert len(active) == 5
    identities = set()
    for path in active:
        profile = load_profile_file(path)
        identity = (profile.profile_id, profile.version)
        assert identity not in identities
        identities.add(identity)
        assert profile.profile_hash == canonical_hash(profile.to_document())
        assert profile.allow_unspecified is False
        assert set(profile.required_backbone_paths).issubset(profile.rule_map())


def test_profile_hash_is_semantic_and_independent_of_json_key_order(tmp_path):
    source = PROFILE_DIR / "secretary-task-profile.v0.2.json"
    document = json.loads(source.read_text(encoding="utf-8"))
    reordered = {key: document[key] for key in reversed(document)}
    target = tmp_path / "reordered.json"
    target.write_text(json.dumps(reordered, ensure_ascii=False), encoding="utf-8")
    assert load_profile_file(source).profile_hash == load_profile_file(target).profile_hash
