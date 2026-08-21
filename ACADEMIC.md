# World v6.2 — Academic & Research Entry Point

**Fractal Multi-Brain Architecture for durable, model-independent AI entities**

- **Author:** Saeed Farokhi
- **Release:** `6.2.0-rc.3`
- **Status:** `RATIFICATION_CANDIDATE_NOT_CANONICAL_NOT_DEPLOYED`
- **Evidence boundary:** `E2 — Local Component/Contract Evidence`
- **Version DOI:** https://doi.org/10.5281/zenodo.22040348
- **Concept DOI:** https://doi.org/10.5281/zenodo.22040347
- **Zenodo record:** https://zenodo.org/records/22040348
- **Code & evidence:** https://github.com/saeedfaai/World-v6-public

> **Research claim boundary:** World v6.2 is a candidate reference architecture and executable research prototype. It is not presented as a production-certified platform, an official standard, or evidence of autonomous personhood or consciousness.

## Abstract

World v6.2 is a ratification-candidate architecture for long-lived AI entities that separates canonical identity, truth, policy, authority, effects, memory, lifecycle, and evidence from any individual language model or provider. It uses a deterministic model-independent Mother Core with replaceable cognitive handlers, bounded fractal decomposition, resolution-aware context projection, explicit approval and effect boundaries, shadow evaluation, staged compilation, and recovery-oriented evidence gates.

The central engineering proposition is that an AI entity should remain accountable across model replacement, provider migration, workflow changes, and infrastructure failure. The model may reason, plan, classify, draft, or critique, but it does not own canonical identity, policy, authority, or history. World v6.2 therefore treats cognition as a replaceable dependency behind deterministic contracts rather than as the durable center of the entity.

The current release claims **E2 local component/contract evidence only**. It intentionally does not claim production deployment, representative database atomicity, live provider failover, fresh-machine recovery, security/load/chaos validation, or canonical ratification.

## Research question

**Can a long-lived AI entity preserve accountable continuity while its cognitive model, provider, workflow engine, and execution environment change?**

World v6.2 expresses continuity as an engineering contract rather than a session or model identity. The durable system owns identity, authority, policy, state, provenance, event history, recovery metadata, and evidence. Models remain proposal-producing handlers.

## Core architectural contributions

### 1. Entity–Brain separation

The entity remains stable while cognitive engines are replaceable. Canonical truth, memory authority, lifecycle state, policy, and effect authorization remain outside the model.

### 2. Fractal execution contract

The architecture repeats the same contract across:

`World → Entity → Mission → Skill → Workflow → Step → Tool → Field`

At every scale:

`Purpose + Input + Output + State Ref + Policy + Handler + Budget + Evidence + Fallback + Audit`

This is intended to keep the starting system small while allowing local expansion only when a task, risk, or evidence requirement justifies it.

### 3. Resolution-aware context projection

Consumers receive bounded projections of canonical state rather than unrestricted context. Up-resolution requires reloading the canonical source under fresh authority and policy checks; omitted data may not be reconstructed by model inference.

### 4. Proposal-only cognition and governed effects

The deterministic action path is:

`SENSE → INTERPRET → PROPOSE → POLICY CHECK → APPROVAL → AUTHORIZE → COMMIT → EXECUTE → OBSERVE → RECONCILE → RECORD`

Cognitive models participate in interpretation, proposal, planning, and critique. External effects are separated through explicit policy, approval, command, outbox, executor, and reconciliation boundaries.

### 5. Hot, Shadow, and Non-Extinction paths

- **Hot Path:** cheapest safe path for current work.
- **Shadow Path:** effect-free parallel execution for measurement and comparison.
- **Non-Extinction Spine:** promotion of sufficiently proven behavior into deterministic, versioned, recoverable code.

### 6. Evidence-gated maturation

Behavior does not become authoritative merely because it appears successful. Candidate behavior moves through explicit evidence stages, shadow comparison, promotion thresholds, human approval where required, rollback binding, and recovery proof.

## Evidence currently published

Current repository evidence boundary:

| Evidence item | Result |
|---|---:|
| Core RC3 tests | `78/78 PASS` |
| Secretary RC3 tests | `22/22 PASS` |
| Preserved ancestor tests | `14/14 PASS` |
| Independent test total | `114/114 PASS` |
| Architecture tests | `7/7 PASS` |
| Offline provider portability | `3/3 PASS` |
| Overall evidence level | **E2** |

The evidence package is intentionally bounded. Passing local tests is **not** treated as proof of production readiness.

## Reproducibility

Repository verification:

```bash
UV_CACHE_DIR=/tmp/world-v62-uv-cache \
UV_PROJECT_ENVIRONMENT=/tmp/world-v62-venv \
uv sync --locked --all-groups

UV_CACHE_DIR=/tmp/world-v62-uv-cache \
UV_PROJECT_ENVIRONMENT=/tmp/world-v62-venv \
uv run --locked --all-groups python tools/verify_repository.py
```

Core candidate tests:

```bash
PYTHONPATH=candidate-v6.2/runtime \
UV_CACHE_DIR=/tmp/world-v62-uv-cache \
UV_PROJECT_ENVIRONMENT=/tmp/world-v62-venv \
uv run --locked --all-groups python -m pytest -q candidate-v6.2/runtime/core/tests
```

Secretary candidate tests:

```bash
PYTHONPATH=candidate-v6.2/runtime:candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001 \
UV_CACHE_DIR=/tmp/world-v62-uv-cache \
UV_PROJECT_ENVIRONMENT=/tmp/world-v62-venv \
uv run --locked --all-groups python -m pytest -q \
candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/tests
```

