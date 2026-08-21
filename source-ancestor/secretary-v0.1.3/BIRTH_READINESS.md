# Birth Readiness - secretary-001 v0.1.0

## Ready in this package
- Identity/version/owner/autonomy manifest.
- Formal letter renderer using the supplied FALAT PARS letterhead PowerPoint as the visual/font/layout reference.
- Simple Persian proforma PDF renderer.
- Task model.
- Customer-specific approved-price lookup; missing/expired/unapproved price creates a Human Root inquiry.
- ChatGPT/Telegram normalized channel contract plus Secretary-local Telegram transport configuration from Secret Store/environment only.
- L0 policy rules.
- PostgreSQL target DDL for Secretary domain tables.
- Minimal world Core source for canonical PostgreSQL authority schema, atomic Birth/WAKE transaction primitives, and provider-neutral Brain Gateway.
- Tests: 6 PASS (task, missing price escalation, known price proforma, official letter PDF, Telegram source verification, Root price inquiry message).
- PDF evidence visually inspected.

## Hard gates still required for CANONICAL BIRTH
- A real PostgreSQL runtime is deployed and the canonical Core schema/migrations are applied.
- The atomic Birth transaction is executed against that PostgreSQL runtime and committed evidence is captured.
- Telegram bot token + Root Telegram user id are connected from approved Secret Store/environment and the bot transport is actually running.
- Brain Gateway has at least one compatible live provider. A second provider is not required to call the Entity born, but is required before a failover-resilience claim.
- Birth transaction finalizes created_at + creation_event_ref + DNA hash and creates Registry state NEWBORN/READY.
- Separate WAKE transaction makes it NEWBORN/AWAKE.

Until these gates pass, this source package is a tested GESTATING candidate and must not be presented as a canonical born Entity.
