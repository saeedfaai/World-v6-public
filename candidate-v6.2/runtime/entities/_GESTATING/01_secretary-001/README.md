# secretary-001 v0.4.0-rc2 — Fractal Multi-Brain Ratification Candidate

Status: **PRE-BIRTH / NOT DEPLOYED / NOT CANONICAL**. The unchanged v0.1.3
ancestor remains beside this candidate.

## RC2 behavior

- Runtime Resolution is mandatory. The silent `None`/legacy bypass is removed.
- Conversation, task and price views always return a provenance-bearing consumer
  envelope; a raw projection is never handed to a Brain without profile,
  canonical, projection and compiler hashes.
- Profiles are loaded from the versioned JSON artifacts under `candidate-v6.2/profiles`.
  Python no longer carries a second hard-coded copy.
- R0 price never contains exact amount or approval wires. Price/proforma actions
  require R1 and the declared action-dependent fields.
- Entity code cannot call Telegram or Drive. It may prepare a deterministic,
  non-authoritative external-effect proposal at R1. The canonical path must then
  bind an exact Human Root approval and commit Command/Event/Outbox atomically
  before a registered Executor performs I/O.
- `root_approved: bool` has no authority and cannot be used as an approval token.
- Letter rendering discovers either `libreoffice` or `soffice` and isolates the
  runtime profile; the system binary/image remains a deployment dependency.
- `PortableSecretaryService` reads the same canonical Store and builds an exact
  profile/hash-bound request for any compatible Brain.
- ChatGPT, Gemini, Grok, Local and Code share one Portable Brain Pack and one
  strict Secretary Decision contract; no provider owns identity or state.
- Standard replies are rendered from deterministic templates, so supported
  Provider fixtures produce the exact same user-facing answer.
- Runtime network and API tokens remain disabled; the Manual Host path works by
  exporting/importing strict JSON.
- Fractal expansion, Council and Shadow evolution are bounded and proposal-only.

## Claim boundary

The included tests establish deterministic E2 component behavior only. They do
not prove PostgreSQL transactionality, crash/replay, live Telegram/Drive/provider
behavior, fresh restore, security, load/chaos, production readiness or Human
Root ratification.
