<div align="center">
  <img src="images/logos/dark_oatlogo1c_transparent_tight.png" alt="Open Audio Tools" width="300" class="logo-dark">
</div>

# Open Audio Tools

Open Audio Tools is an open-source hardware and software platform for music, hardware, and software creators around the world. Designed to be easily produced and self-built.

<div class="carousel">
  <div class="carousel-track">
    <div class="carousel-card">
      <h3>SynTee</h3>
      <p>Standalone virtual sound module and synthesizer — built around the Teensy platform with multi-voice polyphony, real-time effects, and full MIDI control</p>
      <a class="carousel-btn" href="https://github.com/openaudiotools/syntee">View on GitHub →</a>
    </div>
    <div class="carousel-card">
      <h3>MixTee</h3>
      <p>Digital audio mixer, recorder, and USB audio interface — 16 inputs, 8 outputs, designed to be driven by MIDI controllers with all channels available over Ethernet</p>
      <a class="carousel-btn" href="https://github.com/openaudiotools/mixtee">View on GitHub →</a>
    </div>
    <div class="carousel-card">
      <h3>DESPEE</h3>
      <p>ESP32-S3 display board with touch LCD and rotary encoders — offloads the user interface from the audio controller so each device stays focused on its core task</p>
      <a class="carousel-btn" href="https://github.com/openaudiotools/despee">View on GitHub →</a>
    </div>
  </div>
</div>

## The "WHY"

OpenAudioTools is an open-source hardware and software platform for building music tools that are simple, robust, and truly open — free for anyone to build, manufacture, and extend. Born out of need for robust, non experimental and open diy gear. Focused devices, one job done well, built on open standards, designed to work with the controllers you already own. [read more...](rationale.md)

## Firstly: OPEN

The project is first and foremost about creating an open source ecosystem.

## Principles

We're building on the following principles:

<div class="grid cards grid-3" markdown>

- #### OPEN

    - Freely available and open to modification.

- #### ROBUST

    - Providing solid utility while being easy to maintain and durable.

- #### ESSENTIAL

    - Focuses on a single thing and does it well

</div>

### How it applies:

<div class="grid cards grid-3" markdown>

- :material-chip: __Open Hardware__

    - Easy to source parts
    - Only the essentials
    - Easy to modify and recombine
    - Dedicated, swappable components

- :material-chip: __Robust Hardware__

    - Easy to build and repair
    - Common components on separate boards
    - Plug and play
    - Quality audio signal
    - Easy firmware load / update

- :material-chip: __Essential Hardware__

    - One main role per device or component
    - Focus on Utility
    - Repurpose by firmware swap
    - Rely on midi controllers for control

- :material-code-tags: __Open Software__

    - Open source dependencies
    - Modular
    - Extendable

- :material-code-tags: __Robust Software__

    - Minimal dependencies
    - Modular architecture
    - UI and DSP separation
    - System and Function Separation

- :material-code-tags: __Essential Software__

    - Single functionality
    - Standardized UI system

- :material-ethernet: __Open Connectivity__

    - Fewer cables
    - Open, non-proprietary formats
    - No proprietary connectors

- :material-ethernet: __Robust Connectivity__

    - Prefer cables over wireless
    - Single connector per use case
    - USB Midi Host when possible
    - Doesn't need computer to work

- :material-ethernet: __Essential Connectivity__

    - Ethernet with midi and audio
    - Standardized connectors

</div>


### Notes:


### Standardized Hardware:

- **Teensy** microcontrollers for a consistent development environment
- **USB** for power (unified power adapters)
- **TRS 1/8" Type A** for MIDI
- **TS 1/4** for Audio
- **Ethernet** for system integration into a network
- **USB-A MIDI Host** when possible thanks to teensy
- **[DESPEE](https://github.com/openaudiotools/despee)** display module for touchscreen UI

### Robust Hardware

- Often-used components (keys, encoders) are placed on standardized breakout boards for reuse across devices.
- Specific-purpose functionality (mic preamps, effects) is added as separate, interchangeable devices.

### Essential Firmware

- Firmware for SynTEE will be swappable to allow for different synths or other functions but each one will be a separate project.
- UI moved to a separate component to simplify main roles

### Open Connectivity

- Only open, non-proprietary standards.

- MIDI and audio are intended to be available over Ethernet. ([details](networking.md))

## Devices

You can check out the [devices](devices) and [components](components).

## Ecosystem

See [Ecosystem Notes](ecosystem-notes.md) for a full catalog of the open-source hardware, firmware, and software used across the project.
