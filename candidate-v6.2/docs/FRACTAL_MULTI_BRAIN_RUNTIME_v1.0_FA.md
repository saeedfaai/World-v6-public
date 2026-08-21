# World v6.2 RC2 — Fractal Multi-Brain Runtime

وضعیت: **Ratification Candidate / Non-Canonical / Not Deployed**  
Root Constitution: **v1.0 بدون تغییر**  
Evidence فعلی: **E2 محلی؛ نه Production**

## ۱. تصمیم نسخه

این تغییر `World v7` نیست. هویت World، تقدم Human Root، حقیقت Canonical، زنجیرهٔ
Policy/Approval/Event/Outbox، و قراردادهای مادر تغییر نکرده‌اند. این RC2 یک لایهٔ
اجرایی و قابل‌حذف روی v6.2 است که سه مفهوم را صریح می‌کند:

1. اجرای فرکتالی: سادگی در عمل، پیچیدگی در ظرفیت؛
2. Brain Farm: چند موتور قابل‌تعویض زیر کنترل Kernel مادر؛
3. تکامل موازی: مسیر سریع فعال + مسیر Shadow + ستون بقای کدنویسی‌شده.

اگر بعداً یکی از موارد زیر تغییر کند، مرز Major جدید بررسی می‌شود: مالکیت/اختیار
ریشه، معنای هویت، حقیقت Canonical، ترتیب Policy/Approval، یا معنای قراردادهای
FROZEN. RC2 هیچ‌کدام را تغییر نمی‌دهد.

## ۲. اصل مادر

> Model مغز موقت است؛ World Kernel مادر است.

ChatGPT، Gemini، Grok، مدل Local، کد deterministic یا Council می‌توانند پیشنهاد
بدهند، اما هیچ‌کدام هویت، حافظه، Policy، authority یا منبع حقیقت نیستند. تعویض
موتور فقط با همان `Execution Capsule` مجاز است: همان Entity، همان state refs، همان
hash ورودی، همان حداقل Resolution، همان Authority و همان budget.

## ۳. فرکتال بدون دام پیچیدگی

قرارداد واحد در هر مقیاس تکرار می‌شود:

`World → Entity → Mission → Skill → Workflow → Step → Tool → Field`

هر Node فقط این‌ها را می‌داند: purpose، قرارداد ورودی/خروجی، حداقل بردار اجرا،
handlerهای اصلی و fallback، فرزندان اختیاری و budget. Node در سطح درشت آغاز می‌شود
و فقط با یکی از triggerهای صریح باز می‌شود:

- دادهٔ ناکافی (`NEEDS_DETAIL`)،
- ریسک یا Policy بالاتر،
- ابهام حل‌نشده،
- شکست موتور اصلی،
- درخواست صریح Human Root.

هیچ Mega-Prompt یا Mega-Schema برای هر اجرا بار نمی‌شود. هر branch تنها projection
و skill موردنیاز خودش را می‌گیرد. عمق، تعداد تلاش، latency، cost و دور Council سقف
دارند. با تمام شدن سقف، نتیجه `DEFERRED` است، نه حدس.

## ۴. بردارهای مستقل

یک عدد واحد نمی‌تواند پیچیدگی World را بیان کند. محورها مستقل‌اند:

| محور | معنا | قاعده |
|---|---|---|
| `R` | Resolution داده در هر domain | R0 کابل مادر؛ R1+ فقط جزئیات افزوده؛ Truth هرگز downgrade نمی‌شود |
| `X0..X9` | ریزی اجرای Node | فقط با trigger و budget باز می‌شود |
| `B0..B4` | میزان واگذاری cognition | B0 کد؛ B1 یک Brain؛ B2 متخصص؛ B3 Council؛ B4 meta-orchestration؛ B5 مالکیت World ممنوع |
| `D0..D5` | عمق deliberation | از پاسخ سریع تا ارجاع Human Root؛ مستقل از مدل |
| `C0..C6` | بلوغ تبدیل رفتار به کد | Prompt → fixture → candidate → shadow → canary → approved primary → restore-proven spine |
| `A0..A5` | Authority | فقط Policy/Approval تعیین می‌کند؛ از confidence یا رأی استنتاج نمی‌شود |
| `E0..E5` | سطح evidence | ادعا باید دقیقاً به evidence موجود محدود شود |
| `M0..M9` | capability کلاس مدل | profile-specific؛ نام Provider جای capability نیست |

