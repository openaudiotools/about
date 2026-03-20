# Contributing

I'm looking for people who find this project interesting and want to help shape it — electronics folks, firmware developers, product designers, musicians, audio engineers. Professional or hobbyist, doesn't matter. If you care about open, buildable audio gear, you're welcome here.

## Start with the discussions

The single best thing you can do is join the [GitHub Discussions](https://github.com/openaudiotools/about/discussions) and share your thoughts. Each device has its own discussion category — see the [Devices](devices/index.md) page for the full list and the [Project Status](status.md) page for where things stand.

I'd love to hear your thoughts — whether it's high-level ideas about what these devices should do, or specific opinions on implementation details like component choices, circuit topologies, and design trade-offs. I especially appreciate constructive technical critique and concrete proposals. If you've worked with a particular codec, MCU, or connector and have a take on why it does or doesn't fit here, that kind of input is incredibly helpful.

## Where I need help

**Musicians and audio engineers** — you know how this stuff gets used in practice. What matters in a mixer? What's annoying about the gear you have? What would you actually want to build? That kind of input directly shapes what these devices become.

**Electronics and PCB design** — if you know your way around CAD or PCB layout and the project catches your eye, I'd love to have you on board. Once the device specs are finalized, there will be real work to do on schematics, board layout, and prototyping.

**Software and firmware** — this is where I can contribute the most myself, and where I'm most keen to have discussions. Architecture, DSP, networking, embedded dev — all of it. The repos are here:

- [openaudiotools/mixtee](https://github.com/openaudiotools/mixtee)
- [openaudiotools/syntee](https://github.com/openaudiotools/syntee)
- [openaudiotools/despee](https://github.com/openaudiotools/despee)

**Product design** — enclosures, user interfaces, manufacturing. If you have experience there, your perspective would be really helpful. These devices should be easy to build and easy to use.

## Repository structure

Each device repo follows the same layout:

```
device-name/
├── hardware/
│   ├── pcbs/              # KiCad projects, one subfolder per board
│   │   └── board-name/
│   │       ├── designs/   # KiCad schematic + PCB files
│   │       ├── architecture.md
│   │       └── connections.md
│   ├── lib/               # Custom KiCad footprint libraries
│   └── *-layout.*         # Physical layout drawings (SVG, PNG)
├── firmware/
│   ├── src/               # Application source code
│   ├── lib/               # Local libraries
│   └── platformio.ini     # Build configuration (PlatformIO)
├── docs/
│   ├── hardware.md        # Hardware design notes
│   ├── firmware.md        # Firmware architecture notes
│   └── journal/           # Timestamped development log entries
└── README.md
```

The `hardware/pcbs/` folder contains one subfolder per physical board in the device — for example, MixTEE has separate boards for input, output, headphone amp, and more. Each board subfolder has its own KiCad project, architecture description, and connection map.

## Get in touch

Want to help directly? Reach me on Discord: **@juliuszfedyk**

Or just jump into the [Discussions](https://github.com/openaudiotools/about/discussions) — that's where it all happens.