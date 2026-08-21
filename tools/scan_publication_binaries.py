#!/usr/bin/env python3
"""Fail-closed privacy/secret scan for binary publication artifacts.

This scanner does not decide copyright ownership. It detects common credential forms,
email addresses, Office comments/tracked-change payloads, suspicious publication paths,
and exposes document metadata for release review. It is intentionally dependency-free.
"""
from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BINARY_SUFFIXES = {".pdf", ".docx", ".pptx", ".zip"}
SKIP_PARTS = {".git", ".venv", "__pycache__", ".pytest_cache"}

PATTERNS = {
    "openai_key": re.compile(rb"sk-(?:proj-)?[A-Za-z0-9_-]{20,}"),
    "github_token": re.compile(rb"gh[pousr]_[A-Za-z0-9]{30,}"),
    "google_api_key": re.compile(rb"AIza[0-9A-Za-z_-]{30,}"),
    "telegram_bot_token": re.compile(rb"\b[0-9]{8,10}:[A-Za-z0-9_-]{35}\b"),
    "private_key": re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "email": re.compile(rb"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
}

OFFICE_REVIEW_MARKERS = (
    "comments.xml",
    "commentsExtended.xml",
    "people.xml",
    "persons.xml",
)


def _skipped(relative: Path) -> bool:
    return any(part in SKIP_PARTS for part in relative.parts)


def scan_path_hygiene(findings: list[dict]) -> None:
    """Reject malformed or escape-like names before suffix-based binary discovery.

    A previous private-prep snapshot contained quote/backslash-literal filenames that
    looked like DOCX names to a human but did not have a real .docx suffix. Failing on
    these characters prevents binary files from bypassing the suffix scanner.
    """
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if _skipped(relative):
            continue
        rel = relative.as_posix()
        reasons: list[str] = []
        if '"' in rel:
            reasons.append("quote")
        if "\\" in rel:
            reasons.append("backslash")
        if any(ord(char) < 32 or ord(char) == 127 for char in rel):
            reasons.append("control-character")
        if reasons:
            findings.append(
                {
                    "kind": "suspicious_publication_path",
                    "location": rel,
                    "value": ",".join(reasons),
                }
            )


def binary_files() -> list[Path]:
    out: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in BINARY_SUFFIXES:
            continue
        rel = path.relative_to(ROOT)
        if _skipped(rel):
            continue
        out.append(path)
    return sorted(out, key=lambda p: p.relative_to(ROOT).as_posix())


def scan_bytes(label: str, data: bytes, findings: list[dict]) -> None:
    for kind, pattern in PATTERNS.items():
        matches = sorted({m.group(0).decode("utf-8", "replace") for m in pattern.finditer(data)})
        for value in matches:
            findings.append({"kind": kind, "location": label, "value": value})


def scan_office(path: Path, findings: list[dict], metadata: list[dict]) -> None:
    rel = path.relative_to(ROOT).as_posix()
    try:
        with zipfile.ZipFile(path) as zf:
            for name in zf.namelist():
                lower = name.lower()
                if any(lower.endswith(marker.lower()) for marker in OFFICE_REVIEW_MARKERS):
                    findings.append({"kind": "office_review_payload", "location": f"{rel}!{name}", "value": "present"})
                if lower in {"docprops/core.xml", "docprops/app.xml", "docprops/custom.xml"}:
                    text = zf.read(name)
                    metadata.append({"file": rel, "part": name, "text": text.decode("utf-8", "replace")[:4000]})
                    scan_bytes(f"{rel}!{name}", text, findings)
                elif lower.endswith((".xml", ".rels", ".txt", ".json", ".md", ".csv")):
                    try:
                        scan_bytes(f"{rel}!{name}", zf.read(name), findings)
                    except RuntimeError:
                        findings.append({"kind": "encrypted_zip_member", "location": f"{rel}!{name}", "value": "unreadable"})
    except zipfile.BadZipFile:
        findings.append({"kind": "invalid_office_or_zip", "location": rel, "value": "not a valid ZIP container"})


def scan_pdf(path: Path, findings: list[dict], metadata: list[dict]) -> None:
    rel = path.relative_to(ROOT).as_posix()
    data = path.read_bytes()
    scan_bytes(rel, data, findings)
    for key in (b"/Author", b"/Creator", b"/Producer", b"/Title", b"/Subject"):
        pos = data.find(key)
        if pos >= 0:
            metadata.append({"file": rel, "part": key.decode(), "text": data[pos:pos + 500].decode("latin-1", "replace")})


def main() -> int:
    findings: list[dict] = []
    metadata: list[dict] = []
    scan_path_hygiene(findings)
    files = binary_files()
    for path in files:
        suffix = path.suffix.lower()
        if suffix == ".pdf":
            scan_pdf(path, findings, metadata)
        else:
            scan_office(path, findings, metadata)

    report = {
        "scanner": "world-v6-publication-binary-scan-v2",
        "binary_files_scanned": len(files),
        "files": [p.relative_to(ROOT).as_posix() for p in files],
        "metadata_observations": metadata,
        "findings": findings,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if findings:
        print(f"PUBLICATION_BINARY_SCAN=FAIL FINDINGS={len(findings)}", file=sys.stderr)
        return 1
    print(f"PUBLICATION_BINARY_SCAN=PASS FILES={len(files)} PATH_HYGIENE=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
