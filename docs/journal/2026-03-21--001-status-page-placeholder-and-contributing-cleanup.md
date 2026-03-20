# 001 — Status page placeholder and contributing cleanup

**Date:** 2026-03-21
**Scope:** `scripts/fetch_project_status.py`, `docs/status.md`, `docs/contributing.md`, `.gitignore`

## Summary

Refactored the status page generation script to use placeholder markers instead of overwriting the entire file. This preserves hand-written content in `docs/status.md` while still allowing the CI script to update the devices table from the GitHub Projects API. Also simplified the contributing page by replacing the devices table with links to the Devices and Status pages.

## What changed

| File | Change |
|------|--------|
| `scripts/fetch_project_status.py` | Replaced full-file overwrite with marker-based replacement (`<!-- DEVICE_STATUS_TABLE_START -->` / `<!-- DEVICE_STATUS_TABLE_END -->`). Removed `INTRO` and `FALLBACK_PAGE` constants. Renamed `build_page` → `build_table`. Added `replace_table_block()` and updated `write_output()` to read-modify-write. |
| `docs/status.md` | Added `<!-- DEVICE_STATUS_TABLE_START -->` and `<!-- DEVICE_STATUS_TABLE_END -->` markers around the devices table. Hand-written sections (intro, "What's next?", "Phases") are preserved. |
| `.gitignore` | Removed `docs/status.md` — the file is now tracked since the script no longer overwrites it entirely. |
| `docs/contributing.md` | Replaced the 6-row device discussion/status table with inline links to the Devices and Status pages. |

## Context

The previous approach had `fetch_project_status.py` generating the entire `status.md` from scratch, which meant any manual edits (intro text, phases section, what's next) would be lost on the next CI run. The file was gitignored to avoid conflicts, but that also meant CI had no base file to work with. The new marker-based approach solves both problems: the file is tracked with hand-written content, and the script only touches the table block between markers.
