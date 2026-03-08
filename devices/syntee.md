# SynTee

A standalone virtual sound module / synthesizer with basic controls.

## Overview

| Port | Description |
|------|-------------|
| LR In | Stereo audio input |
| LR Out | Stereo audio output |
| MIDI In | MIDI input |
| MIDI Out | MIDI output |
| ETH | Ethernet |
| Power | USB power |

## Purpose

The SynTee is a self-contained synthesizer module that can operate standalone or as part of a networked OpenAudioTools setup. It receives MIDI and produces audio, with Ethernet connectivity for network audio streaming and MIDI.

## Network Role

- Network role: `synth`
- Publishes 1–N `_jfa-audio._udp` TX streams (main/aux outputs).
- Publishes one `_jfa-midi2._udp` endpoint (`dir=inout`, `ep=synth`).
- Optionally browses for controller `_jfa-midi2._udp` services for auto-pairing.
- Hostname: `synth-XXXX.local`

## Hardware Platform

- **Teensy 4.1** — ARM Cortex-M7 @ 600 MHz with native 100 Mbps Ethernet (DP83825I PHY).
- Audio-capable device: participates in PTP clock synchronization as a slave.

## Integration

- Connects to [MixTee](mixtee.md) inputs via audio cables or over Ethernet.
- Can receive MIDI from [HubTee](hubtee.md), USB controllers, or network MIDI 2.0.
- [VoiceTee](voicetee.md) or [StringTee](stringtee.md) preamp modules can feed into SynTee's stereo input.
- See [Networking](../networking.md) for protocol details.

## License

| Scope | License |
|-------|---------|
| Firmware | MIT |
| Hardware | CERN-OHL-P v2 |
| Documentation | CC BY 4.0 |
