from decimal import Decimal

import pytest

from core.resolution import (
    ActionRule,
    CanonicalJSONError,
    FieldRule,
    PatchOperation,
    PatchRejected,
    ProjectionError,
    ProjectionProfile,
    ResolutionError,
    ResolutionMismatch,
    ResolutionPatch,
    apply_patch,
    assert_monotonic_projection,
    canonical_hash,
    negotiate_resolution,
    project,
    require_action_compatibility,
)


def profile() -> ProjectionProfile:
    return ProjectionProfile(
        profile_id="task-backbone",
        version="0.2.0",
        canonical_resolution="R2",
        fields=(
            FieldRule("/task_id", "R0", "R2", "READ_ONLY_WHEN_PROJECTED", expected_type="string"),
            FieldRule("/title", "R0", "R0", expected_type="string"),
            FieldRule("/status", "R0", "R0", expected_type="string"),
            FieldRule("/next_action", "R0", "R0", expected_type="string"),
            FieldRule("/tags", "R1", "R2", "READ_ONLY_WHEN_PROJECTED", expected_type="array"),
            FieldRule("/priority", "R1", "R1", expected_type="string"),
            FieldRule("/domain", "R1", "R1", expected_type="string"),
            FieldRule(
                "/legal/obligation", "R2", "R2", "NO_DOWNGRADE",
                data_class="RESTRICTED", expected_type="string",
            ),
            FieldRule(
                "/legal/source_ref", "R2", "R2", "READ_ONLY_WHEN_PROJECTED",
                data_class="RESTRICTED", expected_type="string",
            ),
        ),
        required_backbone_paths=("/task_id", "/title", "/status", "/next_action"),
        actions=(
            ActionRule("UPDATE_STATUS", "R0", ("/task_id", "/status")),
            ActionRule("LEGAL_COMMIT", "R2", ("/legal/obligation", "/legal/source_ref")),
        ),
    )


def canonical() -> dict:
    return {
        "task_id": "T1",
        "title": "نامه",
        "status": "OPEN",
        "next_action": "draft",
        "tags": ["customer", "legal"],
        "priority": "HIGH",
        "domain": "legal",
        "legal": {"obligation": "must review", "source_ref": "doc-1"},
    }


def projection(level: str = "R0"):
    return project(
        canonical(),
        profile=profile(),
        target_resolution=level,
        source_ref="task:T1",
        source_version=7,
        purpose="TASK_DECISION",
        data_class="RESTRICTED",
        freshness="CURRENT",
    )


def patch_for(*operations: PatchOperation, level: str = "R0", **overrides) -> ResolutionPatch:
    current = canonical()
    view = projection(level)
    values = {
        "actor_resolution": level,
        "expected_canonical_hash": canonical_hash(current),
        "expected_projection_hash": view.projection_hash,
        "expected_version": 7,
        "source_ref": "task:T1",
        "operations": tuple(operations),
        "projection_profile_id": profile().profile_id,
        "projection_profile_version": profile().version,
        "projection_profile_hash": profile().profile_hash,
    }
    values.update(overrides)
    return ResolutionPatch(**values)


def test_projection_preserves_backbone_and_never_mutates_canonical():
    document = canonical()
    before = canonical_hash(document)
    result = projection("R0")
    assert result.value == {
        "task_id": "T1", "title": "نامه", "status": "OPEN", "next_action": "draft"
    }
    assert canonical_hash(document) == before
    assert "/legal/obligation" in result.no_downgrade_paths


def test_consumer_envelope_keeps_provenance_without_leaking_omitted_names():
    result = projection("R0")
    envelope = result.consumer_envelope()
    assert envelope["profile_hash"] == profile().profile_hash
    assert envelope["canonical_hash"] == canonical_hash(canonical())
    assert envelope["projection_hash"] == canonical_hash(envelope["value"])
    assert envelope["projection_derived"] is True
    assert envelope["projection_authoritative"] is False
    assert "omitted_paths" not in envelope
    assert "/legal/obligation" in result.audit_metadata()["omitted_paths"]


def test_projection_is_compositional_and_monotonic():
    assert_monotonic_projection(canonical(), profile=profile(), lower="R0", higher="R1")
    assert_monotonic_projection(canonical(), profile=profile(), lower="R0", higher="R2")


def test_low_resolution_patch_preserves_hidden_fine_wires():
    updated = apply_patch(
        canonical(),
        profile=profile(),
        patch=patch_for(PatchOperation("/status", "DONE")),
        current_version=7,
        source_ref="task:T1",
    )
    assert updated["status"] == "DONE"
    assert updated["priority"] == "HIGH"
    assert updated["legal"] == canonical()["legal"]


