import json
from pathlib import Path
import tempfile
import pytest
from adapters.telegram import TelegramRuntimeConfig, TelegramBotClient
from src.secretary import DirectExternalIOForbidden, Secretary001


class FakeResponse:
    def __init__(self, payload): self.payload = payload
    def __enter__(self): return self
    def __exit__(self, *args): pass
    def read(self): return json.dumps(self.payload).encode()


def fake_opener_ok(req, timeout=30):
    assert req.full_url.endswith('/sendDocument')
    body = req.data
    assert b'name="chat_id"' in body
    assert b'123456789' in body
    assert b'name="document"' in body
    assert b'%PDF-1.4' in body
    return FakeResponse({"ok": True, "result": {"message_id": 77}})


def test_send_document_multipart():
    cfg = TelegramRuntimeConfig('TESTTOKEN', '123456789', '123456789')
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'letter.pdf'
        p.write_bytes(b'%PDF-1.4\nTEST')
        r=TelegramBotClient(cfg, opener=fake_opener_ok).send_document(p, caption='نامه تست')
        assert r['ok'] is True and r['result']['message_id'] == 77


def test_secretary_never_calls_transport_adapter_directly():
    s=Secretary001(execution_resolution="R1")
    cfg = TelegramRuntimeConfig('TESTTOKEN', '123456789', '123456789')
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'letter.pdf'; p.write_bytes(b'%PDF-1.4\nTEST')
        with pytest.raises(DirectExternalIOForbidden):
            s.send_pdf_to_root_telegram(p, root_approved=True, config=cfg, opener=fake_opener_ok)
