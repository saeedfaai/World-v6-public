from __future__ import annotations

from dataclasses import replace

import pytest

from core.fractal_runtime import (
    ExecutionBudget,
    ExecutionVector,
    FractalContractError,
    FractalExecutionError,
    FractalNode,
    FractalOrchestrator,
    HandlerProfile,
    HandlerRegistry,
    HandlerResult,
    HandlerStatus,
    OutcomeStatus,
)


class Handler:
    def __init__(self, profile, status=HandlerStatus.SUCCESS, output=None, error=None):
        self.profile = profile
        self.status = status
        self.output = output or {"proposal_type": "TEST", "value": "ok"}
        self.error = error
        self.calls = 0

    def invoke(self, capsule, payload):
        self.calls += 1
        if self.error:
            raise self.error
        return HandlerResult(
            self.profile.handler_id,
            self.profile.version,
            self.status,
            self.output,
            confidence_millis=900,
            trace_summary="TEST",
        )


def vector(**changes):
    values = {
        "resolutions": (("task", "R0"),),
        "granularity": "X0",
        "brain_delegation": "B0",
        "deliberation": "D0",
        "compilation": "C0",
        "authority": "A0",
        "evidence": "E0",
        "model_capability": "M0",
    }
    values.update(changes)
    return ExecutionVector(**values)


def profile(identifier, nodes, **changes):
    values = {
        "handler_id": identifier,
        "version": "1.0.0",
        "kind": "CODE",
        "maturity": "C2",
        "evidence": "E2",
        "supported_node_ids": tuple(nodes),
        "deterministic": True,
    }
    values.update(changes)
    return HandlerProfile(**values)


def node(identifier="root", handlers=("code",), **changes):
    values = {
        "node_id": identifier,
        "version": "1.0.0",
        "purpose": "test",
        "input_contract_ref": "schema:input@1",
        "output_contract_ref": "schema:output@1",
        "handler_ids": tuple(handlers),
        "minimum_vector": vector(),
    }
    values.update(changes)
    return FractalNode(**values)


def capsule(orchestrator, selected, payload, **changes):
    return orchestrator.build_capsule(
        selected,
        payload,
        capsule_id="cap:1",
        vector=changes.pop("vector", vector()),
        budget=changes.pop("budget", ExecutionBudget()),
        **changes,
    )


def test_cheapest_safe_handler_wins_without_expansion():
    first = Handler(profile("code", ("root",)))
    second = Handler(profile("brain", ("root",), kind="BRAIN", deterministic=False))
    selected = node(handlers=("code", "brain"))
    engine = FractalOrchestrator([selected], HandlerRegistry([first, second]))
    payload = {"title": "hello"}
    outcome = engine.execute("root", capsule(engine, selected, payload), payload)
    assert outcome.status is OutcomeStatus.PROPOSED
    assert first.calls == 1
    assert second.calls == 0


def test_network_and_api_handlers_are_skipped_then_code_fallback_runs():
    remote = Handler(
        profile(
            "remote",
            ("root",),
            kind="BRAIN",
            deterministic=False,
            network_required=True,
            api_token_required=True,
        )
    )
    fallback = Handler(profile("code", ("root",)))
    selected = node(handlers=("remote",), fallback_handler_ids=("code",))
    engine = FractalOrchestrator([selected], HandlerRegistry([remote, fallback]))
    payload = {"title": "offline"}
    outcome = engine.execute("root", capsule(engine, selected, payload), payload)
    assert outcome.status is OutcomeStatus.PROPOSED
    assert [attempt.reason for attempt in outcome.attempts] == [
        "BRAIN_DELEGATION_DISABLED",
        "TEST",
    ]
    outcome = engine.execute(
        "root",
        capsule(engine, selected, payload, vector=vector(brain_delegation="B1")),
        payload,
    )
    assert [attempt.reason for attempt in outcome.attempts] == ["NETWORK_DISABLED", "TEST"]
    assert remote.calls == 0 and fallback.calls == 2


def test_needs_detail_expands_only_bounded_children():
    router = Handler(profile("router", ("root",)), HandlerStatus.NEEDS_DETAIL)
    specialist = Handler(profile("specialist", ("child",)))
    root = node(
        handlers=("router",),
        expandable=True,
        child_ids=("child",),
    )
    child = node(
        "child",
        ("specialist",),
        parent_id="root",
        minimum_vector=vector(granularity="X1"),
    )
    engine = FractalOrchestrator([root, child], HandlerRegistry([router, specialist]))
    payload = {"title": "expand"}
    outcome = engine.execute("root", capsule(engine, root, payload), payload)
    assert outcome.status is OutcomeStatus.EXPANDED
    assert outcome.proposal["proposal_type"] == "FRACTAL_COMPOSITE"
    assert outcome.child_outcomes[0].capsule.parent_capsule_id == "cap:1"
    assert outcome.child_outcomes[0].capsule.vector.granularity == "X1"


