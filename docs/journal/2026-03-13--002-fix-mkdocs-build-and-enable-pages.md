# Fix MkDocs build and enable GitHub Pages

**Date:** 2026-03-13

## Summary

The initial MkDocs deployment (entry 001) failed for two reasons. Both were resolved in this session.

### Issue 1: `docs_dir` cannot be the repo root

MkDocs does not allow `docs_dir` to be the same directory as `mkdocs.yml`. The build errored with:

> The 'docs_dir' should not be the parent directory of the config file.

**Fix:** Moved all documentation content (markdown files, `devices/`, `images/`, `journal/`) into a `docs/` subdirectory and changed `mkdocs.yml` to `docs_dir: docs`. This also eliminated the need for the `exclude_docs` block.

### Issue 2: GitHub Pages not enabled on the repository

The build job succeeded but the deploy job returned a 404:

> Failed to create deployment … Ensure GitHub Pages has been enabled.

**Fix:** Enabled GitHub Pages via the GitHub API with `build_type: workflow`, then re-triggered the workflow. Deploy succeeded and the site is live at https://openaudiotools.github.io/about/.
