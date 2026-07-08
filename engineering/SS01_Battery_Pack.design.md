# SS01 — Battery Pack (12 kWh-class, 48V LFP) · Design Track

**Status:** Detailed v0.1 · **Sequence:** 1 · **Depends on:** frame rail cross-section (SS05)
**Traces to:** Roadmap I.2 #3 (12 kWh LFP frame-integrated), Decision log D4 · **Feeds V0.1 Gate 1:** ≥11.5 kWh usable, 50A continuous discharge, BMS protections verified.

## 1. Purpose & requirements

One battery, in the frame, below the floor. Sized for ~2 hot-AC nights + 4+ mild days off-grid; low CG; zero interior volume cost. Requirements: ≥11.5 kWh usable · 48V nominal · ≥50A continuous discharge (2.5 kW sustained, 3 kVA inverter surge via headroom) · charge from MPPT (solar), MultiPlus (shore), sub-freezing charge protection · survive road vibration + stone strikes.

## 2. Interfaces

- **T1** → SS02: 48V bus via Class-T fused disconnect; BMS talks CAN/RS485 to Cerbo GX
- **T6** → SS05: pack cradle between frame rails, aft of axle option pre-engineered (tongue-weight lever, risk R1)
- **T8**: pack sits outside the cabin envelope — needs its own insulation + heater pad for winter charging
- **T10**: pack case bonded to chassis; 48V negative single-point bond (mirrors House BUS grounding doctrine)

## 3. Components (researched — Sourcing doc §3 + cell research 2026-07)

| Item | Spec | Est. | Notes |
|---|---|---|---|
| 16× EVE LF280K V3, Grade A | 3.2V 280Ah prismatic, ~8,000 cycles | ~$66/cell ≈ **$1,060** | [GobelPower ~$66](https://www.gobelpower.com/ev-grade-a-eve-32v-280ah-rechargeable-lifepo4-battery-cell_p102.html); US stock via [Docan](https://www.docanpower.com/eve-280ah-v3-raw-cell-us-stock), [18650BatteryStore](https://www.18650batterystore.com/products/eve-lf280k) |
| JK PB2A16S20P BMS | 16S 200A, 2A active balance, CAN/RS485, Bluetooth | ~$250 | [Kit reference $528 w/ case](https://www.gobelpower.com/eu-stock-48v-16s-lifepo4-battery-pack-diy-kit-case-with-jk-bms_p217.html) |
| Custom slim enclosure | Al sheet + internal compression fixture, IP67 target | $800–1,500 | The real cost; welded or folded + gasketed |
| Heater pad + thermostat | 48V silicone pad under cells, BMS-interlocked | ~$100 | Charge lockout below 0°C regardless |
| Class-T fuse + holder, disconnect, busbar | 200A class | ~$250 | |

**Pack math:** 16S × 3.2V × 280Ah = **14.3 kWh nameplate** → ~12.9 kWh usable at 90% DoD — clears the 11.5 kWh gate with ~12% margin (cell fade + cold headroom). Mass: 16 × 5.42 kg ≈ 87 kg cells + ~18 kg enclosure/BMS/wiring ≈ **~230 lb** vs. ~200 lb budget line — SS05 mass table carries 230 lb; recover elsewhere or accept (still under envelope).

**Cell geometry vs. frame:** LF280K is 207 mm tall × 173.7 × 71.7 mm. Upright = 8.2" — exceeds the 5–6" rail depth assumption. Options: (a) cells on their side (71.7 mm ≈ 2.8" tall, footprint grows to ~16 cells × 174×207 mm ≈ a 0.58 m² blanket — fits a 78"-wide belly), or (b) accept an 8.5" pack zone amidships with a shallower floor recess. **Leaning (a) side-lay** — thinnest pack, lowest CG, true skateboard. Open question #1 validates side-lay cycle life (EVE permits side orientation with proper compression fixturing; confirm against V3 datasheet).

## 4. Load & autonomy check

5 kWh/hot-night AC budget (roadmap) → 2 nights ≈ 10 kWh < 12.9 usable ✓. Mild-day load ~3 kWh/day vs ~4.5 kWh/day solar harvest (1,050W × ~4.3 eq-hrs) → solar-positive, 4+ day claim holds.

## 5. Open questions

1. Side-lay orientation approval + compression fixture design (EVE datasheet / distributor query)
2. 230Ah vs 280Ah cells if mass budget tightens (11.8 kWh nameplate — thin gate margin, probably no)
3. Enclosure fabricator: same shop as frame (SS05) or separate sheet-metal vendor?
4. BMS ↔ Cerbo integration path: JK CAN profile vs. Victron-native shunt (SmartShunt ~$130 as belt-and-braces)

## 6. V0.1 bench plan

Assemble on bench in enclosure → capacity test (C/2 to 11.5 kWh usable) → 50A continuous 2 hr → BMS protection walk (OV/UV/OT/UT/short) → heater-pad interlock test → then integrate with SS02 for the 7-day gate.

---
*Detailed 2026-07-07. Cell prices are street; re-quote at purchase. Mass table update owed to SS05.*
