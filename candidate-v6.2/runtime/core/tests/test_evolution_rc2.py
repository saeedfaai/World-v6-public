from __future__ import annotations

import pytest

from core.evolution import (
    CompilationMaturity,
    EvolutionContractError,
    PromotionController,
    PromotionThreshold,
    ShadowRunRecord,
)


H = "a" * 64
MATCH = "b" * 64
DIFF = "c" * 64


def record(index, *, match=True, invariant=0, effect=0, replay=True, candidate_hash=H):
    return ShadowRunRecord(
        run_id=f"run-{index}",
        candidate_id="candidate",
        candidate_version="1.0.0",
        candidate_hash=candidate_hash,
        node_id="secretary.route",
        input_hash=f"{index:064x}",
        primary_semantic_hash=MATCH,
        candidate_semantic_hash=MATCH if match else DIFF,
        invariant_failures=invariant,
        forbidden_effect_attempts=effect,
        replay_match=replay,
    )


def controller():
    return PromotionController({
        CompilationMaturity.C1: PromotionThreshold(1, 0),
        CompilationMaturity.C2: PromotionThreshold(3, 666),
        CompilationMaturity.C3: PromotionThreshold(3, 900),
        CompilationMaturity.C4: PromotionThreshold(3, 900),
        CompilationMaturity.C5: PromotionThreshold(3, 900, True, True),
        CompilationMaturity.C6: PromotionThreshold(3, 900, True, True, True),
    })


def assess(current, rows, **kwargs):
    return controller().assess(
        candidate_id="candidate",
        candidate_version="1.0.0",
        candidate_hash=H,
        current=current,
        records=rows,
        **kwargs,
    )


def test_promotion_is_one_step_and_evidence_gated():
    result = assess(CompilationMaturity.C1, [record(1), record(2), record(3, match=False)])
    assert result.target_maturity == "C2"
    assert result.eligible
    assert result.agreement_millis == 666 or result.agreement_millis == 667
    assert result.recommendation_only


def test_invariant_effect_and_replay_failures_each_block_promotion():
    rows = [record(1), record(2), record(3, invariant=1, effect=1, replay=False)]
    result = assess(CompilationMaturity.C2, rows)
    assert not result.eligible
    assert {"INVARIANT_FAILURE", "FORBIDDEN_EFFECT_ATTEMPT", "NONDETERMINISTIC_REPLAY"} <= set(result.reasons)


def test_primary_and_non_extinction_promotions_require_root_and_restore_proof():
    rows = [record(1), record(2), record(3)]
    c5 = assess(CompilationMaturity.C4, rows)
    assert c5.reasons == ("HUMAN_ROOT_APPROVAL_REQUIRED",)
    c5_ok = assess(CompilationMaturity.C4, rows, human_root_approval_ref="approval:root-1")
    assert c5_ok.eligible and c5_ok.target_maturity == "C5"
    c6 = assess(CompilationMaturity.C5, rows, human_root_approval_ref="approval:root-2")
    assert c6.reasons == ("RESTORE_PROOF_REQUIRED",)
    c6_ok = assess(
        CompilationMaturity.C5,
        rows,
        human_root_approval_ref="approval:root-2",
        restore_proof_ref="restore:drill-1",
    )
    assert c6_ok.eligible and c6_ok.target_maturity == "C6"


def test_mixed_candidate_evidence_and_promotion_beyond_c6_are_forbidden():
    with pytest.raises(EvolutionContractError, match="mixed"):
        assess(CompilationMaturity.C1, [record(1), record(2, candidate_hash="d" * 64)])
    with pytest.raises(EvolutionContractError, match="terminal"):
        assess(CompilationMaturity.C6, [record(1)])
    with pytest.raises(EvolutionContractError, match="duplicate Shadow"):
        assess(CompilationMaturity.C1, [record(1), record(1)])
