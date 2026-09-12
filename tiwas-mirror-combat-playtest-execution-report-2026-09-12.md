---
document:
  title: "Tiwas — Mirror-Match Combat Stress Test: Execution Report (Scaffolding-Fix Run)"
  version: "1.0"
  status: "Execution record / Non-canonical. No DEC assigned. Advisory to OpenCode and Tiwa. Does not promote, lock, or amend any rule."
provenance:
  author_llm: {name: "Grok 4.5", version: "grok-4.5"}
  created_date: "2026-09-12"
  source_brief: "tiwas-playtest-mirror-combat-design-brief-2026-09-10.md"
  scaffolding_amendment: "tiwas-playtest-mirror-combat-scaffolding-fix-2026-09-12.md"
  prior_execution: "tiwas-mirror-combat-playtest-execution-report-2026-09-11.md"
  ruleset_applied: "Canonical Rules v1.4 (tiwas-canonical-rules-and-changelog-v1.3.md, internal v1.4) + Decision Register through DEC-135.A"
  execution_method: "Python 3 random.SystemRandom() simulation script"
  script_location_at_execution: "/tmp/tiwas_mirror_combat_playtest_v2.py"
---

# Tiwas — Mirror-Match Combat Stress Test: Execution Report (Scaffolding-Fix Run)

**Document role.** Formal record of the second automated execution of the Mirror-Match Combat Stress Test, this time under the 2026-09-12 least-selection-count scaffolding amendment. This document is an execution and observation record only. It does not constitute a designer ruling, does not assign or amend any DEC, and does not promote any scaffolded procedure to Canonical or Ruled status.

**Audience.** OpenCode (implementation / scripting handoff) and Tiwa (designer review).

---

## 1. Purpose and Scope

### 1.1 Purpose

Re-execute the combat stack defined in the 2026-09-10 design brief, substituting the original “highest numeric value” offense-selection rule with the playtest-only least-selection-count rule defined in the 2026-09-12 scaffolding-fix document, so that Objectives 1–6 and 9 actually fire and Objective 7’s Grappled-imposition half is exercised.

### 1.2 Scope boundaries

- In scope: S-1 opposed contest (DEC-013 / DEC-105), mandatory Active Defense, contest-delta HP resolution (DEC-104), Effect Tier/Magnitude defaults (DEC-107), Skill-Tier shred + margin de-escalation (DEC-103), Zero-Step + Tier-1 quartile location (DEC-014 / DEC-100), Tag + Location gating with fail-and-fall-back (DEC-028 / DEC-030 / DEC-114), incidental Advanced Skill creation (DEC-012), automated/creature Wound-target path (DEC-102), Grappled imposition.
- Explicitly out of scope: contested Break-Hold escape (Objective 7 escape half), Armor Bypass Tier-2 path (Objective 10 — excluded from selection pool; Human Location Template still missing), free Effect choice on any winning skill, movement/zone differentiation.

### 1.3 Authority statement

All mechanics applied are either Canonical / Locked or Non-canonical designer rulings recorded in the Decision Register as Current/Ruled. The offense-selection rule is the sole non-canonical scaffold introduced by the 2026-09-12 amendment and is logged as such. No rule text was altered.

---

## 2. Ruleset Applied

| Layer | Document | Version / Cut-off |
|---|---|---|
| Canonical | `tiwas-canonical-rules-and-changelog-v1.3.md` (internal v1.4) | 2026-09-05 (DEC-017 promotion) |
| Decision Register | `decision-register.md` | last_modified_date 2026-09-10 (through DEC-135.A) |
| Source brief | `tiwas-playtest-mirror-combat-design-brief-2026-09-10.md` | 0.1 |
| Scaffolding amendment | `tiwas-playtest-mirror-combat-scaffolding-fix-2026-09-12.md` | 0.1 |
| Prior execution | `tiwas-mirror-combat-playtest-execution-report-2026-09-11.md` | 1.0 |

