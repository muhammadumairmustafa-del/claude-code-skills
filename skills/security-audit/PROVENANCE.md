# Provenance

Vendored unchanged from cloudflare/security-audit-skill (https://github.com/cloudflare/security-audit-skill), path `skills/security-audit/`, commit c1c8a8c1471069fb0e188eeaff69b8e8db6564a8 (2026-09-14). MIT License (see `LICENSE`). Added to this library 2026-11-09 as `security-audit` v1.0.0+cloudflare.c1c8a8c; only this PROVENANCE.md and LICENSE were added.

Local use notes (not part of upstream):
- Guidance mode is the default; full audit mode writes files under `~/security-audit-skill/<repo>/run-N` and runs target code only in an OS-enforced sandbox. Do not run full mode without explicit request.
- `make-audit-push` 2.2.0 calls this skill in guidance mode for its security phase.
- Never probe deployed or shared endpoints.
