# 001 — Devices page grid cards

**Date:** 2026-03-20
**Scope:** `docs/devices/index.md`, `mkdocs.yml`

## Summary

Replaced the flat list-and-table layout on the Devices overview page with mkdocs-material grid cards for a cleaner, more visual presentation. Added the `pymdownx.emoji` extension to support material and octicons icons.

## What changed

| File | Change |
|------|--------|
| `docs/devices/index.md` | Full rewrite from table-based layout to `div.grid.cards` markup |
| `mkdocs.yml` | Added `pymdownx.emoji` extension with `material.extensions.emoji` index and generator |

Each device card now shows:
- A material icon for visual differentiation (`:material-mixer-settings:`, `:material-piano:`, `:material-hub:`, `:material-microphone:`, `:material-guitar-electric:`)
- One-line description
- Links on a single line separated by `·`: Issue, Discussion, and either Repo (MixTee, SynTee) or Read more (HubTee, Voicee, Stringee)

Removed the per-device **Status** field — status is already tracked on the dedicated Status page.

## Context

The `attr_list` and `md_in_html` extensions required for grid cards were already enabled in `mkdocs.yml`. Only `pymdownx.emoji` needed to be added for icon rendering. Build verified clean with `mkdocs build`.
