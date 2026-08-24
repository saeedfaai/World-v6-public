
# فراتر از Agentهای مدل‌محور: معماری پنج‌Plane برای Entityهای هوش مصنوعی پایدار، مستقل از Provider و Governed

**World 8 / Z0-A - مقاله فنی مفصل**  
**نویسنده:** Saeed Farokhi  
**تاریخ:** 24 August 2026  
**وضعیت:** DRAFT FOR REVIEW / NOT A PRODUCTION CLAIM

## چکیده

بخش بزرگی از Agent Systemهای امروز Identity، Memory، Objective، Authority و Continuity را به Session مدل یا Orchestration Framework گره می‌زنند. برای Assistant کوتاه‌عمر این coupling ممکن است کافی باشد، اما وقتی یک Entity دیجیتال باید Provider را عوض کند، Writer همزمان داشته باشد، Crash و Restore را تحمل کند، Task طولانی اجرا کند، External Effect واقعی بسازد و فرآیند Development خودش را به‌صورت کنترل‌شده بهبود دهد، این coupling تبدیل به ریسک معماری می‌شود.

World 8 / Z0-A یک Runtime پنج‌Plane شامل Canonical Spine، Operational، Observation، Development/Mason و Evidence/Governance است. اصل مرکزی، جداسازی Cognition قابل تعویض از Identity، Canonical State، Authority، Objective، Accepted History و Evidence پایدار است. در Development نیز قاعده روشن است: Observation اندازه‌گیری می‌کند، Mason Proposal می‌دهد، Evaluator مستقل قضاوت می‌کند، Promotion Authority تصمیم می‌گیرد و Canonical Spine ثبت می‌کند.

معماری از Primitiveهای شناخته‌شده استفاده می‌کند و ادعای اختراع آن‌ها را ندارد: commit-time CAS، intent-bound idempotency، append-oriented event history، transactional outbox، effect receipt، sequencer lease و fencing token، DB-enforced append-only، deterministic replay، checkpoint و clean-host restore. Objective Contract و Phenotype Revision نسخه‌دار اجازه نمی‌دهند Optimization هدف یا Authority را بی‌صدا بازنویسی کند. Evaluation Receipt نیز Principal، Build، Candidate، Objective Version، Environment، Metrics و Evidence را bind می‌کند زیرا DB Constraint به‌تنهایی هویت Evaluator را ثابت نمی‌کند.

Contribution این معماری یک Composition قابل ابطال برای Persistent AI Identity و Governed Adaptation است، نه ادعای Biological Life، Consciousness، AGI، Autonomous Evolution یا Production Readiness. Evidence Levelهای E0 تا E5 مرز بین Design، Local Evidence، Integration، Production-like و Longitudinal Evidence را مشخص می‌کنند.

**کلیدواژه‌ها:** Persistent AI Agent؛ Provider-independent Identity؛ Canonical Spine؛ Event Sourcing؛ CAS؛ Transactional Outbox؛ AI Governance؛ Evidence Registry؛ Clean-host Restore؛ Multi-brain.

## ۱. مقدمه

Model Call شناخت است، نه Identity. Provider Thread ظرف مکالمه است، نه دفتر قانون اساسی. Prompt قرارداد هدف پایدار نیست. Vector Index History مرجع نیست. Human Approval Button به‌تنهایی Security Boundary کامل نیست. این تفاوت‌ها در Demo کوتاه دیده نمی‌شوند چون همه‌چیز داخل یک Process موقت است؛ در سامانه‌ای که باید ماه‌ها یا سال‌ها ادامه پیدا کند، به Requirement معماری تبدیل می‌شوند.

سؤال World 8 این نیست که «کدام Model خود Agent است؟» بلکه این است که «وقتی Model عوض می‌شود چه چیزی باید ثابت بماند؟» پاسخ Z0-A شامل Identity پاسخ‌گو، Canonical Accepted State، Authority، Objective، Revision Lineage و Evidence است. Cognition به این Boundary متصل می‌شود ولی مالک آن نیست.

World v6.2 و World 7 ایده‌های Multi-brain، Persistent Entity، Genome، Spine، Event-sourced State، Development Stage و Proof Obligation را بررسی کردند. Review نشان داد Self-development وقتی Self-referential می‌شود که همان Optimizer Telemetry را انتخاب کند، Metric را تعریف کند، Change بسازد، خودش را Evaluate و خودش Promote کند. Z0-A این مشکل را به Separation of Duties اجرایی تبدیل می‌کند.

## ۲. سؤال تحقیق

سؤال اصلی این است که آیا یک Entity دیجیتال مبتنی بر AI می‌تواند با تعویض Cognition Provider همچنان Identity، Authority، Accepted History و Governed Change خود را حفظ کند و در عین حال Audit و Falsification پذیر باشد؟ این مسئله فقط Memory Persistence نیست؛ Stable Identity Namespace، Canonical Serialization، Objective Versioning، Authorization، Observation/Evaluation قابل Attribution و Recovery واقعی لازم است.

Architecture عمداً Claimهای بزرگ‌تر را قبل از Evidence نمی‌پذیرد. Persistence مساوی Biological Life نیست؛ Provider Switch مساوی Immortality نیست؛ Self-modification مساوی Evolution نیست؛ و Local Test Suite مساوی Production Readiness نیست.

## ۳. پنج Plane

Canonical Spine Identity و History پذیرفته‌شده را نگه می‌دارد. Operational Task، Role، Cognition، Context، Connector و Effect را اجرا می‌کند. Observation رفتار را می‌سنجد و Gap قابل انتساب می‌سازد. Development/Mason Candidate می‌سازد. Evidence/Governance Claim، Evaluation و Promotion را کنترل می‌کند.

هر Plane یک Trust Problem متفاوت را حل می‌کند. Spine باید Truth را Serialize کند. Operational باید Replaceable باشد. Observation نباید در مالکیت Optimizer باشد. Mason باید Productive ولی غیرحاکم باشد. Governance باید از Evidence قابل Attribution تصمیم بگیرد.

