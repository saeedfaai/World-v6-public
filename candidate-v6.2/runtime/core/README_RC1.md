# World Core — v6.2 Resolution-Native RC1

This directory is a deterministic reference implementation, not a deployed
authority service.

## Modules

- `resolution.py`: strict World Canonical JSON v1, version/hash-bound profiles,
  deterministic projections, provider-safe envelopes, action dependencies and
  bounded existing-scalar patches.
- `brain_gateway.py`: multi-segment, per-profile capability negotiation. A
  provider receives projected envelopes only.
- `effects.py`: immutable effect proposal and exact Human Root ApprovalBinding;
  it prepares but does not commit an Outbox intent.
- `kernel.py`: minimal transaction coordinator reference and patch-validation
  hook. Resolution validation grants no authority.
- `postgres_schema.sql`: Phase-1 target tables for World, Entity, Event, Command,
  Approval and Outbox.

## Non-negotiable boundary

The only permitted external-effect path is deterministic Policy -> exact bound
approval -> one PostgreSQL transaction -> committed Outbox -> registered
Executor -> adapter -> outcome/reconciliation Event. Entity private code and
Brain output cannot call adapters.

## Claim boundary

Local tests are E2 evidence. PostgreSQL integration, crash/replay, live provider
and adapter behavior, recovery, security/load/chaos and Canonical ratification
remain separate blocking gates.
