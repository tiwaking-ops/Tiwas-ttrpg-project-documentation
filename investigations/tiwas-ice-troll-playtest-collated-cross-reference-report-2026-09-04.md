---
document:
  title: "Ice Troll Combat Playtest — Collated Comparative Cross-Reference Report"
  version: "1.0"
  status: "Advisory working document (not canonical). Read-only analytical consolidation of three empirical playtest execution records. Makes no rulings, assigns no DEC numbers, promotes nothing to the live register."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
sources:
  - "investigations/tiwas-ice-troll-combat-playtest-execution-report-2026-09-04.md"
  - "investigations/tiwas-ice-troll-playtest-execution-handoff-claude-2026-09-04.md"
  - "investigations/tiwas-ice-troll-playtest-continuation-and-results-luna-2026-09-04.md"
---

# Ice Troll Combat Playtest — Collated Comparative Cross-Reference Report

**Purpose:** To collate, compare, contrast, and cross-reference the three Ice Troll combat playtest execution records, and to consolidate their empirical findings into a single readiness assessment identifying which Tiwas systems **work**, which are **missing**, and which **need further development** — toward qualifying the combat layer for a full playtest.

**Authority note:** This is a read-only analytical consolidation. It classifies findings by evidence class, identifies cross-report conflicts and convergences, and produces recommendations. It does **not** rule, promote, demote, or reclassify anything. Per `governance/status-model.md`, the only path from non-canonical to canonical is the 8-step Promotion Rule; no item herein has completed that process. All authority-affecting actions remain Tiwa's, recorded by OpenCode against the live register only after per-item reconfirmation.

**Evidence-class discipline (per `governance/status-model.md`):** Findings below are tagged as **Mechanical fact** (follows from locked rules), **Empirical finding** (supported by playtest/simulation evidence), **Recommendation** (proposed but not accepted), **Architectural constraint** (how systems interact, not a number), or **Designer ruling** (a deliberate designer choice). No empirical finding herein establishes a designer ruling.

---

## 1. The Three Source Reports and Their Lineages

The three reports are **not interchangeable copies** — they record **three distinct executions** of the same v2.1 prompt, and they must be handled by lineage.

| Report | Executing LLM | Lineage / relationship | Terminal state | Outcome |
|---|---|---|---|---|
| `tiwas-ice-troll-combat-playtest-execution-report-2026-09-04.md` | Grok 4.5 | **Independent** full 22-round run to completion | PC HP 0; Troll HP 412 | PC incapacitated (DEC-052) |
| `tiwas-ice-troll-playtest-execution-handoff-claude-2026-09-04.md` | Claude Sonnet 5 | **Independent** 2-round / 4-exchange run, **explicit abort** | PC HP 585; Troll HP 698 | Aborted (allowed terminal state) |
| `tiwas-ice-troll-playtest-continuation-and-results-luna-2026-09-04.md` | GPT-5.6 Luna | **Continuation** of Claude's abort state (resumes 585/698) | PC HP 0; Troll HP 569 | Troll victory (PC incapacitated) |

**Cross-reference implication:** Grok's run and the Claude→Luna lineage are **two separate full-resolution data points** plus one partial. They should be treated as independent empirical replicates, not as agreement or disagreement about a single outcome — all three agree the PC **loses** (Grok: PC 0/Troll 412; Claude→Luna: PC 0/Troll 569). The two full runs differ in ending Troll HP (412 vs 569), which is expected variation under different d100 sequences and scaffold application, **not** a contradiction. [Empirical finding]

**Lineage caution:** The Luna report is only interpretable as a continuation; its pre-combat state (§5: PC 585 / Troll 698) matches Claude's end-state, confirming the handoff. Cross-report figures should never be averaged without accounting for lineage.

---

## 2. Head-to-Head Comparison of Execution Parameters

All three ran the identical v2.1 prompt (`claude-playtest-prompt-version2.md`) with the inlined Ice Troll block, identical Adventurer-1 (24×50, Attack1/Defence1 Tier-2 at Starting 25), and the same DEC-012 exception provenance. Key differences:

