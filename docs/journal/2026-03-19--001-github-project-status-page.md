# 001 — GitHub Project Status Page

**Date:** 2026-03-19
**Scope:** CI pipeline, docs site

## Summary

Added a build-time integration that fetches the "innitiative Status" field from the GitHub Projects v2 board (org project #2) and renders it as a Status page on the docs site. The script was created in a prior session; this session verified the build and switched the workflow token to `github.token`.

## What changed

| File | Change |
|------|--------|
| `scripts/fetch_project_status.py` | Created (prior session) — queries GitHub GraphQL API, writes `docs/status.md` with a markdown table of items and their initiative status. Falls back to a warning page if no token or API error. |
| `.github/workflows/deploy-docs.yml` | Added `projects: read` permission and a pre-build step to run the script. Changed token from `secrets.PROJECT_READ_TOKEN` to `github.token` since the org project is public. |
| `mkdocs.yml` | Added `Status: status.md` to the nav. |
| `.gitignore` | Added `docs/status.md` (generated file). |

### Design decisions

- **Stdlib only**: The script uses `urllib.request` — no new pip dependencies needed.
- **Graceful fallback**: If the token is missing or the API fails, the script writes a page with an admonition linking to the live project board and exits 0 so the build never breaks.
- **Default token**: The `github.token` with `projects: read` permission is sufficient for public org projects, avoiding the need for a separate PAT or repo secret.

## Context

The Status page gives visitors a quick view of initiative progress without leaving the docs site. The data is refreshed on every push to `main` via the existing deploy workflow. If >100 items are added to the project board, pagination will need to be added to the GraphQL query.
