# World 8 / Z0-A - سند جامع و آرشیوی معماری کامل

**Runtime پایدار مستقل از Provider با Observation مستقل و Development Proposal-only**

**وضعیت:** FINAL DESIGN BASELINE / NOT PRODUCTION / ARCHIVAL MASTER

**تاریخ تثبیت:** 2026-08-24

**هدف آرشیوی:** این نسخه برای بازسازی پروژه در آینده نوشته شده و عمداً از نسخه کوتاه مفصل‌تر است. متن استخراج‌شده کامل از Baseline نهایی، Roadmap و Cross-Review Closure نیز در پیوست‌ها بدون حذف نگه داشته شده است.


## 1. وضعیت معماری و مرز ادعا

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Z0-A خط مبنای طراحی تثبیت‌شده است، نه گواهی آمادگی Production. هر ادعای اجرایی فقط با Evidence مخصوص همان Claim ارتقا پیدا می‌کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `design freeze is separate from deployment`
- `no autonomous-evolution claim`
- `no biological or consciousness claim`
- `evidence status remains independently versioned`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 2. حکم نهایی معماری

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

منبع حقیقت باید خارج از Cognition قابل تعویض، Session ارائه‌دهنده، Interface، Telemetry implementation و Development Agent باقی بماند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `accepted change moves known canonical state to new canonical state`
- `explicit authority`
- `commit-time CAS`
- `intent-bound idempotency`
- `append-oriented accepted history`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 3. توپولوژی ثابت پنج‌Plane

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

توپولوژی هنجاری دقیقاً شامل Canonical Spine، Operational، Observation، Development/Mason و Evidence/Governance است.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `Cognition is an Operational service`
- `Ingress is an Operational service`
- `Observation is not canonical truth`
- `Mason is not a promotion authority`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 4. مالکیت Canonical Spine

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Spine مالک Identity پاسخ‌گو، Event History پذیرفته‌شده، Head و Revision کاننیکال، Checkpoint reference، Authorization و تاریخچه Activation است.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `models cannot write directly`
- `telemetry cannot rewrite state`
- `commits require governed interface`
- `history corrections are new events`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 5. Operational Plane

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

سرویس‌های Operational کار واقعی را انجام می‌دهند: Task، Role، RoleBinding، Cognition routing، Context loading، Connector، Outbox dispatch و Effect settlement.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `provider identifiers are provenance`
- `workflow engines are not source of truth`
- `task state must survive process loss`
- `effects remain explicit obligations`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 6. Observation Plane

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Observation تلهمتری خام را می‌گیرد و به‌صورت مستقل Measurement، SLO result، Invariant result و gap_signal قابل انتساب تولید می‌کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `loss of telemetry must not break replay`
- `detector version recorded`
- `windowing recorded`
- `Mason cannot choose its own evidence window`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 7. Development / Mason Plane

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Mason یک قابلیت توسعه Proposal-only است که Gap معتبر را مصرف و Candidate Phenotype Revision بازگشت‌پذیر تولید می‌کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `cannot alter objectives`
- `cannot alter hard constraints`
- `cannot alter authority or identity`
- `cannot self-evaluate`
- `cannot self-promote`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 8. Evidence / Governance Plane

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Evidence/Governance مالک Predicate، Falsifier، Evidence Reference، Evaluation Receipt، Approval Policy، Promotion Gate و Audit است.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `PASS does not propagate to unrelated claims`
- `OPEN means required evidence is absent`
- `human approval is not the only security boundary`
- `promotion is separately authorized`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 9. شیء World

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

World بالاترین Governance/Namespace boundary است، نه Session مدل یا Agent تعریف‌شده فقط با Prompt.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `contains constitutional invariants`
- `contains canonical identifier namespace`
- `can contain multiple entities and societies`
- `tracks architecture/runtime lineage`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 10. مدل Entity

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Entity یک شیء پایدار و پاسخ‌گو با Canonical ID ثابت، Lifecycle، State Head، Authority Ceiling و Event Lineage است.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `entity survives provider replacement`
- `entity is not a role name`
- `entity can be individual or organizational`
- `retirement does not silently recycle identity`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 11. Society و company-001

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

company-001 یک Entity/Society عملیاتی با History، Objective، Role، Task، Policy و Resource مستقل است.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `society can host multiple roles`
- `society identity persists across executors`
- `role changes do not fork society identity`
- `organizational state is canonical where required`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 12. مدل Role

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Role جایگاه مسئولیت با Contract نسخه‌دار است؛ به‌صورت خودکار Entity با هویت مستقل نیست.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `examples: secretary, sales, accountant`
- `role name does not mint authority`
- `role can require skills`
- `role output contract is versioned`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 13. RoleBinding

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

RoleBinding اتصال Governed است که Role را برای Holder/Executor در Scope و Grant محدود فعال می‌کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `provider-neutral binding`
- `scope and validity explicit`
- `authority grant bounded by ceilings`
- `binding changes are auditable`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 14. Holder و Executor

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Holder/Executor جاری می‌تواند Human Proxy، Runtime مبتنی بر LLM، سرویس deterministic، Shared Runtime یا Dedicated Entity باشد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `holder is operational provenance`
- `holder replacement need not replace entity`
- `holder capabilities remain bounded`
- `credentials are scoped`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 15. Task و Task Bus

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Task واحد کار Governed با ID، State، Role/Scope، Artifact، Approval، Output و Provenance است؛ Task Bus پایدار Handoff را هماهنگ می‌کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `task may cross providers`
- `workflow engine state is not authoritative`
- `retries preserve task identity`
- `terminal/waiting states are explicit`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 16. مدل Skill

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Skill یک Capability Contract قابل استفاده مجدد است و تا زمانی که Identity/Authority/State/Lifecycle مستقل لازم نباشد در Library/Runtime می‌ماند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `skills do not mint authority`
- `repeated behavior may become deterministic skill`
- `role may bind skills`
- `entity birth is a separate governance decision`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 17. هویت مستقل از Provider

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Provider، Model، Session، Thread و Channel فقط Provenance هستند؛ Canonical Identity نباید از آن‌ها مشتق شود.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `provider handoff preserves World/Entity/Role/Task IDs`
- `provider switch may be recorded as provenance`
- `identity change requires canonical event`
- `session closure is not identity death`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 18. Objective Contract

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Goal و Boundary سخت در Objective Contract کاننیکال، Immutable و Versioned ذخیره می‌شوند، نه فقط داخل Prompt.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `objective`
- `success metrics and SLOs`
- `hard constraints`
- `authority ceiling`
- `risk class`
- `observation contract`
- `allowed adaptation surface`
- `promotion policy`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.



### Objective Contract Schema مرجع
```json
{
  "objective_contract_id": "obj-...",
  "version": 1,
  "scope": "world|entity|role|task",
  "objective": "...",
  "success_metrics_and_slos": [],
  "hard_constraints": [],
  "authority_ceiling": [],
  "risk_class": "...",
  "observation_contract": {},
  "allowed_adaptation_surface": [],
  "promotion_policy": {},
  "created_by": "...",
  "created_at": "...",
  "previous_version": null
}
```

### Phenotype Revision Schema مرجع
```json
{
  "phenotype_revision_id": "rev-...",
  "parent_revision_id": "rev-...",
  "objective_contract_id": "obj-...",
  "objective_version": 1,
  "change_set": [],
  "migration_plan": {},
  "rollback_plan": {},
  "expected_metrics": [],
  "risk": {},
  "evidence_requirements": [],
  "proposal_origin": "human|mason|other",
  "status": "CANDIDATE"
}
```

### Canonical Event Schema مرجع
```json
{
  "event_id": "evt-...",
  "world_id": "world-001",
  "entity_id": "company-001",
  "event_type": "...",
  "event_version": 1,
  "occurred_at": "...",
  "committed_at": "...",
  "actor_principal": "...",
  "authority_ref": "...",
  "task_id": "...",
  "objective_ref": {"id":"obj-...","version":1},
  "expected_head": "...",
  "previous_head": "...",
  "idempotency_key": "...",
  "intent_hash": "...",
  "payload": {},
  "payload_hash": "...",
  "event_hash": "...",
  "fencing_token": 42,
  "evidence_refs": []
}
```

### Gap Signal Schema مرجع
```json
{
  "gap_id": "gap-...",
  "objective_ref": {"id":"obj-...","version":1},
  "metric_or_invariant_id": "...",
  "window": {"start":"...","end":"..."},
  "detector_version": "...",
  "observed_value": "...",
  "expected_condition": "...",
  "severity": "...",
  "telemetry_refs": [],
  "provenance": {},
  "status": "OPEN"
}
```

### Evaluation Receipt Schema مرجع
```json
{
  "evaluation_receipt_id": "eval-...",
  "evaluator_principal_id": "...",
  "evaluator_role_or_credential_ref": "...",
  "evaluator_build_digest": "...",
  "candidate_revision_id": "...",
  "objective_ref": {"id":"obj-...","version":1},
  "test_suite_digest": "...",
  "environment_digest": "...",
  "result": "PASS|FAIL|INCONCLUSIVE",
  "metrics": {},
  "evidence_refs": [],
  "evaluated_at": "...",
  "attestation_or_signature": null
}
```


## 19. مسیر تغییر قانون اساسی

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

تغییر Objective، Hard Constraint، Authority Ceiling، Identity Rule یا Constitutional invariant یک Optimization معمولی Mason نیست.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `separate governance authorization`
- `stronger evidence/approval`
- `versioned change`
- `rollback/transition plan`
- `audit trail`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 20. Phenotype Revision

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Phenotype Revision تغییر Candidate اجرایی/Configuration نسخه‌دار است که به Parent Revision و Objective Version مشخص متصل است.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `change set`
- `migration plan`
- `rollback plan`
- `expected metrics`
- `risk`
- `evidence requirements`
- `candidate status before activation`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 21. جبر Authority

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Effective Authority حاصل Intersection بین Entity Ceiling، RoleBinding Grant فعال، Task Grant احتمالی، Policy Allowance و Temporal/Scope validity است.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `edges are conditions not grants`
- `role names do not grant`
- `authority expansion is privileged`
- `fail closed on ambiguity`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 22. رکورد Authorization

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

