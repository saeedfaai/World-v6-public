# W8-P01 Public Reviewer Package v0.1

Status: **PUBLIC REPRODUCTION PASS / READY FOR FREEZE REF / NO LIVE EFFECTS**

Paper:
**A Governed Shared-Kernel Architecture for Persistent, Auditable Multi-Agent Societies Beyond the LLM Session**

This is the narrow public reviewer-facing reproduction package for W8-P01. It exists so reviewers do not need access to the private World 8 engineering repository to reproduce the manuscript's principal synthetic/reference and external-runtime evidence.

## Evidence lineage

Private canonical evidence commit:
`34ed68b6e04c548e7ee14aa16e0e3eecdb1b31f0`

Private evidence freeze:
`freeze/w8-p01-evidence-v0.1`

Public executable-source commit that was tested:
`a0b2cf32915c9d63cca0ddd7c3eeb497ae8ce6d0`

Public reproduction run:
https://github.com/saeedfaai/World-v6-public/actions/runs/33113474577

Result: **SUCCESS**

Artifact:
`w8-p01-public-review-package-v0.1`

Artifact digest:
`sha256:46e15a72c59c5e6035e0732590941f20d1ed7c44b7870b8d54002c790efe166c`

Manifest:
`MANIFEST.json`

Final public freeze ref:
`freeze/w8-p01-review-package-v0.1`

## What the single public gate reproduces

### E1 — hardened reference baseline
- 98,000 deterministic trials.
- exact frozen valid-path check/evidence counts are asserted.
- revoke/CAS/durable-idempotency cases are asserted to be handled by the hardened baseline.
- the frozen actor-theft, no-fence, tamper and runtime-identity-continuity differentiators are asserted rather than inferred.

### E2 — shared-kernel cross-Society conformance
- Company: 1,000 trials.
- Trading: 1,000 trials.
- same eight-invariant suite and same kernel.
- all frozen pass rates = 1.0.
- `market_performance_evaluated=false`.
- `live_effects=false`.

### E4 — mutation and compound faults
- 5/5 controlled reference-model mutations killed.
- mutation score = 1.0.
- three compound cases × 1,000 trials.
- frozen valid-path false-deny rate = 0.0.
- production/runtime database is not destructively mutation-tested.

### E5 — independent AutoGen Core runtime
- pinned `autogen-core==0.7.5`.
- the public fixture is materialized from exact source commit `ba9fe95cc41b02bd04962d6e38b1b6afdeefe26a`.
- real `SingleThreadedAgentRuntime`, `AgentId`, and `RoutedAgent` execution.
- 2,000 deterministic cases.
- no LLM/API key.
- no external effects.
- the hardened generic layer passes the frozen revoke/CAS/idempotency families.
- the frozen stolen-approval, stale-fence, tamper and effect-before-recovery families remain exposed in that hardened variant.
- the World-8-style governance composition closes the frozen four families with zero false denials on the frozen valid paths.

## Included source

`reference/` contains the synthetic/reference E1/E2/E4 source required by the public gate. The E5 fixture is not copied by hand: CI materializes it from its exact prior public Git commit, preserving source lineage and avoiding silent duplication.

## Explicit exclusions

This package contains no:
- credentials, API keys, tokens or secrets;
- private Supabase/project identifiers or operational database rows;
- customer, supplier or private business data;
- credential-broker internals;
- live trading;
- live provider or external business effects;
- private engineering-control-plane state not needed to reproduce the manuscript evidence.

## Claim ceiling

This package supports only the frozen, bounded W8-P01 claims. It does **not** establish production readiness, profitability, universal security, universal domain generality, or general superiority over AutoGen/LangGraph/OpenAI Agents SDK. It also does not claim standalone novelty for persistent/provider-independent identity, MAS governance/norms, authorization, leases/fencing, CAS, idempotency, recovery, hash chains/provenance, tracing or orchestration.

The evaluated contribution is the tested **effect-governance composition + contract boundary + falsification evidence**.

## Reproduce

The canonical reproduction recipe is the workflow:
`.github/workflows/w8-p01-public-review-package-v0.1.yml`

It pins Python 3.12 and AutoGen Core 0.7.5, executes all public gates, validates the bounded frozen outcomes, hashes the source/results and uploads a receipt artifact.

## Archival status

The Git freeze ref is the reviewer-stable code reference. A DOI/archive snapshot may be added before final journal submission; absence of that DOI must not be represented as if already archived.
