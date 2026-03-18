# 006 — Cross-linking and nav updates

**Date:** 2026-03-18
**Scope:** Documentation, navigation, cross-linking

## Summary

Added discussion links to all device and component pages, added external nav links (AI Journal, Discussions, Project board) to `mkdocs.yml`, and filled in the missing HubTee issue link on the devices page.

## What changed

| File | Change |
|------|--------|
| `mkdocs.yml` | Added nav entries: AI Journal (GitHub journal dir), Discussions, Project board |
| `docs/devices/index.md` | Added Discussion links for MixTee, SynTee, HubTee, VoiceTee, StringTee; added missing Issue link for HubTee |
| `docs/components/index.md` | Added Discussion link for DESPEE |

### Nav additions

| Nav item | Target |
|----------|--------|
| AI Journal | `https://github.com/openaudiotools/about/tree/main/docs/journal` |
| Discussions | `https://github.com/openaudiotools/about/discussions` |
| Project | `https://github.com/orgs/openaudiotools/projects/2` |

## Context

Completes the cross-linking between the docs site, GitHub Discussions (entry 004), and the project board (entry 003). Every device now links to its issue, discussion category, and repository (where applicable) from both the docs site and GitHub.
