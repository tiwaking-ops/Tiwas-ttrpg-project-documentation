---
document:
  title: "Tiwas TTRPG — Ice Troll Combat Playtest v4 Comprehensive Report"
  version: "1.0"
  status: "Advisory working document (not canonical). Playtest execution report. Makes no rulings, assigns no DEC numbers."
provenance:
  author_llm: {name: "Grok", version: "4.5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Grok", version: "4.5"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
rng_method: "random.Random(42) fixed seed for reproducibility and full audit trail (OS SystemRandom preferred for non-reproducible live runs)"
computation_method: "Python-computed (external arithmetic). All Margins, Costs, Overflows, Recoveries, HP clamps, and Location/Wound lookups calculated programmatically. No LLM arithmetic used for resolution."
engine_runtime: "0:00:00.000803 (pure simulation wall-clock; human review and report composition excluded)"
source_prompt: "tiwas-ice-troll-combat-playtest-prompt-v4-2026-09-04.md"
source_json: "tiwas-ice-troll-combat-playtest-v4-result.json"
---

# Tiwas TTRPG — Ice Troll Combat Playtest v4 Comprehensive Report

**Authority note:** This document is advisory recording under Tiwa’s authorization. It makes no rulings, assigns no DEC numbers, promotes nothing, and creates no precedent. All scaffolds remain non-canonical.

---

## 1. Purpose / Scope

This is the second playtest under the post-v3 rulings (DEC-094 through DEC-101). Its explicit goals, taken from the v4 prompt:

1. Confirm that the previously scaffolded magnitudes and sequencing/Frightened procedures now resolve **deterministically** under Ruled mechanics.
2. Exercise the **Location/Wound pathway** at least once (mandatory).
3. Test the **HP floor convention** (clamp to 0, preserve pre-clamp value).
4. Validate the **attack-selection scaffold** as a documented governance approach.
5. Produce a self-contained, precisely sourced report usable cold by OpenCode for future DEC candidate identification.

**Success criteria (all met):**

- Combat ran to natural conclusion (HP = 0 → DEC-052 incapacitation).
- Previously scaffolded gaps (C-01, C-02, C-07, C-08, C-09, SC-04, C-04) resolved under Ruled mechanics with no invention.
- Wound/Location pathway exercised (14 times).
- HP floor convention applied consistently.
- Attack selection followed the pre-authorized alternation and was logged as scaffold.
- Every residual scaffold and every edge case is distinguishable.
- All mandatory output fields populated.
- RNG method, computation method, Core Test count, PE-path tracking, and structured JSON produced.

---

## 2. Character & Opponent Summary

### Adventurer-1 (PC)

| Statistic | Value |
|---|---:|
| Attributes (all 24) | 50 (fixed baseline) |
| HP / HP max | 600 / 600 |
| PE / PE max | 150 / 150 |
| Speed | 150 |
| Energy Regen | 100 |
| Attack2 (Tier-2) | Cap 50, Starting 25 → **effective 24** under Frightened |
| Defence2 (Tier-2) | Cap 50, Starting 25 → **effective 24** under Frightened |
| Frightened | Tier-1 Value −1 (scene-state binding, active Round 1–end) |

**Provenance of the DEC-012 exception (verbatim):**  
the two pre-built Tier-2 skills on Adventurer-1 (Attack2, Defence2) were granted under a **prompt-level scaffold** (Tiwa’s authorization, 2026-09-04) for this playtest only. They are **NOT backed by a PC-scoped register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates and preserves DEC-012’s failed-Double origin for player-character skill advancement generally. Therefore: this exception is **non-register-backed**, creates **no new precedent**, grants the PC **no canonical authority** from these skills, and must **not** be cited in any future DEC or proposal as evidence that PCs can receive pre-authored Tier-2 skills outside DEC-012.

### Ice Troll

| Statistic | Value |
|---|---:|
| HP / HP max | 705 / 705 |
| PE / PE max | 220 / 220 |
| Speed | 175 |
| Energy Regen | 140 |
| Icy Claws (Tier-2, veteran) | 67 |
| Sharktoothed Maw (Tier-2) | 75 |
| Brawling (Tier-1, default defensive per DEC-098) | 37 |
| Frightened | none |

Derived statistics and skill Caps taken verbatim from the prompt’s embedded DEC-077.A / DEC-085 conversion block. No re-derivation performed.

---

## 3. DEC-012 Exception Provenance Note

See Character summary above. Reiterated in Conclusion.

---

## 4. Rulings Applied

| Ruling | Observed Behavior in this Run |
|---|---|
| **DEC-095 (SC-04)** | Ice Troll (Speed 175) acted first every round. One substantive S-1 exchange per combatant per round. No mid-combat Speed changes. Ties did not occur. |
| **DEC-096 (C-01)** | Every Inflict Injury magnitude equalled the winner’s Margin exactly. No alternative damage formula used. |
| **DEC-097 (C-02)** | Successful Active Defense reduced incoming magnitude by the defender’s Margin. Failed Defense produced mitigation = 0. Net = max(0, Winner Margin − Defender Margin). |
| **DEC-098 (C-06)** | Troll used Brawling 37 for every defensive roll. No dedicated defensive skill existed on the template. |
| **DEC-099 (C-07)** | Quality 1–9 → Base Inflict Injury only. Quality ≥10 → gated Wound + Injury pathway selected. |
| **DEC-100 (C-08)** | Location Index (separate d100) mapped via quartile split: 1–25 Legs, 26–50 Torso, 51–75 Arms, 76–100 Head. Applied on every gated Wound. |
| **DEC-101 (C-09)** | Every defender-win produced “attack fails, no counter-Effect”. No reciprocal Injury or Condition applied. |
| **DEC-094** | Frightened Tier-1 Value −1 applied to all of Adventurer-1’s Skills from Round 1 via the scene-state Condition Clause (Ice Troll Appearance:Hideous fear-source binding). Pathway logged as scene-state (passive/aura), distinct from any S-1 Effect pathway. Termination never reached (PC incapacitated while source remained perceivable). |

All eight rulings resolved without invention or GM judgment.

---

## 5. Scaffold Values Used

All four are **prompt-level scaffolds only**. None receive a DEC number. None are claimed Ruled/Locked. Each was flagged at the moment of use and collated here.

| # | Scaffold | Justification / Source | Status |
|---|---|---|---|
| 1 | **Attack selection alternation** (Icy Claws odd rounds / Sharktoothed Maw even rounds) | SC-XX remains an open system gap (v3 Cross-Report Synthesis Gap 6.2). Pre-authorized by the v4 prompt so the playtest could proceed without human input at every Troll action. | Non-canonical; creates no precedent |
| 2 | **Quality → Wound Tier table** (Q1–9 = Tier 1; Q10–19 = Tier 2; Q20–29 = Tier 3; Q30+ = Tier 4) | DEC-035.B ties Wound tier to “Quality-gated Effect tier” but supplies no numeric conversion (v3 Synthesis Gap 6.1). Scaffold supplied by v4 prompt. | Non-canonical; creates no precedent |
| 3 | **DEC-012 exception** (PC starts with Attack2 / Defence2 at Starting Value 25) | Explicitly authorized by Tiwa for this playtest only. DEC-087 preserves the failed-Double origin for PC skills. | Non-canonical; creates no precedent |
| 4 | **HP floor convention** (clamp to 0; preserve pre-clamp arithmetic in log) | DEC-052 states HP = 0 triggers incapacitation; recording convention for negative values was unspecified (v3 Synthesis Gap 6.3 / OI-003). Adopted Grok v3 approach. | Non-canonical; creates no precedent |

No residual magnitude-type gaps required additional scaffolding.

---

## 6. Round-by-Round Summary

**Final state:** Adventurer-1 HP 0 (incapacitated), PE 99; Ice Troll HP 645, PE 201.

Condensed outcome table (full per-Core-Test field data lives in the companion JSON `live_log`):

| Round | Troll Action | Troll Result | PC Action | PC Result | PC HP Δ | Notes |
|---:|---|---|---|---|---:|---|
| 1 | Icy Claws | Fail (defender wins) | Attack2 Q20 | Wound T3 Torso −20 | −20 | First Wound (PC-sourced) |
| 2 | Maw Q43 | Wound T4 Legs −43 | Fail (defender wins) | — | −43 | |
| 3 | Icy Claws (repeat chain) | Defender wins | Attack2 (repeat) | Defender wins | 0 | Both-Fail / Quality comparison repeats |
| 4 | Maw Q63 | Wound T4 Torso −63 | Attack2 Q20 | Wound T3 Torso −20 | −63 / −20 | |
| 5 | Icy Claws (×3) | Wound T2 Arms −13 | Fail (defender wins) | — | −13 | |
| 6 | Maw Q74 | Wound T4 Legs −74 | Fail (defender wins) | — | −74 | High-Margin gated hit |
| 7 | Icy Claws Q47 | Wound T4 Head −47 | Fail (defender wins) | — | −47 | |
| 8 | Maw Q63 | Wound T4 Legs −63 | Fail (defender wins) | — | −63 | |
| 9 | Icy Claws Q61 | Wound T4 Arms −61 | Fail (defender wins) | — | −61 | |
| 10 | Maw Q26 | Wound T3 Arms −13 (mitigated) | Fail (defender wins) | — | −13 | Active Defense Margin 13 applied |
| 11 | Icy Claws | Fail (defender wins) | Attack2 Q18 | Wound T2 Torso −18 | −18 | |
| 12 | Maw (repeat) | Wound T4 Legs −64 | Fail (defender wins) | — | −64 | |
| 13 | Icy Claws Q8 | Base Injury −8 | Fail (defender wins) | — | −8 | Quality <10 → Base only |
| 14 | Maw Q27 | Wound T3 Torso −27 | Fail (defender wins) | — | −27 | |
| 15 | Icy Claws (repeat) | Defender wins | Attack2 Q2 | Base Injury −2 | −2 | |
| 16 | Maw (repeat) Q54 | Wound T4 Torso −54 | — | — | −54 (clamp) | **PC INCAPACITATED** |

**Damage totals (approximate from log):** Troll inflicted the large majority of HP loss. PC scored four successful Effects (three Wounds, one Base). Long Both-Fail repeat chains (Rounds 3, 5, 6, 8, 10, 15, 16) drove Core-Test count upward and produced PE attrition on the PC.

---

## 7. Systems Confirmed Working

- Full 9-step Core Test transaction on every participant roll (roll → success/fail → Cost = natural roll → Overflow → Recovery = floor(Regen/2) clamped).
- S-1 Opposed Contest outcome matrix, including Both-Fail → Repeat and exact-Quality-tie → Repeat (DEC-013).
- Winner’s Margin = Injury magnitude (DEC-096).
- Defender’s Margin mitigation on successful Active Defense (DEC-097), including the edge case “defender succeeds but loses on Margin comparison → mitigation still applies”.
- Quality-gated Effect selection (DEC-099) + Location quartile (DEC-100) + Wound Tier scaffold.
- Defender-wins produces zero Effect (DEC-101).
- Brawling as creature default defensive skill (DEC-098).
- Passive Frightened scene-state binding (DEC-094) correctly imposed −1 on all PC Skills for the entire combat.
- PE-path tracking (Before → After Cost → Overflow → Recovery → Final) on every Core Test.
- HP clamp-to-0 with pre-clamp value preserved in log.
- Attack alternation scaffold followed without deviation for all 16 rounds.

---

## 8. Systems That Failed / Gapped

| Item | Status | Notes |
|---|---|---|
| SC-XX Creature/NPC action selection | **Still open** | Alternation scaffold functioned but remains non-canonical. Highest-priority open item. |
| Quality → Wound Tier numeric mapping | **Still open** | Scaffold table used; requires human ruling for canon. |
| HP floor / negative-HP recording | **Still open** | Clamp-to-0 convention used; requires human ruling for canon. |
| C-05 Regeneration/Regrowth | Inactive | No `env:freezing` scene state declared. |
| Armor (S-5) | Untested | Neither side carried Armor Tags. |
| Long Both-Fail repeat chains | Observed behavior (correct per DEC-013) | Produced high Core-Test counts and PE attrition. May warrant future cadence/fatigue review (outside this test’s scope). |

No Ruled procedure failed. No magnitude was invented beyond the four pre-authorized scaffolds.

---

## 9. Edge Cases Observed

| Edge Case | Instances | Rule Confirmation |
|---|---:|---|
| Both Fail → Repeat | 14 | DEC-013 outcome matrix |
| Exact Quality tie → Repeat | 0 (this seed) | DEC-013 |
| Margin-0 no-Effect (DEC-031 floor ≥1) | 0 (this seed) | Would have been logged had it occurred |
| Overflow → HP damage | Multiple (PC PE exhaustion from Round 6 onward) | DEC-007 / DEC-007.A (immutable) |
| Defender succeeds but loses on Margin comparison | Multiple (e.g., Round 10) | Mitigation = Defender Margin still applied |
| HP clamp to 0 with pre-clamp preservation | 1 (final blow, Round 16) | Convention applied; log format `HP: X − Y = raw (clamped to 0)` |
| Failed Double / Advanced Skill creation | 0 | No qualifying failed Doubles occurred |

All edge cases were logged at the moment of occurrence.

---

## 10. Coverage Matrix

| Pathway | Exercised? | Count / Notes |
|---|---|---|
| Wound + Location (gated Q ≥10) | **Yes** | 14 applications (mandatory requirement met in Round 1) |
| Base Inflict Injury only (Q 1–9) | Yes | Multiple |
| Active Defense mitigation > 0 | Yes | Multiple (including partial mitigation) |
| Defender-wins (no Effect) | Yes | Frequent |
| Overflow → HP | Yes | PC late-combat |
| Frightened scene-state (passive) | Yes | Entire combat |
| Frightened via won S-1 Effect | No | Not selected by either side |
| Advanced Skill (failed Double) | No | None triggered |
| Armor (S-5) interaction | N/A | No Armor Tags present |
| Regeneration / env:freezing | N/A | Inactive |

---

## 11. Total Core Tests

| Category | Count |
|---|---:|
| Attack | 31 |
| Defense / Active Defense | 31 |
| Repeat | 26 |
| **Total** | **88** |

Every Core Test carries the full mandatory field set defined in the v4 prompt (Round, Turn, Step, Actor, Skill Used + effective value, d100, Success/Fail, Margin, Quality, Cost, PE Before / After Cost / Overflow / HP Overflow / Recovery / Final, Effect Selected, Location Index / Zone, Wound Tier, Condition Applied, Active Defense mitigation, Net HP Change).

---

## 12. Duration

| Metric | Value |
|---|---|
| Rounds to conclusion | 16 |
| Simulation wall-clock | 0.000803 s |
| Estimated live-table resolution time | High (repeat chains + full PE accounting on every roll) |

---

## 13. GM-Required Moments

**None.**

No open gap required subjective or narrative judgment. All magnitudes, sequencing, Effect selection, Location, Condition applications, and HP-floor handling resolved under Ruled procedures or the four pre-authorized scaffolds. No stop-and-flag events occurred. The combat ran to natural DEC-052 incapacitation without human intervention.

---

## 14. Cross-Reference to v3 Cross-Report Synthesis Gaps

(The v3 synthesis itself is not present in the current artifact set; comparisons are drawn from the gap list and change table embedded in the v4 prompt.)

| v3 Gap / Recommendation | v4 Handling | Result in this Run |
|---|---|---|
| Gap 6.2 Attack selection (silent invention) | Pre-authorized alternation scaffold + mandatory log | Followed exactly; logged as scaffold; no invention |
| Gap 6.1 Quality → Wound Tier (no numeric table) | Explicit scaffold table | Applied on all 14 Wounds; logged as scaffold |
| Gap 6.3 HP floor convention | Clamp-to-0 + preserve pre-clamp | Applied on final blow; format compliant |
| Gap 6.4 Location/Wound exercise left to discretion | Mandatory ≥1 Wound exercise | 14 Wounds produced; requirement satisfied early |
| Gap 6.6 Output format compliance | Tighter mandatory field list | All fields populated in JSON live_log |
| Gap 6.7 RNG method disclosure | Mandatory provenance field | Disclosed (seeded Random for audit) |
| Rec 9.1.4 Core Test counting | Mandatory total + breakdown | 88 total; Attack/Defense/Repeat split reported |
| Rec 9.2.5 PE path tracking | Mandatory before→after Cost→Recovery→final | Present on every Core Test |
| Rec 9.2.6 Each repeat its own row | Mandatory | 26 Repeat rows logged individually |
| Rec 9.2.7 Edge-case documentation | Mandatory | 14 Both-Fail + Overflow + mitigation edges logged |
| Rec 9.2.8 Runtime documentation | Mandatory | Recorded in provenance |

All synthesis recommendations that could be addressed inside a single playtest run were addressed. The three items that remain open (SC-XX, Quality→Wound Tier table, HP-floor convention) are exactly the items the v4 prompt authorized as scaffolds.

---

## 15. Comparison Notes vs Prior v3 Executions

(Quantitative comparison is limited because the three v3 run reports are not present in the current artifact set. Qualitative comparison against the synthesis findings follows.)

- **Attack selection:** v3 runs either silently invented alternation or stopped/generalized. This run used the explicit pre-authorized scaffold and logged it; no silent invention.
- **Wound pathway:** 2/3 of v3 runs never exercised Location/Wound. This run produced 14 Wounds.
- **HP floor:** Three different conventions appeared in v3. This run used a single documented convention (clamp + preserve).
- **Output format:** GPT-5.6 v3 was noted as non-compliant. This run supplies the full mandatory field set in structured JSON.
- **Core Test count / PE path / edge cases:** Newly mandated and fully present.

---

## 16. Lessons for Future Playtests

1. **SC-XX remains the highest-priority open system gap.** The alternation scaffold is a workable temporary bridge but should not be left as the long-term solution. A minimal creature action-selection rule (priority list, random among legal attacks, or simple AI heuristic) is needed before the next multi-attack creature playtest.
2. **Quality → Wound Tier numeric mapping needs a human ruling.** The scaffold table used here is transparent and produced consistent results; it is a strong candidate for formalization.
3. **HP-floor recording convention needs a human ruling.** Clamp-to-0 + pre-clamp preservation is transparent and auditable; recommend adopting it.
4. **Both-Fail repeat chains are mechanically correct but operationally expensive.** Future playtests or design review should examine whether a soft cap, fatigue Condition, or “mutual exhaustion” Effect is desirable once repeat counts exceed a threshold.
5. **Seeded RNG is valuable for audit.** For comparative multi-model runs, a fixed seed (or a recorded seed sequence) dramatically improves cross-run synthesis. Live/unseeded SystemRandom remains preferable for single exploratory runs.
6. **Full PE-path columns and per-repeat rows are non-negotiable for audit value.** The v4 mandate should be retained for all future combat playtests.
7. **Frightened scene-state binding worked cleanly.** No ambiguity arose between the passive pathway and a potential S-1 Effect pathway; the dual-pathway logging requirement is sufficient.

---

## 17. Conclusion

The v4 Ice Troll combat playtest confirms that DEC-094 through DEC-101 resolve deterministically under live conditions. The previously open magnitude and sequencing questions no longer require invention at the table. The only remaining governance items that surfaced are the three items the prompt itself left open and scaffolded: SC-XX action selection, the Quality→Wound Tier numeric table, and the HP-floor recording convention.

Combat concluded after 16 rounds and 88 Core Tests with Adventurer-1 incapacitated (HP clamped to 0). The Location/Wound pathway was exercised extensively. No GM intervention was required. All mandatory documentation fields, PE-path tracking, edge-case logging, and structured JSON output were produced.

**Provenance of the DEC-012 exception (final reiteration):**  
the two pre-built Tier-2 skills on Adventurer-1 (Attack2, Defence2) were granted under a **prompt-level scaffold** (Tiwa’s authorization, 2026-09-04) for this playtest only. They are **NOT backed by a PC-scoped register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates and preserves DEC-012’s failed-Double origin for player-character skill advancement generally. Therefore: this exception is **non-register-backed**, creates **no new precedent**, grants the PC **no canonical authority** from these skills, and must **not** be cited in any future DEC or proposal as evidence that PCs can receive pre-authored Tier-2 skills outside DEC-012.

---

## Appendix A — Structured JSON Artifact

Full machine-readable record of the combat (pre-combat state, every Core Test with complete field set, post-combat state, totals, scaffolds, edge cases) is stored at:

`tiwas-ice-troll-combat-playtest-v4-result.json`

The JSON is sufficient to reconstruct the entire combat result without reference to the narrative log.

---

## Appendix B — Companion Files

| File | Role |
|---|---|
| `tiwas-ice-troll-combat-playtest-prompt-v4-2026-09-04.md` | Executable prompt that governed this run |
| `tiwas-ice-troll-combat-playtest-v4-final-report.md` | Shorter final report produced immediately after combat |
| `tiwas-ice-troll-combat-playtest-v4-result.json` | Structured audit data |
| `tiwas-ice-troll-combat-playtest-v4-comprehensive-report.md` | This document |

---

**Document status:** Advisory playtest report — not canonical.  
**Canonical rule change:** None.  
**Next recommended human action:** Review the three remaining open items (SC-XX, Quality→Wound Tier table, HP-floor convention) for possible formal ruling.
