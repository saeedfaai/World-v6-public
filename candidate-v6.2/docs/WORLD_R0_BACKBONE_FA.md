# World v6.2 — R0 Backbone / کابل‌های مادر

R0 قرار نیست همه داده را داخل یک پیام بریزد؛ فقط قراردادهایی را که برای «همان موجود ماندن و امن عمل کردن» لازم‌اند ثابت نگه می‌دارد:

`IDENTITY → INPUT → TASK/COMMAND → PROPOSAL → POLICY → APPROVAL → ACTION → EVENT → STATE/MEMORY POINTERS`

در Resolution بالاتر هر کابل می‌تواند به سیم‌های بیشتری شکسته شود، اما semantics کابل مادر حذف یا عوض نمی‌شود. Kernel/Policy همیشه Canonical truth را می‌بیند؛ R0 بیشتر برای Brain/Context/Workflow/UX یک View کم‌جزئیات است.

نمونه: `TASK` در R0 می‌تواند `id/title/status/next_action` باشد؛ در R1 `due/priority/domain/goal` اضافه شود؛ در R2 dependency/risk/evidence وارد شود. برگشت R2→R0 فقط Projection است و R2 data را پاک نمی‌کند.

قرارداد normative کامل، قواعد Profile/hash، Action wiring، Patch، Brain vector و
اثر خارجی در `RESOLUTION_CABLE_MODEL_v0.2_FA.md` و artifact ماشین‌خوان
`profiles/world-backbone-profile.v0.2.json` قرار دارد.
