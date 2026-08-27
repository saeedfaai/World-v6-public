from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"
OUT.mkdir(parents=True, exist_ok=True)

FONT = "Arial,Helvetica,sans-serif"


def esc(x: object) -> str:
    return html.escape(str(x), quote=True)


def svg_open(w: int, h: int, title: str, desc: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{esc(title)}</title>',
        f'<desc id="desc">{esc(desc)}</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        '<style>text{font-family:Arial,Helvetica,sans-serif;fill:#111}.t{font-size:28px;font-weight:700}.s{font-size:18px}.m{font-size:16px}.b{font-weight:700}.box{fill:white;stroke:#222;stroke-width:2}.soft{fill:#f4f4f4;stroke:#555;stroke-width:1.5}.line{stroke:#222;stroke-width:2;fill:none}.dash{stroke:#555;stroke-width:2;stroke-dasharray:8 7;fill:none}</style>',
    ]


def text(x: int, y: int, value: str, cls: str = "s", anchor: str = "middle") -> str:
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{esc(value)}</text>'


def rect(x: int, y: int, w: int, h: int, cls: str = "box", rx: int = 12) -> str:
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}"/>'


def line(x1: int, y1: int, x2: int, y2: int, cls: str = "line") -> str:
    return f'<path d="M{x1},{y1} L{x2},{y2}" class="{cls}" marker-end="url(#arrow)"/>'


def defs() -> str:
    return '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#222"/></marker></defs>'


def figure1() -> Path:
    w, h = 1400, 820
    s = svg_open(w, h, "World 8 governed effect contract", "Conceptual architecture showing a logical Actor independent from transient runtime identity and a proposal, decision, effect sequence guarded by authority, fencing, evidence and recovery checks.")
    s += [defs(), text(700, 55, "Figure 1. Governed effect contract and runtime separation", "t")]

    # Identity plane
    s += [rect(70, 120, 250, 105, "soft"), text(195, 160, "Logical Actor", "s b"), text(195, 192, "durable authority + attribution", "m")]
    s += [rect(70, 300, 250, 150, "box"), text(195, 340, "Transient execution", "s b"), text(195, 372, "provider / session / process", "m"), text(195, 400, "runtime AgentId / worker", "m")]
    s += [line(195, 225, 195, 300, "dash"), text(335, 270, "explicit binding", "m", "start")]

    # Domain stages
    xs = [410, 700, 990]
    labels = [("Proposal / Prediction", "domain information; not authority"), ("Approval / Decision", "governed authorization evidence"), ("Effect / Execution", "externally visible state change")]
    for x, (a, b) in zip(xs, labels):
        s += [rect(x, 145, 250, 105, "box"), text(x+125, 184, a, "s b"), text(x+125, 216, b, "m")]
    s += [line(660, 197, 700, 197), line(950, 197, 990, 197)]
    s += [text(845, 115, "PROPOSAL ≠ DECISION ≠ EFFECT", "s b")]

    # Governance gates
    gates = [
        (410, "Actor/action/resource", "effect-time authority"),
        (650, "Fence / lease generation", "reject stale effectors"),
        (890, "Evidence integrity", "tamper-evident receipts"),
        (1130, "Recovery gate", "reconstruct before effect"),
    ]
    for x, a, b in gates:
        s += [rect(x, 350, 210, 110, "soft"), text(x+105, 390, a, "m b"), text(x+105, 422, b, "m")]
    s += [line(320, 375, 410, 405), line(620, 405, 650, 405), line(860, 405, 890, 405), line(1100, 405, 1130, 405)]
    s += [line(1235, 350, 1115, 250)]

    # Society adapters
    s += [rect(410, 585, 350, 120, "box"), text(585, 623, "Company Society adapter", "s b"), text(585, 655, "QUOTE → PURCHASE APPROVAL → ORDER EFFECT", "m")]
    s += [rect(820, 585, 350, 120, "box"), text(995, 623, "Trading Society adapter", "s b"), text(995, 655, "FORECAST → TRADE DECISION → SYNTHETIC ORDER", "m")]
    s += [text(790, 535, "Same governed kernel; domain semantics remain outside the kernel", "s b")]
    s += [line(585, 585, 585, 460, "dash"), line(995, 585, 995, 460, "dash")]

    s += [text(700, 775, "Scope: architectural contract evaluated under frozen synthetic/runtime experiments; no live trading or business effect.", "m"), '</svg>']
    p = OUT / "figure1_governed_effect_contract.svg"
    p.write_text("\n".join(s), encoding="utf-8")
    return p


