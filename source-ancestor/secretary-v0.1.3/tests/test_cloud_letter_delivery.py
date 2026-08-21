import json
from dataclasses import dataclass
import pytest
from src.secretary import Secretary001
from src.drive_archive import ArchivedDocument
from src.telegram_adapter import TelegramRuntimeConfig


LATEST_NAME = "برق منطقه‌ای انزلی - ۱۴۰۵-۰۵-۲۵.pdf"
LATEST_ID = "15dB1-BWSEKJ5W3pc1fF1S90KW69HQyCk"


class FakeDrive:
    def latest_pdf(self):
        return ArchivedDocument(LATEST_ID, LATEST_NAME, "application/pdf", "2026-08-16T08:14:20.264Z", 160011)
    def download_bytes(self, document):
        assert document.file_id == LATEST_ID
        return b"%PDF-1.7\nFAKE-CANONICAL-LETTER"


class FakeResponse:
    def __enter__(self): return self
    def __exit__(self, *args): pass
    def read(self): return json.dumps({"ok": True, "result": {"message_id": 101}}).encode()


def fake_telegram(req, timeout=30):
    assert req.full_url.endswith('/sendDocument')
    assert LATEST_NAME.encode('utf-8') in req.data
    assert b'%PDF-1.7' in req.data
    assert b'99887766' in req.data
    return FakeResponse()


def test_latest_letter_exact_name_and_send():
    s = Secretary001()
    cfg = TelegramRuntimeConfig('TOKEN', '123', '123')
    out = s.send_latest_archived_letter_to_telegram(
        root_approved=True,
        chat_id='99887766',
        expected_filename=LATEST_NAME,
        drive_client=FakeDrive(),
        telegram_config=cfg,
        telegram_opener=fake_telegram,
    )
    assert out['status'] == 'SENT'
    assert out['drive_file_id'] == LATEST_ID
    assert out['filename'] == LATEST_NAME
    assert out['telegram']['result']['message_id'] == 101


def test_filename_mismatch_blocks_send():
    s = Secretary001()
    cfg = TelegramRuntimeConfig('TOKEN', '123', '123')
    with pytest.raises(RuntimeError, match='mismatch'):
        s.send_latest_archived_letter_to_telegram(
            root_approved=True,
            chat_id='99887766',
            expected_filename='نامه اشتباه.pdf',
            drive_client=FakeDrive(),
            telegram_config=cfg,
            telegram_opener=fake_telegram,
        )


def test_root_approval_required():
    s = Secretary001()
    with pytest.raises(PermissionError):
        s.send_latest_archived_letter_to_telegram(
            root_approved=False,
            chat_id='99887766',
            drive_client=FakeDrive(),
        )
