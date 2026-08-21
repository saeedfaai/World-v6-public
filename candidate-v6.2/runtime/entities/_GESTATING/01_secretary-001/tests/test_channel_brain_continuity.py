from src.channels import normalize_chatgpt
from src.secretary import Secretary001
from adapters.telegram import TelegramRuntimeConfig, normalize_update


def test_same_root_identity_across_chatgpt_and_telegram():
    s = Secretary001()
    chat = normalize_chatgpt("chatgpt-session-user", "اول این کار رو یادداشت کن")
    s.ingest_message(chat)

    cfg = TelegramRuntimeConfig("token", "777", "saeedfaut")
    tg = normalize_update({"message":{"message_id":12,"from":{"id":777,"username":"saeedfaut"},"text":"حالا ادامه همون کار"}},
                          verified_transport=True, config=cfg)
    s.ingest_message(tg)

    ctx = s.brain_context()
    assert [x["value"]["text"] for x in ctx] == ["اول این کار رو یادداشت کن", "حالا ادامه همون کار"]
    assert all(x["profile_id"] == "secretary.conversation" for x in ctx)


def test_provider_handoff_does_not_change_conversation():
    s = Secretary001(execution_resolution="R1")
    s.ingest_message(normalize_chatgpt("user", "نامه رو آماده کن"))
    s.record_reply("پیش‌نویس آماده شد", provider="openai", channel="chatgpt")
    s.record_reply("برای ادامه همان نامه آماده‌ام", provider="google", channel="telegram")
    ctx = s.brain_context()
    assert ctx[-2]["value"]["brain_provider"] == "openai"
    assert ctx[-1]["value"]["brain_provider"] == "google"
    assert len(ctx) == 3


def test_non_root_telegram_does_not_merge_into_root_context():
    s = Secretary001()
    cfg = TelegramRuntimeConfig("token", "777", "saeedfaut")
    other = normalize_update({"message":{"message_id":1,"from":{"id":999,"username":"customer"},"text":"قیمت بده"}},
                             verified_transport=True, config=cfg)
    s.ingest_message(other)
    assert s.brain_context() == []
    assert len(s.store.conversation_context("telegram:999", "telegram:999:secretary-001")) == 1