هر Canonical Change یا External Effect حساس باید به Authorization Record یا Authority Context قابل استنتاج متصل باشد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `principal identity`
- `scope`
- `required capability`
- `grant source`
- `expiry`
- `risk class`
- `policy decision`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 23. Schema رویداد کاننیکال

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Canonical Event محتوای معنایی، Lineage، Authority، Objective/Revision context، شرط Concurrency و Provenance را bind می‌کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `event_id unique`
- `event_version explicit`
- `expected/previous head`
- `intent hash`
- `payload hash`
- `fencing token`
- `evidence refs`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 24. Commit-time CAS

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Expected Head باید داخل همان Transactionی بررسی شود که Canonical Head را Advance می‌کند؛ Pre-read در Application کافی نیست.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `two writers one head: only one commits`
- `stale writer fails closed`
- `no silent overwrite`
- `retry requires new proposal or rebase`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 25. Idempotency متصل به Intent

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Idempotency Key به Semantic Intent bind است؛ Retry یکسان Deduplicate می‌شود ولی استفاده همان Key برای Intent متفاوت Collision است.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `durable idempotency record`
- `semantic hash`
- `target/type included`
- `collision is explicit`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 26. Transition کاننیکال اتمیک

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Event Append، Head Advance، Projection ضروری و ایجاد Outbox Obligation برای Transition Governed به‌صورت Atomic coupled هستند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `fault injection must not create half-state`
- `transaction rollback on partial failure`
- `analytical projections may be asynchronous`
- `authoritative minimum remains atomic`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 27. Transactional Outbox

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

External Effect به‌صورت Obligation ثبت‌شده همراه Intent کاننیکال مدل می‌شود و بعد Effect Executor آن را claim می‌کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `obligation has stable id`
- `attempts audited`
- `provider id captured`
- `ambiguous outcome reconciled`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 28. Effect Receipt

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

موفقیت یا Settlement اثر بیرونی با Receipt ثبت می‌شود که Obligation، Attempt، Connector، Provider result و Reconciliation state را متصل می‌کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `scoped effectively-once only`
- `no universal exactly-once claim`
- `duplicate protection connector-specific`
- `irreversible ambiguity is first-class`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 29. Sequencer Lease

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Sequencer Lease Authority جاری برای Serialization یک Scope را مشخص می‌کند و Expiry/Renewal صریح دارد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `lease state durable for claim scope`
- `single active authority or equivalent serialization`
- `expired holder cannot be trusted by itself`
- `monitor lease health`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 30. Fencing Token

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

هر Sequencer Epoch یک Fencing Token افزایشی می‌گیرد تا Process قدیمی حتی اگر زنده بماند Reject شود.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `storage-side validation`
- `stale token rejection`
- `fresh token after failover`
- `fresh higher token after restore`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 31. Append-only در سطح DB

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

History متعهدشده با Privilege/Control پایگاه‌داده محافظت می‌شود، نه فقط Convention کد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `runtime roles denied UPDATE`
- `denied DELETE`
- `denied TRUNCATE`
- `correction is a new event`
- `break-glass admin is audited`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 32. Canonicalization و Hash

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Semantic Hash از Serialization deterministic و Formula نسخه‌دار استفاده می‌کند تا Content و Chain قابل Verify باشد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `RFC 8785/JCS is a suitable reference`
- `hash binds previous head and semantic content`
- `hash is tamper-evidence`
- `hash is not confidentiality or authorization`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 33. مدل Checkpoint

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Checkpoint یک State materialized متصل به Canonical Head و Reducer/Schema Version است؛ Recovery را سریع می‌کند ولی جای History پذیرفته‌شده را نمی‌گیرد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `checkpoint hash/reference`
- `version compatibility`
- `periodic verification`
- `stale checkpoints detected`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 34. Replay تاییدشده

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Replay قبل از Materialization، Chain، Hash، Event Version، Duplicate ID، Ordering، Reducer Compatibility و Final Head را Verify می‌کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `corruption fails closed`
- `mutation removing hash check must be caught`
- `duplicate event id rejected`
- `unsupported version requires migration path`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 35. Clean-host Restore

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Continuity با Restart همان Process ثابت نمی‌شود. Recovery باید روی Clean Environment بازسازی شود و سپس Fresh Governed Write بپذیرد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `different system identity`
- `restore schema/data`
- `verify chain/head/objective/revision`
- `recreate separated credentials`
- `fresh lease/fencing`
- `record RTO/RPO and restore receipt`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 36. Ingress و Routing

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

External Input Normalize و در صورت نیاز Authenticate می‌شود، به Entity/Task/Role Scope resolve می‌شود و بدون Direct Truth Mutation Route می‌گردد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `channel-specific data stays provenance`
- `routing decision auditable`
- `unknown identity handled explicitly`
- `input cannot bypass policy`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 37. Brain Gateway

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Brain Gateway مستقل از Provider، Cognition قابل تعویض را با Scoped Context، Role Contract، Tool Description، Authority Limit و Output Schema فراخوانی می‌کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `ChatGPT/Grok/DeepSeek/Gemini/Claude/local/deterministic possible`
- `provider selection by policy`
- `brain output is proposal/result`
- `brain cannot directly commit`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 38. Context Compiler با K0 تا K4

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Context بر اساس Scope کامپایل می‌شود: World Kernel، Entity/Society Context، Role Contract، Current Task و حداقل Evidence/Memory دارای Provenance.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `minimize context without losing invariants`
- `source remains outside generated summary`
- `staleness tracked`
- `provider context window is not canonical memory`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 39. معماری Memory

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Retrieval Memory از Authoritative State جداست و می‌تواند Working، Episodic، Semantic، Document/Evidence، Cold Archive و Protected Vault داشته باشد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `summary does not replace source`
- `vector index is rebuildable projection`
- `provenance and timestamps retained`
- `retention/privacy policy explicit`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 40. Observation Pipeline

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Pipeline هنجاری raw telemetry -> normalization -> aggregation/windowing -> SLO/invariant evaluation -> gap_signal -> Evidence Registry است.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `detector outside Mason`
- `source refs retained`
- `window and method recorded`
- `coverage gaps explicit`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 41. قرارداد SLO و Invariant

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Success Metric و Invariant به‌عنوان بخشی از Objective/Observation Contract نسخه‌دارند تا Optimization با Target پایدار سنجیده شود.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `threshold changes are versioned`
- `identity continuity can be invariant`
- `authorization-before-effect can be invariant`
- `restore success can be SLO/gate`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 42. Gap Signal

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Gap یک Discrepancy قابل انتساب با Objective Version، Metric/Invariant، Window، Detector Version، Observed Value، Expected Condition و Evidence Ref است.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `status OPEN/CLOSED/INVALIDATED/SUPERSEDED/EXPIRED`
- `Mason does not own gap definition`
- `confidence/severity optional but explicit`
- `gap provenance immutable`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 43. قرارداد Proposal در Mason

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Mason به Gap معتبر و Objective جاری reference می‌دهد، کوچک‌ترین Intervention reversible را پیشنهاد می‌کند، Test/Rollback می‌دهد و داخل Adaptation Surface می‌ماند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `proposal has parent revision`
- `proposal has risk`
- `proposal has expected metrics`
- `forbidden fields rejected before evaluation`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 44. هویت Evaluator

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

هویت Evaluator باید به Principal احراز‌شده و Build/Profile دقیق قابل انتساب باشد؛ DB Constraint به‌تنهایی Proof کافی نیست.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `principal id`
- `credential/role ref`
- `build digest`
- `candidate/objective refs`
- `environment/test digests`
- `metrics/evidence`
- `optional attestation/signature`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 45. Evaluation Receipt

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Evaluation Receipt رکورد پایدار اتصال Evaluator، Candidate، Objective، Test Environment، Result، Metric و Evidence است.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `PASS/FAIL/INCONCLUSIVE explicit`
- `receipt immutable once committed`
- `promotion references receipt`
- `receipt does not store secrets`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 46. تفکیک وظایف

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Observation اندازه‌گیری می‌کند، Mason Proposal می‌دهد، Evaluator قضاوت می‌کند، Promotion Authority ارتقا می‌دهد، Spine ثبت می‌کند و Effect Executor Obligation را settle می‌کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `separate credentials for high assurance`
- `single host may contain logical modules only at low evidence levels`
- `self-approval forbidden`
- `one actor controlling all stages violates Z0-A`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 47. Promotion Gate

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Candidate فقط پس از Evidence/Policy Check و Promotion Decision مستقل می‌تواند با CAS فعال شود.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `receipt required`
- `hard constraints unchanged`
- `authority unchanged unless constitutional path`
- `stale active revision rejected`
- `activation itself is canonical event`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 48. Rollback

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Rollback یک Canonical Event جدید برای فعال کردن Known-good یا Repair Revision است و History شکست‌خورده را پاک نمی‌کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `trigger recorded`
- `incident/evidence refs`
- `authority recorded`
- `post-rollback verification`
- `external effect compensation handled separately`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 49. سطوح Evidence از E0 تا E5

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Evidence Level بین Definition، Static Artifact، Local Executable، Persistent Integration، Production-like Testing و Longitudinal Operation فرق می‌گذارد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `E0 defined`
- `E1 static`
- `E2 local/disposable`
- `E3 persistent/integration`
- `E4 restore/security/load/chaos/independent credentials`
- `E5 longitudinal SLO/failure envelope`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 50. Proof Registry

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

