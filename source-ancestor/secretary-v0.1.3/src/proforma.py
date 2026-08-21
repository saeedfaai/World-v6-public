from __future__ import annotations
from pathlib import Path
from decimal import Decimal
from html import escape
from weasyprint import HTML
from .models import ProformaRequest


def fmt_num(v: Decimal) -> str:
    return f"{v:,.0f}"


def render_proforma_pdf(req: ProformaRequest, output_pdf: str | Path) -> Path:
    subtotal = sum((i.total_irr for i in req.items), Decimal("0"))
    tax = (subtotal * req.tax_rate).quantize(Decimal("1"))
    grand = subtotal + tax
    rows = "".join(
        f"<tr><td>{n}</td><td>{escape(i.description)}</td><td>{fmt_num(i.quantity)}</td><td>{escape(i.unit)}</td><td>{fmt_num(i.unit_price_irr)}</td><td>{fmt_num(i.total_irr)}</td></tr>"
        for n, i in enumerate(req.items, 1)
    )
    notes = "".join(f"<li>{escape(n)}</li>" for n in req.notes)
    html = f'''<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><style>
    @page {{ size:A4; margin:14mm; }}
    body {{ font-family:'Noto Sans Arabic','DejaVu Sans',sans-serif; direction:rtl; font-size:11pt; }}
    h1 {{ text-align:center; font-size:16pt; margin:0 0 12px; }}
    .meta {{ display:flex; justify-content:space-between; border:1px solid #777; padding:8px; margin-bottom:8px; }}
    table {{ width:100%; border-collapse:collapse; }} th,td {{ border:1px solid #777; padding:6px; text-align:center; }}
    th {{ font-weight:700; }} .totals {{ margin-top:10px; width:45%; margin-right:auto; }}
    .foot {{ margin-top:16px; font-size:9.5pt; }}
    </style></head><body>
    <h1>پیش فاکتور فروش کالا - شرکت کارن پلیمر فلات پارس</h1>
    <div class="meta"><span>خریدار: {escape(req.customer_name)} | تلفن: {escape(req.customer_phone)}</span><span>شماره: {escape(req.document_no)} | تاریخ: {escape(req.document_date)}</span></div>
    <table><thead><tr><th>ردیف</th><th>شرح کالا/خدمات</th><th>تعداد</th><th>واحد</th><th>مبلغ واحد (ریال)</th><th>مبلغ کل (ریال)</th></tr></thead><tbody>{rows}</tbody></table>
    <table class="totals"><tr><td>جمع</td><td>{fmt_num(subtotal)}</td></tr><tr><td>مالیات/عوارض</td><td>{fmt_num(tax)}</td></tr><tr><td><b>جمع قابل پرداخت</b></td><td><b>{fmt_num(grand)}</b></td></tr></table>
    <div class="foot"><p>اعتبار قیمت: {req.validity_hours} ساعت.</p><ul>{notes}</ul><p>این سند Draft است تا زمانی که سیاست/تأیید لازم برای قیمت و ارسال طی شود.</p></div>
    </body></html>'''
    output_pdf = Path(output_pdf); output_pdf.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html).write_pdf(str(output_pdf))
    return output_pdf
