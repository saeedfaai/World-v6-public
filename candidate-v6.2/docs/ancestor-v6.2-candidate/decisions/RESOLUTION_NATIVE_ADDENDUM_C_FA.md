# World v6.2 — Resolution-Native Architecture Addendum C

**Status:** CANDIDATE / NOT YET RATIFIED AS CANONICAL CORE  
**Date:** 2026-08-20  
**Authority boundary:** Root Constitution v1.0 remains unchanged.  
**Purpose:** تبدیل اصل «simple in actuality, complex in potential» به یک الگوی مهندسی قابل‌پیاده‌سازی و قابل‌آزمون، بدون ساختن یک معماری موازی.

## 1. تعریف رسمی

World v6.2 یک **واقعیت Canonical واحد** را نگه می‌دارد و اجازه می‌دهد همان واقعیت با Resolutionهای عملیاتی متفاوت دیده و مصرف شود. Resolution پایین‌تر نسخه دیگری از حقیقت نیست؛ یک **Projection مشتق‌شده** از حقیقت Canonical است.

- `R0`: Backbone / کابل مادر؛ کمینه اطلاعات لازم برای هویت، وظیفه و کنترل امن.
- `R1+`: Refinementهای تدریجی؛ سیم‌های دقیق‌تر که از همان Backbone منشعب می‌شوند.
- تعداد سطوح، معنای جزئیات و حداکثر Resolution برای هر Domain توسط **Resolution Profile نسخه‌دار** تعریف می‌شود؛ R0/R1/R2 معنای جهانی ثابت برای همه Domainها ندارند.

## 2. چهار Invariant اصلی

**RN-INV-01 — Canonical truth is never downgraded.**  
کم‌کردن Resolution فقط View/Execution را ساده می‌کند؛ داده Canonical، Eventها، State معتبر و History حذف یا بازنویسی نمی‌شوند.

**RN-INV-02 — Refinement never replaces the backbone.**  
هر قابلیت/قرارداد پیشرفته باید به یک Backbone پایین‌تر قابل Projection باشد. Refinement ساختار پایه را نابود نمی‌کند.

**RN-INV-03 — Lower-resolution writes are bounded patches.**  
Actor با Resolution پایین اجازه Whole-object replace ندارد. فقط فیلدهایی که در همان Resolution قابل مشاهده و قابل نوشتن‌اند، با `expected_canonical_hash` به‌صورت Patch تغییر می‌کنند. State پنهانِ Resolution بالاتر باید حفظ شود.

**RN-INV-04 — No inverse hallucination.**  
R0 به R2 «تخمین زده» نمی‌شود. برای بازگشت به Resolution بالاتر، سیستم داده Canonical را دوباره Load می‌کند. Projection پایین منبع بازسازی جزئیات حذف‌شده نیست.

## 3. Invariantهای ایمنی تکمیلی

**RN-INV-05 — Identity invariance.** `entity_id`, root binding, lineage و سایر Hard Identityها در همه Viewهای مجاز ثابت می‌مانند.

**RN-INV-06 — Authority monotonicity.** کاهش Resolution هرگز Permission، Autonomy، Approval یا Capability جدید ایجاد نمی‌کند. Policy Gate همیشه با حقیقت/Policy Canonical تصمیم می‌گیرد، نه با خلاصه‌ای که Brain دیده است.

**RN-INV-07 — Risk cannot disappear by projection.** اگر جزئیات لازم برای ارزیابی ریسک در View پایین موجود نیست، Action به Resolution بالاتر نیاز دارد یا Fail/Queue/Escalate می‌شود؛ «ندیدن ریسک» معادل «نبود ریسک» نیست.

**RN-INV-08 — Projection provenance.** هر Projection قابل ممیزی باید profile id/version، source/canonical hash، source/target resolution و derived/non-authoritative بودن را مشخص کند.

**RN-INV-09 — Structural projection should be compositional.** برای projector قطعی و یک profile ثابت، هدف طراحی این است که برای `i <= j`: `P_i(P_j(x)) = P_i(x)`. Semantic summaryهای آینده فقط با provenance/evaluation و به‌عنوان derived artifact وارد می‌شوند و این property را بدون آزمون ادعا نمی‌کنند.

**RN-INV-10 — Resolution != Maturity != Autonomy != Version != Evidence.** موجود Mature می‌تواند با R0 اجرا شود؛ Brain قوی می‌تواند روی Entity نوزاد R0 بنشیند؛ تغییر Resolution به‌خودی‌خود Promotion/Demotion یا Version migration نیست.

## 4. سه سیاست Downgrade در سطح فیلد/قابلیت