هر Claim اصلی Predicate، Falsifier، Required Evidence Level، Status، Environment/Build و Evidence Reference مستقل دارد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `OPEN is not failure but absence of required proof`
- `runner output should drive status`
- `manual status cannot override evidence`
- `claims do not inherit neighbor PASS`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 51. Threat Model

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

معماری Failure و Adversary را در Provider، Credential، Concurrency، Operator، Telemetry، Storage و External Effect در نظر می‌گیرد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `stale writer`
- `compromised model`
- `prompt injection`
- `compromised Mason`
- `evaluator substitution`
- `credential theft`
- `partial DB failure`
- `corrupt backup`
- `operator error`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 52. Secret و Credential

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Secret Material خارج از Canonical Event Payload و Evaluation Receipt نگه داشته می‌شود و فقط Reference/Principal در Audit Durable می‌آید.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `rotation does not change identity`
- `logs scanned for leaks`
- `least privilege`
- `high-risk credentials separated`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 53. ماتریس DB Role

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Roleهای PostgreSQL مرجع Sequencer، Observer، Mason، Evaluator، Effect Executor، Promotion Authority، Audit و Migration را جدا می‌کنند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `GRANT/REVOKE versioned`
- `negative privilege tests`
- `runtime cannot rewrite events`
- `evaluator cannot promote`
- `effect executor cannot self-authorize`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 54. مرز Service/API

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Boundaryهای منطقی شامل Commit، Query/Projection، Task، Brain Gateway، Context Compiler، Observation، Gap Detection، Mason، Evaluation، Promotion، Effect و Recovery است.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `not required to be microservices`
- `contracts matter more than process count`
- `capability boundaries explicit`
- `API versions governed`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 55. Lifecycle State

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Lifecycle Entity یک State Machine عملیاتی صریح است، نه تابع باز یا بسته بودن Session مدل.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `PROVISIONED`
- `ACTIVE`
- `DEGRADED`
- `FROZEN/QUARANTINED`
- `HIBERNATED`
- `RESTORED`
- `RETIRED/TOMBSTONED`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 56. Health، Repair، Sleep و Wake

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

مفاهیم قبلی Health، Sleep/Wake، Repair، Freeze و Reconstruction فقط وقتی حفظ می‌شوند که به Transition و Evidence صریح نگاشت شوند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `sleep can reduce active cognition`
- `wake reloads current canonical state`
- `repair is governed revision/recovery`
- `no biological claim`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 57. Multi-brain Routing

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

چند Provider شناخت می‌توانند پشت Brain Gateway باشند و بر اساس Capability، Cost، Latency، Privacy، Jurisdiction، Availability یا Policy انتخاب شوند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `fallback preserves identity`
- `ensemble vote is not authority`
- `provider metadata retained as provenance`
- `hard constraints cannot weaken on fallback`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 58. رشد Skill به Role و Entity

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

رفتار موفق تکراری ممکن است Skill deterministic شود، Specialization پایدار Role توجیه کند و نیاز به Isolation/State مستقل Entity جدید را توجیه کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `growth is evidence-driven`
- `Mason cannot autonomously birth entities in Z0-A`
- `authority ceilings inherited/bounded`
- `genome/evolution language remains exploratory`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 59. Risk Class برای Effect

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

External Action بر اساس Reversibility و Impact طبقه‌بندی می‌شود تا Authorization/Evidence متناسب با Risk افزایش یابد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `read-only`
- `reversible low-risk write`
- `externally visible communication`
- `financial/legal/contractual`
- `destructive/high-impact`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 60. مدل Audit

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Audit باید بازسازی کند چه کسی/چه چیزی، چه Actionی، تحت کدام Objective/Authority، روی کدام Head، با کدام Provider/Build و با چه Result انجام داده است.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `link events/tasks/principals`
- `link objective/revision`
- `link effects/receipts`
- `link gaps/evaluations/promotions`
- `survives workflow engine loss`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 61. ماتریس Failure و Response

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Failure Handling صریح است و هرجا Ambiguity بتواند Identity، Authority، History یا Effect برگشت‌ناپذیر را خراب کند Fail-closed می‌شود.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `stale writer -> reject`
- `collision -> reject`
- `partial transaction -> rollback`
- `telemetry outage -> coverage degraded`
- `hash mismatch -> stop replay`
- `ambiguous effect -> reconcile`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 62. Adversarial Testing

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Testها عمداً Boundary را با Race، Stale Token، Duplicate ID، Privilege Violation، Corrupt Replay، Forbidden Mason Change و Stale Promotion حمله می‌کنند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `negative tests mandatory`
- `fault injection`
- `cross-provider continuity test`
- `restore on clean host`
- `effect ambiguity test`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 63. Mutation Testing

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Mutation Gate ثابت می‌کند حذف Check حیاتی مثل Replay Hash Verification یا Idempotency Collision Handling باعث Fail شدن Test می‌شود.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `avoid vacuous test counts`
- `report mutation score by family`
- `critical mutants cannot survive`
- `runner/evidence registry linked`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 64. Deployment Profile

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Evidence Level به Deployment Profile از Local Development تا Persistent Integration، Production-like با Credential جدا و Longitudinal Operation نگاشت می‌شود.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `E2 local`
- `E3 persistent integration`
- `E4 restore/security/load/chaos`
- `E5 longitudinal`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 65. معماری Backup

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Backup شامل Canonical DB، Event History، Schema/Migration، Objective/Revision Artifact، Evidence Registry، Manifest و Protected Recovery Procedure است.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `backup is not proof until restore tested`
- `checksums and manifests`
- `restore order documented`
- `source code alone is insufficient`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 66. انضباط Repository و Release

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Artifact هنجاری Versioned است و Stable Release immutable؛ Fix با Version، Manifest و Hash جدید منتشر می‌شود.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `no secrets/private payloads in release`
- `schema migrations versioned`
- `rollback plan for destructive change`
- `machine-readable contracts accompany prose`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 67. Lineage از World v6.2

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

World v6.2 اصول Entity Stability، Replaceable Brain، Scoped Context، Authority خارج از Cognition، Effect Handling، Evidence Gate و Recovery Discipline را به ارث گذاشت.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `retained where compatible`
- `older topology not automatically current`
- `fractal/multi-brain ideas remain operational patterns`
- `Z0-A is stricter about five planes`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 68. Lineage از World 7

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

World 7 Persistent Identity، Spine، Proposal-only Cognition، Expected-head Conflict، Idempotency، Hash Chain، Reconstruction و Proof Obligation صریح را تقویت کرد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `genomic metaphor moved out of normative core`
- `autonomous evolution claim rejected without evidence`
- `review exposed vacuous/self-referential tests`
- `mutation and registry discipline strengthened`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 69. Lineage از World 8 v0.1/v0.1.1

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

World 8 v0.1/v0.1.1 Lineage عملیاتی world-001، company-001، RoleBindingها، Task Bus و Persistent Canonical History را فراهم می‌کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `prior evidence remains valuable`
- `new Z0-A gates require new evidence`
- `Observation/Mason split is new fixed boundary`
- `evaluator attribution is strengthened`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 70. برداشت‌های منسوخ

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

برداشت قدیمی متناقض فقط برای History حفظ می‌شود و نباید بی‌صدا به Current Architecture برگردد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `more than five normative planes`
- `Role treated as Entity by name`
- `Mason-controlled telemetry/gaps`
- `direct self-promotion`
- `objective only in prompt`
- `hash chain called secure storage`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 71. عدم‌ادعاهای صریح

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

معماری Consciousness، Biological Life، AGI، Legal Personhood، Autonomous Evolution اثبات‌شده، Universal Exactly-once یا Production Readiness صرفاً با Freeze Design را ادعا نمی‌کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `claim modesty is normative`
- `metaphors are operational only`
- `production requires E3/E4/E5 as applicable`
- `security claims remain scoped`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 72. Safety Propertyهای رسمی

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Claimهای Core به‌صورت Safety Property قابل ابطال بیان می‌شوند تا معماری با Test سنجیده شود نه با Metaphor.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `provider replacement preserves identity`
- `stale head cannot commit`
- `stale fencing cannot commit`
- `Mason cannot mutate hard boundaries`
- `promotion requires attributed receipt`
- `restore requires fresh write`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 73. Liveness Goal

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

System باید در نهایت Task معتبر را Resolve کند، Lease منقضی را جایگزین کند، Effect را Settle/Reconcile کند، Candidate را Decide کند، Entity را Recover کند و Gap را Close/Invalidate کند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `liveness never bypasses safety`
- `timeouts become explicit states`
- `stuck work is observable`
- `manual escalation is allowed but audited`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 74. سناریوی End-to-End مرجع

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Proof مرجع هر پنج Plane را لمس می‌کند: Task پایدار، Provider Handoff، Governed Commit، Effect Receipt واقعی کم‌ریسک، SLO Breach، Mason Proposal، Evaluation مستقل و Promotion جدا.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `same entity/task identity across provider change`
- `effect authorization/outbox/receipt`
- `gap from predefined SLO`
- `revision activated with CAS`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 75. Roadmap اجرایی Z0-A

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

پیاده‌سازی از Freeze Contract به Spine Hardening، Entity/Role، Objective/Revision، Observation، Mason، Evaluation، Promotion، Recovery و Operational Proof می‌رود.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `Z0A-0 contracts`
- `Z0A-1 spine`
- `Z0A-2 identity/role`
- `Z0A-3 objective/revision`
- `Z0A-4 observation`
- `Z0A-5 mason`
- `Z0A-6 evaluator`
- `Z0A-7 promotion`
- `Z0A-8 restore`
- `Z0A-9 operational proof`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 76. Gateهای خروج Z0-A

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