کاهش `B` یا تغییر Provider هرگز اجازهٔ کاهش حداقل `R/A/E` را نمی‌دهد. اگر کد
fallback فقط R0 می‌فهمد ولی کار R2 می‌خواهد، سیستم باید به Human Root ارجاع دهد.

## ۵. سه ستون اجرا

### Hot Path

ارزان‌ترین handler ایمن ابتدا اجرا می‌شود. کارهای ثابت با کد و Template؛ کارهای
زبانی/مبهم با Manual Brain یا مدل؛ کارهای حساس با Council. Cache فقط با کلید کامل
`pack_hash + node_hash + projection_hashes + state versions + vector + freshness`
مجاز است.

### Shadow Path

نسخهٔ نامزد همان ورودی را بدون effect می‌بیند. خروجی معنایی آن با مسیر فعال
مقایسه و append-only ثبت می‌شود. اختلاف برای آموزش، fixture و تولید کد نامزد مصرف
می‌شود؛ نتیجهٔ Shadow به کاربر یا Executor فرمان نمی‌دهد.

### Non-Extinction Spine

رفتارهای پرتکرار و تثبیت‌شده به کد deterministic تبدیل می‌شوند، ولی تنها پس از
تست، replay، Shadow و promotion مرحله‌ای. «کد وجود دارد» معادل بقا نیست؛ C6 فقط
بعد از artifact hash، backup قابل‌اعتماد و restore drill ثبت می‌شود.

## ۶. سطح بلوغ C

- `C0`: رفتار فقط در prompt/manual flow؛
- `C1`: ورودی/خروجی و trace به fixture نسخه‌دار تبدیل شده؛
- `C2`: کد نامزد و unit/conformance test وجود دارد؛
- `C3`: Shadow agreement و replay به آستانه رسیده؛
- `C4`: برای canary محدود و rollback‌پذیر واجد شرایط است؛
- `C5`: با approval صریح Human Root می‌تواند primary شود؛
- `C6`: علاوه بر approval، restore proof و بستهٔ بقای hash-bound دارد.

Promotion فقط یک پله است. invariant failure، effect attempt، replay mismatch،
evidence مخلوط از چند نسخه یا نبود approval، promotion را fail-closed می‌کند.
Self-mutation Production ممنوع است؛ خروجی مولد کد فقط candidate artifact/branch است.

## ۷. Portable Brain Pack

Brain Pack استاندارد منشی شامل این‌هاست:

- binding هویت و DNA overlay؛
- Prompt Contract ثابت؛
- Profileهای دقیق با `id + version + hash`؛
- خروجی `world-v6.secretary-decision.v1`؛
- Templateهای deterministic؛
- Provider Overlayهای بدون مالکیت و state؛
- fixtureهای هم‌ارزی بین مدل‌ها.

برای کارهای استاندارد، Provider فقط `intent`, `template_id`, `slots` و proposal را
انتخاب می‌کند؛ متن نهایی Runtime رندر می‌کند. بنابراین پاسخ ظاهری دقیقاً یکسان
می‌شود. برای متن خلاق، فقط semantic equivalence قابل‌ادعاست؛ یکسانی byte-by-byte
واقع‌بینانه نیست.

## ۸. بدون API Token در شروع

RC2 سه adapter مرجع دارد:

1. `ManualHostAdapter`: بستهٔ hash-bound را در ChatGPT/Gemini/Grok قرار می‌دهیم و
   JSON را برمی‌گردانیم؛ Runtime نه network دارد نه token؛
2. `ScriptedPortableAdapter`: fixture و code fallback برای تست و کارهای ثابت؛
3. interface همان `BrainAdapter`: در آینده adapter زنده می‌تواند اضافه شود بدون
   تغییر Entity/DNA/Decision، ولی key بیرون artifact و در secret manager می‌ماند.

در RC2 هیچ SDK فروشنده، endpoint زنده یا API key اضافه یا تست نشده است.

