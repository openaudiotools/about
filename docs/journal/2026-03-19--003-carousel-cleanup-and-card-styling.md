# 003 — Carousel cleanup and card styling

**Date:** 2026-03-19
**Scope:** `docs/stylesheets/extra.css`, `docs/README.md`

## Summary

Removed the carousel navigation dots entirely after animation-pause-on-hover could not be reliably fixed across browsers, then restyled the carousel cards with inverted theme colors and a shadow for visual depth.

## What changed

| File | Change |
|------|--------|
| `docs/stylesheets/extra.css` | Removed all `.carousel-dots` rules, dot keyframes (`carousel-dot1/2/3`), dot hover/focus pause rules, and reduced-motion dot hiding |
| `docs/stylesheets/extra.css` | Added inverted color scheme to `.carousel-card`: dark navy background (`--md-primary-fg-color`), light text (`--md-primary-bg-color`), and `box-shadow: 0 4px 12px rgba(0,0,0,0.3)` |
| `docs/stylesheets/extra.css` | Updated `.carousel-btn` to use light border/text with inverted hover (cream background, navy text) |
| `docs/README.md` | Removed the `.carousel-dots` div and its three `<span>` elements |

### Dot removal rationale

The dot animations used the `animation` shorthand, which implicitly set `animation-play-state: running` and competed with the hover rule's longhand `animation-play-state: paused`. An initial fix converting to longhand properties was attempted but the dots were ultimately removed as unnecessary UI.

## Context

The carousel is a pure-CSS auto-rotating component on the landing page. With the dots removed, the only animation is the card track scroll, which pauses cleanly on hover via a single rule targeting `.carousel-track`. The inverted card colors adapt automatically to light/dark theme since they reference CSS custom properties.
