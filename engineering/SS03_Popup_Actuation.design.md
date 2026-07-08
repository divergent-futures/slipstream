# SS03 — Pop-up Actuation (quad synchronized lift) · Design Track

**Status:** Detailed v0.1 · **Sequence:** 2 · **Depends on:** SS02 (24V rail), roof mass estimate (SS04)
**Traces to:** Roadmap I.2 #4 (pop-up, 4× actuators), Decision log D2 · **Feeds V0.1 Gate 3:** 4-corner rig raises/lowers 200 lb test load 50 cycles with ≤1° rack.

## 1. Purpose & requirements

Roof goes up when parked, down when moving — the fork that dissolves the aero/headroom trade. Requirements: 24" stroke (6' popped headroom) · lift ~200–300 lb roof assembly + wind/snow-slush margin → ≥500 lb per corner working, 2,000 lb rated · 4-corner sync ≤1° rack (soft walls + seal tolerate little skew) · <60 s full travel (V0.5 gate) · self-locking at any position (power-off hold) · IP65+ (corners live outdoors).

## 2. Interfaces

- **T7** roof assembly: corner posts, over-center travel latches (4×, mechanical — actuators are not the travel restraint), perimeter EPDM seal compression at full-down
- **T1/SS02**: 24V rail via 48→24V DC-DC, 25A fused branch; sync controller signal to Cerbo relay for remote inhibit (no pop-up while hitched — interlock via 7-pin sense or manual)
- **T6/SS05**: lower mount bosses on frame corner posts
- **T8/SS04**: drip-skirt geometry over the box; actuator penetrations sealed

## 3. Components (Sourcing doc §1)

| Item | Spec | Est. |
|---|---|---|
| 4× Progressive Automations PA-17-24-2000 | 24V, 24" stroke, 2,000 lb dyn., IP65, ACME self-locking | 4 × ~$380 = $1,520 |
| Sync controller, 4-ch | Hall/encoder feedback, closed-loop position match | ~$300 |
| 48→24V DC-DC 25A | Shared with SS02 branch | (SS02) |
| Test rig steel frame + 200 lb load | Bench article, reused as mount-geometry mule | ~$250 |
| Limit switches + manual override (drill drive) | Stuck-up recovery at a campsite | ~$100 |

**Duty math:** 4 corners × ~75 lb share nominal; PA-17 at 2,000 lb rating = huge margin, chosen for gearbox longevity and side-load tolerance, not lift force. Current: ~5A/actuator at this load → ~20A peak on the 24V rail during travel ✓ 25A DC-DC.

**Fallback vendor:** LINAK 48V custom (quote pending — Sourcing §1). Swap is mount-compatible if we hold a 2-bolt clevis standard at both ends.

## 4. Mass contribution

4× actuator ~9 lb each + controller + brackets ≈ **~45 lb** (in the ~200 lb pop-up assembly line of the mass budget).

## 5. Open questions

1. Encoder sync (closed loop) vs. hydraulic-style flow-divider simplicity — committed to electronic sync; which controller (FIRGELLI FCB-4, PA's 4-ch box, or DIY ESP32 + hall counters feeding Cerbo)?
2. Hitched interlock signal source: 7-pin presence, GPS speed via Cerbo, or manual key switch (V0.1 = key switch, revisit V0.5)
3. Corner post bushing material (UHMW vs bronze) for rack stiffness
4. Snow-load alarm: strain on actuator current draw as proxy — nice-to-have, log current in V0.1 rig anyway

## 6. V0.1 bench plan

Steel test frame with 4 corner posts at true trailer geometry → mount PA-17s → tune sync controller → 50-cycle gate with 200 lb distributed load, rack measured by cross-corner laser/level at top of stroke → then 10 cycles with deliberate 60/40 load imbalance (wind stand-in) → log current signatures per corner.

---
*Detailed 2026-07-07. 24V-rail decision per Sourcing doc §1 (true 48V actuators are quote-only).*