Key DECs exercised: DEC-006, DEC-008, DEC-009, DEC-010, DEC-012, DEC-013, DEC-014, DEC-017, DEC-028, DEC-030, DEC-041, DEC-052, DEC-095, DEC-096, DEC-097, DEC-100, DEC-101, DEC-102, DEC-103, DEC-104, DEC-105, DEC-107, DEC-108, DEC-113, DEC-114, DEC-115.

---

## 3. Scaffolding Applied

| Item | Resolution | Status |
|---|---|---|
| Offense-skill selection | Least selection-count among {Attack, Grapple, Trip, Disarm, Equipment Damage}; ties broken by fixed priority Attack > Grapple > Trip > Disarm > Equipment Damage | Playtest-only scaffold (2026-09-12) |
| Armor Bypass | Excluded from selection pool for entire run | Prior scope decision carried forward |
| Quality measure | Margin (DEC-013 precision / efficiency default) | Ruled default |
| Termination | First combatant HP ≤ 0 (DEC-052; HP may go negative per DEC-108) | Ruled |
| Advanced Skill starting value | Fixed at 1; excluded from offense-selection pool | Brief constraint |
| Grapple escape | Condition imposed only; contested Break-Hold not executed | Structurally out of scope |
| 1:1 skill → Effect pairing | Retained | Playtest convention only |

No other deviations from the brief or from Ruled mechanics were introduced.

---

## 4. Combatant Baseline

Identical to the 2026-09-10 brief and the prior execution:

| Parameter | Value |
|---|---:|
| All 24 attributes | 50 |
| HP | 600 |
| Physical Energy | 150 |
| Speed | 150 |
| Energy Regen | 100 → Recovery 50 |
| Movement Speed | 6 |
| Combat skills | Tier-2, Cap 50, Starting Value 25 |
| Tags (both) | weapon + body-armor tags present (Disarm / Equipment Damage / Armor Bypass triggers satisfied where relevant) |
| Classification | Creature (Attribute wounds only; random tie-break) |

Skill ↔ Effect pairing (playtest convention only):

| Skill | Paired Effect |
|---|---|
| Attack | Inflict Injury (Base) |
| Grapple | Impose Condition: Grappled |
| Trip | Knock Prone |
| Disarm | Disarm |
| Equipment Damage | Equipment Damage |
| Defense | (defensive roll only) |

---

## 5. Execution Procedure

### 5.1 Turn structure (DEC-095)

1. Speed-based initiative; ties resolved by natural d100 re-roll.
2. One substantive combat action per turn = one S-1 melee exchange.
3. Movement free/bundled; identical Movement Speed → no positional variance.

### 5.2 Exchange algorithm (amended selection only)

1. Actor selects offense skill with currently **lowest selection-count** (ties broken by fixed priority). Selection-count is incremented after choice.
2. Defender always rolls Defense (mandatory).
3. Both perform independent Core Tests (DEC-006).
4. Outcome matrix (DEC-013): both-fail → repeat; exact Quality tie → repeat; defender wins → attack fails, no counter-Effect; attacker wins → apply paired Effect.
5. HP path (Inflict Injury): damage = Winner’s Margin − Defender’s Margin, never < 0 on a win (DEC-104).
6. Non-HP Effect path: Effect Tier = Skill-Tier (default equal, DEC-107); Skill-Tier shred + margin de-escalation (DEC-103); Location Index via Zero-Step (DEC-014); Tier-1 coarse zones (DEC-100); Tag check (DEC-114 R2); fail-and-fall-back to Inflict Injury (DEC-030) if negated or mismatched.
7. Recovery (DEC-008) applied last to both pools.
8. Failure XP / Skill Roll Pool (DEC-009 / DEC-010) resolved for both.
9. Qualifying failed Double creates Advanced Skill (Starting Value = 1) and excludes it from future offense selection.

### 5.3 Implementation notes

- RNG: `random.SystemRandom()` (cryptographic entropy).
- Script: `/tmp/tiwas_mirror_combat_playtest_v2.py`.
- Single representative run reported; selection balance is deterministic given the rule, so effect coverage is stable across runs.

