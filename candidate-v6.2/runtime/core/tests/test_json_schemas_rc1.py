import json
from pathlib import Path

from jsonschema import Draft202012Validator

from core.resolution import (
    FieldRule,
    PatchOperation,
    ProjectionProfile,
    ResolutionPatch,
    canonical_hash,
    project,
)
from core.effects import ApprovalBinding, ExternalEffectProposal, sha256_bytes


ROOT = Path(__file__).resolve().parents[3]
SCHEMAS = ROOT / "schemas"
PROFILES = ROOT / "profiles"


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def test_all_active_profiles_conform_to_one_machine_schema():
    validator = Draft202012Validator(load(SCHEMAS / "resolution-profile.schema.json"))
    active = sorted(PROFILES.glob("*.v0.2.json"))
    assert active
    for path in active:
        errors = sorted(validator.iter_errors(load(path)), key=lambda error: list(error.path))
        assert not errors, f"{path.name}: {[error.message for error in errors]}"


def test_runtime_envelope_conforms_to_schema():
    profile = ProjectionProfile(
        "sample", "1", "R0",
        (FieldRule("/id", "R0", "R0", expected_type="string"),),
        required_backbone_paths=("/id",),
    )
    envelope = project(
        {"id": "E1"}, profile=profile, target_resolution="R0",
        source_ref="entity:E1", source_version=2, purpose="TEST",
    ).consumer_envelope()
    Draft202012Validator(load(SCHEMAS / "resolution-envelope.schema.json")).validate(envelope)


def test_patch_contract_requires_every_concurrency_and_provenance_guard():
    profile = ProjectionProfile(
        "sample", "1", "R0",
        (FieldRule("/status", "R0", "R0", expected_type="string"),),
    )
    canonical = {"status": "OPEN"}
    view = project(canonical, profile=profile, target_resolution="R0")
    patch = {
        "actor_resolution": "R0",
        "expected_canonical_hash": canonical_hash(canonical),
        "expected_projection_hash": view.projection_hash,
        "expected_version": 1,
        "source_ref": "state:E1",
        "profile_id": profile.profile_id,
        "profile_version": profile.version,
        "profile_hash": profile.profile_hash,
        "operations": [{"op": "set", "path": "/status", "value": "DONE"}],
    }
    Draft202012Validator(load(SCHEMAS / "resolution-patch.schema.json")).validate(patch)


def test_effect_and_approval_documents_are_machine_validated():
    proposal = ExternalEffectProposal(
        "world-v6", "secretary-001", "cmd-1", "telegram", "SEND_DOCUMENT",
        "artifact:x.pdf", "telegram-chat:1", "blob:x", sha256_bytes(b"pdf"),
        "1.2.0", 2, 1, "secretary:telegram", "x-to-1",
    )
    approval = ApprovalBinding(
        "approval-1", "human-root", "APPROVE", "cmd-1", "SEND_DOCUMENT",
        "telegram-chat:1", proposal.payload_hash, proposal.effect_hash, "1.2.0",
        2, 1, "2026-08-20T10:00:00Z", "2026-08-20T11:00:00Z",
    )
    Draft202012Validator(load(SCHEMAS / "external-effect-proposal.schema.json")).validate(
        proposal.binding_document()
    )
    approval_document = {
        field: getattr(approval, field)
        for field in approval.__dataclass_fields__
    }
    Draft202012Validator(load(SCHEMAS / "approval-binding.schema.json")).validate(
        approval_document
    )
