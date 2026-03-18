# 001 — Docs site restructure and branding

**Date:** 2026-03-18
**Scope:** mkdocs config, devices/components pages, site theming

## Summary

Restructured the devices section, added a new components section for DesPee, added the OAT logo to the site header and landing page, and applied a custom color palette replacing the default Material theme colors.

## What changed

| File | Change |
|------|--------|
| `mkdocs.yml` | Collapsed Devices nav to single link, added Components nav entry, added logo/favicon, added `extra_css`, replaced built-in palette colors with custom CSS |
| `docs/devices/index.md` | Rewrote as a single page with sections per device — repo links for MixTee/SynTee, detail page links for concept devices, issue links for all |
| `docs/components/index.md` | New section for standalone components; DesPee listed with repo and issue links |
| `docs/components/despee.md` | Created then removed — DesPee has its own repo so no separate detail page needed |
| `docs/README.md` | Added centered OAT logo at top of landing page |
| `docs/stylesheets/extra.css` | New custom CSS overriding Material theme colors with project palette |
| `docs/images/logos/` | User added logo variants (oatlogo1a, 1b, 1c in multiple sizes) |

### Color palette applied

| Role | Color | Hex |
|------|-------|-----|
| Primary (header, nav) | Oxford Navy | `#1d3557` |
| Primary light | Cerulean | `#457b9d` |
| Accent (links, hover) | Punch Red | `#e63946` |
| Background (light mode) | Honeydew | `#f1faee` |
| Frosted Blue | Reserved | `#a8dadc` |

### Devices/Components restructure decisions

- Side menu links to `devices/index.md` as a whole — MkDocs nav does not support anchor links to sections within a page.
- Devices with their own repos (MixTee, SynTee) get inline descriptions + repo link; no separate detail page.
- Concept devices (HubTee, VoiceTee, StringTee) keep their own detail pages.
- DesPee categorized as a "component" rather than a "device" — has its own repo at `openaudiotools/despee`.
- Issue links added from the org-level GitHub Project #2 ("Open Audio Tools").

## Context

This is the first visual identity pass on the MkDocs site, aligning it with the OAT logo palette. The devices/components split clarifies the distinction between full devices and modular components like DesPee.
