# Why I'm Building This

I'm a hobby musician, and I love tinkering with electronics and DIY gear. Naturally, I found myself drawn into the world of DIY audio and music hardware — a vibrant, generous, creative community of people building their own instruments, sharing schematics, writing firmware, pushing the limits of cheap hardware into unexpected territory. I bought some of it. I built some of it. I love that world.

But I also kept running into the same frustrations, in different forms.

## The Gap

> The gap between *"fun to experiment with"* and *"robust enough to actually use"* is real. And nobody is quite filling it.

Some DIY devices are **gloriously experimental** — glitchy, unpredictable, perfect for an exploratory jam or an interesting video. But they're not controllable enough to build a finished track around.

Others are **deeply niche** — beautifully executed for one specific sound or genre, but closed, opinionated, with no real path to making them do something different.

Then there's the **expensive end**: robust, modular, genuinely powerful — but Eurorack, for example, will drain a budget faster than almost anything else in music.

And finally there are the **ambitious all-in-one platforms** — remarkable achievements, but built on a sprawling stack of dependencies that becomes increasingly daunting to maintain over time.

None of these are failures. They're honest tradeoffs made by people doing their best work.

## Openness as a Strategy

Many small-manufacturer and tinkerer projects — even ones built on open-source tools — keep their hardware designs and firmware closed. That's an understandable choice; it protects the work and the business. But it limits who can build, distribute, and improve them.

I want OpenAudioTools to be different: **fully open hardware and firmware**, so that anyone can manufacture these devices, sell them, adapt them, and grow the ecosystem. More supply means lower prices. More builders means faster improvement. Openness isn't just a value here — it's a strategy for adoption.

## The Design Principles

OpenAudioTools is my attempt to fill the gap. The principles came directly from those frustrations:

- **One role per device** — firmware stays focused, maintainable, and works well at its one job
- **Teensy as the hardware platform** — minimal library dependencies, shallow and understandable stack
- **Ethernet instead of USB** — USB in audio is a headache; a cheap network switch solves problems that no amount of driver debugging ever will
- **No built-in controller** — you already have one. The whole point of MIDI is that it separates control from sound. Let's actually honor that

The spirit underneath all of this is simple: **tools should belong to the people who use them.** Open hardware. Open firmware. Open formats. No lock-in, no proprietary connectors, no dependency on a company staying solvent.

## AI for the Music Community

There's one more reason I want to do this. With all the controversy around AI and music, I wanted to find a way to make it work *for* the music community, not against it. I'm a software developer by trade, not a hardware engineer — PCB layout, analog signal chains, codec configurations are not my home ground. So I'm using AI to help bridge that gap, contributing the results to an open platform that belongs to everyone.

## An Invitation

If you're a builder, a firmware developer, a hardware designer, or just someone who's had the same frustrations I have — this is meant to be yours too. The devices are designed to be extended. The firmware is meant to be forked. The whole thing only becomes what it should be if more people bring their ideas to it.

That's why I'm building this.
