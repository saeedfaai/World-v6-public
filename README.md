# World v6.2 — Fractal Multi-Brain Architecture RC3

**Version:** `6.2.0-rc.3`  
**Status:** `RATIFICATION_CANDIDATE_NOT_CANONICAL_NOT_DEPLOYED`  
**Evidence:** `E2 — Local Component/Contract Evidence`  
**Author:** Saeed Farokhi  
**Repository:** `saeedfaai/world-v6`

> World v6.2 is a model-independent architecture in which identity, canonical truth,
> policy, authority, effects, memory, and lifecycle remain outside any individual AI
> model or provider. AI systems act as replaceable proposal-producing cognitive
> handlers behind deterministic contracts and governance boundaries.

`Secretary-001` remains **GESTATING / PRE-BIRTH / NOT DEPLOYED**. Files do not create
or activate an entity. Birth requires the defined Birth Gate, real operational truth
and event infrastructure, exact Human Root approval, and the required evidence.

## Architecture in one sentence

**Entity remains stable; Brain is replaceable; Context is compiled at bounded
Resolution; complexity expands locally and fractally; authority remains outside
cognition; external effects are policy-bound and reconcilable; proven behavior can
mature through Shadow evidence into deterministic, recoverable code.**

The architecture follows the fractal path:

`World → Entity → Mission → Skill → Workflow → Step → Tool → Field`

At every scale, the same base contract repeats:

`Purpose + Input + Output + State Ref + Policy + Handler + Budget + Evidence + Fallback + Audit`

## Core planes

World v6.2 separates seven planes so that a failure in cognition cannot silently
become truth or authority:

1. **Governance** — Root Constitution, Policy, Approval, Kill Switch.
2. **Truth** — Registry, State, Event Ledger, Artifact Index.
3. **Control** — World API, deterministic Kernel, Scheduler, Queue, Lifecycle.
4. **Cognition** — Brain Gateway, Router, model adapters, Council; proposal-only.
5. **Effect** — Command, Transactional Outbox, Executor, Reconciler.
6. **Evolution** — Shadow evaluation, compiler, promotion controls; no self-deploy.
7. **Observability** — traces, metrics, logs, evidence records.

## Non-negotiable invariants

- `Human Root` is the highest authority and cannot be replaced by a model.
- Provider, model, channel, session, and workflow are not identity.
- Brain output is a proposal; Kernel and policy determine permission; Executor performs effects.
- Canonical state is never reconstructed from a lower-resolution projection.
- Up-resolution requires reload from the canonical source.
- Availability cannot weaken classification, residency, retention, legal basis, approval, or minimum evidence.
- Stable artifacts are versioned rather than silently rewritten.
- Council consensus does not create authority.
- Shadow execution has no authoritative user-facing or external effect.
- Self-mutation may create candidates, never deploy them directly.
- A backup is not survival evidence until a restore drill succeeds.

## Start here

### Reference Persian architecture

The current reference architecture language is Persian. The normative identifiers,
schemas, state names, APIs, hashes, and contracts remain language-neutral.

1. [`README_FA.md`](README_FA.md)
2. [`docs/IMPLEMENTATION_INDEX_FA.md`](docs/IMPLEMENTATION_INDEX_FA.md)
3. [`candidate-v6.2/docs/WORLD_V6_2_FRACTAL_MULTI_BRAIN_ARCHITECTURE_v1.1_FA.md`](candidate-v6.2/docs/WORLD_V6_2_FRACTAL_MULTI_BRAIN_ARCHITECTURE_v1.1_FA.md)
4. [`candidate-v6.2/docs/RESOLUTION_CABLE_MODEL_v0.2_FA.md`](candidate-v6.2/docs/RESOLUTION_CABLE_MODEL_v0.2_FA.md)
5. [`candidate-v6.2/docs/FRACTAL_MULTI_BRAIN_RUNTIME_v1.0_FA.md`](candidate-v6.2/docs/FRACTAL_MULTI_BRAIN_RUNTIME_v1.0_FA.md)
6. [`candidate-v6.2/architecture/ARCHITECTURE_MANIFEST_v1.1.0-rc3.json`](candidate-v6.2/architecture/ARCHITECTURE_MANIFEST_v1.1.0-rc3.json)
7. [`candidate-v6.2/docs/IMPLEMENTATION_PLAN_PHASE1_FA.md`](candidate-v6.2/docs/IMPLEMENTATION_PLAN_PHASE1_FA.md)
8. [`candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/README.md`](candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/README.md)

