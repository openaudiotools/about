# MkDocs + GitHub Pages setup

**Date:** 2026-03-13

## Summary

Four uncommitted changes add a MkDocs-based documentation site with automatic GitHub Pages deployment:

| Change | Description |
|--------|-------------|
| `.gitignore` (modified) | Added `site/` to ignore the MkDocs build output directory. |
| `mkdocs.yml` (new) | MkDocs Material configuration. Sets up site navigation (Overview, Rationale, five device pages, Networking, Ecosystem Notes), deep-purple/amber theme with dark-mode toggle, search, and common Markdown extensions. Docs are served from the repo root (`docs_dir: .`) with internal files excluded. |
| `requirements.txt` (new) | Pins `mkdocs >=1.6,<2` and `mkdocs-material >=9.5,<10`. |
| `.github/workflows/deploy-docs.yml` (new) | GitHub Actions workflow that builds and deploys to GitHub Pages on every push to `main` (or manual dispatch). Uses Python 3.12, `mkdocs build --strict`, and the `deploy-pages` action. |

## Notes

- The `journal/` directory itself is also untracked and will need to be committed alongside these changes (or excluded).
- None of these changes have been staged or committed yet.
