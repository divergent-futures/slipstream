# SS05a — Flagship Frame & Layout Study · Design Track

**Status:** Layout v0.1 (pre-CAD design brief) · **Parent:** SS05 · **Governs:** Phase C frame CAD
**Traces to:** Flagship Plan D-F1 (≤3,500 lb loaded, Model Y), D-F3 (12' box), weight budget §3
**Purpose:** settle geometry, axle placement, and the drive-axle architecture decision so CAD starts from answers, not questions.

## 1. The envelope

12' box (144"), 78" outside / ~74" inside width, 3' tongue → coupler ~42" ahead of box front. Coordinates below: **x = 0 at the coupler**, box spans x = 42–186.

**The pack defines the floor.** Model 3 LFP pack (BTF-series, same enclosure family as 2170): ~84.5" long × ~59" wide, main slab ~5.5–6" thick, **penthouse hump (~13" tall) over the last ~12" at one end**. Placement: centered laterally → **7.5" channels each side** between pack and wall — the plumbing/wiring spine (peripheral-channel doctrine, same as the bus). Penthouse faces REAR (service access via rear hatch, HV runs short to the DU).

## 2. THE structural decision: the donor subframe IS the axle

The rear DU comes attached to the Model 3 rear subframe with suspension, hubs, brakes, and halfshafts — and the DU *only* drives wheels through its own halfshafts. So the trailer's drive axle is not "Timbren + motor somehow": **the harvested Tesla rear subframe assembly bolts under the frame as the complete suspension + drive axle.** Consequences:

- **Timbren pair is DELETED from the flagship BOM** (stays for unpowered tiers) — saves ~$1,100 and the rating question
- Track width 62.2" under a 78" body → wheels fully inboard → **skirted wheels = free aero** (the fenders become smooth body)
- Springs: Model 3 rear coils are valved for ~2,600 lb rear-axle load in a 4,000 lb car; our static axle load is ~3,200 lb (§3). **Trade study: stock coils (likely over-stiff ride, acceptable) vs. aftermarket coilovers vs. air springs (ride height + tongue trim!)** — air is tempting for the dock/campsite leveling story
- **Brakes: the subframe brings Tesla hydraulic calipers + EPB.** Trailer law wants controller-actuated brakes → **electric-over-hydraulic actuator (~$400, boat-trailer standard, Curt Echo compatible) driving the donor calipers**, breakaway-compatible; EPB motors = parking brake, wired to the trailer controller. This replaces the Dexter drum plan on the flagship
- ⚠️ **GAWR flag:** 3,140 lb static on an assembly from a ~2,600 lb/axle duty car. Margin exists (car GAWR includes dynamic reserve; our duty is gentler) but this needs a real check: spring upgrade + bearing duty review = CAD-phase task #1

## 3. Longitudinal balance (the tongue war, with numbers)

First-order mass placement (loaded, ~3,506 lb total; masses per Flagship Plan §3):

*The balance is a coupled system (the 600 lb subframe rides at the axle, so moving the axle moves the CG) — solved self-consistently in code, twice corrected in drafting. The solver script is the authority; it ships in the repo alongside this doc.*

- **Design point: pack center at x = 110 (68" into the box), axle at x = 120 (78" into the box, 54% of box length)**
- **Tongue = 303 lb loaded / 327 lb gray-empty** — both under the Y's 350 cap; note the counterintuitive one: **gray-empty is the HEAVIER tongue state** (the gray tank sits aft of the axle), so the cap must be verified in that condition, and it is ✓
- **Sensitivities (the design levers):** axle 1" aft → tongue +22 lb (forward = lighter — the coarse knob); pack 1" aft → tongue −8 lb (the fine knob)
- Battery-off-season (pack docked at house): ~2,540 lb trailer; recompute at CAD — expect well under cap ✓
- **Axle static load ≈ 3,200 lb** → the §2 GAWR flag is real: ~23% over the donor's ~2,600 lb rear-axle duty. Spring upgrade + bearing review is CAD task #1, not optional

## 4. Floor plan consequence (v0.1 sketch, for the CAD model)

```
x=42 ────────────────── 120 ──────────── 186
FRONT of box            AXLE             REAR
[galley + wet gear      [skirted         [transverse bed 74"
 + fridge + 12V bay      wheels,          over penthouse hump
 + fresh tank (x~95)]    gray tank        (hump = under-bed
                         under bed edge]  storage step) + DU
                                          below, rear hatch]
Pack floor spans x=68–152 (under everything); pop-up above all of it.
```

The penthouse hump under the bed is the one interior compromise the pack demands — and it's storage, not waste. Composting head + shower stay per reference layout (curb side, mid).

## 5. CAD handoff checklist (Phase C starts here)

1. Model the pack from measured donor dimensions (not these estimates) — **the frame is drawn around the measured pack**
2. Tesla subframe mount geometry (axle line at x=120 per §3): pick up the donor's four subframe bushings with frame bosses; measure before designing
3. Spring/damper decision (stock/coilover/air) + GAWR verification with real corner weights
4. Coupler machining: load-cell isolation per Guide #4 §2 (longitudinal-only path, spherical seats)
5. Tongue frame sized for 3,500 lb + load cell insert; jack + caster per BOM
6. Belly: pack IS most of the belly — fairing panels bridge pack edge to frame rails; skid plate under penthouse
7. Thermal bay (Lane 2 provisions): radiator + pump plate near penthouse, plumbing stubs capped
8. Carry CG + tongue live in the CAD tree (the §3 sensitivities are the design dashboard)

## 6. Open questions

1. Spring path (stock/coilover/air) — air adds the leveling + tongue-trim story for ~$800; decide at corner-weigh
2. GAWR formal check (bearing + spring duty at ~3,200 lb static)
3. E/H brake actuator model selection + breakaway integration test
4. Does the 2021–2023 DU-donor subframe geometry match 2024+ expectations if the DU donor is Highland after all? (split-donor: measure what arrives)
5. Fender/skirt structure: foam-core panels (SS04 stack) vs aluminum

---
*Layout v0.1, 2026-07-09. All masses/positions first-order from Flagship Plan §3; every number above is superseded by the first measurement of real hardware. Feeds SS05 CAD, updates configurator (Timbren deletion on flagship) when the subframe decision survives corner-weighing.*
