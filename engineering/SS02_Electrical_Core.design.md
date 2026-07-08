# SS02 — Electrical Core (48V Victron spine, AC in/out) · Design Track

**Status:** Detailed v0.1 · **Sequence:** 1 (with SS01) · **Depends on:** SS01 pack
**Traces to:** Roadmap I.2 (Victron ecosystem, NEMA 14-50 universal interface), Decision log D7 · **Feeds V0.1 Gate 2:** inverter + MPPT + battery + Cerbo run a 5 kWh/day simulated load for 7 days unattended.

## 1. Purpose & requirements

One electrical language: 48V DC spine, 120V AC where appliances demand it, one universal AC connector standard. Requirements: 3 kVA AC output (window AC + water heater + galley, not simultaneous) · shore charging at 15A–50A pedestals via adapters · Tesla/EV pass-through with load balancing · full remote monitoring + pre-conditioning relays.

## 2. Interfaces

- **T1** 48V bus: pack (SS01) → Lynx-style busbar → inverter/charger, MPPT, DC loads
- **T3** AC: NEMA 14-50 inlet → MultiPlus AC-in; NEMA 14-50 outlet ← MultiPlus AC-out-2 (load-balanced pass-through)
- **T4** Solar: roof array (~1,050W, 2S or 3S strings) → SmartSolar MPPT 250/60 → T1
- **T7** SS03 actuators: 48→24V DC-DC branch, 25A, fused at busbar
- **T9** Cerbo GX: BMS CAN, VRM cellular, smart relays → water heater + AC pre-conditioning
- **T10** Grounding: 48V single-point bond to chassis; AC ground per MultiPlus manual (neutral-ground relay handles shore vs. inverter mode)

## 3. Components (Sourcing doc §5)

| Item | Est. | Notes |
|---|---|---|
| Victron MultiPlus-II 48/3000/35 | ~$1,200 | Inverter/charger, PowerAssist for weak pedestals |
| Victron SmartSolar MPPT 250/60-Tr | ~$435 | One controller, full roof |
| Victron Cerbo GX MK2 (+ GX LTE) | ~$300 + ~$250 | VRM remote monitoring + relays |
| Victron SmartShunt 500A | ~$130 | SoC truth independent of JK BMS |
| Busbar/fusing (Lynx Distributor or equiv.) | ~$250 | Class-T main + MEGA branch fuses |
| NEMA 14-50 inlet + outlet + adapter kit (50→30→20→15A) | ~$350 | |
| 48→24V DC-DC 25A (actuators) + 48→12V 30A (fridge, fans, pumps, lights) | ~$300 | Two rails, both fused |
| Smart relays / contactors (heater, AC) | ~$120 | Driven by Cerbo |
| Wiring, lugs, conduit, breakers | ~$500 | |

**Total ≈ $3,850** — top of the V0.1 $3–4K bucket ✓ (SmartShunt + LTE are the adds; both cheap insurance).

## 4. Load budget (drives Gate 2 simulation)

| Load | Rail | Draw | Duty |
|---|---|---|---|
| Window AC (5K BTU class) | 120V AC | 400–500W run | 12 hr/night hot weather |
| Water heater 2–4 gal | 120V AC | 1,200W | 30–45 min/day, pre-heat via relay |
| Induction single | 120V AC | 1,800W peak | 20–30 min/day |
| Fridge 3 cu ft | 12V | 45W avg | 24 hr |
| Pump, fans, lights, Cerbo, projector | 12V/48V | ~30W avg | varies |

Design day ≈ 5 kWh (hot) / ~3 kWh (mild) — matches roadmap. **Pass-through load balancing:** MultiPlus AC-out-2 sheds the EV outlet when trailer charge current + EV draw would exceed pedestal rating; simple current-limit config, tested on bench with a resistive load bank.

## 5. Open questions

1. One MPPT vs two (roof split port/starboard for partial-shade resilience — +$300, likely V1.0 refinement not V0.1)
2. GX LTE vs. phone-hotspot-only for V0.1 (LTE earns its keep at the campsite, buy it)
3. Pass-through contactor rating for 40A continuous EV draw — spec 50A contactor + derate
4. 12V rail sizing: fridge compressor start surge — 30A DC-DC adequate? Bench-verify.

## 6. V0.1 bench plan

Assemble spine on plywood board (Victron's own bench pattern) → commission via VictronConnect → 7-day scripted load profile (space heater + timer as AC stand-in, heater relay cycling, MPPT on 2 panels) → log to VRM → gate passes if zero manual interventions.

---
*Detailed 2026-07-07. All part slugs shared with House BUS platform vocabulary (victron-multiplus2-48, victron-cerbo-gx, victron-mppt, nema-14-50-inlet).*