Cognition و Ingress در Z0-A داخل Operational هستند و Top-level Plane مستقل نیستند.

## ۴. Entity، Role و RoleBinding

در Frameworkهای Agent، Agent می‌تواند Prompt، Persona، Process، Graph Node یا Session باشد. World 8 بین Persistent Object و Responsibility Slot فرق می‌گذارد.

Entity دارای Canonical ID، Lifecycle، State Head، Authority Ceiling و Event Lineage است. Role فقط مسئولیت است. RoleBinding آن Role را برای Holder/Executor مشخص در Scope، Validity و Grant محدود فعال می‌کند.

بنابراین `company-001` Society عملیاتی ثابت می‌ماند و `secretary-role` می‌تواند در زمان‌های مختلف توسط Brain یا Holderهای مختلف اجرا شود. Provider فقط Provenance است. Role name Authority ایجاد نمی‌کند.

## ۵. Objective خارج از Cognition

اگر Component بهبوددهنده بتواند همان Prompt هدفی را که با آن ارزیابی می‌شود بازنویسی کند، Improvement معنای قابل آزمون خود را از دست می‌دهد. Z0-A Objective Contract را Canonical و Immutable per Version می‌کند و Objective، Metric/SLO، Hard Constraint، Authority Ceiling، Risk Class، Observation Contract، Adaptation Surface و Promotion Policy را ثبت می‌کند.

تغییر Objective یا Hard Constraint یک Constitutional Governance Change است، نه Mason Optimization معمولی.

## ۶. Phenotype Revision

Phenotype Revision یک Candidate Change اجرایی/Configuration است که Parent Revision، Objective Version، Change Set، Migration، Rollback، Expected Metric، Risk و Evidence Requirement دارد.

واژه Phenotype در اینجا Operational است، نه Biological. Candidate تا زمان Promotion فعال نیست. Activation یک Canonical CAS Event است. Rollback نیز Event جدید است و History را پاک نمی‌کند.

## ۷. Canonical Concurrency

CAS در زمان Commit انجام می‌شود. Pre-read خارج Transaction Lost Update را متوقف نمی‌کند. اگر دو Writer روی یک Head شروع کنند، دقیقاً یکی باید Commit شود.

Idempotency هم Semantic است. Same Key + Same Intent prior result را برمی‌گرداند؛ Same Key + Changed Intent Collision است. این قاعده از تبدیل Deduplication به Corruption جلوگیری می‌کند.

## ۸. Atomicity و External Effect

اگر Canonical Transition یک External Effect برنامه‌ریزی کند، Event Append، Head Advance، Projection ضروری و Outbox Obligation با هم Commit می‌شوند. Provider Call بعداً انجام می‌شود.

Effect Executor Attempt و Receipt ثبت می‌کند. Timeout می‌تواند Ambiguous باشد چون Provider ممکن است Action را انجام داده باشد. بنابراین Claim فقط Scoped Effectively-once است و Universal Exactly-once صریحاً رد می‌شود.

## ۹. Lease، Fencing و Append-only

Lease بدون Fencing کافی نیست، چون Process expired ممکن است هنوز زنده باشد. هر Sequencer Epoch Fencing Token افزایشی دارد و Storage Token stale را Reject می‌کند.

History Committed با DB Privilege محافظت می‌شود؛ Runtime Role حق UPDATE/DELETE/TRUNCATE ندارد. Hash Chain Tamper Evidence است، نه Secure Storage کامل.

## ۱۰. Replay و Clean-host Restore

Replay باید قبل از Materialization Chain، Hash، Previous Head، Event Version، Duplicate ID، Ordering، Reducer Compatibility و Final Head را Verify کند. Replayی که Hash Verification ندارد—even اگر Happy Path درست باشد—Claim Reconstructability را کامل نمی‌کند.

Recovery با Restart همان Service ثابت نمی‌شود. Clean-host Restore یعنی Environment جدید، Restore Schema/Data، Verify Head/Objective/Revision، Recreate Credential Separation، Fresh Fencing Token بالاتر و یک Fresh Governed Write. Write نهایی ثابت می‌کند System واقعاً ادامه‌پذیر است.

## ۱۱. Observation مستقل

Observation Pipeline: Raw Telemetry -> Normalization -> Aggregation/Windowing -> SLO/Invariant -> Gap Signal.

Gap به Objective Version، Metric/Invariant، Window، Detector Version، Source Telemetry و Rule متصل است. Mason می‌تواند Gap را مصرف کند ولی حق ندارد Evidence Window یا Metric خودش را تعریف کند.

## ۱۲. Mason به‌عنوان Engineering Proposer

Mason Sovereign Self-modifier نیست. Gap و Objective جاری را Reference می‌کند، Smallest Reversible Change می‌سازد، Test و Rollback ارائه می‌دهد و داخل Adaptation Surface می‌ماند.

Identity، Authority، Hard Constraint، Objective و Spine خارج از اختیار Mason هستند. Direct Commit، Sole Self-evaluation و Self-promotion ممنوع است.

## ۱۳. Evaluation قابل Attribution

Independent Evaluation فقط وقتی معنا دارد که Evaluator قابل Attribution باشد. DB Role فقط Capability Credential را نشان می‌دهد؛ نشان نمی‌دهد کدام Build، Model، Service Principal یا Human نتیجه را تولید کرده است.

Evaluation Receipt Principal، Credential Ref، Build Digest، Candidate، Objective Version، Test Environment، Metric، Result و Evidence را bind می‌کند. Promotion به این Receipt reference می‌دهد.

## ۱۴. Separation of Duties

Rule هنجاری: Observation measures؛ Mason proposes؛ Evaluator judges؛ Promotion Authority promotes؛ Canonical Spine records؛ Effect Executor settles.

