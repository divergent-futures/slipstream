# Drive Unit Bench Bring-Up Guide — Salvage Tesla Model 3/Y

**v0.1 · 2026-07-08 · Slipstream open-source build series · Guide #3**
**What this is:** first controlled spin of a salvaged Model 3/Y drive unit on the bench, and the path decision that precedes it. Follows Guide #1 (donor) and Guide #2 (pack). Authority sources: [Maguire M3-DU repo](https://github.com/damienmaguire/Tesla-Model-3-Drive-Unit) (GPL-3.0, includes OEM pinouts, CAN logs, oil-pump LIN controller), [EV Controls T2C manual](https://www.ev-controls.com/wp-content/uploads/2020/12/EVControlsT2CManual_February_2023.pdf), openinverter forum M3-RDU threads.

> **⚠️ THE hazard specific to this guide: PMSM back-EMF.** The rear drive unit is a permanent-magnet machine — **it generates high voltage at its terminals whenever its output shafts turn, powered or not, 12V or no 12V.** On the bench: never turn the shafts by hand with HV connectors exposed. On the trailer: the DC link is live any time the trailer rolls — this drives the whole SS07 contactor/interlock design.

---

## Phase 0 — Pick your path (the decision is different for a trailer)

| | Maguire V3.2 (openinverter) | EV Controls T2-C | JTAG stock-board reflash |
|---|---|---|---|
| Invasiveness | **6–8 hrs**: open inverter, strip conformal coating (MG Chemicals 8310A, not Dremel), desolder **51 joints**, 11× T20 + 3× T10, swap board | None — reflashes stock firmware via harness (EV Controls does it remotely, one DU per unit) | JTAG adapter onto stock board |
| Cost | Board ~€100–300 class (evbmw; confirm) + hours | **$2,699** (+$1,499 TBC pack controller if wanted) | Adapter cheap; firmware maturity unverified |
| Maturity (July 2026) | V3.2 shipped Mar 2026, **tester-grade** — Damien's bench + Volvo mule only, no independent field reports yet | Mature commercial, dealer network (EV West etc.) | Experimental |
| Torque control | **Arbitrary, including continuous negative torque (regen)** — full openinverter parameter access | Pedal-oriented; regen slider | openinverter-class |
| **Trailer fit** | ✅ **The path.** A trailer needs headless CAN torque commands and continuous regen | ⚠️ **Problematic:** stock firmware "will detect that there is no vehicle attached pretty quickly" (their manual) — it expects a car around it | Watch it mature |

**Slipstream verdict:** the trailer is a *headless* application — no pedal, no vehicle plausibility signals, torque commanded by the hitch-force controller. That's exactly what the openinverter path provides and exactly what stock firmware rejects. **Plan Maguire V3.2, but treat it as what it is (tester-grade): bench it hard, watch the openinverter forum for field reports, keep T2-C as the fallback for a car-like build only.** Front vs rear: rear (PMSM/SiC) is the primary target and the performance pick; front (induction/IGBT) support is newer — but note an induction front unit has *no* back-EMF when towed, which is a genuinely interesting trailer trade. Flag for SS07.

## Phase 1 — Parts and prep