The complete Persian architecture/proof/roadmap/secretary report is preserved under
`docs/reports/`.

### Publication controls

Before public release, read:

- [`LICENSE`](LICENSE)
- [`NOTICE`](NOTICE)
- [`CITATION.cff`](CITATION.cff)
- [`SECURITY.md`](SECURITY.md)
- [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)
- [`PUBLICATION_GATES.md`](PUBLICATION_GATES.md)

This repository is intended as **public/source-available/non-commercial**, not OSI Open Source. Original World v6 software materials are licensed for permitted noncommercial uses under **PolyForm Noncommercial 1.0.0**; original World v6 documentation and architecture materials are licensed under **CC BY-NC-SA 4.0**, unless a file states otherwise. **Commercial use requires a separate written commercial license from Saeed Farokhi.** Patent rights are not granted beyond any limited patent license expressly contained in the PolyForm terms for permitted noncommercial software uses.

## Repository structure

- `canonical-baseline/` — preserved canonical documents; no direct mutation.
- `candidate-v6.2/` — candidate architecture, contracts, profiles, schemas, runtime, and growing entity.
- `candidate-v6.2/runtime/core/` — deterministic Mother Core, independent of provider.
- `candidate-v6.2/runtime/adapters/` — transport/effect boundary outside the Entity.
- `candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/` — secretary before Birth.
- `candidate-v6.2/brain-packs/secretary-001/` — portable behavior and provider overlays.
- `candidate-v6.2/fractal/` — nodes, handlers, councils, and maturity artifacts.
- `candidate-v6.2/evidence/` — raw tests and machine-readable evidence.
- `source-ancestor/` — preserved ancestor for regression and rollback.
- `research/` and `legacy-reference/` — non-canonical references; publication rights must be separately cleared.
- `tools/` — build, verification, and Universal Model Bridge tooling.
- `FILE_INVENTORY.txt` and `SHA256SUMS.txt` — deterministic inventory and integrity chain.

## Reproducible local verification

```bash
UV_CACHE_DIR=/tmp/world-v62-uv-cache \
UV_PROJECT_ENVIRONMENT=/tmp/world-v62-venv \
uv sync --locked --all-groups

UV_CACHE_DIR=/tmp/world-v62-uv-cache \
UV_PROJECT_ENVIRONMENT=/tmp/world-v62-venv \
uv run --locked --all-groups python tools/verify_repository.py
```

Candidate tests:

```bash
PYTHONPATH=candidate-v6.2/runtime \
UV_CACHE_DIR=/tmp/world-v62-uv-cache \
UV_PROJECT_ENVIRONMENT=/tmp/world-v62-venv \
uv run --locked --all-groups python -m pytest -q candidate-v6.2/runtime/core/tests

PYTHONPATH=candidate-v6.2/runtime:candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001 \
UV_CACHE_DIR=/tmp/world-v62-uv-cache \
UV_PROJECT_ENVIRONMENT=/tmp/world-v62-venv \
uv run --locked --all-groups python -m pytest -q \
candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/tests
```

## Universal manual model path

Any model capable of reading a self-contained JSON package and returning JSON that
conforms to `secretary-decision.schema.json` can be used through the manual host path
without changing Entity identity or DNA:

```bash
python tools/universal_model_bridge.py export-task \
  --task-json candidate-v6.2/brain-packs/secretary-001/examples/task-input.example.json \
  --provider-label any-conforming-model > portable-model-bundle.json

python tools/universal_model_bridge.py validate-bundle \
  --bundle-json portable-model-bundle.json
```

Model output remains a proposal and must pass schema validation, policy, approval when
required, and the effect boundary before it can alter state or create an external effect.

## Current evidence boundary

- Core RC3: `78/78 PASS`
- Secretary RC3: `22/22 PASS`
- Preserved ancestor: `14/14 PASS`
- Independent total: `114/114 PASS`
- Architecture tests: `7/7 PASS`
- Offline provider portability: `3/3 PASS`
- Current evidence level: `E2`

The following remain explicitly unproven/open: PostgreSQL atomic integration,
crash/replay/reconciliation, fresh-machine restore, live provider adapters, live
Telegram/Drive effects, security/load/chaos, canonical ratification, and production
readiness.

## Citation

Use [`CITATION.cff`](CITATION.cff). A version DOI will be added after the first cleared
public GitHub pre-release is archived through Zenodo.