در Evidence Level پایین ممکن است Moduleها روی Host مشترک باشند، اما Semantic Boundary باقی است. در Assurance بالاتر Principal و Credential جدا لازم است. اگر یک Actor همه مراحل را کنترل کند، Claim Development Governance شکست می‌خورد.

## ۱۵. Evidence به‌عنوان معماری

E0 Defined، E1 Static، E2 Local Executable، E3 Persistent Integration، E4 Production-like و E5 Longitudinal است.

این Ladder Score نیست. E2 Race Test، E4 Disaster Recovery را ثابت نمی‌کند. Provider Switch، Security را ثابت نمی‌کند. Hash Chain، Secure Storage را ثابت نمی‌کند. Proof Registry برای هر Claim Predicate، Falsifier، Required Level، Status و Evidence Reference مستقل دارد.

## ۱۶. Failure-oriented Testing

Test Program باید Architecture را حمله کند: Race دو Writer، Same Idempotency Key با Changed Intent، Fault بین Event/Head/Outbox، Stale Fencing، Forbidden DB Write، Corrupt Replay، Mutation حذف Hash Verify، Mason Hard-boundary Change، Promotion بدون Receipt، Stale Promotion، Clean-host Restore و Ambiguous Effect Timeout.

Mutation Testing حیاتی است چون ممکن است هزار Happy-path Test سبز بماند ولی Critical Check حذف شده باشد.

## ۱۷. Provider-independent Continuity

Provider Handoff باید World، Entity/Society، Role، Task، Objective، Active Revision و Canonical Lineage را حفظ کند. Provider جدید Context تازه K0-K4 می‌گیرد بدون اینکه مالک Identity شود.

K0 World Kernel، K1 Entity/Society، K2 Role Contract، K3 Current Task و K4 حداقل Evidence/Memory با Provenance است. Provider Context Window Projection موقت است، نه Canonical Memory.

## ۱۸. Multi-brain Operation

Brain Gateway می‌تواند ChatGPT، Grok، DeepSeek، Gemini، Claude، Local Model یا Algorithm deterministic را Route کند. Criteria شامل Capability، Cost، Latency، Availability، Privacy، Jurisdiction و Policy است.

Fallback Availability Feature است، نه Identity Change. Ensemble Vote هم Authority ایجاد نمی‌کند.

## ۱۹. نسبت با نسخه‌های قبلی World

World v6.2 Entity Stability، Replaceable Brain، Scoped Context، Authority خارج از Cognition، Effect Control، Evidence Gate و Recovery Discipline را تقویت کرد. World 7 Persistent Identity، Spine، Expected-head Conflict، Idempotency، Hash Chain، Reconstruction، Development Stage و Proof Obligation را گسترش داد.

Review World 7 نیز Riskهای Metaphor، Self-referential Proof، Vacuous Assertion، Mutation Coverage ضعیف و Evidence Registry غیرمستقیم را آشکار کرد. Z0-A Systems Insightها را حفظ و Autonomous Evolution را از Core هنجاری بیرون آورد.

World 8 v0.1/v0.1.1 Lineage عملیاتی `world-001`، `company-001`، RoleBinding، Task Bus و Persistent Canonical History را دارد، اما Gateهای جدید Observation Independence، Mason Confinement، Evaluator Identity و Clean-host Recovery را خودکار PASS نمی‌کند.

## ۲۰. مرز Novelty

World 8 اختراع Event Sourcing، CAS، Transaction Isolation، Outbox، Fencing، Hash Chain، RBAC، SLO Monitoring، Provenance یا Model Routing را ادعا نمی‌کند.

Contribution احتمالی در Composition این مکانیزم‌ها حول Persistent AI Identity و Governed Development Loop است، به‌ویژه Separation ثابت:

**Observation measures -> Mason proposes -> Evaluator judges -> Promotion Authority promotes -> Canonical Spine records.**

Novelty باید با Prior Art و Experiment سنجیده شود، نه با Terminology.

## ۲۱. محدودیت‌ها و Non-claimها

Design Frozen معادل Production Certificate نیست. معماری در برابر compromise کامل OS، DB Admin، Secret Manager یا Supply Chain به‌تنهایی کافی نیست. Objective ممکن است ناقص باشد. Evaluator مستقل ممکن است اشتباه کند. SLO ممکن است Proxy بد باشد.

Consciousness، Biological Life، AGI، Legal Personhood، Universal Exactly-once و Autonomous Evolution اثبات‌شده ادعا نمی‌شوند.

## ۲۲. Roadmap ارزیابی

ترتیب Implementation: Contract Freeze، Spine Hardening، Entity/Role Separation، Objective/Revision Versioning، Independent Observation، Constrained Mason، Attributed Evaluation، Governed Promotion، Clean-host Recovery و End-to-End Operational Proof.

Demonstration قوی اولیه باید هر پنج Plane را لمس کند: یک Task پایدار، Provider Handoff بدون Identity Fork، External Effect واقعی کم‌ریسک با Authorization/Outbox/Receipt، SLO Breach از پیش تعریف‌شده، Mason Proposal، Independent Evaluation و Promotion Decision جدا.

## ۲۳. نتیجه‌گیری

World 8 / Z0-A Persistent AI Agent را Entity دیجیتال Governed می‌بیند که Cognition آن Replaceable است ولی Identity، Authority، Objective، Accepted State و Evidence در مالکیت Cognition نیستند. معماری با Collapse کردن Boundaryها دنبال Autonomy نیست؛ با Explicit کردن Boundaryها دنبال Automation قابل اعتماد است.

اصل پایدار: **Brain را عوض کن بدون اینکه Entity پاسخ‌گو عوض شود؛ Implementation را بهتر کن بدون اینکه Improver بتواند قانون بازی را بی‌صدا بازنویسی کند.**

## منابع

