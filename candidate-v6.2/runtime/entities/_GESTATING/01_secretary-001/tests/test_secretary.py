from decimal import Decimal
from pathlib import Path
from src.secretary import Secretary001
from src.models import LetterRequest, PriceKey, PriceRecord
from src.channels import normalize_telegram


def test_task_create():
    s=Secretary001()
    t=s.add_task(title="پیگیری مشتری", priority="HIGH", due_at="2026-08-17T09:00:00+03:30")
    assert t.status == "OPEN" and t.task_id in s.store.tasks


def test_missing_price_asks_root():
    s=Secretary001()
    r=s.resolve_price_or_ask_root("cust-1","geotextile-300g","m2",Decimal("1000"))
    assert r["status"] == "ASK_ROOT"


def test_known_price_builds_proforma(tmp_path):
    s=Secretary001(execution_resolution="R1")
    s.store.put_price(PriceRecord(PriceKey("cust-1","geotextile-300g","m2"), Decimal("460000")))
    out=tmp_path/"pi.pdf"
    r=s.make_proforma_from_known_price(customer_id="cust-1",customer_name="مشتری تست",customer_phone="09120000000",product_key="geotextile-300g",description="ژئوتکستایل پلی استر ۳۰۰ گرم",quantity=Decimal("1000"),unit="m2",document_no="TEST-001",document_date="۱۴۰۵/۰۵/۲۵",output_pdf=out)
    assert r["status"] == "DRAFT_READY" and out.exists() and out.stat().st_size > 1000


def test_letter_pdf(tmp_path):
    s=Secretary001()
    out=tmp_path/"letter.pdf"
    req=LetterRequest(recipient="مدیریت محترم پروژه تست",subject="نامه آزمایشی تولد منشی",body="احتراماً، این نامه جهت آزمون مسیر تولید PDF منشی صادر شده است.",document_no="TEST-SECRETARY-001",document_date="۱۴۰۵/۰۵/۲۵")
    s.make_letter(req,out)
    assert out.exists() and out.stat().st_size > 1000


def test_unverified_telegram_is_not_authenticated():
    m=normalize_telegram("user-1","منشی پیش فاکتور بزن",False)
    assert m.authenticated is False


def test_root_price_inquiry_message():
    from adapters.telegram import root_price_inquiry_text
    s=Secretary001()
    r=s.resolve_price_or_ask_root("cust-9","pvc-1.5mm","m2",Decimal("250"))
    msg=root_price_inquiry_text(r["inquiry"])
    assert "استعلام قیمت جدید" in msg and "cust-9" in msg and "pvc-1.5mm" in msg
