# Migration / Rollback Plan — World v6.2 Resolution-Native Candidate

## ورود به Candidate
1. Canonical v6 baseline و secretary-001 v0.1.3 را immutable ancestor نگه دار.
2. Resolution profiles/schema/code را در candidate branch اضافه کن.
3. Runtime bindingهای جدید Resolution صریح می‌فرستند؛ legacy callers بدون پارامتر همان رفتار قبلی را دارند.
4. ابتدا R0 read/projection و internal task/draft را shadow-test کن.
5. R1 را فقط برای price/proforma/external-document paths فعال کن؛ policy/approval فعلی دست‌نخورده است.
6. هیچ DB schema migration در v0.1 اجرا نکن.

## Rollback
- active candidate code/profile را disable کن؛
- entity manifest candidate را به ancestor v0.1.3 برگردان؛
- Canonical State/Event را دست نزن؛
- optional Resolution metadata رویدادها را historical نگه دار؛
- چون projection destructive نیست، restore داده‌ای لازم نیست.

## Failure rule
اگر Projection یا negotiation مبهم باشد: `STOP/QUEUE + RECORD + ESCALATE`؛ هیچ fallbackی مجاز نیست minimum resolution یا existing policy/data rules را کاهش دهد.