Integrity references are preserved in `FILE_INVENTORY.txt` and `SHA256SUMS.txt`.

## What remains unproven

The following are explicitly open and should be treated as research/engineering work rather than completed claims:

- representative PostgreSQL atomic state/event/outbox integration;
- crash/replay/reconciliation under real failure injection;
- fresh-machine restore with measured RPO/RTO;
- live provider adapters and policy-safe failover;
- live external effects through channels such as Telegram/Drive;
- adversarial security review, prompt-injection and memory-poisoning tests;
- load, latency, cost, and chaos testing;
- multi-framework interoperability demonstrations;
- independent replication by external researchers;
- canonical ratification and production readiness.

## Related work and positioning

World v6.2 is not intended to replace established databases, workflow engines, agent frameworks, observability systems, or consensus infrastructure. Its proposed contribution is the **integration of continuity, authority, provenance, model replacement, effect governance, and recovery into one explicit contract**.

Useful comparison points include:

- **Letta / persistent-agent approaches:** persistent memory and agent state;
- **LangGraph persistence:** resumable graph/workflow execution;
- **Microsoft Agent Framework:** agent orchestration and framework abstractions;
- **Google ADK:** sessions, memory, tools, and agent development;
- **NIST AI RMF:** governance and risk-management framing;
- **CloudEvents:** interoperable event-envelope patterns;
- **W3C PROV-O:** provenance modeling;
- **OpenTelemetry:** traces, metrics, and logs;
- **Transactional Outbox / reconciliation patterns:** controlled external effects.

The research question is not whether these systems already solve valuable subproblems—they do. The differentiating hypothesis is whether a unified continuity contract can reduce measurable migration, recovery, authorization, and accountability risk across heterogeneous cognitive runtimes.

## Suggested evaluation program

External researchers are invited to challenge the architecture through:

1. **Fresh-machine recovery:** reconstruct an entity from a verified recovery bundle and compare identity/state/ledger hashes.
2. **Two-provider portability:** run the same bounded task through two real model providers while verifying policy-constrained field exposure.
3. **Failure injection:** test retries, replay, duplicate-effect prevention, and reconciliation under crashes and ambiguous network outcomes.
4. **Formal modeling:** model identity stability, authorization invariants, event ordering, and effect fencing in TLA+ or an equivalent formal method.
5. **Independent security review:** test prompt injection, memory poisoning, capability escalation, confused-deputy behavior, replay, artifact tampering, and malicious recovery inputs.
6. **Interoperability:** demonstrate the same entity manifest, policy contract, and recovery discipline across multiple agent frameworks.
7. **Bounded real pilot:** measure task value, human approval burden, correction rates, policy incidents, recovery time, operational failures, and cost per accepted artifact.

## Primary research artifacts

- [`README.md`](README.md) — architecture summary and repository entry point
- [`CITATION.cff`](CITATION.cff) — canonical citation metadata
- [`candidate-v6.2/docs/WORLD_V6_2_FRACTAL_MULTI_BRAIN_ARCHITECTURE_v1.1_FA.md`](candidate-v6.2/docs/WORLD_V6_2_FRACTAL_MULTI_BRAIN_ARCHITECTURE_v1.1_FA.md) — reference candidate architecture
- [`candidate-v6.2/docs/RESOLUTION_CABLE_MODEL_v0.2_FA.md`](candidate-v6.2/docs/RESOLUTION_CABLE_MODEL_v0.2_FA.md) — resolution/context model
- [`candidate-v6.2/docs/FRACTAL_MULTI_BRAIN_RUNTIME_v1.0_FA.md`](candidate-v6.2/docs/FRACTAL_MULTI_BRAIN_RUNTIME_v1.0_FA.md) — fractal runtime
- [`candidate-v6.2/evidence/`](candidate-v6.2/evidence/) — machine-readable evidence
- [`docs/reports/World_v6.2_ARCHITECTURE_PROOF_ROADMAP_SECRETARY_COMPLETE_FA.pdf`](docs/reports/World_v6.2_ARCHITECTURE_PROOF_ROADMAP_SECRETARY_COMPLETE_FA.pdf) — complete Persian report
- **English publication package and archived release:** https://zenodo.org/records/22040348

## Cite this work

### DOI

**Farokhi, Saeed. World v6.2 — Fractal Multi-Brain Architecture, version 6.2.0-rc.3. 2026.**  
https://doi.org/10.5281/zenodo.22040348

### BibTeX

```bibtex
@software{farokhi_world_v6_2_2026,
  author  = {Farokhi, Saeed},
  title   = {World v6.2 — Fractal Multi-Brain Architecture},
  year    = {2026},
  version = {6.2.0-rc.3},
  doi     = {10.5281/zenodo.22040348},
  url     = {https://zenodo.org/records/22040348}
}
```

For software citation tools, use [`CITATION.cff`](CITATION.cff).

## For researchers

Independent critique, replication, formal verification, security review, interoperability experiments, and comparative evaluations are welcome. Please open a GitHub Issue for public technical discussion and reference the DOI when discussing or citing the release.

For confidential commercial or strategic discussions, do **not** post deal terms in public Issues; see [`COMMERCIAL.md`](COMMERCIAL.md).

## License and rights boundary

This repository is public/source-available/non-commercial, not OSI Open Source. Original software materials are licensed for permitted noncommercial uses under PolyForm Noncommercial 1.0.0; original architecture and documentation are licensed under CC BY-NC-SA 4.0 unless a file states otherwise. Commercial use requires a separate written commercial license. See [`LICENSE`](LICENSE), [`NOTICE`](NOTICE), and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).
