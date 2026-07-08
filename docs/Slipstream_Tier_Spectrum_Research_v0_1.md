# Slipstream Tier Spectrum — Deep Research v0.1

**Date:** 2026-07-08 | **Method:** 5 parallel research agents (~60 web searches), claims flagged verified (2+ independent sources) vs single-source | **Purpose:** ground every configurator tier — foamie to Range-Neutral — in real products, real prices, and real law. Feeds `engineering/SS07_Propulsion.design.md` and `configurator/slipstream.config.json`.

---

## 1. The Range-Neutral anchor: how Lightship actually does it

Lightship's L1 became the **AE.1** in Dec 2024; volume production since Aug 2025 (Broomfield, CO), ~$157,500 as configured in 2026 with a **77 kWh LFP** pack standard ([Lightship](https://lightshiprv.com/specs), [Electrek](https://electrek.co/2025/08/12/lightship-begins-us-production-ae-1-travel-trailer-two-additional-trims/), [Weekly Driver](https://theweeklydriver.com/2026/04/lightship-ae1-colorado-expansion-2026/)). The drive system, **TrekDrive**, is verified across Lightship, RVtravel, TFLtruck, and The Autopian:

- **Motor on the rear axle**, ~70–75 kW peak / ~20–30 kW continuous (never officially spec'd — deliberately *underpowered* against 8,300 lb GVWR as a safety posture)
- **Force sensors in the hitch coupler** — the controller reads push/pull force between the vehicles and commands torque to hold a small positive drawbar load. **No tow-vehicle data connection**; works behind gas, diesel, or EV
- **Speed-windowed**: assist engages ~15 mph, tapers out by 50–60 mph
- **Regen is triggered by the standard 7-pin trailer-brake signal** — no custom interface
- IMU + traction/stability-control-style supervision on top of the force loop
- Known wrinkle: weight-distribution hitches route load around the force sensor — WDH use is restricted

**Independently verified results:** TFLtruck's Denver loop: 19.66 MPG solo vs 19.42 MPG towing — zero penalty; the trailer burned 34% of 77 kWh over 115 mi ([TFLtruck](https://tfltruck.com/2025/09/video-this-camping-trailer-will-change-towing-forever-denver-100-mpg-loop/)). Rivian R1T owner data: 2.1 mi/kWh solo → 0.9 towing with TrekDrive OFF → **1.9 with it ON** ([Rivian Forums](https://www.rivianforums.com/forum/threads/real-world-efficiency-stats-towing-a-lightship-ae-1-with-a-rivian-r1t-gen1-quad.57441/)). Range-neutral is real — *while the trailer battery lasts (~250–300 mi), then it's a normal heavy trailer.*

**Competitors:** Pebble Flow beat Lightship to production (spring 2025): 45 kWh LFP, dual motors on one axle, $135,500 Magic Pack; control philosophy "always tension on the coupler — the tow vehicle always does more work than the trailer," app-settable arrival state-of-charge ([Autopian](https://www.theautopian.com/the-worlds-first-self-towing-camper-has-actually-gone-into-production/)). Dethleffs E.Home coco (ZF, Europe): drawbar force sensor, torque re-regulated within ~0.1 s to hold towed load at ~20 kg preset; crossed the Alps behind an Audi e-tron with zero charging stops; **never got general EU road approval** — powered trailers have no EU type-approval category. Airstream eStream stayed a concept. Colorado Teardrops Boulder = battery-only range extender, no motor.

**The convergent control architecture (all three systems):** (1) sense force at the coupling, (2) closed-loop torque to a small always-in-tension setpoint — trailer never pushes the tug, (3) underpower deliberately, (4) speed-window the assist, (5) IMU/ESC supervision, (6) regen via the brake signal, (7) free-wheel when dead. This is the SS07 design spec.

## 2. Salvaged Tesla packs: what's actually true

- **LR 2170 pack (Model 3/Y): 96s46p, 4,416 cells, ~355 V nominal, 78 kWh gross / ~75 usable, ~479 kg (1,054 lb)** — verified ([Electrek teardown](https://electrek.co/2017/08/24/tesla-model-3-exclusive-battery-pack-architecture/), [BatteryDesign.net](https://www.batterydesign.net/benchmark/tesla/)). Four glued/welded modules (2×25s + 2×23s) — **not practically separable**; the pack is reused whole.
- **SR/RWD LFP packs (2021+): CATL prismatic, 55–60 kWh, 106s/108s, ~438 kg** — the cheaper, safer-chemistry salvage option.
- **Avoid Austin 4680 structural packs** — foam-potted, non-serviceable, lower capacity (~67 kWh).
- **Street prices are stunning:** used LR packs **$1,499–$1,999** on eBay (~$20–27/kWh); newer packs to $5,499 ([eBay](https://www.ebay.com/b/Tesla-Car-and-Truck-Batteries/177703/bn_20278056)). Single-source aggregation; SoH varies — budget $2,000–4,000 + freight for a graded pack.
- **BMS strategy (community-verified default):** keep the pack sealed, keep the stock Tesla BMS, talk to it over CAN. Model 3/Y cell monitoring uses a proprietary ISO-SPI ("Batman" chip) incompatible with standard BMS hardware — re-BMSing is the wrong path. The dominant tool is **[Battery-Emulator](https://github.com/dalathegreat/Battery-Emulator)** (open source, ~$40–70 LilyGo ESP32-CAN board): closes contactors, reads the BMS, emulates a BYD HV battery. Alternative: Damien Maguire's open **[M3 BMS controller](https://www.evbmw.com/index.php/evbmw-webshop/tesla-boards/tesla-model-3-bms)** (€100 + harvested Batman chip). The pack's penthouse already contains contactors, precharge, and the pyro fuse — keeping it intact inherits Tesla's HV safety hardware.
- **The 400V→48V wall:** OEM DC-DCs (Tesla PCS) output 12 V only (~2.5 kW). Victron tops out at 400 W and low input voltages. True 400V-input/48V-output converters are industrial, quote-priced, realistically **1–3 kW ceiling**. **Architecture consequence: the propulsion pack and the 48V house system stay separate.** House stays on the 12 kWh LFP spine; the Tesla pack feeds the drive inverter; an optional small industrial DC-DC gives a 1–2 kW trickle from propulsion→house. (The grid-storage community solves this by AC-coupling via HV hybrid inverters — wrong tool on a moving trailer.)
- **HV safety non-negotiables:** precharge before contactor close, intact HVIL loop, intact pyro fuse (never bus-bar it), Class-0 gloves + one-hand rule, isolation monitoring. All standard practice, all documented in the sources.

## 3. Drivetrain + control: the open-source path

**DIY prior art exists** — "pusher trailers" from the 2000s EV community (Mr. Sharkey's half-Civic pusher, EVAlbum #304) used crude interlocks (brake-pedal switch cuts thrust). The refinement everyone proposed but rarely built — **a hitch that measures push/pull force as the control input** — is exactly what Lightship/Pebble/ZF productized, and it's patented territory to study, not copy: [US 11,642,970](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11642970) (per-wheel motors + 3-axis coupling force sensor), [US 12,162,363](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12162363) (dynamic tow + regen). An open-source implementation must design around these claims — flag for legal review before publishing the controller repo.

**Motor/inverter decision matrix (10–30 kW class for a ~3,000 lb trailer):**

| Path | Parts | Est. cost | Verdict |
|---|---|---|---|
| **Tesla SDU + openinverter** (400 V native) | Salvage small drive unit (~63 kg motor + 12 kg inverter, to 220 kW) + open logic board ([Westside EV ready-to-run](https://www.westside-ev.com/store/p/ready-to-run-tesla-front-small-drive-unit-for-ev-build-openinverter-jailbroken), [EVBMW boards](https://www.evbmw.com/index.php/evbmw-webshop/tesla-boards)) | ~$2,000–3,500 | **Lead.** Voltage-matched to the salvage pack, absurd power margin (software-limited), mature open-source control, one e-axle-like unit |
| Prius Gen3 inverter + PMAC motor (chain to live axle) | Salvage inverter + $300 openinverter logic board + ME1616 (~20 kW cont.) | ~$2,500–4,000 | Viable Tier-A alternative; more fabrication |
| HPEVS AC-34 + Curtis kit (48–108 V) | Complete kit $3,657–4,826 ([canEV](https://shop.canev.com/products/curtis-1236se-5621-hpevs-ac-34-brushless-ac-motor-kit-48-volts)) | ~$4,500 | Turnkey but voltage-mismatched to a Tesla pack — needs its own LV pack |
| QS hub motors (2×8 kW) | ~$750–1,100 each + Fardriver | ~$2,500 | Unsprung mass + moto bearings vs trailer loads — same reason we rejected hubs on the bus |
| VESC 75/300 | £300 | — | Tops out ≤100 V; can't run a Tesla pack |

**Supervisor:** ZombieVerter VCU (open source, €350 kit/€750 built) manages contactors, precharge, inverter CAN, charging — purpose-built for exactly this stack.

**Brakes + regen (the legal architecture, verified):** electric drum brakes stay, wired to the tow vehicle's controller — they are the legal service brake. Breakaway switch must apply friction brakes and hold **15 minutes** (49 CFR 393.43) — regen can't do that. Regen rides on top as throttle-off "Category A" braking commanded by the trailer's own controller, cut whenever the brake signal is present. Brake thresholds: most states 3,000 lb, **CA/ID/NV/NH/OR at 1,500 lb**, TX 4,500 — so every Slipstream above the foamie gets brakes + breakaway by design.

## 4. Regulatory posture (US)

- **Federal:** 49 CFR 571.3 defines a trailer as a motor vehicle "**with or without motive power**, designed... for being drawn by another motor vehicle." NHTSA's 1985 interpretation letter ([1985-03.21](https://www.nhtsa.gov/interpretations/1985-0321)) classified a motorized pusher axle as a *trailer*. Lightship and Pebble both register their products as travel trailers and are delivering in the US. Applicable FMVSS for trailers: 108 (lighting), 119/120 (tires/rims), VIN + cert label — **no crash standards, no standard for electric trailer brakes**.
- **The design rule that keeps trailer status:** propulsion assists **only while hitched** (hitch always in tension, tow vehicle always does more work); unhitched movement limited to walking-speed remote maneuvering; free-wheels when dead.
- **Home-built path is well-trodden in every state checked** (CA/TX/FL/WA/CO): component receipts → state VIN inspection (CHP/State Patrol/DMV examiner) → assigned VIN → certified weight slip → register. CA = SPCNS/PTI; TX title optional ≤4,000 lb; WA even publishes a homemade-RV inspection guide.
- **Honest gray zones:** (a) no precedent for a *home-built* powered trailer at a state inspection desk — inspector discretion; (b) insurance for a powered homebuilt is unwritten territory (insurers extend tow-vehicle liability to trailers *because they have no engine*); (c) unhitched road propulsion would break the trailer classification. The configurator's Range-Neutral tier carries these as standing warnings.

## 5. The low end, validated

- **Foamie method (tnttt.com-verified):** 2" XPS shell, no wood frame, Gorilla Glue joints, skinned in Poor Man's Fiberglass (canvas + Titebond II + exterior paint — the paint is structural). Real weights: **350–550 lb all-up**; real costs **under $1,500 DIY**; ~50 build-hours vs ~250 for a stitch-and-glue plywood kit. Durability: 10-year outdoor reports; dents self-heal with heat; puncture resistance is the accepted weakness.
- **Standard base:** Harbor Freight 4x8 folding trailer (~$300–400, 1,195 lb capacity, 253 lb) + known upgrades (radial tires, Dexter EZ-Lube axle).
- **Where beginners fail — and what a kit must therefore include:** doors (warp, seal), window installation, hatch sealing (hurricane hinge), and glue chemistry conflicts. Consensus parts source: **Vintage Technologies** (teardroptrailerparts.com) — insulated door pairs, RV windows ~$122–142, hurricane hinges.
- **Kit spec that falls out of the data:** HF trailer + CNC-cut 2" XPS panel set + Vintage Tech doors/window + hurricane hinge + PMF pack + vent fan ≈ **$2,500–3,500 and 350–550 lb** — undercutting the CLC kit ($2,995 kit-only) at 1/5 the build hours. This is the Foamie tier product.
- **Middle-tier lessons:** Polydrops P17A (1,200 lb, $25–46K) proves flat structural panels + angular geometry = CNC-friendly kit, and battery-flat-in-frame; Earth Traveler proves foam-cored monocoque scales upmarket (claims unverified — no independent weights); Bowlus (5,000 rivets, $265K) is the anti-kit cautionary tale; Airstream Basecamp ($48K/2,700 lb) marks the conventional floor Slipstream undercuts.

## 6. What this changes in the configurator

1. **Two-battery architecture for Range-Neutral** — new `propulsion_pack` fork (Tesla 2170 LR ~75 kWh/1,054 lb, or CATL LFP 55–60 kWh/~966 lb), separate from the 48V house battery. Propulsion requires its own pack; the house spine is untouched.
2. **Real numbers** — pack $2–4K salvage, SDU+openinverter ~$2–3.5K, interface electronics ~$500–1,000; drums stay; hitch load-cell + controller.
3. **Foamie effects re-based** to verified weights/costs.
4. **Standing warnings** — powered-homebuilt registration/insurance gray zones; WDH incompatibility with hitch-force sensing; patent-clearance flag on the open controller.

*All agent source lists preserved in the research transcripts; key URLs inline above.*
