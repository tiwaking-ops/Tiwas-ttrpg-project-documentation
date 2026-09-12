---
document:
  title: "Tiwas — Mirror-Match Combat Stress Test: Scaffolding Fix (Offense Selection)"
  version: "0.1 (playtest-only scaffolding amendment — not executed, not ruled)"
  status: "Advisory / Non-canonical. No DEC assigned. Does not amend Canonical Rules, Decision Register, or the 2026-09-10 design brief’s intent. Exists solely so the existing scenario can exercise the mechanics it was built to test."
provenance:
  author_llm: {name: "Grok 4.5", version: "grok-4.5"}
  created_date: "2026-09-12"
  source_brief: "tiwas-playtest-mirror-combat-design-brief-2026-09-10.md"
  prior_execution: "tiwas-mirror-combat-playtest-execution-report-2026-09-11.md"
  ruleset_reference: "Canonical Rules v1.4 + Decision Register through DEC-135.A"
---

# Tiwas — Mirror-Match Combat Stress Test: Scaffolding Fix

**Document role.** Playtest-only amendment to the offense-skill selection rule used by the 2026-09-10 Mirror-Match design brief. This document is scaffolding for a single automated scenario. It does not propose, lock, or amend any Tiwas rule. It does not assign or modify any DEC. It is advisory to OpenCode (script implementation) and Tiwa (designer review).

**Problem statement (from prior execution).**  
The brief’s offense-selection rule (“currently highest numeric value,” ties broken by fixed priority Attack > Grapple > Trip > Disarm > Armor Bypass > Equipment Damage) combined with Failure-XP awarded only to the skill that was rolled produces permanent single-skill lock-in after the first differentiation. Once Attack advances, every subsequent selection is Attack. Grapple, Trip, Disarm, Equipment Damage (and Armor Bypass) receive zero further selections and therefore zero Failure-XP. Objectives that require those Effects never fire after the opening exchanges.

**Constraint set (unchanged).**  
- Combatants remain mechanically identical.  
- No new skill → Effect pairings.  
- No new actions or Effects.  
- Armor Bypass remains out of scope (already decided; Tier-2 path blocked by missing Human Location Template).  
- Same dice methodology (`random.SystemRandom()`).  
- Failure-XP, Advanced Skill creation, and exclusion rules unchanged.  
- All scaffolding is explicitly non-canonical and local to this scenario.

---

## 1. Replacement Offense-Selection Rule (Playtest Scaffold Only)

**Rule (non-canonical, this scenario only).**  
On each of an actor’s turns the acting combatant selects, from the eligible offense-skill pool, the skill that has been **selected the fewest times** so far in the combat (including the current exchange).  

**Eligible pool.**  
{Attack, Grapple, Trip, Disarm, Equipment Damage}  
Armor Bypass is excluded from the pool for the entire run (scope decision carried forward from the original brief and the 2026-09-11 execution).

**Tie-break.**  
When two or more skills share the current minimum selection-count, break ties by the fixed priority order:  
**Attack > Grapple > Trip > Disarm > Equipment Damage**.

**Initial state.**  
All five skills begin with selection-count = 0. First selection is therefore Attack (highest priority among zeros). Subsequent selections cycle through the remaining skills before any skill is selected a second time, then a third time, etc.

**Growth interaction.**  
Failure-XP continues to be awarded only to the skill that was actually rolled (DEC-009 / DEC-010). Because selection is driven by usage count rather than current value, a skill that has fallen behind in value is still selected on its turn in the rotation. Value differentiation therefore cannot produce permanent lock-out of any eligible skill.

**Rationale for this particular scaffold.**  
- Guarantees every eligible Effect is exercised a near-equal number of times.  
- Deterministic and fully auditable (selection-count is an observable state variable).  
- Requires no new mechanical vocabulary, no change to skill→Effect mapping, and no alteration of the Failure-XP or Advanced Skill rules.  
- Directly satisfies the test objectives that depend on non-Attack Effects while remaining local to this playtest.

---

## 2. Unchanged Procedure Elements

Everything in the 2026-09-10 brief §§1–3, 4.1, 4.2 steps 2–9, 4.3, 5–7 remains exactly as written, subject only to the following explicit scope notes:

