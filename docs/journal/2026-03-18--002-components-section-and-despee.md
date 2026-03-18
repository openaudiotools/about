# 002 — Components section and DESPee

**Date:** 2026-03-18
**Scope:** docs/components, naming decisions

## Summary

Refined the components section: updated the intro to clarify components are reusable across designs (not standalone), added an accurate description for DESPee based on its repo, and settled on the "DESPee" capitalization.

## What changed

| File | Change |
|------|--------|
| `docs/components/index.md` | Updated intro text, renamed DesPee → DESPee, replaced incorrect "de-esser" description with accurate ESP32-S3 display board summary, changed status from Concept to Pre-prototype |

### Naming decision

Considered three capitalizations: DesPee, dESPee, DESPee. Settled on **DESPee** — highlights the ESP in the name while remaining readable.

### DESPee description

DESPee is an ESP32-S3 display board with a 4.3" 800×480 capacitive touch LCD and 3 rotary encoders. Connects to any host MCU via a 6-pin UART link and renders widgets using LVGL. Repo: `openaudiotools/despee`.

## Context

The initial DESPee description was a placeholder guess ("de-esser audio processor") that was incorrect. The actual component is a display controller board. Description now sourced from the DESPee repo README. See also [entry 001](2026-03-18--001-docs-site-restructure-and-branding.md) for the broader restructure that created the components section.
