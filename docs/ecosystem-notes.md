# OpenAudioTools Ecosystem Notes

Working document cataloging the open-source ecosystem used across the OpenAudioTools project.

---

## 1. Hardware & Design Tools

### KiCad (v9.0+)
- **What:** Open-source EDA suite for schematic capture, PCB layout, and routing.
- **Where used:** All PCB design — schematics, placement, routing, DRC, Gerber export.
- **Link:** <https://kicad.org>

### FreeRouting
- **What:** Standalone autorouter using Specctra DSN/SES interchange format.
- **Where used:** Complex multi-layer trace routing — export DSN from KiCad, autoroute in FreeRouting, import SES back.
- **Link:** <https://github.com/freerouting/freerouting>

### SKiDL
- **What:** Python library for creating KiCad netlists programmatically.
- **Where used:** Text-native netlist definition for each PCB board module before layout in KiCad.
- **Link:** <https://github.com/devbisme/skidl>

### KiCad MCP Servers (AI-assisted PCB workflow)
- **kicadmixelpixx/KiCAD-MCP-Server** — Component placement, DRC validation, zone operations, Gerber export (52 tools). <https://github.com/mixelpixx/KiCAD-MCP-Server>
- **Seeed-Studio/kicad-mcp-server** — Schematic analysis, netlist reading, pin tracing, design review. <https://github.com/Seeed-Studio/kicad-mcp-server>

### kicad-cli & pcbnew Python API
- **What:** KiCad command-line interface and Python scripting API.
- **Where used:** DRC validation, Gerber/drill export, programmatic placement scripts, DSN/SES import-export.

---

## 2. Firmware Platform

### Teensy 4.1 / Teensyduino / Arduino
- **What:** ARM Cortex-M7 @ 600 MHz microcontroller (PJRC) with Arduino-compatible framework.
- **Where used:** Main processor for all firmware — audio DSP, mixer control, SD recording, USB host, Ethernet, I2C codec control.
- **Link:** <https://www.pjrc.com/store/teensy41.html>

### DESPEE (ESP32-S3 Display Module)
- **What:** Standard display module for all Open Audio Tools devices. Custom PCB with ESP32-S3-WROOM-1-N16R8 + bare 4.3" 800×480 LCD. Runs a device-agnostic LVGL display engine — no device-specific knowledge on the module itself.
- **Where used:** Touchscreen UI across all devices. Teensy streams binary widget commands (COBS-encoded, CRC16) over UART. Touch events forwarded as coordinates.
- **Link:** <https://github.com/openaudiotools/despee>

### XMOS XU216-256-TQ128-C20
- **What:** Multi-core xCore processor for real-time USB audio.
- **Where used:** USB Audio Class 2 bridge on the Main Board — 24-in/8-out UAC2 + USB MIDI composite device.
- **Link:** <https://www.xmos.com>

---

## 3. Audio Libraries

### PJRC Audio Library
- **What:** Block-based audio DSP framework for Teensy (128 samples @ 48 kHz = 2.67 ms latency).
- **Where used:** Core audio processing — `AudioInputTDM`, `AudioOutputTDM`, `AudioMixer4`, and custom objects. Multi-data-line TDM receive requires SAI_RCR3 register modification.
- **Link:** <https://www.pjrc.com/teensy/td_libs_Audio.html>

### XMOS sw_usb_audio
- **What:** Open-source USB Audio Class 2 reference firmware for XMOS processors.
- **Where used:** XU216 firmware providing 24-in/8-out multichannel audio + MIDI forwarding. Includes Thesycon ASIO driver for Windows.
- **Link:** <https://github.com/xmos/sw_usb_audio>

### alex6679/teensy-4-usbAudio
- **What:** Community UAC2 implementation for Teensy 4.x.
- **Where used:** Legacy/fallback alternative to the XMOS bridge for cost-reduced builds. Up to 8 channels on macOS/Linux; Windows limited without a commercial driver.
- **Link:** <https://github.com/alex6679/teensy-4-usbAudio>

---

## 4. UI & Input Libraries

### LVGL (Light and Versatile Graphics Library)
- **What:** Embedded graphics library with widget toolkit and touch support.
- **Where used:** Display rendering on the DESPEE display module (ESP32-S3) — meters, channel strips, navigation.
- **Link:** <https://lvgl.io>

### Adafruit NeoPixel / FastLED
- **What:** Libraries for driving WS2812B addressable RGB LEDs.
- **Where used:** 16× NeoPixel LEDs (one per key switch), daisy-chained on a single data pin. Firmware defaults to 30 % brightness cap for noise/power mitigation.
- **Links:** <https://github.com/adafruit/Adafruit_NeoPixel> · <https://github.com/FastLED/FastLED>

### PJRC Encoder
- **What:** Quadrature decoding library for rotary encoders.
- **Where used:** 3× rotary encoders (NavX, NavY, Edit).
- **Link:** <https://www.pjrc.com/teensy/td_libs_Encoder.html>

