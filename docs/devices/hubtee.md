# HubTee

A USB / MIDI / Ethernet hub with clock. Central routing and connectivity hub for the OpenAudioTools ecosystem.

## Overview

| Port | Quantity |
|------|----------|
| USB MIDI Host | 4 |
| PC Ethernet | 1 |
| Ethernet Connector | 8 |
| MIDI In | 2 |
| MIDI Out | 2 |

## Purpose

The HubTee serves as the central nervous system of an OpenAudioTools studio setup:

- **MIDI routing** — Bridges USB MIDI devices, DIN/TRS MIDI, and Network MIDI 2.0 (UMP over UDP). 4× USB-A host ports for MIDI controllers.
- **Ethernet hub** — 8× Ethernet connectors allow star or daisy-chain topology for connecting multiple devices (SynTees, MixTees, computers).
- **Clock distribution** — Can act as PTP grandmaster (IEEE 1588v2) for synchronizing audio clocks across all networked devices.
- **Audio bridging** — Subscribes to audio streams from synths/mixers and can publish its own `_jfa-audio._udp` streams.

## Network Role

- Network role: `hub`
- Publishes `_jfa-midi2._udp` endpoints for bridging Network MIDI 2.0 to DIN/USB MIDI.
- Publishes `_jfa-audio._udp` TX if it exposes its own audio stream(s).
- Can run the **Patchbay "brain"** — periodically browses `_jfa-audio._udp` and `_jfa-midi2._udp`, builds an in-RAM device/port graph, and exposes a web UI or OSC/JSON API for managing routes.
- Hostname: `hub-XXXX.local` (or similar pattern)

## Hardware Platform

- **Teensy 4.1** — ARM Cortex-M7 @ 600 MHz with native 100 Mbps Ethernet (DP83825I PHY).
- Same UDP/IP network stack as other audio-capable devices (QNEthernet).

## Connectivity Example

Multiple devices ([SynTees](syntee.md), computers, [MixTees](mixtee.md)) connected through the HubTee via Ethernet and MIDI, creating a centralized studio network.

See [Networking](../networking.md) for protocol details and [Ecosystem Notes](../ecosystem-notes.md) for the full technology stack.

## License

| Scope | License |
|-------|---------|
| Firmware | MIT |
| Hardware | CERN-OHL-P v2 |
| Documentation | CC BY 4.0 |
