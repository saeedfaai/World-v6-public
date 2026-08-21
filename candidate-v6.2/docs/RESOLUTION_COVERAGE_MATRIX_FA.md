# World v6.2 Resolution-Native Coverage Matrix

| لایه | وضعیت v6.2 RC1 | تصمیم |
|---|---|---|
| Root Constitution | NO CHANGE | Brain != Entity، fail-closed و action path همان canonical v1.0 |
| Entity DNA | OVERLAY | top-level جدید ندارد؛ Resolution داخل slotهای موجود |
| Registry | OVERLAY / NO DB COLUMN | execution/profile در state/config pointer؛ Registry truth حفظ |
| Event Ledger | OVERLAY | metadata در payload؛ Ledger موازی ممنوع |
| Audit | OVERLAY | profile/compiler/canonical/projection hash، source version و effective resolution قابل trace |
| Policy Gate | CODE + OVERLAY | minimum + action-required wires داخل Policy؛ authority تغییر نمی‌کند |
| Kernel API | CODE HOOK + OVERLAY | version/source/profile/projection-hash-guarded scalar patch؛ no new authority stage |
| Brain Gateway | IMPLEMENTED RC1 | projection واقعی ورودی و per-profile segment vector؛ no policy downgrade |
| Context Compiler | IMPLEMENTED CORE PRIMITIVE | deterministic projection؛ semantic agent فعلاً خارج Core |
| Memory | RULED | raw/canonical حفظ؛ low-res summary مشتق و non-authoritative |
| Knowledge | RULED | low-res knowledge provenance/freshness را حفظ می‌کند |
| Skills | CONTRACT RULE | skill/action می‌تواند minimum/desired resolution اعلام کند |
| Workflows | CONTRACT RULE | backbone R0؛ stepها minimum مستقل |
| Scheduler/Economics | RULED | کمترین resolution مجاز برای کاهش cost، بعد از hard constraints |
| Inter-Entity | OVERLAY | additive envelope extension؛ dual auth حفظ |
| Relationships | RULED | summary authority نمی‌سازد؛ canonical contract برای policy |
| External Effects | HARD BOUNDARY + TEST | Entity-direct I/O ممنوع؛ coarse proposal کافی برای اجرا نیست |
| Approval | EXACT BINDING IMPLEMENTED | command/action/recipient/payload/effect/version/epoch/expiry همگی bind |
| Outbox/Executor | PREPARATION IMPLEMENTED / DB OPEN | intent/outcome جدا؛ commit و live Executor هنوز promotion blocker |
| State | RULED | canonical state full fidelity؛ operational view مشتق |
| Versioning | CLARIFIED | Resolution downgrade != Version rollback |
| Migration | NO RESOLUTION-SPECIFIC COLUMN IN RC1 | metadata در payload؛ PostgreSQL atomic integration همچنان لازم |
| Rollback | IMPLEMENTED DESIGN | disable candidate path؛ canonical data untouched |
| Backup | OVERLAY | canonical + profile/compiler؛ projection cache survival truth نیست |
| Restore | OVERLAY | restore canonical first؛ R0 only after integrity/reconcile |
| Genesis Seed | OVERLAY | profile/compiler refs + emergency R0 pointer |
| Repository Isolation | OVERLAY | generic engine Core candidate؛ mappings local-first |
| Foundry | RULED | R0-first births/refinements only on proven need |
| Nursery/Evolution | RULED | maturity and resolution independent |
| Autonomy L0..L5 | NO MERGE | Resolution does not imply autonomy |
| Evidence E0..E5 | NO MERGE | Resolution does not imply evidence level |
| SHARD candidate | ISOLATED | no promotion; staleness/critic remain candidate and non-authorizing |
| Observability | RULED | desired/min/effective/profile logged, telemetry not authority |
| Security / prompt injection | NO WEAKENING | projection cannot convert untrusted data into authority |
| Data classification | NO WEAKENING | resolution != sanitization/F1; residency/retention remain hard |
| secretary-001 manifest | IMPLEMENTED RC1 0.3.0-rc1 | mandatory R0/R1؛ no legacy bypass؛ DNA v1.2 canonical remains |
| secretary conversation | IMPLEMENTED | R0 direction/text; R1 adds transport/provider/time/id |
| secretary tasks | IMPLEMENTED | R0 backbone; R1 refinements |
| secretary prices | IMPLEMENTED | R0 no financial amount; R1 value/approval detail NO_DOWNGRADE |
| secretary proforma | IMPLEMENTED | minimum R1 |
| secretary Telegram effect | PROPOSAL IMPLEMENTED / DIRECT SEND FORBIDDEN | R1 proposal؛ exact approval + atomic Outbox + Executor لازم |
| secretary legal/financial commitment | FAIL/ESCALATE | minimum R2 but current candidate supports R0/R1 only |
| PostgreSQL | UNCHANGED | no claim of integration run in this candidate |
| Production deployment | NOT CLAIMED | candidate source only; Birth/runtime status unchanged |
| Local validation | E2 PASS | RC1 62/62 + ancestor 14/14؛ total 76/76 |
