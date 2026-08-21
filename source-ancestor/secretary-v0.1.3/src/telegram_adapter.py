"""Secretary-local Telegram interface.

Telegram is only a transport. Entity identity/conversation/state live outside Telegram.
Secrets come only from environment/secret store.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import json
import mimetypes
import os
import secrets
import urllib.request
import urllib.error
from .channels import normalize_telegram


class TelegramDeliveryError(RuntimeError):
    pass


@dataclass(frozen=True)
class TelegramRuntimeConfig:
    bot_token: str
    root_user_id: str | None
    root_chat_id: str | None = None
    root_username: str = "saeedfaut"
    webhook_secret: str | None = None

    @classmethod
    def from_env(cls):
        token = os.environ.get("TELEGRAM_BOT_TOKEN")
        root = os.environ.get("TELEGRAM_ROOT_USER_ID")
        chat_id = os.environ.get("TELEGRAM_ROOT_CHAT_ID") or root
        username = os.environ.get("TELEGRAM_ROOT_USERNAME", "saeedfaut").lstrip("@")
        if not token:
            raise RuntimeError("TELEGRAM_BOT_TOKEN must come from Secret Store/environment")
        return cls(token, root, chat_id, username, os.environ.get("TELEGRAM_WEBHOOK_SECRET"))


def is_declared_root_handle(username: str | None, config: TelegramRuntimeConfig) -> bool:
    """Setup hint only; username is not sufficient authentication."""
    return bool(username) and username.lstrip("@").casefold() == config.root_username.casefold()


def is_root_actor(actor_id: str, config: TelegramRuntimeConfig) -> bool:
    """Authority is granted only by the verified immutable Telegram numeric user_id."""
    return bool(config.root_user_id) and str(actor_id) == str(config.root_user_id)


def normalize_update(update: dict, *, verified_transport: bool, config: TelegramRuntimeConfig):
    message = update.get("message") or update.get("edited_message") or {}
    user = message.get("from") or {}
    actor_id = str(user.get("id", "unknown"))
    text = message.get("text") or message.get("caption") or ""
    telegram_message_id = str(message.get("message_id") or "")
    principal_id = "human-root" if is_root_actor(actor_id, config) else f"telegram:{actor_id}"
    return normalize_telegram(
        actor_id,
        text,
        verified_transport,
        principal_id=principal_id,
        conversation_id=("human-root:secretary-001" if principal_id == "human-root" else f"{principal_id}:secretary-001"),
        message_id=(f"telegram:{actor_id}:{telegram_message_id}" if telegram_message_id else None),
    )


class TelegramBotClient:
    """Small Bot API client for outbound text/document delivery.

    No framework dependency is required. File upload uses Telegram Bot API sendDocument
    with multipart/form-data. This class never decides authorization; caller must pass
    an already-authorized effect.
    """

    def __init__(self, config: TelegramRuntimeConfig, *, timeout: float = 30.0, opener=None):
        self.config = config
        self.timeout = timeout
        self._opener = opener or urllib.request.urlopen

    def _url(self, method: str) -> str:
        return f"https://api.telegram.org/bot{self.config.bot_token}/{method}"

    def _decode(self, raw: bytes) -> dict:
        try:
            payload = json.loads(raw.decode("utf-8"))
        except Exception as exc:
            raise TelegramDeliveryError("Telegram returned a non-JSON response") from exc
        if not payload.get("ok"):
            raise TelegramDeliveryError(payload.get("description") or "Telegram Bot API request failed")
        return payload

    def send_message(self, text: str, *, chat_id: str | None = None) -> dict:
        target = str(chat_id or self.config.root_chat_id or "")
        if not target:
            raise TelegramDeliveryError("TELEGRAM_ROOT_CHAT_ID/USER_ID is not bound")
        body = json.dumps({"chat_id": target, "text": text}, ensure_ascii=False).encode("utf-8")
        req = urllib.request.Request(self._url("sendMessage"), data=body, headers={"Content-Type": "application/json"}, method="POST")
        try:
            with self._opener(req, timeout=self.timeout) as resp:
                return self._decode(resp.read())
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise TelegramDeliveryError(f"Telegram HTTP {exc.code}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise TelegramDeliveryError(f"Telegram network error: {exc.reason}") from exc

    def send_document(self, file_path: str | Path, *, caption: str | None = None,
                      chat_id: str | None = None) -> dict:
        path = Path(file_path)
        if not path.is_file():
            raise FileNotFoundError(path)
        return self.send_document_bytes(
            path.read_bytes(), filename=path.name, caption=caption, chat_id=chat_id
        )

    def send_document_bytes(self, data: bytes, *, filename: str, caption: str | None = None,
                            chat_id: str | None = None, mime_type: str | None = None) -> dict:
        """Send in-memory document bytes. Useful for PDFs downloaded from Drive/cloud storage."""
        if not data:
            raise TelegramDeliveryError("document payload is empty")
        target = str(chat_id or self.config.root_chat_id or "")
        if not target:
            raise TelegramDeliveryError("TELEGRAM_ROOT_CHAT_ID/USER_ID is not bound")

        boundary = "----WorldV6" + secrets.token_hex(12)
        chunks: list[bytes] = []

        def add_field(name: str, value: str) -> None:
            chunks.extend([
                f"--{boundary}\r\n".encode(),
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),
                value.encode("utf-8"), b"\r\n",
            ])

        add_field("chat_id", target)
        if caption:
            add_field("caption", caption[:1024])

        mime = mime_type or mimetypes.guess_type(filename)[0] or "application/octet-stream"
        chunks.extend([
            f"--{boundary}\r\n".encode(),
            f'Content-Disposition: form-data; name="document"; filename="{filename}"\r\n'.encode("utf-8"),
            f"Content-Type: {mime}\r\n\r\n".encode(),
            data, b"\r\n",
            f"--{boundary}--\r\n".encode(),
        ])
        body = b"".join(chunks)
        req = urllib.request.Request(
            self._url("sendDocument"), data=body,
            headers={"Content-Type": f"multipart/form-data; boundary={boundary}"}, method="POST",
        )
        try:
            with self._opener(req, timeout=self.timeout) as resp:
                return self._decode(resp.read())
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise TelegramDeliveryError(f"Telegram HTTP {exc.code}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise TelegramDeliveryError(f"Telegram network error: {exc.reason}") from exc


def root_price_inquiry_text(inquiry) -> str:
    return (
        "منشی — استعلام قیمت جدید\n"
        f"مشتری: {inquiry.customer_id}\n"
        f"کالا: {inquiry.product_key}\n"
        f"مقدار: {inquiry.requested_quantity} {inquiry.unit}\n"
        f"شناسه استعلام: {inquiry.inquiry_id}\n"
        "قیمت فعال/معتبر برای این مشتری و کالا پیدا نشد. لطفاً قیمت را اعلام و تأیید کنید."
    )