1. S. Farokhi, *World v6.2: Fractal Multi-Brain Architecture*, Zenodo, 2026, DOI: 10.5281/zenodo.22040348.
2. World 7 project artifacts, *Living Genome / Genomic Runtime Architecture*, 2026.
3. World 8 / Z0-A, *Final Architecture Baseline*, 24 August 2026.
4. NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, 2023.
5. W3C, *PROV-O: The PROV Ontology*.
6. CNCF, *CloudEvents Specification*.
7. OpenTelemetry Authors, *OpenTelemetry Specification*.
8. PostgreSQL Global Development Group, *PostgreSQL Documentation*.
9. RFC 8785, *JSON Canonicalization Scheme*.
10. Martin Kleppmann, *Designing Data-Intensive Applications*, O'Reilly, 2017.
11. Pat Helland, "Life Beyond Distributed Transactions: An Apostate's Opinion," CIDR, 2007.
12. Leslie Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System," CACM, 1978.

## افشای استفاده از AI

ابزارهای AI برای Organization، Language Editing، Formatting و آماده‌سازی Manuscript بر اساس مواد معماری نویسنده استفاده شده‌اند. هیچ Measurement تجربی نباید از متن Draft استنباط شود. مسئولیت Architecture، Claim، Citation، Evidence و Verification نهایی با نویسنده انسانی است.


# پیوست فنی - چک‌لیست معماری

### A.1 وضعیت معماری و مرز ادعا
Z0-A خط مبنای طراحی تثبیت‌شده است، نه گواهی آمادگی Production. هر ادعای اجرایی فقط با Evidence مخصوص همان Claim ارتقا پیدا می‌کند. نکات Verification: design freeze is separate from deployment؛ no autonomous-evolution claim؛ no biological or consciousness claim؛ evidence status remains independently versioned.

### A.2 حکم نهایی معماری
منبع حقیقت باید خارج از Cognition قابل تعویض، Session ارائه‌دهنده، Interface، Telemetry implementation و Development Agent باقی بماند. نکات Verification: accepted change moves known canonical state to new canonical state؛ explicit authority؛ commit-time CAS؛ intent-bound idempotency؛ append-oriented accepted history.

### A.3 توپولوژی ثابت پنج‌Plane
توپولوژی هنجاری دقیقاً شامل Canonical Spine، Operational، Observation، Development/Mason و Evidence/Governance است. نکات Verification: Cognition is an Operational service؛ Ingress is an Operational service؛ Observation is not canonical truth؛ Mason is not a promotion authority.

### A.4 مالکیت Canonical Spine
Spine مالک Identity پاسخ‌گو، Event History پذیرفته‌شده، Head و Revision کاننیکال، Checkpoint reference، Authorization و تاریخچه Activation است. نکات Verification: models cannot write directly؛ telemetry cannot rewrite state؛ commits require governed interface؛ history corrections are new events.

### A.5 Operational Plane
سرویس‌های Operational کار واقعی را انجام می‌دهند: Task، Role، RoleBinding، Cognition routing، Context loading، Connector، Outbox dispatch و Effect settlement. نکات Verification: provider identifiers are provenance؛ workflow engines are not source of truth؛ task state must survive process loss؛ effects remain explicit obligations.

### A.6 Observation Plane
Observation تلهمتری خام را می‌گیرد و به‌صورت مستقل Measurement، SLO result، Invariant result و gap_signal قابل انتساب تولید می‌کند. نکات Verification: loss of telemetry must not break replay؛ detector version recorded؛ windowing recorded؛ Mason cannot choose its own evidence window.

### A.7 Development / Mason Plane
Mason یک قابلیت توسعه Proposal-only است که Gap معتبر را مصرف و Candidate Phenotype Revision بازگشت‌پذیر تولید می‌کند. نکات Verification: cannot alter objectives؛ cannot alter hard constraints؛ cannot alter authority or identity؛ cannot self-evaluate؛ cannot self-promote.

### A.8 Evidence / Governance Plane
Evidence/Governance مالک Predicate، Falsifier، Evidence Reference، Evaluation Receipt، Approval Policy، Promotion Gate و Audit است. نکات Verification: PASS does not propagate to unrelated claims؛ OPEN means required evidence is absent؛ human approval is not the only security boundary؛ promotion is separately authorized.

### A.9 شیء World
World بالاترین Governance/Namespace boundary است، نه Session مدل یا Agent تعریف‌شده فقط با Prompt. نکات Verification: contains constitutional invariants؛ contains canonical identifier namespace؛ can contain multiple entities and societies؛ tracks architecture/runtime lineage.

### A.10 مدل Entity
Entity یک شیء پایدار و پاسخ‌گو با Canonical ID ثابت، Lifecycle، State Head، Authority Ceiling و Event Lineage است. نکات Verification: entity survives provider replacement؛ entity is not a role name؛ entity can be individual or organizational؛ retirement does not silently recycle identity.

### A.11 Society و company-001
company-001 یک Entity/Society عملیاتی با History، Objective، Role، Task، Policy و Resource مستقل است. نکات Verification: society can host multiple roles؛ society identity persists across executors؛ role changes do not fork society identity؛ organizational state is canonical where required.

### A.12 مدل Role
Role جایگاه مسئولیت با Contract نسخه‌دار است؛ به‌صورت خودکار Entity با هویت مستقل نیست. نکات Verification: examples: secretary, sales, accountant؛ role name does not mint authority؛ role can require skills؛ role output contract is versioned.

### A.13 RoleBinding
RoleBinding اتصال Governed است که Role را برای Holder/Executor در Scope و Grant محدود فعال می‌کند. نکات Verification: provider-neutral binding؛ scope and validity explicit؛ authority grant bounded by ceilings؛ binding changes are auditable.

### A.14 Holder و Executor
Holder/Executor جاری می‌تواند Human Proxy، Runtime مبتنی بر LLM، سرویس deterministic، Shared Runtime یا Dedicated Entity باشد. نکات Verification: holder is operational provenance؛ holder replacement need not replace entity؛ holder capabilities remain bounded؛ credentials are scoped.

