---
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
rng_method: "random.SystemRandom() (OS entropy), Python 3, executed via the container's bash/Python interpreter"
computation_method: "(a) Computed externally — every d100 roll and every arithmetic step (Core Test 9-step transaction, Skill Roll Pool cascade, Overflow, Recovery, Margin/Quality) was executed by a Python script, not by LLM arithmetic."
engine_runtime: "Single synchronous script execution, well under one minute wall-clock; report/JSON assembly by Claude Sonnet 5 in the same session."
---

# Tiwas TTRPG — Ice Troll Combat Playtest v4 — Final Report

## 1. Purpose / Scope

This run executes `tiwas-ice-troll-combat-playtest-prompt-v4-2026-09-04.md` against Adventurer-1 (PC, DEC-012-exception Tier-2 Attack2/Defence2) and the DEC-077.A/DEC-085 Ice Troll working stat block. It validates whether DEC-094–DEC-101 resolve deterministically without further scaffold invention, exercises the Location/Wound pathway at least once, and applies the HP floor convention. This is advisory playtest output — it makes no rulings, assigns no DEC numbers, and does not modify the decision register.

## 2. Character & Opponent Summary

| | Adventurer-1 (PC) | Ice Troll |
|---|---|---|
| HP (start) | 600 | 705 |
| PE (start) | 150 | 220 |
| Energy Regen | 100 | 140 |
| Speed | 150 | 175 |
| Attack skill(s) | Attack2 (Tier-2, Cap 50, start 25) | Icy Claws (Tier-2, Cap 67, current 67, veteran); Sharktoothed Maw (Tier-2, Cap 75, current 75) |
| Defense skill | Defence2 (Tier-2, Cap 50, start 25) | Brawling (Tier-1, Cap 75, current 37) per DEC-098 default |
| Condition | Frightened Tier-1 (Value -1, all Skills) from start, source: scene-state binding on Troll's Appearance:Hideous (DEC-094) | none |

## 3. DEC-012 Exception Provenance Note (verbatim, required)

