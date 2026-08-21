"""Shadow evolution and compilation-maturity gates for World v6.2 RC2.

Generated or model-derived logic may learn beside the active path, but this
module can only recommend a one-step promotion.  It cannot rewrite code,
change DNA, deploy, or grant authority.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable

from .resolution import canonical_hash


class EvolutionContractError(ValueError):
    pass


class CompilationMaturity(str, Enum):
    C0 = "C0"  # prompt/manual only
    C1 = "C1"  # captured fixture/trace
    C2 = "C2"  # executable candidate
    C3 = "C3"  # shadow-equivalent
    C4 = "C4"  # bounded canary eligible
    C5 = "C5"  # approved primary eligible
    C6 = "C6"  # restore-proven non-extinction spine

    @property
    def rank(self) -> int:
        return int(self.value[1:])

    def next(self) -> "CompilationMaturity | None":
        if self is CompilationMaturity.C6:
            return None
        return CompilationMaturity(f"C{self.rank + 1}")


@dataclass(frozen=True)
class ShadowRunRecord:
    run_id: str
    candidate_id: str
    candidate_version: str
    candidate_hash: str
    node_id: str
    input_hash: str
    primary_semantic_hash: str
    candidate_semantic_hash: str
    invariant_failures: int = 0
    forbidden_effect_attempts: int = 0
    replay_match: bool = True
    latency_ms: int = 0
    estimated_cost_micros: int = 0

    def __post_init__(self) -> None:
        for digest in (
            self.candidate_hash,
            self.input_hash,
            self.primary_semantic_hash,
            self.candidate_semantic_hash,
        ):
            if len(digest) != 64 or any(char not in "0123456789abcdef" for char in digest):
                raise EvolutionContractError("Shadow hashes must be lowercase SHA-256")
        for value in (
            self.invariant_failures,
            self.forbidden_effect_attempts,
            self.latency_ms,
            self.estimated_cost_micros,
        ):
            if not isinstance(value, int) or value < 0:
                raise EvolutionContractError("Shadow metrics must be non-negative integers")

    @property
    def semantic_match(self) -> bool:
        return self.primary_semantic_hash == self.candidate_semantic_hash

    def to_document(self) -> dict[str, object]:
        return {
            "run_id": self.run_id,
            "candidate_id": self.candidate_id,
            "candidate_version": self.candidate_version,
            "candidate_hash": self.candidate_hash,
            "node_id": self.node_id,
            "input_hash": self.input_hash,
            "primary_semantic_hash": self.primary_semantic_hash,
            "candidate_semantic_hash": self.candidate_semantic_hash,
            "semantic_match": self.semantic_match,
            "invariant_failures": self.invariant_failures,
            "forbidden_effect_attempts": self.forbidden_effect_attempts,
            "replay_match": self.replay_match,
            "latency_ms": self.latency_ms,
            "estimated_cost_micros": self.estimated_cost_micros,
        }


@dataclass(frozen=True)
class PromotionThreshold:
    minimum_runs: int
    minimum_agreement_millis: int
    require_all_replays: bool = True
    human_root_approval_required: bool = False
    restore_proof_required: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.minimum_runs, int) or self.minimum_runs < 1:
            raise EvolutionContractError("minimum_runs must be a positive integer")
        if (
            not isinstance(self.minimum_agreement_millis, int)
            or not 0 <= self.minimum_agreement_millis <= 1000
        ):
            raise EvolutionContractError("agreement threshold outside 0..1000")


DEFAULT_THRESHOLDS: dict[CompilationMaturity, PromotionThreshold] = {
    CompilationMaturity.C1: PromotionThreshold(1, 0),
    CompilationMaturity.C2: PromotionThreshold(5, 600),
    CompilationMaturity.C3: PromotionThreshold(20, 850),
    CompilationMaturity.C4: PromotionThreshold(50, 930),
    CompilationMaturity.C5: PromotionThreshold(100, 970, True, True),
    CompilationMaturity.C6: PromotionThreshold(200, 990, True, True, True),
}


@dataclass(frozen=True)
class PromotionAssessment:
    candidate_id: str
    candidate_version: str
    candidate_hash: str
    from_maturity: str
    target_maturity: str
    eligible: bool
    reasons: tuple[str, ...]
    run_count: int
    agreement_millis: int
    evidence_hash: str
    recommendation_only: bool = True


class PromotionController:
    def __init__(
        self,
        thresholds: dict[CompilationMaturity, PromotionThreshold] | None = None,
    ) -> None:
        self.thresholds = dict(thresholds or DEFAULT_THRESHOLDS)
        required = set(CompilationMaturity) - {CompilationMaturity.C0}
        if set(self.thresholds) != required:
            raise EvolutionContractError("thresholds must define exact targets C1..C6")

    def assess(
        self,
        *,
        candidate_id: str,
        candidate_version: str,
        candidate_hash: str,
        current: CompilationMaturity,
        records: Iterable[ShadowRunRecord],
        human_root_approval_ref: str | None = None,
        restore_proof_ref: str | None = None,
    ) -> PromotionAssessment:
        target = current.next()
        if target is None:
            raise EvolutionContractError("C6 is terminal; create a new candidate version")
        selected = tuple(records)
        reasons: list[str] = []
        if not selected:
            reasons.append("NO_SHADOW_EVIDENCE")
        for record in selected:
            if (
                record.candidate_id != candidate_id
                or record.candidate_version != candidate_version
                or record.candidate_hash != candidate_hash
            ):
                raise EvolutionContractError("mixed candidate evidence is forbidden")
        run_ids = [record.run_id for record in selected]
        if len(run_ids) != len(set(run_ids)):
            raise EvolutionContractError("duplicate Shadow run_id is forbidden")
        threshold = self.thresholds[target]
        matches = sum(record.semantic_match for record in selected)
        agreement = (matches * 1000 // len(selected)) if selected else 0
        if len(selected) < threshold.minimum_runs:
            reasons.append("INSUFFICIENT_RUNS")
        if agreement < threshold.minimum_agreement_millis:
            reasons.append("AGREEMENT_BELOW_THRESHOLD")
        if any(record.invariant_failures for record in selected):
            reasons.append("INVARIANT_FAILURE")
        if any(record.forbidden_effect_attempts for record in selected):
            reasons.append("FORBIDDEN_EFFECT_ATTEMPT")
        if threshold.require_all_replays and any(not record.replay_match for record in selected):
            reasons.append("NONDETERMINISTIC_REPLAY")
        if threshold.human_root_approval_required and not human_root_approval_ref:
            reasons.append("HUMAN_ROOT_APPROVAL_REQUIRED")
        if threshold.restore_proof_required and not restore_proof_ref:
            reasons.append("RESTORE_PROOF_REQUIRED")
        evidence_document = {
            "candidate_id": candidate_id,
            "candidate_version": candidate_version,
            "candidate_hash": candidate_hash,
            "from_maturity": current.value,
            "target_maturity": target.value,
            "records": [record.to_document() for record in selected],
            "human_root_approval_ref": human_root_approval_ref,
            "restore_proof_ref": restore_proof_ref,
        }
        return PromotionAssessment(
            candidate_id=candidate_id,
            candidate_version=candidate_version,
            candidate_hash=candidate_hash,
            from_maturity=current.value,
            target_maturity=target.value,
            eligible=not reasons,
            reasons=tuple(reasons),
            run_count=len(selected),
            agreement_millis=agreement,
            evidence_hash=canonical_hash(evidence_document),
        )
