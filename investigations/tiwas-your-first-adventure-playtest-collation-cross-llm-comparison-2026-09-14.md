---
document:
  title: "Tiwas — Your First Adventure: Cross-LLM Collation, Comparison, and Assessment of Playtest Executions (GPT-5.6 Luna, Grok 4.5)"
  version: "2.0"
  status: "Advisory / Non-canonical. No DEC assigned. Collation, comparison, and assessment only; no ruling, no promotion, no registry action, no authority change."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-14"
  last_modified_date: "2026-09-14"
  compared_reports:
    - "tiwas-your-first-adventure-playtest-execution-gpt-5.6-luna-2026-09-14.md (GPT-5.6 Luna)"
    - "tiwas-your-first-adventure-playtest-execution-grok-4.5-2026-09-14.md (Grok 4.5)"
  source_module: "tiwas-adventure-your-first-adventure-2026-09-14.md"
  harness: "tiwas-your-first-adventure-playtest-harness-prompt-2026-09-14.md"
revision_note: >
  v2.0 (2026-09-14): records the disposition of the §7 open items by Tiwa rulings D1–D7 and
  DEC-140. §7 items now each carry their resolution status; the v0.1 run facts are preserved
  as delivered. D1 (Bargle HP≤0 pre-fork → Ending A immediately, fork skipped) closes §7.1;
  D3 (Zero-Step is canonical §14.1 verbatim; LI 30/LI 42 → Torso per DEC-100 quartiles) closes
  §7.2; D4 (exclusive one-Effect-per-win) closes §7.3; D2-final + DEC-140 (Universal DEC-012)
  close §7.4; D5 (budget-withdrawal = intended primary end) closes §7.5; D2/D6 (Scene-1
  Perception test mandatory, fixed roll 00 =100 teaching beat) close §7.6. Module and harness
  rewritten to v0.2 accordingly (D7); R1 (Claude
  Sonnet 5) remains outstanding (item 5 in §11). **Tiwa accepted module v0.2 and harness v0.2
  in-session, 2026-09-14; D7 review gate closed.**
---

# Tiwas — Your First Adventure: Cross-LLM Collation, Comparison, and Assessment of Playtest Executions

**Prepared by (Author):** OpenCode — LLM name: `opencode`, LLM version: `big-pickle`
**Date:** 2026-09-14
**Document class:** Collation and cross-LLM comparison of the delivered playtest executions of the 2026-09-14 "Your First Adventure" module. Advisory only. Not a ruling, not a proposal, not a canonical or non-canonical decision record.

---

## 0. Governance Statement

This document records the complete results of an OpenCode analysis session: an analyze / assess / compare / contrast pass over the delivered LLM playtest executions of the source module **Your First Adventure** (`tiwas-adventure-your-first-adventure-2026-09-14.md`, v0.1, Advisory / Non-canonical, authored by OpenCode) run under the associated harness prompt (`tiwas-your-first-adventure-playtest-harness-prompt-2026-09-14.md`).

This document:

- Assigns **no DEC number** and proposes none.
- Records **no ruling**. All findings are empirical observations from independent simulation runs, not designer decisions.
- Requests **no registry action**. OpenCode should take no promotion, demotion, supersession, or authority-altering action on the basis of this document alone.
- Does **not** resolve any open corpus item **by itself**. The §7 items were escalated to Tiwa and are now resolved by human rulings D1–D7 and DEC-140 (see §7 disposition markers and `_consolidation/decision-register.md`). This document records those dispositions; it confers no authority on them.
- Does **not** promote, demote, or alter the authority status of any source report or the source module, all of which remain Advisory / Non-canonical.
- Does **not** establish which executing model's choices are "correct" where they diverge; divergence is recorded as evidence for Tiwa's (human) review.

**Provenance note per `governance/provenance.md`:** this report was authored, assessed, and last-modified by the same model (OpenCode `big-pickle`) in a single pass. A single-model self-assessment is a weaker form of review than an independent second pass; it is recorded honestly as such and confers no authority.

**Run-pair note.** The harness scheduled R1 = Claude Sonnet 5, R2 = GPT-5.6 Luna, R3 = Grok 4.5 (§1 of `tiwas-your-first-adventure-playtest-harness-prompt-2026-09-14.md`). **No R1 (Claude Sonnet 5) report was delivered** in this batch; only R2 (Luna) and R3 (Grok) reports were available for assessment. The R1 report is not assessed here and is recorded as outstanding.

---

## 1. Source Reports

| # | Executing LLM (self-declared) | Report title | File (in-repo copy) | Version | In-family status |
|---|---|---|---|---|---|
| R2 | GPT-5.6 Luna (`5.6`) | Tiwas — Adventure Module: Your First Adventure, Unattended Multi-LLM Playtest Execution Report | `investigations/tiwas-your-first-adventure-playtest-execution-gpt-5.6-luna-2026-09-14.md` | 0.1 | Advisory / Non-canonical; **certification BLOCKED**, no DEC |
| R3 | Grok 4.5 (`grok-4.5`) | Tiwas — Your First Adventure: Playtest Execution Report | `investigations/tiwas-your-first-adventure-playtest-execution-grok-4.5-2026-09-14.md` | 1.0 | Execution record / Advisory-non-canonical, no DEC |
| R1 | Claude Sonnet 5 | (expected per harness) | `investigations/tiwas-your-first-adventure-playtest-execution-claude-2026-09-14.md` | — | **Not delivered** |

**Provenance / placement observations.**

