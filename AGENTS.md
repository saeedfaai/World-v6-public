# Repository Instructions

## Constitutional rules

- Human Root is the highest authority and cannot be delegated or replaced.
- Treat files marked `FROZEN`, `NORMATIVE`, or `STABLE` as immutable. Create a new version
  instead of editing them in place.
- Never enable external effects from the Phase 0 kernel.
- Never add secrets, credentials, tokens, private keys, or raw confidential payloads to code,
  prompts, logs, events, fixtures, or commits.
- Every permission must be scoped, purposeful, time-bound, revocable, and auditable.
- Preserve append-only history. Corrections require compensating events, not rewriting history.
- A backup is not verified until a recorded restore drill passes.
- Do not claim Production readiness below E4 evidence.

## Change requirements

- Keep JSON deterministic and UTF-8 encoded.
- Run `python3 scripts/verify_integrity.py --strict` and the unit tests before proposing a merge.
- Any stable contract change requires a version bump, migration, rollback, tests, Human Root
  approval, and updated SHA-256 manifests.
- Prefer fail-safe behavior and least privilege when requirements conflict.

