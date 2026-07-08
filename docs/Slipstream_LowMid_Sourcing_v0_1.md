# Slipstream — Low & Mid Tier Sourcing v0.1

**Date:** 2026-07-08 | **Method:** 3 parallel research agents (~43 searches), July 2026 US street prices, every number cited in agent transcripts | **Companion:** `Slipstream_Component_Sourcing_v0_1.md` (core platform), `Slipstream_Tier_Spectrum_Research_v0_1.md` (tier architecture)
**Purpose:** firm numbers for the Foamie / Weekend / Explorer tiers → configurator `parts[]` data.

---

## 1. Foamie tier — the kit bill closes

| Item | Price | Note |
|---|---|---|
| Harbor Freight 4x8 folding trailer #62666 | $329–400 | Appears to be clearance-phasing; #58703 (1,720 lb) is $499.99 successor |
| Vintage Technologies insulated door SET (26x36 L+R) | $825.95 | The #1 beginner failure point, bought |
| Windows (12x24 vertical ~$115; VT 30x20 $122.95) | ~$240/pair | |
| RecPro 62" hurricane hinge | $51.95 | Galley hatch leak point, solved |
| 2" XPS Foamular 250 4x8 | ~$39–45/sheet × 6–8 sheets | Shell ≈ $290 |
| PMF pack (13 yd 10oz duck ~$120, 2 gal Titebond II $50, Gripper $24, ext. paint $35) | ~$230 | Paint is structural |
| Adhesives (Gorilla 36oz $28, PL300 tubes, foam-safe spray) | ~$60 | |
| MaxxFan Dome 12V | $84.88 | Cheap powered vent |
| LED light kit $40, 4-pin harness $15, chains $14 | ~$70 | |
| Highway axle upgrade (Dexter EZ-Lube $445 + 2 Taskmaster radials $205) | ~$650 | Optional but recommended |

**Bare-minimum foamie ≈ $1,050–1,250** (matches community "<$1,500"). **Kit version ≈ $2,400–2,650**; **+axle upgrade ≈ $3,100 loaded.** Configurator Foamie tier bracket ($3–12K) confirmed.

## 2. Weekend tier movers (config parts updated)

- **Cooling:** 5K BTU mechanical crept up to ~$156 (tariffs); **Midea U 8K inverter $399 MAP (~$356 after rebate)** — inverter modulation makes it the smarter default despite +$240
- **Fridge:** dual-zone chest fridges collapsed in price (Alpicool CF45 $280); 3 cu ft upright ~$400–550; 5 cu ft upright $700–1,100
- **Water:** 20 gal fresh ~$160, 10 gal gray ~$100, Shurflo 4008 ~$95, **Bosch ES4 4-gal $250–295** (up 30–40% since 2023)
- **Toilets:** Nature's Head now **$1,025** factory-direct; Trelino Evo M **$475 list / ~$404 on recurring 15% sales**
- **Awning:** ALEKO 8x8 manual ~$300; Carefree Fiesta quality tier $725–900 (starts at 10 ft — ALEKO fits the 12' box)
- **Running gear:** Timbren Axle-Less 2,000 lb HD pair ~$1,000–1,200 (ASR2KHDS series superseded ASR2200HD — cart-confirm); Dexter 10" brake pair $143.55; breakaway kit $53–72; electric tongue jack $100–140 (Weize/VEVOR) + BAL caster $52–57; Andersen Rapid Hitch $200–260 (skip WDH entirely at 2,200 lb — also WDH breaks hitch-force sensing on the Range-Neutral tier)
- **Solar (best mover):** Renogy 200W rigid **$145/panel in pairs (~$0.73/W)**, free Z-brackets; semi-flex carries 60–80% premium
- **Soft walls:** Sunbrella Marine $43–62/yd; Stamoid Light $43.95/yd / Top $51.95/yd; YKK #10 Vislon $15/zipper
- **Galley/AV:** Duxtop 1800W induction $71; projector sweet spot $450–600; rugged BT speakers $40–65; 12V dimmable pucks ~$56/6-pack; IP65 LED strip $20–40
- **48V lighting reality:** 48V-native fixtures don't exist as consumer items — the 48→12V buck rail (already in SS02) feeds all lighting

## 3. Explorer tier + the DC-HVAC find

- **THE FIND: RecPro 48V rooftop heat pumps — 9,500 BTU $1,849.95 / 13,500 BTU $1,999.95, cool + heat, native 48V DC.** Runs straight off the house bus with zero inverter conversion loss and no inverter capacity claim. This should become the Explorer-tier default over the 115V mini-split (Pioneer/Senville 9K ~$700–800 + inverter headroom + penetration). Velit 2000R 12/48V $1,679 (cooling-focus), Mabru RV12 $2,599, Nomadic from $3,425 round out the DC field.
- Heating small: PTC ceramic $20–40; Camco 12V blanket $43.67; Webasto AT2000 genuine $800–1,100 vs Chinese 2 kW clone $90–150 (no E-mark; fire-safety tradeoff noted in config)
- Cassette toilet: Thetford C223-CS $800–950; Porta Potti 565E $150–190
- Water heat upgrade: Suburban SW6DE 6-gal $669.99; **240V tankless (EcoSmart ECO11 $285, Stiebel DHC-E $221–289) draws 50–60A @240V = 12–14 kW — physically beyond any onboard inverter; the existing forbid rule is actually understated. Tankless = shore-power-pedestal-only feature.**
- Shower: privacy tent $35–80; exterior hot/cold shower box $30–60
- Windows/door upmarket: Arctic Tern dual-pane ~$450–500 ea; Tern entry doors $1,489–1,982
- MaxxFan Deluxe $299–395; Dometic Penguin II (contrast) $1,100–1,500
- **16 kWh house battery:** DIY EVE route ~$90–112/kWh (US stock) vs EG4/Ruixu server-rack $225–254/kWh — DIY is 2.2–2.5× cheaper; racks buy UL listing + warranty

## 4. Composite panel suppliers (SS04 open question, answered enough to quote)

- **Total Composites** (Blaine, WA): FRP/PU 2" panels, complete camper kits **$17,200–27,000** (truck-camper sized; a 12' trailer box = custom quote, ~$20–25K class). The "buy the shell" fork.
- **Carbon-Core**: FRP/foam flat sheets 4x8 to custom, quote-based, ~$10–20/sqft for 1–2" panels (finish adders: +$0.45/sqft sanded, +$0.43/sqft gelcoat)
- Industry band for 1–2" fiberglass sandwich: **$8–23/sqft** → Slipstream's ~320 sqft shell = $2,600–7,400 bought-panel vs ~$3,500 self-layup materials (SS04). Panel-supplier quotes are now worth soliciting: at the low end of the band, buying beats laminating.
- Fiber-Tech, CPT Panels, Composite Box: OEM/quote only. Crane/Panolam FRP = thin skins to self-laminate; Coosa = structural board, wrong product.

## 5. Configurator effects (applied in this commit)

Parts arrays updated with confirmed prices across ~20 options; foamie option now carries its own kit parts and the BOM engine suppresses the composite-platform baseParts when Foamie is selected; RecPro 48V heat pump replaces the generic mini-split as the heat-pump option's parts; tankless note strengthened; solar parts re-priced down; NH/Trelino re-priced.