قبل از Closed شدن Gate، Architecture و Executable Boundary باید هم‌خوان باشند؛ Compliance فقط در Document کافی نیست.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `G1 plane isolation`
- `G2 entity/role split`
- `G3 objective/revision versioning`
- `G4 observation independence`
- `G5 Mason confinement`
- `G6 evaluator identity`
- `G7 spine atomicity`
- `G8 recovery`
- `G9 effects`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 77. Runbook بازسازی برای Maintainer آینده

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Maintainer آینده از Version تثبیت‌شده شروع می‌کند، Manifest/Schema، Proof/Role Matrix، Replay، Adversarial Gate و Restore Receipt را Verify می‌کند و بعد Development را ادامه می‌دهد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `do not trust old diagrams over current manifest`
- `verify active objective/revision`
- `verify evaluator attribution`
- `verify latest restore`
- `verify provider handoff and effect reconciliation`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 78. حداقل Artifact ماشین‌خوان

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Prose باید کنار Schema، Role Matrix، Forbidden Transition، Promotion Policy، Proof Registry، Runtime Module، Observation Module، Evidence و Release Manifest باشد.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `Objective schema`
- `Revision schema`
- `Event schema`
- `Gap schema`
- `Evaluation receipt schema`
- `RoleBinding schema`
- `Outbox/effect schema`
- `DB role matrix`
- `proof registry`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.


## 79. قرارداد نهایی Continuity

**وضعیت:** NORMATIVE مگر جایی که صریحاً برچسب دیگری خورده باشد.

Cognition و Interface قابل تعویض‌اند؛ Identity پاسخ‌گو، Canonical State، Authority، Objective، Accepted History و Evidence Governed و Persistent می‌مانند.

### دامنه و مالکیت
هدف این بخش این است که Ownership و Trust Boundary مبهم نماند. هر Object کاننیکال یا Governed که در طول زمان تغییر می‌کند باید شناسه پایدار و Version Reference مناسب داشته باشد. State موقت Runtime می‌تواند Cache یا Projection باشد، اما حق ندارد Authoritative Object را بی‌صدا بازتعریف کند. Provider، Workflow Engine، Model Call، UI و Telemetry در صورت حضور به‌عنوان Provenance ثبت می‌شوند و نباید به Canonical Identity ارتقا پیدا کنند.

### قواعد هنجاری
حداقل Requirementهای این بخش در فهرست زیر ثبت می‌شوند:
- `prose and runtime must agree`
- `no bypass path`
- `all stronger claims remain evidence-gated`
- `future revisions require explicit governance`

هرجا Ambiguity بتواند Identity، Authority، Accepted History، Objective Boundary، Revision Activation یا External Effect برگشت‌ناپذیر را تغییر دهد، رفتار باید Fail-closed باشد. Implementation آینده می‌تواند Storage، Batching، Cache یا Service decomposition را Optimize کند، اما Semantic Boundary را فقط با Architecture Version جدید و Governance صریح می‌تواند تغییر دهد.

### میان‌برهای ممنوع و تفسیر Failure
Happy-path موفق به‌تنهایی کافی نیست اگر Bypass Path وجود داشته باشد. Direct Write از Cognition قابل تعویض، Silent Overwrite روی State stale، Objective change بدون Version، Self-approval، Provenance ناقص یا سرایت PASS از Claim نامرتبط Failure معماری محسوب می‌شود. اگر Property در Evidence Level ادعاشده اثبات نشده باشد، Proof Registry باید OPEN یا FAIL بماند و متن معماری حق ارتقای مصنوعی آن را ندارد.

### تعهد Evidence
Evidence باید کوچک‌ترین Test بازتولیدپذیر را داشته باشد که Claim را بتواند Falsify کند، همراه Environment/Build Identity و Artifact Reference. در E3 و بالاتر، Persistent Storage، Process/Credential مستقل در صورت لزوم، Failure Injection و Recovery روی Integration هدف آزمون می‌شوند و از Mock محلی استنتاج نمی‌شوند.



# پیوست A - الگوریتم مرجع Commit

```text
BEGIN TRANSACTION
  authenticate principal
  load/verify authorization context
  verify active sequencer lease
  verify fencing_token >= current_fence and belongs to active epoch
  verify expected_head == canonical_head
  validate schema/event version
  compute semantic intent hash
  check idempotency record
    if same key + same intent: return prior committed result
    if same key + different intent: IDEMPOTENCY_COLLISION
  append canonical event
  advance canonical head
  update required authoritative projections
  create outbox obligation if external effect is planned
COMMIT
```

هیچ Pre-read در Application جای Predicate داخل Transaction را نمی‌گیرد. هیچ خروجی Model/Provider نمی‌تواند Authority/Commit Rule را bypass کند.

# پیوست B - ماتریس تفکیک وظایف

| Capability | مجاز | ممنوع |
|---|---|---|
| Promotion Authority / Human Root | Approve/Reject تحت Gate | Rewrite History یا جایگزین کردن Security Control فنی |
| Sequencer | Commit با Lease/Fencing/CAS معتبر | Self-approve Development Change |
| Observer | Measurement و Signal قابل انتساب | Canonical Mutation یا Objective rewrite برای Measurement خودش |
| Mason | Candidate Revision Proposal | Self-evaluate، Self-promote، تغییر Hard Boundary |
| Evaluator | Judge Candidate و Receipt | Promote همان Candidate |
| Effect Executor | Settle Obligation مجاز | ساخت Authorization برای خودش |
| Brain Provider | Cognition/Proposal/Result | مالکیت Canonical Identity یا Direct Commit |

# پیوست C - Negative Testهای اجباری

1. دو Writer با expected head یکسان: دقیقاً یکی Commit کند.
2. Same key + same intent: Deduplicate/Replay prior result.
3. Same key + changed intent: Collision صریح.
4. Stale fencing token: Reject.
5. Fault بین Event/Head/Outbox: Half-state ایجاد نشود.
6. UPDATE/DELETE/TRUNCATE توسط Runtime Role روی Committed Event: Denied.
7. Replay با Payload/Hash دستکاری‌شده: Reject.
8. Duplicate event_id: Reject.
9. Mutation حذف Hash Verification: Test باید Fail شود.
10. Mutation حذف Idempotency Collision: Test باید Fail شود.
11. Mason برای Objective/Hard Constraint/Authority/Identity/Spine: Reject.
12. Mason برای Promotion: Reject.
13. Promotion بدون Evaluation Receipt قابل انتساب: Reject.
14. Promotion روی Stale Revision/Head: Reject.
15. Evaluator Receipt با Principal/Build ناقص یا mismatch: Gate را نبندد.
16. Effect بدون Committed Obligation: Reject.
17. Provider Timeout مبهم: Reconciliation، نه Blind Retry.
18. Clean-host Restore: Verify Chain/Revision و یک Fresh Governed Write.
19. Provider Handoff: همان World/Entity/Role/Task ID حفظ شود.
20. Telemetry Outage: Coverage degraded و Gap جعلی ساخته نشود.

# پیوست D - حداقل ساختار Repository

```text
/contracts/
  OBJECTIVE_CONTRACT.schema.json
  PHENOTYPE_REVISION.schema.json
  CANONICAL_EVENT.schema.json
  ROLE_BINDING.schema.json
  GAP_SIGNAL.schema.json
  EVALUATION_RECEIPT.schema.json
  OUTBOX_OBLIGATION.schema.json
  EFFECT_RECEIPT.schema.json
/governance/
  DB_ROLE_MATRIX.yaml
  FORBIDDEN_TRANSITIONS.yaml
  PROMOTION_POLICY.yaml
  PROOF_REGISTRY.json
/runtime/
  sequencer/
  replay/
  task_bus/
  brain_gateway/
  context_compiler/
  effect_executor/
/observation/
  telemetry_schema/
  aggregators/
  detectors/
/development/
  mason/
/evidence/
  unit/
  integration/
  mutation/
  restore/
  provider_handoff/
  effects/
/releases/
  manifest.json
  SHA256SUMS
```

# پیوست E - Procedure بازسازی برای دو سال بعد

Maintainer آینده نباید کار را با باز کردن Workflow قدیمی یا انتخاب جدیدترین Model شروع کند. ابتدا Architecture Version از Release Manifest مشخص می‌شود. بعد Schema، DB Role Matrix، Current Canonical Head، Active Objective Contract، Active Phenotype Revision، Proof Registry و آخرین Restore Receipt بررسی می‌شوند. Replay Verification، CAS/Idempotency/Fencing Test، Mason Negative Test، Evaluator Attribution، Provider Handoff و Effect Reconciliation دوباره Verify می‌شوند. فقط بعد از هماهنگ شدن این Foundationها Development جدید شروع می‌شود.

# پیوست F - وضعیت Vocabulary باقی‌مانده از World 7

واژه‌های Genome، Phenotype، Development، Genesis، Evolution، Sleep، Repair و Non-extinction از History پروژه حذف نمی‌شوند. در Z0-A فقط معنای Operational که به Contract صریح نگاشت شود نگه داشته می‌شود. Phenotype یعنی Runtime Revision نسخه‌دار. Repair یعنی Governed Revision یا Recovery Transition. Sleep/Wake Operationهای Lifecycle هستند. Genome/Evolution تا زمانی که Population، Heritable Variation، External Fitness، Selection و Evidence تجربی مستقل وجود نداشته باشد Exploratory است. هیچ ادعای Biological Life وجود ندارد.

# پیوست G - متن کامل Baseline فارسی استخراج‌شده از PDF نهایی

این Block بدون خلاصه‌سازی برای آرشیو نگه داشته شده است. ممکن است Artifactهای Layout ناشی از PDF extraction داخل متن باقی مانده باشد، ولی هدف این است که متن Baseline کوتاه نهایی گم نشود.

