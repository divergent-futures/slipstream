# Salvage-First Architecture + V2H — Deep Research v0.1

**Date:** 2026-07-08 | **Method:** 2 research agents (~31 searches), verified [V] vs single-source [S] flagged per claim in transcripts | **Thesis (TJ):** salvage Tesla packs/drivetrains are absurdly cheap ($1,500–2K packs, growing crash supply), have huge remaining life, and a trailer is the safest, highest-value reuse vehicle — including winter duty as home overflow storage. This stream is the product's moat.

---

## 1. Donor organ reuse: what's mature, what's frontier, what's dead

| Donor system | Verdict | Path | Cost |
|---|---|---|---|
| **Battery pack** | ✅ Mature | Keep sealed, stock BMS, [Battery-Emulator](https://github.com/dalathegreat/Battery-Emulator) CAN interface | $1.5–4K pack + $70 |
| **Drive unit** | ✅ Maturing fast | Front (small) DU **$500–1,150** street; rear low-$1Ks. Open: [Maguire Model 3 DU logic board V3.2](https://github.com/damienmaguire/Tesla-Model-3-Drive-Unit) — supports front AND rear, tester-status, shipping ~Feb 2026. Commercial: [EV Controls T2-C](https://www.ev-controls.com/product/ev-controls-t2c/) (reflashes stock inverter, no teardown); Ingenext (support degraded, availability spotty) | $500–1,150 + board |
| **PCS (charger + 12V DC-DC)** | ✅ Works, semi-mature | [Maguire PCS controller](https://www.evbmw.com/index.php/evbmw-webshop/tesla-boards/tesla-model-3-pcs-con): AC in → ~11 kW pack charging, outside the car. Expect tuning; forum-supported | ~€100 board |
| **CAN visibility** | ✅ Solved (read) | [Model3CAN DBC](https://github.com/joshwardell/model3dbc) 3,000+ signals; Scan My Tesla ~$50–130 all-in; CANserver $190 (read-only by design) | <$200 |
| **HVAC / heat pump** | ⚠️ Frontier — skip for trailer | 2021+ Octovalve "SUPERMANifold" has **no CAN/LIN at all** — direct stepper/analog drive from the body controller; one open controller is WIP, compressor control unfinished ([openinverter thread](https://openinverter.org/forum/viewtopic.php?t=5361)). Trailer answer: our 48V RecPro heat pump is better anyway (native house-bus voltage). Keep watching the open controller for the bus project | — |
| **Center screen / MCU** | ❌ Dead end | FPD-Link serdes hacks, needs the car's gateway ecosystem behind it. Community answer: tablet + CAN dongle | — |

**Bus architecture (answers TJ's "open-source CAN that keeps systems going but controls the drive separately"):** the community-converged pattern is exactly that — **separate CAN buses per subsystem, never one shared donor bus**: drive-unit bus carries only inverter + shunt; [ZombieVerter VCU](https://github.com/damienmaguire/Stm32-vcu) (€350/750, open) is the master bridging drive, charger, DC-DC, contactors; Battery-Emulator handles the pack's dialect. No documented full "organ transplant" exists — Slipstream publishing one integrated, documented salvage stack **is the non-piecemeal win**.

## 2. V2H: the trailer as winter home battery — two-tier architecture

**Tier 1 — Generator-style (day one, ~$300–800 house-side).** Trailer's existing MultiPlus-II AC-out → cord → **NEMA 14-50 generator inlet + breaker interlock kit** ($50–200) on the house panel. NEC 702 optional-standby; the trailer is legally a cord-connected portable source — **no UL 9540 involved**. Precedent at scale: F-150 Lightning owners ran houses through exactly this during outages. Ceiling: our 3000VA = ~2.4 kW (essentials); a 48V house pack upgrade or the Tier-2 path lifts it. **Design lesson from the Lightning fleet: the #1 field failure is neutral-ground bonding tripping GFCI — the MultiPlus's switchable ground relay handles this properly; wire it as a selectable "house-feed mode."** Signage per NEC 702.7(C).

**Tier 2 — Seasonal AC-coupled dock (~$2,400+ house-side, Range-Neutral tier only).** Winter: trailer parks at the house, its **400V salvage pack plugs into a wall-mounted hybrid inverter** ([Solis S6-EH1P11.4K-H-US ~$2,400](https://www.ecodirect.com/Solis-11-400-Watt-220-240-VAC-Grid-Tie-Inverter-p/solis-s6-eh1p11.4k-h-us-rss.htm), 11.4 kW, native 120/240V, the community favorite) via Battery-Emulator. Gets: whole-critical-loads backup, **solar charging, TOU arbitrage** (charge cheap/solar, discharge 2–8 PM — documented DIY precedent), and the inverter itself charges the pack (no separate home charger needed). **Nobody has published a mobile-pack-that-docks-seasonally build — this is pioneer territory**, including the HV dock connector (surplus CCS/Amphenol HVIL class — open design item). Honest gray zone: pairing a listed inverter with an unlisted salvage pack breaks the system listing if the AHJ treats it as permanent ESS (NEC 706/UL 9540); the trailer's vehicle status + seasonal cord-connection is the Track-A argument, but no AHJ ruling exists on this hybrid case.

**Economics.** Average US home ~29 kWh/day → 75 kWh pack ≈ **2.6 days full-house, weeks of essentials** (Lightning outage baseline ~300–360W). OEM V2H benchmarks: Ford $3,895 HIS + install, GM $7,299 bundle, Tesla Powershare $1,990 + install — **the trailer undercuts all of them at Tier 1 and matches at Tier 2 while adding solar + arbitrage that OEM backup-only systems don't do.** Bonus to verify with a tax professional: Colorado Teardrops claims the **30% solar ITC applies to a camping trailer used as home battery backup** [S — marketing claim].

**Road-charging the propulsion pack** (away from the dock): Elcon/TC 6.6 kW charger (110–440 VDC out, **$1,850**) off any NEMA 14-50 pedestal; salvage Tesla PCS (~11 kW, €100 board, experimental); Chevy Volt charger hack (3.3 kW/unit, salvage-cheap, stackable, CAN heartbeat documented). NEC ceiling on a 50A circuit: 9.6 kW continuous.

## 3. Why this stream wins (the strategic frame, TJ 2026-07-08)

Supply is structural: more Teslas on roads + crash rate + no autonomy yet = growing salvage flow. A 75 kWh pack at $2K is **$27/kWh against $74/kWh for new DIY LFP cells and $225+/kWh for UL server racks** — and the pack arrives with contactors, pyro fuse, precharge, BMS, and cooling built in. The trailer is the ideal reuse chassis: outdoor storage (fire posture), suspension already rated, dual-use camping/home-power, and the aftermarket story ("your crashed Model Y becomes your trailer's heart and your house's winter battery") writes itself. What's missing industry-wide is the **integrated, documented, open stack** — every existing build is piecemeal. That integration doc set is Slipstream's contribution.

## 4. Feeds

- `engineering/SS08_Salvage_Donor_and_V2H.design.md` — design track
- `configurator/slipstream.config.json` — `home_power` fork (Tier 1/Tier 2), `hv_charging` fork, drive-unit parts refresh
- SS07 propulsion track — drive-unit pricing + Maguire V3.2 / T2-C decision point
