"""Blind-then-deliberative, proposal-only multi-Brain council for RC2."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping, Sequence

from .resolution import canonical_hash


class CouncilContractError(ValueError):
    pass


class BallotPosition(str, Enum):
    SUPPORT = "SUPPORT"
    OPPOSE = "OPPOSE"
    ABSTAIN = "ABSTAIN"
    VETO = "VETO"


class CouncilOutcome(str, Enum):
    PROPOSED = "PROPOSED"
    DEFERRED = "DEFERRED"
    VETOED = "VETOED"


@dataclass(frozen=True)
class CouncilParticipant:
    participant_id: str
    role: str
    weight_millis: int = 1000
    veto_capable: bool = False

    def __post_init__(self) -> None:
        if not self.participant_id or not self.role:
            raise CouncilContractError("participant identity and role are required")
        if not isinstance(self.weight_millis, int) or not 1 <= self.weight_millis <= 10_000:
            raise CouncilContractError("participant weight outside 1..10000")
        if self.veto_capable and self.role not in {"RISK", "POLICY", "SAFETY", "COMPLIANCE"}:
            raise CouncilContractError("veto capability is restricted to risk/policy roles")


@dataclass(frozen=True)
class CouncilBallot:
    participant_id: str
    round_no: int
    context_hash: str
    proposal_hash: str
    position: BallotPosition
    confidence_millis: int
    rationale: str
    evidence_refs: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not isinstance(self.round_no, int) or self.round_no < 1:
            raise CouncilContractError("round_no must be positive")
        for digest, label in (
            (self.context_hash, "context_hash"),
            (self.proposal_hash, "proposal_hash"),
        ):
            if len(digest) != 64 or any(char not in "0123456789abcdef" for char in digest):
                raise CouncilContractError(f"{label} must be lowercase SHA-256")
        if not isinstance(self.position, BallotPosition):
            raise CouncilContractError("invalid ballot position")
        if not isinstance(self.confidence_millis, int) or not 0 <= self.confidence_millis <= 1000:
            raise CouncilContractError("confidence outside 0..1000")
        if not isinstance(self.rationale, str) or not self.rationale or len(self.rationale) > 2_000:
            raise CouncilContractError("rationale must be bounded and non-empty")

    def to_document(self) -> dict[str, object]:
        return {
            "participant_id": self.participant_id,
            "round_no": self.round_no,
            "context_hash": self.context_hash,
            "proposal_hash": self.proposal_hash,
            "position": self.position.value,
            "confidence_millis": self.confidence_millis,
            "rationale": self.rationale,
            "evidence_refs": list(self.evidence_refs),
        }


@dataclass(frozen=True)
class CouncilDecision:
    session_id: str
    outcome: CouncilOutcome
    proposal_hash: str | None
    round_count: int
    support_millis: int
    oppose_millis: int
    abstentions: int
    vetoes: tuple[str, ...]
    dissent: tuple[str, ...]
    transcript_hash: str
    proposal_only: bool = True


class CouncilSession:
    """Stateful local session; ballots are hidden until every member submits."""

    def __init__(
        self,
        session_id: str,
        context_hash: str,
        participants: Sequence[CouncilParticipant],
        *,
        max_rounds: int = 2,
        minimum_support_millis: int = 667,
        high_risk: bool = False,
    ) -> None:
        if not session_id:
            raise CouncilContractError("session_id is required")
        if len(context_hash) != 64 or any(
            char not in "0123456789abcdef" for char in context_hash
        ):
            raise CouncilContractError("context_hash must be lowercase SHA-256")
        if len(participants) < 2:
            raise CouncilContractError("a council requires at least two participants")
        ids = [item.participant_id for item in participants]
        if len(ids) != len(set(ids)):
            raise CouncilContractError("duplicate participant")
        if not 1 <= max_rounds <= 5:
            raise CouncilContractError("max_rounds outside 1..5")
        if not 501 <= minimum_support_millis <= 1000:
            raise CouncilContractError("support threshold must be a strict majority")
        self.session_id = session_id
        self.context_hash = context_hash
        self.participants = {item.participant_id: item for item in participants}
        self.max_rounds = max_rounds
        self.minimum_support_millis = minimum_support_millis
        self.high_risk = high_risk
        self.current_round = 1
        self._rounds: list[tuple[CouncilBallot, ...]] = []
        self._pending: dict[str, CouncilBallot] = {}

    def submit(self, ballot: CouncilBallot) -> None:
        if ballot.round_no != self.current_round:
            raise CouncilContractError("ballot round mismatch")
        if ballot.context_hash != self.context_hash:
            raise CouncilContractError("ballot context/state snapshot mismatch")
        if ballot.participant_id not in self.participants:
            raise CouncilContractError("unknown participant")
        if ballot.participant_id in self._pending:
            raise CouncilContractError("duplicate ballot in round")
        participant = self.participants[ballot.participant_id]
        if ballot.position is BallotPosition.VETO and not participant.veto_capable:
            raise CouncilContractError("participant has no veto capability")
        self._pending[ballot.participant_id] = ballot

    @property
    def round_complete(self) -> bool:
        return len(self._pending) == len(self.participants)

    def reveal(self) -> tuple[CouncilBallot, ...]:
        if not self.round_complete:
            raise CouncilContractError("blind ballots remain sealed until all participants submit")
        return tuple(self._pending[key] for key in sorted(self._pending))

    def advance(self) -> tuple[CouncilBallot, ...]:
        revealed = self.reveal()
        if self.current_round >= self.max_rounds:
            raise CouncilContractError("maximum deliberation rounds reached")
        self._rounds.append(revealed)
        self._pending = {}
        self.current_round += 1
        return revealed

    def finalize(self) -> CouncilDecision:
        current = self.reveal()
        rounds = (*self._rounds, current)
        latest = rounds[-1]
        vetoes = tuple(
            ballot.participant_id
            for ballot in latest
            if ballot.position is BallotPosition.VETO
        )
        # In low-risk councils a veto is still an oppose; in high-risk councils
        # a calibrated safety/compliance veto blocks the proposal.
        hard_veto = bool(vetoes and self.high_risk)
        proposals = {
            ballot.proposal_hash
            for ballot in latest
            if ballot.position in {BallotPosition.SUPPORT, BallotPosition.VETO}
        }
        proposal_hash = next(iter(proposals)) if len(proposals) == 1 else None
        support = 0
        oppose = 0
        abstentions = 0
        dissent: list[str] = []
        for ballot in latest:
            weight = self.participants[ballot.participant_id].weight_millis
            calibrated = weight * ballot.confidence_millis
            if ballot.position is BallotPosition.SUPPORT and ballot.proposal_hash == proposal_hash:
                support += calibrated
            elif ballot.position is BallotPosition.ABSTAIN:
                abstentions += 1
                dissent.append(ballot.participant_id)
            else:
                oppose += calibrated
                dissent.append(ballot.participant_id)
        total = support + oppose
        ratio = support * 1000 // total if total else 0
        if hard_veto:
            outcome = CouncilOutcome.VETOED
        elif proposal_hash is not None and ratio >= self.minimum_support_millis:
            outcome = CouncilOutcome.PROPOSED
        else:
            outcome = CouncilOutcome.DEFERRED
        transcript = {
            "session_id": self.session_id,
            "context_hash": self.context_hash,
            "participants": [
                {
                    "participant_id": participant.participant_id,
                    "role": participant.role,
                    "weight_millis": participant.weight_millis,
                    "veto_capable": participant.veto_capable,
                }
                for participant in sorted(
                    self.participants.values(), key=lambda item: item.participant_id
                )
            ],
            "rounds": [
                [ballot.to_document() for ballot in sorted(row, key=lambda item: item.participant_id)]
                for row in rounds
            ],
            "high_risk": self.high_risk,
            "minimum_support_millis": self.minimum_support_millis,
        }
        return CouncilDecision(
            session_id=self.session_id,
            outcome=outcome,
            proposal_hash=proposal_hash,
            round_count=len(rounds),
            support_millis=ratio,
            oppose_millis=1000 - ratio if total else 0,
            abstentions=abstentions,
            vetoes=vetoes,
            dissent=tuple(sorted(dissent)),
            transcript_hash=canonical_hash(transcript),
        )