```text
‫‪WORLD 8 / Z0-A‬‬



          ‫معماری نهایی ‪ - World 8‬خط مبنای ‪Z0-A‬‬
                  ‫ٔ‬
     ‫توسعه پیشنهاد‪-‬محور‬                                                          ‫ٔ‬
                        ‫سامانه عملیاتی پایدار‪ ،‬مستقل از ارائهدهنده‪ ،‬با مشاهد ٔه مستقل و‬


                                                 ‫وضعیت‪FINAL DESIGN BASELINE / NOT PRODUCTION :‬‬
                                                                                         ‫تاریخ تثبیت‪2026-08-24 :‬‬
               ‫دامنه‪ :‬معماری هنجاری ‪Z0-A‬؛ پیادهسازی‪ ،‬آزمون و ارتقای شواهد در رجیستری جداگانه دنبال میشود‪.‬‬



                                   ‫ٔ‬
   ‫تاریخچه پذیرفتهشده خارج از آنها میماند‪.‬‬ ‫مغز و رابط قابل تعویضاند؛ هویت‪ ،‬وضعیت کاننیکال‪ ،‬اختیار‪ ،‬هدف و‬   ‫اصل مرکزی‬

 ‫پنج ‪ Plane‬ثابت‪/Canonical Spine، Operational، Observation، Development/Mason، Evidence :‬‬                      ‫ٔ‬
                                                                                                              ‫هندسه‬
                                                                                         ‫‪.Governance‬‬           ‫نهایی‬

‫فقط ‪Proposal‬؛ بدون حق تغییر مستقیم ‪Objective، Hard Constraints، Authority، Identity، Canonical‬‬                   ‫مرز‬
                                                                                    ‫‪ Spine‬یا ‪.Promote‬‬        ‫‪Mason‬‬

   ‫این سند «نهایی شدن طراحی ‪ »Z0-A‬را ثبت میکند‪ ،‬نه آمادگی ‪ ،Production‬خودمختاری کامل یا تکامل خودکار‪.‬‬        ‫مرز ادعا‬
                                                                                         ‫‪ .1‬حکم نهایی معماری‬
‫‪ World 8‬در ‪ Z0-A‬یک ‪ Runtime‬پایدار و قابل ممیزی برای موجودات‪/‬سازمانهای دیجیتال است که شناخت‪ ،‬کانال و مدل‬
               ‫ٔ‬
  ‫سامانه توسعهگر‪ ،‬مدل‬ ‫را از مالکیت هویت و حقیقت جدا میکند‪ .‬تصمیم نهایی پس از بازبینی متقاطع این است که هیچ‬
                          ‫زبانی‪ ،‬داشبورد‪ ،‬سیستم تلهمتری یا مخزن کد نباید بتواند خود را منبع حقیقت ‪ Runtime‬جا بزند‪.‬‬


      ‫قاعد ٔه پایه‪ :‬هر تغییر معتبر باید از یک وضعیت کاننیکال معلوم به یک وضعیت کاننیکال جدید برسد‪ ،‬با ‪Proposal‬‬
                                                 ‫ٔ‬
     ‫تاریخچه ‪ ،append-only‬و ‪ Evidence‬متصل به همان ‪.Claim‬‬ ‫مشخص‪ ،‬اختیار معتبر‪ CAS ،‬در زمان ‪،Commit‬‬


                                                                               ‫‪ .2‬پنج ‪ Plane‬ثابت ‪Z0-A‬‬

                             ‫ممنوعیت اصلی‬                                    ‫مالک چه چیزی است؟‬                   ‫‪Plane‬‬

  ‫مدل‪ UI، Observation ،‬یا ‪ Mason‬حق نوشتن‬          ‫‪/World/Entity identity، event history، head‬‬       ‫‪Canonical Spine .1‬‬
              ‫مستقیم در حقیقت کاننیکال ندارند‪.‬‬         ‫‪،version، checkpoints، authorizations‬‬
                                                                             ‫‪canonical revisions‬‬

   ‫‪ Provider/Session/Channel‬نباید به هویت‬             ‫‪،Entity/Role/RoleBinding، Task، ingress‬‬           ‫‪Operational .2‬‬
                           ‫کاننیکال تبدیل شود‪.‬‬     ‫‪/Brain Gateway، context loading، outbox‬‬
                                                                             ‫‪effects، connectors‬‬

  ‫‪ Observation‬منبع ‪ Truth‬نیست و نباید توسط‬        ‫‪ Telemetry‬خام‪،normalization، aggregation ،‬‬           ‫‪Observation .3‬‬
                 ‫‪ Mason‬انتخاب‪/‬دستکاری شود‪.‬‬                      ‫‪SLO evaluation، gap signals‬‬

       ‫خود‪-‬تغییری‪ ،self-approval ،‬تغییر ‪Hard‬‬       ‫ساخت ‪ Proposal‬برای ‪ Phenotype Revision‬بر‬          ‫‪/ Development .4‬‬
   ‫‪ Constraints/Authority/Identity/Spine‬و‬                                         ‫اساس ‪ gap‬معتبر‬                ‫‪Mason‬‬
                     ‫‪ Promote‬مستقیم ممنوع‪.‬‬

     ‫‪ PASS‬همسایه‪ Claim ،‬دیگر را ارتقا نمیدهد؛‬             ‫‪،Proof Registry، evaluator receipts‬‬            ‫‪/ Evidence .5‬‬
    ‫‪ evaluator‬باید مستقل و قابل انتساب باشد‪.‬‬      ‫‪approvals، promotion gates، audits، policy‬‬              ‫‪Governance‬‬


                                                                                               ‫ٔ‬
      ‫نسخه قبلی‪ Cognition ،‬و ‪ Ingress‬ممکن بود بهصورت ‪Plane‬های جدا دیده شوند‪ .‬در ‪ Z0-A‬آنها سرویسها و‬ ‫در‬
           ‫مرزهای درون ‪ Operational‬هستند تا توپولوژی هنجاری به پنج ‪ Plane‬کاهش یابد و مسئولیتها شفافتر شود‪.‬‬

                                                 ‫‪ .3‬مدل هویت‪ Entity :‬با ‪ Role‬یکی نیست‬
  ‫‪ Entity‬یک موجود‪/‬سازمان با هویت پایدار‪ lifecycle ،‬و ‪ state head‬مستقل است‪ Role .‬یک جایگاه مسئولیت است‪.‬‬
      ‫یک‬    ‫‪company-001‬‬     ‫‪ RoleBinding‬اتصال ‪ governed‬میان ‪ Role‬و ‪ Entity/Society/Executor‬است‪ .‬بنابراین‬
         ‫فعال میشود‪.‬‬      ‫‪role_binding‬‬   ‫یک ‪ Role‬است و از طریق‬          ‫‪secretary-role‬‬   ‫‪ Entity/Society‬عملیاتی است‪ ،‬اما‬

                          ‫نمونه‬                     ‫وضعیت مستقل؟‬                  ‫هویت مستقل؟‬                      ‫شیء‬

                ‫‪company-001‬‬                                       ‫بله‬                         ‫بله‬       ‫‪Entity / Society‬‬

                ‫‪secretary-role‬‬        ‫تعریف‪/‬نسخه دارد اما ‪ Entity‬نیست‬         ‫خیر‪ ،‬جایگاه مسئولیت‬                  ‫‪Role‬‬
                                                                                            ‫است‬
    -company-001 ↔ secretary              ‫ دارد‬binding state ،‫بله‬               ‫خیر‬            RoleBinding
                          role

ChatGPT، Grok، API session            provenance/runtime ‫فقط‬                    ‫خیر‬        /Provider/Model
                                                     metadata                                      Session



                                                                    ٔ
                                                             ‫نسخه فنوتیپ‬ ‫ قرارداد هدف و‬.4
                                                  ‫ نسخهدار و کاننیکال‬- Objective Contract 4.1
                                                                         ٔ
    ‫ یک شیء نسخهدار است و حداقل شامل‬Objective Contract ‫ هر‬.‫حافظه موقتی دفن شود‬ ‫ یا‬Prompt ‫هدف نباید در‬
       scope، objective، success metrics/SLO، hard constraints، authority ceiling، risk ،‫ نسخه‬،‫شناسه‬
                           .‫ میشود‬promotion policy ‫ و‬class، observation schema، adaptation surface

objective_contract = {
     objective_contract_id,
     version,
     scope,
     objective,
     success_metrics_and_slos,
     hard_constraints,
     authority_ceiling,
     risk_class,
     observation_contract,
     allowed_adaptation_surface,
     promotion_policy
}


        /governance ‫» نیست؛ نیازمند مسیر‬Mason ‫ محدودیت سخت یا سقف اختیار یک «ویرایش عادی‬،‫تغییر هدف‬
                                                            .‫ جداگانه و مجوز صریح است‬constitutional change

                                            ‫ تغییر اجرایی نسخهدار‬- Phenotype Revision 4.2
،parent revision، diff :‫ نسخهدار ثبت میشود‬Phenotype Revision ‫ به شکل یک‬Runtime ‫هر تغییر در نحو ٔه عمل‬
                ٔ
    ‫نسخه قبلی پاک یا‬ .status ‫ و‬risk، evidence refs، proposer ،‫ معیار پذیرش‬،‫ پیشبینی اثر‬،migration/rollback
                                                                                           .‫بازنویسی نمیشود‬

phenotype_revision = {
     revision_id, parent_revision_id,
     objective_contract_version,
     change_set,
     migration_plan, rollback_plan,
     target_metrics, risk_class,
     evidence_refs,
     proposed_by, evaluated_by,
     status
}



                                       Mason ‫ قبل از‬- ‫ مستقل‬Observation .5
                                                                           ٔ
                                    :‫ جریان هنجاری‬.‫سامانه توسعهگر وجود داشته باشد‬ ‫ باید قبل از هر‬Observation
 raw telemetry
   -> normalization
   -> aggregation/windowing
   -> SLO / invariant evaluation
   -> gap_signal
   -> Evidence/Governance registry
   -> Mason may consume the signal


     ‫ حق ندارد خودش ورودیها را گزینشی‬Mason .‫ و داد ٔه مشاهدهشده مشتق شود‬Objective Contract ‫ باید از‬Gap
     ‫ میتوان از منطق‬gap ‫ برای تشخیص‬.‫ را بازتعریف کند یا «مشکل» را صرفا ً برای توجیه تغییر بسازد‬SLO ،‫انتخاب کند‬
،Mason ‫ نیز باید خارج از‬classifier ‫ اما آن‬،‫ مستقل مجاز است‬classifier ‫ استفاده کرد؛ در صورت نیاز‬deterministic
                                                                         .‫ قابل آزمون و قابل تعویض باشد‬،‫نسخهدار‬

                                                                            ‫فیلدهای حداقلی‬               ‫خروجی‬
                                                                                                 Observation

      ،gap_id، objective_contract_version، metric/invariant، window، expected، observed             gap_signal
                                      severity، provenance، detector_version، created_at

   /SLO، threshold، sampled values، aggregation method، breach duration، confidence ‫نام‬            SLO breach
                                                                              quality flags

                      scope، signal type، state، evidence pointers، non-canonical marker          health signal



                                                    ‫ توسعهگر با دست بسته‬- Mason .6
  ‫ معتبر میتواند‬gap ‫ محدود است که فقط پس از دریافت‬proposer ‫ یک‬.‫ «عامل خودتکاملی» نیست‬Z0-A ‫ در‬Mason
                                                                                   .‫ بسازد‬Candidate Revision

                                                             .‫• میتواند یک تغییر کوچک و قابل بازگشت پیشنهاد دهد‬
                                                      .‫ را مرجع کند‬Objective Contract version ‫ و‬gap_id ‫• باید‬
                            .‫ ارائه کند‬test plan ‫ و‬change-set، migration، rollback، expected impact ‫• باید‬
             .‫ را تغییر دهد‬Canonical Spine ‫ یا‬Objective، Hard Constraints، Authority، Identity ‫• نمیتواند‬
                                                                        ٔ
                         .‫ کند‬Promote ‫ را‬Candidate ‫نتیجه ارزیابی را بنویسد یا‬ ،‫ خودش باشد‬evaluator ‫• نمیتواند‬
                                  .‫ مصنوعی بسازد‬Gap ‫ را بهدلخواه انتخاب کند تا‬Observation data set ‫• نمیتواند‬


             ;Mason may propose; Observation may measure; Evaluator may judge :‫اصل کنترل‬
                        .‫ هیچ نقش واحدی نباید هر چهار کار را انجام دهد‬.Promotion authority may promote


                                                ‫ مستقل و هویت ارزیاب‬Evaluator .7
     /‫ اما بهتنهایی ثابت نمیکند چه فرد‬،»‫ای اجاز ٔه نوشتن دارد‬DB role ‫ پایگاه داده میتواند محدود کند «چه‬Constraint
                                                                                                  ٔ
‫ باید هویت عملیاتی ارزیاب را به نتیجه‬Evaluation Receipt ‫ هر‬Z0-A ‫ در‬.‫نسخه کدی ارزیابی را انجام داده است‬/‫سرویس‬
                                                                                                       .‫ کند‬bind

                                                            ‫هدف‬                                            ‫فیلد‬
                            ‫انسان ارزیاب‬/‫ سرویس‬authenticated ‫هویت‬                          evaluator_principal_id

  ‫ ذخیره نمیشود‬receipt ‫ داخل‬secret ‫؛‬credential reference ‫مرز اختیار و‬              evaluator_role / credential_ref

                                                            ٔ
                          evaluator code/model/profile ‫نسخه دقیق‬                          evaluator_build_digest

                                            ‫اتصال نتیجه به ورودی دقیق‬   candidate_revision_id + objective_version

                                           drift ‫قابلیت تکرار و تشخیص‬             test_suite_digest / environment

                                                    ‫خروجی قابل ممیزی‬             result + metrics + evidence refs

                           ‫تقویت انتساب؛ جایگزین کنترل دسترسی نیست‬          attestation/signature where available


   ‫ این‬.‫ جداگانه دارد‬capability ‫ نیز‬Promotion .‫ جدا داشته باشند‬DB role ‫ و‬credential ‫ باید‬Mason ‫ و‬Evaluator
  ‫ اعمال و آزمون‬PostgreSQL ROLE/GRANT/REVOKE ‫ باید هم در سطح مدل داده و هم با‬Separation of Duties
                                                                                                              .‫شود‬

                                  ‫ نهایی‬commit ‫ قرارداد‬- Canonical Spine .8
   fencing ‫ یا‬CAS، event sourcing، outbox ‫های شناختهشده استفاده میکند و ادعای اختراع‬primitive ‫ از‬Spine
                                                           .‫ قابل ممیزی است‬continuity ‫ هدف آن ایجاد یک مرز‬.‫ندارد‬

                                                                                  Commit-time CAS 8.1
            ‫ در‬pre-read ‫ چک‬.‫» بررسی شود‬commit ‫ را تغییر میدهد و در «زمان‬head ‫ باید در همان تراکنشی که‬CAS
                         .‫ شود‬fail-closed ‫ جدید باید‬write ‫ برای‬stale expected head .‫ کافی نیست‬application

                                                         collision handling ‫ با‬Idempotency 8.2
reuse ‫ را برگرداند؛‬prior result ‫ میتواند‬semantics ‫ با همان‬retry .‫ میشود‬intent« bind« ‫ به‬Idempotency key
                             .‫ کند‬silently overwrite ‫ متفاوت خطاست و نباید‬event type/payload ‫ با‬key ‫همان‬

                                                                 Atomic append/head/outbox 8.3
  create ‫ و‬append event، advance head، update projections ،‫برای عملیاتی که اثر خارجی برنامهریزی میکند‬
                                                    .‫ اتمیک انجام شوند‬transaction ‫ باید در یک‬outbox obligation

                                              Transactional Outbox + Effect Receipts 8.4
 ‫ میشوند و‬audit ‫ها‬attempt .‫ مستقل داشته باشد‬obligation ‫ باید‬side effect ‫ یا هر‬CRM ‫ ثبت‬،‫ پیام‬،‫ارسال ایمیل‬
 -effectively ‫ فقط‬World 8 .‫ میشود‬settle ‫ در صورت وجود‬provider-side effect id ‫ و‬receipt ‫موفقیت نهایی با‬
     .‫ ممنوع است‬universal exactly-once ‫ مشخص هدف میگیرد؛‬key/connector/receipt ‫ را در محدود ٔه‬once

                                                                    Sequencer lease + fencing 8.5
‫ قدیمی‬token ‫ نباید با‬expired ‫ جابهجا یا‬sequencer .‫ الزم است‬fencing token ‫ با‬active sequencer lease ‫یک‬
                                                               .‫ قدیمی هنوز زنده باشد‬process ‫ حتی اگر‬،‫ کند‬commit

                                                                                 DB ‫ در‬Append-only 8.6
 UPDATE/DELETE/TRUNCATE ‫ باید‬DB ‫ غیرقابلویرایش باشند؛‬convention ‫ نباید فقط با‬committed ‫رویدادهای‬
                           .‫ رویداد جدید است‬،‫ اصالح گذشته‬.‫ کنترل کند‬role/trigger/privilege ‫ را با‬Runtime ‫مسیر‬
                                           Checkpoint, replay, clean-host restore 8.7
      .‫ کند‬verify ‫ها را‬hash ‫ و‬version sequence، duplicate IDs ،‫ زنجیره‬materialization ‫ باید قبل از‬Replay
     artifacts ‫ معتبر فقط وقتی است که یک محیط پاک از‬Restore .‫ میشود‬head/version bind ‫ به‬Checkpoint
                         .‫ تازه قبول کند‬lease ‫ جدید را با‬write governed ‫ و سپس یک‬verify ،‫ بازسازی‬durable

                     Context ‫ و‬Provider-independent identity .9
        World/Entity/Role/Task .‫ هستند‬provenance ‫ فقط‬channel ‫ و‬Provider، model، session، thread
 Context .‫ را حفظ کند‬Task state ‫ و‬canonical IDs ‫ باید همان‬Provider ‫ تعویض‬.‫ از آنها مشتق نمیشود‬identity
                                                                 :‫ انجام میشود‬scoped ‫ نیز بهصورت‬loading

                                                                                           ‫محتوا‬          ‫الیه‬

                                                                ‫های الزم‬invariant ‫ و‬World kernel          K0

                                                  shared constraints ‫ و‬Entity/Society objective           K1

                                                   Role contract، permissions، output contract            K2

                                                           state، artifacts، approvals ،‫ جاری‬Task         K3

                                                    provenance ‫ مرتبط با‬evidence/memory ‫حداقل‬             K4



                                                  ‫ و توسعه‬Runtime ‫ جریان کامل‬.10

 External input
   -> Operational ingress/auth/route
   -> scoped context + replaceable cognition
   -> proposal/result
   -> policy/authority evaluation
   -> Canonical Spine commit (CAS + lease + idempotency)
   -> task/state projection + optional outbox
   -> effect attempt -> receipt
   -> Observation telemetry
   -> aggregation / SLO evaluation
   -> gap_signal
   -> Mason proposal (optional)
   -> independent evaluation
   -> Governance promotion decision
   -> canonical Phenotype Revision activation



                                                     Evidence / Governance .11
    ‫ مستقل داشته‬evidence references ‫ و‬predicate، falsifier، required evidence، status ‫ باید‬Claim ‫هر‬
‫ سطح پایینتر نمیتواند‬Evidence .‫ یعنی شاهد الزم وجود ندارد‬OPEN .‫ جای کیفیت شواهد را نمیگیرد‬،‫ تعداد تست‬.‫باشد‬
                                                                          .‫ادعای سطح باالتر را خودکار ارتقا دهد‬

                                                                                         Z0-A ‫معنی‬      ‫سطح‬
                                                                               ‫ایده بدون اجرای شاهد‬/‫تعریف‬         E0

                                                             ‫ مشخص و قابل ابطال‬schema/privilege/‫قرارداد‬           E1

                                                            mutation-sensitive ‫ و‬local/disposable ‫اجرای‬           E2

                                                             ‫ واقعی‬integration ‫ یا‬persistent target ‫اجرای‬         E3

                    production-like: restore/security/load/chaos/independent credentials/runbooks                 E4

                                        ‫ از پیش تعیینشده‬failure envelope ‫ و‬SLO ‫ با‬longitudinal operation          E5



                                               Separation of Duties ‫ امنیت و‬.12

                            ‫نمیتواند‬                                      ‫میتواند‬               Capability/Role

         ٔ
‫همه کنترلهای‬ ‫؛ جایگزین‬rewrite history        policy ‫ یا‬approve/revoke promotion         Human Root / Promotion
                           ‫امنیتی شود‬                                      ‫حساس‬                             Authority

  bypass revocation ‫؛‬self-approve              commit under lease/fencing/CAS                          Sequencer

     identity ‫ یا تغییر‬mint authority                 request effect ‫ و‬Task work           Operational Executor

      define ‫ یا‬canonical mutation            /produce signed ‫ و‬read telemetry                              Observer
                           objective                           attributed signals

 hard ‫ تغییر‬،promote، self-evaluate                propose phenotype changes                                  Mason
                        constraints

promote ‫ یا‬candidate ‫ همان‬propose                            evaluate candidate                         Evaluator
                                  ‫آن‬

      create its own authorization         settle authorized outbox obligations                   Effect Executor



                                                    Rollback ‫ و‬Promotion ‫ قواعد‬.13
                                                                       .‫ ثبت شود‬Observation ‫ معتبر توسط‬Gap .1
                                                                   .‫ بسازد‬Candidate Revision ‫ یا انسان‬Mason .2
                                              .‫ مشخص ارزیابی شود‬shadow/replay/test profile ‫ در‬Candidate .3
                                             .‫ ثبت شود‬evidence ‫ و‬build digest ،‫ با هویت‬Evaluator Receipt .4
                          .‫ دستنخوردهاند‬authority ‫ و‬hard constraints ‫ بررسی کند‬Policy/Promotion gate .5
                                                                             .‫ تصمیم بدهد‬Promotion Authority .6
                     .‫ شود‬commit ‫ کاننیکال‬CAS ‫ و‬expected current revision/head ‫ با‬revision ‫ فعالسازی‬.7
                .‫ انجام شود‬known-good/‫ قبلی‬revision ‫ جدید به‬event ‫ با‬breach، rollback ‫ یا‬regression ‫ در‬.8

                                                            ‫ و خطوط قرمز‬Non-claims .14
                                              .‫ یا شخصیت حقوقی ندارد‬AGI ،‫ حیات زیستی‬،‫• این معماری ادعای آگاهی‬
                                                                   .‫ «خودتکاملی» اثباتشده نیست‬Z0-A ‫ در‬Mason •
                                                  .‫ نیست‬superuser ‫ در برابر‬secure storage ‫ برابر‬Hash chain •
                                                    .‫ را اثبات نمیکنند‬evaluator ‫ بهتنهایی هویت‬DB constraints •
                                                  .‫ کافی نیست‬security boundary ‫ بهتنهایی‬Human approval •
                                                      .‫ ادعا نمیشود‬External effect universal exactly-once •
        /credential separation، persistent restore، security/load ‫ تا بستهشدن‬Production readiness •
                                                                                   .‫ است‬OPEN ‫ها‬SLO ‫ و‬chaos

                                                                           Z0-A ‫ معیار خروج از‬.15

                                                                 PASS ‫معیار‬                               Gate

     .bypass test fail-closed ‫ مرزبندی شده؛‬schema/API/DB roles ‫ در‬Plane ‫پنج‬              Z0A-G1 Plane isolation

canonical identity ‫ در‬provider field ‫؛‬RoleBinding portable ‫ جدا؛‬Role ‫ و‬Entity        Z0A-G2 Identity/Role split
                                                                   .‫الزم نیست‬

    CAS ‫ با‬Phenotype Revision immutable/versioned ‫ و‬Objective Contract              Z0A-G3 Objective/Revision
                                                                 .promotion                          versioning

             .‫ کامل‬provenance ‫؛‬Mason ‫ مستقل از‬raw→aggregate→SLO→gap                        Z0A-G4 Observation
                                                                                                 independence

‫ را عوض‬Objective/Authority/Identity/Spine ‫ نمیتواند‬Mason ‫تست منفی ثابت کند‬         Z0A-G5 Mason confinement
                                                              .‫ کند‬Promote ‫یا‬

   ‫ از‬evaluator credential ‫ شده و‬principal/build/input/output bind ‫ به‬receipt        Z0A-G6 Evaluator identity
                                                              .‫ جداست‬Mason

   stale/fencing/collision ‫؛‬CAS/idempotency/append/head/outbox atomic                  Z0A-G7 Spine atomicity
                                                                 .tests PASS

   clean-host restore + fresh post-restore governed write + new fencing                       Z0A-G8 Recovery
                                                                .token PASS

  fail-closed ‫ و‬authorized outbox→attempt→receipt، duplicate-effect test                         Z0A-G9 Effects
                                                                 .ambiguity



                                               World 8 v0.1.1 ‫ وضعیت نسبت به‬.16
   ‫ و زنجیر ٔه‬Task Bus ،‫ نقشها‬،world-001، company-001 ‫ همچنان شاهد عملیاتی مهمی برای‬v0.1/v0.1.1 ‫نامزد‬
          ‫ استقالل‬،Plane ‫ تثبیت پنج‬:‫ را با چهار اصالح معماری اصلی میبندد‬lineage ‫ این‬Z0-A .‫ است‬persistent
evaluator ‫ و اثباتپذیر کردن هویت‬،Objective/Phenotype Revision ‫ نسخهدار شدن‬،Mason ‫ از‬Observation
Z0-A ‫های‬Gate ‫ نمیکند؛ آنها‬PASS ‫ هیچ شاهد قدیمی بهصورت خودکار این الزامات جدید را‬.DB constraint ‫فراتر از‬
                                                                                                          .‫هستند‬


                                              World 8 / Z0-A - Final Design Baseline - 2026-08-24 - NOT PRODUCTION

```

