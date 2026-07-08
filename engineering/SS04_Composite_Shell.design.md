# SS04 — Composite Shell (foam-core fiberglass panels) · Design Track

**Status:** Detailed v0.1 · **Sequence:** 2 (samples parallel to SS03) · **Depends on:** SS06 geometry freeze for panel dimensions
**Traces to:** Roadmap I.2 #7 (aluminum frame + foam-core composite, weight target) · **Feeds V0.1:** panel samples pass insulation, water-intrusion, and structural rigidity tests before any tooling money.

## 1. Purpose & requirements

The shell is where the 1,900 lb dry target is won or lost. Requirements: 1" foam core (summer spec, fork allows 1.5"/2") · fiberglass skins both faces · target ≤1.2 lb/ft² panel areal weight · self-supporting spans between frame attach points · rounded leading edges + partial rear teardrop executable in the same layup · zero water path at joints, penetrations (AC, vents, shore inlet), and the pop-up drip skirt.

## 2. Interfaces

- **T6/SS05**: panel-to-frame bond line (adhesive + mechanical at edges); lower box is structural with the frame, upper pop-up lid is a stiff tray
- **T7/SS03**: drip-skirt geometry over box walls; actuator and latch penetrations
- **T8**: R-value ≈ R-5 to R-6 at 1" (XPS/PU class) — matches summer-only envelope; AC opening with gasket flange + removable storage plug (Decision D3)

## 3. Candidate stacks (sample all three in V0.1)

| Stack | Core | Skins | Est. areal | Notes |
|---|---|---|---|---|
| A | 1" XPS (Foamular 250) | 2× 6 oz E-glass epoxy per face | ~1.0–1.2 lb/ft² | Cheapest, proven in foamie/teardrop community; styrene-safe epoxy only |
| B | 1" PU/PIR board | same | ~1.1–1.3 lb/ft² | Better temp tolerance, bonds well |
| C | 1" PET foam (Airex T92 class) | 1× 12 oz biax per face | ~1.3 lb/ft² | Marine-grade, best fatigue + screw retention, priciest |

Shell area ~320 ft² (12' box, popped-lid tray, floor excluded) → ~350–420 lb shell at target areal weights, consistent with the mass budget. Skin/core bond is vacuum-bag or weighted wet layup on a flat table — no molds at V0.1; compound curvature (leading-edge radii, taper) via kerf-bent core or shaped EPS + overlay, decided by sample results.

## 4. Components / materials (V0.1 samples)

Foam sheets (3 types) + E-glass roll + epoxy kit + vacuum-bag consumables ≈ **$500–900** ✓ V0.1 bucket. Panel test articles: 2'×4' each stack.

## 5. Test plan (the V0.1 deliverable)

1. **Stiffness:** 3-point bend, span 36", pass = <0.5" deflection at 40 lb center load
2. **Water:** 48 hr spray-rig soak on a panel with a bonded joint + a sealed penetration; pass = zero core moisture gain
3. **Thermal:** hot-plate ΔT check against R-5 prediction
4. **Fastener pull-out:** each stack, for hinge/latch/awning hardpoints (informs where plywood/G10 inserts are required)
5. **Weigh everything** — areal weight truth feeds the mass budget

## 6. Open questions

1. Panel supplier vs. self-layup: quote 2–3 flat-panel vendors (FRP sandwich suppliers) against DIY table cost — handoff doc §9 open item
2. Exterior finish stack: gelcoat vs. paint over glass (ties to `finish` fork)
3. Pop-up lid: same stack or lighter (lid carries solar, ~120 lb array + wind) — likely stack C for the lid
4. Fire behavior of core choice near the galley — check XPS flame spread; PIR wins here

---
*Detailed 2026-07-07. Sample results pick the stack; no composite tooling money before SS06 CFD gate passes (roadmap de-risk order).*
