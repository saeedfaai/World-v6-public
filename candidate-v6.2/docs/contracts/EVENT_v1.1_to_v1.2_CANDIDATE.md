# Event Schema v1.2 Candidate Overlay
Relevant command/proposal/policy/action payloads carry profile id/version/hash,
compiler id/version/hash, source/version, desired/minimum/effective Resolution,
canonical/projection hashes, purpose/class/freshness and derived/non-authoritative
flags. Event Ledger stays append-only; external effect success still requires
Executor result/reconciliation. Projection metadata cannot substitute for an
exact approval/effect hash.
