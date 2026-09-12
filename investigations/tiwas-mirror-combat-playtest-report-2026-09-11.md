# Tiwas — Mirror-Match Combat Stress Test Playtest Report

**Author:** GPT-5.6 Luna  
**Date:** 2026-09-11  
**Status:** Advisory / Non-canonical empirical playtest record  
**Source brief:** `tiwas-playtest-mirror-combat-design-brief-2026-09-10.md`  
**Random seed:** 20260911  
**Combats:** 250  
**Executable stress-slice exchange cap:** 20000

## 1. Execution basis

The supplied brief was executed against the latest available Tiwas decision state, not blindly against stale wording in the brief.

Important current-state corrections:

| Item | Brief | Executed interpretation |
|---|---|---|
| Automated combatant economy | Highest-valued offense selected | **Current DEC-106 creature rule:** automated playtest Characters are creatures and use all authored legal attacks on their turn, highest-applicable-Skill → lowest |
| Active Defense | Mandatory in the brief | Brief convention retained for this stress test; this is not the current voluntary-defense default |
| Armor Bypass Tier-2 location | Brief flags contradiction | **Execution blocked at the first successful Armor Bypass requiring Tier-2 template resolution**; no anatomy was invented |
| Location architecture | Brief references secondary roll | Current DEC-112 hierarchical single-source address model supersedes the former secondary-roll architecture |
| Fatigue | Brief predates DEC-135 | DEC-135 now exists, but this mirror run's one Defense per exchange does not create a repeated-defense sequence under the stated sequence boundary |

The current corpus explicitly leaves human-authored Location Template content and the 100-state allocation as content-authoring material. Therefore a Tier-2 Armor Bypass cannot be fully resolved from the supplied corpus without inventing content.

## 2. Baseline

Both combatants:

| Stat | Value |
|---|---:|
| All 24 attributes | 50 |
| HP | 600 |
| MP | 600 |
| Physical Energy | 150 |
| Speed | 150 |
| Energy Regen | 100 |
| Movement Speed | 6 |
| Tier-2 combat Skill Cap | 50 |
| Starting combat Skill | 25 |

## 3. Executable stress slice

To obtain meaningful end-to-end combat statistics without inventing the unresolved Tier-2 anatomy, the primary statistical run used:

`Attack, Grapple, Trip, Disarm, Equipment Damage`

Equipment/Tag matching was corrected to the authored loadout: the held weapon is an arm/main-hand item; body armor is torso-bound. A Tag-gated Effect that misses its required location falls back to Base Inflict Injury.

### 3.1 Combat outcomes

| Measure | Result |
|---|---:|
| Combats | 250 |
| Alpha wins | 115 |
| Beta wins | 134 |
| Unresolved at cap | 1 |
| Mean exchanges/combat | 127.94 |
| Median exchanges/combat | 127.5 |
| Min exchanges | 45 |
| Max exchanges | 221 |

### 3.2 S-1 outcomes

| Outcome | Count | Rate |
|---|---:|---:|
| Attacker wins | 7001 | 21.89% |
| Defender wins | 10496 | 32.81% |
| Repeat | 14489 | 45.30% |

### 3.3 Effect-path coverage

| Skill / Effect | Exchanges | Wins | Tag fallback | Location generated |
|---|---:|---:|---:|---:|
| Attack / Inflict Injury | 6497 | 1428 | 0 | 0 |
| Grapple / Grappled | 6440 | 1434 | 0 | 1434 |
| Trip / Prone | 6399 | 1397 | 0 | 1397 |
| Disarm / Disarm | 6353 | 1366 | 1117 | 1366 |
| Equipment Damage / Equipment Damage | 6297 | 1376 | 776 | 1376 |

## 4. Armor Bypass blocker probe

The full brief-defined attack set was also executed until the first Armor Bypass win requiring Tier-2 resolution.

| Measure | Result |
|---|---:|
| Full-set combats attempted | 250 |
| Runs blocked by Tier-2 Armor Bypass template | 244 |
| Median exchange at blocker | 17.0 |

**Finding:** the supplied/current corpus does not provide enough creature-specific Location Template content to resolve the Tier-2 address deterministically. DEC-112 makes the template a content-authoring dependency. The correct playtest behavior is therefore to stop/flag the branch rather than invent a mapping.

## 5. Mechanical observations

1. **The mirror baseline is mechanically symmetric.** Any systematic Alpha/Beta difference should arise from initiative and stochastic rolls rather than stat construction.
2. **The current creature multi-action rule materially changes the brief's intended combat loop.** A creature/automated character does not simply choose one highest-valued attack; it uses all authored legal attacks in descending applicable-Skill order.
3. **The brief's 1:1 Skill→Effect mapping remains a scenario convention.** It is not a general Tiwas Skill identity gate.
4. **Tag-gated Effects visibly exercise fallback behavior.** Disarm can fall back to Base Inflict Injury when the struck coarse zone does not contain the required held main-hand object.
5. **Armor Bypass is the principal execution blocker.** Its Tier-2 location resolution depends on content that the current corpus explicitly leaves open.
6. **No invented anatomy was used.** This preserves the authority boundary and makes the blocker itself a valid playtest finding.

## 6. Evidence / inference / ruling separation

### Empirical findings
- 250 mirror combats were executed in the executable slice.
- S-1 outcome frequencies and combat lengths are recorded in the attached CSV.
- Armor Bypass Tier-2 resolution reached a corpus-supported execution boundary and was not fabricated beyond it.

### Design inference
- The current automated-creature multi-action rule makes a mirror match exercise the interaction of multiple consecutive S-1 exchanges much more strongly than the original one-action brief.
- The unresolved creature Location Template is a genuine blocker to claiming that the entire six-effect stack was executed end-to-end.

### No new ruling
This playtest does **not** change, supersede, promote, or create any DEC.

## 7. Artifacts

- Raw exchange log: `tiwas-mirror-combat-playtest-log-2026-09-11.csv`
- Machine-readable summary: `tiwas-mirror-combat-playtest-summary-2026-09-11.json`

