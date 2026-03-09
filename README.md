# Open Audio Tools

Open Audio Tools is an open-source hardware and software platform for music, hardware, and software creators around the world. Designed to be easily produced and self-built.

## The "WHY"

OpenAudioTools is an open-source hardware and software platform for building music tools that are simple, robust, and truly open — free for anyone to build, manufacture, and extend. Born out of frustration with DIY gear that is either too experimental, too niche, too expensive, or too fragile to maintain, it takes a different approach: one focused device, one job done well, built on open standards, designed to work with the controllers you already own. [read more...](rationale.md)

## Core Principles

The project is built on three pillars:

### Open Hardware

- Easy to source components
- Affordable
- Only the essentials
- Easy to modify

### Open Software

- Simple
- Modular
- Extendable

### Open Connectivity

- Open, non-proprietary formats
- Fewer cables
- No proprietary connectors

## Hardware

Hardware should be **open**, **essential**, **standardized**, and **modular**.

### Open

All designs allow for easy modifications and adaptations.

### Essential

Each device focuses on one function and does it well. No frills, reasonable cost.

### Standardized

- **Teensy** microcontrollers for a consistent development environment
- **USB** for power (unified power adapters)
- **TRS 1/8" Type A** for MIDI
- **Ethernet** for system integration
- **USB-A MIDI Host** when possible

### Modular

A motherboard approach:

- Often-used components (keys, encoders) are placed on standardized breakout boards for reuse across devices.
- Specific-purpose functionality (mic preamps, effects) is added as separate, interchangeable devices compatible with other gear.

## Firmware

- **Open** — Easy to extend, modify, and adapt
- **Essential** — Provides the main function very well
- **Standardized** — Teensy provides a unified architecture and common language

## Connectivity

Only open, non-proprietary standards. The essential signals are **audio** and **MIDI**, carried over cables only.

### Ethernet ([details](networking.md))

MIDI and audio are intended to be available over Ethernet:

- Single cable for audio and MIDI
- Low latency
- Cheap hubs and switches
- Easy internet connectivity
- Most boards already include Ethernet support

## Devices

### [SynTee](devices/syntee.md)

A standalone sound module with basic controls.

| Port | Description |
|------|-------------|
| LR In | Stereo audio input |
| LR Out | Stereo audio output |
| MIDI In | MIDI input |
| MIDI Out | MIDI output |
| ETH | Ethernet |
| Power | USB power |

### [HubTee](devices/hubtee.md)

A USB / MIDI / Ethernet hub with clock.

| Port | Quantity |
|------|----------|
| USB MIDI Host | 4 |
| PC ETH | 1 |
| ETH Connector | 8 |
| MIDI In | 2 |
| MIDI Out | 2 |

### [MixTee](devices/mixtee.md)

A digital audio mixer, recorder, and interface. Designed to be used with MIDI controllers. No built-in preamps.

- 16 inputs, 8 outputs (4 stereo)
- All channels available over Ethernet

### [VoiceTee](devices/voicetee.md)

A small mic preamp module that connects to MixTee or SynTee inputs.

- ADS combo inputs with phantom power
- USB powered, fully analogue signal path
- 2 pots for gain control, 1 switch for phantom power
- Connects via double TR 1/4" coupler

### [StringTee](devices/stringtee.md)

A small guitar/instrument preamp module that connects to MixTee or SynTee inputs.

- 1/4" TS high-impedance input (instrument level)
- USB powered, fully analogue signal path
- 1 pot for gain control
- Connects via double TR 1/4" coupler

## Ecosystem

See [Ecosystem Notes](ecosystem-notes.md) for a full catalog of the open-source hardware, firmware, and software used across the project.