- `SAFE_TO_PROJECT`: در View پایین قابل نمایش/استفاده مطابق Profile است.
- `READ_ONLY_WHEN_PROJECTED`: در Projection قابل مشاهده یا مشتق‌سازی است اما Actor پایین حق تغییر آن را ندارد.
- `NO_DOWNGRADE`: برای اقدام/تغییر معتبر باید Resolution لازم حاضر باشد. اگر Brain/Context آن را پشتیبانی نکند، Action متوقف، صف یا Escalate می‌شود.

این طبقه‌بندی جای Policy/Permission را نمی‌گیرد؛ فقط Compatibility Resolution را بیان می‌کند.

## 5. دو نوع بازگشت که نباید مخلوط شوند

### Resolution downgrade
همان Entity، همان نسخه، همان Canonical State و همان History؛ فقط Operational View ساده‌تر می‌شود. این باید اولین ابزار Graceful Degradation باشد.

### Version rollback
کد/Contract/Skill/Policy فعال واقعاً به Release قبلی برمی‌گردد و طبق قواعد Version/Migration/Rollback فعلی انجام می‌شود.

قاعده: **اگر خطا فقط از توان Brain/Context/complexity است، ابتدا Resolution را پایین بیاور؛ اگر خود Release/Contract خراب است، Version rollback انجام بده.**

## 6. DNA

هیچ top-level organ جدیدی به DNA v1.2 اضافه نمی‌شود. Resolution داخل slotهای موجود تعریف می‌شود:

- `cognition.context_policy` → active/default Resolution Profile و قواعد Context Projection.
- capability/skill/action config → `minimum_resolution`, `desired_resolution`, downgrade policy.
- continuity/audit pointers → profile/version/projection provenance refs.

Stable DNA پس از Birth برای تغییر Resolution عملیاتی بازنویسی نمی‌شود؛ Resolution اجرایی جزو live/config state است. این با جداسازی DNA پایدار از Registry/State زنده سازگار است.

## 7. Registry و State

Candidate v0.1 **ستون DB جدید اجباری نمی‌کند**. `desired_state_ref/actual_state_ref` موجود می‌تواند Resolution profile/current execution view را حمل کند. Registry ممکن است read-model مشتق‌شده برای نمایش Resolution بسازد، اما منبع Authority جدید ایجاد نمی‌شود.

اگر بعداً Query/SRE واقعی ثابت کرد که فیلدهای indexable مثل `execution_resolution` لازم‌اند، migration additive نسخه‌دار جداگانه ساخته می‌شود.

## 8. Event Ledger و Audit

Resolution metadata در Event/Command payload موجود حمل می‌شود، نه در Ledger موازی. برای عملیات مرتبط می‌توان ثبت کرد:

- `resolution_profile_ref`
- `desired_resolution`
- `minimum_resolution`
- `effective_resolution`
- `canonical_hash`
- `projection_hash`
- `projection_derived=true`

External effect همچنان باید به payload/effect hash Canonical و Approval معتبر bind شود. Approval روی یک View مبهم یا بعداً regenerated content معتبر نیست.

## 9. Policy Gate

Resolution یک **constraint داخل Policy evaluation موجود** است، نه stage جدید در action path. مسیر قانون اساسی همان است:

`SENSE → INTERPRET → PROPOSE → POLICY CHECK → APPROVAL → AUTHORIZE → EXECUTE → OBSERVE → RECORD EVENT → UPDATE STATE`

Policy evaluation باید در صورت Resolution-aware request کنترل کند:

1. Resolution requested/desired معتبر است.
2. Brain/actor effective resolution از `minimum_resolution` پایین‌تر نیست.
3. downgrade، data classification/residency/retention/training rules را ضعیف نکرده است.
4. projection فیلدهای `NO_DOWNGRADE` لازم برای Action را پنهان نکرده است.
5. approval/permission/capability/budget طبق Canonical truth بررسی می‌شوند.

## 10. Kernel API

Kernel authority تغییر نمی‌کند. Candidate API می‌تواند Resolution Envelope و Resolution Patch بپذیرد و قبل از mutation بررسی کند:

- profile id/version شناخته‌شده؛
- expected canonical hash/version تازه؛
- Actor فقط pathهای قابل نوشتن در Resolution خودش را تغییر می‌دهد؛
- hidden high-resolution state حفظ می‌شود؛
- whole-object replacement از View پایین ممنوع است؛
- بعد از validation، همان Policy/Approval/Transaction/Event rules فعلی اجرا می‌شوند.

Resolution Compiler اجازه مستقیم execute/adapters/state mutation ندارد.

## 11. Brain Gateway و Brain Contract

هر Task سه مقدار مستقل دارد:

- `desired_resolution`
- `minimum_resolution`
- `effective_resolution`

هر Brain/Adapter می‌تواند `max_resolution` اعلام کند. بعد از عبور از Data/Policy compatibility، انتخاب ساده Candidate v0.1:

`effective = min(desired, brain_max)` فقط اگر `effective >= minimum`.

اگر Brain ضعیف‌تر باشد ولی هنوز minimum را تأمین کند، Task با View ساده‌تر ادامه می‌یابد. اگر minimum را تأمین نکند، Provider بعدی امتحان می‌شود یا Work صف/Degrade/Escalate می‌شود. هیچ‌گاه minimum برای دستیابی به availability پایین آورده نمی‌شود.

## 12. Resolution & Context Compiler

Context Compiler موجود نقش Resolution Compiler را نیز می‌گیرد؛ component مستقل Authority ساخته نمی‌شود.

### Candidate v0.1
فقط **deterministic structural projection**: انتخاب/حذف/نگاشت صریح فیلدها بر اساس profile نسخه‌دار.

### آینده
Semantic Resolution Agent/LLM می‌تواند چند Event را به Summary سطح پایین تبدیل کند، اما خروجی:

- Derived و non-authoritative است؛
- provenance به Raw Event/Memory دارد؛
- به‌تنهایی Rule/Permission/Fact canonical نمی‌شود؛
- برای promotion از Gateهای existing knowledge/evidence استفاده می‌کند.

## 13. Memory و Knowledge

Raw event/memory حذف نمی‌شود تا R0 ساخته شود. R0/R1 memory view می‌تواند cache/summary/index باشد. Freshness, provenance, contradiction و classification باید از Canonical data به Projection منتقل شوند؛ Summary نباید stale/risky evidence را «پاک» نشان دهد.

Projectionهای reproducible cache هستند و الزاماً backup مستقل نمی‌خواهند؛ profile/compiler version و Canonical source باید recoverable باشند.

## 14. Skills و Capabilities

Skill/Action می‌تواند به‌صورت نسخه‌دار اعلام کند:

- `minimum_input_resolution`
- `desired_input_resolution`
- `minimum_output_resolution`
- supported projection profiles
- lower-resolution fallback behavior
- `NO_DOWNGRADE` fields/effects

نصب Skill جدید Autonomy یا Resolution را خودکار بالا نمی‌برد.

## 15. Workflow و Scheduler

Workflow backbone می‌تواند در R0 بماند و stepهای خاص Resolution بالاتر بخواهند. Scheduler می‌تواند برای کاهش هزینه **کمترین Resolutionی را انتخاب کند که minimum task را تأمین می‌کند**؛ ولی Risk/Data/Approval constraints اولویت بالاتر دارند.

## 16. Inter-Entity Communication

Message backbone حفظ می‌شود. Resolution metadata extension است، نه protocol replacement. Sender می‌تواند desired/minimum را اعلام کند؛ Recipient/Kernel فقط طبق capability/policy خودش effective resolution را تعیین می‌کند.

- Sender حق ندارد minimum گیرنده را پایین بیاورد.
- ACK همچنان business success نیست.
- dual sender/recipient authorization همچنان برقرار است.
- effect-capable message همچنان sender_epoch/sequence و integrity requirements فعلی را دارد.

## 17. Relationships

Relationship/Delegation Canonical در Resolution پایین پاک نمی‌شود. UI/Brain ممکن است فقط relation type اصلی را ببیند؛ ولی Permission/Policy evaluation باید قرارداد کامل Canonical را بررسی کند. Relationship summary هرگز Authority جدید ایجاد نمی‌کند.

## 18. Foundry / Nursery / Evolution

Foundry برای Entity جدید **R0-first** است. فقط Backbone لازم برای Birth و اولین vertical واقعی فعال می‌شود. Refinement زمانی اضافه می‌شود که Task/Failure/Evidence نیاز آن را نشان دهد.

Maturity می‌تواند بالا برود بدون افزایش Resolution دائمی؛ Resolution بیشتر یک execution/context choice است. Evolution Manager می‌تواند profile Candidate بسازد، اما direct production mutation ممنوع باقی می‌ماند.

## 19. Autonomy و Evidence

Resolution محور جدا از L0..L5 و E0..E5 است. مثال معتبر:

`Mature Entity + L2 autonomy + E4 capability evidence + R0 current execution`

هیچ mapping خودکار مثل `R3 => L3` مجاز نیست.

## 20. External Effects و Approval

Brain پایین-resolution فقط Proposal می‌سازد. Kernel قبل از effect باید Canonical action/effect را reconstruct/normalize کند، policy را روی truth کامل بررسی کند و approval را به payload/effect hash تغییرناپذیر bind کند.

اگر Action جزئیات `NO_DOWNGRADE` لازم دارد، R0 proposal حتی با Approval عمومی مجاز به Execute نیست؛ باید Context/Brain مناسب یا Human resolution موجود باشد.

