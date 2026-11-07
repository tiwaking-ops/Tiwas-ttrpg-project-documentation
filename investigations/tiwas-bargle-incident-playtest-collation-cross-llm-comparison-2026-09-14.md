---
document:
  title: "Tiwas — The Bargle Incident: Cross-LLM Collation, Comparison, and Assessment of Three Playtest Executions"
  version: "1.0"
  status: "Advisory / Non-canonical. No DEC assigned. Collation, comparison, and assessment only; no ruling, no promotion, no registry action, no authority change."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-14"
  last_modified_date: "2026-09-14"
  compared_reports:
    - "tiwas-bargle-incident-playtest-results-claude-2026-09-13.md (Claude Sonnet 5, claude-sonnet-5)"
    - "tiwas-bargle-incident-playtest-execution-chatgpt-2026-09-13.md (GPT-5.6 Luna)"
    - "tiwas-bargle-incident-playtest-execution-report-2026-09-13.md (Grok 4.5, grok-4.5)"
  source_module: "tiwas-adventure-the-bargle-incident-2026-09-13.md"
---

# Tiwas — The Bargle Incident: Cross-LLM Collation, Comparison, and Assessment of Three Playtest Executions

**Prepared by (Author):** OpenCode — LLM name: `opencode`, LLM version: `big-pickle`
**Date:** 2026-09-14
**Document class:** Collation and cross-LLM comparison of three independent executions of the same 2026-09-13 playtest module. Advisory only. Not a ruling, not a proposal, not a canonical or non-canonical decision record.

---

## 0. Governance Statement

This document records the complete results of an OpenCode analysis session: an analyze / assess / compare / contrast pass over three independent LLM playtest executions of the same source module, **The Bargle Incident** (`tiwas-adventure-the-bargle-incident-2026-09-13.md`, v0.1, Advisory / Non-canonical, authored by Claude Sonnet 5).

This document:

- Assigns **no DEC number** and proposes none.
- Records **no ruling**. All findings are empirical observations from three independent simulation runs, not designer decisions.
- Requests **no registry action**. OpenCode should take no promotion, demotion, supersession, or authority-altering action on the basis of this document alone.
- Does **not** resolve any open corpus item, including the DEC-106 multi-action vs single-action question, the S-11 Margin-to-HP conversion boundary, R1's Findings 1–4, or the module correction flags listed in §8.
- Does **not** promote, demote, or alter the authority status of any of the three source reports or the source module, all of which remain Advisory / Non-canonical.
- Does **not** establish which LLM's execution choices are "correct" where they diverge — divergence is recorded as evidence for Tiwa's (human) review.

**Provenance note per `governance/provenance.md`:** this report was authored, assessed, and last-modified by the same model (OpenCode `big-pickle`) in a single pass. A single-model self-assessment is a weaker form of review than an independent second pass; it is recorded honestly as such and confers no authority.

---

## 1. Source Reports

| # | Executing LLM (self-declared) | Report title | File | Version | In-family status |
|---|---|---|---|---|---|
| R1 | Claude Sonnet 5 (`claude-sonnet-5`) | Executed Playtest Results | `investigations/tiwas-bargle-incident-playtest-results-claude-2026-09-13.md` | 0.1 | Advisory / Non-canonical, no DEC |
| R2 | GPT-5.6 Luna | Complete Playtest Execution Report | `investigations/tiwas-bargle-incident-playtest-execution-chatgpt-2026-09-13.md` | 0.1 | Advisory / Non-canonical, no DEC |
| R3 | Grok 4.5 (`grok-4.5`) | Playtest Execution Report | `investigations/tiwas-bargle-incident-playtest-execution-report-2026-09-13.md` | 1.0 | Execution record / Non-canonical, no DEC |

**Provenance observation.** R2's **filename** says `chatgpt` while its frontmatter `execution_llm.name` and `.version` both read "GPT-5.6 Luna". The filename and the self-declared provenance differ; the self-declared field is treated as authoritative here and the filename inconsistency is flagged in §8 for correction if desired.

**Execution method comparison:**

| Aspect | R1 (Claude) | R2 (GPT-5.6 Luna) | R3 (Grok 4.5) |
|---|---|---|---|
| Method | Dedicated engine `tiwas_bargle_playtest.py` + scenario runner `run_playtest.py` | Chat-based Python simulation | Python 3 `random.SystemRandom()` simulation script |
| RNG | `random.SystemRandom()` (fresh OS entropy) | Seeded (`20260913`), deterministic | `random.SystemRandom()` (fresh OS entropy) |
| Reproducible | No (different result each run; documented) | Yes (fixed seed) | No |
| Artifacts in repo | Yes: `*_rolls.csv`, `*_effects.csv`, `*_summary.json`, both `.py` files in `investigations/` | None beyond the report (all inline) | No — script and logs at external `/tmp`/`/home` paths flagged as not-in-repo |