### A.15 Task و Task Bus
Task واحد کار Governed با ID، State، Role/Scope، Artifact، Approval، Output و Provenance است؛ Task Bus پایدار Handoff را هماهنگ می‌کند. نکات Verification: task may cross providers؛ workflow engine state is not authoritative؛ retries preserve task identity؛ terminal/waiting states are explicit.

### A.16 مدل Skill
Skill یک Capability Contract قابل استفاده مجدد است و تا زمانی که Identity/Authority/State/Lifecycle مستقل لازم نباشد در Library/Runtime می‌ماند. نکات Verification: skills do not mint authority؛ repeated behavior may become deterministic skill؛ role may bind skills؛ entity birth is a separate governance decision.

### A.17 هویت مستقل از Provider
Provider، Model، Session، Thread و Channel فقط Provenance هستند؛ Canonical Identity نباید از آن‌ها مشتق شود. نکات Verification: provider handoff preserves World/Entity/Role/Task IDs؛ provider switch may be recorded as provenance؛ identity change requires canonical event؛ session closure is not identity death.

### A.18 Objective Contract
Goal و Boundary سخت در Objective Contract کاننیکال، Immutable و Versioned ذخیره می‌شوند، نه فقط داخل Prompt. نکات Verification: objective؛ success metrics and SLOs؛ hard constraints؛ authority ceiling؛ risk class؛ observation contract؛ allowed adaptation surface؛ promotion policy.

### A.19 مسیر تغییر قانون اساسی
تغییر Objective، Hard Constraint، Authority Ceiling، Identity Rule یا Constitutional invariant یک Optimization معمولی Mason نیست. نکات Verification: separate governance authorization؛ stronger evidence/approval؛ versioned change؛ rollback/transition plan؛ audit trail.

### A.20 Phenotype Revision
Phenotype Revision تغییر Candidate اجرایی/Configuration نسخه‌دار است که به Parent Revision و Objective Version مشخص متصل است. نکات Verification: change set؛ migration plan؛ rollback plan؛ expected metrics؛ risk؛ evidence requirements؛ candidate status before activation.

### A.21 جبر Authority
Effective Authority حاصل Intersection بین Entity Ceiling، RoleBinding Grant فعال، Task Grant احتمالی، Policy Allowance و Temporal/Scope validity است. نکات Verification: edges are conditions not grants؛ role names do not grant؛ authority expansion is privileged؛ fail closed on ambiguity.

### A.22 رکورد Authorization
هر Canonical Change یا External Effect حساس باید به Authorization Record یا Authority Context قابل استنتاج متصل باشد. نکات Verification: principal identity؛ scope؛ required capability؛ grant source؛ expiry؛ risk class؛ policy decision.

### A.23 Schema رویداد کاننیکال
Canonical Event محتوای معنایی، Lineage، Authority، Objective/Revision context، شرط Concurrency و Provenance را bind می‌کند. نکات Verification: event_id unique؛ event_version explicit؛ expected/previous head؛ intent hash؛ payload hash؛ fencing token؛ evidence refs.

### A.24 Commit-time CAS
Expected Head باید داخل همان Transactionی بررسی شود که Canonical Head را Advance می‌کند؛ Pre-read در Application کافی نیست. نکات Verification: two writers one head: only one commits؛ stale writer fails closed؛ no silent overwrite؛ retry requires new proposal or rebase.

### A.25 Idempotency متصل به Intent
Idempotency Key به Semantic Intent bind است؛ Retry یکسان Deduplicate می‌شود ولی استفاده همان Key برای Intent متفاوت Collision است. نکات Verification: durable idempotency record؛ semantic hash؛ target/type included؛ collision is explicit.

### A.26 Transition کاننیکال اتمیک
Event Append، Head Advance، Projection ضروری و ایجاد Outbox Obligation برای Transition Governed به‌صورت Atomic coupled هستند. نکات Verification: fault injection must not create half-state؛ transaction rollback on partial failure؛ analytical projections may be asynchronous؛ authoritative minimum remains atomic.

### A.27 Transactional Outbox
External Effect به‌صورت Obligation ثبت‌شده همراه Intent کاننیکال مدل می‌شود و بعد Effect Executor آن را claim می‌کند. نکات Verification: obligation has stable id؛ attempts audited؛ provider id captured؛ ambiguous outcome reconciled.

### A.28 Effect Receipt
موفقیت یا Settlement اثر بیرونی با Receipt ثبت می‌شود که Obligation، Attempt، Connector، Provider result و Reconciliation state را متصل می‌کند. نکات Verification: scoped effectively-once only؛ no universal exactly-once claim؛ duplicate protection connector-specific؛ irreversible ambiguity is first-class.

### A.29 Sequencer Lease
Sequencer Lease Authority جاری برای Serialization یک Scope را مشخص می‌کند و Expiry/Renewal صریح دارد. نکات Verification: lease state durable for claim scope؛ single active authority or equivalent serialization؛ expired holder cannot be trusted by itself؛ monitor lease health.

### A.30 Fencing Token
هر Sequencer Epoch یک Fencing Token افزایشی می‌گیرد تا Process قدیمی حتی اگر زنده بماند Reject شود. نکات Verification: storage-side validation؛ stale token rejection؛ fresh token after failover؛ fresh higher token after restore.

### A.31 Append-only در سطح DB
History متعهدشده با Privilege/Control پایگاه‌داده محافظت می‌شود، نه فقط Convention کد. نکات Verification: runtime roles denied UPDATE؛ denied DELETE؛ denied TRUNCATE؛ correction is a new event؛ break-glass admin is audited.

### A.32 Canonicalization و Hash
Semantic Hash از Serialization deterministic و Formula نسخه‌دار استفاده می‌کند تا Content و Chain قابل Verify باشد. نکات Verification: RFC 8785/JCS is a suitable reference؛ hash binds previous head and semantic content؛ hash is tamper-evidence؛ hash is not confidentiality or authorization.