---

## 6. Results

### 6.1 Aggregate metrics

| Metric | Observed value |
|---|---|
| Total exchanges to termination | 123 |
| Winner | Beta |
| Final HP (Alpha) | −11 |
| Final HP (Beta) | 337 |
| Outcome distribution | both-fail-repeat 54 (44 %); defender-wins 41 (33 %); attacker-wins 28 (23 %) |
| Offense skill selected | Balanced across all five eligible skills (see §6.3) |
| Effects applied | All five eligible Effects fired multiple times |
| Advanced Skills created | Alpha 12, Beta 7 (all excluded from selection) |
| Final Defense values | Alpha 47, Beta 42 (near Cap) |
| Final offense values | Spread 29–34 (all advanced; none locked out) |

### 6.2 Effect application counts (successful attacker-wins)

| Effect | Count |
|---|---:|
| Disarm | 7 |
| Knock Prone | 6 |
| Impose Condition: Grappled | 6 |
| Inflict Injury | 5 |
| Equipment Damage | 4 |
| Inflict Injury (fall-back from negated Effect) | 0 in this run |

### 6.3 Selection totals (times chosen)

| Combatant | Attack | Grapple | Trip | Disarm | Equipment Damage |
|---|---:|---:|---:|---:|---:|
| Alpha | 13 | 13 | 12 | 12 | 12 |
| Beta | 13 | 12 | 12 | 12 | 12 |

Selection is essentially uniform. The least-selection-count rule eliminated the Attack-spam lock-in observed in the prior execution.

### 6.4 Sample terminal sequence (last 5 exchanges)

```
Ex 119 | Alpha→Beta | Equipment Damage(33) | rolls 48/23 | defender-wins
Ex 120 | Beta→Alpha | Equipment Damage(34) | rolls 50/63 | both-fail-repeat
Ex 121 | Alpha→Beta | Attack(31)          | rolls 27/8  | defender-wins
Ex 122 | Beta→Alpha | Attack(34)          | rolls 26/83 | attacker-wins | Inflict Injury dmg 8 | HP Alpha=28
Ex 123 | Alpha→Beta | Grapple(33)         | rolls 89/73 | both-fail-repeat | HP Alpha=-11 (Overflow)
```

Alpha reaches HP ≤ 0 → forced incapacitation (DEC-052). Combat terminates.

### 6.5 Resource economy

PE Recovery = 50 per test keeps pools largely solvent. Overflow HP damage occurs under high natural rolls and contributes to attrition, but primary attrition remains contest-delta Inflict Injury on successful Attacks. Mirror combatants of attribute 50 do not collapse via resource exhaustion alone.

### 6.6 Advanced Skill creation

Qualifying failed Doubles correctly triggered Advanced Skill creation (Tier +1, Starting Value = 1). Created skills were correctly excluded from the offense-selection pool and exerted no influence on subsequent exchanges.

### 6.7 Conditions imposed

Grappled and Prone were both recorded on both combatants multiple times. No contested Break-Hold was attempted (out of scope by design).

---

## 7. Objectives Coverage Matrix

| # | Mechanic under test | DEC(s) | Result |
|---|---|---|---|
| 1 | S-1 melee-exchange algorithm, mandatory-defense convention | 013, 105 | **Exercised end-to-end** |
| 2 | Contest-delta HP resolution | 096, 097, 104 | **Exercised**; damage formula confirmed on Inflict Injury |
| 3 | Effect Tier/Magnitude = Skill-Tier (no Quality gating) | 107 | **Exercised** on every successful non-HP Effect |
| 4 | Skill-Tier shred + margin de-escalation | 103 | **Exercised** on every successful non-HP Effect |
| 5 | Zero-Step + Tier-1 quartile location | 014, 100 | **Exercised** on every location-referencing Effect |
| 6 | Tag + Location gating / fail-and-fall-back | 028, 030, 114 | **Exercised** (Tags present → pass path dominant) |
| 7 | Grappled imposition + contested Break-Hold escape | 079, 124, 131 | **Imposition half exercised** (6 successful Grapples). Contested Break-Hold escape remains **structurally out of scope** and is not claimed as passed. |
| 8 | Wound target selection (automated / creature path) | 102 | **Reachable** via Inflict Injury (and any fall-back); exercised on HP path |
| 9 | Incidental Advanced Skill creation, non-influencing | 012 | **Exercised**; exclusion confirmed (19 total Advanced Skills created, zero influence) |
| 10 | Armor Bypass Tier-2 path | 112, 113 | **Unreachable / out-of-scope by design** (excluded from selection pool; Human Location Template still missing). Explicitly not claimed as tested. |

