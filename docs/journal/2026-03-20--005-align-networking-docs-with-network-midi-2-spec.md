# 005 — Align networking docs with Network MIDI 2.0 spec

**Date:** 2026-03-20
**Scope:** `docs/networking.md`, `docs/ecosystem-notes.md`

## Summary

Aligned networking documentation with the MMA Network MIDI 2.0 specification (M2-124-UM v1.0.1). The previous entry (004) introduced `_midi2._udp` DNS-SD but used invented TXT record keys and a vague session description. This entry corrects those against the actual 56-page spec.

## What changed

| File | Change |
|------|--------|
| `docs/networking.md` | Replaced 5 custom TXT keys (`name`, `dir`, `ump`, `model`, `ch`) with spec-correct `UMPEndpointName` + `ProductInstanceId` (§4.4, Table 6) |
| `docs/networking.md` | Clarified Service Instance Name is an internal identifier; `UMPEndpointName` is the canonical display name (§4.2) |
| `docs/networking.md` | Added Host/Client model subsection (§2.1-2.2) — OAT devices act as Hosts when exposing endpoints, Clients when connecting |
| `docs/networking.md` | Added packet format subsection — `0x4D494449` signature, 16-bit sequence numbers, FEC |
| `docs/networking.md` | Replaced vague "handshake" session description with accurate Invitation → Accepted → UMP Data → Bye lifecycle (§6) |
| `docs/networking.md` | Security section now acknowledges optional SHA-256 session authentication (§6.7-6.10) instead of blanket "no authentication" |
| `docs/networking.md` | Device roles: removed custom TXT key references (`dir=inout`, `model=syntee`), replaced with "Host, bidirectional" |
| `docs/ecosystem-notes.md` | Fixed mDNS/DNS-SD entry: TXT records carry `UMPEndpointName` and `ProductInstanceId`, not "role, direction, channel count" |
| `.gitignore` | Added `.tmp/` |

## Context

Entry 004 established the DNS-SD + SAP/SDP discovery split but predated access to the actual M2-124-UM spec. Several details were guessed or simplified. Now that the spec is available, the docs match it section-by-section. OAT-specific metadata (direction, model, channels) moves to UMP MIDI-CI Property Exchange after session establishment, keeping DNS-SD records spec-compliant and interoperable with any Network MIDI 2.0 device.

Key spec sections referenced: §2.1-2.2 (Host/Client), §4.2 (Service Instance Name), §4.4 (TXT records), §5.2 (packet signature), §5.6 (sequence numbers), §6 (session lifecycle), §6.7-6.10 (authentication), §7.2.2 (FEC), §9 (dual role).
