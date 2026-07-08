# Slipstream — Engineering Design Tracks

Subsystem-by-subsystem detailing of the V0.1 bench scope (see `docs/PROJECT-SLIPSTREAM-Prototype-Roadmap.md` Part II.1). Same method as the House BUS design tracks: every component names its interface back to the trailer's shared systems, every decision traces to a locked decision (roadmap I.2), and every track carries its V0.1 gate.

## Interface map (T1–T10)

| ID | Interface | Owner track |
|---|---|---|
| T1 | 48V DC bus (battery ↔ inverter ↔ loads) | SS02 |
| T2 | Tow interface (hitch, brakes, 7-pin, brake controller) | SS05 |
| T3 | AC power (NEMA 14-50 shore in / pass-through out) | SS02 |
| T4 | Solar roof (panels → MPPT → T1) | SS02 |
| T5 | Water (tanks-in-frame, pump, heater, gray routing) | SS05 (volumes) / later track (systems) |
| T6 | Structure (frame rails, hardpoints, shell mounting) | SS05 |
| T7 | Pop-up mechanism (actuators, seal, latches) | SS03 |
| T8 | Thermal envelope (shell R-value, AC penetration) | SS04 |
| T9 | Monitoring & control (Cerbo GX, VRM, smart relays) | SS02 |
| T10 | Chassis ground / bonding | SS02 |

## Tracks

| Track | Subsystem | V0.1 gate it feeds | Status |
|---|---|---|---|
| [SS01](SS01_Battery_Pack.design.md) | Battery pack (12 kWh-class 48V LFP) | Gate 1: ≥11.5 kWh usable, 50A cont., BMS verified | Detailed v0.1 |
| [SS02](SS02_Electrical_Core.design.md) | Electrical core (Victron spine, AC in/out) | Gate 2: 7-day simulated load unattended | Detailed v0.1 |
| [SS03](SS03_Popup_Actuation.design.md) | Pop-up actuation (quad actuator rig) | Gate 3: 50 cycles, 200 lb, ≤1° rack | Detailed v0.1 |
| [SS04](SS04_Composite_Shell.design.md) | Composite shell (foam-core panels) | Panel samples: structural + water-intrusion tests | Detailed v0.1 |
| [SS05](SS05_Frame_and_Chassis.design.md) | Frame & chassis (alu frame, axle, tow) | Gate 7: fabricator quote signed ≤$6,000 | Detailed v0.1 |
| [SS06](SS06_Aero_CFD.design.md) | Aero / CFD | Gates 4-5: ≤10% drag added @65 mph; tunnel within 15% | Detailed v0.1 |

**Sequence:** SS01 + SS02 first (bench electrical is the long pole and everything monitors through it) → SS03 rig → SS04 samples in parallel → SS05 drawings/quote → SS06 runs continuously from locked geometry.

Weight discipline: every track lists its mass contribution against the 1,900 lb dry target. Tongue weight never exceeds 350 lb (roadmap I.3).
