# Live Combat Log — Ice Troll vs Adventurer-1 (v4 playtest)

RNG source: `random.SystemRandom()` (OS entropy, via Python 3). Computation method: (a) Computed externally — Python script executed all rolls and all arithmetic (Core Test 9-step transaction, Skill Roll Pool cascade, Overflow, Recovery). LLM did not hand-compute any roll or arithmetic result.

> R1 pre-combat: Frightened (Tier-1, Value -1) applied to Adventurer-1 via scene-state Condition Clause binding on Ice Troll's Appearance:Hideous (DEC-094), active from start of combat while Troll is perceivable. Source pathway: scene-state binding (not a won S-1 Effect).

> SCAFFOLD: Attack selection. SC-XX remains open. Ice Troll alternates Icy Claws (odd rounds)/Sharktoothed Maw (even rounds). Prompt-level scaffold only, not a rule/precedent (Gap 6.2).
> SCAFFOLD: Quality->Wound Tier mapping table (1-9=T1/Base,10-19=T2/Gated,20-29=T3/Gated,30+=T4/Gated). Prompt-level scaffold, non-canonical (Gap 6.1).
> SCAFFOLD: HP floor convention - clamp to 0, preserve pre-clamp value in log (Gap 6.3).
> SCAFFOLD: DEC-012 exception - Adventurer-1's Attack2/Defence2 are pre-built Tier-2 skills, prompt-level scaffold only, NOT register-backed (see mandatory provenance note).
> EXECUTION NOTE (not a scaffold): Adventurer-1 has exactly one attack skill (Attack2) and one defense skill (Defence2), so no action-selection ambiguity exists on the PC side (unlike the Troll's SC-XX gap).
> EXECUTION NOTE (not a scaffold): interpretation of how DEC-013 (S-1)/DEC-044-050 (Active Defense)/DEC-096/DEC-097/DEC-101 combine into a single exchange procedure is stated explicitly in the Final Report methodology section for audit, since no single DEC spells out the combined algorithm.

| Round | Turn | Step | Actor | Skill Used | d100 Roll | Success/Fail | Margin | Quality | Cost | PE Before | PE After Cost | Overflow | HP Overflow Dmg | Recovery | PE Final | Effect Selected | Location Index | Location Zone | Wound Tier | Condition Applied | Active Defense Mitigation | Net HP Change |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Turn order R1** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 1 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 19 | Success | 48 | 48 | 19 | 220 | 201 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Arms Tier-4 Wound -4) | 58 | Arms | 4 | - | 0 | - |
| 1 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 51 | Fail | 0 | 0 | 51 | 150 | 99 | 0 | 0 | 50 | 149 | - | - | - | - | - | - | - |
| *Outcome R1 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 1 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 25 | Fail | 0 | 0 | 25 | 149 | 124 | 0 | 0 | 50 | 150 | - | - | - | - | - | - | - |
| *Outcome R1 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R1** | PC HP=600 / Troll HP=705 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R2** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 2 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 62 | Success | 13 | 13 | 62 | 220 | 158 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-2 Wound -2) | 5 | Legs | 2 | - | 0 | - |
| 2 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 65 | Fail | 0 | 0 | 65 | 150 | 85 | 0 | 0 | 50 | 135 | - | - | - | - | - | - | - |
| *Outcome R2 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 2 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 92 | Fail | 0 | 0 | 92 | 135 | 43 | 0 | 0 | 50 | 93 | - | - | - | - | - | - | - |
| *Outcome R2 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R2** | PC HP=600 / Troll HP=705 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R3** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 3 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 16 | Success | 51 | 51 | 16 | 220 | 204 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-4 Wound -4) | 6 | Legs | 4 | - | 0 | - |
| 3 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 96 | Fail | 0 | 0 | 96 | 93 | 0 | 3 | 3 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R3 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 3 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 85 | Fail | 0 | 0 | 85 | 50 | 0 | 35 | 35 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R3 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R3** | PC HP=562 / Troll HP=705 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R4** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 4 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 66 | Success | 9 | 9 | 66 | 220 | 154 | 0 | 0 | 70 | 220 | Inflict Injury (Base) magnitude 9 | - | - | - | - | 0 | -9 |
| 4 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 55 | Fail | 0 | 0 | 55 | 50 | 0 | 5 | 5 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R4 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 4 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 43 | Fail | 0 | 0 | 43 | 50 | 7 | 0 | 0 | 50 | 57 | - | - | - | - | - | - | - |
| *Outcome R4 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R4** | PC HP=548 / Troll HP=705 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R5** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 5 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 12 | Success | 55 | 55 | 12 | 220 | 208 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-4 Wound -4) | 15 | Legs | 4 | - | 0 | - |
| 5 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 71 | Fail | 0 | 0 | 71 | 57 | 0 | 14 | 14 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R5 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 5 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 60 | Fail | 0 | 0 | 60 | 50 | 0 | 10 | 10 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R5 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R5** | PC HP=524 / Troll HP=705 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R6** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 6 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 44 | Success | 31 | 31 | 44 | 220 | 176 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 81 | Head | 4 | - | 0 | - |
| 6 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 93 | Fail | 0 | 0 | 93 | 50 | 0 | 43 | 43 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R6 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 6 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 3 | Success | 26 | 26 | 3 | 50 | 47 | 0 | 0 | 50 | 97 | - | - | - | - | - | 29 | - |
| 6 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 8 | Success | 29 | 29 | 8 | 220 | 212 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R6 PC->Troll* | Ice Troll wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| **End R6** | PC HP=481 / Troll HP=705 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R7** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 7 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 74 | Fail | 0 | 0 | 74 | 220 | 146 | 0 | 0 | 70 | 216 | - | - | - | - | - | - | - |
| *Outcome R7 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 7 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 100 | FUMBLE | 0 | 0 | 100 | 97 | 0 | 3 | 3 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R7 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R7** | PC HP=478 / Troll HP=705 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R8** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 8 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 91 | Fail | 0 | 0 | 91 | 216 | 125 | 0 | 0 | 70 | 195 | - | - | - | - | - | - | - |
| *Outcome R8 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 8 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 40 | Fail | 0 | 0 | 40 | 50 | 10 | 0 | 0 | 50 | 60 | - | - | - | - | - | - | - |
| *Outcome R8 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R8** | PC HP=478 / Troll HP=705 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R9** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 9 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 27 | Success | 40 | 40 | 27 | 195 | 168 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-4 Wound -4) | 18 | Legs | 4 | - | 26 | - |
| 9 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 5 | Success | 26 | 26 | 5 | 60 | 55 | 0 | 0 | 50 | 105 | - | - | - | - | - | - | - |
| *Outcome R9 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 26 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 9 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 52 | Fail | 0 | 0 | 52 | 105 | 53 | 0 | 0 | 50 | 103 | - | - | - | - | - | - | - |
| *Outcome R9 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R9** | PC HP=478 / Troll HP=705 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R10** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 10 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 92 | Fail | 0 | 0 | 92 | 220 | 128 | 0 | 0 | 70 | 198 | - | - | - | - | - | - | - |
| *Outcome R10 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 10 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 92 | Fail | 0 | 0 | 92 | 103 | 11 | 0 | 0 | 50 | 61 | - | - | - | - | - | - | - |
| *Outcome R10 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R10** | PC HP=478 / Troll HP=705 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R11** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 11 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 36 | Success | 31 | 31 | 36 | 198 | 162 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 82 | Head | 4 | - | 26 | - |
| 11 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 5 | Success | 26 | 26 | 5 | 61 | 56 | 0 | 0 | 50 | 106 | - | - | - | - | - | - | - |
| *Outcome R11 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 26 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 11 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 80 | Fail | 0 | 0 | 80 | 106 | 26 | 0 | 0 | 50 | 76 | - | - | - | - | - | - | - |
| *Outcome R11 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R11** | PC HP=478 / Troll HP=705 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R12** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 12 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 28 | Success | 47 | 47 | 28 | 220 | 192 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Arms Tier-4 Wound -4) | 75 | Arms | 4 | - | 8 | - |
| 12 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 23 | Success | 8 | 8 | 23 | 76 | 53 | 0 | 0 | 50 | 103 | - | - | - | - | - | - | - |
| *Outcome R12 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 8 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 12 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 34 | Fail | 0 | 0 | 34 | 103 | 69 | 0 | 0 | 50 | 119 | - | - | - | - | - | - | - |
| *Outcome R12 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R12** | PC HP=478 / Troll HP=705 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R13** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 13 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 37 | Success | 30 | 30 | 37 | 220 | 183 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Arms Tier-4 Wound -4) | 55 | Arms | 4 | - | 0 | - |
| 13 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 70 | Fail | 0 | 0 | 70 | 119 | 49 | 0 | 0 | 50 | 99 | - | - | - | - | - | - | - |
| *Outcome R13 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 13 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 64 | Fail | 0 | 0 | 64 | 99 | 35 | 0 | 0 | 50 | 85 | - | - | - | - | - | - | - |
| *Outcome R13 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R13** | PC HP=478 / Troll HP=705 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R14** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 14 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 80 | Fail | 0 | 0 | 80 | 220 | 140 | 0 | 0 | 70 | 210 | - | - | - | - | - | - | - |
| *Outcome R14 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 14 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 26 | Success | 7 | 7 | 26 | 85 | 59 | 0 | 0 | 50 | 109 | Inflict Injury (Base) magnitude 7 | - | - | - | - | 0 | -7 |
| 14 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 71 | Fail | 0 | 0 | 71 | 210 | 139 | 0 | 0 | 70 | 209 | - | - | - | - | - | - | - |
| *Outcome R14 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R14** | PC HP=478 / Troll HP=698 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R15** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 15 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 55 | Success | 12 | 12 | 55 | 209 | 154 | 0 | 0 | 70 | 220 | - | - | - | - | - | 24 | - |
| 15 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 8 | Success | 24 | 24 | 8 | 109 | 101 | 0 | 0 | 50 | 150 | - | - | - | - | - | - | - |
| *Outcome R15 Troll->PC* | Adventurer-1 wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| 15 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 34 | Fail | 0 | 0 | 34 | 150 | 116 | 0 | 0 | 50 | 150 | - | - | - | - | - | - | - |
| *Outcome R15 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R15** | PC HP=478 / Troll HP=698 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R16** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 16 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 54 | Success | 21 | 21 | 54 | 220 | 166 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Arms Tier-3 Wound -3) | 52 | Arms | 3 | - | 17 | - |
| 16 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 15 | Success | 17 | 17 | 15 | 150 | 135 | 0 | 0 | 50 | 150 | - | - | - | - | - | - | - |
| *Outcome R16 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 17 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 16 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 66 | Fail | 0 | 0 | 66 | 150 | 84 | 0 | 0 | 50 | 134 | - | - | - | - | - | - | - |
| *Outcome R16 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R16** | PC HP=478 / Troll HP=698 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R17** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 17 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 66 | Success | 1 | 1 | 66 | 220 | 154 | 0 | 0 | 70 | 220 | Inflict Injury (Base) magnitude 1 | - | - | - | - | 0 | -1 |
| 17 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 45 | Fail | 0 | 0 | 45 | 134 | 89 | 0 | 0 | 50 | 139 | - | - | - | - | - | - | - |
| *Outcome R17 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 17 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 64 | Fail | 0 | 0 | 64 | 139 | 75 | 0 | 0 | 50 | 125 | - | - | - | - | - | - | - |
| *Outcome R17 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R17** | PC HP=477 / Troll HP=698 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R18** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 18 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 25 | Success | 50 | 50 | 25 | 220 | 195 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Torso Tier-4 Wound -4) | 36 | Torso | 4 | - | 0 | - |
| 18 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 47 | Fail | 0 | 0 | 47 | 125 | 78 | 0 | 0 | 50 | 128 | - | - | - | - | - | - | - |
| *Outcome R18 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 18 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 29 | Success | 5 | 5 | 29 | 128 | 99 | 0 | 0 | 50 | 149 | Inflict Injury (Base) magnitude 5 | - | - | - | - | 0 | -5 |
| 18 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 80 | Fail | 0 | 0 | 80 | 220 | 140 | 0 | 0 | 70 | 210 | - | - | - | - | - | - | - |
| *Outcome R18 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R18** | PC HP=477 / Troll HP=693 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R19** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 19 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 50 | Success | 17 | 17 | 50 | 210 | 160 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-2 Wound -2) | 19 | Legs | 2 | - | 0 | - |
| 19 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 97 | Fail | 0 | 0 | 97 | 149 | 52 | 0 | 0 | 50 | 102 | - | - | - | - | - | - | - |
| *Outcome R19 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 19 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 12 | Success | 22 | 22 | 12 | 102 | 90 | 0 | 0 | 50 | 140 | Impose Condition: Wounded (Location Torso Tier-3 Wound -3) | 40 | Torso | 3 | - | 0 | - |
| 19 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 53 | Fail | 0 | 0 | 53 | 220 | 167 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R19 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R19** | PC HP=477 / Troll HP=693 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R20** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 20 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 71 | Success | 4 | 4 | 71 | 220 | 149 | 0 | 0 | 70 | 219 | - | - | - | - | - | 11 | - |
| 20 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 23 | Success | 11 | 11 | 23 | 140 | 117 | 0 | 0 | 50 | 150 | - | - | - | - | - | - | - |
| *Outcome R20 Troll->PC* | Adventurer-1 wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| 20 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 80 | Fail | 0 | 0 | 80 | 150 | 70 | 0 | 0 | 50 | 120 | - | - | - | - | - | - | - |
| *Outcome R20 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R20** | PC HP=477 / Troll HP=693 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R21** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 21 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 7 | Success | 60 | 60 | 7 | 219 | 212 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 86 | Head | 4 | - | 4 | - |
| 21 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 30 | Success | 4 | 4 | 30 | 120 | 90 | 0 | 0 | 50 | 140 | - | - | - | - | - | - | - |
| *Outcome R21 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 4 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 21 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 36 | Fail | 0 | 0 | 36 | 140 | 104 | 0 | 0 | 50 | 150 | - | - | - | - | - | - | - |
| *Outcome R21 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R21** | PC HP=477 / Troll HP=693 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R22** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 22 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 34 | Success | 41 | 41 | 34 | 220 | 186 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-4 Wound -4) | 18 | Legs | 4 | - | 0 | - |
| 22 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 65 | Fail | 0 | 0 | 65 | 150 | 85 | 0 | 0 | 50 | 135 | - | - | - | - | - | - | - |
| *Outcome R22 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 22 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 41 | Fail | 0 | 0 | 41 | 135 | 94 | 0 | 0 | 50 | 144 | - | - | - | - | - | - | - |
| *Outcome R22 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R22** | PC HP=477 / Troll HP=693 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R23** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 23 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 42 | Success | 25 | 25 | 42 | 220 | 178 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Torso Tier-3 Wound -3) | 41 | Torso | 3 | - | 0 | - |
| 23 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 68 | Fail | 0 | 0 | 68 | 144 | 76 | 0 | 0 | 50 | 126 | - | - | - | - | - | - | - |
| *Outcome R23 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 23 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 61 | Fail | 0 | 0 | 61 | 126 | 65 | 0 | 0 | 50 | 115 | - | - | - | - | - | - | - |
| *Outcome R23 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R23** | PC HP=477 / Troll HP=693 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R24** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 24 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 41 | Success | 34 | 34 | 41 | 220 | 179 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-4 Wound -4) | 22 | Legs | 4 | - | 14 | - |
| 24 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 21 | Success | 14 | 14 | 21 | 115 | 94 | 0 | 0 | 50 | 144 | - | - | - | - | - | - | - |
| *Outcome R24 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 14 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 24 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 49 | Fail | 0 | 0 | 49 | 144 | 95 | 0 | 0 | 50 | 145 | - | - | - | - | - | - | - |
| *Outcome R24 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R24** | PC HP=477 / Troll HP=693 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R25** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 25 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 34 | Success | 33 | 33 | 34 | 220 | 186 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 85 | Head | 4 | - | 25 | - |
| 25 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 10 | Success | 25 | 25 | 10 | 145 | 135 | 0 | 0 | 50 | 150 | - | - | - | - | - | - | - |
| *Outcome R25 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 25 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 25 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 57 | Fail | 0 | 0 | 57 | 150 | 93 | 0 | 0 | 50 | 143 | - | - | - | - | - | - | - |
| *Outcome R25 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R25** | PC HP=477 / Troll HP=693 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R26** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 26 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 75 | Success | 0 | 0 | 75 | 220 | 145 | 0 | 0 | 70 | 215 | - | - | - | - | - | 12 | - |
| 26 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 23 | Success | 12 | 12 | 23 | 143 | 120 | 0 | 0 | 50 | 150 | - | - | - | - | - | - | - |
| *Outcome R26 Troll->PC* | Adventurer-1 wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| 26 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 21 | Success | 14 | 14 | 21 | 150 | 129 | 0 | 0 | 50 | 150 | Impose Condition: Wounded (Location Arms Tier-2 Wound -2) | 53 | Arms | 2 | - | 6 | - |
| 26 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 32 | Success | 6 | 6 | 32 | 215 | 183 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R26 PC->Troll* | Adventurer-1 wins on Quality; mitigated by defender's Margin 6 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| **End R26** | PC HP=477 / Troll HP=693 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R27** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 27 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 97 | Fail | 0 | 0 | 97 | 220 | 123 | 0 | 0 | 70 | 193 | - | - | - | - | - | - | - |
| *Outcome R27 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 27 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 27 | Success | 8 | 8 | 27 | 150 | 123 | 0 | 0 | 50 | 150 | Inflict Injury (Base) magnitude 1 | - | - | - | - | 7 | -1 |
| 27 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 31 | Success | 7 | 7 | 31 | 193 | 162 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R27 PC->Troll* | Adventurer-1 wins on Quality; mitigated by defender's Margin 7 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| **End R27** | PC HP=477 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R28** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 28 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 28 | Success | 47 | 47 | 28 | 220 | 192 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Arms Tier-4 Wound -4) | 73 | Arms | 4 | - | 0 | - |
| 28 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 68 | Fail | 0 | 0 | 68 | 150 | 82 | 0 | 0 | 50 | 132 | - | - | - | - | - | - | - |
| *Outcome R28 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 28 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 9 | Success | 26 | 26 | 9 | 132 | 123 | 0 | 0 | 50 | 150 | Impose Condition: Wounded (Location Head Tier-3 Wound -3) | 96 | Head | 3 | - | 0 | - |
| 28 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 56 | Fail | 0 | 0 | 56 | 220 | 164 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R28 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R28** | PC HP=477 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R29** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 29 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 24 | Success | 43 | 43 | 24 | 220 | 196 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-4 Wound -4) | 1 | Legs | 4 | - | 0 | - |
| 29 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 65 | Fail | 0 | 0 | 65 | 150 | 85 | 0 | 0 | 50 | 135 | - | - | - | - | - | - | - |
| *Outcome R29 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 29 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 21 | Success | 14 | 14 | 21 | 135 | 114 | 0 | 0 | 50 | 150 | - | - | - | - | - | 34 | - |
| 29 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 4 | Success | 34 | 34 | 4 | 220 | 216 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R29 PC->Troll* | Ice Troll wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| **End R29** | PC HP=477 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R30** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 30 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 60 | Success | 15 | 15 | 60 | 220 | 160 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Torso Tier-2 Wound -2) | 26 | Torso | 2 | - | 1 | - |
| 30 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 34 | Success | 1 | 1 | 34 | 150 | 116 | 0 | 0 | 50 | 150 | - | - | - | - | - | - | - |
| *Outcome R30 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 1 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 30 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 87 | Fail | 0 | 0 | 87 | 150 | 63 | 0 | 0 | 50 | 113 | - | - | - | - | - | - | - |
| *Outcome R30 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R30** | PC HP=477 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R31** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 31 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 100 | FUMBLE | 0 | 0 | 100 | 220 | 120 | 0 | 0 | 70 | 190 | - | - | - | - | - | - | - |
| *Outcome R31 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 31 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 73 | Fail | 0 | 0 | 73 | 113 | 40 | 0 | 0 | 50 | 90 | - | - | - | - | - | - | - |
| *Outcome R31 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R31** | PC HP=477 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R32** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 32 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 51 | Success | 24 | 24 | 51 | 190 | 139 | 0 | 0 | 70 | 209 | Impose Condition: Wounded (Location Arms Tier-3 Wound -3) | 70 | Arms | 3 | - | 0 | - |
| 32 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 50 | Fail | 0 | 0 | 50 | 90 | 40 | 0 | 0 | 50 | 90 | - | - | - | - | - | - | - |
| *Outcome R32 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 32 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 84 | Fail | 0 | 0 | 84 | 90 | 6 | 0 | 0 | 50 | 56 | - | - | - | - | - | - | - |
| *Outcome R32 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R32** | PC HP=477 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R33** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 33 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 3 | Success | 64 | 64 | 3 | 209 | 206 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 85 | Head | 4 | - | 0 | - |
| 33 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 65 | Fail | 0 | 0 | 65 | 56 | 0 | 9 | 9 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R33 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 33 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 85 | Fail | 0 | 0 | 85 | 50 | 0 | 35 | 35 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R33 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R33** | PC HP=433 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R34** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 34 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 58 | Success | 17 | 17 | 58 | 220 | 162 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Torso Tier-2 Wound -2) | 30 | Torso | 2 | - | 0 | - |
| 34 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 49 | Fail | 0 | 0 | 49 | 50 | 1 | 0 | 0 | 50 | 51 | - | - | - | - | - | - | - |
| *Outcome R34 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 34 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 67 | Fail | 0 | 0 | 67 | 51 | 0 | 16 | 16 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R34 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R34** | PC HP=417 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R35** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 35 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 81 | Fail | 0 | 0 | 81 | 220 | 139 | 0 | 0 | 70 | 209 | - | - | - | - | - | - | - |
| *Outcome R35 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 35 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 53 | Fail | 0 | 0 | 53 | 50 | 0 | 3 | 3 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R35 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R35** | PC HP=414 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R36** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 36 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 33 | Success | 42 | 42 | 33 | 209 | 176 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Arms Tier-4 Wound -4) | 72 | Arms | 4 | - | 19 | - |
| 36 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 16 | Success | 19 | 19 | 16 | 50 | 34 | 0 | 0 | 50 | 84 | - | - | - | - | - | - | - |
| *Outcome R36 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 19 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 36 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 67 | Fail | 0 | 0 | 67 | 84 | 17 | 0 | 0 | 50 | 67 | - | - | - | - | - | - | - |
| *Outcome R36 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R36** | PC HP=414 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R37** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 37 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 9 | Success | 58 | 58 | 9 | 220 | 211 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Torso Tier-4 Wound -4) | 50 | Torso | 4 | - | 0 | - |
| 37 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 48 | Fail | 0 | 0 | 48 | 67 | 19 | 0 | 0 | 50 | 69 | - | - | - | - | - | - | - |
| *Outcome R37 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 37 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 4 | Success | 35 | 35 | 4 | 69 | 65 | 0 | 0 | 50 | 115 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 98 | Head | 4 | - | 0 | - |
| 37 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 88 | Fail | 0 | 0 | 88 | 220 | 132 | 0 | 0 | 70 | 202 | - | - | - | - | - | - | - |
| *Outcome R37 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R37** | PC HP=414 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R38** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 38 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 52 | Success | 23 | 23 | 52 | 202 | 150 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Arms Tier-3 Wound -3) | 60 | Arms | 3 | - | 0 | - |
| 38 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 63 | Fail | 0 | 0 | 63 | 115 | 52 | 0 | 0 | 50 | 102 | - | - | - | - | - | - | - |
| *Outcome R38 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 38 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 21 | Success | 18 | 18 | 21 | 102 | 81 | 0 | 0 | 50 | 131 | - | - | - | - | - | 35 | - |
| 38 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 4 | Success | 35 | 35 | 4 | 220 | 216 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R38 PC->Troll* | Ice Troll wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| **End R38** | PC HP=414 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R39** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 39 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 98 | Fail | 0 | 0 | 98 | 220 | 122 | 0 | 0 | 70 | 192 | - | - | - | - | - | - | - |
| *Outcome R39 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 39 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 43 | Fail | 0 | 0 | 43 | 131 | 88 | 0 | 0 | 50 | 138 | - | - | - | - | - | - | - |
| *Outcome R39 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R39** | PC HP=414 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R40** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 40 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 87 | Fail | 0 | 0 | 87 | 192 | 105 | 0 | 0 | 70 | 175 | - | - | - | - | - | - | - |
| *Outcome R40 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 40 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 78 | Fail | 0 | 0 | 78 | 138 | 60 | 0 | 0 | 50 | 110 | - | - | - | - | - | - | - |
| *Outcome R40 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R40** | PC HP=414 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R41** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 41 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 40 | Success | 27 | 27 | 40 | 175 | 135 | 0 | 0 | 70 | 205 | Impose Condition: Wounded (Location Torso Tier-3 Wound -3) | 29 | Torso | 3 | - | 0 | - |
| 41 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 63 | Fail | 0 | 0 | 63 | 110 | 47 | 0 | 0 | 50 | 97 | - | - | - | - | - | - | - |
| *Outcome R41 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 41 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 56 | Fail | 0 | 0 | 56 | 97 | 41 | 0 | 0 | 50 | 91 | - | - | - | - | - | - | - |
| *Outcome R41 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R41** | PC HP=414 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R42** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 42 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 53 | Success | 22 | 22 | 53 | 205 | 152 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-3 Wound -3) | 88 | Head | 3 | - | 0 | - |
| 42 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 89 | Fail | 0 | 0 | 89 | 91 | 2 | 0 | 0 | 50 | 52 | - | - | - | - | - | - | - |
| *Outcome R42 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 42 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 81 | Fail | 0 | 0 | 81 | 52 | 0 | 29 | 29 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R42 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R42** | PC HP=385 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R43** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 43 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 63 | Success | 4 | 4 | 63 | 220 | 157 | 0 | 0 | 70 | 220 | Inflict Injury (Base) magnitude 4 | - | - | - | - | 0 | -4 |
| 43 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 61 | Fail | 0 | 0 | 61 | 50 | 0 | 11 | 11 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R43 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 43 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 49 | Fail | 0 | 0 | 49 | 50 | 1 | 0 | 0 | 50 | 51 | - | - | - | - | - | - | - |
| *Outcome R43 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R43** | PC HP=370 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R44** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 44 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 70 | Success | 5 | 5 | 70 | 220 | 150 | 0 | 0 | 70 | 220 | Inflict Injury (Base) magnitude 5 | - | - | - | - | 0 | -5 |
| 44 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 74 | Fail | 0 | 0 | 74 | 51 | 0 | 23 | 23 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R44 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 44 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 1 | Success | 40 | 40 | 1 | 50 | 49 | 0 | 0 | 50 | 99 | Impose Condition: Wounded (Location Arms Tier-4 Wound -4) | 75 | Arms | 4 | - | 24 | - |
| 44 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 15 | Success | 24 | 24 | 15 | 220 | 205 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R44 PC->Troll* | Adventurer-1 wins on Quality; mitigated by defender's Margin 24 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| **End R44** | PC HP=342 / Troll HP=692 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R45** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 45 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 23 | Success | 44 | 44 | 23 | 220 | 197 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-4 Wound -4) | 18 | Legs | 4 | - | 0 | - |
| 45 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 38 | Fail | 0 | 0 | 38 | 99 | 61 | 0 | 0 | 50 | 111 | - | - | - | - | - | - | - |
| *Outcome R45 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 45 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 32 | Success | 9 | 9 | 32 | 111 | 79 | 0 | 0 | 50 | 129 | Inflict Injury (Base) magnitude 9 | - | - | - | - | 0 | -9 |
| 45 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 59 | Fail | 0 | 0 | 59 | 220 | 161 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R45 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R45** | PC HP=342 / Troll HP=683 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R46** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 46 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 28 | Success | 47 | 47 | 28 | 220 | 192 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-4 Wound -4) | 9 | Legs | 4 | - | 0 | - |
| 46 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 40 | Fail | 0 | 0 | 40 | 129 | 89 | 0 | 0 | 50 | 139 | - | - | - | - | - | - | - |
| *Outcome R46 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 46 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 86 | Fail | 0 | 0 | 86 | 139 | 53 | 0 | 0 | 50 | 103 | - | - | - | - | - | - | - |
| *Outcome R46 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R46** | PC HP=342 / Troll HP=683 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R47** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 47 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 32 | Success | 35 | 35 | 32 | 220 | 188 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 100 | Head | 4 | - | 0 | - |
| 47 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 96 | Fail | 0 | 0 | 96 | 103 | 7 | 0 | 0 | 50 | 57 | - | - | - | - | - | - | - |
| *Outcome R47 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 47 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 44 | Fail | 0 | 0 | 44 | 57 | 13 | 0 | 0 | 50 | 63 | - | - | - | - | - | - | - |
| *Outcome R47 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R47** | PC HP=342 / Troll HP=683 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R48** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 48 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 52 | Success | 23 | 23 | 52 | 220 | 168 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-3 Wound -3) | 81 | Head | 3 | - | 0 | - |
| 48 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 51 | Fail | 0 | 0 | 51 | 63 | 12 | 0 | 0 | 50 | 62 | - | - | - | - | - | - | - |
| *Outcome R48 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 48 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 66 | Fail | 0 | 0 | 66 | 62 | 0 | 4 | 4 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R48 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R48** | PC HP=338 / Troll HP=683 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R49** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 49 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 90 | Fail | 0 | 0 | 90 | 220 | 130 | 0 | 0 | 70 | 200 | - | - | - | - | - | - | - |
| *Outcome R49 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 49 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 93 | Fail | 0 | 0 | 93 | 50 | 0 | 43 | 43 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R49 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R49** | PC HP=295 / Troll HP=683 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R50** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 50 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 48 | Success | 27 | 27 | 48 | 200 | 152 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-3 Wound -3) | 13 | Legs | 3 | - | 19 | - |
| 50 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 19 | Success | 19 | 19 | 19 | 50 | 31 | 0 | 0 | 50 | 81 | - | - | - | - | - | - | - |
| *Outcome R50 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 19 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 50 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 10 | Success | 33 | 33 | 10 | 81 | 71 | 0 | 0 | 50 | 121 | Impose Condition: Wounded (Location Arms Tier-4 Wound -4) | 56 | Arms | 4 | - | 0 | - |
| 50 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 67 | Fail | 0 | 0 | 67 | 220 | 153 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R50 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R50** | PC HP=295 / Troll HP=683 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R51** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 51 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 92 | Fail | 0 | 0 | 92 | 220 | 128 | 0 | 0 | 70 | 198 | - | - | - | - | - | - | - |
| *Outcome R51 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 51 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 50 | Fail | 0 | 0 | 50 | 121 | 71 | 0 | 0 | 50 | 121 | - | - | - | - | - | - | - |
| *Outcome R51 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R51** | PC HP=295 / Troll HP=683 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R52** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 52 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 32 | Success | 43 | 43 | 32 | 198 | 166 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Arms Tier-4 Wound -4) | 58 | Arms | 4 | - | 0 | - |
| 52 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 43 | Fail | 0 | 0 | 43 | 121 | 78 | 0 | 0 | 50 | 128 | - | - | - | - | - | - | - |
| *Outcome R52 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 52 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 5 | Success | 38 | 38 | 5 | 128 | 123 | 0 | 0 | 50 | 150 | Impose Condition: Wounded (Location Arms Tier-4 Wound -4) | 52 | Arms | 4 | - | 0 | - |
| 52 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 52 | Fail | 0 | 0 | 52 | 220 | 168 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R52 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R52** | PC HP=295 / Troll HP=683 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R53** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 53 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 89 | Fail | 0 | 0 | 89 | 220 | 131 | 0 | 0 | 70 | 201 | - | - | - | - | - | - | - |
| *Outcome R53 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 53 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 70 | Fail | 0 | 0 | 70 | 150 | 80 | 0 | 0 | 50 | 130 | - | - | - | - | - | - | - |
| *Outcome R53 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R53** | PC HP=295 / Troll HP=683 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R54** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 54 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 63 | Success | 12 | 12 | 63 | 201 | 138 | 0 | 0 | 70 | 208 | Impose Condition: Wounded (Location Arms Tier-2 Wound -2) | 60 | Arms | 2 | - | 0 | - |
| 54 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 49 | Fail | 0 | 0 | 49 | 130 | 81 | 0 | 0 | 50 | 131 | - | - | - | - | - | - | - |
| *Outcome R54 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 54 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 81 | Fail | 0 | 0 | 81 | 131 | 50 | 0 | 0 | 50 | 100 | - | - | - | - | - | - | - |
| *Outcome R54 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R54** | PC HP=295 / Troll HP=683 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R55** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 55 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 96 | Fail | 0 | 0 | 96 | 208 | 112 | 0 | 0 | 70 | 182 | - | - | - | - | - | - | - |
| *Outcome R55 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 55 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 78 | Fail | 0 | 0 | 78 | 100 | 22 | 0 | 0 | 50 | 72 | - | - | - | - | - | - | - |
| *Outcome R55 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R55** | PC HP=295 / Troll HP=683 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R56** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 56 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 78 | Fail | 0 | 0 | 78 | 182 | 104 | 0 | 0 | 70 | 174 | - | - | - | - | - | - | - |
| *Outcome R56 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 56 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 26 | Success | 17 | 17 | 26 | 72 | 46 | 0 | 0 | 50 | 96 | - | - | - | - | - | 25 | - |
| 56 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 14 | Success | 25 | 25 | 14 | 174 | 160 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R56 PC->Troll* | Ice Troll wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| **End R56** | PC HP=295 / Troll HP=683 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R57** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 57 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 62 | Success | 5 | 5 | 62 | 220 | 158 | 0 | 0 | 70 | 220 | Inflict Injury (Base) magnitude 5 | - | - | - | - | 0 | -5 |
| 57 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 39 | Fail | 0 | 0 | 39 | 96 | 57 | 0 | 0 | 50 | 107 | - | - | - | - | - | - | - |
| *Outcome R57 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 57 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 40 | Success | 3 | 3 | 40 | 107 | 67 | 0 | 0 | 50 | 117 | Inflict Injury (Base) magnitude 3 | - | - | - | - | 0 | -3 |
| 57 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 100 | FUMBLE | 0 | 0 | 100 | 220 | 120 | 0 | 0 | 70 | 190 | - | - | - | - | - | - | - |
| *Outcome R57 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R57** | PC HP=290 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R58** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 58 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 9 | Success | 66 | 66 | 9 | 190 | 181 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Torso Tier-4 Wound -4) | 43 | Torso | 4 | - | 0 | - |
| 58 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 87 | Fail | 0 | 0 | 87 | 117 | 30 | 0 | 0 | 50 | 80 | - | - | - | - | - | - | - |
| *Outcome R58 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 58 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 98 | Fail | 0 | 0 | 98 | 80 | 0 | 18 | 18 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R58 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R58** | PC HP=272 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R59** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 59 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 3 | Success | 64 | 64 | 3 | 220 | 217 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 79 | Head | 4 | - | 27 | - |
| 59 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 12 | Success | 27 | 27 | 12 | 50 | 38 | 0 | 0 | 50 | 88 | - | - | - | - | - | - | - |
| *Outcome R59 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 27 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 59 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 31 | Success | 13 | 13 | 31 | 88 | 57 | 0 | 0 | 50 | 107 | Impose Condition: Wounded (Location Legs Tier-2 Wound -2) | 9 | Legs | 2 | - | 0 | - |
| 59 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 90 | Fail | 0 | 0 | 90 | 220 | 130 | 0 | 0 | 70 | 200 | - | - | - | - | - | - | - |
| *Outcome R59 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R59** | PC HP=272 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R60** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 60 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 62 | Success | 13 | 13 | 62 | 200 | 138 | 0 | 0 | 70 | 208 | - | - | - | - | - | 23 | - |
| 60 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 16 | Success | 23 | 23 | 16 | 107 | 91 | 0 | 0 | 50 | 141 | - | - | - | - | - | - | - |
| *Outcome R60 Troll->PC* | Adventurer-1 wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| 60 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 14 | Success | 30 | 30 | 14 | 141 | 127 | 0 | 0 | 50 | 150 | - | - | - | - | - | 35 | - |
| 60 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 6 | Success | 35 | 35 | 6 | 208 | 202 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R60 PC->Troll* | Ice Troll wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| **End R60** | PC HP=272 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R61** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 61 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 16 | Success | 51 | 51 | 16 | 220 | 204 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 79 | Head | 4 | - | 0 | - |
| 61 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 66 | Fail | 0 | 0 | 66 | 150 | 84 | 0 | 0 | 50 | 134 | - | - | - | - | - | - | - |
| *Outcome R61 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 61 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 92 | Fail | 0 | 0 | 92 | 134 | 42 | 0 | 0 | 50 | 92 | - | - | - | - | - | - | - |
| *Outcome R61 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R61** | PC HP=272 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R62** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 62 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 42 | Success | 33 | 33 | 42 | 220 | 178 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 95 | Head | 4 | - | 24 | - |
| 62 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 15 | Success | 24 | 24 | 15 | 92 | 77 | 0 | 0 | 50 | 127 | - | - | - | - | - | - | - |
| *Outcome R62 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 24 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 62 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 71 | Fail | 0 | 0 | 71 | 127 | 56 | 0 | 0 | 50 | 106 | - | - | - | - | - | - | - |
| *Outcome R62 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R62** | PC HP=272 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R63** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 63 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 43 | Success | 24 | 24 | 43 | 220 | 177 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Arms Tier-3 Wound -3) | 54 | Arms | 3 | - | 0 | - |
| 63 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 54 | Fail | 0 | 0 | 54 | 106 | 52 | 0 | 0 | 50 | 102 | - | - | - | - | - | - | - |
| *Outcome R63 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 63 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 7 | Success | 38 | 38 | 7 | 102 | 95 | 0 | 0 | 50 | 145 | Impose Condition: Wounded (Location Arms Tier-4 Wound -4) | 72 | Arms | 4 | - | 0 | - |
| 63 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 58 | Fail | 0 | 0 | 58 | 220 | 162 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R63 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R63** | PC HP=272 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R64** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 64 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 18 | Success | 57 | 57 | 18 | 220 | 202 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 89 | Head | 4 | - | 0 | - |
| 64 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 62 | Fail | 0 | 0 | 62 | 145 | 83 | 0 | 0 | 50 | 133 | - | - | - | - | - | - | - |
| *Outcome R64 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 64 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 70 | Fail | 0 | 0 | 70 | 133 | 63 | 0 | 0 | 50 | 113 | - | - | - | - | - | - | - |
| *Outcome R64 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R64** | PC HP=272 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R65** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 65 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 59 | Success | 8 | 8 | 59 | 220 | 161 | 0 | 0 | 70 | 220 | Inflict Injury (Base) magnitude 8 | - | - | - | - | 0 | -8 |
| 65 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 68 | Fail | 0 | 0 | 68 | 113 | 45 | 0 | 0 | 50 | 95 | - | - | - | - | - | - | - |
| *Outcome R65 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 65 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 32 | Success | 13 | 13 | 32 | 95 | 63 | 0 | 0 | 50 | 113 | - | - | - | - | - | 16 | - |
| 65 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 25 | Success | 16 | 16 | 25 | 220 | 195 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R65 PC->Troll* | Ice Troll wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| **End R65** | PC HP=264 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R66** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 66 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 68 | Success | 7 | 7 | 68 | 220 | 152 | 0 | 0 | 70 | 220 | Inflict Injury (Base) magnitude 7 | - | - | - | - | 0 | -7 |
| 66 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 40 | Fail | 0 | 0 | 40 | 113 | 73 | 0 | 0 | 50 | 123 | - | - | - | - | - | - | - |
| *Outcome R66 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 66 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 89 | Fail | 0 | 0 | 89 | 123 | 34 | 0 | 0 | 50 | 84 | - | - | - | - | - | - | - |
| *Outcome R66 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R66** | PC HP=257 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R67** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 67 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 89 | Fail | 0 | 0 | 89 | 220 | 131 | 0 | 0 | 70 | 201 | - | - | - | - | - | - | - |
| *Outcome R67 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 67 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 48 | Fail | 0 | 0 | 48 | 84 | 36 | 0 | 0 | 50 | 86 | - | - | - | - | - | - | - |
| *Outcome R67 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R67** | PC HP=257 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R68** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 68 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 7 | Success | 68 | 68 | 7 | 201 | 194 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-4 Wound -4) | 6 | Legs | 4 | - | 0 | - |
| 68 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 86 | Fail | 0 | 0 | 86 | 86 | 0 | 0 | 0 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R68 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 68 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 75 | Fail | 0 | 0 | 75 | 50 | 0 | 25 | 25 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R68 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R68** | PC HP=232 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R69** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 69 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 17 | Success | 50 | 50 | 17 | 220 | 203 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 93 | Head | 4 | - | 0 | - |
| 69 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 80 | Fail | 0 | 0 | 80 | 50 | 0 | 30 | 30 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R69 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 69 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 60 | Fail | 0 | 0 | 60 | 50 | 0 | 10 | 10 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R69 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R69** | PC HP=192 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R70** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 70 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 42 | Success | 33 | 33 | 42 | 220 | 178 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Arms Tier-4 Wound -4) | 67 | Arms | 4 | - | 0 | - |
| 70 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 59 | Fail | 0 | 0 | 59 | 50 | 0 | 9 | 9 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R70 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 70 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 71 | Fail | 0 | 0 | 71 | 50 | 0 | 21 | 21 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R70 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R70** | PC HP=162 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R71** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 71 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 65 | Success | 2 | 2 | 65 | 220 | 155 | 0 | 0 | 70 | 220 | Inflict Injury (Base) magnitude 2 | - | - | - | - | 0 | -2 |
| 71 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 96 | Fail | 0 | 0 | 96 | 50 | 0 | 46 | 46 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R71 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 71 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 65 | Fail | 0 | 0 | 65 | 50 | 0 | 15 | 15 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R71 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R71** | PC HP=99 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R72** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 72 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 76 | Fail | 0 | 0 | 76 | 220 | 144 | 0 | 0 | 70 | 214 | - | - | - | - | - | - | - |
| *Outcome R72 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 72 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 44 | Success | 1 | 1 | 44 | 50 | 6 | 0 | 0 | 50 | 56 | - | - | - | - | - | 31 | - |
| 72 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 10 | Success | 31 | 31 | 10 | 214 | 204 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R72 PC->Troll* | Ice Troll wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| **End R72** | PC HP=99 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R73** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 73 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 81 | Fail | 0 | 0 | 81 | 220 | 139 | 0 | 0 | 70 | 209 | - | - | - | - | - | - | - |
| *Outcome R73 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 73 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 22 | Success | 23 | 23 | 22 | 56 | 34 | 0 | 0 | 50 | 84 | Impose Condition: Wounded (Location Legs Tier-3 Wound -3) | 23 | Legs | 3 | - | 0 | - |
| 73 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 94 | Fail | 0 | 0 | 94 | 209 | 115 | 0 | 0 | 70 | 185 | - | - | - | - | - | - | - |
| *Outcome R73 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R73** | PC HP=99 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R74** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 74 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 20 | Success | 55 | 55 | 20 | 185 | 165 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Torso Tier-4 Wound -4) | 26 | Torso | 4 | - | 0 | - |
| 74 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 97 | Fail | 0 | 0 | 97 | 84 | 0 | 13 | 13 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R74 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 74 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 46 | Fail | 0 | 0 | 46 | 50 | 4 | 0 | 0 | 50 | 54 | - | - | - | - | - | - | - |
| *Outcome R74 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R74** | PC HP=86 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R75** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 75 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 24 | Success | 43 | 43 | 24 | 220 | 196 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-4 Wound -4) | 10 | Legs | 4 | - | 0 | - |
| 75 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 64 | Fail | 0 | 0 | 64 | 54 | 0 | 10 | 10 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R75 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 75 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 49 | Fail | 0 | 0 | 49 | 50 | 1 | 0 | 0 | 50 | 51 | - | - | - | - | - | - | - |
| *Outcome R75 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R75** | PC HP=76 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R76** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 76 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 79 | Fail | 0 | 0 | 79 | 220 | 141 | 0 | 0 | 70 | 211 | - | - | - | - | - | - | - |
| *Outcome R76 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 76 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 50 | Fail | 0 | 0 | 50 | 51 | 1 | 0 | 0 | 50 | 51 | - | - | - | - | - | - | - |
| *Outcome R76 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R76** | PC HP=76 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R77** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 77 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 47 | Success | 20 | 20 | 47 | 211 | 164 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Torso Tier-3 Wound -3) | 42 | Torso | 3 | - | 0 | - |
| 77 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 74 | Fail | 0 | 0 | 74 | 51 | 0 | 23 | 23 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R77 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 77 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 26 | Success | 19 | 19 | 26 | 50 | 24 | 0 | 0 | 50 | 74 | - | - | - | - | - | 39 | - |
| 77 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 3 | Success | 39 | 39 | 3 | 220 | 217 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R77 PC->Troll* | Ice Troll wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| **End R77** | PC HP=53 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R78** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 78 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 91 | Fail | 0 | 0 | 91 | 220 | 129 | 0 | 0 | 70 | 199 | - | - | - | - | - | - | - |
| *Outcome R78 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 78 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 19 | Success | 26 | 26 | 19 | 74 | 55 | 0 | 0 | 50 | 105 | Impose Condition: Wounded (Location Arms Tier-3 Wound -3) | 61 | Arms | 3 | - | 0 | - |
| 78 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 54 | Fail | 0 | 0 | 54 | 199 | 145 | 0 | 0 | 70 | 215 | - | - | - | - | - | - | - |
| *Outcome R78 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R78** | PC HP=53 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R79** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 79 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 32 | Success | 35 | 35 | 32 | 215 | 183 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Torso Tier-4 Wound -4) | 50 | Torso | 4 | - | 17 | - |
| 79 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 26 | Success | 17 | 17 | 26 | 105 | 79 | 0 | 0 | 50 | 129 | - | - | - | - | - | - | - |
| *Outcome R79 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 17 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 79 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 91 | Fail | 0 | 0 | 91 | 129 | 38 | 0 | 0 | 50 | 88 | - | - | - | - | - | - | - |
| *Outcome R79 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R79** | PC HP=53 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R80** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 80 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 91 | Fail | 0 | 0 | 91 | 220 | 129 | 0 | 0 | 70 | 199 | - | - | - | - | - | - | - |
| *Outcome R80 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 80 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 21 | Success | 25 | 25 | 21 | 88 | 67 | 0 | 0 | 50 | 117 | Impose Condition: Wounded (Location Arms Tier-3 Wound -3) | 75 | Arms | 3 | - | 0 | - |
| 80 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 68 | Fail | 0 | 0 | 68 | 199 | 131 | 0 | 0 | 70 | 201 | - | - | - | - | - | - | - |
| *Outcome R80 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R80** | PC HP=53 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R81** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 81 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 62 | Success | 5 | 5 | 62 | 201 | 139 | 0 | 0 | 70 | 209 | - | - | - | - | - | 14 | - |
| 81 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 29 | Success | 14 | 14 | 29 | 117 | 88 | 0 | 0 | 50 | 138 | - | - | - | - | - | - | - |
| *Outcome R81 Troll->PC* | Adventurer-1 wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| 81 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 71 | Fail | 0 | 0 | 71 | 138 | 67 | 0 | 0 | 50 | 117 | - | - | - | - | - | - | - |
| *Outcome R81 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R81** | PC HP=53 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R82** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 82 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 73 | Success | 2 | 2 | 73 | 209 | 136 | 0 | 0 | 70 | 206 | Inflict Injury (Base) magnitude 2 | - | - | - | - | 0 | -2 |
| 82 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 75 | Fail | 0 | 0 | 75 | 117 | 42 | 0 | 0 | 50 | 92 | - | - | - | - | - | - | - |
| *Outcome R82 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 82 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 7 | Success | 39 | 39 | 7 | 92 | 85 | 0 | 0 | 50 | 135 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 78 | Head | 4 | - | 0 | - |
| 82 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 63 | Fail | 0 | 0 | 63 | 206 | 143 | 0 | 0 | 70 | 213 | - | - | - | - | - | - | - |
| *Outcome R82 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R82** | PC HP=51 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R83** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 83 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 48 | Success | 19 | 19 | 48 | 213 | 165 | 0 | 0 | 70 | 220 | - | - | - | - | - | 22 | - |
| 83 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 21 | Success | 22 | 22 | 21 | 135 | 114 | 0 | 0 | 50 | 150 | - | - | - | - | - | - | - |
| *Outcome R83 Troll->PC* | Adventurer-1 wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| 83 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 84 | Fail | 0 | 0 | 84 | 150 | 66 | 0 | 0 | 50 | 116 | - | - | - | - | - | - | - |
| *Outcome R83 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R83** | PC HP=51 / Troll HP=680 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R84** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 84 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 23 | Success | 52 | 52 | 23 | 220 | 197 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Arms Tier-4 Wound -4) | 51 | Arms | 4 | - | 2 | - |
| 84 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 41 | Success | 2 | 2 | 41 | 116 | 75 | 0 | 0 | 50 | 125 | - | - | - | - | - | - | - |
| *Outcome R84 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 2 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 84 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 42 | Success | 4 | 4 | 42 | 125 | 83 | 0 | 0 | 50 | 133 | Inflict Injury (Base) magnitude 4 | - | - | - | - | 0 | -4 |
| 84 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 88 | Fail | 0 | 0 | 88 | 220 | 132 | 0 | 0 | 70 | 202 | - | - | - | - | - | - | - |
| *Outcome R84 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R84** | PC HP=51 / Troll HP=676 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R85** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 85 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 69 | Fail | 0 | 0 | 69 | 202 | 133 | 0 | 0 | 70 | 203 | - | - | - | - | - | - | - |
| *Outcome R85 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 85 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 80 | Fail | 0 | 0 | 80 | 133 | 53 | 0 | 0 | 50 | 103 | - | - | - | - | - | - | - |
| *Outcome R85 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R85** | PC HP=51 / Troll HP=676 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R86** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 86 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 29 | Success | 46 | 46 | 29 | 203 | 174 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-4 Wound -4) | 24 | Legs | 4 | - | 0 | - |
| 86 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 53 | Fail | 0 | 0 | 53 | 103 | 50 | 0 | 0 | 50 | 100 | - | - | - | - | - | - | - |
| *Outcome R86 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 86 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 3 | Success | 43 | 43 | 3 | 100 | 97 | 0 | 0 | 50 | 147 | Impose Condition: Wounded (Location Torso Tier-4 Wound -4) | 27 | Torso | 4 | - | 32 | - |
| 86 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 11 | Success | 32 | 32 | 11 | 220 | 209 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R86 PC->Troll* | Adventurer-1 wins on Quality; mitigated by defender's Margin 32 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| **End R86** | PC HP=51 / Troll HP=676 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R87** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 87 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 49 | Success | 18 | 18 | 49 | 220 | 171 | 0 | 0 | 70 | 220 | - | - | - | - | - | 25 | - |
| 87 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 18 | Success | 25 | 25 | 18 | 147 | 129 | 0 | 0 | 50 | 150 | - | - | - | - | - | - | - |
| *Outcome R87 Troll->PC* | Adventurer-1 wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| 87 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 5 | Success | 41 | 41 | 5 | 150 | 145 | 0 | 0 | 50 | 150 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 93 | Head | 4 | - | 0 | - |
| 87 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 55 | Fail | 0 | 0 | 55 | 220 | 165 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R87 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R87** | PC HP=51 / Troll HP=676 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R88** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 88 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 61 | Success | 14 | 14 | 61 | 220 | 159 | 0 | 0 | 70 | 220 | - | - | - | - | - | 39 | - |
| 88 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 4 | Success | 39 | 39 | 4 | 150 | 146 | 0 | 0 | 50 | 150 | - | - | - | - | - | - | - |
| *Outcome R88 Troll->PC* | Adventurer-1 wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| 88 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 10 | Success | 36 | 36 | 10 | 150 | 140 | 0 | 0 | 50 | 150 | Impose Condition: Wounded (Location Legs Tier-4 Wound -4) | 16 | Legs | 4 | - | 0 | - |
| 88 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 46 | Fail | 0 | 0 | 46 | 220 | 174 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R88 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R88** | PC HP=51 / Troll HP=676 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R89** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 89 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 49 | Success | 18 | 18 | 49 | 220 | 171 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-2 Wound -2) | 85 | Head | 2 | - | 0 | - |
| 89 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 76 | Fail | 0 | 0 | 76 | 150 | 74 | 0 | 0 | 50 | 124 | - | - | - | - | - | - | - |
| *Outcome R89 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 89 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 44 | Success | 2 | 2 | 44 | 124 | 80 | 0 | 0 | 50 | 130 | Inflict Injury (Base) magnitude 2 | - | - | - | - | 0 | -2 |
| 89 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 46 | Fail | 0 | 0 | 46 | 220 | 174 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R89 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R89** | PC HP=51 / Troll HP=674 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R90** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 90 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 17 | Success | 58 | 58 | 17 | 220 | 203 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 91 | Head | 4 | - | 0 | - |
| 90 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 63 | Fail | 0 | 0 | 63 | 130 | 67 | 0 | 0 | 50 | 117 | - | - | - | - | - | - | - |
| *Outcome R90 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 90 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 32 | Success | 14 | 14 | 32 | 117 | 85 | 0 | 0 | 50 | 135 | Impose Condition: Wounded (Location Legs Tier-2 Wound -2) | 4 | Legs | 2 | - | 0 | - |
| 90 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 68 | Fail | 0 | 0 | 68 | 220 | 152 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R90 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R90** | PC HP=51 / Troll HP=674 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R91** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 91 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 34 | Success | 33 | 33 | 34 | 220 | 186 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-4 Wound -4) | 10 | Legs | 4 | - | 0 | - |
| 91 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 61 | Fail | 0 | 0 | 61 | 135 | 74 | 0 | 0 | 50 | 124 | - | - | - | - | - | - | - |
| *Outcome R91 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 91 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 21 | Success | 25 | 25 | 21 | 124 | 103 | 0 | 0 | 50 | 150 | Impose Condition: Wounded (Location Head Tier-3 Wound -3) | 86 | Head | 3 | - | 0 | - |
| 91 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 94 | Fail | 0 | 0 | 94 | 220 | 126 | 0 | 0 | 70 | 196 | - | - | - | - | - | - | - |
| *Outcome R91 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R91** | PC HP=51 / Troll HP=674 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R92** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 92 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 74 | Success | 1 | 1 | 74 | 196 | 122 | 0 | 0 | 70 | 192 | - | - | - | - | - | 28 | - |
| 92 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 15 | Success | 28 | 28 | 15 | 150 | 135 | 0 | 0 | 50 | 150 | - | - | - | - | - | - | - |
| *Outcome R92 Troll->PC* | Adventurer-1 wins the opposed contest (DEC-101/C-09): attack fails, no counter-Effect | | | | | | | | | | | | | | | | | | | | | |
| 92 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 91 | Fail | 0 | 0 | 91 | 150 | 59 | 0 | 0 | 50 | 109 | - | - | - | - | - | - | - |
| *Outcome R92 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R92** | PC HP=51 / Troll HP=674 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R93** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 93 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 27 | Success | 40 | 40 | 27 | 192 | 165 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 96 | Head | 4 | - | 0 | - |
| 93 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 69 | Fail | 0 | 0 | 69 | 109 | 40 | 0 | 0 | 50 | 90 | - | - | - | - | - | - | - |
| *Outcome R93 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| 93 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 11 | Success | 35 | 35 | 11 | 90 | 79 | 0 | 0 | 50 | 129 | Impose Condition: Wounded (Location Torso Tier-4 Wound -4) | 32 | Torso | 4 | - | 0 | - |
| 93 | Ice Troll->defend | ActiveDefense | Ice Troll | Brawling | 67 | Fail | 0 | 0 | 67 | 220 | 153 | 0 | 0 | 70 | 220 | - | - | - | - | - | - | - |
| *Outcome R93 PC->Troll* | Adventurer-1 wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R93** | PC HP=51 / Troll HP=674 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R94** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 94 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 81 | Fail | 0 | 0 | 81 | 220 | 139 | 0 | 0 | 70 | 209 | - | - | - | - | - | - | - |
| *Outcome R94 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 94 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 65 | Fail | 0 | 0 | 65 | 129 | 64 | 0 | 0 | 50 | 114 | - | - | - | - | - | - | - |
| *Outcome R94 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R94** | PC HP=51 / Troll HP=674 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R95** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 95 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 34 | Success | 33 | 33 | 34 | 209 | 175 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Head Tier-4 Wound -4) | 85 | Head | 4 | - | 2 | - |
| 95 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 41 | Success | 2 | 2 | 41 | 114 | 73 | 0 | 0 | 50 | 123 | - | - | - | - | - | - | - |
| *Outcome R95 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 2 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 95 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 100 | FUMBLE | 0 | 0 | 100 | 123 | 23 | 0 | 0 | 50 | 73 | - | - | - | - | - | - | - |
| *Outcome R95 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R95** | PC HP=51 / Troll HP=674 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R96** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 96 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 97 | Fail | 0 | 0 | 97 | 220 | 123 | 0 | 0 | 70 | 193 | - | - | - | - | - | - | - |
| *Outcome R96 Troll->PC* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| 96 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 94 | Fail | 0 | 0 | 94 | 73 | 0 | 21 | 21 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R96 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R96** | PC HP=30 / Troll HP=674 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R97** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 97 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 33 | Success | 34 | 34 | 33 | 193 | 160 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Legs Tier-4 Wound -4) | 7 | Legs | 4 | - | 21 | - |
| 97 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 22 | Success | 21 | 21 | 22 | 50 | 28 | 0 | 0 | 50 | 78 | - | - | - | - | - | - | - |
| *Outcome R97 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 21 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 97 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 95 | Fail | 0 | 0 | 95 | 78 | 0 | 17 | 17 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R97 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R97** | PC HP=13 / Troll HP=674 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R98** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 98 | Ice Troll->attack | Attack | Ice Troll | SharktoothedMaw | 71 | Success | 4 | 4 | 71 | 220 | 149 | 0 | 0 | 70 | 219 | Inflict Injury (Base) magnitude 2 | - | - | - | - | 2 | -2 |
| 98 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 41 | Success | 2 | 2 | 41 | 50 | 9 | 0 | 0 | 50 | 59 | - | - | - | - | - | - | - |
| *Outcome R98 Troll->PC* | Ice Troll wins on Quality; mitigated by defender's Margin 2 (DEC-097) | | | | | | | | | | | | | | | | | | | | | |
| 98 | Adventurer-1->attack | Attack | Adventurer-1 | Attack2 | 69 | Fail | 0 | 0 | 69 | 59 | 0 | 10 | 10 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R98 PC->Troll* | Attack fails (attacker's own Core Test failed) | | | | | | | | | | | | | | | | | | | | | |
| **End R98** | PC HP=1 / Troll HP=674 | | | | | | | | | | | | | | | | | | | | | |
| **Turn order R99** | Troll Speed 175 (acts first), Adventurer-1 Speed 150 | | | | | | | | | | | | | | | | | | | | | |
| 99 | Ice Troll->attack | Attack | Ice Troll | IcyClaws | 30 | Success | 37 | 37 | 30 | 219 | 189 | 0 | 0 | 70 | 220 | Impose Condition: Wounded (Location Arms Tier-4 Wound -4) | 52 | Arms | 4 | - | 0 | - |
| 99 | Adventurer-1->defend | ActiveDefense | Adventurer-1 | Defence2 | 100 | FUMBLE | 0 | 0 | 100 | 50 | 0 | 50 | 50 | 50 | 50 | - | - | - | - | - | - | - |
| *Outcome R99 Troll->PC* | Ice Troll wins (defense failed); mitigation=0 | | | | | | | | | | | | | | | | | | | | | |
| **End R99** | PC HP=0 / Troll HP=674 | | | | | | | | | | | | | | | | | | | | | |

## Edge cases logged during play
- R4 Adventurer-1: failed Double on roll 55 using Defence2 -> Advanced Skill 'Skill-(3)' created (Tier 3), starting value 1 (DEC-012). Not used further this combat.
- R7 Adventurer-1: failed Double on roll 100 using Attack2 -> Advanced Skill 'Skill-(4)' created (Tier 3), starting value 1 (DEC-012). Not used further this combat.
- R16 Adventurer-1: failed Double on roll 66 using Attack2 -> Advanced Skill 'Skill-(5)' created (Tier 3), starting value 1 (DEC-012). Not used further this combat.
- R31 Ice Troll: failed Double on roll 100 using IcyClaws -> Advanced Skill 'Skill-(4)' created (Tier 3), starting value 1 (DEC-012). Not used further this combat.
- R37 Ice Troll: failed Double on roll 88 using Brawling -> Advanced Skill 'Skill-(5)' created (Tier 3), starting value 1 (DEC-012). Not used further this combat.
- R47 Adventurer-1: failed Double on roll 44 using Attack2 -> Advanced Skill 'Skill-(6)' created (Tier 3), starting value 1 (DEC-012). Not used further this combat.
- R48 Adventurer-1: failed Double on roll 66 using Attack2 -> Advanced Skill 'Skill-(7)' created (Tier 3), starting value 1 (DEC-012). Not used further this combat.
- R57 Ice Troll: failed Double on roll 100 using Brawling -> Advanced Skill 'Skill-(6)' created (Tier 3), starting value 1 (DEC-012). Not used further this combat.
- R61 Adventurer-1: failed Double on roll 66 using Defence2 -> Advanced Skill 'Skill-(8)' created (Tier 3), starting value 1 (DEC-012). Not used further this combat.
- R84 Ice Troll: failed Double on roll 88 using Brawling -> Advanced Skill 'Skill-(7)' created (Tier 3), starting value 1 (DEC-012). Not used further this combat.
- R87 Ice Troll: failed Double on roll 55 using Brawling -> Advanced Skill 'Skill-(8)' created (Tier 3), starting value 1 (DEC-012). Not used further this combat.
- R95 Adventurer-1: failed Double on roll 100 using Attack2 -> Advanced Skill 'Skill-(9)' created (Tier 3), starting value 1 (DEC-012). Not used further this combat.
- R99 Adventurer-1: failed Double on roll 100 using Defence2 -> Advanced Skill 'Skill-(10)' created (Tier 3), starting value 1 (DEC-012). Not used further this combat.

## GM stops
- None. No genuine GM-required stop occurred; combat resolved deterministically under the Ruled mechanics + pre-authorized scaffolds.