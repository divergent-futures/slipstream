# Slipstream

> Intended home: `github.com/divergent-futures/slipstream`

An open-source, aerodynamic, all-electric camping trailer family — designed to be towed behind an EV without destroying its range. Sister project to the [House BUS](https://github.com/divergent-futures/divergent-house-bus): the bus is the dwelling, Slipstream is the weekend base camp.

*A weekend base camp that pulls 75% of its own weight in aerodynamics and the rest in elegance.*

## The idea

One platform, many builds — configured, not customized. The invariant core (~80% of parts) is shared across every trailer: aluminum frame with frame-integrated battery and tanks, 48V Victron electrical spine, NEMA 14-50 universal power interface, composite foam-core shell, sealed aero belly pan, torsion suspension. The fork tree (~20%) is what you choose.

The tier ladder is **build complexity, not range**:

| Tier | ~Price | What it is |
|---|---|---|
| Foamie | $5–12K | Beginner A-frame/foam build, weekend tools |
| Weekend | $30–40K | The reference: 12' pop-up, summer, 12 kWh, sleeps 2 |
| Explorer | $50–60K | 3-season, heat pump, bigger systems |
| Base Camp | $70–90K | 4-season, interior wet stall, expedition tanks |
| Overland | $80–100K | Off-road package + drive assist |
| Range-Neutral | $90–120K | Salvaged Tesla Model 3/Y pack (~80 kWh) + tongue-force-sensing propulsion — the trailer pushes itself; your car loses ≈0% range |

## Repository structure

- `docs/` — design source of truth: the fork-tree handoff (every decision point + rationale), the three-version prototype roadmap (V0.1 bench → V0.5 rolling → V1.0 refined), and vendor sourcing research
- `configurator/` — `slipstream.config.json` (the full fork tree in `df-configurator/v1` schema: 62 forks, 45 compatibility rules, parts/BOM data) and a self-contained HTML configurator — open it in any browser

The configurator data format is shared with the House BUS (see `Configurator_Platform_Spec.md` in that repo); a standalone configurator app consuming both products is planned as its own repository.

## Status

Pre-build. Reference Build #1 (the maintainer's personal summer/Model Y config) is locked and V0.1 bench validation is scheduled Q3 2026 → Q1 2027. Numbers in the configurator are first-order estimates; they get replaced by real weights and invoices as the build progresses.

## License

Hybrid open-source: hardware under CERN-OHL-S-2.0, code under MIT, documentation under CC-BY-4.0 — see [LICENSE.md](LICENSE.md).