### PJRC Bounce
- **What:** Debouncing library for mechanical switches.
- **Where used:** 16× CHOC key switches and other button inputs.
- **Link:** <https://www.pjrc.com/teensy/td_libs_Bounce.html>

---

## 5. Connectivity Libraries

### QNEthernet
- **What:** TCP/IP stack for the Teensy 4.1 built-in Ethernet PHY (DP83825I).
- **Where used:** Network audio streaming (RTP/AES67), mDNS/DNS-SD service discovery, PTP clock synchronization.
- **Link:** <https://github.com/ssilverman/QNEthernet>

### USBHost_t36
- **What:** USB host library for Teensy.
- **Where used:** MIDI controller connectivity via 2× USB-A host ports (through FE1.1s USB hub IC).
- **Link:** <https://github.com/PaulStoffregen/USBHost_t36>

### SdFat (Bill Greiman)
- **What:** SD card file I/O library with SDIO DMA support.
- **Where used:** 16-track interleaved WAV recording to SD card. Uses `createContiguous()` for pre-allocation to eliminate filesystem fragmentation. RF64 for files > 4 GB.
- **Link:** <https://github.com/greiman/SdFat>

---

## 6. Standards & Protocols

### USB Audio Class 2 (UAC2)
- **What:** Standard USB device class for multichannel, high-resolution audio.
- **Where used:** XMOS XU216 provides 24-in/8-out, 24-bit, 48 kHz, class-compliant audio. Native on macOS (Core Audio) and Linux (snd-usb-audio); Thesycon ASIO driver on Windows.

### USB Power Delivery (USB PD)
- **What:** USB PD 2.0/3.0 power negotiation standard.
- **Where used:** STUSB4500 breakout module on the power USB-C port. Configured for 5 V @ 5 A; falls back to 5 V @ 3 A via 5.1 kΩ CC resistors when PD is unavailable.

### TDM / I2S
- **What:** Serial audio bus protocols (Time Division Multiplexing / Inter-IC Sound).
- **Where used:** 2× SAI buses on Teensy 4.1 (SAI1 = TDM1, SAI2 = TDM2). 24.576 MHz BCLK, 48 kHz LRCLK, 24-bit, 16 slots per bus. Each bus connects 2× AK4619VN codecs via dual data lines (RX_DATA0 + RX_DATA1).

### AES67 / RTP
- **What:** Professional audio-over-IP standard; RTP carries audio payload over UDP.
- **Where used:** Network audio streaming — 48 kHz 24-bit PCM, 1 ms packet time (48 samples). RTP timestamps derived from PTP clock.

### PTP (IEEE 1588v2)
- **What:** Precision Time Protocol for clock synchronization across a network.
- **Where used:** Software-based implementation on Teensy's GPT timer (1 MHz). One mixer acts as PTP grandmaster; others as slaves. Accuracy: ~10–100 µs (sufficient for studio use with 1 ms packet times). Hardware PTP would require DP83640 PHY.

### mDNS / DNS-SD
- **What:** Zero-configuration networking for device discovery and service advertisement.
- **Where used:** Advertises MIDI services via `_midi2._udp.local` (DNS-SD) and audio streams via SAP/SDP (multicast to `239.255.255.255:9875`). Hostname format: `device-type-XXXX.local`. MIDI TXT records carry `UMPEndpointName` and `ProductInstanceId` per the Network MIDI 2.0 spec (M2-124-UM §4.4); audio stream metadata is expressed in SDP session descriptions.

### MIDI 2.0 / UMP
- **What:** Universal MIDI Packet protocol (successor to MIDI 1.0).
- **Where used:** USB MIDI via XMOS composite device (forwarded to/from Teensy via SPI0). Physical 3.5 mm TRS Type A jacks for MIDI IN (optoisolated) and MIDI OUT (31.25 kbaud current-loop). Network MIDI 2.0 over UDP planned for future versions.

### TRS Type A MIDI
- **What:** Standard 3.5 mm TRS wiring convention for MIDI (tip = current source/sink, ring = current return, sleeve = shield).
- **Where used:** MIDI IN and MIDI OUT jacks on the IO Board.

### BWF / RF64
- **What:** Broadcast Wave Format extension allowing WAV files > 4 GB.
- **Where used:** SD card recording — SdFat handles RF64 transparently. iXML or cue chunks carry channel naming for DAW import.

---

## 7. Licenses

| Scope | License | Notes |
|-------|---------|-------|
| **Firmware** | MIT | Teensy/Arduino source code |
| **Hardware** | CERN-OHL-P v2 | PCB designs and schematics; permissive variant allows commercial use without reciprocal disclosure. License text required on PCB silkscreen. |
| **Documentation** | CC BY 4.0 | All markdown, diagrams, and specifications. Attribution to Juliusz Fedyk / openaudiotools required. |

---

*Last updated: 2026-03-08*
