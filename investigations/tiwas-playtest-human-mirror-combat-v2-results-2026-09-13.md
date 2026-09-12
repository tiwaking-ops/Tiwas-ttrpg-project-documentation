---
document:
  title: "Tiwas — Human-Templated Mirror Combat Stress Test v2: Results"
  version: "1.0"
  status: "Advisory / Non-canonical playtest output. No DEC assigned. Storage and assessment confer no authority."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-13"
  execution: "random.SystemRandom(); single run, no forced seed"
---

# Results — Human-Templated Mirror Combat Stress Test v2

Companion to `tiwas-playtest-human-mirror-combat-v2-design-brief-2026-09-13.md`. Full
per-exchange data in `mirror_combat_v2_log.csv`; full end-state (attributes, skills,
records) in `mirror_combat_v2_summary.json`.

## 1. Run summary

| Metric | Value |
|---|---:|
| Total exchanges | 129 |
| Total rounds | 65 |
| Termination trigger | Beta HP ≤ 0 (forced incapacitation, DEC-052) |
| Final HP — Alpha | 260 / 616 max |
| Final HP — Beta | **−22** / 624 max (uncapped negative, DEC-108) |
| Attacker-wins / Defender-wins | 45 / 84 |
| Max same-exchange repeats (double-fail / exact-tie) | 6 |
| Negative PE observed | None (DEC-007 Overflow correctly zeroes the pool, never goes negative) |

**How the fight actually ended** is itself a finding worth flagging: the terminating blow
was **not** an opponent's attack. Beta's final action was a *failed* Armor Bypass roll
(77 vs. a Skill value of 36); the natural-roll Cost (77) exceeded Beta's remaining
Physical Energy (52), producing 25 Overflow — which, per DEC-007/DEC-007.A, became direct
HP damage. That pushed Beta from 3 HP to −22, triggering DEC-052 forced incapacitation.
**Beta was defeated by its own resource exhaustion, not by Alpha's offense.** This is the
Overflow mechanic working exactly as specified, not a bug — but it's a sharp illustration
of how punishing high-roll-cost tests become once PE runs low relative to Skill.

## 2. Effect / outcome distribution

| Effect declared | Count |
|---|---:|
| EquipmentDamage | 14 |
| Wounded | 8 |
| Disarm | 7 |
| ArmorBypass | 7 |
| Prone (Trip) | 3 |
| Grappled | 3 |
| Inflict Injury (Attack, or fallback) | 3 direct + 5 fallback |

| Tag-check result | Count |
|---|---:|
| Pass — Weapon (Disarm) | 6 |
| Pass — Body armor / Chest (Equipment Damage / Armor Bypass) | 5 |
| Pass — Helmet | 3 |
| Fail-and-fallback — no matching gear (Equipment Damage) | 8 |
| Fail-and-fallback — no armor at struck location (Armor Bypass) | 6 |

Both the **success** and **fail-and-fallback** paths of DEC-030 fired repeatedly for
Disarm, Equipment Damage, and — for the first time in this project's playtesting —
**Armor Bypass**, now that DEC-137 gives it a real target to hit or miss.

## 3. Objective-by-objective reconciliation