### A.33 مدل Checkpoint
Checkpoint یک State materialized متصل به Canonical Head و Reducer/Schema Version است؛ Recovery را سریع می‌کند ولی جای History پذیرفته‌شده را نمی‌گیرد. نکات Verification: checkpoint hash/reference؛ version compatibility؛ periodic verification؛ stale checkpoints detected.

### A.34 Replay تاییدشده
Replay قبل از Materialization، Chain، Hash، Event Version، Duplicate ID، Ordering، Reducer Compatibility و Final Head را Verify می‌کند. نکات Verification: corruption fails closed؛ mutation removing hash check must be caught؛ duplicate event id rejected؛ unsupported version requires migration path.

### A.35 Clean-host Restore
Continuity با Restart همان Process ثابت نمی‌شود. Recovery باید روی Clean Environment بازسازی شود و سپس Fresh Governed Write بپذیرد. نکات Verification: different system identity؛ restore schema/data؛ verify chain/head/objective/revision؛ recreate separated credentials؛ fresh lease/fencing؛ record RTO/RPO and restore receipt.

### A.36 Ingress و Routing
External Input Normalize و در صورت نیاز Authenticate می‌شود، به Entity/Task/Role Scope resolve می‌شود و بدون Direct Truth Mutation Route می‌گردد. نکات Verification: channel-specific data stays provenance؛ routing decision auditable؛ unknown identity handled explicitly؛ input cannot bypass policy.

### A.37 Brain Gateway
Brain Gateway مستقل از Provider، Cognition قابل تعویض را با Scoped Context، Role Contract، Tool Description، Authority Limit و Output Schema فراخوانی می‌کند. نکات Verification: ChatGPT/Grok/DeepSeek/Gemini/Claude/local/deterministic possible؛ provider selection by policy؛ brain output is proposal/result؛ brain cannot directly commit.

### A.38 Context Compiler با K0 تا K4
Context بر اساس Scope کامپایل می‌شود: World Kernel، Entity/Society Context، Role Contract، Current Task و حداقل Evidence/Memory دارای Provenance. نکات Verification: minimize context without losing invariants؛ source remains outside generated summary؛ staleness tracked؛ provider context window is not canonical memory.

### A.39 معماری Memory
Retrieval Memory از Authoritative State جداست و می‌تواند Working، Episodic، Semantic، Document/Evidence، Cold Archive و Protected Vault داشته باشد. نکات Verification: summary does not replace source؛ vector index is rebuildable projection؛ provenance and timestamps retained؛ retention/privacy policy explicit.

### A.40 Observation Pipeline
Pipeline هنجاری raw telemetry -> normalization -> aggregation/windowing -> SLO/invariant evaluation -> gap_signal -> Evidence Registry است. نکات Verification: detector outside Mason؛ source refs retained؛ window and method recorded؛ coverage gaps explicit.

### A.41 قرارداد SLO و Invariant
Success Metric و Invariant به‌عنوان بخشی از Objective/Observation Contract نسخه‌دارند تا Optimization با Target پایدار سنجیده شود. نکات Verification: threshold changes are versioned؛ identity continuity can be invariant؛ authorization-before-effect can be invariant؛ restore success can be SLO/gate.

### A.42 Gap Signal
Gap یک Discrepancy قابل انتساب با Objective Version، Metric/Invariant، Window، Detector Version، Observed Value، Expected Condition و Evidence Ref است. نکات Verification: status OPEN/CLOSED/INVALIDATED/SUPERSEDED/EXPIRED؛ Mason does not own gap definition؛ confidence/severity optional but explicit؛ gap provenance immutable.

### A.43 قرارداد Proposal در Mason
Mason به Gap معتبر و Objective جاری reference می‌دهد، کوچک‌ترین Intervention reversible را پیشنهاد می‌کند، Test/Rollback می‌دهد و داخل Adaptation Surface می‌ماند. نکات Verification: proposal has parent revision؛ proposal has risk؛ proposal has expected metrics؛ forbidden fields rejected before evaluation.

### A.44 هویت Evaluator
هویت Evaluator باید به Principal احراز‌شده و Build/Profile دقیق قابل انتساب باشد؛ DB Constraint به‌تنهایی Proof کافی نیست. نکات Verification: principal id؛ credential/role ref؛ build digest؛ candidate/objective refs؛ environment/test digests؛ metrics/evidence؛ optional attestation/signature.

### A.45 Evaluation Receipt
Evaluation Receipt رکورد پایدار اتصال Evaluator، Candidate، Objective، Test Environment، Result، Metric و Evidence است. نکات Verification: PASS/FAIL/INCONCLUSIVE explicit؛ receipt immutable once committed؛ promotion references receipt؛ receipt does not store secrets.

### A.46 تفکیک وظایف
Observation اندازه‌گیری می‌کند، Mason Proposal می‌دهد، Evaluator قضاوت می‌کند، Promotion Authority ارتقا می‌دهد، Spine ثبت می‌کند و Effect Executor Obligation را settle می‌کند. نکات Verification: separate credentials for high assurance؛ single host may contain logical modules only at low evidence levels؛ self-approval forbidden؛ one actor controlling all stages violates Z0-A.

### A.47 Promotion Gate
Candidate فقط پس از Evidence/Policy Check و Promotion Decision مستقل می‌تواند با CAS فعال شود. نکات Verification: receipt required؛ hard constraints unchanged؛ authority unchanged unless constitutional path؛ stale active revision rejected؛ activation itself is canonical event.

### A.48 Rollback
Rollback یک Canonical Event جدید برای فعال کردن Known-good یا Repair Revision است و History شکست‌خورده را پاک نمی‌کند. نکات Verification: trigger recorded؛ incident/evidence refs؛ authority recorded؛ post-rollback verification؛ external effect compensation handled separately.

### A.49 سطوح Evidence از E0 تا E5
Evidence Level بین Definition، Static Artifact، Local Executable، Persistent Integration، Production-like Testing و Longitudinal Operation فرق می‌گذارد. نکات Verification: E0 defined؛ E1 static؛ E2 local/disposable؛ E3 persistent/integration؛ E4 restore/security/load/chaos/independent credentials؛ E5 longitudinal SLO/failure envelope.

