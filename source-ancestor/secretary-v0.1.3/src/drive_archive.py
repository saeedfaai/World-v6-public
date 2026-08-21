"""Google Drive archive reader for secretary-001.

This module is entity-local. It reads the configured letters folder and can fetch the
latest PDF without making Google Drive part of Entity identity/state. Secrets/tokens
must come from runtime secret injection or an injected client.
"""
from __future__ import annotations
from dataclasses import dataclass
import json
import os
import urllib.parse
import urllib.request
import urllib.error


class DriveArchiveError(RuntimeError):
    pass


@dataclass(frozen=True)
class ArchivedDocument:
    file_id: str
    name: str
    mime_type: str
    modified_time: str | None = None
    size: int | None = None


@dataclass(frozen=True)
class DriveArchiveConfig:
    access_token: str
    letters_folder_id: str = "1CP3dc0EeC31us3GXneH3ftJaoAe_aefj"

    @classmethod
    def from_env(cls, *, letters_folder_id: str | None = None):
        token = os.environ.get("GOOGLE_DRIVE_ACCESS_TOKEN")
        if not token:
            raise RuntimeError(
                "GOOGLE_DRIVE_ACCESS_TOKEN must come from Secret Store/runtime, "
                "or inject a DriveArchiveClient backed by the host's Google credential"
            )
        return cls(
            access_token=token,
            letters_folder_id=(letters_folder_id or os.environ.get("LETTERS_DRIVE_FOLDER_ID")
                               or cls.letters_folder_id),
        )


class DriveArchiveClient:
    API = "https://www.googleapis.com/drive/v3"

    def __init__(self, config: DriveArchiveConfig, *, timeout: float = 30.0, opener=None):
        self.config = config
        self.timeout = timeout
        self._opener = opener or urllib.request.urlopen

    def _request(self, url: str) -> bytes:
        req = urllib.request.Request(
            url,
            headers={"Authorization": f"Bearer {self.config.access_token}"},
            method="GET",
        )
        try:
            with self._opener(req, timeout=self.timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise DriveArchiveError(f"Google Drive HTTP {exc.code}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise DriveArchiveError(f"Google Drive network error: {exc.reason}") from exc

    def latest_pdf(self) -> ArchivedDocument:
        folder = self.config.letters_folder_id
        query = f"'{folder}' in parents and trashed = false and mimeType = 'application/pdf'"
        params = urllib.parse.urlencode({
            "q": query,
            "orderBy": "modifiedTime desc",
            "pageSize": "1",
            "fields": "files(id,name,mimeType,modifiedTime,size)",
            "supportsAllDrives": "true",
            "includeItemsFromAllDrives": "true",
        })
        raw = self._request(f"{self.API}/files?{params}")
        try:
            payload = json.loads(raw.decode("utf-8"))
        except Exception as exc:
            raise DriveArchiveError("Google Drive list response was not valid JSON") from exc
        files = payload.get("files") or []
        if not files:
            raise DriveArchiveError("No PDF found in the configured letters archive")
        f = files[0]
        return ArchivedDocument(
            file_id=str(f["id"]),
            name=str(f["name"]),
            mime_type=str(f.get("mimeType") or "application/pdf"),
            modified_time=f.get("modifiedTime"),
            size=(int(f["size"]) if f.get("size") is not None else None),
        )

    def download_bytes(self, document: ArchivedDocument) -> bytes:
        if document.mime_type != "application/pdf" and not document.name.lower().endswith(".pdf"):
            raise DriveArchiveError(f"Refusing non-PDF archive object: {document.name}")
        file_id = urllib.parse.quote(document.file_id, safe="")
        return self._request(f"{self.API}/files/{file_id}?alt=media&supportsAllDrives=true")
