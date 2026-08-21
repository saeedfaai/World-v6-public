# فهرست اجرایی کامل World v6.2 RC3

این فایل جایگزین هیچ سندی نیست. وظیفهٔ آن فقط تعیین مسیر خواندن و محل قراردادهای
کامل است. متن کامل هر قرارداد در فایل مرجع خودش باقی مانده است.

## ۱. قانون، Truth و مرز Canonical

- `canonical-baseline/Root Constitution v1.0 — World v6.docx`
- `canonical-baseline/START_HERE — World v6.docx`
- `canonical-baseline/Entity DNA Schema v1.2 — World v6.docx`
- `canonical-baseline/World Registry Schema v1.2 — World v6.docx`
- `canonical-baseline/Event Schema v1.1 — World v6.docx`
- `candidate-v6.2/docs/contracts/`
- `candidate-v6.2/docs/decisions/RC1_FREEZE_AND_ROLLBACK_FA.md`
- `candidate-v6.2/docs/decisions/RC2_VERSION_SCOPE_AND_ROLLBACK_FA.md`
- `candidate-v6.2/docs/decisions/RC3_ARCHITECTURE_SCOPE_AND_ROLLBACK_FA.md`

## ۲. معماری فراکتالی و Resolution

- `candidate-v6.2/docs/WORLD_V6_2_FRACTAL_MULTI_BRAIN_ARCHITECTURE_v1.1_FA.md`
- `candidate-v6.2/docs/RESOLUTION_CABLE_MODEL_v0.2_FA.md`
- `candidate-v6.2/docs/RESOLUTION_COVERAGE_MATRIX_FA.md`
- `candidate-v6.2/docs/RESOLUTION_COVERAGE_MATRIX.json`
- `candidate-v6.2/docs/WORLD_R0_BACKBONE_FA.md`
- `candidate-v6.2/docs/FRACTAL_MULTI_BRAIN_RUNTIME_v1.0_FA.md`
- `candidate-v6.2/architecture/ARCHITECTURE_MANIFEST_v1.1.0-rc3.json`

## ۳. Mother Core و Runtime

- `candidate-v6.2/runtime/core/resolution.py`
- `candidate-v6.2/runtime/core/fractal_runtime.py`
- `candidate-v6.2/runtime/core/brain_gateway.py`
- `candidate-v6.2/runtime/core/portable_brain.py`
- `candidate-v6.2/runtime/core/council.py`
- `candidate-v6.2/runtime/core/effects.py`
- `candidate-v6.2/runtime/core/evolution.py`
- `candidate-v6.2/runtime/core/kernel.py`
- `candidate-v6.2/runtime/core/postgres_schema.sql`

## ۴. Schema و قرارداد ماشین‌خوان

تمام schemaهای فعال در `candidate-v6.2/schemas/` قرار دارند، شامل Resolution
Envelope/Patch/Profile، Brain Handler، Portable Brain/Model Bundle، Model Capability
Card، Manual Exchange، Decision، Council Session، Shadow Run، Compilation Maturity،
Approval Binding، External Effect Proposal، Fractal Node و Execution Capsule.

## ۵. Brain Farm، مدل قابل تعویض و Council

- `candidate-v6.2/brain-packs/secretary-001/`
- `candidate-v6.2/fractal/council/secretary-high-risk-council.v1.json`
- `candidate-v6.2/fractal/nodes/`
- `candidate-v6.2/fractal/handlers/`
- `candidate-v6.2/fractal/maturity/`
- `tools/universal_model_bridge.py`
- `tools/demo_portable_secretary.py`

## ۶. Secretary-001

- `candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/README.md`
- `candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/BIRTH_READINESS.md`
- `candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/entity.yaml`
- `candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/src/`
- `candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/migrations/`
- `candidate-v6.2/runtime/adapters/telegram.py`
- `candidate-v6.2/runtime/adapters/drive_archive.py`

Secretary در این درخت PRE-BIRTH است. Telegram فقط Transport و Brain فقط Proposal
Producer است. Identity، Conversation Spine، State و Memory خارج از Provider و Channel
باقی می‌مانند. Effect زنده بدون ApprovalBinding و Outbox مجاز نیست.

## ۷. Evidence و Proof

- `candidate-v6.2/evidence/FINAL_VALIDATION_RC1.txt`
- `candidate-v6.2/evidence/FINAL_VALIDATION_RC2.txt`
- `candidate-v6.2/evidence/FINAL_VALIDATION_RC3.txt`
- `candidate-v6.2/evidence/v6.2-rc1-evidence.json`
- `candidate-v6.2/evidence/v6.2-rc2-evidence.json`
- `candidate-v6.2/evidence/v6.2-rc3-evidence.json`
- `candidate-v6.2/runtime/core/tests/`
- `candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/tests/`
- `source-ancestor/secretary-v0.1.3/tests/`
- `SHA256SUMS.txt`
- `FILE_INVENTORY.txt`
- `SBOM.cdx.json`

## ۸. Roadmap، Rollback و Ratification

- `candidate-v6.2/docs/IMPLEMENTATION_PLAN_PHASE1_FA.md`
- `candidate-v6.2/docs/ACCEPTANCE_GATES_v6.2_RC1.json`
- `candidate-v6.2/docs/ACCEPTANCE_GATES_v6.2_RC2.json`
- `candidate-v6.2/docs/ACCEPTANCE_GATES_v6.2_RC3.json`
- `candidate-v6.2/docs/RATIFICATION_RECORD_TEMPLATE.json`
- `candidate-v6.2/docs/FINAL_AUDIT_AND_RATIFICATION_CANDIDATE_FA.md`
- `RELEASE_MANIFEST.json`
- `SOURCE_PROVENANCE.json`
- `REPOSITORY_STATUS.json`

## ۹. گزارش یکپارچه

- `docs/reports/World_v6.2_ARCHITECTURE_PROOF_ROADMAP_SECRETARY_COMPLETE_FA.pdf`
- `docs/reports/World_v6.2_ARCHITECTURE_PROOF_ROADMAP_SECRETARY_COMPLETE_FA_SHA256.txt`

## ۱۰. قواعد تغییر

1. Canonical/FROZEN/STABLE درجا ویرایش نمی‌شود.
2. تغییر Stable Contract به version، migration، rollback، test، SHA و تأیید Human Root نیاز دارد.
3. Brain/Provider/Channel هرگز Identity، Authority، Memory یا Canonical Truth نیست.
4. Canonical Truth downgrade نمی‌شود و Up-resolution فقط از Canonical reload می‌کند.
5. خروجی Brain/Council/Shadow Proposal است.
6. External Effect به Policy، Approval دقیق، Outbox اتمیک و Executor idempotent نیاز دارد.
7. E2 را نمی‌توان E3/E4/E5 یا Production معرفی کرد.

