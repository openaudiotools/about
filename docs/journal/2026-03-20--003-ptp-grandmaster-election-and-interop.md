# 003 — PTP grandmaster election and interop

**Date:** 2026-03-20
**Scope:** `docs/networking.md`

## Summary

Rewrote the PTP clock synchronisation section in `docs/networking.md` to document the Best Master Clock Algorithm (BMCA) for grandmaster election, per-device `priority1` values, and interoperability with third-party AES67/Dante/Ravenna gear and DAW computers.

## What changed

| Location | Change |
|----------|--------|
| PTP section (lines 93–101) | Replaced brief bullet list with full BMCA explanation, priority table, tie-breaking rules, and a new **Interoperability** subsection |
| MixTEE device role (line 150) | Changed "Acts as PTP grandmaster" → "Default PTP grandmaster (`priority1=128`)" |
| Topology example (line 215) | Changed "The MixTee is PTP grandmaster" → "The MixTee wins PTP grandmaster election by priority" |

### Priority table added

| Priority | Device | Rationale |
|----------|--------|-----------|
| 128 | MixTEE | Receives and mixes multiple streams — natural clock anchor |
| 144 | HubTEE | Bridges audio and MIDI — good fallback |
| 160 | SynTEE | Single-output source — least preferred |

### Interoperability scenarios documented

- Third-party AES67 devices participate in the same BMCA election; a dedicated PTP grandmaster clock wins naturally.
- USB-connected computers are bridged by the OAT device (no PTP participation).
- Ethernet-connected computers with AES67 software drivers join BMCA as regular participants.

## Context

The previous PTP section stated "by default the MixTEE" was grandmaster but did not explain what happens on networks without a MixTEE or how OAT devices coexist with third-party gear. This was a gap given the project's open-standards principle. Using standard IEEE 1588 BMCA with `priority1` values makes OAT devices interoperable with any PTP-capable device on the LAN without custom negotiation logic.