---

## 2. Shared Baseline (All Three Runs, Verified Against the Module)

All three executions initialized the module's full 24-attribute stat blocks and confirmed the same derived statistics. No divergence was found in character construction.

| Character | HP | PE | MP | Speed | Key skills (start) | ROLE |
|---|---:|---:|---:|---:|---|---|
| Rowan (PC) | 615 | 170 | 549 | 166 | Attack 29 (T1), Defense 27 (T1), Perception 27 (T1), Stealth 30 | Tier-1 fresh PC, Leather Armor (`defense:armor`) |
| Aleena (Ally) | 566 | 159 | 624 | 133 | Smite 27 (T1), Defense 23 (T1), Devotion 32 (T1) | Ally NPC; Vestments deliberately lack `defense:armor` |
| Goblin (Creature) | 421 | 102 | 273 | 128 | Crude Attack 40 (T1 sig), Trip 46 (T2 sig), Defense 24 | Creature; signature full-Cap starts (DEC-086/087) |
| Bargle (Villain) | 452 | 105 | 680 | 124 | Bolt 66 (T2 sig), Defense 23 (T1), Beguile 27 | Creature; Robes deliberately lack `defense:armor` |

All three runs also used the same Speed-based turn order (Rowan 166 → Aleena 133 → Goblin 128 / Bargle 124, per DEC-095) and the S-1 / DEC-105 melee-exchange model.

---

## 3. Individual Report Assessments

### 3.1 R1 — Claude Sonnet 5: "Executed Playtest Results" (175 lines)

**What it is.** A results-focused empirical finding record with per-run aggregate statistics, three worked examples pulled from the actual run, and six structural findings. Heaviest use of actual artifacts (202 roll CSV, 63-exchange CSV, summary JSON).

**Scenario outcomes.** Scene 2: Goblin defeated, HP −6, Rowan 567/615 (6 rounds). Interlude: 8 intervals, Margin 43 ≥ target 40, healing convention HP = Margin total → Rowan 610. Scene 3: Bargle incapacitated, HP −11, Rowan 515/615, **Aleena 356/566 — survives** (15 rounds).

**What it exercised that the others did not.** The PC Advanced Skill branch **naturally occurred**: Rowan rolled exactly 100 on Attack (a 100-Fumble, auto-fail, qualifying Double) in Scene 2 Round 2, generating **Power Strike (Tier 2)** from a real roll; a later qualifying failed Double on Power Strike generated **Power Strike (Advanced), Tier 3** (DEC-012.4 cascade confirmed). Aleena gained **Smite (Advanced)** and **Iron Faith** under GM Fiat (DEC-130). Run aggregates: 202 Core Tests, 65 S-1 exchanges, 1 fumble, 15 qualifying failed Doubles, 5 Advanced Skills, 30 Overflow events, 8 net Wound records, 0 safety-cap hits.

**Notable empirical confirmations.** DEC-106 self-Overflow risk **manifested**: the Goblin, firing Trip + Crude Attack back-to-back per DEC-106(2)/(4), inflicted 78 points of self-Overflow HP damage on itself in Round 1 alone before landing any attack. DEC-103's "magnitude ≤ 0 → Effect fully negated" branch fired three times under ordinary play (two Rowan→Bargle, one Bargle→Rowan Wound declarations entirely negated by shred + de-escalation).

**Findings.** Six, all framed as "open questions for Tiwa," none resolved: (1) above-Cap via Wound shrinkage is unruled (Goblin Crude Attack ended `Cap 37, current 40`); (2) Wound location and Wound target-attribute are fully decoupled random processes, producing narratively odd but mechanically correct combinations; (3) Armor Bypass and its DEC-030 fallback resolved to the same formula — declaring Armor Bypass currently has **no observable mechanical consequence**; (4) ally-NPC Advanced-Skill eligibility rests entirely on GM Fiat with no corpus category for named player-adjacent NPCs; (5) repeated Advanced-Skill cascades function cleanly through two levels; (6) no runaway repeat-contest loop observed (one data point, not a proof).

**Assessment.** The highest-completion single run of the three: it is the only execution that reached the full intended PC-side Advanced-Skill → Tier-2 Effect → Wound chain naturally. Its modeling conventions (per-skill effect rotation, rng-resolved "player chooses," auto-clearing Prone, tag-simplified Armor Bypass) are explicitly declared as conventions, not rulings. Two numeric items require verification (§8).