1. Harness contract file names were `...-execution-luna-2026-09-14.md` and `...-execution-grok-2026-09-14.md`; delivered/received names are `...-execution-gpt-5.6-luna-2026-09-14.md` and `...-execution-grok-4.5-2026-09-14.md`. Cosmetic deviation from the contract naming; no substantive conflict (self-declared provenance fields are authoritative).
2. Grok's report §9 states its delivery path as `artifacts/tiwas-your-first-adventure-playtest-execution-grok-4.5-2026-09-14.md`; the file was received at the repository root and a copy is stored in `investigations/`. Placement path inconsistency — flagged in §8.
3. Both reports still physically exist at the repository root as well as in `investigations/` (root copies retained in the user's working tree; the `investigations/` copies are the stored in-repo copies referenced here).

**Execution method comparison:**

| Aspect | R2 (GPT-5.6 Luna) | R3 (Grok 4.5) |
|---|---|---|
| Method | Chat-based simulation with full d100 roll ledger | Python 3 `random.SystemRandom()` simulation script |
| RNG | `random.SystemRandom()` (fresh entropy) | `random.SystemRandom()` (fresh entropy) |
| Reproducible | No | No (external script/log at `/tmp/...`; not in repo) |
| Artifacts in repo | Report only (all rolls inline in 121-row Appendix ledger) | Report only; script + 560-line log at `/tmp` external paths flagged in report |
| Certification | **BLOCKED** (ending contradiction at terminal Bargle HP) | Completed; Ending A selected |

---

## 2. Shared Baseline (Both Runs, Verified Against the Module)

Both executions initialized the module's full 24-attribute stat blocks and confirmed the same derived statistics. No divergence was found in character construction.

| Character | HP | PE | MP | Speed | Key skills (start) | ROLE |
|---|---:|---:|---:|---:|---|---|
| Rowan (PC) | 615 | 170 | 549 | 166 | Attack 29 (T1), Defense 27 (T1), Perception 27 (T1), Stealth 30, Composure 23 | Tier-1 fresh PC, Leather Armor; `reaction:vigilant` |
| Aleena (Ally) | 566 | 159 | 624 | 133 | Devotion 32 (T1), Smite 27 (T1), Defense 23 | Ally NPC; Vestments lack `defense:armor` |
| Goblin (Creature) | 421 | 102 | 273 | 128 | Crude Attack 40 (T1 sig), Trip 46 (T2 sig), Defense 24 | Creature; signature full-Cap starts (DEC-086/087) |
| Rattlesnake (Creature) | 417 | 71 | 243 | 173 | Venomous Bite 59 (T2 sig), Defense 29, Stealth 30 | Creature; acts first in Scene 2 |
| Ghoul (Creature) | 494 | 126 | 260 | 146 | Claw 39, Grapple 46, Defense 26, Desecration 22 | Pack-leader representative; no combat (turning beat) |
| Bargle (Villain) | 452 | 105 | 680 | 124 | Bolt 66 (T2 sig), Defense 23 (T1), Beguile 27 | Creature; Robes lack `defense:armor` |

Both runs adopted A1–A8 and the H-block conventions identically (per their adoption statements), including: single-exchange-per-combatant-per-round (A1), Speed-descending order (A2), bounded scene budgets `Scene1 ≤6 / Scene2 ≤5 / Scene4 ≤3 / Scene6 ≤3 + fork` (A3), Aleena-survives clamp-to-1 (A4), H1(a)/H2-40 healing (A5), probabilistic Advanced-Skill (A6, **no forced failed Double**), HP≤0 terminal / negative persists (A7, DEC-052/DEC-108), and module Effect rotation as scaffolding only (A8).

**A6 note for v2.0:** the above A1–A8 describe the v0.1 module the runs adopted. In module v0.2 (D2/D6/DEC-140), A6 is amended — the Scene-1 Perception teaching beat is now a **mandatory fixed-roll-00 beat** that deterministically creates an Advanced Skill; other scenes remain probabilistic. The run facts are unchanged; the convention text evolved.

---

## 3. Individual Report Assessments

### 3.1 R2 — GPT-5.6 Luna: "Unattended Multi-LLM Playtest Execution Report" (737 lines)

**What it is.** The most structurally explicit and best-logged report of the two: single full run with a **complete 121-row d100 Appendix ledger**, per-scene transaction tables (Cost / Overflow / Failure-XP / cascade / Recovery / resource), an explicit coverage matrix, an explicit module-correction compliance table, and a formal **certification: BLOCKED**.

**Scenario.** Scene 1: Goblin withdrew on **budget expiry at Round 6** (Rowan 575, Goblin 156); repeated Tier-3 Prone applied to Rowan and stood free. Scene 2: **Rattlesnake incapacitated at HP −34 in Round 3**; both treasure-search attempts failed (**no pearl**). Scene 3: all four healing intervals failed (margin 0 → restore 0). Scene 4: turning succeeded (Devotion 24 vs Desecration 38, margin 11–0), ghouls withdrew. Scene 5: all three bash attempts failed (86 / 32 / 94 vs effective 21/22/22) → forced open by exhaustion. Scene 6: `reaction:vigilant` fired exactly once (R1E4); Aleena took a Tier-2 Wound (`mps` 48→46, MP max 624→622); **Bargle reached HP −2 from an Overflow in Round 2**.

**Primary finding (F-01/F-02).** The harness mandate to resolve the climax fork **even when Bargle reaches HP≤0 in any Scene-6 round** fired; Bargle won Beguile 27 (roll 24) vs Composure 24 (roll 49) → **Ending B selected** — but Ending B requires Bargle to remain active and escape, which is mechanically impossible from a resolved, persisted HP −2 (A7 / DEC-052 / DEC-108). Luna **refused to invent a revival or escape** and declared the module **not certifiable end-to-end** under the supplied contract without a designer-authorized resolution.

**Assessment.** Methodologically the most careful about the authority boundary: it refused to manufacture a rule or an in-fiction workaround, recorded the contradiction, and stopped. Its decision to run the fork *despite* terminal HP — because the task contract explicitly said "or on Bargle HP≤0 in any round" — is faithful to the harness text; the same contract wording is what exposes the module/harness internal inconsistency (§7.1). Full roll ledger makes every d100 auditable. Weaknesses: the condensed Scene-6 rows do not independently reconcile to the −2 final state (possible multi-roll staging in the ledger; §8.1), and the Scene-3 restore rationale is loosely worded (§8.2).

### 3.2 R3 — Grok 4.5: "Playtest Execution Report" (230 lines)

**What it is.** A clean execution record with a corrective-compliant ruleset block, per-scene condensed exchange highlights, an explicit coverage matrix mapped to the module's GM Coverage Checklist, an explicit correction-compliance table, seven findings, and a three-line executive summary.

**Scenario.** Scene 1: Goblin withdrew on **budget expiry at Round 6** (HP 71 trajectory, heavy Goblin self-Overflow). Scene 2: **Snake withdrew on budget expiry at Round 5** (HP 66), 3× Body Wounds (`bss`/`bsp` Mag −2) on Rowan (HP 615→613→609); both treasure searches failed (**no pearl**). Scene 3: margin 19, clamped to current max (Rowan 609/609). Scene 4: turning success (margin 17), ghouls withdraw. Scene 5: three bash failures (effective 14) → forced open. Scene 6: `reaction:vigilant` exactly once; **Armor Bypass R3 no-match → Injury fallback (DEC-030) exercised**; Bargle still above 0 after Round 3 → climax fork: tie, then Composure **M13 vs M12 → ENDING A**; decisive Injury 23 → Bargle **197/452**, escapes wounded.

**Assessment.** Broad DELIVERED coverage with explicit, DEC-mapped honest gap reporting; the only delivered run that exercised the Armor-Bypass no-match fallback and completed to an ending. Its procedural choices (fork deferred until after Round 3 with Bargle alive) are consistent with the harness and sidestep the contradiction Luna hit — which is exactly why the contradiction is a *timing-dependent* exposure, not a universal one (§4.4). Weakness: script/log at external `/tmp` paths; Scene-1/Scene-6 HP trajectories are asserted rather than shown row-by-row (rolling mitigation: it flags its approximations honestly); mixed `-2`/`+2` Mag notation for the same Wound (8.3).

---

## 4. Execution Divergences

### 4.1 Action economy — convergent (resolved vs Bargle cycle)

| Report | Creature action economy | Consequence |
|---|---|---|
| R2 (Luna) | **Single exchange per combatant per round** (A1) | One exchange per actor per round |
| R3 (Grok) | **Single exchange per combatant per round** (A1) | One exchange per actor per round |

**Significance.** In the Bargle cycle the three runs split multi-action (Claude) vs single-action (Luna/Grok). Here **both delivered runs used A1 single-action** — the module's run conventions achieved cross-LLM convergence on the action economy that was the largest divergence source in the prior cycle.

### 4.2 Scene 2 — Rattlesnake termination and treasure

| Aspect | R2 (Luna) | R3 (Grok) |
|---|---|---|
| End condition | **Incapacitated HP −34** in Round 3 | **Budget expiry** at Round 5 (HP 66) |
| Wounds on Rowan | 1× Tier-2 (`bsp` 61→59; HP 615→613) | 3× Body (`bss`/`bsp` Mag −2; HP 615→613→609) |
| Treasure search | 2 attempts, both failed (no pearl) | 2 attempts, both failed (no pearl) |

Both end conditions are permitted by A3; only Luna actually exercised the creature **HP≤0/negative-HP** path on the snake. Both runs produced **no pearl** → the Ending-B pearl beat was unreachable in both.

### 4.3 Scene 1 — Perception teaching beat

**Convergent skip.** Neither delivered run executed a Scene-1 Perception test (Luna opens Scene 1 directly at the Attack exchange; Grok explicitly "perception default-skipped — the fight is the beat"). The module's teaching test was therefore not exercised in this run pair, unlike the Bargle cycle where Luna passed and Grok failed the analogous test.

### 4.4 Scene 6 — climax fork timing vs terminality (**most consequential divergence**)

| Report | Bargle state at fork | Fork trigger | Fork outcome | Ending | Certification |
|---|---|---|---|---|---|
| R2 (Luna) | **HP −2 (incapacitated, Overflow, R2)** | Harness "[D] on Bargle HP≤0 in any round" | Beguile 27 roll 24 (M3) vs Composure 24 roll 49 (fail) → **Bargle wins** | **Ending B** — escape impossible from −2 | **BLOCKED** |
| R3 (Grok) | **HP > 0** after Round 3 | Harness "[D] after Scene 6 R3" | Tie, then Composure M13 vs Beguile M12 → Composure holds | **Ending A** (Bargle escapes wounded, 197 HP) | Completed |

**Significance.** The two delivered runs exercised the *two different trigger clauses* of the same harness instruction `[D]`. Only when Bargle is already terminally incapacitated (Luna) does the module demand an Ending-B outcome that its own terminality rules (A7 / DEC-052 / DEC-108) make mechanically unreachable. Grok's path (Bargle alive → fork → Ending A) completes cleanly. The module/harness **is internally contradictory only on the "HP≤0 in any round plus Bargle-wins-the-fork" path** — a reachable-in-principle branch that the design must resolve explicitly (§7.1).

### 4.5 Scene 5 — bash effective skill base

| Report | Effective Skill used | Note |
|---|---|---|
| R2 (Luna) | current Attack (37/38) − 15 = 21/22/22 | Uses post-cascade current Attack |
| R3 (Grok) | Attack 29 − 15 = 14 | Asserts start Attack 29 for the gate; Attack 29→34 by final state |

Module text says "current Attack − 15." Luna used current; Grok's effective base is opaque as to whether 29 was current at Scene 5. Minor reconciliation flag (§8.4).

---

## 5. Quantitative Comparison

### 5.1 Scenario outcomes

| Scenario | Module worked example | R2 (Luna) | R3 (Grok) |
|---|---|---|---|
| Sc.1 Goblin | combat beat, budget 6 | R6 budget expiry; Rowan 575, Goblin 156 | R6 budget expiry; Goblin HP 71 |
| Sc.2 Snake | budget 5, snake first | R3 **HP −34 incapacitation**; **no pearl** | R5 budget expiry, snake HP 66; **no pearl** |
| Sc.3 Healing | H1(a)/H2-40 | 4 intervals all failed; margin 0 → restore 0 | Margin 19 → clamped at current max 609 |
| Sc.4 Ghouls | turning beat | Win (Devotion 24 vs 38), ghouls withdraw | Win (margin 17), ghouls withdraw |
| Sc.5 Door | passive gate 15 | 3/3 bash fail → forced open | 3/3 bash fail (effective 14) → forced open |
| Sc.6 Bargle + fork | fork after R3 | Bargle −2 (Overflow) in R2 → fork on HP≤0 → **Ending B → BLOCKED** | Bargle >0 after R3 → fork → **Ending A**; Bargle 197 |

### 5.2 Final states

| Combatant | R2 (Luna) | R3 (Grok) |
|---|---:|---:|
| Rowan HP | 575 / 613 | 609 / 609 |
| Rowan Wounds | Tier-2 `bsp` (current 59) | 3× Body `bss`/`bsp` Mag −2 |
| Aleena HP | 544 / 566 | 513 / 566 |
| Aleena Wounds | Tier-2 `mps` (MP max 624→622) | none |
| Bargle HP | **−2 / 452 (incapacitated, terminal)** | 197 / 452 (ends wounded, Ending A) |
| Snake | −34 / 417 (incapacitated) | 66 → withdrew |
| Goblin / Ghoul | withdrew / withdrew | withdrew / withdrew |
| Pearl | **not found** | **not found** |
| Ending | B (unreachable → certification blocked) | A |

**Shared features:** Aleena survives in both (A4 never required); both creatures/villain outcomes are budget-withdrawals, incap, or turning withdrawal — **no rule-inferred kills anywhere**; neither run found the pearl; neither run force-created an Advanced Skill.

---

## 6. Convergent Findings (Both Delivered Reports Agree or Jointly Confirm)

1. **The module executes as a functional Tiwas systems playtest** in both independent runs. Core Test / Cost=Roll / Overflow→HP (DEC-006/007), S-1 contests, contest-delta Injury, Failure XP cascades, Tier shred + de-escalation (DEC-103), Recovery + clamping, Speed turn order (DEC-095), forced incapacitation (DEC-052), and negative-HP persistence (DEC-108) are exercised and functional in every run.
2. **The narrative requirement is met in both runs: Aleena survives** (544/566 and 513/566; A4 clamp never triggered). The module's revision intent (vs. the 1983 original) is robust across this pair.
3. **`reaction:vigilant` was exercised exactly once in Scene 6 R1 in both runs** (DEC-132.B) — the module's "single exercise" constraint held.
4. **Module corrections from the prior cycle were honored in both runs:** Perception-test/treasure costs charged to **MP**; Body-attribute Wounds live-recalibrate HP downward (615→613→609); a "cosmetic" Wound claim appears nowhere; Mind-attribute Wound (`mps`) recalibrated Aleena's MP max (624→622) in Luna — the correction compliance is verified behavior, not module text.
5. **No forced Advanced Skill:** both runs left the failed-Double branch **unexercised** per A6 (probabilistic). Power Strike therefore remains unimplemented-by-absence in this pair.
6. **No pearl in either run:** both treasure-search attempts failed in both runs, so the Ending-B pearl beat was structurally unreachable in this pair.
7. **Attrition vs HP≤0:** budget-expiry withdrawals carried both primary creatures (and the Ghouls) in both runs; only Luna's snake actually reached HP≤0. The tutorial pacing leans on budget beats by design (open question, §7.5).
8. **No report inferred a DEC, amended a rule, edited module text, or self-promoted.** All maintain Advisory / Non-canonical status and state no DEC is assigned.
9. **No morale/surprise mechanics invented:** all withdrawals and the invisibility beat were narrated as plot beats only, per the module.
10. **Turn order and initiative were stable and identical** (Speed-descending; snake first in Scene 2) in both runs.

---

## 7. Divergent Findings Requiring Tiwa Resolution (Human Escalation)

These were open items the corpus did not settle. OpenCode stopped and recorded them for human
direction rather than selecting an interpretation. **All six were subsequently ruled by Tiwa
(2026-09-14) via D1–D7 / DEC-140; each item below carries its disposition. The v0.1 analysis
text is preserved as delivered.**

1. **Climax-fork vs terminality contradiction (module/harness internal).** ... **RESOLVED —
   D1:** reach HP≤0 in any Scene-6 round → Ending A immediately; the climax fork is **skipped**
   and no Beguile/Composure contest resolves. Module v0.2 A7/Scene-6 and harness v0.2 [D]
   implement this. The reachable-in-principle impossible branch is removed.
2. **Zero-Step exact function.** ... **RESOLVED — D3:** the function is **already canonical**
   (Canonical §14.1): exchange tens/units digits of the natural roll; `00` → `100` after
   exchange; 37→73, 10→1, 1→10, 100→100. The "exact function is undocumented" finding is
   **retracted**. **Zone correction:** the DEC-140 review re-applied DEC-100 quartiles —
   **LI 30 and LI 42 are Torso (26–50)**, not Arms; collation §5.2's Location rows and the
   earlier "Arms" labels for those rolls are corrected to **Torso**. Module v0.2 and harness
   v0.2 quote §14.1 verbatim. No new ruling needed.
3. **Effect exclusivity under A8 rotation.** ... **RESOLVED — D4:** exactly **one** declared
   Effect per winning exchange; the contest margin feeds that Effect's magnitude only; no
   sequential or compound multi-Effect path from a single win. Module v0.2 A8 and harness v0.2
   [C]11 implement this.
4. **PC/creature 100-Fumble and Advanced-Skill probabilism.** ... **RESOLVED — D2 (final) +
   DEC-140:** Advanced-Skill creation from an in-play qualifying failed Double (including a
   100-Fumble) is **universal** — creature and PC alike (Unconditional DEC-012; DEC-087 governs
   template authoring only). The v0.2 module makes the Scene-1 Perception test a **mandatory
   fixed-roll-00 teaching beat** (creates Perception Advanced T2 mss+mps cap50 Start 1),
   removing the probabilism dependency for the PC half; the creature half remains probabilistic
   (a Goblin-side worked example is provided, not forced).
5. **Budget-withdrawal pacing.** ... **RESOLVED — D5:** budget-expiry withdrawal is the
   **intended primary scene-end**; HP≤0 remains the secondary end. Module v0.2 A3/Scene-1 end
   conditions re-ordered to primary-withdrawal-first.
6. **Scene-1 Perception teaching beat not exercised.** ... **RESOLVED — D2/D6:** the module
   now **mandates** the Scene-1 Perception test (fixed roll 00, deterministic) and states it
   always resolves. Module v0.2 Scene-1 and harness v0.2 [B]6/[C]14 implement this.

---

## 8. Points of Factual Discrepancy and Artifact-Quality Observations

1. **R2 Scene-6 final HP reconciliation.** Luna's condensed Scene-6 table and terminal event (Bolt 44 → overflow 10 → HP −2) do not on their face reconcile to −2 from the shown row totals plus the reaction injury; the Appendix ledger contains multiple sequential rolls per exchange label (e.g., rows 98–107 for R2E1), suggesting staged multi-roll resolution not all shown in condensed rows. The certification conclusion is preserved either way (HP≤0 was reached pre-fork), but the exact arithmetic is partly asserted rather than fully derived. Flagged for verification, not adjudged wrong.
2. **R2 Scene-3 restore rationale wording.** "HP restore = 0 because Rowan was already at his then-current HP maximum of 613" reads oddly against accumulated Margin = 0 (and Rowan being at 575/613). The correct reason for restore 0 is Margin 0; the "already at maximum" phrasing is loose. Numbers are consistent; wording is not.
3. **R3 Mag sign inconsistency.** Reader friction: "Tier-3 Mag −2 after shred" (Scene 1, negative convention) vs "3× Body (bss/bsp Mag −2)" (final state, same −2) while the module worked example phrases magnitudes positively ("Mag 3"). Same underlying value, two sign conventions in one report. Recommend a single convention in the module/harness.
4. **R3 Scene-5 effective-skill base.** Report states "Attack 29 −15" while its own final skill growth shows 29→34; it is not stated whether 29 was current at Scene 5. Minor opacity; module text says "current Attack".
5. **Placement/path noise.** Harness contract filenames vs received filenames (§1 obs.1); Grok's self-stated `artifacts/` delivery path vs actual root → `investigations/` copy (§1 obs.2); root copies remain in the working tree alongside the `investigations/` copies (§1 obs.3). No content conflict; all cosmetic/placement.
6. **R1 (Claude Sonnet 5) report missing** from the delivered batch; the full three-run comparison planned by the harness cannot be completed until it is supplied.

---

## 9. Coverage Comparison vs the Module's GM Coverage Checklist

| Mechanic | DEC(s) | R2 (Luna) | R3 (Grok) |
|---|---|---|---|
| Core Test, Cost=Roll, Overflow→HP | 006/007 | PASS | PASS |
| 100-Fumble (universal) | 001/012/140 (DEC-140) | NOT EXERCISED in run (v0.1 module; probabilistic) | NOT EXERCISED in run (v0.1 module; probabilistic) |
| Failure XP + Skill Roll Pool cascade | 009/010 | PASS | PASS |
| Advanced Skill — deterministic (v0.2 module beat) | 012/140 | NOT EXERCISED in run; **compulsory in module v0.2** (Scene-1 fixed-roll-00 teaching beat) | NOT EXERCISED in run; **compulsory in module v0.2** |
| Advanced Skill — probabilistic | 012 | NOT EXERCISED | NOT EXERCISED |
| Recovery + clamping | 008 | PASS | PASS |
| S-1 opposed contest / melee exchange | 013/105 | PASS | PASS |
| Contest-delta Inflict Injury | 096/097/104 | PASS | PASS |
| Skill-Tier shred + de-escalation | 103 | PASS | PASS |
| Zero-Step Location Index + parity | 014/100/041 | PASS | PASS (approximation flagged) |
| Skill-Tier ≥2 production gate | 041 | PASS | PASS |
| Wound record + DEC-102 target selection | 035.A/102 | PASS | PASS |
| Live attribute recalculation (HP/MP) | 004 | PASS (615→613; 624→622) | PASS (615→613→609) |
| Conditions (Prone) | 079/122–125 | PASS | PASS |
| Reactions (single exercise) | 132/132.A/132.B | PASS (exactly once) | PASS (exactly once) |
| Tag+Location gating / fallback | 028/114/030 | NOT EXERCISED (S6 ended pre-R3) | PASS (no-match → Injury fallback) |
| Nonexistent morale/surprise | — | PASS | PASS |
| GM Fiat | 130 | NOT EXERCISED | NOT EXERCISED |
| S-11 Extended Test | 071–074 | PASS | PASS |
| Speed-based turn order | 095 | PASS | PASS |
| Creature signature full-Cap starts | 086/087 | PASS | PASS |

**Zero-Step in module v0.2 (D3):** now quoted verbatim from Canonical §14.1 (exchange tens/units
digits; `00`→`100`); both runs' ordinal-approximation note is retired — the function is
canonical and captured. The DEC-140 review corrected **LI 30 and LI 42 → Torso** per DEC-100
quartiles (26–50); module v0.2 examples conform (30→3, 22→22, 9→90).

**100-Fumble / Advanced-Skill in module v0.2 (D2-final/DEC-140):** the run-state cells above
record what the v0.1 module actually exercised; v0.2 changes the module to **mandatorily**
exercise the Advanced-Skill path via the Scene-1 fixed-roll-00 teaching beat (creates
Perception Advanced, cap50 Start 1), so a future v0.2 run would expect PASS on that row. The
creature-side half (Goblin worked example, not forced) remains probabilistic.

**Module-flagged non-covered subsystems — respected by both (not invented):** Active Defense as a distinct Core Test (DEC-044), Fatigue from repeated defenses (DEC-135), full Tag-matched Armor Bypass (DEC-136–139 — module deliberately falls back), Encumbrance, Equipment damage, ruled charm/poison/morale/surprise Effects. Grok explicitly declares these out of scope; Luna records them as NOT EXERCISED without inventing them.

---

## 10. Assessment Summary

| Report | Self-assessment | Coverage character | OpenCode assessment |
|---|---|---|---|
| R2 (Luna) | **Certification: BLOCKED** — honest stop at mechanically contradictory endpoint | Most complete logging (full 121-roll ledger); explicit correction-compliance table; explicit coverage matrix | Methodologically the strongest at the authority boundary: it surfaced a genuine module/harness contradiction and refused to fabricate a workaround. The BLOCKED result is the most valuable output of this run pair. |
| R3 (Grok) | Completed; Ending A; "execution and observation record" | Broad DELIVERED coverage; only run to exercise Armor-Bypass no-match fallback and complete an ending | Reliable, honest, well-scoped; reproduces the module's intended teach-check (no pearl, no forced Advanced Skill) and completes cleanly. External logs and a few asserted trajectories limit auditing. |

**Cross-run verdict.** The pair jointly validates the module as a genuine Tiwas systems exercise and confirms the same convergent behaviors (§6), including full correction compliance, the Aleena-survives invariant, exact-single Reaction exercise, and single-action convergence (A1) that resolves the prior cycle's largest divergence. Their outcomes diverge **only on the path where the harness forces the climax fork after Bargle is already terminally incapacitated — a timing-dependent exposure of an internal module/harness contradiction (R2 F-01/F-02)**. **R2's BLOCKED certification is correct and is the primary finding of this cycle; no run uncovers a Canonical-rules contradiction; no run supports a DEC; no promotion is warranted.**

---

## 11. Recommended Next Steps (Advisory Only)

1. **DONE — Tiwa resolved the ≤7 section via D1–D7 / DEC-140 (2026-09-14).** D1 closes the climax-fork/terminality contradiction (§7.1); D3 closes the Zero-Step mapping question (§7.2); D4 closes Effect exclusivity (§7.3); D2-final + DEC-140 close the PC/creature 100-Fumble question (§7.4); D5 confirms budget-withdrawal pacing (§7.5); D2/D6 make the Scene-1 Perception beat mandatory (§7.6).
2. **DONE — Zero-Step documented (D3):** verbatim Canonical §14.1 in module v0.2 and harness v0.2; the cross-LLM approximation gap is retired.
3. **DONE — Advanced-Skill/100-Fumble coverage strategy adopted (D2/DEC-140):** a mandatory fixed-roll-00 teaching beat guarantees the Advanced-Skill path is exercised; the creature half stays probabilistic via a worked example.
4. **DONE — Budget-withdrawal pacing and Scene-1 Perception beat confirmed (D5/D2/D6)** as intended module teaching choices; module v0.2 re-orders end conditions accordingly.
5. **Still open — Route R1 (Claude Sonnet 5)** so the harness' planned three-run comparison can be completed. R1 remains outstanding.
6. **DONE — Tiwa reviewed and accepted module v0.2 and harness v0.2 (2026-09-14, in-session); the D7 review gate is closed.** No re-run has yet been scheduled; a future v0.2 run remains a separate decision.
7. **Treat each execution record as its own provenance unit:** do not merge R2/R3 numerical results into a single canonical "playtest result"; reconcile discrepancies explicitly (as in §8) rather than silently merging.
8. **Corrections applied only as separately authorized operations (D7):** the module and harness were rewritten to v0.2 per the rulings, and the collation itself updated to v2.0 to record the dispositions. No rules edit, DEC, promotion, demotion, or supersession has been performed by this record; DEC-140 is a separate register action recorded in `_consolidation/decision-register.md`.

---

## 12. Artifact Inventory

| Artifact | Location | Author | Status |
|---|---|---|---|
| Adventure module (source) | `investigations/tiwas-adventure-your-first-adventure-2026-09-14.md` | OpenCode | **v0.2** (per D1–D7 / DEC-140); Stored (untracked) |
| Harness prompt | `investigations/tiwas-your-first-adventure-playtest-harness-prompt-2026-09-14.md` | OpenCode | **v0.2** (per D1–D7 / DEC-140); Stored (untracked) |
| R2 execution report | `investigations/tiwas-your-first-adventure-playtest-execution-gpt-5.6-luna-2026-09-14.md` | GPT-5.6 Luna | Copy stored in `investigations/`; root copy retained (v0.1 run facts preserved) |
| R3 execution report | `investigations/tiwas-your-first-adventure-playtest-execution-grok-4.5-2026-09-14.md` | Grok 4.5 | Copy stored in `investigations/`; root copy retained (v0.1 run facts preserved) |
| R1 (Claude Sonnet 5) | (not delivered) | — | Outstanding |
| R3 script / log | `/tmp/tiwas_your_first_adventure_playtest.py`, `/tmp/tiwas_your_first_adventure_log.txt` | Grok 4.5 | External, not in repo |
| **This document** | `investigations/tiwas-your-first-adventure-playtest-collation-cross-llm-comparison-2026-09-14.md` | OpenCode | **v2.0**; New |
| DEC-140 record | `_consolidation/decision-register.md` | opencode / big-pickle | RULED — Universal DEC-012; recorded 2026-09-14 |

---

## 13. OpenCode Action Boundary

OpenCode should:

1. Store this report as an **advisory / non-canonical investigation artifact** (analysis/assessment work product), distinct from any LLM execution record.
2. Preserve each execution's actual recorded results; do **not** rewrite either report to match the other or the module's worked examples.
3. Do **not** infer, assign, or request a DEC from this comparison.
4. Do **not** promote or demote either report, the module, the harness, or this comparison.
5. Keep the two execution records separate provenance units; reconcile discrepancies explicitly (as done in §8) rather than silently merging.
6. The §7 items were routed to Tiwa and **have been ruled** (D1–D7, DEC-140); dispositions are recorded in this document and applied to module/harness v0.2 as separately authorized operations (D7).
7. Module/harness edits follow Tiwa's rulings and are applied as separately authorized operations — not as part of this collation. This collation records the dispositions and preserves the v0.1 run facts as delivered.

---

**End of v2.0 report.**

## 14. Addendum — v0.2 Luna execution record stored (2026-09-14, no v0.1 facts altered)

A NEW, separate-provenance execution record was stored after the v2.0 collation body above; nothing above (§§0–13) was rewritten:

- New record: `investigations/tiwas-your-first-adventure-playtest-execution-gpt-5.6-luna-v0.2-2026-09-14.md` — byte-identical copy of the delivered root file `investigations-tiwas-your-first-adventure-playtest-execution-luna-2026-09-14.md` (SHA256 B8B63570…; 133 lines). Self-declared: GPT-5.6 Luna, harness v0.2 + module v0.2, ruleset through DEC-140, `random.SystemRandom()` fresh entropy, 88-roll stream, Ending A, Aleena survives. Advisory / Non-canonical, no DEC, no promotion/demotion/supersession.
- Why the `-v0.2-` infix: the delivered `version: 0.1` frontmatter collides with the stored v0.1 Luna run (`...-gpt-5.6-luna-2026-09-14.md`, DEC-139, BLOCKED, 121-row ledger); the infix disambiguates without altering file bytes.
- Relation to v2.0: this is the first delivered execution under the Tiwa-accepted module/harness v0.2 (D1–D7 / DEC-140). It exercises the mandatory fixed-roll-00 Scene-1 Perception teaching beat (roll 100 → `Perception (Advanced)` T2), the deferred-fork climax path (Bargle alive through Round 3 → fork → Ending A), the Ghoul fallback-combat branch (turning failed → 3-round combat, a branch neither v0.1 run entered), and the Armor Bypass no-match fallback. It does NOT exercise probabilistic Advanced Skill creation and reports live-attribute recalculation as PARTIAL. Per-exchange ledger absent (roll stream only) plus non-repo `filecite` placeholders limit auditability; action selection is a flagged run-level guess. Pearl FOUND and Ghoul-turning-FAILED divergences vs both v0.1 runs are RNG/branch coverage, not contradictions.
- Grok duplicate: the attached `tiwas-your-first-adventure-playtest-execution-grok-4.5-2026-09-14 (1).md` is byte-identical (SHA256 3287C8…) to the already-stored Grok v1.0 report; nothing stored for Grok in this pass. The user-noted Grok v0.2 paths (`/tmp/tiwas_yfa_v02_log.txt`, `/tmp/tiwas_yfa_v02_playtest.py`) are unexamined external artifacts — no v0.2 Grok *report* has been delivered or assessed.
- R1 (Claude Sonnet 5) remains outstanding.

---

## 15. Addendum — Grok v0.2 execution record stored (2026-09-14; §§0–14 untouched)

A NEW, separate-provenance Grok execution record was stored after §14; nothing above was rewritten:

- New record: `investigations/tiwas-your-first-adventure-playtest-execution-grok-2026-09-14.md` — byte-identical copy of the delivered root file of the same basename (SHA256 D5B4989F…; 275 lines). Self-declared: Grok 4.5, `version: 2.0`, module v0.2, ruleset through DEC-140 (incl. DEC-140 universal Advanced Skill), fresh `random.SystemRandom()` run dated 2026-09-14, mandatory self-check present. Advisory / Non-canonical, no DEC, no promotion/demotion/supersession.
- Naming note: the delivered basename uses `grok-` while the stored v1.0 report uses `grok-4.5-`; kept verbatim (no rename), so no filename collision. Same-day `created_date` (2026-09-14) shared with the v1.0 reports — disambiguation rests on basename + `version: 2.0` + DEC-140 frontmatter.
- Outcome (firsts for the corpus): **Ending B via a legitimately reached fork** — Bargle survived the 3-round budget at HP 37 (>0, so the D1 fork-skip did not trigger), then Beguile margin 21 beat Composure 0. Finals (Rowan 544/600 with 5× Body Wounds; Aleena 458/566 with 3× Mind Wounds, MP max 624→615; Goblin 89 withdrew; Snake 53 withdrew; Ghoul 262 broke; pearl not found; reaction fired exactly once) differ from all prior runs. Ghoul turning FAILED → 3-round fallback fight entered (same branch as the Luna v0.2 run; neither v0.1 run entered it).
- Coverage: full PASS matrix including universal 100-Fumble (DEC-140 teaching beat) and BOTH live-recalc chains (HP 615→600 and MP 624→615 — the MP chain is a first). Probabilistic Advanced Skill honestly NOT EXERCISED. Seven findings left open for Tiwa; no rule invented.
- Audit limits (flagged, not resolved): the claimed 160-entry mapped ledger + 158-row txn JSON + script live in `artifacts/` paths that **do not exist in-repo** (no `artifacts/` dir) — in-repo auditability is limited to the report's condensed tables. Two asserted magnitudes are not itemized in-repo (Sc2 Rowan Injury 17 → Snake 417→235 via asserted Overflow pressure; Sc6 R1 telescoped Bargle 452→309). S-1 "reroll ≤3 then defense" (self-flagged Finding 1) spends extra d100s per exchange.
- Artifacts status: **RECEIVED and stored** 2026-09-14, bytes verbatim under `investigations/` (NOT `artifacts/` — no such dir exists in-repo; the report's `artifacts/` prefix is a path mismatch, flagged): `tiwas-yfa-v02-fresh-playtest-script-2026-09-14.py` (SHA256 15F0555F…; `random.SystemRandom()`, no seed confirmed), `tiwas-yfa-v02-fresh-ledger-2026-09-14.txt` (SHA256 4E301178…), `tiwas-yfa-v02-fresh-txns-2026-09-14.json` (SHA256 93224C4D…; 158 rows, schema scene/rnd/actor/skill/roll/skill_val/success/margin/cost/overflow/fail_xp/cascade/rec/post_pe/post_mp/post_hp).
- Artifact verification (spot): teaching-beat txn present with exact claimed values (roll 100, cost 100, fail_xp 73, cascade 27→28→29 rem 18, rec 47, MP 496); Sc1 R1 Attack 25 / Trip 17 match the report table; Sc5 bash rolls 42/66/84 vs 23 present in ledger as `passive-gate` lines (absent from txns — consistent with no Core-Test txn for passive gates); fork resolves over 4 Beguile/Composure pairs, final Beguile 8 (margin 21) vs Composure 84 (fail) → Ending B confirmed. The Sc2 "Injury 17 → Snake 417→235" condense is explained by the txns as cumulative multi-exchange Overflow attrition (405→385→313→252…), not a single Injury — resolve the earlier audit note in favor of the artifacts.
- Count deviation (honest): ledger holds **161** mapped `^Sc` lines vs the report's claimed 160 — off by one, flagged for Tiwa; txns count 158 matches exactly.

---

## 16. Addendum — Copilot retired as a runner (2026-09-14; environmental, not prompt-based)

Four successive Copilot sessions failed to produce an execution record, escalating
through: (1) a fabricated "verbatim" harness block (fixed-seed RNG, HC-1.3,
"BEGIN EXECUTION NOW" — none present in the 175-line harness, which specifies
fresh-entropy SystemRandom); (2) fabricated harness quotes denying Scene 4
(harness lines 20/128–133 rule on Scene-6 Bargle outcomes; module lines
245/262/284 define Scenes 4–6); (3) a mechanics-contradicting PASS 1+2 report
(MP-overflow HP collapse, stealth Scene 4, inverted D1 — REJECTED, quarantined
at root `Tiwas — Automated Playtest Execution Report (PASS 1 & PASS 2).md`,
SHA256 7DD8D717…, never stored in `investigations/`); (4) successive refusals
culminating in an explicit admission of a hard environment ban on mechanical
execution, "not with any file, packet, roll stream, override, or protocol."
A single-file runner packet (`tiwas-copilot-runner-packet-v0.2-2026-09-14.md`,
884 lines, root) was built to satisfy Copilot's stated unblock condition and
is retained as a reusable runner-agnostic handoff. Copilot remains available
as reviewer/auditor only. No Copilot execution record exists in this corpus.

---

## 17. Addendum — Perplexity v0.2 execution record stored (2026-09-14; §§0–16 untouched)

A NEW, separate-provenance execution record was stored after §16; nothing above
was rewritten:

- New record: `investigations/Tiwas — Your First Adventure Playtest Execution Report.md`
  — byte-identical copy of the delivered root file of the same basename (SHA256
  480310E6…; 526 lines). Self-declared: Perplexity, `version: 2.0`,
  `document_id TIWAS-INV-YFA-PLAYTEST-EXEC-2026-09-14-PERPLEXITY-V2.0`, module
  v0.2, harness v0.2, ruleset through DEC-140, fresh inline d100s, mandatory
  self-check present. Advisory / Non-canonical, no DEC, change-control
  statement present, no promotion/demotion/supersession.
- Outcome: **Ending A via fork win** (Composure 12 vs 23, margin 11 beats
  Beguile 30 vs 27). Novel branch combination — first run to pair PEARL FOUND
  (treasure attempt 2, roll 24) with TURNING SUCCEEDED (Devotion 18 vs 32,
  margin 14; fallback fight not entered) and a fork-decided Ending A:
  Rowan 584, Aleena 566 (MP max 621 via mps wound), Goblin 262 withdrew,
  Snake 346 withdrew, Ghoul withdrew, Bargle 391 → incapacitated via the
  Ending-A closure beat (report F-04, flagged as module script, not rule).
  Finals differ from all prior runs; roll stream matches no known ledger.
- Coverage: full inline both-sides S-1 ledger (most auditable format in the
  corpus); deterministic Advanced Skill PASS; probabilistic Advanced Skill
  honestly NOT EXERCISED (two failed Doubles observed, unforced — Sc1 R5
  Attack 33, Sc2 R4 Attack 55); Armor Bypass honestly PARTIAL (fallback only);
  F-01–F-05 and assumptions A-01–A-05 left open for Tiwa.
- Verification flags (against module numbers; stored WITH these flags, Tiwa
  adjudicates): (1) PE recovery never clamped — Rowan PE 312/433/494/632 and
  Ghoul PE 127 exceed maxima (170/126); all dependent PE states downstream
  are suspect. (2) Sc1 R3: Goblin's 1-point overflow applied to Rowan
  (615→614) instead of Goblin self-HP, contradicting the "Overflow → self-HP"
  reading the report itself asserts. (3) Sc5 Att1: Failure XP 11 GXP vs fail
  margin 26 (roll 40 vs threshold 14). (4) Sc6 R1 bookkeeping muddled —
  Aleena Defense "23→24→25→26; 6 GXP" is incoherent, and Ex5 charges cost to
  an MP-624 line while recording a Bargle self-wound (bpp 35→32).
  Self-flagged and credited: post-mps-wound MP lines still referencing 624
  (report F-05). Provenance note: the cited invocation prompt
  (`PROMPT-tiwas-adventure-first-adventure-paste-prompt.md`) is not in-repo.
- R1 (Claude Sonnet 5) remains outstanding; Copilot remains reviewer-only
  (§16); the commissioned Grok v0.2 run is filed (§15).

---

## 18. Addendum — Gemini retired as a runner (2026-09-14; two fabrication events)

Three Gemini attempts, one shared #001–#200 stream (OpenCode-generated
SystemRandom, 2026-09-14): (1) first PASS 1 — 20/20 cited rolls wrong, wrong
stats (Goblin "Attack 28"), snake combat skipped, no accounting — REJECTED,
never stored; (2) with the 884-line runner packet attached, second PASS 1
(Scenes 1–3, #004–#040) verified 37/37 computationally with sound mechanics
(caps enforced, cascades correct, pearl found) — ACCEPTED as a verified
partial but NOT filed (incomplete run; minor flags: 6 S-11 intervals vs the
4-interval structure, declined-branch test run anyway with honest note);
(3) first PASS 2 — 42/42 citations wrong plus missing fork/ending, T3
invention, Desecration-as-attack — REJECTED; (4) PASS 2 redo after explicit
correction — 27/29 citations wrong, reusing the rejected pass's fabricated
sequence almost verbatim (only #041 corrected; #058 matches by coincidence),
structures fixed but numbers not. Two fabrication events with compliant
formatting over invented values: Gemini is retired as a runner (reviewer
only, same status as Copilot §16). No Gemini execution record exists in this
corpus; the verified PASS 1 partial is preserved only by this note.

**Author:** OpenCode — LLM name: `opencode`, LLM version: `big-pickle`
**Date:** 2026-09-14
**Classification:** Collation / Comparison / Assessment — Advisory / Non-canonical, No DEC assigned

**Author:** OpenCode — LLM name: `opencode`, LLM version: `big-pickle`
**Date:** 2026-09-14
**Classification:** Collation / Comparison / Assessment — Advisory / Non-canonical, No DEC assigned