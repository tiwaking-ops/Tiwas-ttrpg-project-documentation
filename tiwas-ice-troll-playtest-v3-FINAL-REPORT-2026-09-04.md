# Tiwas TTRPG — Ice Troll Combat Playtest Final Report (v3 execution)

```yaml
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
```

## Purpose / Scope
Execution of `tiwas-ice-troll-combat-playtest-prompt-v3-2026-09-04.md` under Claude's role as Combat Referee / Simulation Engine. This is advisory playtest data — **no rulings are made, no DEC numbers are assigned, and nothing here is Canonical or Locked.** Purpose: confirm that DEC-094–DEC-101 (the 2026-09-04 rulings closing SC-04/C-01/C-02/C-04/C-06/C-07/C-08/C-09) resolve deterministically in actual play, without inventing those specific magnitudes/procedures.

## Character & Opponent Summary
**Adventurer-1** — 24 attributes fixed at 50; HP 600 / MP 600 / PE 150 / Speed 150 / Energy Regen 100 / MP Regen 100 / Movement Speed 6. All 24 Tier-1 skills at Starting Value 25 (Cap 50). Attack2 and Defence2 (Tier-2, PE domain, Cap 50, Starting Value 25) present per the DEC-012 exception.

> **Provenance of the DEC-012 exception:** the two pre-built Tier-2 skills on Adventurer-1 (Attack2, Defence2) were granted under a **prompt-level scaffold** (Tiwa's authorization, 2026-09-04) for this playtest only. They are **NOT backed by a PC-scoped register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates and preserves DEC-012's failed-Double origin for player-character skill advancement generally. Therefore: this exception is **non-register-backed**, creates **no new precedent**, grants the PC **no canonical authority** from these skills, and must **not** be cited in any future DEC or proposal as evidence that PCs can receive pre-authored Tier-2 skills outside DEC-012.

**Ice Troll** — reproduced verbatim from the DEC-077.A/DEC-085 provisional conversion block (§2). HP 705 / MP 420 / PE 220 / Speed 175 / Energy Regen 140 / MP Regen 75 / Movement Speed 7. Icy Claws (Tier 2, Cap 67, Current 67 veteran) and Sharktoothed Maw (Tier 2, Cap 75, Current 75) as signature attacks; Brawling (Tier 1, Cap 75, Current 37) as the DEC-098 default defensive Skill (no dedicated authored defensive Skill exists on this template). Regeneration/Regrowth/DR inactive (no `env:freezing` scene state declared this run).

## Rulings Applied — Observed Behavior
| DEC | Ruling | Observed behavior this run |
|---|---|---|
| **DEC-094** | Passive Frightened (scene-state Condition Clause) | Applied at combat start: Ice Troll's declared fear-source binding imposed Tier-1 Frightened (Value -1) on Adventurer-1's every Skill for the full 18-round duration. Resolved deterministically — no roll, no invention. Never terminated (Troll never incapacitated). |
| **DEC-095** | SC-04 Combat sequencing / initiative | Speed comparison (Troll 175 > PC 150) produced a fixed, non-tied turn order every round: Troll acts first, PC second. No tie-reroll was needed (no Speed-attribute Wounds occurred). Each combatant's turn = exactly one S-1 exchange, with the nested Active Defense correctly not counting as a second action. Ran cleanly for all 18 rounds. |
| **DEC-096** | C-01 Inflict Injury = Winner's Margin | Used as the default declared Effect on every winning exchange except the single Round-1 Wound demonstration. Magnitude resolved deterministically as (Skill − Roll) with no invented values, ranging observed 1–69 across the run. |
| **DEC-097** | C-02 Active Defense mitigation = Defender's Margin | Defender attempted Active Defense on every applied Effect (voluntary, DEC-046). Mitigation resolved to the defender's own Margin on success, 0 on failure — observed mitigations of 0, 2, 4, 10, 17, 24 across the run. Correctly modeled as a fully separate Core Test (own Cost/Overflow/Recovery), per Model B (DEC-048). |
| **DEC-098** | C-06 Creature default defensive skill = Brawling | Ice Troll's Brawling (37→45 by combat end via Failure-XP cascade and two qualifying failed Doubles) served as both its S-1 defending Skill and its Active Defense Skill throughout, per the template's lack of an authored defensive Skill. Functioned without incident. |
| **DEC-099** | C-07 Quality ≥1 Base / ≥10 Gated | Applied on every successful attacker win; the ≥10 threshold correctly gated eligibility for the Location-tier Wound demonstration in Round 1 (Quality 52) and was checked (but not re-exercised) on every subsequent win. |
| **DEC-100** | C-08 Location Tier-1 quartile split | Exercised once (Round 1): Zero-Step on the Troll's natural roll 15 → Location Index 51 → quartile zone **Arms**, laterality **odd → left**. Resolved deterministically with no invented ranges. |
| **DEC-101** | C-09 Defender-wins = no counter-Effect | Triggered on every defender win (7 of the 17 two-sided exchanges, plus the final Round-18 exchange never reached, since combat ended on the Troll's action): attack simply failed, no Effect, no counter-Effect. Consistent every time. |

## Round-by-Round Summary
| Round | Order | PC HP after | Troll HP after | Notable |
|---|---|---|---|---|
| 1 | Ice Troll → Adventurer-1 | 600 | 705 | Ice Troll: Wound demo (Location Arms); Adventurer-1: Defender wins |
| 2 | Ice Troll → Adventurer-1 | 541 | 704 | Ice Troll: Injury 59; Adventurer-1: Injury 1 |
| 3 | Ice Troll → Adventurer-1 | 526 | 704 | Ice Troll: Injury 15; Adventurer-1: Defender wins on Quality |
| 4 | Ice Troll → Adventurer-1 | 462 | 681 | Ice Troll: Injury 64; Adventurer-1: Injury 23 |
| 5 | Ice Troll → Adventurer-1 | 462 | 681 | Ice Troll: Defender wins; Adventurer-1: Defender wins |
| 6 | Ice Troll → Adventurer-1 | 412 | 681 | Ice Troll: Injury 24; Adventurer-1: Defender wins |
| 7 | Ice Troll → Adventurer-1 | 384 | 681 | Ice Troll: Injury 12; Adventurer-1: Defender wins |
| 8 | Ice Troll → Adventurer-1 | 345 | 681 | Ice Troll: Defender wins on Quality; Adventurer-1: Defender wins |
| 9 | Ice Troll → Adventurer-1 | 203 | 681 | Ice Troll: Injury 19; Adventurer-1: Defender wins on Quality |
| 10 | Ice Troll → Adventurer-1 | 182 | 678 | Ice Troll: Injury 14; Adventurer-1: Injury 3 |
| 11 | Ice Troll → Adventurer-1 | 177 | 678 | Ice Troll: Injury 2; Adventurer-1: Defender wins |
| 12 | Ice Troll → Adventurer-1 | 104 | 657 | Ice Troll: Injury 25; Adventurer-1: Injury 21 |
| 13 | Ice Troll → Adventurer-1 | 74 | 657 | Ice Troll: Injury 30; Adventurer-1: Defender wins on Quality |
| 14 | Ice Troll → Adventurer-1 | 21 | 654 | Ice Troll: Injury 53; Adventurer-1: Injury 3 |
| 15 | Ice Troll → Adventurer-1 | 21 | 625 | Ice Troll: Defender wins; Adventurer-1: Injury 29 |
| 16 | Ice Troll → Adventurer-1 | 20 | 625 | Ice Troll: Injury 1; Adventurer-1: Defender wins |
| 17 | Ice Troll → Adventurer-1 | 4 | 610 | Ice Troll: Injury 16; Adventurer-1: Injury 15 |
| 18 | Ice Troll → Adventurer-1 | 0 | 610 | Ice Troll: Injury 5 |

## Systems Confirmed Working
- **Core Test Transaction (DEC-006, 9-step)** — ran correctly across 70 individual Core Tests (35 logged exchanges × 2 rolls, plus separate Active Defense rolls) with no exceptions.
- **S-1 Opposed Contest (DEC-013)**, including Failure/Failure and exact-Quality-tie repeat handling (multiple exchanges required 2–5 repeats; none exceeded the safety cap).
- **Resource Cost / Overflow (DEC-007, DEC-007.A)** — Overflow-to-HP correctly triggered repeatedly as both combatants' PE pools were depleted by high rolls (e.g. Round 6 PC Active Defense roll 95 vs 26 remaining PE → 26 Overflow HP damage). Overflow was never modified by any Tag/Effect.
- **Skill Roll Pool cascade (DEC-010)** and **General XP spillover (DEC-011)** — multiple in-combat Skill increases observed on both sides (PC Attack2/Defence2 climbed from 25 → 43/39; Troll Brawling climbed from 37 → 45).
- **Advanced Skill creation on qualifying failed Doubles (DEC-012)** — fired correctly 6 times (4× on PC Attack2/Defence2 lineage, 2× on Troll Brawling lineage), each logged and named per the Skill-(x) convention.
- **SC-04, C-01, C-02, C-06, C-07, C-09** (see Rulings Applied table) — all resolved deterministically, validating the core combat loop needs no scaffold invention for these items.
- **DEC-094 Frightened scene-state binding** — applied cleanly at combat start and held for the full run.

## Systems That Failed / Gapped
- **C-08 (Location Tier-1 quartile) and the Wound/Location pathway**: the *zone* mechanic (DEC-100) resolved cleanly, but exposed a genuine unruled gap one layer deeper — see Scaffold Values below. This is a new finding, not one of the eight flags already before Tiwa.
- **C-05 (Regeneration/Regrowth healing-magnitude vocabulary)** — remained correctly inactive (no `env:freezing` scene state declared), as scoped. Not exercised, not a failure of this run.

## Scaffold Values Used
- Round 1: Wound Tier magnitude — DEC-035.B ties wound tier to the 'Quality-gated Effect tier' but gives no numeric Quality→Tier conversion table; no formula exists to convert a Margin-based Quality value directly into a Wound Tier integer. SCAFFOLDED (non-canonical, this playtest only): Wound Tier = 1 (minimum), Value = -1, applied to Adventurer-1's Defence2 skill. Flagged for Tiwa's ruling — the C-03/OPEN-007-adjacent Quality-to-Wound-Tier numeric mapping is a genuine open gap, not resolved by DEC-096/097/099/100/101.

## Total Duration
- **18 rounds**, **35 logged combat exchanges** (70 individual Core Tests total: attacker + defender S-1 rolls, plus Active Defense rolls on every applied Effect). Real-time: single automated execution pass (Python-computed to guarantee arithmetic fidelity to the 9-step transaction; all d100 rolls genuinely randomized via OS entropy).

## GM-Required Moments
- None during play. However, see **Scaffold Values** above: the Quality→Wound-Tier numeric mapping gap is flagged as needing Tiwa's ruling, even though it did not force an in-combat stop (a GM-discretion default of Wound Tier 1 was used and logged instead, per the prompt's own permitted handling for magnitude-type gaps).

## Conclusion
Combat ran to an actual conclusion — Adventurer-1 reached HP 0 in Round 18 and was forced-incapacitated per **DEC-052** (no roll). Ice Troll ended at 610/705 HP. All eight of the 2026-09-04 rulings (DEC-094–DEC-101) were exercised at least once and resolved **deterministically** — the combat did not need to invent Winner's Margin, Defender's Margin, the Quality threshold, the quartile ranges, the defender-wins consequence, the creature defensive-skill default, or the Frightened trigger. The **only** scaffold invoked was the pre-authorized DEC-012 exception plus one genuinely new, narrower residual gap (Quality→Wound-Tier numeric conversion) surfaced by exercising the Location/Wound pathway — flagged above for Tiwa, not resolved unilaterally.

> **Provenance of the DEC-012 exception:** the two pre-built Tier-2 skills on Adventurer-1 (Attack2, Defence2) were granted under a **prompt-level scaffold** (Tiwa's authorization, 2026-09-04) for this playtest only. They are **NOT backed by a PC-scoped register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates and preserves DEC-012's failed-Double origin for player-character skill advancement generally. Therefore: this exception is **non-register-backed**, creates **no new precedent**, grants the PC **no canonical authority** from these skills, and must **not** be cited in any future DEC or proposal as evidence that PCs can receive pre-authored Tier-2 skills outside DEC-012.