- [ ] Rear DU with **both sides of the motor harness** (inverter 30-pin + shielded resolver harness) — harvest generously at teardown
- [ ] HV harness p/n **1109000-00-D** (Guide #2 shopping list)
- [ ] Maguire V3.2 board (evbmw) + MG Chemicals 8310A stripper, UV light, hot-air station, quality iron
- [ ] Oil pump stays connected (p/n 1108202-00-E) — it's **LIN-controlled (pin 2), not dumb-12V**; use the repo's `Oil_Pump_LIN/` controller
- [ ] HV source for first spin: **two 48V-class modules in series (~87–96V works with `udcmin=0`)** or a 100–350V supply — you do NOT need the full pack for first spin
- [ ] **Series resistor / 2 kW kettle element** in the HV feed (current limit + precharge in one — the community's first-power ritual)
- [ ] 12V supply, bench stand or pallet (bolt through the three mount bosses, strap it), ESD mat + strap for board work
- [ ] Cut-resistant gloves (halfshaft circlips), covers for open output splines

## Phase 2 — The board swap (Maguire path)

1. Inverter off the DU per Tesla manual ("Inverter — Rear Drive Unit"): coolant drained, ESD discipline, note the thermal gap pad for reassembly.
2. Conformal coating off chemically (8310A + brushes + UV inspection). **A propane torch has already killed one builder's board — heat gun/hot-air only, patience.**
3. 30-pin connector clamp (long flat screwdriver, inward latches) → 11× T20 → current sensor housing 3× T10 → **51 solder joints + HVIL joints** desoldered (top/bottom only on HVIL; the white plastic burns easily).
4. V3.2 board in, reverse order. Resolver conditioning is on-board (1 V p-p, 1.6 V offset) — your job is clean shielded wiring, not signal massaging.
5. Reassemble inverter to DU with gap pad checked.

## Phase 3 — Bench setup

1. DU bolted + strapped; **both halfshafts out** (open diff: one shaft in = it whips at 2× speed) — stubs out per manual, gloves on, splines covered.
2. Wiring per repo pinouts (`M3_RearDU_OEM_Pinout.ods` + `OI_Pinout.png`): 12V, CAN (DU has an internal 120 Ω terminator), resolver harness (factory shielded or STP), oil pump LIN node.
3. HV: kettle-element/resistor in series → inverter DC input. Verify polarity. Precharge = the resistor doing its job; watch DC-link voltage come up before any enable.
4. openinverter web UI: confirm firmware comms, set `udcmin` for your bench voltage, torque/speed limits at minimums.

## Phase 4 — First spin

1. Everyone clear of the output side. HV energized through the limiter.
2. Command a **walking-pace spin** (low `ampnom` / low FOC torque). You want slow, smooth rotation — nothing more on day one.
3. **Pass:** smooth low-RPM rotation both directions, sane current draw, steady RPM plot. **Fail modes:** bucking/cogging or slow jerky turning = resolver wiring (shielding, continuity); no comms = CAN termination/12V sequence; jumpy RPM trace = dirty resolver signal.
4. Short runs only: no-load spins need no oil flow (splash) or inverter coolant, but keep sessions to seconds-to-a-minute at low RPM. **Never floor an unloaded DU** (18,000+ RPM ceiling; unloaded runaway is how benches get redecorated).
5. Log everything (openinverter plots) — your baseline for commissioning on the trailer.

## Phase 5 — What this means for the trailer axle (feeds SS07)

- **Gearing works straight up:** 9.036:1 single-speed; at 65 mph on a 30.6" trailer tire the motor sits at **~6,450 RPM** — comfortable mid-band. The complete DU (with its gearbox) IS the trailer e-axle; no extra reduction stage.
- **Back-EMF = design driver:** the DC link is live whenever the trailer rolls. SS07 must treat the DU-side HV as energized-when-moving: contactor logic, interlocks, and service procedure all assume it.
- **No park pawl** in the DU (the car uses brake calipers) — the trailer's parking brake is the drum brakes, as designed. Nothing extra needed, but know it freewheels in "park."
- **Regen on a towed axle is electrically proven, operationally unpublished** — continuous negative torque is a standard openinverter command, but nobody has documented an M3 DU as a trailer regen axle. Slipstream would be first. Bench regen testing (motoring the DU with a second machine, or downhill towing tests at V0.5-equivalent stage) is the validation path.
- **The induction front unit question:** no magnets = no back-EMF when towed = intrinsically safer dead-trailer behavior, at the cost of newer board support and lower efficiency. Genuine SS07 trade study.

## STOP conditions

| Condition | Verdict |
|---|---|
| Any hand-rotation of shafts with HV connectors exposed | Stop — PMSM generates whenever it turns |
| One halfshaft in, one out, spin commanded | Stop — 2× whip hazard |
| Resolver faults "solved" by raising torque | Stop — fix the wiring, not the symptom |
| Unloaded DU commanded above walking-pace RPM on day one | Why? Stop. |
| Isolation fault between HV and chassis at any point | Meg-test everything before proceeding (bad isolation has killed controllers and boards) |

**Next in series (planned):** Guide #4 — hitch-force controller (SS07's core) once the patent design-around review clears; Guide #5 — first dock to the house inverter (SS08 Tier 2).

*v0.1 — V3.2 is four months old and tester-grade as of writing; re-check the openinverter forum for field reports before committing the board swap. When this guide and the Maguire repo disagree, the repo wins.*
