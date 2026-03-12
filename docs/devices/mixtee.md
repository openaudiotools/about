# MixTee

A digital audio mixer, recorder, and USB audio interface. Designed to be used with MIDI controllers. No built-in preamps.

## Overview

| Spec | Value |
|------|-------|
| Inputs | 16 (unbalanced 1/4" TRS) |
| Outputs | 8 (4 stereo pairs: Main, Aux1, Aux2, Aux3) |
| Headphone | 1× 1/4" TRS stereo |
| USB Audio | 24-in / 8-out (USB Audio Class 2 via XMOS XU216) |
| Recording | 16-track to SD card (WAV / RF64) |
| Ethernet | 100 Mbps (all channels available over network) |
| MIDI | 3.5 mm TRS Type A In/Out + USB MIDI via XMOS + 2× USB-A host |
| Display | 4.3" 800x480 touchscreen ([DESPEE](https://github.com/openaudiotools/despee) module) |
| Controls | 3 rotary encoders, 16 CHOC key switches with NeoPixel LEDs |
| Power | USB-C PD 5 V / 5 A (STUSB4500) |
| Dimensions | 260 × 100 × 50 mm |

## Hardware Platform

- **Teensy 4.1** — ARM Cortex-M7 @ 600 MHz, main processor for DSP, mixer logic, recording, and network.
- **XMOS XU216-256-TQ128-C20** — USB Audio Class 2 bridge (24-in/8-out + USB MIDI composite). Firmware: [xmos/sw_usb_audio](https://github.com/xmos/sw_usb_audio). Thesycon ASIO driver for Windows.
- **[DESPEE](https://github.com/openaudiotools/despee) display module** — Runs LVGL UI; receives meter data + parameter state from Teensy over UART at 30 Hz.
- **4× AK4619VN codecs** — 4-in/4-out each, arranged as 2 per TDM bus (SAI1 + SAI2). U1/U2 full ADC+DAC, U3/U4 ADC-only.

## Audio Architecture

- PJRC Audio Library — block-based DSP, 128 samples @ 48 kHz (2.67 ms latency).
- 2× TDM buses: 24.576 MHz BCLK, 48 kHz LRCLK, 24-bit, 16 slots per bus, dual data lines (RX_DATA0 + RX_DATA1).
- Galvanic isolation between digital and analog domains: Si8662BB (TDM), ISO1541 (I2C), MEJ2S0505SC (power).
- Pop suppression via TS5A3159 analog mute switches on all output pairs.

## Key ICs

| IC | Function |
|----|----------|
| AK4619VN (×4) | Audio codecs |
| Si8662BB (×2) | TDM digital isolators |
| ISO1541 (×2) | I2C isolators |
| MEJ2S0505SC (×2) | Isolated DC-DC converters |
| MCP23017 | Key matrix scanner (I2C GPIO expander) |
| MCP23008 | Mute control, codec PDN, headphone detect |
| TCA9548A | I2C bus multiplexer |
| FE1.1s | USB 2.0 host hub (2 downstream ports) |
| TPS2051 (×2) | USB per-port current limiters |
| STUSB4500 | USB PD sink controller |
| DP83825I | Ethernet PHY (on Teensy 4.1) |
| OPA1678 | Input/output op-amps |
| TPA6132 / MAX97220 | Headphone amplifier |

## Firmware Libraries

| Library | Purpose |
|---------|---------|
| PJRC Audio Library | Block-based audio DSP |
| PJRC Encoder | Rotary encoder decoding |
| PJRC Bounce | Switch debouncing |
| Adafruit NeoPixel / FastLED | WS2812B LED control |
| QNEthernet | TCP/IP, mDNS, PTP |
| USBHost_t36 | USB MIDI host |
| SdFat | SD card recording (SDIO DMA, RF64) |
| LVGL (on ESP32-S3) | Touchscreen UI rendering |

## Network Role

- Network role: `mixer`
- Acts as PTP grandmaster by default.
- Publishes `_jfa-audio._udp` streams (RX inputs + TX buses/mains/auxes).
- Publishes `_jfa-midi2._udp` endpoint for full MIDI control.
- Optional HTTP server at `http://mixer-XXXX.local/` for web UI.
- Hostname: `mixer-XXXX.local`

## PCB Boards

The MixTee uses a modular multi-board design connected via FFC (1.0 mm pitch) and JST-PH harnesses:

- **Main Board** — Teensy 4.1, XMOS XU216, TCA9548A, power management, FFC connectors to Input Mother Boards.
- **Input Mother Board (×2)** — 2× AK4619VN codecs each, analog front-end (OPA1678), isolation boundary.
- **IO Board** — FE1.1s USB hub, 2× USB-A, RJ45 MagJack, MIDI TRS jacks.
- **Key PCB** — 16× CHOC sockets, MCP23017, WS2812B NeoPixels.
- **HP Board** — Headphone amplifier (TPA6132 / MAX97220 breakout).
- **Power Board** — STUSB4500 USB PD breakout, USB-C connector.

## Connectivity Examples

- **USB mode** — Audio routed via USB in/out to a computer, MIDI connections to controllers and synths.
- **Ethernet direct** — Audio transported over Ethernet to a computer, with separate MIDI connections.
- **Ethernet switch** — Audio and MIDI both carried over Ethernet using a network switch, single-cable setup.

See [Networking](../networking.md) for protocol details and [Ecosystem Notes](../ecosystem-notes.md) for the full technology stack.

## License

| Scope | License |
|-------|---------|
| Firmware | MIT |
| Hardware | CERN-OHL-P v2 |
| Documentation | CC BY 4.0 |
