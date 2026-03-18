# 001 — Devices overview page and repo link migration

**Date:** 2026-03-15
**Scope:** docs/devices, mkdocs.yml, docs/networking.md

## Summary

Created a single devices overview page and removed the MixTee and SynTee spec pages, since both devices now have their own GitHub repositories. Cross-references throughout the docs were updated to point to the repos instead of deleted local files.

## What changed

| File | Change |
|------|--------|
| `docs/devices/index.md` | Created — overview table listing all five devices with descriptions and links |
| `docs/devices/mixtee.md` | Deleted — specs now live in [openaudiotools/mixtee](https://github.com/openaudiotools/mixtee) |
| `docs/devices/syntee.md` | Deleted — specs now live in [openaudiotools/syntee](https://github.com/openaudiotools/syntee) |
| `docs/devices/hubtee.md` | Updated MixTee/SynTee links to GitHub repos |
| `docs/devices/voicetee.md` | Updated MixTee/SynTee links to GitHub repos |
| `docs/devices/stringtee.md` | Updated MixTee/SynTee links to GitHub repos |
| `docs/networking.md` | Updated MixTee/SynTee links to GitHub repos |
| `mkdocs.yml` | Replaced per-device nav with Overview + three concept pages (HubTee, VoiceTee, StringTee) |

## Context

MixTee and SynTee graduated to standalone repositories. Keeping duplicate spec pages in the about repo would drift out of sync. HubTee, VoiceTee, and StringTee remain concept-stage and stay as local pages.
