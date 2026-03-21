# 002 — Add PHONEE component to docs

**Date:** 2026-03-21
**Scope:** docs/components, GitHub project

## Summary

Added PHONEE (reusable headphone output module) to the components documentation and created a tracking issue on the GitHub project board, mirroring the existing DESPee component pattern.

## What changed

| Item | Detail |
|------|--------|
| `docs/components/index.md` | Added PHONEE section with description, status, repo link, and issue link |
| GitHub issue #15 | Created on `openaudiotools/about`, modeled after DESPEE issue (#3) |
| GitHub project board #2 | Added issue #15 to the org project |

### PHONEE overview

- TPA6132A2 ground-referenced stereo headphone amp on a ~30×20mm 2-layer PCB
- PCB-mount 10k log volume pot + 1/4" TRS jack with detect switch
- 4-pin JST-PH input (Audio L, Audio R, VCC, GND)
- Currently used in MIXTEE; designed to be device-agnostic
- Repo: `openaudiotools/phonee`

## Context

PHONEE is the second reusable component (after DESPee) in the OpenAudioTools ecosystem. The `phonee` repo already contains full documentation (architecture, connections, integration guide). The about repo entry serves as the central index pointer, following the same pattern established by DESPee.