### A.50 Proof Registry
هر Claim اصلی Predicate، Falsifier، Required Evidence Level، Status، Environment/Build و Evidence Reference مستقل دارد. نکات Verification: OPEN is not failure but absence of required proof؛ runner output should drive status؛ manual status cannot override evidence؛ claims do not inherit neighbor PASS.

### A.51 Threat Model
معماری Failure و Adversary را در Provider، Credential، Concurrency، Operator، Telemetry، Storage و External Effect در نظر می‌گیرد. نکات Verification: stale writer؛ compromised model؛ prompt injection؛ compromised Mason؛ evaluator substitution؛ credential theft؛ partial DB failure؛ corrupt backup؛ operator error.

### A.52 Secret و Credential
Secret Material خارج از Canonical Event Payload و Evaluation Receipt نگه داشته می‌شود و فقط Reference/Principal در Audit Durable می‌آید. نکات Verification: rotation does not change identity؛ logs scanned for leaks؛ least privilege؛ high-risk credentials separated.

### A.53 ماتریس DB Role
Roleهای PostgreSQL مرجع Sequencer، Observer، Mason، Evaluator، Effect Executor، Promotion Authority، Audit و Migration را جدا می‌کنند. نکات Verification: GRANT/REVOKE versioned؛ negative privilege tests؛ runtime cannot rewrite events؛ evaluator cannot promote؛ effect executor cannot self-authorize.

### A.54 مرز Service/API
Boundaryهای منطقی شامل Commit، Query/Projection، Task، Brain Gateway، Context Compiler، Observation، Gap Detection، Mason، Evaluation، Promotion، Effect و Recovery است. نکات Verification: not required to be microservices؛ contracts matter more than process count؛ capability boundaries explicit؛ API versions governed.

### A.55 Lifecycle State
Lifecycle Entity یک State Machine عملیاتی صریح است، نه تابع باز یا بسته بودن Session مدل. نکات Verification: PROVISIONED؛ ACTIVE؛ DEGRADED؛ FROZEN/QUARANTINED؛ HIBERNATED؛ RESTORED؛ RETIRED/TOMBSTONED.

### A.56 Health، Repair، Sleep و Wake
مفاهیم قبلی Health، Sleep/Wake، Repair، Freeze و Reconstruction فقط وقتی حفظ می‌شوند که به Transition و Evidence صریح نگاشت شوند. نکات Verification: sleep can reduce active cognition؛ wake reloads current canonical state؛ repair is governed revision/recovery؛ no biological claim.

### A.57 Multi-brain Routing
چند Provider شناخت می‌توانند پشت Brain Gateway باشند و بر اساس Capability، Cost، Latency، Privacy، Jurisdiction، Availability یا Policy انتخاب شوند. نکات Verification: fallback preserves identity؛ ensemble vote is not authority؛ provider metadata retained as provenance؛ hard constraints cannot weaken on fallback.

### A.58 رشد Skill به Role و Entity
رفتار موفق تکراری ممکن است Skill deterministic شود، Specialization پایدار Role توجیه کند و نیاز به Isolation/State مستقل Entity جدید را توجیه کند. نکات Verification: growth is evidence-driven؛ Mason cannot autonomously birth entities in Z0-A؛ authority ceilings inherited/bounded؛ genome/evolution language remains exploratory.

### A.59 Risk Class برای Effect
External Action بر اساس Reversibility و Impact طبقه‌بندی می‌شود تا Authorization/Evidence متناسب با Risk افزایش یابد. نکات Verification: read-only؛ reversible low-risk write؛ externally visible communication؛ financial/legal/contractual؛ destructive/high-impact.

### A.60 مدل Audit
Audit باید بازسازی کند چه کسی/چه چیزی، چه Actionی، تحت کدام Objective/Authority، روی کدام Head، با کدام Provider/Build و با چه Result انجام داده است. نکات Verification: link events/tasks/principals؛ link objective/revision؛ link effects/receipts؛ link gaps/evaluations/promotions؛ survives workflow engine loss.

### A.61 ماتریس Failure و Response
Failure Handling صریح است و هرجا Ambiguity بتواند Identity، Authority، History یا Effect برگشت‌ناپذیر را خراب کند Fail-closed می‌شود. نکات Verification: stale writer -> reject؛ collision -> reject؛ partial transaction -> rollback؛ telemetry outage -> coverage degraded؛ hash mismatch -> stop replay؛ ambiguous effect -> reconcile.

### A.62 Adversarial Testing
Testها عمداً Boundary را با Race، Stale Token، Duplicate ID، Privilege Violation، Corrupt Replay، Forbidden Mason Change و Stale Promotion حمله می‌کنند. نکات Verification: negative tests mandatory؛ fault injection؛ cross-provider continuity test؛ restore on clean host؛ effect ambiguity test.

### A.63 Mutation Testing
Mutation Gate ثابت می‌کند حذف Check حیاتی مثل Replay Hash Verification یا Idempotency Collision Handling باعث Fail شدن Test می‌شود. نکات Verification: avoid vacuous test counts؛ report mutation score by family؛ critical mutants cannot survive؛ runner/evidence registry linked.

### A.64 Deployment Profile
Evidence Level به Deployment Profile از Local Development تا Persistent Integration، Production-like با Credential جدا و Longitudinal Operation نگاشت می‌شود. نکات Verification: E2 local؛ E3 persistent integration؛ E4 restore/security/load/chaos؛ E5 longitudinal.

### A.65 معماری Backup
Backup شامل Canonical DB، Event History، Schema/Migration، Objective/Revision Artifact، Evidence Registry، Manifest و Protected Recovery Procedure است. نکات Verification: backup is not proof until restore tested؛ checksums and manifests؛ restore order documented؛ source code alone is insufficient.

