# برنامهٔ پیاده‌سازی پس از Freeze — World v6.2

## Slice 1 — Canonical Resolution Core

خروجی: strict hashing، Profile registry، compiler، envelope، patch validator و
Brain segment vector به‌صورت package مستقل. معیار پایان: تمام تست‌های property،
schema و profile drift روی CI.

## Slice 2 — PostgreSQL Authority Boundary

خروجی: repository واقعی با optimistic version، `control_epoch` و یک transaction
برای State + Event + Command + Approval + Outbox. معیار پایان: integration test
روی PostgreSQL واقعی و crash در هر نقطهٔ transaction بدون partial truth.

## Slice 3 — Policy و Approval Binding

خروجی: action dependency evaluation، approval دقیق و expiry/revocation. معیار
پایان: recipient/payload/effect/version/epoch mismatch همگی deny شوند.

## Slice 4 — Executor و Adapter Registry

خروجی: worker فقط روی Outbox committed، fencing/recheck، idempotency، receipt و
reconciliation Event. Telegram ابتدا با sandbox/fake server، سپس یک live canary.

## Slice 5 — secretary-001 Vertical Slice

خروجی: Conversation R0/R1، Task patch، Price R0/R1، Proforma draft و PDF delivery
از مسیر Outbox. هیچ method داخل Entity حق network I/O ندارد.

## Slice 6 — Recovery و Promotion Evidence

خروجی: restore روی ماشین تازه از backup، source commit، migrations، `uv.lock`,
SBOM، Profile/Compiler hash و artifact bytes. سپس security/load/chaos و گزارش
E3/E4 طبق evidence ladder.

## ترتیب ممنوع

تا Slice 2 و 3 کامل نشده‌اند، وصل‌کردن live Telegram/Drive مجاز نیست. تا Slice 6
و Ratification نهایی کامل نشده، هیچ Entity با عنوان Canonical Born معرفی نمی‌شود.
