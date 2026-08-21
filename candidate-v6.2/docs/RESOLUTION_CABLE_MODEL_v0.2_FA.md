# مدل نهایی کابل و رزولوشن — World v6.2 RC1

وضعیت: **Ratification Candidate / هنوز Canonical نشده**  
نسخهٔ مدل: `0.2.0`  
اصل حاکم: Root Constitution v1.0 بدون تغییر است.

## ۱. تصمیم معماری

World یک حقیقت Canonical با بیشترین fidelity نگه می‌دارد. Resolution فقط شکل
عملیاتی مشاهده و کار با همان حقیقت است:

- `R0` کابل‌های مادر و معنای پایدار سیستم است.
- `R1+` سیم‌های ریزتری هستند که اطلاعات، کنترل و دقت بیشتری اضافه می‌کنند.
- سیم ریز حق ندارد کابل مادر را حذف، جایگزین یا بازتفسیر کند.
- پایین‌آمدن Resolution حذف داده از Canonical نیست؛ فقط projection مشتق‌شده است.
- بالارفتن Resolution از روی View پایین بازسازی نمی‌شود؛ Canonical دوباره load و
  compile می‌شود.
- Resolution با Version، Maturity، Autonomy، Evidence و Authority پنج محور جداست.

این ساختار همان ایدهٔ «تصویر ثابت با وضوح‌های مختلف» را به یک قرارداد قابل تست
تبدیل می‌کند.

## ۲. کابل‌های مادر R0

| cable_id | معنای تغییرناپذیر | نمونهٔ سیم‌های مادر |
|---|---|---|
| `IDENTITY` | این World/Entity/Root چه کسی است | `world_id`, `entity_id`, `root_owner_ref` |
| `INPUT` | چه چیزی از چه منبع و بازیگری وارد شد | `source_ref`, `actor_ref`, `classification` |
| `TASK_COMMAND` | درخواست کاری چیست و در چه وضعی است | `command_id`, `intent`, `status` |
| `PROPOSAL` | چه عملِ هنوز اجرا‌نشده‌ای پیشنهاد شده | `proposal_ref`, `requested_action` |
| `POLICY` | تصمیم سیاست چیست | `decision_ref`, `verdict` |
| `APPROVAL` | آیا approval دقیقاً به همان effect بسته است | `approval_ref`, `bound_effect_hash` |
| `ACTION` | نوع هدف و وضعیت اثر چیست | `action_type`, `target_ref`, `effect_state` |
| `EVENT` | چه رخداد append-only ثبت شد | `event_id`, `event_type`, `entity_sequence`, `outcome` |
| `STATE_MEMORY` | وضعیت و cursor حافظه کجاست | `state_ref`, `event_cursor`, `memory_profile_ref` |

فایل ماشین‌خوان متناظر:
`profiles/world-backbone-profile.v0.2.json`.

## ۳. سیم ریز چیست؟

هر Field Rule یک سیم نسخه‌دار است و حداقل این مشخصات را دارد:

- `path`: JSON Pointer دقیق و بدون ابهام؛
- `cable_id`: کابل مادر والد؛
- `semantic_contract_id`: معنای مستقل و پایدار سیم؛
- `introduced_at`: اولین Resolution قابل مشاهده؛
- `write_min_resolution`: حداقل Resolution برای پیشنهاد تغییر؛
- `downgrade_policy`: یکی از `SAFE_TO_PROJECT`،
  `READ_ONLY_WHEN_PROJECTED` یا `NO_DOWNGRADE`؛
- `data_class`: طبقه‌بندی که projection حق پایین‌آوردنش را ندارد؛
- `expected_type`: نوع Canonical؛
- `required_for_actions`: اعمالی که بدون این سیم مجاز نیستند.

Profile نیز به `profile_id + version + profile_hash` بسته است. عدد `R1` بدون
Profile هیچ معنای کامل و قابل اعتماد ندارد.

## ۴. قوانین ریاضی/رفتاری

برای Profile ثابت و `i <= j`:

1. **Monotonic inclusion:** سیم‌های R0 در R1+ باقی می‌مانند.
2. **Compositionality:** `P_i(P_j(x)) = P_i(x)`.
3. **Identity invariance:** source و canonical hash در همهٔ Viewها ثابت‌اند.
4. **Authority monotonicity:** Resolution پایین‌تر یا بالاتر به‌تنهایی authority
   ایجاد نمی‌کند.
5. **Risk/classification monotonicity:** کم‌شدن جزئیات، خطر یا طبقه‌بندی را کم
   اعلام نمی‌کند.
6. **No inverse hallucination:** تابع `P_j^-1` برای ساخت Canonical از View پایین
   وجود ندارد.
7. **Projection provenance:** هر View باید Profile/Compiler/Canonical/Projection
   hash، source version، purpose، class و freshness را حمل کند.

## ۵. Envelope مصرف‌کننده و متادیتای Audit

Envelope‌ای که Brain یا مصرف‌کننده می‌بیند شامل این موارد است:

