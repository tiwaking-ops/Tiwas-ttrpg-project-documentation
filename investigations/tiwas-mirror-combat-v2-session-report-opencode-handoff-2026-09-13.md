---
document:
  title: "Tiwas — Human-Templated Mirror Combat Stress Test v2: Session Report and OpenCode Handoff"
  version: "1.0"
  status: "Advisory / Non-canonical session report. No DEC assigned. Documents playtest activity only — records no ruling, resolves no open fork, and confers no authority on any content described herein."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-13"
  last_modified_date: "2026-09-13"
---

# Tiwas — Human-Templated Mirror Combat Stress Test v2
## Session Report and OpenCode Handoff

## 0. Document Status and Authority Boundary

This document is a **session report**, not a ruling, proposal, investigation, or design
draft in the sense governed by the 8-step Promotion Rule (Proposals/WIP §21 / REQ-021). It
records what was designed, executed, and observed in a single chat session on 2026-09-13.

- No DEC number is assigned or implied by anything in this report.
- No open corpus fork is resolved by this report.
- No content in this report is Canonical, Ruled, or binding on future sessions.
- All scenario conventions described below (Section 3) are **playtest-scoped house rules**
  authorized by Tiwa for this session only — they are not Tiwas rules and must not be
  read into the corpus.
- Per standing governance (`governance/status-model.md`, LLM Governance Rule 6 /
  `tiwas-implementation-roadmap...` §24 Rule 6), this report surfaces one open corpus
  tension (Section 6) rather than silently resolving it. It requires Tiwa's ruling before
  any future session treats it as settled.

**Required OpenCode action:** file this report under `investigations/` (or the project's
equivalent non-canonical evidentiary-record location); do **not** file under `canonical/`
or treat any table below as a recording target for the Decision Register unless Tiwa
explicitly rules on Section 6.

---

## 1. Session Purpose

Tiwa requested a second automated combat playtest to exercise systems the first
mirror-match playtest (`tiwas-playtest-mirror-combat-design-brief-2026-09-10.md`,
executed 2026-09-11/12, reconciled 2026-09-12) either could not reach or had not yet
tried: Wound target selection (DEC-102), full-depth Armor Bypass resolution now that
DEC-137 exists, mid-combat attribute growth via General XP, and mid-combat Advanced Skill
creation with the new skill remaining usable afterward.

The session followed a structured interview → tailored brief → execution workflow at
Tiwa's explicit request, rather than proceeding directly to design.

---

## 2. Interview and Scoping Decisions (Tiwa's answers, recorded verbatim in effect)

Three scoping questions were put to Tiwa before drafting the brief; all three answers are
load-bearing on the design and are recorded here for provenance:

| Question | Tiwa's answer |
|---|---|
| Combatant symmetry | **Symmetric mirror** (identical combatants, as in the 2026-09-10 playtest) |
| Location template | **Human-templated** (DEC-137), specifically to unlock full Tier-2 Armor Bypass resolution |
| Deliverable scope | **Design brief + execution + results**, in-session |

All other parameters (skill loadout, equipment/Tag loadout, exchange procedure, General
XP tie-break rule wording, Advanced-Skill effect-inheritance convention, termination
condition, out-of-scope systems) were drafted by Claude as a tailored design brief and
were not separately re-confirmed line-by-line by Tiwa before execution — see Section 7
for the reconfirmation checklist this raises.

---

## 3. Design Brief Summary (full text in the companion file)

Full brief: `tiwas-playtest-human-mirror-combat-v2-design-brief-2026-09-13.md`.

### 3.1 Combatants
Two identical automated combatants ("Alpha", "Beta"), all 24 attributes = 50 at start
(HP 600/600, MP 600/600, PE 150, Speed 150, Movement Speed 6 — DEC-004 formulas, matching
the 2026-09-10 baseline for comparability). Per DEC-076/102, both are treated as
**creatures** for stat-generation and Wound-target purposes.

### 3.2 Skill loadout (9 skills, Tier-2 at start)
Seven offense skills (Attack, Grapple, Trip, Disarm, Equipment Damage, **Wound**,
**Armor Bypass**) and two defense skills (Defense, Guard). The Wound and Armor Bypass
offense skills are new additions relative to the 2026-09-10 loadout, added specifically to
close that playtest's Objective 8 (Wound target selection, unreached) and Objective 10
(Armor Bypass, explicitly out of scope pending the Human template).

### 3.3 House rules authorized for this playtest only (not Tiwas rules)
1. **General XP mandatory spend** (Tiwa's instruction): any banked General XP (DEC-011
   remainder after the DEC-010 Skill Roll Pool cascade) is spent immediately on the
   combatant's lowest current attribute(s); ties broken alphabetically by 3-letter
   attribute code.