def test_resolution_and_axis_minima_never_downgrade_on_fallback():
    handler = Handler(profile("code", ("root",)))
    selected = node(
        handlers=("code",),
        minimum_vector=vector(
            resolutions=(("task", "R1"),),
            authority="A1",
            evidence="E1",
        ),
    )
    engine = FractalOrchestrator([selected], HandlerRegistry([handler]))
    payload = {"title": "unsafe-low"}
    with pytest.raises(FractalExecutionError, match="Resolution below"):
        engine.execute("root", capsule(engine, selected, payload), payload)
    with pytest.raises(FractalExecutionError, match="A below"):
        engine.execute(
            "root",
            capsule(
                engine,
                selected,
                payload,
                vector=vector(resolutions=(("task", "R1"),), evidence="E1"),
            ),
            payload,
        )
    assert handler.calls == 0


def test_capsule_binds_exact_node_and_input_hash():
    handler = Handler(profile("code", ("root",)))
    selected = node()
    engine = FractalOrchestrator([selected], HandlerRegistry([handler]))
    payload = {"title": "original"}
    bound = capsule(engine, selected, payload)
    with pytest.raises(FractalExecutionError, match="input hash"):
        engine.execute("root", bound, {"title": "tampered"})
    with pytest.raises(FractalExecutionError, match="selected node"):
        engine.execute("root", replace(bound, node_hash="0" * 64), payload)


def test_tree_cycles_are_rejected_before_execution():
    h1 = Handler(profile("h1", ("one",)))
    h2 = Handler(profile("h2", ("two",)))
    one = node("one", ("h1",), parent_id="two", child_ids=("two",), expandable=True)
    two = node("two", ("h2",), parent_id="one", child_ids=("one",), expandable=True)
    with pytest.raises(FractalContractError, match="cycle"):
        FractalOrchestrator([one, two], HandlerRegistry([h1, h2]))


def test_global_attempt_budget_is_shared_across_sibling_expansion():
    router = Handler(profile("router", ("root",)), HandlerStatus.NEEDS_DETAIL)
    left_h = Handler(profile("left-h", ("left",)))
    right_h = Handler(profile("right-h", ("right",)))
    root = node(
        handlers=("router",), expandable=True, child_ids=("left", "right")
    )
    left = node("left", ("left-h",), parent_id="root", minimum_vector=vector(granularity="X1"))
    right = node("right", ("right-h",), parent_id="root", minimum_vector=vector(granularity="X1"))
    engine = FractalOrchestrator(
        [root, left, right], HandlerRegistry([router, left_h, right_h])
    )
    payload = {"title": "bounded"}
    outcome = engine.execute(
        "root",
        capsule(engine, root, payload, budget=ExecutionBudget(max_attempts=2)),
        payload,
    )
    assert outcome.status is OutcomeStatus.DEFERRED
    assert router.calls == 1 and left_h.calls == 1 and right_h.calls == 0


def test_handler_below_node_maturity_or_evidence_is_not_invoked():
    weak = Handler(profile("weak", ("root",), maturity="C1", evidence="E1"))
    selected = node(
        handlers=("weak",),
        minimum_vector=vector(compilation="C2", evidence="E2"),
    )
    engine = FractalOrchestrator([selected], HandlerRegistry([weak]))
    payload = {"title": "gate"}
    outcome = engine.execute(
        "root",
        capsule(engine, selected, payload, vector=vector(compilation="C2", evidence="E2")),
        payload,
    )
    assert outcome.status is OutcomeStatus.DEFERRED
    assert outcome.attempts[0].reason == "MATURITY_BELOW_NODE_MINIMUM"
    assert weak.calls == 0

    # Even when the node minimum is lower, a stricter capsule request remains binding.
    low_node = node("low", ("low-handler",))
    low_handler = Handler(profile("low-handler", ("low",), maturity="C1", evidence="E1"))
    low_engine = FractalOrchestrator([low_node], HandlerRegistry([low_handler]))
    strict_capsule = capsule(
        low_engine,
        low_node,
        payload,
        vector=vector(compilation="C2", evidence="E2"),
    )
    strict_outcome = low_engine.execute("low", strict_capsule, payload)
    assert strict_outcome.status is OutcomeStatus.DEFERRED
    assert low_handler.calls == 0


def test_b5_world_ownership_and_unbounded_payload_are_rejected():
    with pytest.raises(FractalContractError):
        vector(brain_delegation="B5")
    with pytest.raises(FractalContractError):
        vector(granularity="X00")
    handler = Handler(profile("code", ("root",)))
    selected = node()
    engine = FractalOrchestrator([selected], HandlerRegistry([handler]))
    payload = {"text": "x" * 100}
    bound = capsule(engine, selected, payload, budget=ExecutionBudget(max_input_tokens=1))
    with pytest.raises(FractalExecutionError, match="token approximation"):
        engine.execute("root", bound, payload)
