# تصمیم Freeze و Rollback — World v6.2 RC1

## Freeze

پس از تأیید صریح Human Root، مدل Profile/کابل v0.2، strict Canonical JSON،
provenance envelope، bounded patch، Brain segment vector و external-effect
boundary به‌عنوان مبنای Phase 1 freeze می‌شوند. این تأیید به‌تنهایی Production
یا Canonical runtime promotion نیست.

## Migration

RC1 برای خود Resolution ستون یا جدول Authority جدیدی اضافه نمی‌کند. Profile و
Compiler artifactهای نسخه‌دارند و metadata در payloadهای Command/Event موجود
حمل می‌شود. پیاده‌سازی Phase 1 همچنان باید schema موجود State/Event/Command/
Approval/Outbox را روی PostgreSQL واقعی migrate و آزمایش کند.

## Rollback

1. Profile/Compiler RC1 از active path خارج می‌شوند.
2. هیچ Canonical State/Event/History پاک یا کم‌Resolution نمی‌شود.
3. projection cache قابل حذف است.
4. event metadata ناشناخته append-only باقی می‌ماند.
5. rollback به ancestor فقط rollback کد است؛ legacy bypass یا Entity-direct I/O
   دوباره مجاز نمی‌شود.
6. failure در projection/hash/profile برابر STOP/QUEUE/RECORD/ESCALATE است.
