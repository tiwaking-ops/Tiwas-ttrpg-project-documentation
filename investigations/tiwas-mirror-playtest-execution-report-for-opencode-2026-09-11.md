---
document:
  title: "Mirror-Match Combat Stress Test — Execution Report (Advisory Handoff to OpenCode)"
  type: "Playtest Execution Report"
  version: "1.0"
  status: "Advisory / Non-canonical. No DEC assigned. No recording action taken or requested. Pending Tiwa's review and explicit direction before OpenCode performs any registry action."
  addressee: "OpenCode (documentarian role, live GitHub repository)"
  supersedes: "None"
  related_documents:
    - "tiwas-playtest-mirror-combat-design-brief-2026-09-10.md (v0.2, source brief)"
    - "tiwas-mirror-playtest-results-2026-09-11.md (prior in-chat results summary; superseded in scope by this report)"
provenance:
  author_llm:
    name: "Claude Sonnet 5"
    version: "claude-sonnet-5"
  role: "Advisory only — per standing project governance, Claude presents options, runs simulations/playtests, and drafts documents; Claude does not rule, assign DEC numbers, or record decisions."
  created_date: "2026-09-11"
  last_modified_date: "2026-09-11"
  requested_by: "Tiwa (in-session request: 'write formal project documentation report for OpenCode about the complete results from this chat')"
---

# Mirror-Match Combat Stress Test — Execution Report

**Author:** Claude Sonnet 5 (`claude-sonnet-5`)
**Prepared for:** OpenCode (documentarian; live repository authority)
**Prepared by direction of:** Tiwa
**Document class:** Advisory playtest execution report — **not** a ruling, **not** a proposal edit, **not** a canonical or non-canonical decision record.

---

## 0. Governance Statement

This report is issued under the project's standing advisory-only constraint. It:

- Assigns **no DEC number** and proposes none.
- Records **no ruling**. Every finding below is an empirical observation from one executed simulation run-pair, not a designer decision.
- Requests **no registry action**. OpenCode should take no recording, promotion, or file-edit action on the basis of this report alone. Any such action requires Tiwa's explicit direction, per standing project governance (`governance/authority.md`; LLM Governance Rules, Roadmap §24 / Corpus §24).
- Does **not** alter the status of `tiwas-playtest-mirror-combat-design-brief-2026-09-10.md`, which remains "Advisory / Non-canonical... Pending Tiwa review."
- Does **not** touch, resolve, or narrow the open DEC-112/DEC-113 Armor Bypass contradiction, G1, G3, or any other open corpus item. Where this report's findings bear on open items, that is noted explicitly and only as a flag for Tiwa's attention.

This report is Claude's own advisory work product. It is not styled or represented as an OpenCode-authored documentation artifact.

---

## 1. Purpose and Scope

**Purpose.** To document, for OpenCode's records and Tiwa's review, the complete results of executing the Mirror-Match Combat Stress Test design brief (`tiwas-playtest-mirror-combat-design-brief-2026-09-10.md`, v0.2) as a running simulation, including:

1. The methodology used to translate the brief into an executable script.
2. Every point at which the brief was underspecified and a modeling choice had to be made to run it at all (flagged individually — none are rulings).
3. The full quantitative results of two executed variants.
4. An emergent structural finding not anticipated by the brief itself.
5. Coverage assessment against the brief's own ten stated test objectives (§9 of the brief).
6. The complete file manifest delivered alongside this report.

**Scope boundary.** This report covers only the single chat session in which the brief was executed (2026-09-11). It does not cover the brief's authorship (a separate, already-delivered artifact) and does not extend to any other open playtest thread (e.g., BToV-Madness creature conversions).

---

## 2. Source Materials

| Item | Role | Status |
|---|---|---|
| `tiwas-playtest-mirror-combat-design-brief-2026-09-10.md` (v0.2) | Design brief executed by this report | Advisory / Non-canonical, unchanged by this report |
| `mirror_playtest.py` | Executable simulation implementing the brief | New artifact, delivered with this report |
| `exchange_log_run_a_priority.csv` | Full per-roll log, Run A | New artifact, delivered with this report |
| `exchange_log_run_b_random.csv` | Full per-roll log, Run B | New artifact, delivered with this report |
| `summary.json` | Machine-readable summary of both runs | New artifact, delivered with this report |

