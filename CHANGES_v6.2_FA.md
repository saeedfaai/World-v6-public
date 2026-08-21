# تغییرات World v6.2 Resolution-Native Candidate

1. تعریف Resolution به‌عنوان محور مستقل از Version/Maturity/Autonomy/Evidence.
2. تعریف R0 Backbone و Refinementهای R1+.
3. Canonical truth never downgraded.
4. تعریف Projection deterministic و non-authoritative.
5. تعریف `SAFE_TO_PROJECT / READ_ONLY_WHEN_PROJECTED / NO_DOWNGRADE`.
6. ممنوعیت inverse reconstruction از View پایین؛ برای افزایش Resolution باید Canonical دوباره Load شود.
7. lower-resolution write فقط bounded leaf patch با canonical hash guard.
8. حفظ hidden high-resolution state هنگام patch.
9. Resolution constraint داخل Policy Gate موجود، نه stage جدید.
10. Brain resolution negotiation بدون پایین‌آوردن minimum یا data policy.
11. Kernel validation hook بدون grant authority.
12. Event/Audit metadata به‌صورت extension داخل payload موجود، نه Ledger موازی.
13. بدون DB migration جدید در v0.1 برای حفظ سادگی و rollback.
14. Backup/Restore/Genesis بر Canonical full-fidelity باقی می‌مانند؛ projection cache survival truth نیست.
15. Foundry R0-first و refinement فقط بر اساس need/failure/evidence.
16. secretary-001 v0.2.0 candidate با R0/R1؛ ancestor v0.1.3 محفوظ.
17. conversation/task/price projection پیاده شد.
18. amount/approval price در R0 پنهان؛ proforma R1؛ Telegram external delivery R1 + existing Root approval؛ legal/financial commitment R2 و بنابراین در candidate فعلی fail/escalate.
19. SHARD candidate جدا و غیر-authorizing باقی ماند.
20. 31/31 test candidate PASS؛ PostgreSQL/live/security/recovery/production همچنان OPEN.

## RC1 hardening — 2026-08-20

21. strict World Canonical JSON v1 جایگزین `default=str` شد.
22. JSON Pointer امن، guard نسخه/source/profile/projection و ممنوعیت collection replacement اضافه شد.
23. Profile v0.2 یک منبع حقیقت runtime/schema شد و Profile hash اجباری شد.
24. consumer envelope کامل و audit metadata جدا شد؛ omitted path به Brain نشت نمی‌کند.
25. Brain Gateway ورودی را واقعاً project می‌کند و multi-profile Resolution vector دارد.
26. Provider capability فقط برای `profile_id@version#hash` معتبر است.
27. action-required fine wires علاوه بر minimum Resolution اجباری شد.
28. silent legacy `execution_resolution=None` حذف شد.
29. Entity-direct Telegram/Drive I/O مسدود و adapterها به لایهٔ مشترک منتقل شدند.
30. `root_approved` boolean با immutable exact ApprovalBinding جایگزین شد.
31. effect proposal/outbox preparation از execution جدا شد؛ intent هرگز outcome نیست.
32. LibreOffice/soffice discovery portable و per-run profile isolation اضافه شد.
33. `pyproject.toml`, `uv.lock`, `pylock.toml` و CycloneDX SBOM اضافه شد.
34. cache/pyc از release حذف و evidence قدیمی به ancestor evidence منتقل شد.
35. تست مستقل RC1: Core 41/41، Secretary 21/21، ancestor 14/14؛ مجموع 76/76 PASS.
36. وضعیت همچنان RC / NOT CANONICAL / NOT DEPLOYED است؛ PostgreSQL/recovery/live/security و Human Root ratification بازند.

## RC2 Fractal Multi-Brain — 2026-08-20