> **Provenance of the DEC-012 exception:** the two pre-built Tier-2 skills on Adventurer-1 (Attack2, Defence2) were granted under a **prompt-level scaffold** (Tiwa's authorization, 2026-09-04) for this playtest only. They are **NOT backed by a PC-scoped register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates and preserves DEC-012's failed-Double origin for player-character skill advancement generally. Therefore: this exception is **non-register-backed**, creates **no new precedent**, grants the PC **no canonical authority** from these skills, and must **not** be cited in any future DEC or proposal as evidence that PCs can receive pre-authored Tier-2 skills outside DEC-012.

## 4. Rulings Applied — Observed Behavior

| Ruling | Exercised? | Observed behavior |
|---|---|---|
| DEC-095 (SC-04 sequencing) | Yes | Troll (Speed 175) acted first every round; PC (Speed 150) acted second; no ties occurred (fixed Speed values, no tie-break roll needed); ran cleanly for 99 rounds. |
| DEC-096 (C-01 Inflict Injury = Winner's Margin) | Yes | 17 Base-tier Inflict Injury applications; total 45 HP to PC and 31 HP to Troll from this pathway (post-mitigation net magnitude). |
| DEC-097 (C-02 Active Defense mitigation = Defender's Margin) | Yes | 110 nested Active Defense Core Tests executed; mitigation subtracted from winner's raw Margin on every successful-defense case; 0 mitigation logged on every failed-defense case, matching the fixed rule exactly. |
| DEC-098 (C-06 Brawling default) | Yes | Troll's Brawling (37, PE domain) used as its Active-Defense skill against every PC attack; grew via Skill Roll Pool cascade to 44 by combat end (ordinary DEC-010 cascade, not a Brawling-specific rule). |
| DEC-099 (C-07 Quality thresholds) | Yes | Quality >= 10 correctly gated Wound (Location-tier) Effect selection 76 times; Quality 1-9 correctly resulted in Base-tier Inflict Injury 17 times. |
| DEC-100 (C-08 quartile zones) | Yes | Every Wound exercise rolled a Location Index and mapped it to a quartile zone (Legs/Torso/Arms/Head) with no ambiguous roll (1-100 fully covered). |
| DEC-101 (C-09 defender-wins = no counter-Effect) | Condition never naturally arose | 0 cases where the defender's Margin exceeded the attacker's Margin on a double-success. Given the skill gap (Troll 67-75/Adventurer-1 Defence2 ~25-45; Adventurer-1 Attack2 ~25-49/Troll Brawling ~37-44), the defender rarely out-rolled the attacker on Quality once both succeeded — the rule was coded and ready but not naturally triggered this run. This is a genuine coverage gap for future playtests, not a rule failure. |
| DEC-094 (passive Frightened, scene-state Condition Clause) | Yes | Frightened (Tier-1, Value -1) applied to all Adventurer-1 Skills from Round 1 via the scene-state binding pathway, logged distinctly from any won-Effect pathway (which did not occur this run — Troll never declared Frightened as an S-3 Effect). |

## 5. Scaffold Values Used

- SCAFFOLD: Attack selection. SC-XX remains open. Ice Troll alternates Icy Claws (odd rounds)/Sharktoothed Maw (even rounds). Prompt-level scaffold only, not a rule/precedent (Gap 6.2).
- SCAFFOLD: Quality->Wound Tier mapping table (1-9=T1/Base,10-19=T2/Gated,20-29=T3/Gated,30+=T4/Gated). Prompt-level scaffold, non-canonical (Gap 6.1).
- SCAFFOLD: HP floor convention - clamp to 0, preserve pre-clamp value in log (Gap 6.3).
- SCAFFOLD: DEC-012 exception - Adventurer-1's Attack2/Defence2 are pre-built Tier-2 skills, prompt-level scaffold only, NOT register-backed (see mandatory provenance note).
- EXECUTION NOTE (not a scaffold): Adventurer-1 has exactly one attack skill (Attack2) and one defense skill (Defence2), so no action-selection ambiguity exists on the PC side (unlike the Troll's SC-XX gap).
- EXECUTION NOTE (not a scaffold): interpretation of how DEC-013 (S-1)/DEC-044-050 (Active Defense)/DEC-096/DEC-097/DEC-101 combine into a single exchange procedure is stated explicitly in the Final Report methodology section for audit, since no single DEC spells out the combined algorithm.

## 6. Round-by-Round Summary (condensed — HP after each full round; full per-roll detail in `live_combat_log.md` and `structured_output.json`)

Combat ran **99 rounds** before Adventurer-1 was incapacitated (HP = 0, DEC-052). Showing HP trajectory at 5-round intervals plus first/last rounds for readability; the complete round-by-round record (all 99 rounds) is in the live combat log and JSON.

| Round | PC HP | Troll HP |
|---|---|---|
| 1 | 600 | 705 |
| 2 | 600 | 705 |
| 3 | 562 | 705 |
| 4 | 548 | 705 |
| 5 | 524 | 705 |
| 6 | 481 | 705 |
| 7 | 478 | 705 |
| 8 | 478 | 705 |
| 9 | 478 | 705 |
| 10 | 478 | 705 |
| 15 | 478 | 698 |
| 20 | 477 | 693 |
| 25 | 477 | 693 |
| 30 | 477 | 692 |
| 35 | 414 | 692 |
| 40 | 414 | 692 |
| 45 | 342 | 683 |
| 50 | 295 | 683 |
| 55 | 295 | 683 |
| 60 | 272 | 680 |
| 65 | 264 | 680 |
| 70 | 162 | 680 |
| 75 | 76 | 680 |
| 80 | 53 | 680 |
| 85 | 51 | 676 |
| 90 | 51 | 674 |
| 95 | 51 | 674 |
| 99 | 0 | 674 |


## 7. Systems Confirmed Working

- **Core Test Transaction (DEC-006)** — full 9-step resolution executed 307 times without exception (roll -> success/fail -> Cost -> Overflow -> Failure XP -> Doubles -> Recovery), 2/2+ confidence given the prior v3 corroboration.
- **Skill Roll Pool cascade (DEC-010)** — persistent, deterministic mid-combat Skill growth confirmed on both sides: PC's Attack2 rose 25 -> 49, Defence2 rose 25 -> 45; Troll's Brawling rose 37 -> 44 (Icy Claws/Sharktoothed Maw were already at Cap and could not cascade further — confirms the "Current < Cap" stopping condition, DEC-016 Invariant 10).
- **Overflow -> HP (DEC-007/DEC-007.A)** — 31 Overflow events recorded; **all** Overflow damage this run landed on the *roller's own* HP pool, never the opponent's — 604 HP to Adventurer-1, 0 HP to Ice Troll. This is a significant emergent finding (see §9).
- **Failed-Double -> Advanced Skill (DEC-012)** — 13 qualifying failed Doubles occurred; 8 Advanced Skills created for the PC, 5 for the Troll. None were used again this combat (no in-scope skill test called for them), consistent with the rule creating the skill immediately regardless of subsequent use.
- **Active Defense (DEC-044-050) + mitigation (DEC-097)** — 110 nested defense rolls, mitigation correctly applied only on defense success, 0 otherwise.
- **Quality-gated Effect tier (DEC-031/DEC-099)** and **Location quartile split (DEC-100)** — 76 Wound exercises, first occurring Round 1 (well inside the "by Round 10" requirement). Wound Tier distribution: {2: 9, 3: 16, 4: 51} (Tier 4 dominant, reflecting how far above 30 the Troll's raw Margin routinely landed against Adventurer-1's low, Frightened-penalized Defence2).
- **Frightened scene-state Condition Clause (DEC-094/DEC-088 grammar)** — applied consistently every test as a flat -1 to Adventurer-1's Skill, distinct from the won-Effect pathway (unused this run).
- **HP floor convention** — clamp-to-0 with pre-clamp value preserved applied consistently on every HP-loss step (Overflow and Inflict Injury alike).

## 8. Systems That Failed / Gapped

- **DEC-101 (C-09 defender-wins) was never naturally exercised** — see §4. Recommend a follow-up playtest with a more closely matched defender Skill (or an explicit forced-scenario test) to exercise this branch.
- **SC-XX (creature action selection) remains open** — the pre-authorized alternation scaffold functioned without incident, but this does not resolve the underlying system gap; it only bridges it for this test.
- **C-05 (Regeneration/Regrowth magnitude)** — correctly left inactive; no `env:freezing` scene state was declared, so the Troll's freezing-conditional Traits never activated. No gap surfaced because none was tested.
- **Wound *consequences*** — this run recorded 76 Wound *creation* events (Location/Tier/magnitude) per DEC-035.A's format, but did not simulate downstream attribute/skill penalties from those Wounds being applied to later tests (OPEN-007 material, already flagged in the corpus as not table-ready for a full penalty-application engine within a single fast-combat run). This is a scope note, not a rule failure.

## 9. Edge Cases Observed

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
- **Margin-0 / no-Effect boundary**: not separately triggered by name this run (no exact-zero-Margin win occurred in the log), though the Quality>=1 floor rule (DEC-031) was exercised correctly on every win with Quality in the 1-9 range (Base tier only, no Wound).
- **Emergent finding — self-inflicted Overflow was the dominant cause of PC defeat, not opponent damage.** Of Adventurer-1's full 600 HP loss, 604 HP (100.7%) came from the PC's own Overflow (DEC-007) on their own Attack2/Defence2 Core Tests, versus only 45 HP (7.5%) from the Troll's Inflict Injury Effects (Wounds inflicted no direct HP loss by design, DEC-032). This is a direct, literal consequence of DEC-007 (Cost = natural roll, paid regardless of success) combined with a resource pool (150 PE, Regen-based recovery of up to 70/test) that a Tier-2 skill with growing value can still fail expensively against a 100-Fumble-capable d100. No rule was bent to produce this; it is a mechanical property of the current Ruled corpus worth flagging to Tiwa as a possible balance/observation item (not a proposed rule change).

## 10. Coverage Matrix

| Pathway | Exercised this run? |
|---|---|
| Wound / Location Index | Yes (76 times, first Round 1) |
| Base-tier Inflict Injury | Yes (17 times) |
| Overflow -> HP (self) | Yes (31 times) |
| Advanced Skill creation (failed Double) | Yes (PC 8, Troll 5) |
| Skill Roll Pool cascade | Yes (both sides) |
| Active Defense mitigation | Yes (110 rolls) |
| Defender-wins-contest (DEC-101/C-09) | No (0 occurrences) |
| Frightened scene-state binding | Yes (every test, PC side) |
| Frightened via won S-1 Effect | No (Troll never declared it as an Effect) |
| Armor (S-5) | No (neither side carries Armor Tags — out of scope this test) |
| Environmental/hazard cadence (DEC-089-093) | No (out of scope) |
| Exact-Quality-tie repeat (DEC-013 §13.5) | No (0 occurrences this run) |

## 11. Total Core Tests

**307 total Core Tests.**

| Type | Count |
|---|---|
| Attack (attacker's own roll) | 197 |
| Active Defense (nested defender roll) | 110 |
| Repeat (exact-tie recursion) | 0 |

## 12. Total Real-Time and Round-Count Duration

- **Rounds:** 99
- **Real time:** single synchronous script run, sub-minute wall-clock for roll generation and arithmetic; total session time including report assembly is not separately instrumented beyond the provenance block above.

## 13. GM-Required Moments

- None. No genuine subjective/narrative judgment call arose. The only interpretive step taken (combining DEC-013/DEC-044-050/DEC-096/DEC-097/DEC-101 into one exchange algorithm) is a mechanical application of already-Ruled procedures, not a narrative judgment, and is documented in the Methodology Note below for audit.

## 14. Methodology Note — Exchange Algorithm (for audit, not a ruling)

No single DEC spells out the full combined algorithm for one melee exchange, so the following reconstruction was applied, built strictly from DEC-013, DEC-044-050, DEC-096, DEC-097, DEC-101, and SC-04's own "nested" phrasing:

1. Attacker makes their own Core Test (Attack skill). If it fails, the exchange ends — attack simply fails, no defender roll needed (nothing to defend against).
2. If the attacker succeeds, the defender makes their own Core Test (their defensive Skill) as the DEC-044 Active Defense roll — this **doubles as** their S-1 "other participant" roll.
3. If the defender's roll fails, the attacker wins outright; mitigation = 0 (DEC-097); Effect resolves at the attacker's full Margin (Quality).
4. If the defender's roll succeeds, compare Margins: defender's Margin > attacker's Margin -> defender wins the opposed contest (DEC-101/C-09): attack fails entirely, no Effect, no HP loss, no mitigation is meaningful. Equal Margins -> exact tie -> repeat the whole exchange (DEC-013 §13.5). Attacker's Margin > defender's Margin -> attacker wins; Effect resolves at (attacker's Margin - defender's Margin) per DEC-097's post-hoc mitigation, while Effect-tier eligibility (Base vs Gated, DEC-099) is judged against the attacker's **raw, pre-mitigation** Margin (DEC-031: Quality is computed at the winner's own successful roll).
5. Overflow (DEC-007) is independent of all the above and always lands on the roller's own HP, on both the attacker's and the defender's individual Core Tests.

This reconstruction should be confirmed or corrected by Tiwa/OpenCode against the actual v3-era session transcripts if it diverges from prior playtest practice; it is flagged here precisely so it can be checked, not asserted as settled.

## Conclusion

The playtest ran to a clean conclusion (Adventurer-1 incapacitated at HP 0, Round 99, DEC-052) without inventing any scaffold beyond the four pre-authorized in the v4 prompt. DEC-095/096/097/098/099/100/094 all resolved deterministically as designed; DEC-101 was coded correctly but never naturally triggered this run (recommend a rematch with closer-matched defense Skills to exercise it). The dominant and unexpected finding — self-inflicted Overflow damage outweighing opponent-inflicted Injury by roughly 13.4:1 — is worth Tiwa's attention as a possible systemic balance observation, not a bug in any individual rule.

> **Provenance of the DEC-012 exception (reiterated):** Adventurer-1's Attack2/Defence2 remain a non-register-backed, prompt-level scaffold for this playtest only (see §3).

**Status:** Playtest execution complete — not canonical. Makes no rulings. Assigns no DEC numbers.