def figure2() -> Path:
    w, h = 1500, 780
    s = svg_open(w, h, "W8-P01 evidence ladder", "Five-stage evidence ladder from hardened reference falsification through cross-society conformance, runtime binding, mutation and compound faults, and AutoGen external runtime composability.")
    s += [defs(), text(750, 55, "Figure 2. Evidence ladder and claim ceiling", "t")]
    cards = [
        (70, "E1", "Reference falsification", "98,000 trials", "Hardened baseline removes generic revoke/CAS/idempotency advantages"),
        (350, "E2", "Cross-Society conformance", "1,000 + 1,000", "Same 8 invariants across Company and Trading; all rates 1.0"),
        (630, "E3", "Canonical/runtime binding", "rollback-safe probes", "Authorization, fencing, immutability, actor/work and recovery checks"),
        (910, "E4", "Mutation + compound faults", "5/5 + 3×1,000", "Reference mutation score 1.0; frozen valid-path false-deny 0.0"),
        (1190, "E5", "External runtime", "2,000 AutoGen cases", "Pinned AutoGen Core 0.7.5; bounded composability result"),
    ]
    for x, stage, title, metric, note in cards:
        s += [rect(x, 150, 240, 280, "box"), text(x+120, 195, stage, "t"), text(x+120, 238, title, "s b"), text(x+120, 285, metric, "s b")]
        words = note.split()
        lines=[]; cur=[]
        for word in words:
            if len(" ".join(cur+[word])) > 29:
                lines.append(" ".join(cur)); cur=[word]
            else: cur.append(word)
        if cur: lines.append(" ".join(cur))
        for i, l in enumerate(lines[:5]): s.append(text(x+120, 330+i*28, l, "m"))
    for a,b in zip([310,590,870,1150],[350,630,910,1190]): s.append(line(a,290,b,290))

    s += [rect(140, 525, 1220, 120, "soft"), text(750, 565, "Claim ceiling after stronger baselines and prior-art review", "s b")]
    s += [text(750, 602, "Supported: bounded effect-governance composition, cross-Society conformance, tested fault containment, external-runtime composability", "m")]
    s += [text(750, 630, "Not supported: production readiness, universal security, universal domain generality, profitability, or general framework superiority", "m")]
    s += [text(750, 720, "Frozen private evidence commit: 34ed68b6…  |  Public reviewer reproduction: run 33113474577", "m"), '</svg>']
    p = OUT / "figure2_evidence_ladder.svg"
    p.write_text("\n".join(s), encoding="utf-8")
    return p


def figure3(summary_path: Path) -> Path:
    d = json.loads(summary_path.read_text(encoding="utf-8"))
    assert d["autogen_core_version"] == "0.7.5"
    h = d["rates"]["hardened"]
    g = d["rates"]["full"]
    scenarios = [
        ("V1_NORMAL", "Valid normal"),
        ("V2_RUNTIME_SWAP", "Valid runtime swap"),
        ("V3_RUNTIME_RECREATE_RECOVER", "Valid recreate + recover"),
        ("X2_REVOKED", "Revoked"),
        ("X3_STALE_VERSION", "Stale version / CAS"),
        ("X4_DUPLICATE", "Duplicate / idempotency"),
        ("X1_STOLEN_APPROVAL", "Stolen approval"),
        ("X5_STALE_FENCE", "Stale fence"),
        ("X6_TAMPER", "Audit tamper"),
        ("X7_EFFECT_BEFORE_RECOVERY", "Effect before recovery"),
    ]
    w, hpx = 1400, 820
    s = svg_open(w, hpx, "AutoGen frozen fault-family comparison", "Matrix of safe rates for hardened generic AutoGen controls versus the same pinned AutoGen runtime with the World-8-style governance composition.")
    s += [text(700, 55, "Figure 3. Frozen AutoGen 0.7.5 fault-family comparison", "t")]
    s += [text(860, 112, "Hardened generic controls", "s b"), text(1120, 112, "+ World-8-style governance", "s b")]
    y0, rowh = 145, 58
    for i,(key,label) in enumerate(scenarios):
        y=y0+i*rowh
        s += [text(610, y+36, label, "m", "end")]
        for x, rate in [(790, h[key]["safe_rate"]),(1050, g[key]["safe_rate"])]:
            fill = "#f2f2f2" if rate == 1.0 else "white"
            stroke = "#222"
            s.append(f'<rect x="{x}" y="{y+8}" width="210" height="42" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
            s.append(text(x+105, y+36, f"safe = {rate:.1f}", "s b"))
    s += [text(700, 760, "100 trials per case × 10 scenarios × 2 variants = 2,000 runtime cases; no LLM/API key; no external effects.", "m"), '</svg>']
    p=OUT/"figure3_autogen_fault_matrix.svg"
    p.write_text("\n".join(s), encoding="utf-8")
    return p


def main() -> None:
    import argparse
    ap=argparse.ArgumentParser()
    ap.add_argument("--autogen-summary", type=Path, required=True)
    a=ap.parse_args()
    files=[figure1(), figure2(), figure3(a.autogen_summary)]
    for p in files:
        txt=p.read_text(encoding="utf-8")
        assert txt.startswith('<svg') and txt.rstrip().endswith('</svg>')
        print(p, p.stat().st_size)


if __name__ == "__main__":
    main()