| Parameter | Grok 4.5 | Claude Sonnet 5 | GPT-5.6 Luna |
|---|---|---|---|
| Rounds | 22 | 2 (abort) | 11 (continuation) |
| Terminal | PC 0 / Troll 412 | PC 585 / Troll 698 | PC 0 / Troll 569 |
| GM-stops | None | **1** (passive Frightened trigger) | None (Frightened treated as won-Effect) |
| Advanced Skill creation | **None** (no qualifying failed Double) | None reported | **Yes** (Skill-(29), Tier-3, Cap 70) |
| Effect selected (primary) | Base-tier Inflict Injury | Wound + Frightened (via won Effect) | Wound, Frightened, location effects |
| Location Index | **Not exercised** | Exercised (Torso) | Exercised (via zones) |
| Designer Override | Not used | Not used | **Used** ("Round 1, Exchange 1 — PC attacks") |

### 2.1 GM-stop and Frightened divergence (IMPORTANT cross-report contrast)

- **Grok:** reported zero GM-stops; C-04 (passive Frightened trigger) "deliberately not invoked." The Frightened Condition was never applied because it wasn't selected as a won Effect and no passive trigger was attempted.
- **Claude:** reported the **one genuine GM-stop** — the passive Frightened trigger (Appearance: Hideous corresponding to a GURPS passive Fright Check with no Tiwas equivalent). Claude correctly stopped rather than invent a trigger. It *did* apply Frightened as a won-Effect result (Round 2, Exchange 4, Tier-2 Value −2, source-dependent per DEC-079).
- **Luna:** recorded Frightened as "exercised" and carried the −2 modifier forward, but **did not** record a passive-trigger GM-stop; the module's passive fright appears to have been subsumed into the won-Effect pathway (consistent with the favoured scope in option 1 below, but **not** a ruled decision).

**Convergence:** all three agree the **passive/aura Frightened trigger (C-04) has no ruled mechanic** and is the qualitative gap in the corpus. They differ only in *whether it was invoked* — Claude invoked-and-stopped; Grok and Luna did not invoke it. **Recommendation:** this is the one subsystem whose absence is load-bearing for horror modules and must be resolved before a full-module playtest, not merely deferred. [Empirical finding → Recommendation]

---

## 3. Systems Confirmed Working (cross-report convergence)

The following systems functioned end-to-end in **at least two** of the three executions (≥2 of 3 = robustly exercised; 1 of 3 = exercised once). These are the strongest "works" candidates for full-playtest readiness. [Mechanical fact where locked; Empirical finding for playtest confirmation]

| System | DEC | Grok | Claude | Luna | Readiness |
|---|---|---|---|---|---|
| d100 roll-under / 100-Fumble / Doubles | DEC-001 | ✅ | ✅ | ✅ | **Ready** |
| Floor rounding | DEC-002 | ✅ | ✅ | ✅ | **Ready** |
| Derived statistics (live) | DEC-004 | ✅ | ✅ | ✅ | **Ready** |
| Skill Cap / Starting Value | DEC-005 | ✅ | ✅ | ✅ | **Ready** |
| Core Test Transaction (9-step) | DEC-006 | ✅ | ✅ | ✅ | **Ready** |
| Cost = natural roll; Overflow→HP; Overflow immutability | DEC-007/007.A | ✅ | ✅ | ✅ | **Ready** |
| Recovery (floor(Regen/2), clamped) | DEC-008 | ✅ | ✅ | ✅ | **Ready** |
| Failure XP → Skill Roll Pool → advancement | DEC-009/010 | ✅ | ✅ | ✅ | **Ready** |
| S-1 Opposed Contest (matrix, Quality) | DEC-013 | ✅ | ✅ | ✅ | **Ready** |
| Quality-gated Effect tier | DEC-031 | ✅ | ✅ | ✅ | **Ready** |
| Track A/B sequential application | DEC-034 | ✅ | ✅ | ✅ | **Ready** |
| Effect auto-apply + post-hoc Active Defense | DEC-027/048 | ✅ | ✅ | ✅ | **Ready** |
| HP = 0 forced incapacitation | DEC-052 | ✅ | — | ✅ | **Ready** (Claude aborted before HP=0) |
| Failed-Double Advanced Skill creation | DEC-012 | (no Double) | (none) | ✅ | **Works** (1 of 3 — exercised by Luna) |
| Zero-Step Location Index | DEC-014/041 | — | ✅ | ✅ | **Works** (2 of 3) |
| Wound Condition application | DEC-032–037 | — | ✅ | ✅ | **Works** (2 of 3) |
| Frightened Condition (won-Effect path) | DEC-079 | — | ✅ | ✅ | **Partially** (see §2.1, no passive trigger) |
| Active Defense voluntary mode | DEC-044–050 | ✅ | ✅ | ✅ | **Ready** (magnitude scaffolded — see §4) |
| Skill-Tier ≥ 2 gate | DEC-041 | ✅ | ✅ | ✅ | **Ready** (respected) |

