# Flagship Integration Matrix — v0.1

**Date:** 2026-07-08 | **Purpose:** every flagship *function* traced to the *parts* that deliver it, with gaps named. Ran against the configurator's flagship BOM (LFP pack + range-neutral + 12V spine + seasonal dock + donor-PCS charging): **46 parts, ~$32.7K researched.** This is the pre-spend integration check.

Legend: ✅ part(s) in BOM · 🔧 fabrication/design scope (not a purchasable part — tracked in an SS doc) · ⚠️ open item with owner

| # | Function | Delivered by | Status |
|---|---|---|---|
| **Propulsion** ||||
| 1 | Traction energy | CATL LFP salvage pack (sealed, stock BMS/contactors/pyro/precharge) | ✅ |
| 2 | Pack CAN control | Battery-Emulator (LilyGo) | ✅ |
| 3 | Drive torque | Rear DU + Maguire V3.2 board | ✅ (board = tester-grade; bench gate) |
| 4 | System supervision | ZombieVerter VCU (contactors, precharge, modes) | ✅ |
| 5 | Thrust command | Hitch load cell + IMU + drive controller | ✅ part; 🔧 controller firmware = Guide #4 scope, ⚠️ patent review first (SS07) |
| 6 | **Thermal (pack cold plates + DU inverter + ATF heat-exchanger)** | Propulsion thermal loop kit (pump/radiator/fan/reservoir/G48) | ✅ **added this pass — was the biggest missing part** ; 🔧 sizing for 20 kW duty = SS07 todo |
| 7 | DU mounting | — | 🔧 SS05 frame-around-pack CAD scope (subframe adaptation) |
| 8 | Hitch force-sensing coupler integration | load cell part | 🔧 coupler machining = SS05/SS07 scope |
| **Braking / running** ||||
| 9 | Service brakes + breakaway | Dexter drums + breakaway kit (SS05 buy list) + Curt Echo | ✅ |
| 10 | Regen overlay | DU via controller, cut on brake signal | ✅ (firmware scope in #5) |
| 11 | Suspension/wheels/hitch/jack | Timbren pair, 15" wheels, Rapid Hitch, powered jack | ✅ ⚠️ Timbren rating vs flagship GVWR — re-confirm at ~3,500 lb loaded (SS05 Q1) |
| **House power (12V spine)** ||||
| 12 | 12V generation from pack | Donor PCS + Maguire PCS controller | ✅ ⚠️ Phase-A gate: 2 kW for 1 hr on the bench |
| 13 | 12V buffering + winter hibernation | 100Ah 12V LFP buffer | ✅ |
| 14 | 120V loads | MultiPlus 12/3000 | ✅ (48V inverter correctly suppressed from BOM — bug fixed this pass) |
| 15 | 12V distribution at up to ~200A | LV backbone + protection | ✅ part; 🔧 12V-specific busbar/fuse sizing detail = SS02 flagship variant note |
| 16 | Solar | MPPT 250/60 + 4–5×200W | ✅ ⚠️ at 12V the MPPT caps usable array ~900W — plan targets 800W; warn rule added |
| 17 | Monitoring + load mgmt | Cerbo GX (12–70V native) + VRM + relays | ✅ |
| **Charging** ||||
| 18 | Shore → pack (~11 kW) | Donor PCS + controller, NEMA 14-50 inlet | ✅ (semi-mature; Elcon fallback exists in fork) |
| 19 | Home dock charge/discharge | Solis 11.4K + wall Battery-Emulator + HV dock connector | ✅ ⚠️ dock connector = pioneer design item (SS08 Q1) ⚠️ sub-0°C dock charging — BMS lockout; garage dock or warm-loop (SS08 Q4) |
| **V2H** ||||
| 20 | Generator mode | inlet + interlock kit; MultiPlus ground relay = house-feed mode | ✅ |
| 21 | Seasonal whole-loads backup + arbitrage | dock stack (#19) | ✅ ⚠️ AHJ gray zone documented (SS08 Q5) |
| **Habitat** ||||
| 22 | Shell/pop-up/actuation | composite materials, PA-17 quad **(12V coil on this spine — wording fixed this pass)**, sync controller | ✅ |
| 23 | Climate (summer) | Midea 5K via 12/3000 + 12V blanket + side vent | ✅ |
| 24 | Water/sanitation | tanks, Shurflo, Bosch ES4, Nature's Head, shower box | ✅ |
| 25 | Galley/lighting/media | induction, 12V fridge, LED (12V — wording fixed), projector | ✅ |
| **Cross-cutting** ||||
| 26 | CAN visibility | Scan My Tesla + Model3CAN dash | ✅ |
| 27 | HV safety | isolation monitor, disconnect, fusing, in-pack pyro | ✅ |
| 28 | Weight/tongue governance | — | 🔧 CAD-carried; tongue ~350 lb at the Y's cap = design war #2 (Flagship Plan §3) |

## Verdict

**No missing purchasable parts remain.** The pass found and fixed: the missing **propulsion thermal loop** (the one true hardware gap — pack and DU inverter both need coolant on sustained assist), a **config bug** double-counting the 48V inverter in the flagship BOM, stale **48V wording** on actuators/backbone/lighting for the 12V-spine build, and an unstated **solar-at-12V ceiling** (now a warn rule).

What remains open is design/validation scope, each with an owner: controller firmware + patent review (SS07/Guide #4), DU subframe + force-coupler machining (SS05 CAD), 12V distribution detail (SS02), thermal loop sizing (SS07), dock connector + winter dock thermal + AHJ (SS08), Timbren rating confirmation (SS05), and the Phase-A bench gates (PCS 2 kW/1 hr; pack SoH; DU spin). Nothing blocks starting Phase A — the donor watch is already running.
