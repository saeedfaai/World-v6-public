# World v6.2 Candidate — چرا در v0.1 Migration دیتابیس جدید نداریم؟

Resolution v0.1 یک لایه View/Compatibility است، نه منبع حقیقت تازه. Schema فعلی از قبل state/config pointers و Event/Command payload دارد؛ بنابراین profile ref و desired/minimum/effective resolution بدون جدول Authority جدید قابل حمل‌اند.

افزودن ستون/جدول فقط وقتی مجاز است که نیاز واقعی Query/Index/locking یا persistence ثابت شود. تا آن زمان عدم migration سه مزیت دارد: rollback بدون data rewrite، عدم ایجاد Source of Truth موازی، و حفظ سادگی Phase-1 PostgreSQL transaction boundary.

اگر نیاز اثبات شد، migration آینده باید additive، versioned، rollbackable و همراه conformance/crash tests باشد.