| # | Objective | Result |
|---|---|---|
| 1 | S-1 melee-exchange algorithm | **Fired.** All four DEC-013 outcome branches observed (attacker-wins, defender-wins, and both repeat conditions — max 6 repeats in one exchange). |
| 2 | Contest-delta HP resolution | **Fired.** 3 direct Inflict Injury hits + 5 DEC-030 fallback hits, all computed as Attacker Margin − Defender Margin, floored at 0. |
| 3 | Effect Tier/Magnitude = Skill-Tier (DEC-107) | **Fired.** Every non-HP record's initial `Tier` equals the acting skill's Skill-Tier at time of the win (visible directly in the records, e.g. a Tier-5 `EquipmentDamage` record from a Tier-5 Advanced Skill). |
| 4 | Skill-Tier shred + margin de-escalation (DEC-103) | **Fired** on every non-HP win; several resolved to `Tier-0` **negation** (visible in the CSV as empty `record` on some `attacker_wins` rows for non-HP effects — the shred + margin math fully consumed the magnitude). |
| 5 | Zero-Step + Tier-1 quartile resolution | **Fired** for Grapple/Trip/Disarm/Equipment Damage/Wound — all resolved to one of the four DEC-100 quartiles with correct parity. |
| 6 | Tag+Location gating / fail-and-fall-back | **Fired both ways** for Disarm, Equipment Damage, **and Armor Bypass** (see §2). |
| 7 | Grappled imposition | **Fired** (3× on each side); contested Break-Hold escape correctly **not** simulated (out of scope, §9.4 of the brief). |
| 8 | **Wound target selection (DEC-102)** | **Fired — reached for the first time in this project's playtesting.** 9 Wound records total. Alpha's wounds landed on `bps` (5×) vs `bpe` (2×) from the Wound skill's two-attribute candidate pool, consistent with DEC-102(2)'s random tie-break for creature/automated wounders; Beta's single wound landed on `bpe`. |
| 9 | Advanced Skill creation, non-excluded, effect-inheriting | **Fired extensively** — 11 (Alpha) + 13 (Beta) Advanced Skills created, up to **Tier 5** (e.g. `EquipmentDamage+bse+mpp+bss` on Alpha), each retaining its parent's paired Effect and PE resource domain, each correctly re-entering the random-selection pool (visible in later exchanges' `offense_skill` column). |
| 10 | **Full-depth Armor Bypass via DEC-137** | **Fired both ways.** One full-address hit landed on **Heart** (Torso, idx 30) where Body armor's Chest binding matched (§9.3's flagged full-depth reading was exercised, not merely theorized); six others missed armor entirely (Legs/Head-uncovered-face/etc.) and correctly fell back to Base Inflict Injury per DEC-030. |
| 11 | General XP mandatory-lowest-attribute spend | **Fired continuously** — 36 (Alpha) + 39 (Beta) spend events. Both combatants' final attribute spreads are extremely tight (Alpha 51–52, Beta 51–52 across all 24 attributes) despite dozens of Skill Roll Pool cascades feeding General XP from wildly different skills — direct confirmation the "lowest attribute, alphabetical tie-break" convention is self-flattening exactly as written. |
| 12 | Uncapped/negative HP, forced incapacitation | **Fired.** Beta terminated at −22 HP (self-Overflow, §1); HP never clamped to 0 mid-simulation, consistent with DEC-108. |

**All twelve objectives fired**, including both objectives (8 and 10) that were explicitly
unreachable or out-of-scope in the 2026-09-10 playtest.

## 4. Notable emergent behavior (not a rule, an observation)

- **Skill-Tier escalation outpaced by margin de-escalation.** Several high-Tier Advanced
  Skill wins (Tier 4–5) still fully negated after DEC-103's margin subtraction, because
  the defender's Active Defense (also frequently Tier-3 by that point) shredded the
  magnitude before the margin step even applied. This suggests DEC-103's interaction with
  a **mutually escalating** Skill-Tier environment (both sides gaining Advanced Skills at
  a similar rate) trends toward Effects landing at low Tier/Magnitude or full negation
  more often than a single-Tier-2 baseline fight would predict — worth a wider-N
  statistical run if you want to check whether that's a genuine balance signal or this
  run's variance.
- **General XP's flattening effect on attribute spread** may be worth comparing against a
  "no mandatory spend" or "spend on skill's own attributes" alternative convention in a
  future run, since it visibly suppressed any specialization drift this session.

## 5. Flagged assumptions carried from the design brief (not re-litigated here)

See design brief §9 in full. In short: DEC-106 creature multi-attack was deliberately not
used (your stated single-random-skill rule); Armor Bypass resolved at full DEC-137 depth
without applying a Skill-Tier-based truncation (an open corpus tension, not resolved by
this run); Reactions/Fatigue/Movement-zone/Break-Hold-escape mechanics were out of scope.

## 6. Files

- `tiwas-playtest-human-mirror-combat-v2-design-brief-2026-09-13.md` — design brief
- `mirror_combat_v2.py` — simulation source
- `mirror_combat_v2_log.csv` — full 129-exchange log
- `mirror_combat_v2_summary.json` — final attributes/skills/records for both combatants
- This file — results summary and objective reconciliation

**No ruling, no DEC assigned.** This is advisory playtest output pending your review.
