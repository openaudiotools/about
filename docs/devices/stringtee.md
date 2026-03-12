# StringTee

A small guitar/instrument preamp module that connects to [MixTee](mixtee.md) or [SynTee](syntee.md) inputs.

## Overview

| Feature | Detail |
|---------|--------|
| Input | 1/4" TS high-impedance (instrument level) |
| Signal path | Fully analogue |
| Power | USB |
| Controls | 1× gain pot |
| Output | Connects via double TR 1/4" coupler |

## Purpose

The StringTee is an accessory device that adds guitar/instrument connectivity to devices that lack built-in preamps (MixTee, SynTee). It provides impedance matching and gain control for instrument-level signals.

## Design Philosophy

Follows the OpenAudioTools "modular" principle — specific-purpose functionality (instrument preamps) is kept as a separate, interchangeable device compatible with other gear. No digital processing; the signal path is entirely analogue.

## Integration

- Plugs directly into a [MixTee](mixtee.md) or [SynTee](syntee.md) 1/4" TRS input via a double TR coupler.
- USB powered — uses the same unified USB power approach as the rest of the ecosystem.

## License

| Scope | License |
|-------|---------|
| Hardware | CERN-OHL-P v2 |
| Documentation | CC BY 4.0 |