2. **Attack-skill selection** (Tiwa's instruction): the acting combatant selects uniformly
   at random among its currently unlocked offense skills each turn — this deliberately
   does **not** exercise DEC-106's automated-creature multi-attack default (flagged, not
   silently overridden — see brief §9.2).
3. **Defense-skill selection** (Tiwa's instruction): the defender always uses whichever of
   its current defensive skills has the highest numeric value; ties broken alphabetically.
4. **Advanced Skill creation** (Tiwa's instruction, matches canonical DEC-012 exactly): on
   a qualifying failed Double, the new skill's formula = all attributes of the failed
   skill's formula + one additional attribute chosen randomly. No deviation from DEC-012
   was introduced by this instruction.
5. **Advanced Skill effect inheritance** (Claude's drafting convention, flagged as such,
   not requested by Tiwa): a newly created Advanced offense/defense skill inherits its
   parent's paired Effect (or lack thereof) and joins the corresponding random-selection
   pool immediately — unlike the 2026-09-10 playtest's permanent exclusion of newly
   created skills.

### 3.4 Equipment and armor coverage
Both combatants carry an identical weapon (Arms-bound) and two armor pieces bound to
specific DEC-137 leaves: Body armor → Chest (idx 26–35), Helmet → Skull (idx 76–91).
Coverage was deliberately left incomplete (Legs, Neck, Abdomen, Pelvis, Groin, Spine,
Shoulder–Hand, Eyes/Ears/Nose/Jaw are unarmored) so that Armor Bypass's tag-match and
fail-and-fallback (DEC-030) paths would both be reachable.

### 3.5 Out of scope (flagged explicitly in the brief, not silently omitted)
DEC-106 creature multi-attack; DEC-132 Reactions; DEC-135 repeated-Defense Fatigue;
DEC-133 Movement/zone mechanics; DEC-124/131 contested Break-Hold escape.

---

## 4. Execution

**Method:** Python 3, `random.SystemRandom()` (OS entropy), single run, no forced seed.
Source: `mirror_combat_v2.py`. Full per-exchange log: `mirror_combat_v2_log.csv` (129
rows). Full end-state (attributes, skill values/tiers/caps, StateRecords, Advanced Skill
creation log) per combatant: `mirror_combat_v2_summary.json`.

**Termination:** 129 exchanges, 65 rounds. Beta reached HP = −22 and was forced
incapacitated (DEC-052). Alpha ended at 260/616 HP.

**Notable causal detail:** the terminating HP loss was **self-inflicted Overflow**
(DEC-007/DEC-007.A), not opponent damage — Beta's final action was a failed 77-roll
Armor Bypass attempt (Skill value 36) against 52 remaining Physical Energy, producing 25
Overflow applied directly to HP. This is correct behavior under the locked Core Test
Transaction, not an implementation defect, and is recorded here because it is a genuine
emergent finding about how punishing high-roll-cost tests become at low resource levels
relative to Skill — an observation, not a proposal, per the corpus's own
observation/proposal/rule discipline (Proposals/WIP §0).

---

## 5. Objective Reconciliation

All twelve stated test objectives fired at least once during the run. Full detail (counts,
representative CSV rows, per-objective DEC citations) is in
`tiwas-playtest-human-mirror-combat-v2-results-2026-09-13.md` §3. Headline items:

| Objective | Status | Evidence |
|---|---|---|
| Wound target selection (DEC-102) — **unreached by the 2026-09-10 playtest** | **Fired** | 9 Wound records; Alpha `bps`×5/`bpe`×2, Beta `bpe`×1 — consistent with DEC-102(2)'s random tie-break for automated/creature wounders |
| Full-depth Armor Bypass via DEC-137 — **explicitly out of scope in the 2026-09-10 playtest** | **Fired both directions** | 7 attempts; 1 tag-match on **Heart** (Chest armor binding), 6 fail-and-fallback (DEC-030) at unarmored leaves |
| DEC-103 Skill-Tier shred + margin de-escalation | **Fired**, including Tier-0 negation outcomes on several high-Tier Advanced Skill wins |
| General XP mandatory-lowest-attribute spend | **Fired continuously** (36 + 39 spend events); both combatants' final attribute spreads stayed within 51–52 across all 24 attributes |
| Advanced Skill creation, non-excluded | **Fired extensively** — 11 (Alpha) + 13 (Beta) Advanced Skills, up to Tier 5 |
| Uncapped/negative HP, forced incapacitation (DEC-052/108) | **Fired** — see §4 |

Remaining objectives (S-1 exchange algorithm, contest-delta HP, Zero-Step + Tier-1
quartile resolution, Tag+Location gating both directions for Disarm/Equipment Damage,
Grapple imposition) all fired as expected and are not separately flagged here as novel.

---

## 6. Open Corpus Tension Surfaced — Requires Tiwa's Ruling

**Not resolved by this session. Flagged per LLM Governance Rule 6 (never silently resolve
an open designer fork).**

DEC-136 R2 states: *"Skill-Tier maps directly to Location Tier with no cap."* Read
literally, this could mean a Skill-Tier-2 actor's location resolution should be truncated
to a Location-Tier-2 depth within the DEC-137 hierarchy (i.e., stop above leaf-level nodes
like Heart/Lungs/individual fingers). However:

- DEC-113 R2 classifies Armor Bypass as a **binary** Tier-1-vs-Tier-2 Effect
  classification (it is simply "the Tier-2 Effect"), not a depth that itself scales
  further with the acting Skill-Tier beyond that binary gate.
- DEC-137's adopted address table is not itself sub-labeled with per-node Tier numbers,
  so there is no mechanical instruction in the adopted text for *how* to truncate it even
  if truncation were intended.

This playtest resolved Armor Bypass to the **full DEC-137 leaf** (e.g., "Heart") whenever
the DEC-113 Tier-2 classification and the DEC-041 Skill-Tier≥2 gate were both satisfied,
without inventing a truncation scheme, on the reasoning that DEC-137 was adopted
specifically to give Armor Bypass a real deterministic target. **This is a playtest-scoped
interpretive choice, not a ruling**, and it is the same choice the design brief (§9.3)
flagged before execution — recorded here again for OpenCode's decision-register visibility
and Tiwa's eventual ruling. No DEC should be inferred from this session's use of the
full-depth reading.

**Suggested resolution paths for Tiwa (informational only, not a recommendation):**
1. Confirm the full-depth reading as the operative interpretation (closes the tension with
   no rule change).
2. Rule that Location-Tier depth scales with acting Skill-Tier independently of DEC-113's
   binary Tier-1/Tier-2 Effect classification, and specify how DEC-137's currently
   flat/unlabeled table should be truncated per Skill-Tier.

---

## 7. Reconfirmation Checklist for Tiwa

Before this session's material is treated as settled precedent for a future playtest,
please confirm or correct:

- [ ] The five house rules in §3.3 are acceptable as recorded (especially #5, which was
      Claude's drafting convention, not your explicit instruction).
- [ ] The Human-templated armor coverage choice (§3.4) — specifically, that leaving most of
      the body unarmored was an acceptable design choice for this run rather than something
      you'd want re-specified.
- [ ] The out-of-scope list (§3.5) reflects everything you'd want excluded, or whether a
      future run should fold in Reactions/Fatigue/Movement/Break-Hold-escape.
- [ ] The open corpus tension in §6 — whether you want to rule on it now or leave it open
      for a future session.

---

## 8. File Manifest

| File | Description |
|---|---|
| `tiwas-playtest-human-mirror-combat-v2-design-brief-2026-09-13.md` | Full design brief (baseline, skills, house rules, procedure, flagged assumptions) |
| `tiwas-playtest-human-mirror-combat-v2-results-2026-09-13.md` | Full results report and objective-by-objective reconciliation |
| `mirror_combat_v2.py` | Simulation source (Python 3, `random.SystemRandom()`) |
| `mirror_combat_v2_log.csv` | Full 129-exchange per-roll log |
| `mirror_combat_v2_summary.json` | Final attributes, skill states, StateRecords, Advanced Skill creation log per combatant |
| This document | Session report and OpenCode handoff |

---

## 9. Required OpenCode Actions

1. File this report and its companions under the project's non-canonical evidentiary
   record location (`investigations/` or equivalent) — not `canonical/`.
2. Do **not** create or renumber any DEC entry from this session's content.
3. Surface Section 6 (open corpus tension) to Tiwa for a ruling decision; do not resolve it
   on OpenCode's own authority.
4. If Tiwa rules on Section 6 or on any item in the Section 7 checklist, record that
   ruling as a new dated entry per standard procedure — this document should not be
   edited in place to absorb a future ruling.

---

## 10. Governance Statement

Per `governance/status-model.md` and `governance/authority.md`: this document is Evidence
class **Empirical finding** (a single simulation run) plus **session record** (the
interview answers and drafting choices in §2–§3). It is not a **Designer ruling**. Nothing
in it advances any material toward Canonical status. The 8-step Promotion Rule has not
been run for anything described here, and nothing here is proposed for promotion.

**Author:** Claude Sonnet 5 (claude-sonnet-5)
**Created:** 2026-09-13