@pytest.mark.parametrize(
    "operation",
    [
        PatchOperation("/legal/obligation", "ignore"),
        PatchOperation("/unknown", "x"),
        PatchOperation("/tags", ["replace-all"]),
        PatchOperation("/status", 1),
    ],
)
def test_unsafe_low_resolution_writes_fail_closed(operation):
    with pytest.raises(PatchRejected):
        apply_patch(
            canonical(),
            profile=profile(),
            patch=patch_for(operation),
            current_version=7,
            source_ref="task:T1",
        )


@pytest.mark.parametrize(
    "override,match",
    [
        ({"expected_canonical_hash": "0" * 64}, "canonical"),
        ({"expected_projection_hash": "0" * 64}, "projection"),
        ({"expected_version": 6}, "version"),
        ({"source_ref": "task:T2"}, "source_ref"),
        ({"projection_profile_hash": "0" * 64}, "profile"),
    ],
)
def test_all_patch_guards_are_enforced(override, match):
    with pytest.raises(PatchRejected, match=match):
        apply_patch(
            canonical(),
            profile=profile(),
            patch=patch_for(PatchOperation("/status", "DONE"), **override),
            current_version=7,
            source_ref="task:T1",
        )


def test_missing_or_non_object_ancestor_is_never_overwritten():
    altered = canonical()
    altered["legal"] = "hidden-scalar"
    bad_profile = ProjectionProfile(
        "x", "1", "R1",
        (FieldRule("/legal/obligation", "R1", "R1", expected_type="string"),),
    )
    view = project(
        {"legal": {"obligation": "x"}}, profile=bad_profile, target_resolution="R1"
    )
    patch = ResolutionPatch(
        "R1", canonical_hash(altered), view.projection_hash, 1, "state:E1",
        (PatchOperation("/legal/obligation", "y"),),
        "x", "1", bad_profile.profile_hash,
    )
    with pytest.raises(PatchRejected, match="no longer conforms"):
        apply_patch(
            altered, profile=bad_profile, patch=patch, current_version=1, source_ref="state:E1"
        )


def test_strict_hashing_distinguishes_types_and_rejects_implicit_conversion():
    assert canonical_hash({"v": 1}) != canonical_hash({"v": "1"})
    with pytest.raises(CanonicalJSONError):
        canonical_hash({"v": Decimal("1")})
    with pytest.raises(CanonicalJSONError):
        canonical_hash({"v": 1.0})


def test_profile_fails_closed_on_unknown_fields_or_unsafe_structure():
    with pytest.raises(ProjectionError, match="no projection rule"):
        project({**canonical(), "surprise": "leak"}, profile=profile(), target_resolution="R0", data_class="RESTRICTED")
    with pytest.raises(ResolutionError, match="allow_unspecified"):
        ProjectionProfile("x", "1", "R0", (FieldRule("/id"),), allow_unspecified=True)
    with pytest.raises(ResolutionError, match="above canonical"):
        ProjectionProfile("x", "1", "R0", (FieldRule("/id", "R1"),))
    with pytest.raises(ResolutionError, match="overlap"):
        ProjectionProfile("x", "1", "R1", (FieldRule("/a"), FieldRule("/a/b", "R1")))


def test_data_classification_cannot_be_lowered_by_projection():
    with pytest.raises(ProjectionError, match="understates"):
        project(canonical(), profile=profile(), target_resolution="R0", data_class="INTERNAL")


def test_action_requires_level_and_declared_fine_wires():
    require_action_compatibility(profile=profile(), action="UPDATE_STATUS", projection=projection("R0"))
    with pytest.raises(ResolutionMismatch):
        require_action_compatibility(profile=profile(), action="LEGAL_COMMIT", projection=projection("R1"))
    require_action_compatibility(profile=profile(), action="LEGAL_COMMIT", projection=projection("R2"))


def test_negotiation_never_weakens_minimum_or_exceeds_profile_canonical():
    assert negotiate_resolution(
        desired="R2", minimum="R0", brain_max="R1", canonical_resolution="R2"
    ) == "R1"
    with pytest.raises(ResolutionMismatch):
        negotiate_resolution(
            desired="R2", minimum="R2", brain_max="R1", canonical_resolution="R2"
        )
    with pytest.raises(ResolutionMismatch):
        negotiate_resolution(
            desired="R3", minimum="R0", brain_max="R3", canonical_resolution="R2"
        )
