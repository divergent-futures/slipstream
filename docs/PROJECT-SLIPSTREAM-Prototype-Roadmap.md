# PROJECT SLIPSTREAM — Prototype Roadmap

> **⚠️ BUILD ORDER SUPERSEDED (2026-07-08):** Build #1 is now the Range-Neutral flagship — see [`Flagship_First_Build_Plan_v0_1.md`](Flagship_First_Build_Plan_v0_1.md), which changes locked decisions I.2 #2 (weight target → ≤3,500 lb *loaded*), #3 (no 12 kWh 48V house pack → 12V spine off the donor PCS), and the version arc below. This document remains the reference-build (Weekend tier) roadmap — the future kit — and its bench methods, gates, and budget discipline still govern.

**Version:** v0.1 | **Date:** 2026-06-25 | **Owner:** TJ
**References:** Concept synthesis conversation, 2026-06-25. All numbers below trace to locked decisions in Part I.2.

*Working name. Rename freely.*

---

# Part I — Strategic Frame

## I.1 What this is

Project Slipstream is a custom aerodynamic electric weekend trailer designed to be towed behind a Tesla Model Y by a single owner-builder, sleeping two and serving as an off-grid base for hiking-focused weekend trips. Three prototype versions, one trailer growing up in public. Each version retires specific risks from the locked V1.0 baseline and earns the right to spend the next tier of resources. The V0.1 bench rig validates the same architecture as the V1.0 trailer — broken into subsystems on the workbench rather than integrated into a road-going vehicle.

The arc is a personal-cash flywheel with a hard stop point: V0.1 is bench work in the garage with the major component purchases (battery, electrical, actuators, CFD validation). V0.5 is the first complete rolling prototype — functional, not pretty. V1.0 is the refined, livable, finished version. **Personal cash exposure caps at the end of V1.0.** V2.0 and V3.0 (DFM pass and small-batch production) are speculative and only proceed if external interest emerges post-V1.0; they are not committed.

## I.2 Locked decisions

