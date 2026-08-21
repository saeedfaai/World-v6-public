# تصمیم نسخه و Rollback — World v6.2 RC2

## تصمیم

نام انتشار: `World v6.2 Fractal Multi-Brain RC2`  
نسخه: `6.2.0-rc.2`  
نوع تغییر: لایهٔ runtime و قرارداد candidate؛ بدون تغییر Root Constitution یا
Canonical DNA v1.2.

## چرا v7 نیست

این بسته اصل جدیدی بالاتر از قانون اساسی ایجاد نمی‌کند. Brain Farm، Council، محور
بلو‌غ C و Fractal Node همگی زیر Kernel/Policy موجود قرار دارند. نسخهٔ Major فقط در
صورت تغییر معنای قراردادهای FROZEN یا authority لازم است.

## سازگاری

- RC1 به‌عنوان ancestor مستقل حفظ شده است.
- Profileهای v0.2 و compiler v0.2 بدون تغییر مصرف می‌شوند.
- DNA execution overlay فایل جداست و Canonical DNA را overwrite نمی‌کند.
- Entity قدیمی می‌تواند بدون فعال‌کردن Portable Brain به کار RC1 ادامه دهد.
- هیچ migration دیتابیس برای این RC لازم نیست.

## فعال‌سازی پیشنهادی

1. فقط `Scripted/Manual` و proposal-only؛
2. اجرای eval/fixture برای هر Provider Overlay؛
3. Shadow روی state snapshot و بدون external effect؛
4. Human Root review برای C5؛
5. adapter زنده فقط در branch/محیط جدا با secret manager؛
6. E3/E4 پیش از هر ادعای Production.

## Rollback

Rollback عملیاتی RC2 یعنی حذف binding به `PortableSecretaryService` و بازگشت به
مسیر RC1. چون RC2 در این مرحله state migration و external effect ندارد، rollback
به بازگردانی code/config محدود است. Eventهای candidate باید append-only باقی
بمانند و حذف نشوند. Artifact RC1 و hash آن باید مستقل نگه داشته شود.

## شرط توقف

هرکدام از موارد زیر rollout را متوقف می‌کند: mismatch هویت/profile/hash، کاهش
Resolution، output خارج schema، direct effect، اختلاف state version، شکست replay،
نشت secret، Council veto در کار high-risk یا پایان budget.
