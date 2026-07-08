# PROJECT SLIPSTREAM — Cowork Handoff Context

**Purpose:** Full context of the trailer product family conversation, structured for ingestion by the Cowork configurator system. This document is *raw material*, not a finished architecture. It captures every fork, decision, rationale, constraint, and reference identified during the design conversation so Cowork's algorithm has what it needs to build the configurator's decision tree.

**Companion artifact:** `PROJECT-SLIPSTREAM-Prototype-Roadmap.md` — the "reference build #1" doc, representing a single walk through the fork tree (TJ's personal summer weekend config).

**Owner:** TJ
**Date:** 2026-06-25
**Status:** Pre-Cowork ingestion

---

## 1. Product family framing

Slipstream is a **product family**, not a product. The output of the configurator is a bespoke trailer specification (BOM, drawings, cost, weight, autonomy predictions) tailored to a user's answers to the fork tree. The design system is open-source; the personal build is the forcing function that validates the tree exists and produces something buildable.

The invariant core is the ~80% of components shared across every valid configuration. The fork tree is the ~20% that varies. The compatibility rules are what prevent invalid configurations from being generated.

Parallel product: TJ's Cowork-hosted electric house bus, which uses the same configurator pattern. Slipstream reuses that infrastructure. Trailer is simpler than the bus because: no drivetrain (optional fork), no compliance surface, smaller weight envelope, no residential occupancy standards.

---

## 2. Invariant core (the 80% every trailer shares)

These are the architectural decisions that hold across every valid configuration. Forks vary parameters within these; they don't replace the architecture.

- **Aluminum frame architecture** — welded 6061-T6 or bolted extrusion. Frame length varies with trailer length fork; cross-section geometry (rail depth, wall thickness) is standard across the family.
- **Frame-integrated skateboard layout** — battery pack lives in frame rails between the axle and tongue. Water tanks (fresh + gray) live in frame rails. Skid plate protects the underside. Lowest possible CG, cleanest belly pan for aero.
- **48V DC electrical spine** — Victron ecosystem (MultiPlus II inverter/charger, MPPT solar charge controller, Cerbo GX with cellular gateway and VRM remote monitoring). Smart relays for remote pre-conditioning (water heater, HVAC).
- **NEMA 14-50 as the universal electrical interface** — one inlet (shore power in), one outlet (Tesla or other EV pass-through out). Adapter kit for downsized pedestals (30A / 20A / 15A). Load-balancing between trailer battery charging and pass-through.
- **Composite wall panel system** — foam core with fiberglass skins. Insulation thickness and skin gauge vary by season fork. Layup process is standard.
- **Pop-up roof mechanism** — 4× synchronized 48V electric linear actuators with encoder-feedback sync controller. Soft canvas sides (Sunbrella or Stamoid) with rigid front and rear panels as an upgrade fork. Perimeter EPDM compression seal. Drip skirt geometry over the box. 4× mechanical over-center travel latches. (Pop-up is standard; fixed-roof is a fork.)
- **Torsion-bar axle** — Timbren or Dexter independent torsion. Axle rating scales with GVWR fork. Standard mounting geometry.
- **Tow interface** — 2" ball hitch with integrated anti-sway (Andersen No-Sway or equivalent). Curt Echo Bluetooth brake controller (Tesla-compatible) or hardwired aftermarket controller depending on tow vehicle fork.
- **Powered tongue jack with caster foot** — swing-down jack wheel eliminates the need to lift the trailer when de-hitching.
- **Sealed smooth belly pan** — aero-critical. Standard across the family.
- **Rounded leading edges + rear taper** — aero geometry standard across every SKU. Degree of rear taper varies with box length (longer trailers can afford more taper without losing interior volume).

---

## 3. Fork inventory (raw list — the ~20% that varies)

Each fork is a decision point the configurator presents to the user. Notes on rationale, weight/cost/complexity implications, and compatibility flags are included where known. Cowork's algorithm should structure these into the decision tree; the ordering below is *not* a proposed tree, just an inventory.

### 3.1 Dimensional forks

- **Box length**: 12' / 15' / 18' (base options). Affects: bed size ceiling, storage, weight class, tongue length, rear taper aggressiveness, campsite/garage fit.
- **Tongue length**: 2.5' / 3' / 4'. Affects: jackknife geometry, storage box size, aero (longer tongues create more turbulence between vehicle and trailer).
- **Overall height (roof down)**: low profile (~5' / in Model Y slipstream) / mid (~6' / above Model Y roofline) / tall (~7'+). Higher = worse aero, more headroom without popping up.
- **Overall width**: 78" (Model Y body match) / 84" (Lightning/R1S body match) / 96" (max legal without wide-load flag). Wider trailers accept larger tow vehicles but create mirror-eddy drag.
- **Pop-up stroke**: 24" (6' popped headroom) / 36" (7' popped headroom). Longer stroke = taller soft walls, slightly more actuator cost.

### 3.2 Structural / shell forks

- **Frame material**: welded aluminum / bolted aluminum extrusion (8020-style) / steel (heavier, cheaper). Configurator should default to welded aluminum for weight; steel option for cost-sensitive builds.
- **Wall insulation thickness**: 1" (summer only) / 1.5" (3-season) / 2" (4-season). Affects: interior volume, weight, cost, thermal performance.
- **Skin material**: fiberglass (standard) / polished aluminum (aesthetic upgrade, Bowlus-style) / painted composite.
- **Roof type**: pop-up soft-side (standard) / pop-up hard-side (heavier, better thermal, better weather sealing) / fixed hard-roof (worst aero, best thermal, no standing headroom in low-profile config).
- **Rear geometry**: flat rear (worst aero, most interior) / partial teardrop taper above bed (best compromise) / full teardrop taper (best aero, worst interior).
- **Belly pan**: sealed smooth (standard, aero-critical) / open frame (weight savings, terrible aero — not recommended, but a fork).

### 3.3 Power system forks

- **Battery capacity**: 8 kWh / 12 kWh / 16 kWh / 20 kWh. Trades autonomy against weight and tongue-weight envelope. 20 kWh may exceed Model Y tow rating depending on other choices.
- **Battery chemistry**: LFP (standard) / LMFP (newest, ~5% denser, same safety) / (future) sodium-ion (heavier but cheaper).
- **Roof solar capacity**: ~600W / ~1000W (full-roof standard) / ~1300W (semi-flex panels following roof curve).
- **Portable solar prep**: none / MC4 input + second MPPT / included 200W foldable panel + input.
- **Inverter capacity**: 2000VA / 3000VA (Victron MultiPlus II — standard) / 5000VA (for high-draw HVAC + induction simultaneous use).
- **Drivetrain / powered trailer**: none (standard) / single-motor regen assist / dual-motor AWD. Adds 150-250 lbs. Requires tow-vehicle communication protocol decision. Fundamentally changes axle spec.
- **Shore power inlet**: NEMA 14-50 (standard) / NEMA 14-50 + TT-30 dual inlet (redundancy).
- **EV pass-through outlet**: NEMA 14-50 (standard) / NEMA 14-50 + J1772 / NEMA 14-50 + NACS.
- **DC-DC charging from tow vehicle**: none / 12V DC-DC (low current) / high-voltage tap (fastest but Tesla-specific hack).

### 3.4 Climate control forks

- **Cooling**: none / window AC 5,000 BTU / window AC 8,000 BTU / mini-split cool-only.
- **Heating**: none (summer only) / electric blanket + small fan (spring/fall) / PTC electric resistance heater / mini-split heat pump / diesel Webasto heater (contradicts "all-electric" but included as a fork for cold-weather users).
- **Combined HVAC**: none / mini-split heat pump (cool + heat, standard for 3-season) / full ducted HVAC (4-season, heaviest, most expensive).
- **Ventilation**: side wall low-front intake + high-rear exhaust (standard, roof-solar-preserving) / roof vent fan (Maxxair-style, sacrifices ~200W solar) / both.
- **Wall thickness coupling**: 4-season heating options require ≥1.5" wall insulation fork.

### 3.5 Water and sanitation forks

- **Fresh water capacity**: 10 gal / 20 gal / 30 gal / 40 gal.
- **Gray water capacity**: 5 gal / 10 gal / 15 gal / portable-tote-only.
- **Black water**: none (composting toilet standard) / cassette toilet + tote / full black tank + macerator.
- **Toilet**: composting with urine diverter (Nature's Head / Trelino) / cassette / dry (no toilet, external only).
- **Shower**: none (external only, no fixture) / outdoor spigot hot+cold / outdoor spigot + privacy enclosure / interior wet stall (requires 4-season shell, doubles gray tank need).
- **Water heater**: none / 2-4 gal tank electric (standard, remote-pre-heatable via Cerbo) / 6 gal / tankless electric (240V/30A+ required, big battery drain).
- **Condensate handling**: to gray tank (standard) / to ground / captured to utility tank for rinse purposes only.
- **Sink**: galley sink + drain / galley sink + foot pump (weight savings) / no interior sink (external only).

### 3.6 Sleep and interior forks

- **Bed size**: twin (38×75) / full (54×75) / short queen (60×74) / queen (60×80). Longer beds require longer box.
- **Bed orientation**: east-west across rear / north-south center / convertible dinette.
- **Sleeps**: 2 / 2+1 (kid bunk over dinette) / 4 (bunk conversion) / 5 (roof-top tent add-on).
- **Interior layout**: bed forward / bed rear / bed center. Affects galley and bathroom placement.
- **Cabinetry**: minimal (open shelving) / standard (closed cabinets, laminate) / premium (hardwood, custom).
- **Countertops**: laminate / butcher block / stone composite.
- **Upholstery**: none (customer-supplied) / standard fabric / premium fabric / marine vinyl (waterproof).

### 3.7 Cooking and appliance forks

- **Cooktop**: none / single induction burner / dual induction / dual induction + convection oven combo.
- **Fridge**: none / 12V compressor 3 cu ft (standard) / 12V compressor 5 cu ft / dual-zone fridge+freezer.
- **Coffee maker prep**: none / dedicated 20A outlet / built-in espresso machine mount.
- **Microwave**: none / countertop / built-in (requires 5000VA inverter fork).

### 3.8 Media and lighting forks

- **Interior lighting**: standard LED / dimmable LED / dimmable + circadian (color-temp shifting).
- **Ambient exterior lighting**: none / perimeter LED strip / perimeter + underglow / perimeter + underglow + smart-controlled.
- **Floodlights**: none / rear only / all-around 360° / all-around + motion-sensor.
- **Interior media**: none / Bluetooth speakers / projector + speakers / projector + speakers + external screen mount for outdoor movies.
- **Awning lighting**: none / string lights / integrated LED in awning arms.

### 3.9 External protection forks

- **Awning**: none / side roll-out (curb side) / side + rear / 360° wraparound. Larger awnings add weight and mount complexity.
- **Awning material**: standard vinyl / Sunbrella / heavy-duty canvas.
- **Awning drop screens**: none / one side / all sides.
- **Roof rack**: none / accessory rails / full rack (conflicts with full roof solar).
- **Bike/gear rack**: none / rear hitch receiver / front tongue mount.

### 3.10 Tow vehicle forks

- **Target tow vehicle**: Tesla Model Y (78" body, 3,500 lb tow, 350 lb tongue) / Tesla Model X (79", 5,000 lb tow) / Ford F-150 Lightning (80", 10,000 lb tow, extended range) / Rivian R1S (81", 7,700 lb tow) / Rivian R1T / other EV / ICE truck. This is the most upstream fork — it constrains width, weight, tongue weight, and available electrical interfaces.
- **Brake controller**: Curt Echo Bluetooth (standard for Tesla and other EVs without native support) / hardwired aftermarket (for trucks with pre-wired trailer connections) / native (some newer EVs).

### 3.11 Season and use-case forks

- **Season rating**: summer only / 3-season / 4-season. Cascades into wall thickness, HVAC, plumbing insulation, water tank freeze protection.
- **Use case**: weekend base camp (TJ's config) / extended off-grid / full-time living / expedition/off-road. Off-road use case adds skid plates, higher ground clearance fork, more aggressive tires.
- **Off-road package**: none (standard) / upgraded suspension + tires + rock sliders + underbody armor.

### 3.12 Aesthetic forks

- **Exterior color / finish**: raw aluminum / painted (color options) / wrapped.
- **Interior design language**: Polydrops-angular / Bowlus-luxury / Airstream-classic / Hutte Hut-boutique / custom.
- **Window count and placement**: minimal (rear + door only) / standard (2 sides + rear + door) / maximum (panoramic).

---

## 4. Locked decisions (for reference build #1: TJ's personal config)

These are the decisions TJ has locked for the personal build. They represent one valid walk through the fork tree above. Every locked decision has rationale attached — this is what makes each fork *smart* rather than a checkbox. When another user runs the configurator with different constraints, these rationales reopen the corresponding forks.

| # | Decision | Fork resolved | Rationale (why this fork closed this way) |
|---|---|---|---|
| 1 | Tesla Model Y | Tow vehicle | Owned vehicle; constrains width to 78", weight to 1,900 lb dry, tongue to 350 lb |
| 2 | 15' overall (12' box + 3' tongue) | Length, tongue | Balances layout completeness against storage / campsite fit / weight |
| 3 | 78" wide | Width | Matches Model Y body; zero overhang; stays in slipstream |
| 4 | Pop-up soft-side | Roof type | Resolves aero/headroom tradeoff; 4× 48V actuators with sync controller |
| 5 | 1" wall insulation | Wall thickness | Summer trailer only; weight savings |
| 6 | 12 kWh LFP (LMFP if available) | Battery capacity + chemistry | 2 hot-AC days + 4+ mild days off-grid; ~200 lbs |
| 7 | ~1000-1100W full-roof solar | Solar capacity | Roof real estate is most valuable as power |
| 8 | Window AC 5,000 BTU | Cooling | Small pop-down volume + 12hr nightly use makes mini-split overkill |
| 9 | Electric blanket + small fan | Heating | Summer trailer; heating the person is 15× more efficient than the air |
| 10 | Side wall vent (no roof vent) | Ventilation | Preserves solar roof real estate |
| 11 | Composting toilet + urine diverter | Toilet | No black tank; simpler; lighter |
| 12 | Outdoor shower only | Shower | Summer trailer; interior wet bath not worth the space/weight |
| 13 | ~20 gal fresh / ~10 gal gray | Water capacity | Sized for 2-3 day weekend + shower drainage |
| 14 | Condensate to gray tank | Condensate | Not potable, not worth capturing separately |
| 15 | Short queen 60×74 east-west | Bed size + orientation | Fits 74" interior width; east-west opens floor space |
| 16 | Sleeps 2 | Sleeps | TJ + partner |
| 17 | Induction single burner | Cooktop | Weekend cooking is minimal; single burner sufficient |
| 18 | 12V 3 cu ft fridge | Fridge | Sized for weekend food + drinks |
| 19 | 2-4 gal tank water heater | Water heater | Remote pre-heat via Cerbo while driving back from hikes |
| 20 | Projector + Bluetooth speakers | Media | Outdoor movie under awning |
| 21 | Perimeter ambient LED | Exterior lighting | Aesthetic + practical |
| 22 | Side roll-out awning | Awning | Curb-side outdoor kitchen / lounge |
| 23 | Aluminum welded frame | Frame material | Weight + no rust + composite-compatible |
| 24 | Foam-core + fiberglass shell | Skin material | Weight target |
| 25 | Torsion axle (Timbren) | Axle | Better ride, no maintenance, sealed |
| 26 | 15" wheels, LT-rated tires | Wheels | 6" fender clearance, occasional dirt road access |
| 27 | 2" ball + Andersen No-Sway | Hitch | No weight-distribution needed at 1,900 lbs |
| 28 | Curt Echo Bluetooth brake controller | Brake controller | Tesla-compatible, phone-app paired |
| 29 | Cerbo GX + cellular + VRM | Remote monitoring | Enables remote pre-conditioning |
| 30 | No powered drivetrain | Drivetrain | Weight/complexity not justified for TJ's use case |

---

## 5. Compatibility rules (partial list — Cowork should extend)

These are pairs (or triples) of fork choices that produce invalid or physically impossible configurations. The list is not exhaustive; Cowork's system should extend it based on physics + tow-vehicle math.

- **Model Y + 18' box + 16 kWh battery** — exceeds 3,500 lb tow rating or 350 lb tongue weight (depending on other choices).
- **Summer-only + PTC heater / heat pump** — contradiction; heater implies at least 3-season.
- **4-season + 1" wall insulation** — insufficient thermal envelope.
- **Interior wet stall + summer-only** — inconsistent; wet stall implies 3-season minimum.
- **Interior wet stall + 12' box** — insufficient floor area.
- **Composting-only + full black tank** — mutually exclusive.
- **Full roof solar + roof rack / roof vent** — competes for real estate.
- **Tankless water heater + <5000VA inverter** — insufficient power for on-demand heating.
- **Fixed hard roof + low profile (<5.5')** — no standing headroom, no pop-up compensation; only valid for sit-inside use case.
- **Drivetrain fork + Model Y tow vehicle** — Tesla's regen protocol not exposed for third-party trailer integration; drivetrain fork requires a tow vehicle with published trailer communication (Ford Pro Trailer, Rivian Tow).
- **96" width + Model Y** — trailer sticks past mirror lines; illegal without wide-load permit; also destroys aero.
- **AWD drivetrain + composting-only sanitation** — no rule against; just noting that drivetrain suggests longer trips which suggests users may want more robust sanitation.
- **Fixed roof + 6' headroom target** — requires trailer height >7', worst aero.

---

## 6. Price tier bracketing (for configurator pricing display)

Rough brackets, in the spirit of the bus's 100/200/300-mile tiers. Each bracket represents a coherent set of fork choices that hangs together as a product identity.

- **Weekend (~$30-40K target)** — 12'-15' box, summer-only, 8-12 kWh, window AC, composting head, outdoor shower, side awning, standard fixtures. Cash build cost for TJ's config estimated at $50-70K over V0.1-V1.0, but self-build labor is uncounted; kit price for someone else would target the lower end via mass-purchased components.
- **Explorer (~$50-60K)** — 15' box, 3-season, 12-16 kWh, mini-split heat pump, composting + outdoor privacy enclosure, projector, wraparound awning, upgraded interior finish.
- **Base Camp (~$70-90K)** — 15'-18' box, 4-season, 16-20 kWh, full HVAC + PTC backup, interior wet stall, larger tanks, expedition suspension, premium finish.
- **Overland (~$80-100K)** — 15'-18' box, 3-4 season, drivetrain fork engaged (regen), off-road package, upgraded electrical, satellite communications prep.

---

## 7. Parts fungibility notes (what's shared across SKUs)

Following the "Model Y and Model 3 share 80% of parts" principle. High-level notes for Cowork to extend:

**Shared across all SKUs:**
- Aluminum frame extrusion profiles (cut to length per SKU)
- Battery cell format + BMS (capacity varies by cell count only)
- Victron electrical components (inverter/MPPT/Cerbo sized per SKU but same product family)
- Water tank moldings (same tanks, different quantity/plumbing per SKU)
- Composite wall layup process + fiberglass roll stock
- Pop-up actuator model (only quantity and stroke vary)
- Wiring harness backbone (branches added/removed per SKU)
- Tow interface hardware
- Torsion axle from the same vendor family (rating varies)

**Variant-specific:**
- Wall panel dimensions (cut per SKU)
- Interior cabinetry (per layout choice)
- Appliance mounting brackets (per appliance choice)
- HVAC penetrations (per climate control choice)

---

## 8. Reference articles (competitive and aesthetic anchors)

The configurator's UI should probably surface these as inspirations at the appropriate fork points:

- **Lightship L1** — closest architectural analog. Electric, pop-up, aero-optimized. Anchor for the "premium electric" identity.
- **Polydrops P17A / P21 / XP19** — angular, faceted aesthetic. Battery-in-frame skateboard. No pop-up. Anchor for the "modern minimal" identity.
- **Bowlus Volterra** — polished aluminum, luxury, no pop-up. Anchor for the "premium classic" identity.
- **Hutte Hut** — boutique teardrop. Anchor for the "small, beautiful" identity.
- **Earth Traveler T250LX** — ultralight (~340 lbs). Anchor for the "extreme minimalism" identity.
- **Airstream Basecamp** — traditional aluminum semi-monocoque. Anchor for "conventional expectations."

---

## 9. Open questions the configurator will need to resolve

Items TJ and Claude did *not* resolve during the design conversation, which the configurator's algorithm or user will need to answer:

- Exact composite panel supplier and layup process
- Frame fabricator selection
- Pop-up actuator supplier (Linak vs. Progressive Automations vs. others at 48V)
- Composting toilet default (Nature's Head vs. Trelino — likely a fork itself)
- Whether powered-drivetrain fork is worth investing in given the complexity ceiling
- Whether the trailer configurator inherits the bus's BOM-output infrastructure or gets its own
- Regulatory compliance surface for different jurisdictions (US state-by-state trailer weight/length/lighting regs; EU regs if the open-source system goes international)
- Whether kits are shipped as flat-pack for user assembly or as finished trailers

---

## 10. What Cowork receives at handoff

1. **This document** — raw context, fork inventory, decisions, rationale, compatibility hints.
2. **`PROJECT-SLIPSTREAM-Prototype-Roadmap.md`** — reference build #1, TJ's personal summer weekend config as a fully worked example.
3. **Conversation thread** (via chat export) — the reasoning trail behind every decision, useful for the algorithm to understand *why* each fork exists.
4. **Reference images** — Lightship L1, Bowlus Volterra, Polydrops P17A/Eagle/XP19/P21, Hutte Hut, Earth Traveler T250LX (retrieved via image search during the conversation).

The Cowork system's job is to:
- Structure the fork inventory into a coherent decision tree
- Build the compatibility rule engine
- Wire the BOM output infrastructure
- Produce the pricing model per configuration
- Generate the drawings / build documentation per configuration
- Publish the open-source repository

*End of handoff document.*