### A.66 انضباط Repository و Release
Artifact هنجاری Versioned است و Stable Release immutable؛ Fix با Version، Manifest و Hash جدید منتشر می‌شود. نکات Verification: no secrets/private payloads in release؛ schema migrations versioned؛ rollback plan for destructive change؛ machine-readable contracts accompany prose.

### A.67 Lineage از World v6.2
World v6.2 اصول Entity Stability، Replaceable Brain، Scoped Context، Authority خارج از Cognition، Effect Handling، Evidence Gate و Recovery Discipline را به ارث گذاشت. نکات Verification: retained where compatible؛ older topology not automatically current؛ fractal/multi-brain ideas remain operational patterns؛ Z0-A is stricter about five planes.

### A.68 Lineage از World 7
World 7 Persistent Identity، Spine، Proposal-only Cognition، Expected-head Conflict، Idempotency، Hash Chain، Reconstruction و Proof Obligation صریح را تقویت کرد. نکات Verification: genomic metaphor moved out of normative core؛ autonomous evolution claim rejected without evidence؛ review exposed vacuous/self-referential tests؛ mutation and registry discipline strengthened.

### A.69 Lineage از World 8 v0.1/v0.1.1
World 8 v0.1/v0.1.1 Lineage عملیاتی world-001، company-001، RoleBindingها، Task Bus و Persistent Canonical History را فراهم می‌کند. نکات Verification: prior evidence remains valuable؛ new Z0-A gates require new evidence؛ Observation/Mason split is new fixed boundary؛ evaluator attribution is strengthened.

### A.70 برداشت‌های منسوخ
برداشت قدیمی متناقض فقط برای History حفظ می‌شود و نباید بی‌صدا به Current Architecture برگردد. نکات Verification: more than five normative planes؛ Role treated as Entity by name؛ Mason-controlled telemetry/gaps؛ direct self-promotion؛ objective only in prompt؛ hash chain called secure storage.

### A.71 عدم‌ادعاهای صریح
معماری Consciousness، Biological Life، AGI، Legal Personhood، Autonomous Evolution اثبات‌شده، Universal Exactly-once یا Production Readiness صرفاً با Freeze Design را ادعا نمی‌کند. نکات Verification: claim modesty is normative؛ metaphors are operational only؛ production requires E3/E4/E5 as applicable؛ security claims remain scoped.

### A.72 Safety Propertyهای رسمی
Claimهای Core به‌صورت Safety Property قابل ابطال بیان می‌شوند تا معماری با Test سنجیده شود نه با Metaphor. نکات Verification: provider replacement preserves identity؛ stale head cannot commit؛ stale fencing cannot commit؛ Mason cannot mutate hard boundaries؛ promotion requires attributed receipt؛ restore requires fresh write.

### A.73 Liveness Goal
System باید در نهایت Task معتبر را Resolve کند، Lease منقضی را جایگزین کند، Effect را Settle/Reconcile کند، Candidate را Decide کند، Entity را Recover کند و Gap را Close/Invalidate کند. نکات Verification: liveness never bypasses safety؛ timeouts become explicit states؛ stuck work is observable؛ manual escalation is allowed but audited.

### A.74 سناریوی End-to-End مرجع
Proof مرجع هر پنج Plane را لمس می‌کند: Task پایدار، Provider Handoff، Governed Commit، Effect Receipt واقعی کم‌ریسک، SLO Breach، Mason Proposal، Evaluation مستقل و Promotion جدا. نکات Verification: same entity/task identity across provider change؛ effect authorization/outbox/receipt؛ gap from predefined SLO؛ revision activated with CAS.

### A.75 Roadmap اجرایی Z0-A
پیاده‌سازی از Freeze Contract به Spine Hardening، Entity/Role، Objective/Revision، Observation، Mason، Evaluation، Promotion، Recovery و Operational Proof می‌رود. نکات Verification: Z0A-0 contracts؛ Z0A-1 spine؛ Z0A-2 identity/role؛ Z0A-3 objective/revision؛ Z0A-4 observation؛ Z0A-5 mason؛ Z0A-6 evaluator؛ Z0A-7 promotion؛ Z0A-8 restore؛ Z0A-9 operational proof.

### A.76 Gateهای خروج Z0-A
قبل از Closed شدن Gate، Architecture و Executable Boundary باید هم‌خوان باشند؛ Compliance فقط در Document کافی نیست. نکات Verification: G1 plane isolation؛ G2 entity/role split؛ G3 objective/revision versioning؛ G4 observation independence؛ G5 Mason confinement؛ G6 evaluator identity؛ G7 spine atomicity؛ G8 recovery؛ G9 effects.

### A.77 Runbook بازسازی برای Maintainer آینده
Maintainer آینده از Version تثبیت‌شده شروع می‌کند، Manifest/Schema، Proof/Role Matrix، Replay، Adversarial Gate و Restore Receipt را Verify می‌کند و بعد Development را ادامه می‌دهد. نکات Verification: do not trust old diagrams over current manifest؛ verify active objective/revision؛ verify evaluator attribution؛ verify latest restore؛ verify provider handoff and effect reconciliation.

### A.78 حداقل Artifact ماشین‌خوان
Prose باید کنار Schema، Role Matrix، Forbidden Transition، Promotion Policy، Proof Registry، Runtime Module، Observation Module، Evidence و Release Manifest باشد. نکات Verification: Objective schema؛ Revision schema؛ Event schema؛ Gap schema؛ Evaluation receipt schema؛ RoleBinding schema؛ Outbox/effect schema؛ DB role matrix؛ proof registry.

### A.79 قرارداد نهایی Continuity
Cognition و Interface قابل تعویض‌اند؛ Identity پاسخ‌گو، Canonical State، Authority، Objective، Accepted History و Evidence Governed و Persistent می‌مانند. نکات Verification: prose and runtime must agree؛ no bypass path؛ all stronger claims remain evidence-gated؛ future revisions require explicit governance.