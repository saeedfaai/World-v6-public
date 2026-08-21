#!/usr/bin/env python3
"""Fail-closed verification for the World v6.2 RC3 repository snapshot."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_PARTS = {".git", ".venv", ".pytest_cache", "__pycache__"}
FORBIDDEN_SUFFIXES = {".pyc", ".pyo"}
SECRET_PATTERNS = {
    "openai": re.compile(rb"sk-(?:proj-)?[A-Za-z0-9_-]{20,}"),
    "github": re.compile(rb"gh[pousr]_[A-Za-z0-9]{30,}"),
    "google": re.compile(rb"AIza[0-9A-Za-z_-]{30,}"),
    "telegram": re.compile(rb"\b[0-9]{8,10}:[A-Za-z0-9_-]{35}\b"),
}

REQUIRED_PATHS = (
    "README.md",
    "README_FA.md",
    "REPOSITORY_STATUS.json",
    "RELEASE_MANIFEST.json",
    "SOURCE_PROVENANCE.json",
    "SBOM.cdx.json",
    "uv.lock",
    "pylock.toml",
    "candidate-v6.2/docs/WORLD_V6_2_FRACTAL_MULTI_BRAIN_ARCHITECTURE_v1.1_FA.md",
    "candidate-v6.2/docs/RESOLUTION_CABLE_MODEL_v0.2_FA.md",
    "candidate-v6.2/docs/FRACTAL_MULTI_BRAIN_RUNTIME_v1.0_FA.md",
    "candidate-v6.2/architecture/ARCHITECTURE_MANIFEST_v1.1.0-rc3.json",
    "candidate-v6.2/runtime/core/resolution.py",
    "candidate-v6.2/runtime/core/fractal_runtime.py",
    "candidate-v6.2/runtime/core/brain_gateway.py",
    "candidate-v6.2/runtime/core/portable_brain.py",
    "candidate-v6.2/runtime/core/council.py",
    "candidate-v6.2/runtime/core/effects.py",
    "candidate-v6.2/runtime/core/evolution.py",
    "candidate-v6.2/runtime/core/kernel.py",
    "candidate-v6.2/runtime/core/postgres_schema.sql",
    "candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/entity.yaml",
    "candidate-v6.2/runtime/entities/_GESTATING/01_secretary-001/BIRTH_READINESS.md",
    "candidate-v6.2/runtime/adapters/telegram.py",
    "candidate-v6.2/runtime/adapters/drive_archive.py",
    "candidate-v6.2/fractal/council/secretary-high-risk-council.v1.json",
    "candidate-v6.2/brain-packs/secretary-001/portable-brain-pack.v1.0.0.json",
    "tools/universal_model_bridge.py",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def payload_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(part in FORBIDDEN_PARTS for part in relative.parts):
            continue
        if path.is_symlink():
            raise AssertionError(f"symlink forbidden: {relative}")
        if not path.is_file():
            continue
        if path.suffix in FORBIDDEN_SUFFIXES:
            raise AssertionError(f"compiled cache forbidden: {relative}")
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(ROOT).as_posix())


def load_json(relative: str) -> object:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def verify_required_paths() -> None:
    missing = [relative for relative in REQUIRED_PATHS if not (ROOT / relative).is_file()]
    if missing:
        raise AssertionError(f"required files missing: {missing}")


def verify_json() -> int:
    count = 0
    for path in payload_files():
        if path.suffix != ".json":
            continue
        json.loads(path.read_text(encoding="utf-8"))
        count += 1
    return count


def verify_claim_boundaries() -> None:
    status = load_json("REPOSITORY_STATUS.json")
    release = load_json("RELEASE_MANIFEST.json")
    architecture = load_json(
        "candidate-v6.2/architecture/ARCHITECTURE_MANIFEST_v1.1.0-rc3.json"
    )
    assert status["status"] == "RATIFICATION_CANDIDATE_NOT_CANONICAL_NOT_DEPLOYED"
    assert status["canonical"] is False
    assert status["deployed"] is False
    assert status["production_ready"] is False
    assert status["entity"]["birth_declared"] is False
    assert status["evidence"]["level"] == "E2"
    assert release["version"] == "6.2.0-rc.3"
    assert release["status"] == status["status"]
    assert release["ratification"] == "NOT_RECORDED"
    assert release["candidate"]["runtime_network_enabled"] is False
    assert release["candidate"]["runtime_api_tokens_enabled"] is False
    assert release["candidate"]["all_brain_outputs"] == "PROPOSAL_ONLY"
    assert architecture["architecture_version"] == "1.1.0-rc3"
    assert architecture["status"] == status["status"]


def verify_checksum_index() -> int:
    index = ROOT / "SHA256SUMS.txt"
    if not index.is_file():
        raise AssertionError("SHA256SUMS.txt missing")
    count = 0
    for line_number, line in enumerate(index.read_text(encoding="utf-8").splitlines(), 1):
        if not line:
            continue
        digest, separator, relative = line.partition("  ")
        if separator != "  " or len(digest) != 64:
            raise AssertionError(f"invalid checksum line {line_number}")
        path = ROOT / relative
        if not path.is_file():
            raise AssertionError(f"checksummed file missing: {relative}")
        if sha256(path) != digest:
            raise AssertionError(f"checksum mismatch: {relative}")
        count += 1
    return count


def verify_no_embedded_secrets() -> None:
    findings: list[str] = []
    for path in payload_files():
        if path.suffix.lower() in {".pdf", ".docx", ".pptx", ".zip"}:
            continue
        data = path.read_bytes()
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(data):
                findings.append(f"{label}:{path.relative_to(ROOT)}")
    if findings:
        raise AssertionError(f"possible embedded secrets: {findings}")


def main() -> None:
    verify_required_paths()
    json_count = verify_json()
    verify_claim_boundaries()
    checksum_count = verify_checksum_index()
    verify_no_embedded_secrets()
    print("WORLD_V6_REPOSITORY_VERIFICATION=PASS")
    print(f"JSON_DOCUMENTS={json_count}")
    print(f"CHECKSUM_ENTRIES={checksum_count}")
    print("CLAIM_BOUNDARY=RC3_E2_NOT_CANONICAL_NOT_DEPLOYED")
    print("SECRET_SCAN=PASS")


if __name__ == "__main__":
    main()
