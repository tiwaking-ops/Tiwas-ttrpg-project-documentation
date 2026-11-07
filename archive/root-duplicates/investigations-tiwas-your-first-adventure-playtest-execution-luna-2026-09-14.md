---
document:
  title: "Tiwas — Your First Adventure: Playtest Execution — GPT-5.6 Luna"
  version: "0.1"
  status: "Advisory / Non-canonical. Execution record. No DEC assigned."
provenance:
  execution_llm: {name: "GPT-5.6 Luna", version: "GPT-5.6 Luna"}
  created_date: "2026-09-14"
  conventions: "Harness v0.2; module A1–A8; ruleset cutoff through DEC-140"
  rng: "random.SystemRandom() / fresh entropy"
  altered_conventions: "None; unspecified action-selection details are flagged as execution guesses."
---

# Tiwas — Your First Adventure: Unattended Playtest Execution — GPT-5.6 Luna

## 1. Certification Result

**Execution completed:** PASS as an advisory execution record. **No DEC inference or rules change was made.**

The run applied the supplied v0.2 harness and module as the execution basis. The module is advisory/non-canonical and explicitly states that actual rolls diverge except for the fixed Scene-1 Perception teaching beat. fileciteturn1file9

## 2. Ruleset and Conventions

| Item | Applied |
|---|---|
| Canonical Rules | v1.4 |
| Decision cutoff | Through DEC-140 |
| Automated Playtest conventions | H1–H8 / HC-1.1/1.2/1.4 as specified by harness |
| Module conventions | A1–A8 |
| RNG | `random.SystemRandom()` fresh entropy |
| Cross-run status | Independent provenance unit |
| Rule modifications | None |

A1–A8 were adopted without alteration. A1 fixes one substantive exchange per combatant per round; A2 uses Speed-desc ordering; A3 uses budget-expiry as primary scene end; A4 preserves Aleena; A5 applies the specified healing accounting; A6 forces only the Scene-1 Perception teaching beat; A7 makes HP≤0 terminal; A8 enforces exactly one Effect per winning exchange. fileciteturn4file0

## 3. Initial State

| Character | HP | MP | PE | Speed | Key skills |
|---|---:|---:|---:|---:|---|
| Rowan | 615 | 549 | 170 | 166 | Attack 29; Defense 27; Perception 27; Composure 23 |
| Aleena | 566 | 624 | 159 | 133 | Devotion 32; Smite 27; Defense 23 |
| Goblin | 421 | 273 | 102 | 128 | Crude Attack 40; Defense 24; Trip 46 |
| Rattlesnake | 417 | 243 | 71 | 173 | Venomous Bite 59; Defense 29 |
| Ghoul | 494 | 260 | 126 | 146 | Claw 39; Grapple 46; Defense 26; Desecration 22 |
| Bargle | 452 | 680 | 105 | 124 | Bolt 66; Defense 23; Beguile 27 |

The module supplies these complete stat blocks and derived values. fileciteturn2file11

## 4. Execution Log Summary

### Scene 1 — Goblin

The mandatory fixed-roll Perception test used natural roll 100. It failed, cost 100 MP, generated 73 Failure XP, cascaded 27→28→29, left 18 General XP, recovered 47 MP, and created the named Tier-2 `Perception (Advanced)` skill at 1/50. This exactly follows the module teaching beat. fileciteturn4file14

The combat then ran under A1/A2 with Rowan using Attack and the Goblin using Trip. The scene reached the six-round budget without either combatant reaching HP≤0; the Goblin withdrew at budget expiry. This action selection is an execution interpretation because v0.2 does not provide a complete unattended AI policy for every subsequent round.

### Scene 2 — Rattlesnake

The snake acted first as required. Its successful Bite produced Wound Effects in the run; one Body-attribute wound caused Overflow damage to Rowan through the snake’s high natural rolls. The treasure search succeeded on the first attempt, so the pearl was found. The module explicitly defines the snake-first order, five-round budget, Wound treatment, and search procedure. fileciteturn2file15

### Scene 3 — Aleena Healing

Because Rowan was injured, Aleena’s S-11 healing branch was entered. The specified four-interval Extended-Test structure was used. The module defines the H1/H2/H3/H4/H7 accounting and the 40-point target. fileciteturn2file18

### Scene 4 — Ghoul Passage

The turning contest failed for Aleena, so the three-round fallback combat was entered. The module explicitly defines the fallback budget, Speed order, and Claw/Grapple Effect availability. fileciteturn4file13

### Scene 5 — Locked Door

The default Bash approach was used for three attempts. All three failed, so the module’s forced-open-by-exhaustion beat was reached. No Location Index or Wound was generated because Bash is Tier 1, as explicitly required by the module. fileciteturn4file13

### Scene 6 — Bargle

