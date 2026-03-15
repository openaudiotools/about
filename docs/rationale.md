# Why I'm Building This

I'm a hobby musician, and I love tinkering with electronics and DIY gear. Naturally, I found myself drawn into the world of DIY audio and music hardware — a vibrant, generous, creative community of people building their own instruments, sharing schematics, writing firmware, pushing the limits of cheap hardware into unexpected territory. I bought some of it. I built some of it. I love that world.

## The Gap

Most DIY projects are **very simple devices**. Usually very useful in a very specific way. Too simple to be called an instrument but definitely fun to build.

Some DIY devices are **gloriously experimental** — glitchy, unpredictable, perfect for an exploratory jam or an interesting video. But they're not controllable enough to build a finished track around.

Others are **deeply niche** — beautifully executed for one specific sound or genre. Deeply rooted in a very focused niche that their authors really wanted to add to. If you're in that niche, hey you're in luck.

Then there's the **expensive end**: robust, modular, genuinely powerful — but like Eurorack, for example, will drain a budget faster than almost anything else in music.

And finally there are the **ambitious all-in-one platforms** — grooveboxes and multifunctional designs. Remarkable achievements, but built on a sprawling stack of dependencies that always feels like held together with sheer willpower and bugfixing grit.

All of those are amazing projects, and I acquired my share of them. They're result of honest tradeoffs made by people doing their best work. I however wanted something robust.

![](https://media1.tenor.com/m/SC2HUvIEo-cAAAAd/i-need-something-robust-complicated.gif)

## The Design Principles

OpenAudioTools is my attempt to build something robust.

- **One role per device** — device stays focused, maintainable, and works well at its one job, hardware has one role, firmware has one function.
    - **No built-in controller** — you already have one. The whole point of MIDI is that it separates control from sound. The devices are either controlled by midi, or are a controller.

- **Easy to code** - Devices should have unified and easy to learn development workflow. That means reusable components, same microcontrollers, shallow stack.
    - **Teensy as the main hardware platform** — minimal library dependencies, shallow and understandable stack
    - **Separate ESP display/navigation** - [Despee](https://github.com/openaudiotools/despee) is a reusable [LVGL](https://lvgl.io/) based navigation component.


- **Easy to connect** - to serve a single purpose the devices should have good connectivity to allow them to work well with other devices. (Think built in USB midi hosts, Ethernet audio.)
    - **Ethernet over USB** — USB audio can be a real headache to connect unless you use a central PC. Ethernet gives you an easy way to connect any enabled device over a simple network switch, and allows for longer distances.

The spirit underneath all of this is simple: **tools should belong to the people who use them.** Open hardware. Open firmware. Open formats. No lock-in, no proprietary connectors, no dependency on a company staying solvent.

## Openness as a Strategy

I want OpenAudioTools to be a **fully open hardware and firmware**, so that anyone can manufacture these devices, sell them, adapt them, and grow the ecosystem. More supply means lower prices. More builders means faster improvement. Openness isn't just a value here — it's a strategy for adoption.

## AI for the Music Community

There's one more reason I want to do this. With all the controversy around AI and music, I wanted to find a way to make it work **for** the music community, not against it. I'm a software developer by trade, not a hardware engineer — PCB layout, analog signal chains, codec configurations are not my home ground. So I'm using AI to help bridge that gap, contributing the results to an open platform that belongs to everyone. And not gonna lie, I wanted to see how far I can push AI usability.

## An Invitation

If you're a builder, a firmware developer, a hardware designer, or just someone who's had the same frustrations I have — this is meant to be yours too. The devices are designed to be extended. The firmware is meant to be forked. The whole thing only becomes what it should be if more people bring their ideas to it.

That's why I'm building this.
