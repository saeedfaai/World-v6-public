from core.kernel import Kernel
from core.resolution import (
    FieldRule,
    PatchOperation,
    ProjectionProfile,
    ResolutionPatch,
    canonical_hash,
    project,
)


def test_kernel_hook_validates_only_and_never_touches_database():
    profile = ProjectionProfile(
        "x", "1", "R1",
        (
            FieldRule("/id", "R0", "R1", "READ_ONLY_WHEN_PROJECTED"),
            FieldRule("/status", "R0", "R0"),
            FieldRule("/detail", "R1", "R1"),
        ),
        required_backbone_paths=("/id", "/status"),
    )
    state = {"id": "E1", "status": "OPEN", "detail": "secret-detail"}
    view = project(
        state, profile=profile, target_resolution="R0",
        source_ref="state:E1", source_version=3,
    )
    patch = ResolutionPatch(
        "R0",
        canonical_hash(state),
        view.projection_hash,
        3,
        "state:E1",
        (PatchOperation("/status", "DONE"),),
        "x",
        "1",
        profile.profile_hash,
    )
    kernel = Kernel(
        lambda: (_ for _ in ()).throw(AssertionError("DB must not be touched by validation helper"))
    )
    updated = kernel.validate_resolution_patch(
        canonical_state=state,
        profile=profile,
        patch=patch,
        current_version=3,
        source_ref="state:E1",
    )
    assert updated == {"id": "E1", "status": "DONE", "detail": "secret-detail"}