# پیوست H - متن کامل Execution Roadmap استخراج‌شده

```text
‫‪WORLD 8 / Z0-A‬‬


                                        ‫ٔ‬
            ‫نقشه اجرایی و ‪Gate‬های پذیرش ‪Z0-A‬‬
 ‫از تثبیت قراردادها تا ‪ Observation‬مستقل‪ Mason ،‬محدود‪ ،‬ارزیابی مستقل و ‪Restore‬‬


                                ‫وضعیت‪EXECUTION ROADMAP / FINAL DESIGN BASELINE :‬‬
                 ‫اصل‪ :‬هیچ مرحله با گذشت زمان ‪ PASS‬نمیشود؛ فقط ‪ Evidence‬میتواند ‪ Gate‬را ببندد‪.‬‬
                                                                                           ‫ ترتیب اجرا‬.1

                 ‫ اصلی‬Gate                                                       ‫خروجی‬                  ‫مرحله‬

     Contract lint + schema            Plane boundaries، schemas، Objective/Revision            Z0A-0 Freeze
validation + change-control                                       contracts، role model             contracts
                      freeze

  race/adversarial/mutation     /commit-time CAS، intent idempotency، atomic append              Z0A-1 Spine
                        gate                               head/outbox، lease/fencing              hardening

wrong-role/provider-capture     portable binding ‫ و‬Entity, Role, RoleBinding tables/APIs    Z0A-2 Entity/Role
              negative tests                                                                      separation

        immutability + CAS         Phenotype Revision ‫ و‬versioned Objective Contract        & Z0A-3 Objective
       promotion + rollback                                                                          Revision

      provenance، detector                raw telemetry→aggregate→SLO→gap_signal           Z0A-4 Observation
    version، Mason isolation

 forbidden-change negative                          ‫ معتبر‬gap ‫ فقط از‬Candidate Revision         Z0A-5 Mason
                       suite                                                                        proposer

SoD + identity binding tests       /evaluation receipts + separate evaluator principal     Z0A-6 Independent
                                                                                  build            evaluation

   ;self-approval impossible             promotion gate + canonical activation event        /Z0A-7 Promotion
      stale revision rejected                                                                        rollback

  + fresh post-restore write                      checkpoint/replay/clean-host restore        Z0A-8 Recovery
         new fencing token

  E3/E4 claim-specific gates              provider handoff + real effect receipt + SLO      Z0A-9 Operational
                                                                            monitoring                  proof



                                                   ‫ قراردادهای پایه‬Z0A-0 - Freeze .2
                                                                          .object ‫ هر‬owner ‫ و‬Plane ‫• ثبت پنج‬
    .Objective Contract، Phenotype Revision، gap_signal، Evaluation Receipt ‫های‬schema ‫• تعریف‬
                                                                                 .forbidden transitions ‫• ثبت‬
                       ،DB roles: runtime_sequencer، observer، mason_proposer، evaluator ‫• تعریف‬
                                                                  .effect_executor، promotion_authority
                                                   .threat assumptions ‫ ماتریس و‬GRANT/REVOKE ‫• تعریف‬

                                                                                Z0A-1 - Spine .3
                                                                                .‫ نهایی‬transaction ‫ داخل‬CAS •
                                               .idempotency key + semantic hash collision rejection •
                                                                  .atomic event/head/projection/outbox •
                                                                        .lease expiry/rotation + fencing •
                                                                               .append-only at DB level •
                                                .checkpoint verification and replay-integrity checks •

                                                                                      ‫آزمونهای اجباری‬

                                           Expected                                                    Test

                    stale reject ‫؛ دومی‬commit ‫فقط اولی‬                     ‫ یکسان‬expected_head ‫ با‬writer ‫دو‬

                       deduplicate/replay prior result                          intent ‫ و همان‬key ‫ همان‬retry

           partial write ‫؛ هیچ‬IDEMPOTENCY_COLLISION                              ‫ متفاوت‬payload ‫ با‬key ‫همان‬

                                                reject                                 stale fencing token

                                        all-or-nothing               event commit + outbox fault injection

                                 runtime role denied                    UPDATE/DELETE committed_events



                                                Z0A-2 - Entity/Role/Binding .4
‫ جایگاه‬accountant-role ‫ و‬secretary-role، sales-role .‫ باقی میماند‬Entity/Society ‫ به عنوان‬company-001
                                                  .‫ میمانند‬executor/provider-neutral ‫ها‬Binding .‫هستند‬

                                                                       .‫ نمیکند‬Role name authority mint •
                                 .‫ مجاز تطبیق داده میشود‬scope ‫ فعال و‬RoleBinding ‫ با‬Task assignment •
                                                         .‫ را تغییر نمیدهد‬canonical ID ‫ هیچ‬Provider switch •

                                               Z0A-3 - Objective / Revision .5
                                                            .Objective Contract immutable per version •
                                                 .rollback-ready ‫ و‬Phenotype Revision parent-linked •
                                               .‫ را لمس میکند‬allowed_adaptation_surface ‫ فقط‬Mason •
                                      .‫ هستند‬Mason ‫ خارج از مسیر‬authority ceiling ‫ و‬hard constraints •

                                                                 Z0A-4 - Observation .6
                                                                   .‫ را مختل کند‬replay ‫ نباید‬Telemetry loss •
                                                    .‫ ثبت شود‬detector version ‫ و‬Aggregation window •
                                          .‫ داشته باشد‬objective version ‫ و‬provenance ‫ باید‬gap_signal •
                                          .‫ باشد‬code path ‫ و‬Mason credential ‫ مستقل از‬Gap detector •

                                                Evaluator ‫ و‬Z0A-5/6 - Mason .7

                                    Evaluator                   Mason                                ‫موضوع‬
                  ‫ را بررسی کند‬gap ‫میتواند صحت مرجع‬               ‫مصرف میکند‬                                   Gap

                                           ‫ارزیابی میکند‬                ‫میسازد‬                           Candidate

                           ‫ کند تغییر نکردهاند‬verify ‫باید‬         ‫حق تغییر ندارد‬       Objective/Hard Constraints

                                                    ‫ندارد‬                  ‫ندارد‬                         Promotion

         identity/build digest ‫ با‬evaluation receipt          proposal receipt                             Receipt



                                                                            Z0A-7 - Promotion .8
‫ باید‬activation .‫ را فعال کند‬Candidate ‫ میتواند‬policy gate ‫ معتبر و‬receipt ‫ تنها بعد از‬Promotion Authority
   .‫ جدید است‬canonical event ‫ یک‬rollback ‫ هر‬.‫ داشته باشد‬current phenotype revision/head ‫ روی‬CAS

                                                                                   Z0A-8 - Restore .9
                                                                               .Export durable recovery bundle .1
                                                   .Start clean environment with different system identity .2
                                                                                          .Restore schema/data .3
                                                            .Verify chain/checkpoint/head/revision/objective .4
                                                                   .Recreate separated DB roles/credentials .5
                                                              .Acquire fresh lease with higher fencing token .6
                                                                            .Execute one fresh governed write .7
                                                            .Record restore receipt, RTO/RPO, operator steps .8

                                                 Z0A-9 - Operational evidence .10
                                             .ChatGPT→Grok handoff on same Task without identity fork •
                      .One real low-risk external effect with authorization/outbox/attempt/receipt •
                                                              .Observation detects a predefined SLO breach •
                                   .Mason proposes a reversible low-risk improvement from that gap •
             .Independent evaluator judges it; separate promotion decision activates or rejects •

                                                                                    Release rule .11

         A .Z0-A is complete only when architecture and executable boundary agree
  document claiming five planes while runtime still allows Mason to select its own telemetry
                                                       .or promote itself is a FAIL, regardless of test count



                                                                        World 8 / Z0-A Execution Roadmap - 2026-08-24

```

