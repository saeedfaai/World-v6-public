# Portable Brain Pack — Secretary-001

این پوشه یک هویت جدید یا GPT جداگانه نیست؛ بستهٔ قابل‌حمل همان `secretary-001` است.

## اجرای بدون API

1. `portable-brain-pack.v1.0.0.json`، `PROMPT_CONTRACT_v1.0_FA.md` و Projection
   exchange را به میزبان انتخابی بدهید.
2. Overlay همان میزبان را اعمال کنید.
3. فقط JSON مطابق `secretary-decision.schema.json` بگیرید.
4. JSON را از `ManualHostAdapter`/validator عبور دهید.
5. Runtime متن استاندارد را از Template می‌سازد.

در این حالت World Runtime هیچ API token یا network call ندارد. استفادهٔ کاربر از
رابط ChatGPT/Gemini/Grok بیرون Runtime انجام می‌شود.

## فایل‌ها

- `secretary-dna-overlay.v1.3-rc2.json`: جزئیات اجرایی candidate؛ Canonical DNA نیست.
- `portable-brain-pack.v1.0.0.json`: bindingهای hash و Templateها.
- `PROMPT_CONTRACT_v1.0_FA.md`: قواعد یکسان برای همهٔ Brainها.
- `provider-overlays/`: تفاوت پوستهٔ میزبان، بدون تفاوت هویت/Policy.
- `fixtures/`: خروجی‌های هم‌معنا برای تست conformance.

## افزودن Provider جدید

Provider جدید فقط یک Overlay و Adapter می‌گیرد. Entity، Store، Profile، خروجی،
Policy و Template تغییر نمی‌کنند. تا وقتی live eval انجام نشده، وضعیت باید
`NOT_LIVE_VERIFIED` یا معادل آن بماند.

## تضمین پاسخ

وظایف Template-based پاسخ دقیقاً یکسان دارند. وظایف خلاق فقط semantic hash/Policy
هم‌ارز دارند؛ متن آزاد مدل‌ها ممکن است متفاوت باشد و نباید خلاف واقع یکسان اعلام
شود.