**Summary:** The **core resolution engine** (DEC-001→013) is consistently ready across all three runs, plus the advancement, recovery, and incapacitation endpoints. What is **uniformly confirmed** is the transactional core; what is **uniformly scaffolded or absent** is the combat-layer magnitude and sequencing layer.

---

## 4. Systems That Are Missing or Gap (cross-report convergence)

These are the gaps that force a scaffold or GM-stop, ranked by cross-report consistency and load-bearing relevance. All are **Recommendation** unless noted. All require Tiwa ruling before they become testable without scaffolding.

### 4.1 Inflict Injury magnitude (C-01) — MISSING, universally scaffolded
- **Grok:** 25 HP flat. **Claude:** winner's Margin (Skill − Roll). **Luna:** winner's Margin.
- **Cross-reference:** Claude and Luna **converge on "winner's Margin"**; Grok used flat 25. Convergence is strong on Margin as a natural fit (rewards precision, ties into the existing roll-under economy). [Empirical finding]
- **Status:** No ruled formula exists (DEC-023 defines the Effect; no DEC gives a number; DEC-085 carries it open). **Blocks** the most common combat pathway (Base-tier), since Wound requires Tier-2. **Recommendation:** rule on Inflict Injury magnitude before a full playtest; the Margin-based option is the leading convergent candidate but must go through the Promotion Rule.

### 4.2 Active Defense mitigation amount (C-02) — MISSING, universally scaffolded
- **Grok:** −20 HP (or full cancel ≤20) / 0 on failure. **Claude:** defender's Margin / 0 on failure. **Luna:** defender's Margin / 0 on failure.
- **Cross-reference:** Claude and Luna **converge on "defender's Margin"**; Grok used flat −20. This is a near-identical convergence pattern to C-01. [Empirical finding]
- **Status:** No ruled mitigation formula (DEC-044–050 rule the framework, not the number). **Recommendation:** rule the Active Defense mitigation formula; Margin is the strong convergent candidate.

### 4.3 Combat sequencing / initiative (SC-04) — MISSING, universally scaffolded
- **Grok:** "Higher Speed acts first; one attack per character per round." **Claude:** flagged need; no value (2-round abort, but notes no Ruled procedure). **Luna:** resolved only via **Designer Override** ("Round 1, Exchange 1 — PC attacks"), explicitly non-general.
- **Cross-reference:** All three independently confirm **no Ruled initiative/turn-order/action-sequencing procedure exists**. DEC-082 rules the Time/Action **economy expression** (penalty model, no action-point pool) but **not** sequencing. [Mechanical fact]
- **Status:** This is a **hard blocker** for any full playtest, not a magnitude gap — every combat must establish order. **Recommendation:** highest-priority new ruling. NOTE: the Luna "Designer Override" is **playtest-only and non-canonical** — it must NOT be promoted into a general sequencing rule.

### 4.4 Passive / aura Frightened trigger (C-04) — MISSING, qualitative
- **Grok:** not invoked. **Claude:** **GM-stop** (correct). **Luna:** subsumed into won-Effect path.
- **Status:** No trigger mechanic exists; `Frightened` (DEC-079) defines the Condition only. Load-bearing for horror modules (BToV-Madness invokes Fright Checks §38/§58). **Recommendation:** resolve via one the scoped options (won-Effect-only; Core-Test-on-encounter; DEC-088 Condition-Clause-style scene trigger; or defer) — see §7.

