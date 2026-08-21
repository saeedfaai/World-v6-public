import pytest

from core.brain_gateway import (
    BrainGateway,
    BrainInputSegment,
    BrainRequest,
    BrainUnavailable,
)
from core.resolution import FieldRule, ProjectionProfile


def task_profile():
    return ProjectionProfile(
        "task", "0.2.0", "R1",
        (
            FieldRule("/id", "R0", "R1", "READ_ONLY_WHEN_PROJECTED", expected_type="string"),
            FieldRule("/title", "R0", "R0", expected_type="string"),
            FieldRule("/secret", "R1", "R1", "NO_DOWNGRADE", data_class="RESTRICTED", expected_type="string"),
        ),
        required_backbone_paths=("/id", "/title"),
    )


def context_profile():
    return ProjectionProfile(
        "conversation", "0.2.0", "R1",
        (
            FieldRule("/direction", "R0", "R1", "READ_ONLY_WHEN_PROJECTED", expected_type="string"),
            FieldRule("/text", "R0", "R1", "READ_ONLY_WHEN_PROJECTED", expected_type="string"),
            FieldRule("/provider", "R1", "R1", "READ_ONLY_WHEN_PROJECTED", expected_type="string"),
        ),
        required_backbone_paths=("/direction", "/text"),
    )


def segment(profile=None, **overrides):
    profile = profile or task_profile()
    values = {
        "segment_id": "task",
        "canonical": {"id": "T1", "title": "draft", "secret": "never-at-r0"},
        "profile_id": profile.profile_id,
        "profile_version": profile.version,
        "profile_hash": profile.profile_hash,
        "source_ref": "task:T1",
        "source_version": 4,
        "desired_resolution": "R1",
        "minimum_resolution": "R0",
        "purpose": "DRAFT",
        "data_class": "RESTRICTED",
        "freshness": "CURRENT",
    }
    values.update(overrides)
    return BrainInputSegment(**values)


class Provider:
    def __init__(self, name, capabilities, compatible=True, fail=False):
        self.name = name
        self.capabilities = capabilities
        self._compatible = compatible
        self.fail = fail
        self.descriptor = None
        self.seen = None

    def compatible(self, descriptor):
        self.descriptor = descriptor
        return self._compatible

    def max_resolution_for(self, profile_id, profile_version, profile_hash):
        return self.capabilities.get((profile_id, profile_version, profile_hash))

    def invoke(self, request):
        self.seen = request
        if self.fail:
            raise RuntimeError("provider failed")
        return {"ok": True}


def request(*segments):
    return BrainRequest("2", "draft", tuple(segments or (segment(),)))


def capability(profile, level):
    return {(profile.profile_id, profile.version, profile.profile_hash): level}


def test_gateway_projects_real_input_before_provider_boundary():
    profile = task_profile()
    provider = Provider("small", capability(profile, "R0"))
    response = BrainGateway([provider], [profile]).invoke(request(segment(profile)))
    envelope = provider.seen.inputs[0].envelope
    assert response.effective_resolution == "R0"
    assert envelope["value"] == {"id": "T1", "title": "draft"}
    assert "secret" not in envelope["value"]
    assert "omitted_paths" not in envelope
    assert envelope["profile_hash"] == profile.profile_hash


def test_compatibility_gate_receives_metadata_only():
    profile = task_profile()
    provider = Provider("p", capability(profile, "R0"))
    BrainGateway([provider], [profile]).invoke(request(segment(profile)))
    descriptor_segment = provider.descriptor.segments[0]
    assert "canonical" not in descriptor_segment
    assert "never-at-r0" not in repr(provider.descriptor)


def test_provider_capability_is_profile_and_hash_scoped():
    profile = task_profile()
    wrong = {(profile.profile_id, profile.version, "0" * 64): "R1"}
    with pytest.raises(BrainUnavailable):
        BrainGateway([Provider("wrong", wrong)], [profile]).invoke(request(segment(profile)))


def test_scalar_legacy_max_is_not_treated_as_cross_domain_capability():
    profile = task_profile()

    class Legacy:
        name = "legacy"
        max_resolution = "R9"
        def compatible(self, descriptor): return True
        def invoke(self, request): return {"ok": True}

    with pytest.raises(BrainUnavailable):
        BrainGateway([Legacy()], [profile]).invoke(request(segment(profile)))


def test_low_provider_is_skipped_when_any_segment_minimum_is_unmet():
    task = task_profile()
    context = context_profile()
    low_caps = {**capability(task, "R0"), **capability(context, "R0")}
    high_caps = {**capability(task, "R1"), **capability(context, "R1")}
    low = Provider("low", low_caps)
    high = Provider("high", high_caps)
    context_segment = segment(
        context,
        segment_id="context",
        canonical={"direction": "INBOUND", "text": "hello", "provider": "openai"},
        source_ref="message:M1",
        minimum_resolution="R1",
        data_class="INTERNAL",
    )
    response = BrainGateway([low, high], [task, context]).invoke(
        request(segment(task), context_segment)
    )
    assert response.provider == "high"
    assert low.seen is None
    assert dict(response.effective_resolutions) == {"task": "R1", "context": "R1"}
    with pytest.raises(Exception):
        _ = response.effective_resolution


def test_provider_failure_fails_over_without_changing_identity_or_profiles():
    profile = task_profile()
    caps = capability(profile, "R0")
    first = Provider("first", caps, fail=True)
    second = Provider("second", caps)
    response = BrainGateway([first, second], [profile]).invoke(request(segment(profile)))
    assert response.provider == "second"
    assert second.seen.entity_id == "secretary-001"
    assert second.seen.inputs[0].envelope["profile_hash"] == profile.profile_hash


def test_request_profile_hash_mismatch_fails_before_provider_invocation():
    profile = task_profile()
    provider = Provider("p", capability(profile, "R1"))
    bad = segment(profile, profile_hash="0" * 64)
    with pytest.raises(Exception, match="hash mismatch"):
        BrainGateway([provider], [profile]).invoke(request(bad))
    assert provider.seen is None
