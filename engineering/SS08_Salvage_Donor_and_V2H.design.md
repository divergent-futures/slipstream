# SS08 — Salvage Donor Integration & V2H · Design Track

**Status:** Detailed v0.1 (research-grounded) · **Sequence:** with SS07 (same tier) + Tier-1 V2H applies to EVERY Slipstream from V0.5 on
**Traces to:** salvage-first strategy (TJ, 2026-07-08) · **Research basis:** `docs/Slipstream_Salvage_V2H_Research_v0_1.md`
**Design thesis:** one documented, integrated, open salvage stack — pack, drive, charging, home-power — where every existing build is piecemeal.

## 1. Purpose & requirements

Make the salvaged Model 3/Y pack + drive unit a *first-class, reproducible* subsystem, and make the trailer's battery useful 12 months a year: camping in summer, **home overflow storage in winter**. Requirements: pack stays sealed (stock BMS, contactors, pyro, cooling) · every donor interface open-source or commercially available · house-side hardware code-legal (NEC 702 path) day one · seasonal dock upgrade path defined · no donor system kept alive that has a better native-48V answer (HVAC stays RecPro).

## 2. The salvage stack (canonical build)

```
DONOR: crashed Model 3/Y (2170 LR or CATL LFP pack; avoid Austin 4680)
├─ Pack (sealed, penthouse intact) ──CAN── Battery-Emulator (LilyGo, $70)
├─ Rear drive unit ($1-2K) ── Maguire M3-DU logic board V3.2 (open, Feb 2026)
│                              or EV Controls T2-C (commercial, no teardown)
├─ PCS (in penthouse) ── Maguire PCS controller (~€100) → ~11 kW shore charging
└─ NOT reused: heat pump manifold (no CAN - direct actuator drive; WIP open
   controller unfinished), screen/MCU (tablet + CAN dongle instead)

CAN DOCTRINE: separate buses per subsystem. Drive bus = inverter + shunt ONLY.
ZombieVerter VCU = master (contactors, precharge, charger, DC-DC, mode logic).
Monitoring: Model3CAN DBC (3,000+ signals) via Scan My Tesla / custom dash.
```

Drive-unit choice: **rear DU preferred** (best support in both Maguire V3.2 and T2-C); front SDU is the budget option ($500–1,150) with newer board support. Decision point for SS07's build: V3.2 board maturity vs T2-C cost — revisit when V3.2 ships (~Feb 2026 + field reports).

## 3. V2H Tier 1 — "generator mode" (ships with every trailer)

- Trailer side: MultiPlus-II AC-out-2 → dedicated exterior outlet; **ground relay configured for selectable house-feed mode** (the Lightning fleet's #1 field failure is N-G bond GFCI conflicts — we solve it in config, not adapter hacks)
- House side (owner kit, ~$300–800): NEMA 14-50 inlet + panel interlock (NEC 702.5 listed-for-panel) + 702.7(C) signage + cord
- Capacity honesty: 3000VA spine = ~2.4 kW continuous → essentials (fridge, lights, comms, furnace fan ≈ 300–800W typical). 5000VA fork → ~4 kW. House pack (12–16 kWh) = 2–5 days essentials; add solar recharge
- **This works on ANY Slipstream with the 48V spine — not just Range-Neutral.** It's a configurator option, not a tier

## 4. V2H Tier 2 — seasonal dock (Range-Neutral tier)

- House side: Solis S6-EH1P11.4K-H-US (~$2,400, 11.4 kW, UL 1741) on a critical-loads panel; Battery-Emulator wall node
- Trailer side: HV dock connector on the propulsion pack circuit (surplus CCS inlet or Amphenol HVIL-class — **open design item #1**; nobody has published a seasonal-dock standard)
- Winter duty: solar charging + TOU arbitrage (charge off-peak/solar, discharge evening peak) + outage backup — 75 kWh ≈ 2.6 days full-house
- Charging away from dock: Elcon TC 6.6 kW ($1,850) or donor PCS (~11 kW, experimental) or Volt-charger stack (budget)
- Regulatory posture: cord-connected seasonal vehicle = NEC 702 argument; permanent-ESS treatment (NEC 706/UL 9540) is the gray zone — document the AHJ conversation, publish the first ruling we get. ITC angle (30% solar credit for dual-use trailer, Colorado Teardrops precedent) — **verify with tax professional before claiming in any DF material**

## 5. Interfaces

- **T1/SS02:** Tier-1 V2H is pure SS02 (MultiPlus config + outlet); zero new trailer hardware
- **SS07:** shares pack, contactor doctrine, ZombieVerter; SS08 adds dock circuit + charge sources
- **T9:** Cerbo shows house-feed mode + pack SoC; VRM = remote monitoring of the house feed from the ski trip

## 6. Open questions

1. HV dock connector standard (CCS inlet reuse vs industrial HVIL) — safety review required
2. Maguire V3.2 vs T2-C decision (wait for V3.2 field reports)
3. Donor PCS as primary road charger vs $1,850 Elcon (PCS is free-with-pack but experimental — bench both?)
4. Pack thermal in winter dock duty (pack heater draw vs garage ambient; Tesla BMS handles it — verify via Battery-Emulator logs)
5. AHJ engagement strategy: get one written determination on the seasonal-dock classification, publish it
6. ITC dual-use claim verification (tax professional)

---
*Detailed 2026-07-08 from Salvage/V2H research v0.1. Tier-1 V2H should be validated during V0.5's shore-power testing — it's nearly free to add.*
