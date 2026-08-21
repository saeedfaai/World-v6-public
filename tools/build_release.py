#!/usr/bin/env python3
"""Build a clean, deterministic World v6.2 RC3 release ZIP and hash indexes."""
from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import zipfile


ARCHIVE_ROOT = "World_v6.2_Fractal_Multi_Brain_RC3"
FORBIDDEN_DIRS = {".git", ".venv", ".pytest_cache", "__pycache__"}
FORBIDDEN_SUFFIXES = {".pyc", ".pyo"}
INDEX_FILES = {"FILE_INVENTORY.txt", "SHA256SUMS.txt"}
FIXED_ZIP_TIME = (2026, 8, 20, 0, 0, 0)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def payload_files(root: Path, *, include_indexes: bool) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part in FORBIDDEN_DIRS for part in relative.parts):
            continue
        if path.is_symlink():
            raise SystemExit(f"symlink is forbidden in release: {relative}")
        if not path.is_file():
            continue
        if path.suffix in FORBIDDEN_SUFFIXES:
            raise SystemExit(f"compiled cache is forbidden in release: {relative}")
        if not include_indexes and relative.as_posix() in INDEX_FILES:
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(root).as_posix())


def write_indexes(root: Path) -> None:
    payload = payload_files(root, include_indexes=False)
    inventory_lines = [
        "World v6.2 RC3 payload inventory",
        "Generated deterministically; FILE_INVENTORY.txt and SHA256SUMS.txt are index files.",
        "",
        *[path.relative_to(root).as_posix() for path in payload],
        "",
    ]
    (root / "FILE_INVENTORY.txt").write_text("\n".join(inventory_lines), encoding="utf-8")

    hashed = [
        path for path in payload_files(root, include_indexes=True)
        if path.relative_to(root).as_posix() != "SHA256SUMS.txt"
    ]
    checksum_lines = [
        f"{sha256(path)}  {path.relative_to(root).as_posix()}" for path in hashed
    ]
    (root / "SHA256SUMS.txt").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")


def build_zip(root: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in payload_files(root, include_indexes=True):
            relative = path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(f"{ARCHIVE_ROOT}/{relative}", FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: build_release.py ROOT OUTPUT_ZIP")
    root = Path(sys.argv[1]).resolve()
    output = Path(sys.argv[2]).resolve()
    if not root.is_dir():
        raise SystemExit(f"release root not found: {root}")
    if root == output.parent or output.is_relative_to(root):
        raise SystemExit("output ZIP must be outside release root")
    write_indexes(root)
    build_zip(root, output)
    hash_file = output.with_name(output.stem + "_SHA256.txt")
    hash_file.write_text(f"{sha256(output)}  {output.name}\n", encoding="utf-8")
    print(f"ZIP={output}")
    print(f"SHA256={sha256(output)}")
    print(f"FILES={len(payload_files(root, include_indexes=True))}")


if __name__ == "__main__":
    main()
