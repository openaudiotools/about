# 002 — Enrich status page and sync device statuses from project board

**Date:** 2026-03-19
**Scope:** `scripts/fetch_project_status.py`, `docs/status.md`, `docs/devices/index.md`

## Summary

Enhanced the project status page with an intro paragraph, a phases table fetched from the GitHub Projects API, and initiative tables grouped by phase. Also added automatic propagation of the "Innitiative Status" field to the devices index page, replacing hardcoded status lines.

## What changed

| Change | Detail |
|--------|--------|
| Intro paragraph | Static text added to both the live and fallback status page — explains side-project context and prototype-by-2026 goal |
| Phases table | Fetched from the `Innitiative Status` single-select field options via GraphQL; rendered with name and description columns |
| Grouped initiatives | Items grouped by phase in board order (Concept, Product Design, etc.) instead of a flat table |
| `get_field_value()` | Generalized field extractor replacing `get_initiative_status()` — accepts any field name |
| `collect_items()` | Extracted item collection into a shared function used by both `build_page()` and `update_devices_page()` |
| `update_devices_page()` | Reads `docs/devices/index.md`, matches `## Heading` names (case-insensitive) to initiative titles, replaces `**Status:** X` lines with live values |
| Field name fix | Corrected `"innitiative Status"` (lowercase i) to `"Innitiative Status"` (capital I) to match the actual board field |

## Context

The status page infrastructure (workflow, nav entry, gitignore) was set up in entry 001. This entry builds on that by making the generated page richer and keeping the devices page in sync with the project board. The devices page previously had manually maintained statuses ("Active development", "Concept") that could drift from the board — now they're updated automatically during each workflow run.
