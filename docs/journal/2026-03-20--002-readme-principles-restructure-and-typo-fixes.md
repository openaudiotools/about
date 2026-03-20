# 002 — README principles restructure and typo fixes

**Date:** 2026-03-20
**Scope:** `docs/README.md`

## Summary

Restructured the README principles section from a simple three-pillar layout into a 3×3 Material grid cards matrix (Open/Robust/Essential × Hardware/Software/Connectivity), added a "Firstly: OPEN" emphasis section, consolidated hardware/firmware/connectivity details into subsections, simplified the devices listing to link to dedicated pages, and fixed typos throughout.

## What changed

| Area | Change |
|------|--------|
| Principles section | Replaced flat "Core Principles" with a 3×3 grid card layout using Material icons |
| "Firstly: OPEN" | Added new section emphasizing open-source ecosystem as the top priority |
| Hardware/Firmware/Connectivity | Consolidated into "Notes" subsections (Standardized Hardware, Robust Hardware, Essential Firmware, Open Connectivity) |
| Devices section | Replaced individual device listings with links to `devices/` and `components/` pages |
| Typos fixed | `Principals` → `Principles`, `utily` → `utility`, `Preffer` → `Prefer`, `firmare` → `firmware`, `Standarized` → `Standardized` (×2), `swappble` → `swappable`, `functiond` → `functions` |

## Context

The README serves as the landing page for the MkDocs site at openaudiotools.com. The restructure gives a more visual, scannable overview of the project's design philosophy using Material for MkDocs grid cards. Device details now live on their own pages, keeping the homepage focused on principles and identity.
