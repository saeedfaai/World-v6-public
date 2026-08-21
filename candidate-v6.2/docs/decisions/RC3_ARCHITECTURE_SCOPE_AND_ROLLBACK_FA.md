# تصمیم نسخه و Rollback — World v6.2 Fractal Multi-Brain RC3

شناسه: `WV6.2-ADR-RC3-001`  
تاریخ: `2026-08-20`  
وضعیت: `ACCEPTED_FOR_RATIFICATION_CANDIDATE`  

## تصمیم

تغییرات معماری Multi-Brain، قرارداد عمومی Model Capability Card، Portable Model
Bundle، مسیر Universal Manual Host و مانیفست ماشین‌خوان معماری، یک Release Candidate
جدید با نسخهٔ `6.2.0-rc.3` می‌سازند.

این تغییرها:

- Root Constitution v1.0 را تغییر نمی‌دهند؛
- Canonical Entity DNA v1.2 را تغییر نمی‌دهند؛
- RC2 را overwrite نمی‌کنند؛
- هیچ Migration پایگاه‌داده‌ای را اجرا نمی‌کنند؛
- هیچ Provider زنده یا Production Deployment را اثبات نمی‌کنند؛
- همهٔ Brain outputها را proposal-only نگه می‌دارند.

بنابراین RC3 یک معماری و بستهٔ انطباق کامل‌تر روی v6.2 است، نه v7 و نه Canonical
promotion.

## علت نیاز به RC3

RC2 Primitiveهای Runtime را تثبیت کرد، اما برای اجرای فوری با یک مدل دلخواه این
موارد به قرارداد مستقل و قابل‌آزمون نیاز داشتند:

1. تعریف دقیق مرز Provider و Model Capability؛
2. Bundle خودبسنده برای انتقال به هر میزبان مدل؛
3. مسیر بدون API و بدون token در Runtime؛
4. مانیفست معماری با وضعیت هر Component و مرز Evidence؛
5. آزمون tamper، schema، provider-neutral semantics و deterministic rendering؛
6. تفکیک صریح قابلیت «Manual Contract Tested» از «Live API Verified».

## سازگاری

- قرارداد Brain Pack منشی همان `world-v6.secretary-001.portable-brain@1.0.0-rc2`
  باقی می‌ماند تا RC2 consumerها نشکنند.
- Profileهای Resolution همان `0.2.0` و hashهایشان ثابت می‌مانند.
- RC3 فقط قراردادهای افزایشی و ابزار Universal Bridge اضافه می‌کند.
- پاسخ‌های ChatGPT/Gemini/Grok fixture و هر مدل منطبق، پس از normalization به
  semantic hash و renderer مشترک می‌رسند.

## Rollback

Rollback عملیاتی RC3 عبارت است از انتخاب بستهٔ مستقل RC2 با ZIP SHA-256 زیر:

```text
6a49fea3be989005d90622161c1a1bc77e6c8041955e52cbae93c095fc62e114
```

از آنجا که RC3 Migration یا Canonical write جدیدی ندارد، rollback به RC2 نیازمند
Data downgrade نیست. هر Artifact آزمایشی RC3 با `architecture_ref` یا
`bundle_contract` خودش قابل تشخیص و quarantine است.

## شرط Promotion

RC3 تا زمان ثبت تصمیم صریح Human Root روی hash نهایی Release و تکمیل Gateهای E3/E4،
`RATIFICATION_CANDIDATE_NOT_CANONICAL_NOT_DEPLOYED` باقی می‌ماند.