| Element | Status in this run |
|---|---|
| 1:1 skill → Effect pairing | Retained (playtest convention only; not a Tiwas rule) |
| Defense mandatory | Retained |
| Effect Tier / Magnitude defaults (DEC-107) | Retained |
| Skill-Tier shred + margin de-escalation (DEC-103) | Retained |
| Zero-Step + Tier-1 quartile location (DEC-014 / DEC-100) | Retained |
| Tag + Location gating / fail-and-fall-back (DEC-030 / DEC-114) | Retained |
| Advanced Skill creation + exclusion from selection pool | Retained |
| Termination: first combatant HP ≤ 0 | Retained |
| Armor Bypass | **Out of selection pool; Tier-2 path unreachable by design** |

---

## 3. Objectives Coverage After Scaffold Application

| # | Mechanic under test | DEC(s) | Expected coverage under new selection rule |
|---|---|---|---|
| 1 | S-1 melee-exchange algorithm, mandatory-defense convention | 013, 105 | Fires every exchange |
| 2 | Contest-delta HP resolution | 096, 097, 104 | Fires on every successful Attack (and on any fail-and-fall-back) |
| 3 | Effect Tier/Magnitude = Skill-Tier (no Quality gating) | 107 | Fires on every successful non-HP Effect |
| 4 | Skill-Tier shred + margin de-escalation | 103 | Fires on every successful non-HP Effect |
| 5 | Zero-Step + Tier-1 quartile location | 014, 100 | Fires on every location-referencing Effect |
| 6 | Tag + Location gating / fail-and-fall-back | 028, 030, 114 | Fires on every location-referencing Effect (Tags present → pass path dominant) |
| 7 | Grappled imposition + contested Break-Hold escape | 079, 124, 131 | **Imposition half fires** (Grapple is in the rotation). Contested Break-Hold escape remains **structurally out of scope** for this scenario (no follow-up contested action is defined in the brief or this scaffold). |
| 8 | Wound target selection (automated / creature path) | 102 | Reachable via Inflict Injury and via any fail-and-fall-back; labeled reachable. |
| 9 | Incidental Advanced Skill creation, non-influencing | 012 | Fires on qualifying failed Doubles; exclusion still enforced |
| 10 | Armor Bypass Tier-2 path | 112, 113 | **Unreachable / out-of-scope by design** (excluded from selection pool; Human Location Template still missing). Explicitly not claimed as tested. |

---

## 4. Logging Additions Required by the Scaffold

Extend the per-exchange log schema of the original brief (§7) with two fields:

| Field | Description |
|---|---|
| selection_counts_before | Dict of {skill: count} immediately before the selection decision |
| offense_skill_selection_reason | “min-count” or “min-count + priority-tiebreak” |

All other log fields remain unchanged.

---

## 5. Explicit Non-Canonical Disclaimers

1. The least-selection-count rule is **AI-selection scaffolding for this scenario only**. It is not derived from any DEC, is not a candidate rule, and must not be recorded in the Decision Register without an explicit designer instruction.  
2. The original “highest numeric value” rule remains the brief’s stated intent; this document exists solely because that rule prevents the scenario from exercising the Effects it was written to test.  
3. No change is made to skill→Effect pairings, to the Failure-XP economy, or to Advanced Skill handling.  
4. Armor Bypass continues to be treated as out of scope; its exclusion is a continuation of the prior scope decision, not a new ruling.  
5. Contested Break-Hold (the escape half of Objective 7) is not implemented; any future run that wishes to exercise it must add an explicit post-imposition contested action, which is outside the present scaffold.

---

## 6. Implementation Notes for OpenCode

- Maintain a per-combatant selection-count dictionary initialized to zero for the five eligible skills.  
- On each actor turn:  
  1. Identify the current minimum count.  
  2. Among skills at that minimum, choose the highest-priority skill according to the fixed order above.  
  3. Increment that skill’s count **after** the selection is recorded (before the roll).  
- Armor Bypass is never present in the dictionary.  
- Advanced Skills created mid-combat remain excluded from the selection pool (original brief constraint).  
- RNG continues to be `random.SystemRandom()`.  
- No other procedural changes.

---

## 7. Status / Next Steps

This document is a design-scaffold amendment, not an execution and not a ruling.  

Recommended path:  
1. Tiwa review / approval of the least-selection-count scaffold (or an alternative rotation/least-used rule of equivalent effect).  
2. OpenCode implementation of the amended selection logic inside a new or revised `random.SystemRandom()` script.  
3. Execution and production of a new execution report that records actual objective coverage under the corrected selection rule.  
4. No DEC, no Canonical change, no Decision Register entry unless Tiwa explicitly directs one.

---

**End of scaffolding-fix document.**

**Author:** Grok 4.5 (grok-4.5)  
**Date:** 2026-09-12  
**Classification:** Playtest-only scaffolding amendment / Non-canonical / Advisory to OpenCode and Tiwa