All dice rolls were generated with `random.SystemRandom()` (OS-entropy source), per standing playtest methodology recorded in prior sessions.

---

## 3. Methodology

### 3.1 Baseline scenario (unchanged from the brief)

- Combatants "Alpha" and "Beta": mechanically identical. All 24 attributes = 50. HP = 600, MP = 600, Physical Energy = 150, Speed = 150, Movement Speed = 6.
- Six Tier-2 skills each (Cap 50, Starting Value 25): Attack, Grapple, Trip, Disarm, Equipment Damage, Defense. All Body-domain (Physical Energy resource).
- Skill→Effect pairing per the brief's §2: Attack → Inflict Injury; Grapple → Impose Condition: Grappled; Trip → Knock Prone; Disarm → Disarm/Break Hold; Equipment Damage → Equipment Damage; Defense → defensive roll only.
- Weapon (`slot:main_hand`, `state:held`, `offense:melee`, `damage:slashing`, `handling:light`) and body armor (`slot:body`, `state:worn`, `defense:armor`) equipped on both combatants, per the brief's §3.
- Armor Bypass excluded from scope entirely, per the brief's §8.5 playtest-scoped decision (non-canonical, no DEC assigned; does not resolve the underlying DEC-112/DEC-113 contradiction).
- Melee-exchange algorithm per DEC-105: single simultaneous Core Test pair per exchange, both combatants always roll; repeat on both-fail or exact-Quality-tie; Defense mandatory (playtest convention per DEC-105).
- HP resolution per DEC-104 (contest-delta = Winner's Margin − Defender's Margin).
- Non-HP Effect resolution per DEC-103 (Skill-Tier shred + margin de-escalation, unified carry rule).
- Location resolution per DEC-014 (Zero-Step) and DEC-100 (Tier-1 quartiles: 1–25 Legs, 26–50 Torso, 51–75 Arms, 76–100 Head), Tier-1 coarse only per DEC-113 R2 (no Tier-2 sub-roll, consistent with Armor Bypass exclusion).
- Tag+Location gating per DEC-114 R2 for Disarm and Equipment Damage only (Grapple and Trip are not Tag+Location gated, per DEC-028's enumerated scope); mismatch → fail-and-fall-back to Base Inflict Injury per DEC-030.
- Failed-Double → Advanced Skill creation per DEC-012, Starting Value = 1 (brief's explicit instruction), excluded from the offense-selection pool thereafter (brief §4.2 step 9).
- Termination: first HP ≤ 0 (forced incapacitation, DEC-052), per the brief's §4.3 minimal default.

### 3.2 Point of methodological extension beyond the brief

The brief's §8.4 explicitly flags the offense-skill tie-break rule as unresolved ("No corpus rule covers this... Your call") and offers a fixed-priority order only as a non-binding suggested default. To assess whether that specific suggestion drove any observed behavior, **two full variant runs were executed from the same script**, differing only in this one parameter:

| Run | Tie-break rule |
|---|---|
| A | Fixed priority order: Attack > Grapple > Trip > Disarm > Equipment Damage (the brief's suggested default) |
| B | Uniform-random selection among tied candidates |

This is a methodological extension made to produce a more informative report, not a deviation from or correction to the brief. Both runs are reported in full below.

---

## 4. Results — Run A (Fixed-Priority Tie-Break)

| Metric | Value |
|---|---|
| Tie-break mode | Priority (Attack > Grapple > Trip > Disarm > Equipment Damage) |
| Rounds | 21 |
| Logged exchanges (including repeats) | 80 |
| Termination cause | HP ≤ 0 (DEC-052 forced incapacitation) |
| Winner | Alpha |
| Alpha final HP / PE | 393 / 77 |
| Beta final HP / PE | −36 / 63 |
| Outcome distribution | repeat-bothfail: 39; attacker-wins: 21; defender-wins: 20 |
| Effects that fired | Inflict Injury ×21 (100% of wins) |
| Tag-check results | None attempted (Attack carries no Tag/Location gate) |
| Offense-skill usage | Attack: 80/80 (100%), both combatants |
| Alpha Advanced Skills created | 3 — all off Defense (Tier‑3, Starting Value 1) |
| Beta Advanced Skills created | 8 — 4 off Defense, 4 off Attack |
| Alpha total Failure XP / General XP | 1,601 / 757 |
| Beta total Failure XP / General XP | 1,950 / 828 |
| Alpha final Attack / Defense skill value | 38 / 39 |
| Beta final Attack / Defense skill value | 42 / 42 |
| Conditions ever applied (Grappled / Prone / Disarmed / EquipmentDamaged) | 0 (none — Grapple, Trip, Disarm, and Equipment Damage were never selected by either combatant) |

**Result summary.** Both combatants used Attack exclusively for the entire 80-exchange encounter. Beta's skills grew marginally higher on raw value, but Alpha won on roll variance. No non-HP Effect, no Location Index, and no Tag check occurred anywhere in this run.

---

## 5. Results — Run B (Uniform-Random Tie-Break)

| Metric | Value |
|---|---|
| Tie-break mode | Uniform-random among tied candidates |
| Rounds | 30 |
| Logged exchanges (including repeats) | 108 |
| Termination cause | HP ≤ 0 (DEC-052 forced incapacitation) |
| Winner | Alpha |
| Alpha final HP / PE | 273 / 72 |
| Beta final HP / PE | −8 / 66 |
| Outcome distribution | repeat-bothfail: 47; attacker-wins: 29; defender-wins: 31; repeat-tie: 1 |
| Effects that fired | Impose Condition: Grappled ×14; Equipment Damage ×6; Equipment Damage → fail-and-fall-back → Inflict Injury ×9 |
| Tag-check results | pass: 6; fail-and-fall-back: 9; n/a (Grapple, ungated): 14 |
| Offense-skill usage | Alpha: Equipment Damage 52/52 (100%); Beta: Grapple 56/56 (100%) |
| Alpha Advanced Skills created | 9 — 5 off Equipment Damage, 4 off Defense |
| Beta Advanced Skills created | 6 — 5 off Grapple, 1 off Defense |
| Alpha total Failure XP / General XP | 2,169 / 962 |
| Beta total Failure XP / General XP | 2,552 / 1,345 |
| Alpha final Equipment Damage / Defense skill value | 42 / 44 |
| Beta final Grapple / Defense skill value | 44 / 42 |
| Conditions applied to Beta (by Alpha) | 7 Equipment-Damaged StateRecords (Tier 1–2, Magnitude −1/−2, zones Torso ×4 / Arms ×2 / Torso ×1) |
| Conditions applied to Alpha (by Beta) | 13 Grappled StateRecords (Tier 1–2, Magnitude −1/−2) |

**Result summary.** Alpha used Equipment Damage exclusively; Beta used Grapple exclusively — for the entire 108-exchange encounter, each combatant never once selected any of the other four offense skills. Of Alpha's 15 successful Equipment Damage declarations, 9 landed on a struck zone (Legs or Head) with no equipped item present and correctly fell back to Base Inflict Injury per DEC-030; the remaining 6 landed on Arms (weapon) or Torso (armor) and produced genuine Equipment-Damaged StateRecords. All 14 of Beta's Grapple wins applied the Grappled Condition unconditionally, with no fallback branch (consistent with Grapple's exclusion from DEC-028's Tag+Location gate).

---

## 6. Cross-Run Comparative Finding

**Finding (empirical, both runs, not a ruling):** Regardless of which offense-skill tie-break convention is used, each combatant converges on selecting **exactly one** offense skill for the entire encounter and never varies from it once selected.

**Mechanism.** The offense-selection rule specified by the brief ("the skill with the currently highest numeric value," §4.2 step 1) interacts with the Skill Roll Pool / Failure XP mechanic (Core Rules §10, DEC-010) such that:

1. Only the skill actually tested on a given exchange can gain Failure XP and grow.
2. All five candidate skills begin tied (Starting Value 25 each).
3. Whichever skill is selected on the very first exchange — by tie-break, priority or random — is the only skill exposed to failed rolls, and therefore the only skill that can grow.
4. Once that skill's value exceeds the other four (which happens on virtually the first failed roll, since Starting Value 25 against a d100 fails roughly 75% of the time), it is never tied again, and the tie-break clause is never re-consulted.
5. This produces permanent single-skill lock-in for the remainder of the combat, independent of which specific tie-break rule governs the initial selection.

**Consequence for this brief's own test objectives.** The brief's §9 lists ten mechanics intended to be validated by this scenario. Run A (the brief's own suggested tie-break) exercised only 3 of the 10; the remaining 6 (Effect Tier/Magnitude, Skill-Tier shred, Location resolution, Tag+Location gating, Grappled/Break-Hold, and — in both runs — Wound target selection) were never triggered, because Attack (Inflict Injury, HP-only, no location, no Effect record) was the only skill ever used by either combatant. Run B, using a different but equally corpus-unsupported tie-break, incidentally exercised more of the mechanic stack (5 of 10) purely because the random draw happened to select two different, mechanically richer skills — but still left Trip and Disarm completely untested, and still exhibits the same single-skill lock-in structurally.

**This is a design-brief-level finding, not a Core/S-1/S-3/S-4 rules finding.** Nothing about DEC-103, DEC-104, DEC-105, DEC-014, DEC-100, DEC-114, or DEC-030 is implicated as broken; each of those mechanics behaved exactly as specified whenever it was actually invoked (see §5). The finding concerns only the scenario-construction choice in the brief's own §4.2 step 1 (offense-skill selection heuristic), which is itself explicitly non-canonical playtest scaffolding, not a Tiwas rule.

**Independent gap, not caused by tie-break lock-in.** Objective 8 (Wound target selection, DEC-102) could not have fired in *either* run regardless of tie-break outcome, because the brief's own §2 skill→Effect table never pairs any offense skill with "Impose Condition: Wounded" — only Grapple, Trip, Disarm, and Equipment Damage are represented, none of which is a Wound-producing Effect. This is a scope gap in the brief itself, separate from the lock-in finding above.

---

## 7. Test-Objective Coverage Assessment (against brief §9)

| # | Mechanic under test | Governing DEC(s) | Run A | Run B |
|---|---|---|---|---|
| 1 | S-1 melee-exchange algorithm, mandatory defense | 013, 105 | Exercised | Exercised |
| 2 | Contest-delta HP resolution | 096, 097, 104 | Exercised (21 direct hits) | Exercised (9 via fallback) |
| 3 | Effect Tier/Magnitude = Skill-Tier | 107 | Not exercised | Exercised |
| 4 | Skill-Tier shred + margin de-escalation | 103 | Not exercised | Exercised |
| 5 | Zero-Step + Tier-1 quartile location resolution | 014, 100 | Not exercised | Exercised (15 location-referencing rolls) |
| 6 | Tag+Location gating / fail-and-fall-back | 028, 030, 114 | Not exercised | Exercised (6 pass, 9 fallback) |
| 7 | Grappled imposition + contested Break-Hold escape | 079, 124, 131 | Not exercised | Partially exercised — Grappled applied 14×; Break-Hold escape attempt never occurred (no combatant declared an escape action in either run) |
| 8 | Wound target selection (automated/creature path) | 102 | Not reachable — no offense skill in scope is paired with a Wound Effect | Not reachable — same gap |
| 9 | Incidental Advanced Skill creation, non-influencing | 012 | Exercised (11 total across both combatants) | Exercised (15 total across both combatants) |
| 10 | Armor Bypass Tier-2 path | 112, 113 | Out of scope by design (brief §8.5) | Out of scope by design (brief §8.5) |

**Net coverage:** Run A validated 3/10 objectives; Run B validated 5/10 objectives with 1 partially validated; objective 8 was unreachable in both; objective 10 was intentionally excluded from scope in both, per the brief's own prior decision.

---

## 8. Modeling Assumptions Required for Execution (flagged, non-canonical)

The brief left the following points underspecified for literal script execution. Each was resolved by a documented modeling choice below so the logs are interpretable. **None of these are rulings, proposals, or DEC candidates** — they are implementation notes scoped to this one executable artifact.

| ID | Underspecified point | Modeling choice made | Basis |
|---|---|---|---|
| M1 | DEC-104's "never 0 on a win" floor value | If `Winner's Margin − Defender's Margin ≤ 0`, damage is floored to **1** HP | Minimal reading consistent with "never 0"; no other floor value is stated in the register |
| M2 | DEC-103 cascade depth on a large negative negation buffer | Implemented as a single Tier−1 step, buffer reset to new Tier value; not a multi-step cascade proportional to overflow | DEC-103's text describes one Tier−1/Mag=new-Tier transition and states "leftover margin lost"; both combatants use only Tier-2 skills throughout, so only the Atk=Def shred case was actually exercised |
| M3 | Zero-Step laterality parity basis (DEC-041(3)) | Parity applied to the post-swap Location Index value, not the pre-swap natural roll | More literal reading of "Zero-Step output digit-parity"; the alternative reading is not excluded by the cited text |
| M4 | Held-item Location for Tag-check purposes | Weapon (`state:held`, `slot:main_hand`) fixed at Arms; body armor (`state:worn`) fixed at Torso | Consistent with DEC-081 (held items take the holding limb's Location) and DEC-100's own zone names; no corpus text pins this down more precisely at the abstract Tier-1 zone level |
| M5 | Offense-skill tie-break (brief §8.4, explicitly unresolved) | Two full runs executed — priority (Run A, brief's suggested default) and uniform-random (Run B) | Brief explicitly invites either convention |
| M6 | Initiative tie-break re-evaluation frequency | Re-rolled every round (not just once at combat start), per DEC-095 step 7's literal wording | Speed never changed in either run (no Attribute Wound occurred), so this affected only turn order, not any numeric outcome |
| M7 | Grapple/Trip Tag+Location gate applicability | Modeled as **not** gated — DEC-028's Tag+Location requirement is read as scoped only to Disarm/Break Hold, Equipment Damage, and Armor Bypass, per its own enumerated text and DEC-114 R2's table | Direct reading of DEC-028 and DEC-114 R2's enumerated scope |

---

## 9. File Manifest

| File | Description | Rows / Size |
|---|---|---|
| `mirror_playtest.py` | Executable simulation (both runs share one code path; `tie_break` parameter is the only variant) | — |
| `exchange_log_run_a_priority.csv` | Full per-roll log, Run A | 80 data rows |
| `exchange_log_run_b_random.csv` | Full per-roll log, Run B | 108 data rows |
| `summary.json` | Machine-readable summary, both runs | — |
| `tiwas-mirror-playtest-results-2026-09-11.md` | Prior in-chat narrative results summary (informal companion to this report) | — |
| `tiwas-mirror-playtest-execution-report-for-opencode-2026-09-11.md` | This report | — |

Each CSV row records: exchange number, round, repeat sequence, actor, defender, offense skill chosen and its value at roll time, both natural rolls, both success flags, both Margins, outcome, declared Effect, Location Index/zone/laterality (where applicable), Tag-check result, resulting StateRecord, both combatants' HP and PE after the exchange, Overflow (both sides), Failure XP (both sides), and any Advanced Skill created (both sides).

---

## 10. Disposition

This report is submitted to OpenCode as documentation of an executed advisory playtest, for Tiwa's review. It:

- Does not request that OpenCode record any DEC.
- Does not request that OpenCode modify the design brief's status.
- Does not resolve any open corpus item (DEC-112/DEC-113, G1, G3, or otherwise).
- Surfaces one structural, brief-level observation (§6) and one scope gap (§6, final paragraph) for Tiwa's attention, should Tiwa wish to revise the brief or direct a follow-on scenario.

No further action is proposed by this report absent Tiwa's explicit direction.

**— End of report.**
