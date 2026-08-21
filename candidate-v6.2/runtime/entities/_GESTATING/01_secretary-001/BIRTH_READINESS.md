# Birth Readiness — secretary-001 v0.4.0-rc2

## Proven locally at E2

- Mandatory R0/R1 execution binding with no silent legacy bypass.
- Versioned profile artifacts are the sole mapping source used by runtime code.
- Provenance-bearing conversation/task/price projections.
- R0 price redaction and R1 action/field dependency checks.
- Strict canonical hashing, safe patching and profile-scoped Brain negotiation
  are inherited from the RC1 Core.
- Entity-direct Telegram/Drive calls are blocked. A PDF can become only a bound,
  non-authoritative effect proposal.
- Letter/proforma artifact generation and ancestor functional behavior remain
  covered by local regression tests.
- Portable Brain Pack identity/Profile/Prompt/Schema hashes are bound and tested.
- ChatGPT/Gemini/Grok fixture outputs normalize to one semantic decision and one
  deterministic rendered reply without API/network use.
- Fractal limits, fallback invariants, Council blindness/veto, and C0..C6 Shadow
  promotion gates have local conformance tests.

## Hard gates before canonical Birth

1. Human Root explicitly ratifies the exact RC manifest hash.
2. A version-controlled source commit and signed/tagged release are recorded.
3. PostgreSQL migrations run on a fresh database and the State/Event/Command/
   Approval/Outbox atomic transaction is proven.
4. Crash injection proves no state/event/outbox partial commit and replay is safe.
5. Executor rechecks `control_epoch`, approval expiry/binding, policy decision,
   expected version and idempotency before any live adapter call.
6. Live Brain adapters declare exact per-profile hash capabilities; provider
   failover preserves identity, classification and minimum Resolution.
7. Backup/restore on a fresh machine restores canonical truth, source commit,
   profiles, compiler, lockfile/SBOM and then reproduces projections.
8. Security, credential isolation, load and chaos gates pass.
9. Only after Birth commits may a separate WAKE transaction move the Entity from
   NEWBORN/READY to NEWBORN/AWAKE.

Until every gate has evidence, this directory remains **GESTATING / NOT DEPLOYED**.