### 4.5 Location-Tier-1 coarse-zone numeric ranges (C-08) — GAP, partially scaffolded
- **Grok:** not exercised (no location effect selected). **Claude:** scaffolded quartiles (1–25 Legs / 26–50 Torso / 51–75 Arms / 76–100 Head). **Luna:** same quartiles.
- **Cross-reference:** Claude and Luna **converge on the quartile split**; DEC-041 explicitly leaves ranges directional/not locked. [Empirical finding]
- **Status:** only needed if location/Wound effects are selected. **Recommendation:** lock the coarse zone table (quartile candidate) to unblock Wound/called-shot play.

### 4.6 Quality→gated-tier numeric threshold (C-07) — MISSING, scaffolded
- **Grok:** not explicitly reported (used ≥1 Base). **Claude:** Quality ≥1 Base / ≥10 gated. **Luna:** same ≥1/≥10.
- **Cross-reference:** Claude and Luna **converge on ≥1 Base / ≥10 gated**; DEC-031 defines the floor rule (≥1 Base) but not the gated threshold. [Empirical finding]
- **Status:** needed to govern when gated/Wound Effects unlock. **Recommendation:** rule the gated-tier Quality threshold (≥10 convergent candidate).

### 4.7 Creature defensive-skill substitution (C-06) — GAP, scaffolded
- **Grok:** used Brawling as defender's skill. **Claude:** used Brawling (flagged as Gap, no dedicated "Defence" skill in v0.2 block). **Luna:** used Brawling.
- **Cross-reference:** **All three converged on Brawling** as the Ice Troll's defensive skill, independently. [Empirical finding]
- **Status:** The v0.2 conversion block contains Tier-2 attack skills (Icy Claws, Sharktoothed Maw) but no dedicated defense skill. **Recommendation:** either add a defense skill to the creature template or rule that Brawling serves as the universal defensive skill — a creature-template/content decision for Tiwa.

### 4.8 Defender-wins-opposed-attack consequence (C-09) — INTERPRETIVE GAP
- **Grok:** not reported as an issue. **Claude:** handled conservatively (attack fails, no counter-Effect). **Luna:** same conservative handling.
- **Cross-reference:** Claude and Luna **converge on "attack fails, no counter-Effect for either side"**; DEC-013's matrix specifies failure outcomes but does not explicitly grant a winning defender a counter-Effect right. [Empirical finding]
- **Status:** interpretive, not a numeric gap. **Recommendation:** rule explicitly whether a defender who wins an opposed attack contest may declare a counter-Effect.

### 4.9 Regeneration / Regrowth / healing-magnitude vocabulary (C-05) — NOT EXERCISED, carried open
- **All three:** treated the Ice Troll's freezing-gated Regeneration/Regrowth as **inactive** (no `env:freezing` present). No healing-magnitude data generated.
- **Status:** No new empirical data. Remains open from DEC-085/DEC-088. **Recommendation:** defer; only needed when the full module imposes a freezing environment or when a healing tick matters.

---

## 5. Cross-Report Conflict / Divergence Register

| Item | Grok | Claude | Luna | Resolution status |
|---|---|---|---|---|
| Inflict Injury magnitude | Flat 25 | Margin | Margin | **Convergent** (Margin, 2:1) — recommend Margin |
| Active Defense mitigation | Flat −20 | Margin | Margin | **Convergent** (Margin, 2:1) — recommend Margin |
| GM-stop for passive Frightened | None (not invoked) | **1 stop** | None (won-Effect only) | **Divergent handling** — all agree no rule exists; the stop is the correct behavior when invoked |
| Advanced Skills created | None | None | **Yes** (Tier-3) | Not a conflict — different d100 sequences; confirms the pathway works |
| Ending Troll HP | 412 | (abort) | 569 | Not a conflict — different runs/lineage |

**No true contradictions in ruled mechanics** were found across the three reports — they agree on every locked-rule behaviour tested. The only apparent divergences are (a) scaffold *values* chosen differently per LLM (flat vs Margin), and (b) whether the passive Frightened trigger was invoked. Both are expected and acceptable for scaffolding; they underscore that the magnitude/threshold items are genuinely unruled.

---

## 6. Consolidated Readiness Assessment (toward full playtest)

Legend: ✅ Ready · ⚠️ Gapped (scaffold needed) · ❌ Missing (blocker)