## ۹. تالار مشورت

Council برای هر درخواست فعال نمی‌شود. trigger آن risk/uncertainty/impact است.
پروتکل:

1. هر عضو روی یک proposal hash و snapshot یکسان، رأی دور اول را کور می‌دهد؛
2. بعد از رأی همهٔ اعضای لازم، rationale/evidence آشکار می‌شود؛
3. اعضا حداکثر در دورهای محدود رأی را بازبینی می‌کنند؛
4. رأی با وزن کالیبره‌شده و confidence محاسبه می‌شود؛
5. در کار high-risk، veto نقش Risk/Policy نتیجه را متوقف می‌کند؛
6. dissent و abstention حذف نمی‌شوند؛
7. خروجی Council فقط proposal است و هنوز Policy/Approval لازم است.

توافق مدل‌ها حقیقت را تضمین نمی‌کند؛ خطای هم‌بسته، دادهٔ آموزشی مشترک و hallucination
ممکن است. به همین علت blind round، نقش‌های متفاوت، evidence binding و Human Root
حفظ شده‌اند.

## ۱۰. جریان واقعی Secretary-001

1. پیام channel پس از authentication وارد Conversation Spine می‌شود؛
2. Store منشی حقیقت Canonical را نگه می‌دارد؛
3. Profile تنها فیلدهای سطح موردنیاز را Projection می‌کند؛
4. Kernel یک Capsule با hash، version، vector و budget می‌سازد؛
5. Router ارزان‌ترین مسیر ایمن را انتخاب می‌کند؛
6. Brain/Code یک Secretary Decision می‌دهد؛
7. Validator کلید اضافه، action اجرایی، type نامعتبر و approval ناقص را رد می‌کند؛
8. Template خروجی استاندارد را deterministic می‌سازد؛
9. اگر کنشی لازم باشد، فقط Proposal به مسیر Policy/Approval داده می‌شود؛
10. Event/Audit نتیجه را با Provider، pack hash، projection hash و dissent ثبت می‌کند.

## ۱۱. رویدادهای پیشنهادی RC2

این نام‌ها candidate هستند و تا ratification قرارداد Canonical نیستند:

- `BrainInvocationProposed`
- `BrainHandlerAttempted`
- `FractalNodeExpanded`
- `SecretaryDecisionProposed`
- `CouncilBallotCommitted`
- `CouncilRoundRevealed`
- `CouncilDecisionProposed`
- `ShadowRunCompared`
- `CompilationPromotionRecommended`
- `HumanReviewRequested`

Payload خام حساس یا chain-of-thought ذخیره نمی‌شود؛ hash، reason code، evidence ref
و خلاصهٔ audit کافی ثبت می‌شود.

## ۱۲. تهدیدها و کنترل‌ها

| تهدید | کنترل |
|---|---|
| Prompt injection | Projection محدود، Prompt ثابت، output schema، عدم tool authority |
| Provider drift | fixture/eval، versioned overlay، Shadow، semantic hash |
| Token explosion | local expansion، budget، cache hash-bound، template rendering |
| Hallucinated omitted data | منع inverse reconstruction؛ reload Canonical برای up-resolution |
| Secret leakage | عدم ذخیره token در Pack، classification gate، metadata-only compatibility |
| State split | state خارج Provider/channel؛ expected version و canonical hash |
| Council echo chamber | blind round، نقش/مدل متنوع، dissent، veto، evidence |
| Self-modifying runaway | candidate-only generation، one-step promotion، Human Root، rollback |
| Brain outage | code fallback؛ اگر ناکافی بود defer؛ C6 فقط با restore proof |

## ۱۳. آنچه RC2 اثبات نمی‌کند

- کیفیت زندهٔ ChatGPT/Gemini/Grok یا مدل Local؛
- atomicity واقعی PostgreSQL/Outbox؛
- crash/replay روی infrastructure؛
- disaster restore؛
- security/load/chaos؛
- سودآوری یا ایمنی معاملهٔ مالی؛
- Production readiness یا Canonical ratification.

این موارد برای E3/E4 و تصمیم صریح Human Root باز می‌مانند.