1. **Tow vehicle is Tesla Model Y.** Fixes width target (78" body match), tongue weight cap (~350 lbs), GVWR (3,500 lbs), and aero envelope (stay within the Model Y's slipstream).
2. **Target dry weight ~1,900 lbs.** Leaves ~800 lbs for water, gear, food, and personal margin while staying under the tow limit.
3. **12 kWh LFP battery, frame-integrated.** Sized for ~2 hot-night-AC days + ~4+ mild days off-grid. Frame-rail integration drops CG and saves interior volume. LMFP cells acceptable substitution if available.
4. **Pop-up roof with rigid lower box.** Resolves the aero/headroom trade. ~4 ft interior down, ~6 ft up. 4× synchronized 48V electric linear actuators, soft canvas sides.
5. **Window AC, not mini-split.** Chosen for the smaller pop-down sleeping volume and summer-only use. Mounted through a sealed rear-wall opening with a removable foam plug for storage.
6. **Outdoor shower only + composting toilet with urine diverter.** No black tank, no inside wet bath. Gray tank for sink and AC condensate only.
7. **Aluminum frame, foam-core composite walls with fiberglass skin.** The weight target requires both. Sealed belly pan for aero.
8. **Personal cash hard cap at end of V1.0.** V2.0/V3.0 only proceed with external funding (preorders, partners, or investment) — never personal cash.
9. **15 ft overall (12 ft box + 3 ft tongue).** Long enough for the layout, short enough for storage and tight campground loops.

## I.3 Operating principles

- **Traceability.** Every subsystem decision points back to a locked decision in I.2. If a row in the BOM doesn't trace, it gets cut.
- **Aero gains hide in the rear, not the front.** The Model Y has already pushed the air aside ahead of the trailer; rear taper, belly-pan smoothness, and rounded leading edges matter more than front-face shape.
- **Weight cascades.** Every 50 lbs added forces another 50 lbs of tradeoff (less water, less gear, less margin). Weight discipline is non-negotiable.
- **De-risk on the bench before on the road.** Subsystem failures in the garage cost time; subsystem failures at a campsite cost the weekend.
- **Modularity.** V0.5 reuses V0.1 electrical and actuator hardware. V1.0 reuses V0.5 frame and chassis. Nothing thrown away.
- **Honest cadence.** Gates don't get waived to recover schedule. Better to extend than to ship a version that wasn't earned.

## I.4 Version map

| Version | Scale | Primary purpose | Funding | Sourcing tier | Target window |
|---|---|---|---|---|---|
| **V0.1** | Bench | Subsystems validated independently | Personal cash | Tier 1–2 | Q3 2026 → Q1 2027 (~6 months) |
| **V0.5** | Full but rough | First complete rolling trailer; functional not pretty | Personal cash | Tier 1–2 | Q1 2027 → Q3 2027 (~9 months) |
| **V1.0** | Full + refined | Final aesthetic + functional trailer | Personal cash | Tier 2–3 | Q4 2027 → Q2 2028 (~6–9 months) |
| **V2.0** | Speculative | DFM pass — only if commercial interest emerges | External / TBD | TBD | TBD |
| **V3.0** | Speculative | Small-batch production | External / TBD | TBD | TBD |

## I.5 The funding flywheel

```
V0.1 (personal cash, ~$15–20K)
   ↓ subsystems validated
V0.5 (personal cash, ~$20–30K)
   ↓ rolling trailer; weekend trips prove the architecture
V1.0 (personal cash, ~$15–25K incremental)
   ↓ refined, finished article — personal use
[Decision point: stop here, or seek external interest for V2.0]
V2.0 (external only)
V3.0 (external only)
```

Each arrow is a gated handoff. If a gate doesn't pass, the version extends — it does not skip forward. The V1.0 → V2.0 arrow is a hard wall: no personal cash beyond V1.0.

---

# Part II — Per-Version Detail

## II.1 — V0.1: Subsystem bench validation

**Window:** ~6 months. Q3 2026 – Q1 2027.
**Site:** Home garage / shop.
**One-line purpose:** Validate the riskiest subsystems independently before integrating them into a rolling trailer.
**Sourcing strategy:** Tier 1–2. Maker-grade and professional off-the-shelf components. Custom only where commercial doesn't exist (battery pack enclosure, actuator test rig).

### Scope

- **Battery pack:** 12 kWh, 48V nominal, LFP (or LMFP if available). Custom slim-form pack assembled and BMS commissioned. Capacity-tested to ≥11.5 kWh usable.
- **Electrical core:** Victron MultiPlus II 48V/3000VA inverter/charger; Cerbo GX with cellular gateway and VRM monitoring; MPPT solar charge controller. Bench-integrated and run on simulated daily load.
- **Pop-up actuator rig:** 4× 48V linear actuators (24" stroke, ~1,500 lb rated each), sync controller, encoder feedback. Mounted to a small test frame.
- **Composite wall panels:** Sample foam-core + fiberglass panels for insulation, water-intrusion, and structural rigidity testing.
- **Interior mockup:** 1:1 cardboard/foam mockup of the cabin for ergonomic walkthrough — sleep, sit, bathroom access, galley reach.
- **CFD modeling:** Full-scale digital model of the locked geometry. 1:8 scale wind tunnel article for validation.
- **Aluminum frame:** Drawings finalized; fabricator selected; quote in hand.

**Out of scope at V0.1:** Rolling chassis, road testing, shell assembly, water systems, finished interior, paint.

### Gates (all must pass to close V0.1)

1. **Battery capacity:** ≥11.5 kWh usable, 50A continuous discharge, BMS protections verified.
2. **Electrical integration:** Inverter + MPPT + battery + Cerbo run a 5 kWh simulated daily load for 7 days without intervention.
3. **Actuator sync:** 4-corner rig raises/lowers a 200 lb test load 50 cycles with ≤1° rack across corners.
4. **CFD result:** Predicted drag adds ≤10% to Model Y at 65 mph (estimated ~25% range loss).
5. **Wind tunnel validation:** Scale model results match CFD within 15%.
6. **Interior mockup:** Walkthrough confirms 6 ft popped-up headroom, sleep ergonomics, bathroom access without conflicts.
7. **Frame quote:** Fabricator quote signed; ≤$6,000.

### Retires

- Battery integration risk (cells fit the frame rail depth, BMS works, capacity meets spec)
- Pop-up mechanism risk (sync, load, mounting)
- Aero risk (drag prediction validated before composite tooling is committed)
- Ergonomic risk (catches "this floor plan doesn't actually work" before $30K spent)
- LMFP supply chain risk (decision locked: LMFP if available, else standard LFP)

### Budget

| Bucket | Range (USD) |
|---|---|
| LFP/LMFP cells + BMS + enclosure | $5,000 – $7,000 |
| Inverter, MPPT, Cerbo, cellular, wiring | $3,000 – $4,000 |
| 4× actuators + sync controller + test rig | $2,000 – $3,000 |
| Composite panel samples + materials | $500 – $1,000 |
| CFD software/consultant + wind tunnel | $2,000 – $5,000 |
| Mockup materials, tooling, misc | $500 – $1,000 |
| **Total** | **$13,000 – $21,000** |

*Swing item: CFD/wind tunnel — depends on consulting vs. in-house OpenFOAM.*

### Outputs

- Bench-validated electrical system, ready for installation
- Validated pop-up mechanism with documented sync controller settings
- CFD report + wind tunnel data package
- Frame drawings ready for fabrication
- V0.5 BOM and build plan

**Gate to V0.5:** All V0.1 gates pass + V0.5 BOM drafted + frame fabricator under contract.

---

## II.2 — V0.5: First functional rolling prototype

**Window:** ~9 months. Q1 2027 – Q3 2027.
**Site:** Home garage / shop.
**One-line purpose:** Build the first complete trailer. Functional, not pretty. Validate towing dynamics, real-world off-grid performance, and integrated system behavior at full scale.
**Sourcing strategy:** Tier 1–2. Professional off-the-shelf for critical subsystems; bespoke for the frame and composite shell.

### Scope (delta from V0.1)

- **Chassis:** Aluminum frame fabricated and assembled. Timbren or Dexter torsion axle (~2,000 lb rated). 15" wheels, LT-rated tires. Spare on the rear bulkhead.
- **Frame integrations:** Water tanks (~20 gal fresh, ~10 gal gray) within frame rails; battery pack in frame rails with stone-strike skid plate; sealed smooth belly pan.
- **Shell:** Foam-core composite walls with fiberglass skin. Basic profile (less aero refinement than V1.0). Rounded leading edges, partial rear teardrop taper above the bed.
- **Pop-up:** Roof assembly with full roof solar (~1,000–1,100W), 4 production actuators with sync controller, soft canvas sides (Sunbrella or Stamoid), perimeter EPDM gasket, drip-skirt geometry, 4 mechanical over-center latches.
- **Climate:** Window AC unit (Midea U-shape or LG inverter model — ~5,000 BTU, lowest available draw) mounted through sealed rear-wall opening.
- **Galley + utilities:** Induction single-burner, small 12V/48V compressor fridge (~3 cu ft), 2–4 gal tank water heater, water pump, sink, outdoor hot/cold shower spigot.
- **Sanitation:** Composting toilet (Nature's Head or Trelino) with urine diverter; external urine empty port.
- **Electrical interfaces:** NEMA 14-50 shore power inlet; NEMA 14-50 outlet for Tesla pass-through; load-balancing power management.
- **Tow integration:** 2" ball hitch with integrated anti-sway (Andersen No-Sway or equivalent); Curt Echo Bluetooth brake controller; electric brakes on the axle; powered tongue jack with caster foot.
- **Ventilation:** Low front intake + high rear exhaust via 12V reversible fan with auto-louver and external rain shroud. (No roof vent — roof reserved for solar.)
- **Smart layer:** Cerbo GX cellular gateway, VRM remote monitoring, smart relays on water heater and AC for remote pre-conditioning.

**Out of scope at V0.5:** Aesthetic finish (paint, polish), ambient exterior lighting, interior projector + speakers, upholstered surfaces, custom cabinetry.

### Gates (all must pass to close V0.5)

1. **Tow dynamics:** Trailer tows behind Model Y at 65 mph with stable handling, no sway, no clearance issues. 200-mile test run with mixed road conditions.
2. **Pop-up reliability:** Roof raises and lowers in <60 seconds; seals against overnight heavy rain test; 100 cycles with no rack or seal failure.
3. **3-day off-grid:** Starts at 100% battery in mild weather; ends ≥30% after 3 days of normal use (cooking, lighting, fridge, water pumping). Solar fully covers daily load.
4. **Hot-night AC test:** 12 hrs of AC at 85°F+ ambient consumes <5 kWh. Cabin holds ≤72°F throughout.
5. **Range impact:** Tesla range loss vs. solo driving ≤30% in real-world towing on mixed routes.
6. **Water systems:** 30 days of intermittent use with zero leaks. Condensate routes cleanly to gray tank.
7. **Brake controller:** Curt Echo pairs reliably; proportional braking confirmed.
8. **Remote monitoring:** Cerbo + VRM functional; water heater pre-heat triggerable from phone while driving.

### Retires

- Tow dynamics risk (Model Y actually handles the trailer)
- Pop-up sealing in rain
- Real-world power budget (battery + solar deliver the predicted off-grid days)
- AC sizing (window unit is or isn't enough)
- Water/sanitation workflow at the campsite
- Frame fabricator reliability

### Budget

| Bucket | Range (USD) |
|---|---|
| Aluminum frame fabrication | $4,000 – $6,000 |
| Composite wall panels + materials | $3,000 – $5,000 |
| Torsion axle + wheels + tires + spare | $1,500 – $2,500 |
| Production actuators + soft walls | $3,000 – $4,500 |
| Roof solar panels (~1,000–1,100W) + mounts | $1,500 – $2,500 |
| Window AC + water heater + fridge + induction | $2,500 – $3,500 |
| Composting toilet + plumbing fixtures + tanks | $1,500 – $2,000 |
| Hitch + anti-sway + Curt Echo + electric brakes | $1,000 – $1,500 |
| Tongue jack + lights + exterior fittings | $500 – $1,000 |
| Subscriptions (Victron VRM, Starlink trial) | $500 – $1,000 |
| Documentation + overhead | $500 – $1,000 |
| **Total** | **$19,500 – $30,500** |

### Outputs

- Rolling, livable trailer
- 90+ days of real-world data (battery curves, solar harvest, AC load profile, water consumption, miles towed, range impact)
- Punch list for V1.0 refinements
- Decision: continue to V1.0, or stop here

**Gate to V1.0:** All V0.5 gates pass + 30 days of personal use + explicit decision to refine further.

---

## II.3 — V1.0: Refined production-aesthetic build

**Window:** ~6–9 months. Q4 2027 – Q2 2028.
**Site:** Garage; rented shop space for paint and finish if needed.
**One-line purpose:** The trailer as imagined. Full aero refinement, beautiful finish, all features.
**Sourcing strategy:** Tier 2–3. Bespoke where the V0.5 lessons demand it. Documented vendor relationships for critical parts.

### Scope

- **Refined aero shell:** CFD-optimized rear taper executed in composite, fully smooth belly pan, rounded leading edges to V0.1 spec.
- **Finish:** Polished aluminum or painted composite exterior. Interior cabinetry, upholstered bed and dinette, finished surfaces throughout.
- **Ambient exterior lighting:** Perimeter LED strip, warm white, smart-controlled. Adjustable color temp.
- **Interior media:** Ceiling-mounted projector, projection surface on the front bulkhead (or pull-down outside for awning movie nights), Bluetooth speakers.
- **Awning:** Curb-side roll-out awning with poles for rain protection over the outdoor kitchen / lounge area.
- **V0.5 punch list resolved:** All issues from the V0.5 90-day test period addressed.

**Out of scope at V1.0:** Anything requiring qualification testing (vibration chamber, thermal-vacuum). This is a personal article, not a qualified production unit.

### Gates

1. **Aero refinement:** Range loss vs. solo Model Y at 65 mph ≤25% (improving on V0.5's ~30%).
2. **Aesthetic finish:** Subjective gate — passes the "would I let friends see it" test.
3. **V0.5 punch list:** 100% closed.
4. **Two consecutive 4-day off-grid trips:** Zero significant issues, both in summer conditions.
5. **Documentation:** Full build documentation complete (photos, drawings, BOM, decision log).

### Retires

- Aero gaps remaining from V0.5
- Build-quality and finish-quality risk
- Long-term reliability of integrated subsystems

### Budget

| Envelope | Range (USD) |
|---|---|
| Realistic (incremental to V0.5) | $15,000 – $25,000 |
| Scrappy (self-finish, minimal upgrades) | $8,000 – $12,000 |

### Outputs

- Finished trailer
- Complete build documentation
- Decision: stop here for personal use, or explore commercial path (V2.0)

**Gate to V2.0:** Outside expression of interest sufficient to justify committing engineering effort to a DFM pass. Personal cash does not fund V2.0.

---

## II.4 — V2.0: (Speculative) DFM pass

**Not committed.** Proceeds only if, post-V1.0, external interest (preorders, partner, investor) is sufficient to justify the engineering effort. Likely scope: tooled aluminum frame jigs, composite panel molds, simplified assembly process, design refinements to enable a 5–10 unit small batch. Funding: external only.

## II.5 — V3.0: (Speculative) Small-batch production

Even more speculative. Proceeds only if V2.0 validates a path to market.

---

# Part III — Cross-version workstreams

**CAD model.** Single source of truth for geometry, weight distribution, and CG. Built in V0.1, maintained through V1.0. Every meaningful design decision is reflected in the model before being built.

**Weight log.** Spreadsheet tracking every component weight and CG location. Updated whenever a part is purchased or installed. The dry weight does not exceed 1,900 lbs without an explicit decision to revisit the tow envelope. Tongue weight does not exceed 350 lbs at any point.

**Decision log.** Every locked decision recorded with date, rationale, what it retires, and revisit trigger. See Appendix D for entries from this roadmap.

**Build documentation.** Photo and video record of every subsystem build. Essential for the V0.5 → V1.0 carryover, and indispensable if V2.0 ever happens.

**Test trip log.** Every overnight and longer trip logged: weather, ambient temperature, AC runtime, battery start/end, solar production, water consumption, what worked, what didn't.

**Aero workstream.** CFD model maintained continuously. Each shell revision (V0.5 basic profile → V1.0 refined) re-runs the model. Wind tunnel article in V0.1 is the only physical scale test.

---

# Part IV — Risk register

| # | Risk | L | I | Mitigation | Status |
|---|---|---|---|---|---|
| 1 | Tongue weight exceeds 350 lb Model Y limit | M | H | Battery aft-of-axle option pre-engineered. CG tracked from V0.1. Weight log enforced. | Open |
| 2 | Pop-up roof leaks in heavy rain | M | M | Soft-wall seal geometry validated V0.1. Drip skirt over box. Overnight rain test required in V0.5. | Open |
| 3 | Aero predictions off; range loss >30% | L | M | CFD + wind tunnel in V0.1 before composites. Rear taper is dominant variable; refined further in V1.0. | Open |
| 4 | Real-world off-grid performance < predicted | M | M | Bench validation V0.1 + real-trip validation V0.5 before V1.0 spend. | Open |
| 5 | Scope creep / personal-cash overrun | M | H | Hard caps per version. V1.0 only after V0.5 satisfaction check. V2.0+ external only. | Open |
| 6 | Timeline slips >12 months | M | L | Personal project, no external deadline. Acceptable. | Open |
| 7 | Battery thermal management failure | L | H | LFP heater pad. Stone-strike skid plate. Temp sensors. Insulated frame rails. | Open |
| 8 | LMFP supply chain (newest chemistry) | M | L | Fall back to standard LFP if unavailable; ~10% weight penalty acceptable. | Open |
| 9 | Window AC inadequate for hot nights | L | M | V0.5 hot-night test. Mini-split fallback option (pre-install interface space). | Open |
| 10 | Frame fabricator delays | M | M | Quote in hand before V0.1 closes. Alternate fabricator identified. | Open |
| 11 | Tesla pass-through electrical interface fails certification / safety | L | M | Load-balancing tested on bench V0.1. Conservative spec on cabling and breakers. | Open |
| 12 | Brake controller (Curt Echo) compatibility with Tesla Model Y | L | M | Validated in V0.5 with 200-mile test. Fallback: hardwired aftermarket controller. | Open |

---

# Part V — Document control

This roadmap version is **v0.1**. Locked decisions in Part I.2 are stable at this version. Refinements to budget detail, gate thresholds, and subsystem scope are expected as V0.1 progresses; any refinement touching the I.2 decision list bumps the roadmap to v0.2 with a changelog entry.

**Migration plan to per-version files.** This master roadmap stays as the master through V0.1. Once V0.1 closes and V0.5 begins, Part II.2 (V0.5) splits into `SLIPSTREAM_V0_5_Spec.md` and so on. Master keeps Part I and Parts III–V; version detail moves to dedicated files. Migration trigger: V0.1 close + 30 days of stable V0.5 scope.

---

# Appendix A — Surrounding document architecture

Project Slipstream document set (planned, not all required from day one):

- **SLIPSTREAM-00-Charter.md** — Narrative spine. See Appendix B scaffold below.
- **SLIPSTREAM-01-Architecture.md** — Subsystem block diagrams, interfaces, locked geometry, CAD references.
- **SLIPSTREAM-02-Performance-and-Risk.md** — Power budget detail, weight balance, CFD results, risk narrative.
- **SLIPSTREAM-03-Prototype-and-Roadmap.md** — *This document.*
- **SLIPSTREAM-04-Heritage-and-Feasibility.md** — Reference articles (Lightship, Polydrops, Bowlus, Hutte Hut, Earth Traveler T250LX), gap analysis.
- **SLIPSTREAM-99-Decision-Log.md** — Running record of locked decisions. Seeded by Appendix D below.

**Minimum viable on day one:** Charter (00) + Roadmap (03 — this file) + Decision Log (99). Others fill in as needed.

---

# Appendix B — Charter scaffold (narrative spine)

1. **The problem.** Existing EV-compatible camping trailers split into two unsatisfying camps: cheap-but-boxy traditional designs that destroy EV range, and expensive aero-electric flagships ($35K+ Polydrops loaded, ~$250K Lightship L1). No current production model combines full-roof solar, pop-up headroom, frame-integrated battery, and Tesla Model Y body-width — which is the spec that actually works for the way I use a weekend trailer.

2. **What we have for free.** A Tesla Model Y as the tow platform. Garage workspace. Time (weekends, evenings). CAD skills. Patience to iterate.

3. **What we have to make.** A trailer that proves a sleek, aero, livable pop-up EV trailer is achievable by a single builder for ~$50–70K total spend over ~24 months.

4. **The components doing the work.** Aluminum frame (lightweight backbone). Foam-core composite shell (insulation + low weight). 12 kWh LFP battery in the frame rails (low CG, hidden mass). ~1,000W roof solar (energy autonomy). Pop-up roof with 4× linear actuators (aero down, livable up). Window AC (cheap, simple, sufficient). Composting toilet + outdoor shower (no black tank). Each is non-negotiable: remove any one and the trailer's value proposition collapses.

5. **The closure / the loop.** Solar in → battery → 12 hrs of overnight AC + cooking + lighting + projector → next-day's solar refills. The trailer parks itself in the sun during the day while I'm hiking; recharges autonomously; provides full evening comfort when I return. The loop closes daily in mild weather, every 2–3 days in hot weather, and on shore power when needed.

6. **The container / the form.** 78" wide (Model Y body match — zero overhang, zero mirror eddy). 15 ft overall (12 ft box + 3 ft tongue). ~5 ft tall popped down (in the Model Y slipstream), ~7 ft popped up (standing headroom). Partial rear teardrop taper (aero where it counts). The convergence with the Model Y's geometry isn't a coincidence — it's the reason Slipstream has its specific form.

7. **The buffer / the safety margin.** NEMA 14-50 shore power inlet (universal RV park compatibility, adapters down to 30A and 15A). NEMA 14-50 outlet on the trailer (Tesla pass-through — the trailer becomes a backup range extender in emergencies). Foldable solar option (deprecated; full roof solar makes it unnecessary).

8. **The scaling.** Not a scaling project. Single article. The roadmap arc is V0.1 → V0.5 → V1.0; commercial scaling (V2.0/V3.0) is speculative and not part of the personal commitment.

9. **Why now.** LFP and LMFP cell prices and energy density. Affordable 48V actuators and inverters (Victron ecosystem matured). CFD tools (OpenFOAM, Ansys Discovery) accessible to individual builders. Tesla NACS + NEMA 14-50 universal charging compatibility. Reference designs (Lightship, Polydrops) prove the architecture is real.

10. **What this isn't.** Not a Cybertruck-RV replacement. Not for cold-weather camping. Not a full bathroom (no inside shower). Not a "live in it for a month" trailer — it's a weekend base camp. Not a commercial product (yet).

**Closing line.** *A weekend base camp that pulls 75% of its own weight in aerodynamics and the rest in elegance.*

---

# Appendix C — Sourcing tier definitions

(Standard template — tiers 0–5 as defined in the parent template. Project Slipstream targets Tier 1–2 through V0.5 and Tier 2–3 in V1.0. No Tier 0 (recycled) on the critical path; Tier 4–5 only if V2.0 ever happens.)

---

# Appendix D — Decision log (seed entries)

## Decision 1 — Tow vehicle committed to Tesla Model Y
**Date:** 2026-06-25 | **Locked at:** v0.1
**Context:** Defines every downstream constraint — width, weight, tongue weight, electrical interfaces, aero envelope.
**Options:** Model Y / Model X / different EV / ICE truck.
**Decision:** Tesla Model Y.
**Rationale:** Owned vehicle. Constrains the design productively rather than aspirationally.
**Retires:** Tow envelope open question.
**Commits to:** 78" body-match width, 1,900 lb dry target, NEMA 14-50 architecture, Tesla pass-through outlet, Curt Echo (or equivalent) brake controller.
**Revisit trigger:** Primary tow vehicle changes.

## Decision 2 — Pop-up roof with rigid lower box
**Date:** 2026-06-25 | **Locked at:** v0.1
**Context:** Resolving the apparent aero/headroom tradeoff.
**Options:** Fixed low / fixed high / pop-up.
**Decision:** Pop-up roof with 4× synchronized 48V electric linear actuators and soft canvas sides.
**Rationale:** Lightship L1 and Polydrops Eagle prove the concept. The aero/headroom tradeoff dissolves when the roof only goes up while parked.
**Retires:** Aero-vs-headroom debate.
**Commits to:** 4-actuator sync controller, soft-side construction, perimeter EPDM gasket, drip-skirt geometry, 4× mechanical over-center travel latches.
**Revisit trigger:** Pop-up reliability failures persistent in V0.5.

## Decision 3 — Window AC over mini-split
**Date:** 2026-06-25 | **Locked at:** v0.1
**Context:** Climate control for summer-only use.
**Options:** Window AC / mini-split.
**Decision:** Window AC mounted through sealed rear-wall opening.
**Rationale:** Pop-down sleeping volume is small; 12 hrs/night runtime is short; summer-only use makes mini-split overkill. Lower cost, lower complexity, simpler maintenance.
**Retires:** Climate complexity for V1.0.
**Commits to:** Rear-wall mounting frame, gasket flange, removable foam plug for winter storage, ~5 kWh hot-night budget.
**Revisit trigger:** V0.5 hot-night test fails cooling target.

## Decision 4 — 12 kWh LFP battery in frame rails
**Date:** 2026-06-25 | **Locked at:** v0.1
**Context:** Battery sizing for off-grid autonomy versus weight.
**Options:** 10 / 12 / 15 kWh.
**Decision:** 12 kWh LFP (LMFP if available), frame-integrated.
**Rationale:** 2 hot-AC days + 4+ mild days off-grid. Frame integration drops CG, saves interior volume.
**Retires:** Battery sizing debate.
**Commits to:** Custom slim pack (not drop-in box), frame rail depth 5–6", stone-strike skid plate, LFP heater pad for sub-freezing charging.
**Revisit trigger:** V0.5 real-world autonomy persistently below target.

## Decision 5 — Outdoor shower + composting toilet; no inside wet bath
**Date:** 2026-06-25 | **Locked at:** v0.1
**Context:** Sanitation architecture.
**Options:** Inside wet bath / outdoor shower + composting head.
**Decision:** Outdoor shower + composting toilet with urine diverter.
**Rationale:** Summer trailer. Drops black tank entirely. Frees interior space and weight.
**Retires:** Black-tank requirement.
**Commits to:** Gray tank (~10 gal) for sink + AC condensate. Nature's Head or Trelino head. External urine empty port.
**Revisit trigger:** None expected.

## Decision 6 — Full roof solar; ventilation moves to side walls
**Date:** 2026-06-25 | **Locked at:** v0.1
**Context:** Maximizing solar harvest.
**Options:** Roof vent + ~800W solar / full roof solar + side vent (~1,000–1,100W).
**Decision:** Full roof solar.
**Rationale:** Roof real estate is more valuable as power than as ventilation when the pop-up perimeter provides ventilation. Side-wall reversible 12V fan with auto-louver covers closed-up ventilation needs.
**Retires:** Solar capacity ceiling.
**Commits to:** Front-low intake + rear-high exhaust ventilation strategy, external rain-shrouded fan housing.
**Revisit trigger:** V0.5 ventilation testing inadequate.

## Decision 7 — NEMA 14-50 as the universal electrical interface
**Date:** 2026-06-25 | **Locked at:** v0.1
**Context:** Shore-power inlet standard and Tesla pass-through.
**Options:** TT-30 (30A) / NEMA 14-50 (50A).
**Decision:** NEMA 14-50 for both inlet and Tesla pass-through outlet. Adapter kit for 30A / 20A / 15A pedestals.
**Rationale:** Adapters go down, never up. NEMA 14-50 covers everything from Tesla mobile connector to full RV pedestals. Single inlet/outlet standard simplifies the electrical architecture.
**Retires:** Connector debate.
**Commits to:** Victron MultiPlus II 48V/3000VA as the central inverter/charger. Load-balancing between trailer battery charging and Tesla pass-through.
**Revisit trigger:** None expected.

## Decision 8 — Personal cash cap at end of V1.0
**Date:** 2026-06-25 | **Locked at:** v0.1
**Context:** Funding flywheel hard stop.
**Options:** Open-ended personal funding / capped at V1.0 / capped earlier.
**Decision:** Cap at end of V1.0. V2.0 and V3.0 require external funding.
**Rationale:** This is a personal weekend trailer first. Commercial path is speculative and should not put personal finances at risk.
**Retires:** Risk of "throwing good money after bad."
**Commits to:** V1.0 is the final personally-funded version. Decision to pursue V2.0 is contingent on external interest, not on personal motivation.
**Revisit trigger:** External funding offer that changes the calculus (e.g., signed preorders or a partner with capital).

---

*Document status: v0.1. Adapt freely as V0.1 progresses.*