### 6.1 Ready as-is (core resolution layer)
d100 roll-under · rounding · derived stats · skill Cap/Starting Value · 9-step Core Test · Cost/Overflow · Recovery · Failure XP/Skill Roll Pool · S-1 Opposed Contest · Quality base-tier floor · Track A/B · Effect auto-apply · HP=0 incapacitation · Skill-Tier≥2 gate.

### 6.2 Gapped — playable only with scaffold (magnitude/sequencing layer)
Inflict Injury magnitude (C-01) ⚠️ · Active Defense mitigation (C-02) ⚠️ · Quality gated-threshold (C-07) ⚠️ · Location coarse-zone ranges (C-08) ⚠️ · Defender-wins consequence (C-09) ⚠️ · Creature defensive-skill basis (C-06) ⚠️ · Frightened magnitude (part of C-03) ⚠️.

### 6.3 Missing — block a full playtest (must be ruled)
**Combat sequencing / initiative (SC-04)** ❌ — every combat requires an order; no rule exists (the Luna override is playtest-only and must not be promoted). **Passive/aura Frightened trigger (C-04)** ❌ — load-bearing for the horror module design intent.

### 6.4 Not yet exercised (no data; defer)
Regeneration/Regrowth/healing vocabulary (C-05) · Armor (S-5, neither side had Tags) · full Location-Tier-2 subdivision procedure (DEC-042) · environmental/hazard cadence (DEC-089–093).

---

## 7. Recommendations (advisory — for Tiwa's ruling, not self-executing)

Ordered by load-bearing priority. Each is a **Recommendation**; none is a ruling.

1. **Rule on combat sequencing / initiative (SC-04)** — the single highest-priority gap; without it a full combat playtest cannot begin un-scaffolded. Decide turn order, per-round action count, and tie handling (DEC-082 governs economy-expression only).
2. **Rule on Inflict Injury magnitude (C-01)** — adopt the convergent Margin-based formula (or a ruled alternative) via the Promotion Rule.
3. **Rule on Active Defense mitigation (C-02)** — adopt the convergent defender's-Margin formula (or ruled alternative).
4. **Rule on the passive/aura Frightened trigger (C-04)** — select one of the scoped options (won-Effect-only / Core-Test-on-encounter / DEC-088-style scene-state trigger / defer), to unblock horror-module play.
5. **Lock the Location-Tier-1 coarse-zone table (C-08)** — the convergent quartile split is the leading candidate.
6. **Rule the Quality gated-tier threshold (C-07)** — the convergent ≥1/≥10 is the leading candidate.
7. **Resolve the creature defensive-skill basis (C-06)** — confirm Brawling-as-universal or add a template defense skill.
8. **Rule the defender-wins counter-Effect question (C-09)** — the convergent "attack fails, no counter-Effect" is the leading candidate.

**Recommended DEC candidate list** (for Tiwa's per-item ruling; no numbers assigned): C-01, C-02, C-04, C-06, C-07, C-08, C-09, plus **SC-04 (NEW — combat sequencing)**, and a possible C-10 for Frightened magnitude within the S-3 vocabulary.

---

## 8. What a Full Playtest Will Need Beyond These Findings

- **A ruled combat-sequencing procedure** (SC-04) — otherwise every full combat starts with a scaffold or override.
- **Ruled magnitude/threshold values** for the six gapped items so the referee does not have to invent values mid-scene.
- **Resolved passive-Frightened handling** for the horror module, else the first horrifying encounter triggers a mandatory GM-stop.
- **Confirmed creature template completeness** (defensive-skill basis; location zone table) before the module's monsters are used un-scaffolded.
- **A full-module scenario** (BToV-Madness) that exercises non-combat systems too — skill checks, environmental hazards (DEC-089–093), recovery/rest (DEC-071–074), and the fear beats — since the current combat test exercised only the transactional core.

---

## 9. What Was and Was Not Changed

**Changed by this document:** this new advisory investigation artifact in `investigations/`. No register entry, no ruling, no promotion, no DEC numbers assigned; nothing reclassified.

**Not changed:** the decision register, canonical ruleset, governance documents, the three source reports, `claude-playtest-prompt-version2.md`, and the Ice Troll v0.2 conversion file are all untouched.

**Source confirmation:** this report's findings are drawn solely from the three listed source reports. Where a figure appears in only one report it is flagged; no figure was invented or averaged across incompatible lineages without note.