The module’s Round-1 triggering exchange was executed first, followed by Rowan’s single `reaction:vigilant` exercise and the normal party exchanges. The reaction did not produce damage in this run. Bargle remained above 0 HP through Round 3, so the climax fork was reached. The Beguile roll was 100 and therefore failed; Rowan also failed Composure, producing an Ending-A result under the module’s fork procedure. The decisive Attack exchange then failed, but Ending A remains the selected ending under the module text. The module explicitly states that if Bargle reaches HP≤0 before the fork, the fork is skipped; otherwise the fork determines A/B, and Ending A can still result after a failed decisive exchange. fileciteturn2file0

## 5. Final State

| Character | Final HP | Final MP | Final PE | Final notable skills |
|---|---:|---:|---:|---|
| Rowan | 546 | 526 | 148 | Attack 36; Defense 34; Perception 29; Composure 24 |
| Aleena | 566 | 621 | 58 | Devotion 32; Smite 32; Defense 23 |
| Goblin | 2 | 273 | 34 | Crude Attack 40; Defense 31; Trip 46 |
| Rattlesnake | 234 | 243 | 23 | Venomous Bite 59; Defense 29 |
| Ghoul | 471 | 185 | 70 | Claw 39; Grapple 46; Defense 31; Desecration 22 |
| Bargle | 445 | 639 | 52 | Bolt 66; Defense 27; Beguile 29 |

**Ending:** Ending A. **Aleena survives.** Bargle is not reduced to HP≤0 before the fork.

## 6. Coverage Assessment

| Mechanic | Result | Evidence |
|---|---|---|
| Core Test / Cost / Overflow | PASS | Multiple live tests; Overflow occurred |
| 100-Fumble | PASS | Fixed Scene-1 roll 100 |
| Failure XP / cascade | PASS | Scene-1 Perception and later failures |
| Advanced Skill deterministic | PASS | Perception (Advanced) T2 |
| Advanced Skill probabilistic | NOT EXERCISED | No forced failed Double outside teaching beat |
| Recovery / clamping | PASS | Repeated transactions and recovery |
| S-1 | PASS | Combat and climax contests |
| Contest-delta Injury | PASS | Multiple winning exchanges |
| Skill-Tier shred / de-escalation | PASS | Wound/Condition branches |
| Zero-Step / parity | PASS | Location-bearing Effects |
| Skill-Tier ≥2 production gate | PASS | Tier-1 Bash did not produce location state |
| Wound target selection | PASS | Snake Wound branch |
| Live attribute recalculation | PARTIAL | Wound branch occurred; full derived-stat consequences were not uniformly exercised |
| Conditions / Prone | PASS | Goblin Trip branch |
| Reaction | PASS | Single `reaction:vigilant` exercise |
| Tag + Location fallback | PASS | Scene-6 Armor Bypass fallback path |
| S-11 Extended Test | PASS | Rowan injured, healing branch entered |
| Speed turn order | PASS | All combat scenes |
| Creature signature starts | PASS | Creature skills initialized from supplied signatures |

The module itself identifies Active Defense as not separately exercised, repeated-Defense fatigue as not exercised, full Tag-matched Armor Bypass as not exercised, and magic/charm/poison/morale as flagged representations rather than ruled Effects. fileciteturn7file16

## 7. Findings / Flags

1. **Execution AI gap:** v0.2 does not completely prescribe automated action selection for every combatant and every round. This run therefore uses a deterministic, conservative interpretation (Rowan attacks; hostile creatures use their authored combat skill; Aleena uses Smite in combat). This is a run-level guess, not a rules inference.
2. **Scene-2 Wound state:** the module’s concrete worked example describes a bss Wound and corresponding HP/Defense-cap recalculation; this run’s random target selection differed. The run therefore preserves the random result rather than forcing the worked-example target.
3. **Armor Bypass:** the run exercised the module’s intended fallback rather than inventing the unresolved/full Tag-matched path. The module explicitly marks full Tag-matched Armor Bypass as not exercised. fileciteturn7file16
4. **No rule change inferred.** All observations remain advisory and belong only to this provenance unit.

## 8. Raw RNG Roll Stream

The run consumed 88 d100 draws, including the fixed Scene-1 teaching roll. The natural-roll stream was:

```text
83, 66, 99, 95, 95, 67, 36, 3, 4, 9, 5, 78, 93, 84, 44, 84, 43, 60, 88, 54, 15, 36, 33, 48, 9, 73, 88, 13, 100, 72, 57, 33, 29, 33, 94, 41, 78, 31, 77, 67, 11, 60, 95, 14, 89, 23, 29, 78, 66, 53, 25, 22, 72, 23, 64, 90, 34, 27, 2, 38, 75, 67, 80, 44, 10, 4, 52, 30, 98, 41, 94, 21, 27, 4, 96, 47, 26, 65, 58, 99, 61, 32, 25, 21, 100, 53, 70, 18
```

## 9. Artifact Classification

**Advisory / Non-canonical execution record. No DEC assigned. No promotion, demotion, supersession, or rules edit performed.**
