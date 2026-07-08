# SS05 — Frame & Chassis (aluminum frame, suspension, tow interface) · Design Track

**Status:** Detailed v0.1 · **Sequence:** 3 · **Depends on:** SS01 pack envelope (side-lay decision), SS04 shell attach scheme
**Traces to:** Roadmap I.2 #1/#2/#9 (Model Y envelope, 1,900 lb, 15' overall), Decisions D1 · **Feeds V0.1 Gate 7:** fabricator quote signed, ≤$6,000.

## 1. Purpose & requirements

The skateboard: frame carries pack, tanks, floor, shell, tongue — lowest possible CG, sealed smooth belly. Requirements: 6061-T6 welded · 12' box + 3' tongue, 78" overall width · GVWR 2,700 lb (1,900 dry + 800 payload) on a 2,200 lb-class suspension pair *(see open Q1 — rating vs GVWR margin)* · tongue weight 10–12% (190–230 lb loaded target, ≤350 lb hard cap) · pack bay + tank bays inside rails · skid/stone protection under pack.

## 2. Interfaces

- **T2 tow:** 2" coupler + Andersen No-Sway hardware; 7-pin; breakaway; Curt Echo (SS02 supplies no wiring here — Echo is at the plug)
- **T6:** shell bond flange around box perimeter; 4 pop-up corner posts (SS03 loads: ~500 lb/corner working)
- **SS01:** pack cradle amidships, slightly forward of axle; aft-of-axle alternate position pre-engineered (risk R1 tongue-weight lever)
- **T5:** fresh (~20 gal) fwd of axle, gray (~10 gal) aft — tank placement is the tongue-weight trim tool

## 3. Layout & member sizing (first pass, for the fabricator drawing set)

- Main rails: 2×4×0.188" 6061-T6 rect tube, full length; kick-up over axle
- Cross members: 2×2×0.125" on ~16" centers; doubled at pack bay + axle + corner posts
- Tongue: 2×3×0.25" A-frame, bolted to rails (replaceable after a strike)
- Perimeter box flange: 2×2 angle, shell bond + mechanical
- Belly: 0.040" Al sheet riveted + sealed; 0.125" 5052 skid plate under pack bay
- Est. frame mass: **~260–300 lb** (rails ~110, cross ~70, tongue ~45, flange/belly/skid ~60)

## 4. Bought parts (Sourcing doc §6)

| Item | Est. |
|---|---|
| Timbren Axle-Less 2,200 lb pair (4" lift option deferred — `offroad` fork) | ~$1,200 |
| Hubs, 15" wheels, LT tires ×2 + spare | ~$700 |
| 2" coupler + Andersen No-Sway | ~$250 |
| Electric drum brakes 10" + breakaway kit | ~$350 |
| Powered tongue jack w/ caster foot | ~$300 |
| Curt Echo 51180 | ~$250 |

## 5. Fabricator package (Gate 7)

Deliverables to quote: DXF/DWG of rails/cross/tongue, weld map, tolerance notes (corner-post plumb ±1 mm — SS03 rack budget), anodize/none, delivery as welded chassis (no running gear). Quote checklist: 6061 vs 5052 substitutions rejected · certs on material · ≤$6,000 · lead time ≤10 weeks · alternate fabricator identified (risk R10).

## 6. Open questions

1. **Suspension rating:** Timbren 2,200 lb pair at 2,700 lb GVWR — is the pair rating per-side (4,400 total, fine) or per-axle-set? Confirm with Timbren; if marginal, HD tonne class.
2. Rail depth 4" vs pack side-lay height 2.8" + cradle — confirm pack fully shadows inside rails (SS01 Q1 couples here)
3. Bolted-tongue shear joint detail (bolts in double shear + fitted holes)
4. Corner-post to rail joint: welded gusset vs bolted casting (repairability)
5. Tank bay liners / strap standard

## 7. V0.1 deliverables

CAD frame model (single source of truth per roadmap Part III) → drawing set → 2 quotes minimum → signed quote ≤$6,000 = gate. No metal cut until SS06 CFD gate also passes (geometry freeze discipline).

---
*Detailed 2026-07-07. Mass lines here supersede placeholder config numbers when CAD lands.*