37. مرز نسخه `6.2.0-rc.2` تثبیت شد؛ Root Constitution و Canonical DNA بدون تغییر ماندند.
38. Fractal Node، Execution Capsule، بردار مستقل `R/X/B/D/C/A/E/M` و budget محدود پیاده شد.
39. cycle، hash/version mismatch، input tamper، Resolution/axis downgrade و budget overflow fail-closed شدند.
40. handlerهای Code/Brain/Manual/Local/Council با fallback یکسان و proposal-only تعریف شدند.
41. network/API-token adapter در حالت offline پیش از invocation رد می‌شود.
42. Portable Brain Pack استاندارد برای secretary-001 با binding دقیق DNA/Prompt/Schema/Profile ساخته شد.
43. Provider Overlayهای ChatGPT، Gemini، Grok، Local و deterministic code بدون API زنده اضافه شدند.
44. `Secretary Decision v1` پاسخ مدل را محدود و Template renderer متن استاندارد را provider-independent کرد.
45. PortableSecretaryService به state واقعی منشی متصل شد، بدون انتقال هویت/حافظه به Provider.
46. Compilation Maturity `C0..C6`، Shadow evidence و one-step Promotion Gate پیاده شد.
47. C5 نیازمند Human Root approval و C6 علاوه بر آن نیازمند restore proof شد.
48. Council کور-سپس-مشورتی با چند دور محدود، وزن کالیبره، dissent و high-risk veto پیاده شد.
49. تالار و Brain هیچ authority یا external effect ایجاد نمی‌کنند.
50. schemaهای RC2، fixtureهای هم‌ارزی و کنترل عدم secret/API اضافه شدند.
51. Live provider/API، PostgreSQL integration، recovery، chaos و Production همچنان صریحاً تست‌نشده و ادعانشده‌اند.

## RC3 Complete Architecture and Universal Model Path — 2026-08-20

52. مرز نسخه `6.2.0-rc.3` ایجاد و RC2 با manifest/SHA256/ZIP hash مستقل به‌عنوان parent تثبیت شد.
53. سند جامع ۳۳ بخشی معماری Fractal Multi-Brain با planes، levels، axes، state machines، trust boundaries و rollout نوشته شد.
54. Architecture Manifest ماشین‌خوان با binding دقیق SHA-256 به سند معماری اضافه شد.
55. `Model Capability Card v1` برای اعلام صریح قابلیت، Resolution، data class، residency، retention، continuity و evidence تعریف شد.
56. `Manual Brain Exchange v1` و `Portable Model Bundle v1` برای انتقال خودبسنده و بدون API به هر مدل منطبق تعریف شدند.
57. Universal Manual Host با `ANY_CONFORMING_MODEL` و provider label آزاد اضافه شد.
58. ابزار `tools/universal_model_bridge.py` مسیر Export→Integrity Validation→Response Validation→Deterministic Render را عملیاتی کرد.
59. Export پیش‌فرض منشی از Projection حداقلی R0 استفاده می‌کند تا Context و token مصرفی سمت مدل کمینه بماند.
60. Bundle شامل Brain Pack، Prompt Contract، Decision Schema، projected request و hashهای integrity است؛ تغییر Projection fail-closed می‌شود.
61. مرز صداقت Manual/E2 از Live API/E3-E4 به‌صورت صریح در schema، manifest و documentation ثبت شد.
62. تست‌های RC3 سند/manifest hash binding، schema conformance، arbitrary-provider portability، tamper rejection، semantic equivalence و authority smuggling را پوشش دادند.
63. Core به 78/78، Candidate به 100/100 و مجموع مستقل با ancestor به 114/114 تست PASS رسید.
64. Root Constitution v1.0، Canonical DNA v1.2، Entity overlay، Profile hashها و Portable Brain Pack RC2 عمداً بدون تغییر حفظ شدند.
65. PostgreSQL atomic integration، crash/replay، fresh restore، live provider، security/load/chaos، Git tag و canonical ratification همچنان OPEN و ادعانشده‌اند.
