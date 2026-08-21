# System dependencies — World v6.2 RC3

The Python dependency graph is locked by `uv.lock`. PDF letter rendering also
requires one of these executable names on `PATH`:

- `libreoffice`
- `soffice`

The renderer discovers either name and creates an isolated per-run LibreOffice
user profile. Production images must pin the LibreOffice build and the Persian
font packages in their container/IaC digest; that image digest belongs in the
deployment evidence bundle.

No live provider, Telegram, Drive or PostgreSQL credential belongs in this
source package.