### 3.2 R2 — GPT-5.6 Luna: "Complete Playtest Execution Report" (787 lines)

**What it is.** The most detailed and structurally explicit report (18 sections): full per-round tables for both combats, explicit coverage matrix with PASS / PARTIAL / NOT EXERCISED, an explicit worked-examples-vs-actual divergence table, execution limitations, and a recommended repository classification.

**Method.** Deterministic seeded run (seed 20260913). Scene 1 Perception **13 → success** (so no Failure XP, no cascade — the module's teaching path was not entered). Scene 2: 5 rounds, Goblin −94; Rowan Attack advanced 29 → 34 but **no qualifying failed Double ever occurred**; therefore Power Strike was not created. The module's PC Advanced-Skill branch is treated as a **worked example, not a result of this run**. A second Bargle combat used Bargle's pre-authored Tier-2 Bolt to exercise the Tier-2 Wound pathway on Aleena.

**Scene 3.** 10 rounds; Bargle −16; Rowan 530; Aleena 256 (lowest of the three — sustained repeated Tier-3 Wounds and Injuries from Bolt). The two-track harm model was explicitly confirmed: Wounds changed attributes and derived MP without direct HP damage. Interlude: **not** executed for HP restoration — "Authoritative HP restoration: **Not executed**" because the fixed Margin-to-HP conversion is not defined (DEC-074); documented as an open-rule boundary rather than an execution error.

**Primary finding.** **Probabilistic coverage dependency**: a scenario whose downstream subsystem coverage depends on a random failed Double cannot guarantee that coverage in a single ordinary random run. Issue: **PARTIAL SYSTEM-COMPLETENESS PASS** — a playtest-coverage result, not a rules failure.

**Assessment.** Methodologically the most careful about the authority boundary and about not inventing rules: it refused to invent an HP conversion, refused to force a failed Double, and explicitly distinguishes natural gameplay execution from deterministic subsystem-coverage execution. Its major non-result (no PC Advanced Skill) is an absence of a probabilistic event, not a mechanics failure.

### 3.3 R3 — Grok 4.5: "Playtest Execution Report" (232 lines)

**What it is.** An execution report with selected exchange highlights, an extensive DEC-mapped coverage assessment vs the module checklist, five observations, four follow-up recommendations, and a clearly stated ruleset applied (Canonical v1.4 + Decision Register through DEC-135.A).

**Scenario.** Scene 1 Perception **60 → fail** (the module's worked-example path direction): Failure XP 33, cascade to Perception 28, remainder to General XP. Scene 2: Goblin −45; Trip twice applied Tier-3 Prone to Rowan; standing free/bundled per DEC-082; **no failed Double** on Rowan's Attack → no PC Advanced Skill (flagged as legitimate live-roll divergence). Interlude: Extended Test executed, GM target 40; on completion GM discretion restored **80 HP** to Rowan (proportionate, non-formulaic). Scene 3: Bargle −13; Rowan 548; Aleena 462 with **residual Prone**; **Armor Bypass no-match fail-and-fall-back path explicitly exercised** (DEC-114 R2 / DEC-030); Aleena gained **Iron Faith (Tier 2, Start 1)** via a failed Double Defense under GM Fiat (DEC-130).

**Wound production.** In this live run random Effect selection favored **Inflict Injury** over Impose Condition: Wounded; **zero Wound records** were written on Bargle or Aleena, while the Tier-2 production gate and record schema remained available. R3 calls this a "legitimate divergence from the module's sample path (which forced Wound declarations for teaching)."

**Observations/design flags.** (1) Live-roll divergence from worked examples is expected; (2) attack-spam / Effect-selection bias: with Effect choice free (DEC-025) and Injury always available, random or value-maximizing selection under-exercises location-referencing Effects — consistent with prior Mirror-Match observations; (3) HP pools 400–600 vs Margin damage 10–40 → multi-round fights are the norm, no "bloodied" threshold exists; (4) ally Advanced Skill via DEC-130 bounded fiat is consistent; (5) standing from Prone with free/bundled movement (DEC-082) worked as designed.

**Assessment.** Broad DELIVERED coverage with explicit handling of the module's flagged gaps. Its unwillingness to write Wounds when the random Effect mix did not produce them keeps it honest to DEC-025 but means Wound-record mechanics (R1's most productive area) went largely unexercised on the NPC side. Non-reproducible (external script/log paths not in repo).

---

## 4. Execution Divergences

These divergences are the primary reason the three reports' numerical outcomes are not directly comparable.

### 4.1 Action economy (most consequential — cross-LLM reversal vs Mirror-Match cycle)

| Report | Creature action economy | Consequence |
|---|---|---|
| **R1 (Claude)** | **Multi-action per DEC-106(2)/(4)** — Goblin fires Trip then Crude Attack back-to-back on its own turn | Self-Overflow cascade (78 HP self-damage in Round 1); more exchanges per round |
| **R2 (Luna)** | **Single action** per turn (one exchange per actor) | One exchange per round per actor |
| **R3 (Grok)** | **Single action** per turn | One exchange per round per actor |

**Significance.** In the 2026-09-11 Mirror-Match cycle, **Luna** was the multi-action run and Claude/Grok the single-action runs. Here the alignment is **reversed**: Claude (R1) uses DEC-106 multi-action while Luna (R2) and Grok (R3) use single action. The same DEC-106 interpretation question recurs across both playtest cycles and remains unresolved. It materially affects exchange volume, Overflow frequency, Combat-duration, and skill-progression speed.

### 4.2 Scene 1 — Perception Test

| Report | Roll | Outcome | Domain charged | Failure XP |
|---|---|---:|---|---:|
| R1 | Not reported (run begins at Scene 2) | — | — | — |
| R2 | 13 | Success (no Failure XP, no cascade) | MP | — |
| R3 | 60 | Fail | MP | 33 → Perception 28, remainder → General XP |
| Module worked example | 45 | Fail | **PE (45)** | 18 (no cascade) |

R2 and R3 both charged **MP** for the mss (Perception) test, which is the correct domain per DEC-007/DEC-003 (Mind-domain skill → MP). The **module's worked example charges PE** — a module correction flag already raised in the prior OpenCode storage assessment (commit `5132c07`); the executions align with the rules, not the module example.

### 4.3 S-11 Healing — three different operationalizations of the same open boundary

| Report | Treatment | Restoration | Status |
|---|---|---|---|
| R1 | Scripting convention: HP restored = accumulated Margin total | 43 HP (Rowan 567 → 610) | Executed, convention declared as not a ruling |
| R2 | Refused to invent a fixed conversion (DEC-074 GM discretion) | None — "Not executed" | Reviewed only |
| R3 | GM-discretion proportional restore on completion | 80 HP | Executed, non-formulaic |

All three respect DEC-074's "no fixed HP-deficit lock" boundary; none closed it. The divergence is in how an unattended simulation operationalizes a GM-discretion call.

### 4.4 Scene 3 — Bargle's Ambuscade

| Report | Rounds | Bargle final HP | Rowan final | Aleena final | Wounds on Aleena | Notes |
|---|---:|---:|---:|---:|---|---|
| R1 | 15 | −11 | 515 | 356 | 2 × Tier-3 (Head, Legs; both mpp) | PC-side Wound path exercised; 3 Wound declarations fully negated by DEC-103; 5 Armor Bypass declarations |
| R2 | 10 | −16 | 530 | 256 | Multiple Tier-3 (attribute wounds, no direct HP) | Two-track harm demonstrated; no Armor Bypass exercised |
| R3 | unlogged count | −13 | 548 | 462 (residual Prone) | Zero Wound records written | Armor Bypass no-match path exercised; random Effect mix favored Injury |

Final-HP spread (Aleena 256–462, Rowan 515–548, Bargle −11 to −16, Goblin −6 to −94) is the aggregate fingerprint of the §4.1–4.3 divergences plus pure roll variance.

### 4.5 Coverage of specific mechanics

| Mechanic | R1 | R2 | R3 |
|---|---|---|---|
| PC Advanced Skill creation (failed Double) | **Naturally exercised** (Power Strike, + 2 more) | NOT EXERCISED (no failed Double) | NOT EXERCISED (no failed Double on Attack) |
| Wound record production | 8 net records, PC + creature | Creature-side only (Bolt → Aleena) | Zero records (gate available, not selected) |
| Armor Bypass | 5 declarations resolved (both match & fallback), indistinguishable from Injury (Finding 3) | Not exercised | No-match fallback path exercised |
| Overflow → HP | 30 events; DEC-106 self-Overflow confirmed | None naturally triggered | Exercised (marked PASS) |
| DEC-103 full Effect negation | 3 observations | Not reported | Not reported |
| Scene 1 teaching path | Not run/reported | Not entered (success) | Entered (failure + cascade) |

---

## 5. Quantitative Comparison

### 5.1 Scenario outcomes

| Scenario | Module worked example | R1 (Claude) | R2 (Luna) | R3 (Grok) |
|---|---|---|---|---|
| Scene 1 Perception | 45 → fail, PE 45 | (not reported) | 13 → success | 60 → fail, MP 60 |
| Scene 2 Goblin | Injury path; ended by narration | 6 rds, Goblin −6, Rowan 567 | 5 rds, Goblin −94 | Goblin −45 |
| Interlude healing | Margin 51 ≥ 40, GM restore | 8 int, Margin 43, HP=43 → 610 | Reviewed, not executed | Executed, GM restore 80 HP |
| Scene 3 Bargle | Power Strike Wound + closing | 15 rds, Bargle −11, Rowan 515, Aleena 356 | 10 rds, Bargle −16, Rowan 530, Aleena 256 | Bargle −13, Rowan 548, Aleena 462 |
| Aleena outcome | Survives at reduced HP, one Wound | Survives (356), two Wounds | Survives (256), multiple Wounds | Survives (462), no Wounds, residual Prone |
| Rowan Advanced Skill | Power Strike (worked example only) | Power Strike (real 100-Fumble) + 2 more | None | None |

### 5.2 Final states

| Combatant | R1 (Claude) | R2 (Luna) | R3 (Grok) |
|---|---:|---:|---:|
| Rowan HP | 515 / 615 | 530 | 548 / 615 |
| Rowan Attack Skill | 29 → 31 (cascade) + Power Strike 41 (T2) | 29 → 34 | 29 → 34 |
| Rowan Defense Skill | → 34 | 27 → 30 | 27 → 34 |
| Aleena HP | 356 / 566 | 256 | 462 / 566 |
| Aleena Smite | → 34 (+ Smite Advanced) | 27 → 32 | 27 → 36 |
| Aleena Advanced Skills | Smite (Advanced), Iron Faith | none | Iron Faith (T2, Start 1) |
| Goblin HP | −6 | −94 | −45 |
| Bargle HP | −11 | −16 | −13 |

**Agreement on skill-growth direction:** Rowan Attack climbs 29 → 31/34/34 across all three runs; Defense climbs in all three; Aleena Smite climbs in all three. Only R1 additionally produced record-eligible Advanced Skills on the PC and multi-level cascade.

---

## 6. Convergent Findings (All Three Reports Agree or Jointly Confirm)

1. **The module executes as a functional Tiwas systems playtest** in all three independent runs. Core Test, resource cost = roll, Failure XP, S-1 contests, contest-delta Injury, Skill-Tier shred, Speed turn order, forced incapacitation (DEC-052), and negative-HP persistence (DEC-108) are exercised and functional in every run.
2. **The narrative requirement is met in every run: Aleena survives.** She takes real, mechanically-resolved harm (256–462 HP final; Wounds/Injuries in R1/R2) but never dies. The module's revision intent (Aleena survives, vs. the 1983 original) is robust to all three executions.
3. **Both enemies are forcibly incapacitated, never rule-inferred killed:** Goblin and Bargle reach HP ≤ 0 with persisted negative HP in all three runs; no report applies DEC-054 voluntary-death.
4. **The Trip → Tier-3 Prone chain fired in every run:** Goblin's Tier-2 Trip vs Rowan's Tier-1 Defense produces the Skill-Tier shred (mag 2 → 3) exactly as the module's worked example teaches.
5. **Two-track harm independence is confirmed wherever it was reached (R1, R2):** a Wound changes an attribute and derived statistics without itself causing direct HP loss (module GM Tutorial Note validated).
6. **The PC/creature Advanced-Skill asymmetry was respected in all runs:** creatures gained no failed-Double Advanced Skills; only players/player-adjacent (fiat) NPCs did.
7. **No report inferred a DEC, amended a rule, or self-promoted.** All three maintain Advisory / Non-canonical status and state no DEC is assigned or requested.
8. **The S-11 fixed Margin-to-HP conversion remains open** in all three reports; none closed it, and each explicitly treats its restore value as a convention or GM-discretion call, not a ruling.
9. **The HP = 0 boundary and the absence of an intermediate ("bloodied") threshold were respected** in all three runs; no report invented one.
10. **Speed-based turn order was stable and identical** (DEC-095) in all three runs.

---

## 7. Divergent Findings Requiring Tiwa Resolution (Human Escalation)

These are open items the corpus does not settle. OpenCode stops here and records them for human direction rather than selecting an interpretation.

1. **Action economy: multi-action (DEC-106) vs single-action.** R1 applied DEC-106(2)/(4) multi-action for the creature; R2/R3 used one action per turn. This is the same unresolved question surfaced in the Mirror-Match cycle (§8.1 of the 2026-09-11 collation), now with the author-LLM alignment reversed. Impact: exchange volume, Overflow frequency, combat duration, and effect mix all change with this choice.
2. **PC Advanced-Skill coverage strategy.** R1 shows the failed-Double branch **can** occur naturally in a single run; R2 (primary finding) and R3 (recommendation 3) show it is **not guaranteed** by any ordinary random run. Tiwa must decide whether future playtests accept probabilistic coverage or add an explicit "force one failed Double on a designated skill by round N" scaffold.
3. **S-11 automated-playtest HP conversion.** R1 (HP = Margin total), R3 (GM-discretion 80 HP), R2 (abstention) are three operationalizations of the same DEC-074 boundary. Tiwa should either fix a conversion for unattended playtests or accept that healing results are non-comparable across unattended runs.
4. **Above-Cap via Wound (R1 Finding 1).** Whether an Attribute Wound must retroactively clamp a Skill that now exceeds its shrunken Cap, or "above-Cap via Wound" is an acceptable unruled-but-not-prohibited state.
5. **Wound location / target-attribute decoupling (R1 Finding 2).** Whether the corpus should tie fictional hit location to the wounded attribute, or accept the current fully-independent random composition.
6. **Armor Bypass numerical indistinguishability (R1 Finding 3).** Declaring Armor Bypass currently has no observable mechanical consequence distinct from plain Injury on either resolution path. This looks like a genuine gap in S-5 (Armor) rather than a scripting artifact, and blocks meaningfully testable end-to-end Armor Bypass.
7. **Ally-NPC Advanced-Skill eligibility (R1 Finding 4).** The corpus has no named third category between "Player Character" (Advanced Skills from failed Doubles) and "creature" (pre-authored only, DEC-087) for significant named player-adjacent NPCs; eligibility currently rests entirely on DEC-130 GM Fiat.
8. **Effect-selection bias in automated runs (R3 §6.2).** Unguided selection under DEC-025 favors plain Inflict Injury and under-exercises Wound/Trip/Disarm. Whether to add least-used-Effect scaffolding for automated completeness runs without violating DEC-025.

---

## 8. Points of Factual Discrepancy and Artifact-Quality Observations

1. **Power Strike Cap: R1 reports 59; the module computes 55.** R1 and its summary JSON record `Power Strike (bpp+bps, Tier 2, Cap 59)`; the module's worked example computes `Cap = floor((58+52)/2) = 55` for the same formula. Unexplained arithmetic divergence — flagged for verification, not resolved here.
2. **R1 summary JSON `initial_state` snapshot anomaly.** The `initial_state` objects in `tiwas_bargle_playtest_summary.json` carry post-run `wounds` and `advanced_skills_created` (e.g., Rowan's initial state lists Power Strike and a Legs Wound). This appears to be a shared-object/dict-reference artifact of the engine rather than a true pre-run snapshot. The `.md` frontmatter and `totals` block are internally consistent with the JSON totals (202/65/1/15/5/30/8), so the aggregate claims corroborate; only the `initial_state` field semantics look wrong.
3. **R2 filename vs provenance.** Filename says `chatgpt`; frontmatter `execution_llm` says GPT-5.6 Luna in both name and version. Cosmetic inconsistency, no substance.
4. **R1 interlude wording.** "Rowan healed 615→610 after clamping" is internally confusing: he started that phase at 567 and gained 43 → 610, which is below max 615 (no clamp engaged). JSON records gain 43, after 610 — the .md wording is loose, the numbers are consistent.
5. **R3 §4.4 internal wording tension.** "Wounded on several Tier-2 wins" appears alongside "Zero Wound records were written on Bargle or Aleena." Net reading: the Tier-2 production gate fired but the random declared-Effect mix selected Injury, so no record was written. Recommend tightening wording; no factual conflict once read in full.
6. **R3 artifact reproducibility.** Script/logs live at external `/tmp` and `/home` paths; the report's HP transitions are not all derivable from the shown rows, and Aleena's residual Prone source is not documented in-family. These were already flagged in the prior OpenCode storage assessment (commit `5132c07`).
7. **Module Scene 1 domain error (module-side).** The module's worked example charges PE (45) for a Perception (mss, Mind-domain) test; DEC-007/DEC-003 route Mind-domain skills to MP. R2/R3 charged MP. The module's example, not the executions, is the anomaly (previously flagged in commit `5132c07`).
8. **Module 'cosmetic' bps Wound oversight (module-side).** The module calls Bargle's bps Wound "cosmetic," but a Body-attribute Wound steps down derived HP (Σ Body) — Bargle HP falls 452 → 449 per DEC-102(5)/DEC-004 live recalculation. Already flagged in commit `5132c07`; none of the three execution reports relied on the cosmetic claim.
9. **Above-Cap instances (extends R1 Finding 1).** The JSON final state shows the same unruled above-Cap state twice on the Goblin: Crude Attack `Cap 37, current 40` (flagged by R1) and Trip `Cap 45, current 46` (not separately flagged). Both stem from Cap shrinkage under Body-attribute Wounds.

---

## 9. Coverage Comparison vs the Module's GM Coverage Checklist

| Mechanic | DEC(s) | R1 (Claude) | R2 (Luna) | R3 (Grok) |
|---|---|---|---|---|
| Core Test, Cost=Roll, Overflow→HP | 006/007 | Exercised (30 overflows) | Exercised (no Overflow triggered) | Exercised |
| 100-Fumble | 001 | Exercised (1 real, PC) | Path not triggered | Path available, not triggered |
| Failure XP + Skill Roll Pool cascade | 009/010 | Exercised | Exercised | Exercised |
| Advanced Skill creation (both Start options) | 012 | Exercised (rolled PC + flat-1 ally) | NOT EXERCISED | Ally path (flat 1) only |
| Recovery + clamping | 008 | Exercised | Exercised | Exercised |
| S-1 opposed contest / melee exchange | 013/105 | Exercised (65 exchanges) | Exercised | Exercised |
| Contest-delta Inflict Injury | 096/097/104 | Exercised (primary damage path) | Exercised | Exercised |
| Skill-Tier shred + de-escalation | 103 | Exercised (incl. 3 full negations) | Exercised | Exercised |
| Zero-Step Location Index | 014 | Exercised | Exercised | Exercised |
| Tier-1 quartiles + parity laterality | 100/041 | Exercised | Exercised | Exercised |
| Skill-Tier ≥ 2 production gate | 041 | Exercised | Exercised | Exercised |
| Wound record + DEC-102 target selection | 035.A/102 | Exercised (PC + creature) | Creature-side only | Path available, not selected |
| Live attribute recalculation | 004 | Exercised | Exercised | Path available |
| Conditions (Prone) | 079/122–125 | Exercised | Exercised (2× Tier-3) | Exercised (2× Tier-3) |
| Tag+Location gating / fallback | 028/114/030 | Exercised (both match & fallback) | NOT EXERCISED | Exercised (no-match only) |
| GM Fiat (bounded universality) | 130 | Exercised (Aleena) | NOT EXERCISED | Exercised (Aleena Iron Faith) |
| S-11 as Extended Test | 071–074 | Exercised (convention restore) | Reviewed only | Exercised (GM restore) |
| Forced incapacitation HP=0 / negative HP | 052/108 | Exercised | Exercised | Exercised |
| Speed turn order | 095 | Exercised | Exercised | Exercised |
| Creature signature full-Cap start | 086/087 | Exercised | Exercised | Exercised |

**Module-flagged non-covered subsystems — respected by all three (not invented):** Active Defense as a distinct genuine Core Test (DEC-044), Reactions (DEC-132), Equipment damage/repair (DEC-118–129), Encumbrance (DEC-078), and full Armor Bypass against a Tag-matched armored target (DEC-136/137 deterministic address path). No run claims coverage of these; the 2026-09-11 human-templated Mirror-Combat v2 cycle is the current home of the full-depth Armor Bypass exercise, not this module.

---

## 10. Assessment Summary

| Report | Self-assessment | Coverage character | OpenCode assessment |
|---|---|---|---|
| R1 (Claude) | No explicit label; narrative requirement confirmed; 6 findings | Highest single-run completeness: full PC Advanced-Skill → Tier-2 → Wound chain, Overflows, DEC-103 negation, both Armor Bypass paths | Most mechanically informative run; numeric Cap/55-vs-59 and JSON snapshot items to verify; conventions are declared and plausible |
| R2 (Luna) | **PARTIAL SYSTEM-COMPLETENESS PASS** | Most methodologically disciplined; explicitly refuses to force or invent; full per-round logs; explicit coverage matrix | Best-formalized authority handling and the clearest statement of the probabilistic-coverage dependency — the primary cross-run finding |
| R3 (Grok) | Implicit (broad coverage; recommendations) | Explicit DEC mapping vs module checklist; exercises Armor Bypass no-match and GM-Fiat ally Advancement; zero Wounds (Effect bias) | Reliable and well-scoped; weakest on Wound-record evidence; external artifact paths limit reproducibility |

**Cross-run verdict.** The three executions jointly validate the module as a genuine Tiwas systems exercise and independently confirm the same convergent behaviors (§6). Their numeric outcomes are not directly comparable because of §4's divergences — above all the multi-action (R1) vs single-action (R2/R3) reading of DEC-106, which reverses the prior Mirror-Match alignment. **No run uncovered a rules contradiction; no run supports a DEC; no promotion is warranted.**

---

## 11. Recommended Next Steps (Advisory Only)

1. **Resolve the DEC-106 action-economy question (§7.1) before any follow-on playtest uses these results as a baseline.** It recurs across the Mirror-Match and Bargle cycles with reversed author alignment — a strong signal it needs a ruling, not more stored executions.
2. **Decide the PC Advanced-Skill coverage strategy (§7.2):** accept probabilistic coverage (R2) or adopt a force-one-failed-Double scaffold for completeness runs (R3 rec 3). R1 demonstrates the natural branch is reachable; it is just not guaranteed.
3. **Fix a playtest-only S-11 HP conversion for unattended runs (§7.3), or explicitly exclude healed HP from cross-run healing comparisons.**
4. **Give R1 Finding 3 (Armor Bypass numerically indistinguishable from Injury) a dedicated ruling**; it is the clearest candidate "real gap in S-5" surfaced by this cycle.
5. **Verify the Power Strike Cap discrepancy (55 vs 59, §8.1)** against the engine's attribute data before any downstream implementer uses R1's skill record.
6. **Consider a least-used-Effect scaffolding option (R3 rec 2)** for automated completeness runs, contingent on Tiwa's answer to §7.8, so Wound/Trip/Disarm fire at measurable rates without violating DEC-025.
7. **Treat each execution record as its own provenance**: do not merge R1/R2/R3 numerical results into a single canonical "playtest result"; any cross-execution reconciliation must preserve each run's distinct RNG, engine, and convention provenance.

---

## 12. Artifact Inventory

| Artifact | Location | Author | Status |
|---|---|---|---|
| Adventure module (source) | `investigations/tiwas-adventure-the-bargle-incident-2026-09-13.md` | Claude Sonnet 5 | Stored |
| R1 results doc | `investigations/tiwas-bargle-incident-playtest-results-claude-2026-09-13.md` | Claude Sonnet 5 | Untracked in git |
| R2 execution report | `investigations/tiwas-bargle-incident-playtest-execution-chatgpt-2026-09-13.md` | GPT-5.6 Luna | Untracked in git |
| R3 execution report | `investigations/tiwas-bargle-incident-playtest-execution-report-2026-09-13.md` | Grok 4.5 | Stored (commit `5132c07`) |
| R1 engine | `investigations/tiwas_bargle_playtest.py` | Claude Sonnet 5 | Untracked in git |
| R1 scenario runner | `investigations/run_playtest.py` | Claude Sonnet 5 | Untracked in git |
| R1 roll CSV (202 rows) | `investigations/tiwas_bargle_playtest_rolls.csv` | Claude Sonnet 5 | Untracked in git |
| R1 effects CSV (63 rows) | `investigations/tiwas_bargle_playtest_effects.csv` | Claude Sonnet 5 | Untracked in git |
| R1 summary JSON | `investigations/tiwas_bargle_playtest_summary.json` | Claude Sonnet 5 | Untracked in git |
| R3 script/logs | `/tmp` / `/home` (external, not in-repo) | Grok 4.5 | Not staged |
| **This document** | `investigations/tiwas-bargle-incident-playtest-collation-cross-llm-comparison-2026-09-14.md` | OpenCode | New |

---

## 13. OpenCode Action Boundary

OpenCode should:

1. Store this report as an **advisory / non-canonical investigation artifact** (D4/D5 evidentiary work product), distinct from any LLM execution record.
2. Preserve each execution's actual recorded results; do **not** rewrite any of the three reports to match the others or the module's worked examples.
3. Do **not** infer, assign, or request a DEC from this comparison.
4. Do **not** promote or demote any of the three reports, the module, or this comparison.
5. Keep the three execution records separate provenance units; reconcile discrepancies explicitly (as done in §8) rather than silently merging.
6. Route §7's unresolved items to Tiwa for human ruling before any of them is acted on.

---

**End of report.**

**Author:** OpenCode — LLM name: `opencode`, LLM version: `big-pickle`
**Date:** 2026-09-14
**Classification:** Collation / Comparison / Assessment — Advisory / Non-canonical, No DEC assigned