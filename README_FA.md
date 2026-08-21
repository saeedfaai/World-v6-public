# World v6.2 — Complete Fractal Multi-Brain Architecture RC3

این بسته معماری کامل و قراردادهای عملیاتی World v6.2 را برای مسیر فراکتالی
سادگی→پیچیدگی، Resolution، DNA، حافظه، Multi-Brain، Council، Shadow Compilation و
ستون عدم‌انقراض تثبیت می‌کند.

وضعیت رسمی:
`RATIFICATION_CANDIDATE_NOT_CANONICAL_NOT_DEPLOYED`


## همکاری تجاری و پیشنهاد مالی

World v6.2 برای **پیشنهادهای تجاری و مالی** باز است؛ از جمله خرید لایسنس تجاری، اجرای Enterprise، OEM/White-label، سهم از درآمد یا Royalty، شراکت راهبردی و Joint Venture. پیشنهادهای دارای ساختار مالی مشخص در اولویت بررسی هستند.

انتشار عمومی این مخزن هیچ حق استفادهٔ تجاری ایجاد نمی‌کند. هر استفادهٔ تجاری نیازمند **قرارداد کتبی جداگانه با Saeed Farokhi** است.

**[مدل‌های همکاری و راهنمای پیشنهاد تجاری](COMMERCIAL.md)** · **[ارسال Commercial Inquiry](https://github.com/saeedfaai/World-v6-public/issues/new?template=commercial-inquiry.yml)**

> Issueهای GitHub عمومی‌اند؛ اطلاعات محرمانه یا جزئیات خصوصی معامله را در Issue ننویسید. Issue فقط برای شروع ارتباط و انتقال مذاکره به کانال خصوصی است.

Root Constitution v1.0 و Canonical Entity DNA v1.2 تغییر نکرده‌اند. RC2 به‌عنوان
والد مستقل و قابل Rollback محفوظ است. RC3 هیچ Deployment، Migration، Provider API
زنده یا Canonical promotion را ادعا نمی‌کند.

## نتیجهٔ معماری

- Mother Core یک هستهٔ deterministic و مستقل از مدل است؛ Provider هرگز هویت، حافظه،
  حقیقت یا Authority نیست.
- سیستم در هفت Plane مستقل Governance، Truth، Control، Cognition، Effect، Evolution
  و Observability شکسته شده است.
- فراکتال دارای هشت سطح World→Entity→Mission→Skill→Workflow→Step→Tool→Field است؛
  فقط branch لازم و فقط با trigger و budget محدود باز می‌شود.
- بردار اجرای مستقل `R/X/B/D/C/A/E/M` و Continuity مستقل `F0..F4` مانع تبدیل یک
  «Level» مبهم به چند نوع اختیار متفاوت می‌شود.
- Resolution کابل داده است: Projection پایین کوچک است، Canonical truth کامل می‌ماند،
  و Up-resolution فقط با reload منبع حقیقت انجام می‌شود.
- تمام مدل‌ها یک Brain Pack، Prompt Contract، Decision Schema و Model Capability
  Card مشترک می‌بینند؛ پاسخ خام مدل مستقیماً وارد State یا Effect نمی‌شود.
- Universal Manual Host همین حالا برای هر مدلی که از JSON contract پیروی کند قابل
  استفاده است و از سمت Runtime نه network می‌خواهد و نه API token.
- پاسخ‌های هم‌معنا normalize و با renderer قطعی به جواب استاندارد تبدیل می‌شوند؛
  «همان جواب» در سطح Semantic/Rendered تعریف شده، نه الزاماً بایت خام Provider.
- Council برای تصمیم حساس دارای ballot کور، بازبینی محدود، رأی کالیبره، dissent و veto
  است، ولی consensus هیچ‌وقت Policy یا Human Root را دور نمی‌زند.
- Hot Path سریع می‌ماند؛ Shadow Path رفتار را مقایسه و evidence تولید می‌کند؛ C0..C6
  فقط مرحله‌ای promote می‌شود و self-mutation ممنوع است.
- External Effect فقط پس از Policy، exact ApprovalBinding، transactional Outbox و
  Executor idempotent مجاز است.

## مرجع کامل

سند اصلی:

`candidate-v6.2/docs/WORLD_V6_2_FRACTAL_MULTI_BRAIN_ARCHITECTURE_v1.1_FA.md`

مانیفست ماشین‌خوان:

`candidate-v6.2/architecture/ARCHITECTURE_MANIFEST_v1.1.0-rc3.json`

این دو فایل به hash یکدیگر و Release Manifest متصل‌اند. سند شامل قوانین تغییرناپذیر،
topology، primitiveها، الگوریتم expansion، state machine مدل، routing formula، memory
compiler، lifecycle، Council، maturity، effect protocol، استقرار، threat model، SLO،
خطاها، test architecture، acceptance gates و milestones اجرایی است.

## اجرای فوری با هر مدل، بدون API

۱. Bundle کم‌حجم R0 را بسازید:

```bash
python tools/universal_model_bridge.py export-task \
  --task-json candidate-v6.2/brain-packs/secretary-001/examples/task-input.example.json \
  --provider-label any-model-name > portable-model-bundle.json
```

۲. Integrity را بررسی کنید:

```bash
python tools/universal_model_bridge.py validate-bundle \
  --bundle-json portable-model-bundle.json
```

۳. Bundle را بدون تغییر به مدل بدهید و فقط JSON پاسخ را در `response.json` ذخیره کنید.

۴. پاسخ را strict validate و deterministic render کنید:

```bash
python tools/universal_model_bridge.py validate-response \
  --response-json response.json
```

این مسیر `manual portability` را اثبات می‌کند. اتصال خودکار ChatGPT/Gemini/Grok/Local
از طریق API همان قرارداد را دارد، اما تا Adapter زنده و Gateهای E3/E4 پاس نشوند در این
Release ادعا نشده است.

## شواهد RC3

- Core: **78/78 PASS**
- Secretary: **22/22 PASS**
- Candidate: **100/100 PASS**
- Preserved ancestor: **14/14 PASS**
- مجموع مستقل pytest: **114/114 PASS**
- تست اختصاصی معماری/Universal Host: **7/7 PASS**
- Demo آفلاین ChatGPT/Gemini/Grok: **3/3 PASS**
- Schema، hash binding، tamper rejection، secret scan، compileall، lock و SBOM: **PASS**
- سطح ادعای فعلی: **E2 local contract evidence**

موارد باز: Live provider API، PostgreSQL atomic integration، crash/replay/reconciliation،
fresh restore، security/load/chaos، Git tag و Human Root canonical ratification.

## محیط و تست

```bash
UV_CACHE_DIR=/tmp/world-v62-uv-cache \
UV_PROJECT_ENVIRONMENT=/tmp/world-v62-rc3-venv \
uv sync --locked --all-groups

PYTHONPATH=candidate-v6.2/runtime \
UV_CACHE_DIR=/tmp/world-v62-uv-cache \
UV_PROJECT_ENVIRONMENT=/tmp/world-v62-rc3-venv \
uv run --locked --all-groups python -m pytest -q \
  candidate-v6.2/runtime/core/tests

PYTHONPATH=candidate-v6.2/runtime:candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001 \
UV_CACHE_DIR=/tmp/world-v62-uv-cache \
UV_PROJECT_ENVIRONMENT=/tmp/world-v62-rc3-venv \
uv run --locked --all-groups python -m pytest -q \
  candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/tests
```

## ترتیب مطالعه

1. `candidate-v6.2/docs/WORLD_V6_2_FRACTAL_MULTI_BRAIN_ARCHITECTURE_v1.1_FA.md`
2. `candidate-v6.2/architecture/ARCHITECTURE_MANIFEST_v1.1.0-rc3.json`
3. `candidate-v6.2/docs/decisions/RC3_ARCHITECTURE_SCOPE_AND_ROLLBACK_FA.md`
4. `candidate-v6.2/schemas/model-capability-card.schema.json`
5. `candidate-v6.2/schemas/portable-model-bundle.schema.json`
6. `candidate-v6.2/brain-packs/secretary-001/model-cards/universal-manual-host.v1.json`
7. `tools/universal_model_bridge.py`
8. `candidate-v6.2/docs/ACCEPTANCE_GATES_v6.2_RC3.json`
9. `candidate-v6.2/evidence/FINAL_VALIDATION_RC3.txt`

Canonical ratification فقط با تصمیم صریح Human Root روی hash نهایی Release انجام می‌شود.
