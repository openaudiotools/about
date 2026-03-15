# VoiceTee

A small microphone preamp module that connects to [MixTee](https://github.com/openaudiotools/mixtee) or [SynTee](https://github.com/openaudiotools/syntee) inputs.

## Overview

| Feature | Detail |
|---------|--------|
| Input | ADS combo (XLR + 1/4" TRS) with phantom power |
| Signal path | Fully analogue |
| Power | USB |
| Controls | 2× gain pots, 1× phantom power switch |
| Output | Connects via double TR 1/4" coupler |

## Purpose

The VoiceTee is an accessory device that adds microphone connectivity to devices that lack built-in preamps (MixTee, SynTee). It provides phantom power and gain control in a small, self-contained module.

## Design Philosophy

Follows the OpenAudioTools "modular" principle — specific-purpose functionality (mic preamps) is kept as a separate, interchangeable device compatible with other gear. No digital processing; the signal path is entirely analogue.

## Integration

- Plugs directly into a [MixTee](https://github.com/openaudiotools/mixtee) or [SynTee](https://github.com/openaudiotools/syntee) 1/4" TRS input via a double TR coupler.
- USB powered — uses the same unified USB power approach as the rest of the ecosystem.

## License

| Scope | License |
|-------|---------|
| Hardware | CERN-OHL-P v2 |
| Documentation | CC BY 4.0 |
