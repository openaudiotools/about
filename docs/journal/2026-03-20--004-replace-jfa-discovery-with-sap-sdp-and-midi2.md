# 004 — Replace _jfa- discovery with SAP/SDP and _midi2._udp

**Date:** 2026-03-20
**Scope:** `docs/networking.md`, `docs/devices/hubtee.md`, `docs/ecosystem-notes.md`

## Summary

Replaced the custom `_jfa-` DNS-SD service types with standard protocols: SAP/SDP (RFC 2974/4566) for audio stream discovery and `_midi2._udp` (MMA Network MIDI 2.0) for MIDI endpoint discovery. Added user-settable device names so users can distinguish multiple devices of the same type.

## What changed

| File | Changes |
|------|---------|
| `docs/networking.md` | Rewrote discovery section: audio now uses SAP/SDP with full SDP blob example and field table; MIDI uses standard `_midi2._udp` service type. Added "User-settable device name" subsection. Added `name` TXT field to MIDI DNS-SD. Updated Patchbay, Security, and Resource budget sections. |
| `docs/devices/hubtee.md` | Replaced all `_jfa-audio._udp` references with SAP/SDP, all `_jfa-midi2._udp` with `_midi2._udp`. |
| `docs/ecosystem-notes.md` | Updated mDNS/DNS-SD entry to reflect SAP/SDP for audio and `_midi2._udp.local` for MIDI. |

### Key decisions

- **Audio discovery via SAP/SDP** — Standard AES67 mechanism. Any AES67 receiver (Dante, Ravenna, software drivers) can discover OAT audio streams and vice versa. Audio stream metadata (model, channels, sample rate, format, packet time) is expressed in SDP attributes (`c=`, `m=`, `a=` lines) instead of DNS-SD TXT fields.
- **MIDI discovery via `_midi2._udp`** — The standard service type from MMA's Network MIDI 2.0 spec (M2-124-UM), not an OAT-specific prefix. Initially planned as `_oat-midi2._udp`, but research confirmed `_midi2._udp` is the ratified standard.
- **No separate device discovery service** — SAP/SDP `s=` line carries device name for audio; `_midi2._udp` TXT `name` field carries it for MIDI. No need for a dedicated `_oat-device._udp` type.
- **User-settable device name** — Appears in SDP `s=` line (e.g. `s=Bass Synth — Out 1-2`) and as DNS-SD instance name + `name` TXT field for MIDI. mDNS hostname stays stable (`syntee-a3f2.local`).

## Context

The `_jfa-` prefix isolated OAT devices from the AES67 ecosystem — other AES67 devices couldn't discover OAT audio streams. Moving to SAP/SDP and `_midi2._udp` makes OAT fully interoperable with standard audio-over-IP and Network MIDI 2.0 devices out of the box.

The syntee/ and mixtee/ repos still have `_jfa-` references (10+ files) — those are out of scope for this change but already document SAP/SDP for audio internally.
