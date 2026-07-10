# Contributing to Slipstream

Slipstream is an open-source camping-trailer product family — from a $1,100 foamie to a self-propelled, salvage-Tesla-powered flagship. Contributions welcome at every tier.

## Where things live

- `docs/` — research and plans (cited; verified vs single-source claims are flagged)
- `engineering/` — subsystem design tracks SS01–SS08, each traced to build gates and the T1–T10 interface map
- `guides/` — follow-along build procedures, safety-gated. Guide #0 = foamie entry; #1–3 = the salvage flagship path
- `configurator/` — the fork tree (`slipstream.config.json`, `df-configurator/v1` schema) + self-contained HTML configurator

## How to contribute

1. **Build reports** — the most valuable contribution. Followed a guide? File an issue with what worked, what didn't, and real weights/costs. First-order estimates in the configurator get replaced by field numbers.
2. **Corrections with sources** — every technical claim should trace to a source; corrections should too.
3. **Configurator data** — new fork options or price updates: edit `slipstream.config.json` (effects are deltas vs the default option; parts carry `estUsd` + source), keep the JSON valid, and note your source in the PR.
4. **Safety findings** — anything that makes a guide safer jumps the queue. Open an issue titled `SAFETY:`.

## Ground rules

- HV work is described for competent adults; guides are information, not certification
- No copyrighted service-manual content — link to Tesla's free service docs, don't paste them
- The controller work (SS07) has a patent design-around review pending — control-loop PRs wait for it
- Licensing is hybrid: hardware CERN-OHL-S-2.0, code MIT, docs CC-BY-4.0 (see LICENSE.md)

## Style

Design tracks follow the template pattern in `engineering/`; guides follow the phase/gate/STOP-table pattern. Numbers beat adjectives. Cite or flag.
