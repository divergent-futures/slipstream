# Slipstream — Component Sourcing v0.1

**Date:** 2026-07-07 | **Owner:** TJ | **Status:** Web-researched, pre-quote
**Purpose:** Resolve the open supplier forks from the handoff doc (§9) with real parts and street prices, and feed the configurator's BOM output. All prices US street, first-order; quotes supersede.

---

## 1. Pop-up actuators (fork resolved → new `actuators` fork)

**Finding: true 48V COTS actuators are scarce.** Progressive Automations' heavy-duty line (PA-17: 2,000 lb dynamic, strokes to 30-40", IP65) is 12/24V only — [~$350-477 each](https://www.progressiveautomations.com/products/heavy-duty-linear-actuator) depending on stroke ([PA-17-8-2000 at ~$350](https://linactuat.com/pa-17-8-2000), [30" stroke listed at MROSupply](https://www.mrosupply.com/linear-motion/6454395_pa-17-30-2000_mro-supply/)). [LINAK offers 12/24/48V variants](https://www.linak-us.com/products/linear-actuators/) with customizable stroke, but 48V is quote-only, not catalog.

**Default: PA-17 quad (24" stroke, 2,000 lb) on a 24V rail fed from the 48V bus via DC-DC.** 4× ~$380 + sync controller ~$450 ≈ **$1,970**. Fits the V0.1 budget bucket ($2-3K).
**Upgrade fork: LINAK 48V custom** — true 48V, tighter integration, IP66; +$1,200 placeholder pending quote.

## 2. Composting toilet (fork resolved → vendor sub-fork)

| | Nature's Head | Trelino Evo M |
|---|---|---|
| Price | [~$965](https://natureshead.net/) ([review: "worth $1,000?"](https://rvoutfitting.com/natures-head-composting-toilet-review/)) | [~$395 street](https://mytrelino.com/products/trelino-evo-m-portable-composting-toilet) (models from ~$350) |
| Weight | ~23 lb | ~9.5 lb |
| Capacity | large (agitator drum, weeks) | 1.3 gal urine / 2.1 gal solids (weekend-scale) |
| Character | proven marine/RV standard, bulkier | ultralight, no agitator, easy carry-out |

**Both stay in the configurator as a sub-fork.** Trelino matches the weekend-trailer weight ethos (−14 lb, −$570); Nature's Head suits extended-trip configs. Default = Nature's Head (reference build assumed it); flip if weekend-only.

## 3. Salvaged Tesla pack (Range-Neutral tier input)

Recycler/salvage pricing for Model 3/Y packs (~75-82 kWh): [Calimotive lists Model Y packs from ~$4,000 and Model 3 from ~$5,500](https://calimotive.com/products/tesla-model-y-battery-pack-replacement); a SC shop quotes [75 kWh at ~$6,500 installed-with-core](https://www.findmyelectric.com/blog/tesla-battery-replacement-cost-explained/); refurb specialists run [$9,000-14,500](https://recharged.com/articles/tesla-model-y-battery-replacement-cost-2026). **Config estimate of +$6,500 confirmed in-band; BOM carries $6,000 pack-only.** Open: BMS integration path (keep Tesla BMS + CAN decode vs replace), pack condition grading, freight (~1,060 lb item).

## 4. Climate (cooling fork numbers confirmed)

[Midea U-shape 8,000 BTU inverter](https://www.midea.com/us/store/cooling-and-heating/window-air-conditioners/Midea-8,000-BTU-DOE-U-Shaped-Smart-Window-Air-Conditioner.maw08v1qwt): ~$330-380 street, draws [~300W low / ≤500W eco-high](https://diysolarforum.com/threads/1st-time-planning-to-power-window-ac-unit-midea-8k-btu-u-shaped-ac.87664/page-2), 32 dBA — the inverter compressor is why the 5 kWh/hot-night budget works. 5,000 BTU basic units ~$180 but fixed-speed; consider making the Midea 8K the *recommended* cooling pick despite +$120 (inverter modulation beats fixed-speed 5K on energy).

## 5. Victron 48V spine (shared part slugs with House BUS)

- MultiPlus-II 48/3000: ~$1,200 street (48/5000 ~$1,900; MultiPlus 48/2000 ~$800)
- [Cerbo GX MK2: ~$300](https://www.amazon.com/Victron-Energy-Cerbo-GX-MK2/dp/B0D6LVZWGX) (range $210-450 by variant) + GX Touch optional
- [SmartSolar MPPT 250/60-Tr: ~$435](https://offgridstores.com/products/victron-smartsolar-mppt-250-60-tr-solar-charge-controller) ([sale ~$415](https://www.solar-electric.com/victron-energy-smartsolar-mppt-250-60-tr-charge-controller.html)) for the ~1,000-1,100W roof; 150/45 (~$300) suffices for 600W; 250/70 (~$520) for 1,300W

## 6. Running gear

- [Timbren Axle-Less suspension](https://timbren.com/collections/axle-less-trailer-suspension), 2,200 lb HD class w/ 4" lift option — ~$1,000-1,400/pair street ([overlandtrailer.com listings](https://overlandtrailer.com/product/timbren-axel-less-suspension-2200-lb-4-lift/)); BOM carries $1,200
- [Curt Echo 51180 brake controller: ~$230-280](https://www.curtmfg.com/part/51180) ([eTrailer](https://www.etrailer.com/Trailer-Brake-Controller/CURT/C51180.html)); BOM carries $250

## 7. Still open (quotes required)

Frame fabricator (target ≤$6,000 per V0.1 gate 7); composite panel supplier/layup; LINAK 48V quote; salvage-pack BMS integration path; soft-wall sewing (Sunbrella/Stamoid) vendor.

---

*Feeds: `slipstream.config.json` (parts arrays + vendor sub-forks) and the configurator BOM output. Update when real quotes land; replace street prices with PO numbers as V0.1 purchases happen.*