# پیوست I - متن کامل Cross-Review Closure استخراج‌شده

```text
‫‪WORLD 8 / Z0-A‬‬



              ‫ثبت نهایی تصمیمات ‪Cross-Review‬‬
                                                 ‫‪ Closure Record‬برای معماری شاخهای ‪Z0-A‬‬


                                                  ‫وضعیت‪DESIGN DECISIONS CLOSED FOR Z0-A :‬‬
                                                ‫ٔ‬
  ‫کلمهبهکلمه داورها نیست‪ ،‬بلکه تصمیمات نهایی معماری را ثبت‬ ‫منبع‪ :‬جمعبندی بازبینی متقاطع؛ این سند نقلقول‬
                                                                                                ‫میکند‪.‬‬
                                                                           ‫ تصمیمات بستهشده‬.1

                                  ‫علت معماری‬                                      ‫تصمیم نهایی‬               ‫موضوع‬

‫ توسط‬Truth ‫ و جلوگیری از مالکیت‬ambiguity ‫کاهش‬                                   ‫ ثابت‬Plane ‫پنج‬          Plane ‫تعداد‬
                  interface/model/telemetry

 ‫ مستقل‬state/‫ هویت‬Entity ‫ مسئولیت است؛‬Role                                             ‫کامال ً جدا‬   Entity vs Role
                                          ‫دارد‬

            ‫ مستقل‬history ‫دارای هویت عملیاتی و‬                                 Entity/Society        company-001

    ‫ بدون تغییر‬holder/provider ‫قابل تعویض بودن‬                            role_binding ‫ با‬Role       secretary-role
                                Role identity

 Mason ‫ یا قابل دستکاری‬prompt-local ‫هدف نباید‬                     ‫ نسخهدار‬Objective Contract             Objective
                                          ‫باشد‬

            CAS promotion ‫ و‬rollback، audit                      ‫ نسخهدار‬Phenotype Revision               Runtime
                                                                                                          changes

 self-promotion ‫ و‬self-modification ‫جلوگیری از‬                                  Proposal-only               Mason

 self-defined ‫ و‬cherry-picking data ‫جلوگیری از‬                           Mason ‫مستقل و قبل از‬         Observation
                                        gaps

        fail-closed concurrency ‫ و‬continuity     commit-time CAS + idempotency collision                 Canonical
                                                                 atomic outbox + fencing +                   Spine

         ‫ بهتنهایی کافی نیست‬policy convention                                    DB-enforced          Append-only

   ‫ واقعی ناقص است‬recovery ‫پایداری هویت بدون‬     checkpoint/replay/clean-host + fresh write                Restore

   ‫ کافی‬app-level checks ‫ یا‬Human approval         DB roles/GRANT + credential separation                     SoD
                                        ‫نیستند‬

‫ نه‬،‫ را نشان میدهد‬capability ‫ فقط‬DB constraint     ‫ را‬principal/build/input/output ‫ باید‬receipt          Evaluator
                        evaluator ‫هویت واقعی‬                                          ‫ کند‬bind             identity



                                                                     Z0-A ‫ موارد ردشده برای‬.2
                                                       .‫ بسازد‬gap ‫ را انتخاب کند و‬telemetry ‫ که خودش‬Mason •
                                                    .‫ کند‬rewrite ‫ را‬Hard Constraints ‫ یا‬Objective ‫ که‬Mason •
                                                                 .Development Plane ‫ مستقیم از‬Promotion •
                                                      .‫ مستقل فقط چون اسم مسئولیت دارد‬Entity ‫ به عنوان‬Role •
                                                                   .‫ کافی‬secure storage ‫ به عنوان‬Hash chain •
                                             .‫ پرخطر‬effect ‫ برای‬security boundary ‫ به عنوان تنها‬Human click •
                                                            .»evaluator ‫ به عنوان «اثبات هویت‬DB constraint •
                                                                                      .Universal exactly-once •
                                             ‫• هرگونه ادعای ‪ autonomous evolution‬بدون ‪ evidence‬مستقل‪.‬‬

                                                                               ‫‪ .3‬مرز ‪Evidence‬‬
    ‫نامزد ‪ v0.1.1‬و شواهد ‪ E2/E3‬موجود‪ lineage ،‬عملیاتی ‪ World 8‬را نشان میدهند‪ .‬ولی هر ‪ Claim‬جدید ‪ Z0-A‬باید‬
            ‫‪ Gate‬خودش را پاس کند‪ .‬بهخصوص ‪ Observation independence، evaluator identity‬و ‪Mason‬‬
                                                                ‫‪ confinement‬نیازمند آزمونهای جدید هستند‪.‬‬

                                            ‫‪ .4‬اصل نهایی ‪Separation of Roles‬‬

 ‫‪Observation measures‬‬
 ‫‪Mason proposes‬‬
 ‫‪Evaluator judges‬‬
 ‫‪Promotion Authority promotes‬‬
 ‫‪Canonical Spine records‬‬


‫اگر یک ‪ actor‬بیش از یکی از این نقشها را برای همان ‪ change‬بدون کنترل مستقل انجام دهد‪ ،‬معماری ‪ Z0-A‬نقض شده‬
                                                                                                         ‫است‪.‬‬

                                                                                                 ‫‪ .5‬نتیجه‬
‫‪ Cross-review‬به یک معماری «کمتر شاعرانه‪ ،‬سختگیرتر و قابل ابطالتر» ختم شد‪ :‬توسعه همچنان ممکن است‪ ،‬اما خود‬
  ‫توسعهگر مالک هدف‪ ،‬داد ٔه قضاوت‪ ،‬ارزیابی و ارتقا نیست‪ .‬این تصمیم‪ Mason ،‬را از «عامل خودتکاملی» به یک مهندس‬
                                                       ‫پیشنهاددهنده در یک خط تولید ‪ governed‬تبدیل میکند‪.‬‬


                                                               ‫‪World 8 / Z0-A Cross-Review Closure - 2026-08-24‬‬

```
