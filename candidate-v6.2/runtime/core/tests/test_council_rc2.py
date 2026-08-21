from __future__ import annotations

import pytest

from core.council import (
    BallotPosition,
    CouncilBallot,
    CouncilContractError,
    CouncilOutcome,
    CouncilParticipant,
    CouncilSession,
)


PROPOSAL = "a" * 64
OTHER = "b" * 64
CONTEXT = "c" * 64


def participants():
    return (
        CouncilParticipant("domain", "DOMAIN", 1000),
        CouncilParticipant("risk", "RISK", 1200, True),
        CouncilParticipant("policy", "POLICY", 1200, True),
    )


def ballot(who, round_no=1, position=BallotPosition.SUPPORT, proposal=PROPOSAL, confidence=900):
    return CouncilBallot(who, round_no, CONTEXT, proposal, position, confidence, f"reason-{who}")


def test_first_round_is_blind_until_every_participant_submits():
    session = CouncilSession("council-1", CONTEXT, participants())
    session.submit(ballot("domain"))
    with pytest.raises(CouncilContractError, match="sealed"):
        session.reveal()
    session.submit(ballot("risk"))
    session.submit(ballot("policy"))
    assert [item.participant_id for item in session.reveal()] == ["domain", "policy", "risk"]


def test_revision_round_can_reach_a_proposal_but_never_an_execution():
    session = CouncilSession("council-2", CONTEXT, participants(), max_rounds=2, minimum_support_millis=700)
    session.submit(ballot("domain"))
    session.submit(ballot("risk", position=BallotPosition.OPPOSE))
    session.submit(ballot("policy", position=BallotPosition.ABSTAIN))
    first = session.advance()
    assert len(first) == 3
    for who in ("domain", "risk", "policy"):
        session.submit(ballot(who, round_no=2))
    decision = session.finalize()
    assert decision.outcome is CouncilOutcome.PROPOSED
    assert decision.proposal_hash == PROPOSAL
    assert decision.round_count == 2
    assert decision.proposal_only is True


def test_high_risk_safety_veto_blocks_even_majority_support():
    session = CouncilSession("council-3", CONTEXT, participants(), high_risk=True)
    session.submit(ballot("domain"))
    session.submit(ballot("policy"))
    session.submit(ballot("risk", position=BallotPosition.VETO))
    decision = session.finalize()
    assert decision.outcome is CouncilOutcome.VETOED
    assert decision.vetoes == ("risk",)


def test_unqualified_veto_duplicate_vote_and_conflicting_proposals_fail_closed():
    session = CouncilSession("council-4", CONTEXT, participants())
    with pytest.raises(CouncilContractError, match="no veto"):
        session.submit(ballot("domain", position=BallotPosition.VETO))
    session.submit(ballot("domain"))
    with pytest.raises(CouncilContractError, match="duplicate"):
        session.submit(ballot("domain"))
    session.submit(ballot("risk", proposal=OTHER))
    session.submit(ballot("policy"))
    assert session.finalize().outcome is CouncilOutcome.DEFERRED

    mismatched = CouncilSession("council-5", CONTEXT, participants())
    wrong_context = CouncilBallot(
        "domain", 1, "d" * 64, PROPOSAL, BallotPosition.SUPPORT, 900, "wrong-state"
    )
    with pytest.raises(CouncilContractError, match="snapshot mismatch"):
        mismatched.submit(wrong_context)


def test_transcript_hash_is_independent_of_submission_order():
    hashes = []
    for order in (("domain", "risk", "policy"), ("policy", "domain", "risk")):
        session = CouncilSession("same-session", CONTEXT, participants(), max_rounds=1)
        for who in order:
            session.submit(ballot(who))
        hashes.append(session.finalize().transcript_hash)
    assert hashes[0] == hashes[1]