`profile_id`, `profile_version`, `profile_hash`, `source_ref`, `source_version`,
`canonical_hash`, `canonical_resolution`, `effective_resolution`,
`projection_hash`, `compiler_id/version/hash`, `purpose`, `data_class`,
`freshness`, `projection_derived=true`, `projection_authoritative=false`, `value`.

نام سیم‌های حذف‌شده داخل Envelope مصرف‌کننده قرار نمی‌گیرد، چون خود نام یک مسیر
محرمانه ممکن است اطلاعات نشت دهد. `included/omitted/read_only/no_downgrade`
فقط در Audit داخلی نگه‌داری می‌شود.

## ۶. Canonical JSON و Hash

RC1 قرارداد `World Canonical JSON v1` را اعمال می‌کند:

- فقط `null`, boolean, string، integer امن، array و object با کلید string؛
- float، NaN/Infinity، Decimal/datetime خام و هر implicit `default=str` ممنوع؛
- مبلغ دقیق باید طبق schema به decimal string تبدیل شود؛
- ترتیب کلیدها canonical و encoding برابر UTF-8 است؛
- hash برابر SHA-256 بایت Canonical JSON است.

این قاعده collision نوعی مانند عدد `1` در برابر رشتهٔ `"1"` و تفاوت ضمنی بین
زبان‌ها را می‌بندد.

## ۷. Write-back از View پایین

Write-back هیچ‌وقت whole-object replacement نیست. Patch فقط وقتی پذیرفته می‌شود
که هم‌زمان همهٔ guardهای زیر درست باشند:

- `profile_id/version/hash` دقیق؛
- `source_ref` دقیق؛
- `expected_version` جاری؛
- `expected_canonical_hash` جاری؛
- `expected_projection_hash` همان View؛
- مسیر JSON Pointer در Canonical موجود باشد؛
- ancestor آن object باقی مانده باشد؛
- actor مسیر را ببیند و حداقل write resolution را داشته باشد؛
- نوع scalar عوض نشود؛
- array/object به‌صورت یک‌جا جایگزین نشود؛
- مسیر duplicate یا ناشناخته نباشد.

هر mismatch باید fail-closed شود و Canonical دست‌نخورده بماند.

## ۸. Brain Gateway

درخواست Brain از چند `BrainInputSegment` تشکیل می‌شود. هر Segment Profile، hash،
source، desired و minimum مستقل دارد. Provider نیز capability را برای همان
`profile_id@version#hash` اعلام می‌کند. نتیجه یک بردار است، برای مثال:

```text
task=R0, conversation=R1, price=R1
```

Gateway ابتدا Profile را verify و دادهٔ Canonical هر Segment را واقعاً project
می‌کند؛ سپس فقط Envelope مشتق‌شده را به Provider می‌دهد. سازگاری Provider روی
descriptor بدون value سنجیده می‌شود. یک `max_resolution=R9` عمومی پذیرفته نیست.

## ۹. Action و اثر خارجی

Minimum عددی به‌تنهایی کافی نیست. هر Action علاوه بر حداقل Resolution، فهرست
سیم‌های اجباری دارد. برای اجرای خارجی دست‌کم recipient، payload hash، effect
hash، approval ref، policy decision ref، expected version، control epoch و
idempotency لازم است.

`root_approved=true` approval نیست. Approval معتبر باید به command، action،
recipient، payload/effect hash، policy version، expected version، control epoch
و expiry دقیقاً bind شود.

Entity فقط می‌تواند proposal غیرauthoritative بسازد. مسیر مجاز:

```text
Entity proposal
  -> deterministic Policy
  -> exact Human Root ApprovalBinding
  -> one PostgreSQL transaction: Command + State + Event + Outbox
  -> registered Executor recheck
  -> adapter I/O
  -> outcome/reconciliation Event
```

## ۱۰. Cache و افزایش Resolution

کلید حداقل cache:

```text
canonical_hash + source_version + profile_hash + compiler_hash
+ effective_resolution + purpose + data_class + freshness
```

هر تغییر در یکی از این اجزا cache را نامعتبر می‌کند. Cache بقای حقیقت نیست و
در Backup می‌تواند حذف شود. Up-resolution همیشه از Canonical store انجام می‌شود.

## ۱۱. Rollback

Rollback RC1 مسیر candidate/compiler/profile را disable می‌کند؛ هیچ دادهٔ
Canonical downgrade نمی‌شود و هیچ history حذف نمی‌شود. View cache پاک‌شدنی است.
نسخهٔ قدیمی فقط به‌عنوان ancestor/reference نگه داشته می‌شود و حق bypass کردن
Policy یا Resolution را ندارد.

## ۱۲. مرز ادعا

این مدل و reference implementation در سطح E2 تست می‌شوند. تا زمان اثبات
PostgreSQL atomicity، crash/replay، fresh restore، live adapters/providers،
security/load/chaos و ثبت Ratification توسط Human Root، وضعیت **RC / NOT
CANONICAL / NOT PRODUCTION** باقی می‌ماند.
