# Pack Commissioning Guide — Salvage Tesla Model 3/Y + Battery-Emulator

**v0.1 · 2026-07-08 · Slipstream open-source build series · Guide #2**
**What this is:** the bridge from "pack on a cradle" (Guide #1: Donor Procurement & Teardown) to "pack alive, talking, and safe to build around." Follow-along with go/no-go gates. Authority sources: the [Battery-Emulator wiki](https://github.com/dalathegreat/Battery-Emulator/wiki) (especially the [Tesla page](https://github.com/dalathegreat/Battery-Emulator/wiki/Battery:-Tesla-Model-S-3-X-Y)) — read both before starting.

> **⚠️ Same three rules as Guide #1.** The pack is always live inside (350–400 VDC). You never open the pack — the *penthouse cover* is the one exception, for pyro fuse service only, gloves on. One hand, insulated tools, buddy nearby.

---

## Phase 0 — Shopping list (~$250 total, excluding 12V supply)

- [ ] **LilyGo T-2CAN** (recommended: dual isolated CAN — pack + inverter later) or T-CAN485 (~$40–70)
- [ ] **X098 mating plug** — Sumitomo 6189-7077 13-pin (AliExpress, or better: **harvest the pigtail from your donor** before it goes)
- [ ] **HVIL resistors**: 60 Ω (RWD pack) AND 120 Ω (AWD pack) — a few of each, ¼W is fine
- [ ] **Precharge dummy load: 650–1,000 µF, 500V electrolytic capacitor** (simulates the drive unit the pack expects to precharge)
- [ ] **12V supply that can source 30+ A**: a healthy car battery on a maintainer, or a 30 A bench supply (12–16V). This is NOT optional — the PCS pulls 30+ A during contactor close; a wall-wart means contactors never close
- [ ] **6 AWG (≥13 mm²) cable** for the 12V run to the PCS studs — thin wire is the #1 silent failure
- [ ] Spare **pyro fuse** p/n 1064689-00(-J) (~$29–60, Amazon/eBay) if your donor had airbag deployment
- [ ] **Torx Plus 10EPR socket** (pyro service) + 13 mm socket
- [ ] HV harness for later drive-unit hookup: Tesla p/n **1109000-00-D** (rear-DU HV harness — Ingenext/eBay); jumper plugs/resistors for **every unused HV connector's HVIL loop**
- [ ] Shielded twisted pair for CAN, 120 Ω termination resistor, DC fuse (ceramic gBat class) for the eventual inverter run
- [ ] PPE from Guide #1 (Class-0 gloves, face shield, CAT III/IV meter)

## Phase 1 — Flash and configure Battery-Emulator (pack not connected yet)

1. Flash via the **web installer** (Chrome/Edge): `dalathegreat.github.io/BE-Web-Installer` → erase → flash the factory image for your board.
2. Power the board, join WiFi AP **`BatteryEmulator`** (pw `123456789`), browse to `192.168.4.1`.
3. Settings page:
   - Battery Protocol = **Tesla Model 3/Y**
   - **Pack size and donor country set correctly** (wrong = fault codes on the battery side)
   - LFP pack? Set **Battery chemistry = LFP manually** (autodetect takes ~5 min; brief overcharge risk at true 100%)
   - **2024+ (Highland-era) donor? Tick "Digital HVIL (2024+)"** or contactors will never close
   - **No inverter protocol selected yet** — first contact is battery-only
   - Set manual charge/discharge power to match your future inverter (e.g., 6000 W)
4. Enable general logging (USB serial / webserver) — you want to see the BMS's exact complaints later.

## Phase 2 — Pyro fuse service (only if fired — airbag-deployment donors)

🧤 Gloves + face shield. Penthouse cover off (Torx Plus 10EPR).
1. **Expect 100–180 V between the pyro terminals** (the fuse splits the pack; sagging under the meter is normal). This is why gloves.
2. Old fuse out (13 mm bolts), new 1064689-00 in, seated firmly. The two small sense pins must read **~1.8–2 Ω** (squib resistance) — the BMS checks this at every start.
3. **Never bridge the fuse with a bar** — the sense circuit will refuse it, and you'd be deleting the pack's main overcurrent protection.
4. Cover back on. (A pack reading ~1 V total with healthy per-cell voltages = the pyro is blown — diagnose here, not at the cell level.)

## Phase 3 — First contact (read-only; no contactors)

Wire X098 (pin cavities are numbered to 18; not all populated):

| X098 pin | Function | Your wiring |
|---|---|---|
| 1 ↔ 3 | HVIL loop | **60 Ω resistor (RWD) / 120 Ω (AWD)** across them |
| 8, 18 | +12V in | From your 30 A-capable supply |
| 9 | GND | Supply return |
| 16 / 15 | CAN-H / CAN-L | Shielded pair to LilyGo (pack is internally 120 Ω terminated; terminate your end per bus layout) |

Also: 6 AWG 12V run to the **PCS 12V studs** (two M8 near X098); if the penthouse lid is off, ground the bolt holes flanking X098; **jumper the HVIL loops on every unused HV connector** (front-DU, AC-charge) or the pack refuses to start.

**Go/no-go gate:** web UI shows SoC, pack voltage, **per-cell voltages and temps** — with contactors still open. Re-run Guide #1's health gates on better data: cell spread <100 mV, no stored faults, sane temps. (One community user caught a 500 mV dead cell at exactly this step — before wasting another dollar.) Fail → the pack is parts. Pass → Phase 4.

## Phase 4 — First contactor close

1. **Hang the 650–1,000 µF/500V capacitor across HV+/HV−** at the output connector (verify polarity: 1 = −, 2 = +). The pack's internal PCS does its own precharge (0→350 V in ~1 s) and *must see a capacitance charging* or it aborts. No capacitor = no close. (Packs missing the PCS can't self-precharge — different, hairier procedure; see BE issue #429.)
2. Clear the area of the curious. Gloves for anything near HV.
3. Web UI → **Close Contactors**. Listen for the clunk; UI shows pack voltage on the output.
4. **Verify at the meter (gloves, one hand): full pack voltage across the capacitor.** Congratulations — the pack just took its first breath outside the car.
5. Open contactors. Note the keep-alive draw (10–20 W steady-state is normal).

**If contactors won't close, in order of likelihood:**
- 12V sagging during close (UI stuck at "STATUS: Contactor: CLOSING", LV reading ~9 V) → your supply/cabling is undersized
- HVIL: wrong 1–3 resistor (swap 60↔120 Ω), unused HV connectors not jumpered, penthouse lid open
- "Pyro connection check" / squib error → fuse not seated (wants 1.8–2 Ω on sense pins)
- 2024+ pack without the Digital HVIL checkbox
- Contactors cycling open/close every 30–60 s → hard-reset the pack: unplug X098 AND PCS 12V for ≥1 min
- Read the log — the BMS names its objection (e.g., `BMS_a083_SW_Ctr_Close_Failure`)

## Phase 5 — Operating notes (the stuff that bites later)

- **Bond the pack case to protective earth.** The (future) inverter's isolation monitoring only protects you if the case is earthed; unearthed = HV leakage goes undetected + ground loops eat CAN transceivers.
- **Balancing quirk:** Tesla packs balance only with **contactors OPEN at ~99% SoC** (~2 mV/day), and the pack does NOT charge your 12V supply in that state — keep the maintainer on. LFP packs: use BE's "Manual LFP balancing" mode periodically.
- **Thermal:** low-power stationary duty needs **no coolant flow** in temperate weather (BE faults itself >50 °C / <−25 °C). Don't open the coolant loop casually — the fittings are brittle single-use parts.
- **Storage between sessions:** contactors open, ~30–50% SoC, outdoors/detached, 12V maintainer on.
- **First real load:** capacitor test → then straight to the hybrid inverter (SS08 Tier 2) through a ceramic DC fuse, polarity triple-checked ("many EV batteries have no markings"). No polarized DC breakers. For the trailer's drive system, the 1109000-00-D harness feeds the drive unit (SS07).
- Double-battery (two packs in parallel): Tesla 2020+ support is still in testing in BE — not a stable platform yet; plan single-pack.

## STOP conditions

| Condition | Verdict |
|---|---|
| Cell spread >100 mV or stored BMS damage faults at Phase 3 | Pack = parts; do not proceed to contactor close |
| >10 V across pyro terminals *after* claimed pack disconnect steps | Re-read Phase 2 — that voltage is normal AT the pyro; anywhere unexpected = stop and re-verify |
| Contactors close but isolation warnings appear under load | Earth-bond + isolation hunt before any further use |
| Temptation to solder the internal HVIL defeat | Don't. It permanently blinds the pack's unplug detection. |

**Next in series:** Guide #3 (planned) — drive unit bench bring-up (Maguire M3-DU board / EV Controls T2-C). Then SS08 Tier-2: first dock to the house inverter.

*v0.1 — sourced against the Battery-Emulator wiki and community issue tracker, July 2026. The wiki evolves; when this guide and the wiki disagree, the wiki wins.*