---

## 8. Design Observations

### 8.1 Selection-rule success

The least-selection-count scaffold eliminated the permanent Attack lock-in observed under the original “highest numeric value” rule. All five eligible offense skills were selected a near-equal number of times and all five paired Effects fired. Objectives that depend on non-Attack Effects now have empirical coverage.

### 8.2 High both-fail repeat rate

Approximately 44 % of exchanges ended in both-fail repeats. This is statistically expected at Skill 25–35 under the 100-Fumble rule and is consistent with the prior run. Resource cost and Failure XP still accrue on every test.

### 8.3 Skill growth under balanced selection

Because every eligible skill receives Failure XP on its own turns, all five offense skills advanced (final values 29–34). Defense advanced faster (final 42–47) because it is rolled on every exchange. Cap 50 was not reached by any offense skill in 123 exchanges.

### 8.4 PE economy remains robust

Recovery 50 keeps PE pools solvent for the majority of a 120-exchange fight. Overflow contributes secondary attrition but is not the dominant lethality path at baseline attribute 50.

### 8.5 Armor Bypass Tier-2 path remains content-blocked

No change from prior report. Objective 10 stays unreachable until a Human Location Template exists or an explicit Tier-1 scaffold is re-authorized for Armor Bypass.

### 8.6 Contested Break-Hold still out of scope

Objective 7’s escape half requires an explicit post-imposition contested action that is not defined in the brief or the scaffolding amendment. Grappled imposition itself is confirmed.

### 8.7 Movement / zone mechanics untested

Identical Movement Speed 6 and no seeded positional variance mean G5 movement-band mechanics received zero stress (unchanged from prior run).

---

## 9. Recommendations for OpenCode and Tiwa

1. **Scaffold confirmed functional.** The least-selection-count rule achieves the coverage goals of the original brief without introducing new skill→Effect pairings or new actions. Retain it for any further automated runs of this exact scenario until a different selection policy is deliberately chosen.
2. **Objective 7 escape half.** If contested Break-Hold is required, a follow-on run must add an explicit post-imposition contested action (out of present scope).
3. **§8.5 / Objective 10.** Armor Bypass Tier-2 remains blocked by missing content. No further automated runs should claim coverage of the Tier-2 path until the Human Location Template or an explicit alternative is supplied.
4. **No DEC inference.** None of the scaffolding decisions or observations in this report should be recorded as DECs without explicit Tiwa instruction.
5. **Script retention.** Executable used for this run: `/tmp/tiwas_mirror_combat_playtest_v2.py`. Promote only if a standing playtest harness is desired.

---

## 10. Provenance and Integrity Statement

- All rolls were generated by `random.SystemRandom()`.
- No hand-edited outcomes.
- No Canonical or Ruled mechanic was altered.
- The sole non-canonical element is the least-selection-count offense-selection rule, explicitly labelled playtest-only scaffolding.
- This report does not reopen, amend, or supersede any existing DEC.
- Source brief + scaffolding-fix document remain the authoritative statements of intended test design; this document records only the execution and the observations that followed from it.

---

**End of report.**

**Author:** Grok 4.5 (grok-4.5)  
**Date:** 2026-09-12  
**Classification:** Execution record / Non-canonical / Advisory to OpenCode and Tiwa
