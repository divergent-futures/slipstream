# SS07 — Propulsion (Range-Neutral tier) · Design Track

**Status:** Detailed v0.1 (research-grounded, pre-build) · **Sequence:** ~~after V1.0 of the base trailer~~ **THIS IS BUILD #1** (Flagship-First pivot, TJ 2026-07-08 — see `docs/Flagship_First_Build_Plan_v0_1.md`: ≤3,500 lb loaded behind the Model Y, CATL LFP pack preferred, no 48V house pack — 12V spine off the donor PCS)
**Traces to:** configurator Range-Neutral tier · **Research basis:** `docs/Slipstream_Tier_Spectrum_Research_v0_1.md`
**Design thesis:** the Lightship/Pebble/ZF-Dethleffs control architecture, executed open-source with salvage Tesla hardware, published as its own community repo.

## 1. Purpose & requirements

A trailer that pushes its own weight so the tow car loses ≈0% range while the trailer battery lasts. Requirements: assist only while hitched (hitch always in tension — trailer never pushes the tug) · no tow-vehicle data connection (works behind any car) · speed-windowed assist (~15 mph engage, taper out by 50–55 mph) · regen commanded by the standard 7-pin brake signal + throttle-off · free-wheels dead · friction service brakes fully retained · deliberately underpowered (~20 kW continuous is plenty against ≤3,500 lb).

## 2. Architecture (two batteries, by necessity)

```
[Salvage Tesla pack ~355V] ──HV──> [Drive inverter + motor (rear axle)]
      │ (stock BMS kept, CAN via Battery-Emulator/LilyGo)
      └──(optional 1-2 kW industrial DC-DC)──> [48V house bus (SS02), unchanged]
[Hitch force sensor + IMU] ──> [Drive controller (open repo)] ──> torque command
[7-pin brake signal] ──> drums (legal service brake) + regen cut-in
```

The 400V→48V conversion wall (no affordable >3 kW converter exists) means the house system stays exactly as designed in SS01/SS02. The propulsion pack is an *addition*, not a substitution. Pack mass (~1,000 lb) is why this tier needs the 15–18' box, tandem-axle option, and a tow vehicle rated well above Model Y class — or acceptance that the assist itself carries the weight (Lightship's answer; hitch/brake ratings still apply).

## 3. Component stack (researched street prices)

| Block | Choice (lead) | Est. |
|---|---|---|
| Propulsion battery | Salvage Model 3/Y LR 2170 pack, kept whole, penthouse intact (contactors/precharge/pyro) | $2,000–4,000 |
| — alt | CATL LFP 55–60 kWh pack (2021+ SR) — cheaper, safer chemistry, ~90 lb lighter | $1,500–3,000 |
| BMS interface | Battery-Emulator on LilyGo T-CAN485 (open source) | ~$70 |
| Motor + inverter | Salvage Tesla SDU + openinverter logic board (ready-to-run available) — software-limit torque | $2,000–3,500 |
| — alt | Prius Gen3 inverter + openinverter board + ME1616 PMAC, chain to live axle | $2,500–4,000 |
| Supervisor | ZombieVerter VCU (contactors, precharge, CAN, charge control) | €350–750 |
| Force sensing | Hitch coupler load cell (3-axis preferred) + IMU; custom controller board | $300–800 |
| Brakes | Standard electric drums + breakaway (retained from SS05) — regen is Category-A overlay only | (SS05) |
| HV plumbing | Cabling, service disconnect, isolation monitor, fusing | $500–1,000 |

**Tier component total ≈ $6,000–10,000 over the base trailer** — dramatically under the earlier $9K drivetrain-alone placeholder, courtesy of the salvage market ($20–27/kWh packs).

## 4. Control loop (the open-source repo's core)

1. **Primary:** hitch force sensor → PI loop holding small positive drawbar tension (ZF/Dethleffs: setpoint ~20 kg, torque update ≤100 ms)
2. **Envelope:** zero torque below ~15 mph and above ~55 mph; ramp limits; torque ceiling scales with speed
3. **Regen:** brake-signal present → regen at calibrated level, drums do the legal work; throttle-off coast regen mild
4. **Supervision:** IMU sway detection cuts assist (assist during oscillation feeds sway); WDH detection note — weight-distribution hitches bypass the force sensor, must be excluded
5. **Fail-safe:** any sensor fault, CAN loss, HVIL break, or 7-pin disconnect → contactors open → free-wheeling trailer
6. **Never** propel unhitched beyond walking-speed maneuvering (regulatory line — see §5)

## 5. Regulatory + legal posture

- 49 CFR 571.3: trailer = motor vehicle "with or without motive power" designed for being drawn → hitched-assist keeps trailer classification (NHTSA 1985 SPU interpretation letter is the precedent; Lightship/Pebble register as trailers)
- Friction brakes + breakaway (15-min hold, 49 CFR 393.43) are non-negotiable; regen never substitutes
- Home-built powered trailer at a state VIN inspection = untested; expect inspector discretion. Document everything; CA (SPCNS) and WA (homemade-RV guide) are the best-documented paths
- Insurance for a powered homebuilt is unwritten — carry as a standing configurator warning
- **Patent clearance before publishing the controller repo:** US 11,642,970, US 12,162,363/12,416,536, US 12,187,133 cover coupling-force-controlled powered trailers. Design-around review is a gate for the public repo.

## 6. Open questions

0. **RESOLVED direction (2026-07-08, Guide #3 research):** controller path = **Maguire M3-DU V3.2 / openinverter** — the trailer is headless (no pedal, no vehicle-plausibility signals) and needs continuous CAN regen commands; EV Controls T2-C stock firmware "detects there is no vehicle attached" and is unfit for trailer duty. V3.2 is tester-grade (shipped Mar 2026, no independent field reports yet) — bench-validate hard. **New design driver: PMSM back-EMF** — the rear DU's DC link is live whenever the trailer rolls; contactor/interlock/service design must assume energized-when-moving. Gearing confirmed: 9.036:1, ~6,450 motor RPM at 65 mph on 30.6" trailer tires — the complete DU is the e-axle, no extra reduction. **Trade study opened: induction FRONT unit** (no magnets = no back-EMF when towed = safer dead-trailer; newer board support, lower efficiency).
1. SDU torque-limiting calibration — how low can openinverter cleanly cap a 220 kW unit for a 20 kW duty?
2. Load cell spec: 3-axis (sway-capable) vs single-axis tension/compression + IMU fusion
3. Charging the propulsion pack: shore NEMA 14-50 via salvage Tesla PCS (Maguire controller exists) vs CCS via openinverter — or solar-only trickle?
4. Tandem axle requirement at +1,000 lb pack — SS05 frame rework scope for this tier
5. Patent design-around strategy (open publication is the goal; the force-control claims are broad)

---
*Detailed 2026-07-08 from Tier Spectrum Research v0.1. This tier proceeds only after the base trailer proves itself (V1.0 gate) — same discipline as the bus's V2.0 wall.*