## 21. Backup / Restore / Genesis

### Backup
Canonical State/Event/Artifacts/Code/Profiles حفظ می‌شوند. Projectionهای قابل‌بازتولید cache هستند. Backup باید Resolution profile/compiler version موردنیاز برای reproduce viewها را نگه دارد.

### Restore
Restore از R0 summary به‌تنهایی ممنوع است. ترتیب: integrity → canonical state/event restore → profile/compiler restore → reconciliation → سپس در صورت نیاز safe R0 execution. R0 برای Emergency continuity مفید است، نه جای Canonical recovery.

### Genesis
Seed/Vault باید pointer/version مربوط به Resolution profiles/compiler و emergency R0 policy را حفظ کند. هیچ Snapshot کم‌Resolution جای Snapshot/History Canonical را نمی‌گیرد.

## 22. Repository / Build-vs-Integrate

No-empty-scaffolding و local-first برقرار است. در Candidate فعلی:

- `core/resolution.py`: الگوریتم عمومی و deterministic؛ world-level candidate.
- `secretary/src/resolution_profile.py`: mappingهای مخصوص منشی و action minimumها؛ entity-local.

هیچ `/shared/resolution/` یا service جدا ساخته نمی‌شود. Semantic agent، DB index، vector layer یا distributed resolution service تا نیاز واقعی وجود نداشته باشد ساخته نمی‌شود.

## 23. Observability

Trace/metrics می‌توانند `desired/minimum/effective resolution`, profile version, projection failures و fallback counts را ثبت کنند. Telemetry Authority نیست و نباید حاوی secret/raw restricted data غیرضروری باشد.

## 24. SHARD Candidate Interaction

Resolution-native شدن SHARD را به Core promote نمی‌کند. Memory staleness اگر استفاده شود روی Canonical evidence اعمال می‌شود و Projection باید وضعیت freshness را حفظ کند. Semantic conflict critic یا self-improvement candidate همچنان advisory/evidence-gated است و هیچ‌کدام اجازه Authorization ندارند.

## 25. Secretary-001 v0.2.0 Candidate

Source واقعی v0.1.3 به‌عنوان ancestor حفظ شده است. Candidate v0.2.0:

- Canonical DNA همچنان v1.2.0؛ Addendum C فقط candidate extension است.
- Default deployment target = R0؛ legacy API default برای regression compatibility حفظ شده تا runtime binding صریح migration شود.
- Conversation: R0=`direction,text`; R1 metadata کانال/provider/time/id را اضافه می‌کند.
- Task: R0=`task_id,title,status,next_action`; R1 due/priority/domain/goal/time را اضافه می‌کند.
- Price: R0 فقط identity/existence/active؛ amount/validity/approval در R1 و `NO_DOWNGRADE`.
- Internal draft/task actions: R0.
- Approved-price/proforma: حداقل R1.
- Telegram external delivery: حداقل R1 **به‌علاوه** همان Human Root approval قبلی.
- Legal/financial commitment: حداقل R2 + approval؛ چون secretary candidate فعلی فقط R0/R1 پشتیبانی می‌کند، چنین commitmentی باید fail/escalate شود.

## 26. Persistence decision v0.1

Candidate v0.1 عمداً migration جدید PostgreSQL ندارد. دلیل: Resolution metadata با state/config pointer و payload JSON موجود قابل حمل است و ستون جدید هنوز نیاز اثبات‌شده ندارد. این تصمیم Rollback را بسیار ساده می‌کند و از schema complexity زودهنگام جلوگیری می‌کند.

## 27. Rollback Plan

1. Resolution-aware runtime binding را disable کن و به legacy compatibility API برگرد.
2. `core/resolution.py` و profile candidate را از active code path خارج کن.
3. BrainRequestهای جدید را بدون Resolution extension به قرارداد قبلی map کن.
4. چون Canonical data/DB schema downgrade نشده، data migration معکوس لازم نیست.
5. Eventهای candidate باقی می‌مانند و پاک نمی‌شوند؛ reader قدیمی optional metadata را ignore می‌کند.
6. entity v0.1.3 source ancestor برای rollback محفوظ است.

## 28. Promotion Gate

قبل از Canonical promotion:

- unit/property tests Projection/Patch/Negotiation؛
- regression tests secretary 0.1.3 behavior؛
- compatibility mapping به DNA/Registry/Event/Policy/Kernel/Inter-Entity active set؛
- representative PostgreSQL integration برای state/event/outbox path؛
- crash/replay test برای projected proposal → canonical commit؛
- security test: no data/policy/approval downgrade؛
- restore test: full Canonical restore سپس R0 safe execution؛
- Human Root ratification و append-only decision event.

تا آن زمان v6.2 **Candidate E2** است، نه Production/Canonical certification.
