---
document:
  title: "Ice Troll Combat Playtest — Meta-Collation of the Four Collated Cross-Reference Reports (Reports-of-Reports Synthesis)"
  version: "1.0"
  status: "Advisory working document (not canonical). Read-only analytical consolidation of the four collated cross-reference analyses (OpenCode v1 + Claude + Luna + Grok). Makes no rulings, assigns no DEC numbers, promotes nothing."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
sources:
  - "investigations/tiwas-ice-troll-playtest-collated-cross-reference-report-2026-09-04.md (OpenCode v1)"
  - "investigations/tiwas-ice-troll-playtest-cross-reference-comparison-2026-09-04.md (Claude Sonnet 5)"
  - "investigations/tiwas-ice-troll-playtest-comparative-readiness-report-luna-2026-09-04.md (GPT-5.6 Luna)"
  - "investigations/tiwas-ice-troll-combat-playtest-cross-reference-report-2026-09-04.md (Grok 4.5)"
  - "merged-combat-reports-playtest1.md (empirical corpus)"
---

# Ice Troll Combat Playtest — Meta-Collation of the Four Collated Cross-Reference Reports

**Purpose:** To compare, contrast, and synthesize the **four** collated cross-reference analyses (one authored by OpenCode and three authored by other LLMs: Claude Sonnet 5, GPT-5.6 Luna, and Grok 4.5) — all of which independently collate the same three underlying Ice Troll combat playtest execution records. This meta-report identifies **where the four collations converge**, **where they diverge in emphasis or structure**, and assembles a **unified readiness assessment** toward qualifying the Tiwas combat layer for a full playtest.

**Authority note:** This is a read-only analytical consolidation of analytical consolidations. It classifies, compares, and recommends. It does **not** rule, promote, demote, or reclassify anything. Per `governance/status-model.md`, the only path from non-canonical to canonical is the 8-step Promotion Rule; no item herein has completed that process. All authority-affecting actions remain Tiwa's, recorded by OpenCode against the live register only after per-item reconfirmation.

**Evidence-class discipline (per `governance/status-model.md`):** Items below are tagged as **Mechanical fact** (follows from locked rules), **Empirical finding** (supported by playtest/simulation evidence), **Recommendation** (proposed but not accepted), **Architectural constraint** (how systems interact, not a number), or **Designer ruling** (a deliberate designer choice). No empirical finding herein establishes a designer ruling.

---

## 1. The Four Collated Reports at a Glance

All four collate the **same three** underlying execution records (`merged-combat-reports-playtest1.md`), so their *source base* is identical. What differs is structure, depth, emphasis, and the unique value each adds.

| Report | Author | Structure | Length | Primary emphasis | Unique value-add |
|---|---|---|---|---|---|
| OpenCode v1 (`tiwas-ice-troll-playtest-collated-cross-reference-report-2026-09-04.md`) | OpenCode | 9 sections | ~212 lines | Two-lineage discipline; convergence/divergence register; readiness legend | Cross-report conflict register; explicit "no true contradictions in ruled mechanics" finding; 8-item recommendation list |
| Claude (`tiwas-ice-troll-playtest-cross-reference-comparison-2026-09-04.md`) | Claude Sonnet 5 | ~17 sections | ~293 lines | 2-to-1 lineage confidence weighting; G-item discipline; prioritised P1/P2/P3 | Surfaces **G-11** (Attack1/Defence1 attribute-pair disclosure) and **G-12** (scaffold-formula conflict as standalone tracking item); flags the D1/D2 Designer-Override label discrepancy; flags prompt-level initiative ambiguity |
| Luna (`tiwas-ice-troll-playtest-comparative-readiness-report-luna-2026-09-04.md`) | GPT-5.6 Luna | 24 sections | ~957 lines | Core-engine READY / consequence-layer INCOMPLETE distinction; evidence-class taxonomy | Explicit "no replacement Core engine needed" verdict; Phase 1–4 development sequence; P0/P1/P2 ladder; per-layer verdict table; 15-item governance restriction list |
| Grok (`tiwas-ice-troll-combat-playtest-cross-reference-report-2026-09-04.md`) | Grok 4.5 | 12 sections | ~301 lines | L1/L2/L3 lineage naming; status-classification key | Consolidated "Unresolved Mechanics Register" U-01–U-11; functional/scaffolded/interpretive/idle/absent classification of each system |

**Cross-collation note:** No two collations are verbatim copies; each is an independent analytical pass over the same shared evidence. Their differences are therefore *analytical*, not evidential.

---

## 2. Where the Four Collations Converge (unanimous findings)

These findings are asserted by **all four** collated reports independently and are the strongest conclusions of the entire exercise. [Empirical finding / Mechanical fact where locked]

### 2.1 Lineage structure (4/4 agreement)
- There are **two independent full-resolution lineages**, not three interchangeable runs: **Lineage A** = Claude (2-round abort) → Luna (11-round continuation) = a 13-round continuous combat; **Lineage B** = Grok (independent 22-round run). [Mechanical fact]
- Claude and Luna's terminal states must **not** be combined with Grok's as if repeated rounds of one combat. [Architectural constraint]
- All three lineages agree the **PC loses** (Lineage A: PC 0 / Troll 569; Lineage B: PC 0 / Troll 412). Different ending Troll HP is expected variation, not contradiction. [Empirical finding]

### 2.2 Core resolution engine is READY (4/4 agreement)
Every collation independently classifies the transactional core as confirmed working across runs:
d100 roll-under (DEC-001), 100-Fumble, floor rounding (DEC-002), derived stats (DEC-004), Skill Cap/Starting Value (DEC-005), 9-step Core Test (DEC-006), Cost=natural roll + Overflow→HP + immutability (DEC-007/007.A), Recovery (DEC-008), Failure XP → Skill Roll Pool → advancement (DEC-009/010), S-1 Opposed Contest (DEC-013), Quality base-tier floor (DEC-031), Track A/B (DEC-034), Effect auto-apply + post-hoc Active Defense (DEC-027/048), HP=0 incapacitation (DEC-052), Skill-Tier≥2 gate (DEC-041). [Empirical finding]

**Unanimous headline:** Tiwas does **not** need a replacement Core resolution engine. Luna states this most explicitly; all four agree. [Empirical finding → Recommendation]

### 2.3 The two hard blockers (4/4 agreement)
1. **Combat sequencing / initiative (SC-04)** — no Ruled turn-order/action-sequencing procedure exists. DEC-082 rules the Time/Action *economy expression* but not *sequencing*. Every collation independently flags this as a **hard blocker**; every combat needs an order. The Luna "Designer Override" is playtest-only and must **not** be promoted into a general rule. [Mechanical fact]
2. **Passive/aura Frightened trigger (C-04/G-04)** — no trigger mechanic exists; `Frightened` (DEC-079) defines only the Condition, and it works as a won-Effect. The passive/aura pathway (needed for the horror module) is **missing**. Load-bearing. [Mechanical fact / Empirical finding]

### 2.4 The scaffold-formula cross-lineage conflict (4/4 agreement — most important finding)
All four collations flag the same central methodological finding: the seams where scaffolding diverged across lineages:
- **Inflict Injury magnitude:** Lineage A used **winner's Margin**; Lineage B used **flat 25 HP**. Convergent recommendation: Margin (2 lineages : 1 lineage). [Empirical finding]
- **Active Defense mitigation:** Lineage A used **defender's Margin**; Lineage B used **flat −20 HP**. Convergent recommendation: Margin. [Empirical finding]

**Why this matters (unanimous):** because the two lineages used **mutually incompatible scaffold formulas**, cross-lineage combat-duration and lethality numbers are **not directly comparable**. This does not invalidate the Core findings, but it does invalidate any attempt to average or statistically combine HP trajectories across lineages. [Architectural constraint]

### 2.5 The gapped-but-not-blocking items (4/4 agreement)
All four list (with minor ID differences) the same non-blocking gaps requiring ruling before un-scaffolded play:
- Location-Tier-1 coarse-zone ranges (C-08) — quartile split (1–25/26–50/51–75/76–100) converged 2:1 (Claude+Luna vs Grok-unexercised).
- Quality gated-tier threshold (C-07) — ≥1 Base / ≥10 gated, converged 2:1.
- Creature defensive-skill basis (C-06) — **Brawling converged 3/3 independently**; no dedicated Defense skill in the v0.2 block.
- Defender-wins-opposed-attack consequence (C-09) — interpretive gap; conservative "attack fails, no counter-Effect" converged 2:1.

### 2.6 Not-exercised / no-data items (4/4 agreement)
Regeneration/Regrowth (freezing-gated, inactive → untested), Armor (S-5, neither side had Tags), complete Wound lifecycle, Location-Tier-2 subdivision (DEC-042), environmental/hazard cadence (DEC-089–093). All four agree these must remain **untested**, not classed as failures. [Empirical finding]

---

## 3. Where the Four Collations Diverge (exclusive or opposing analyses)

These differences do **not** mark factual disagreement — they are distinct lenses. Each is noted here because it changes what a reader would emphasise.

### 3.1 Confidence-weighting scheme
- **Claude** uses a strict **2-of-2 vs 1-of-2 lineage weighting** — the most rigorous disambiguation of which gaps are "confirmed in two replicates" vs "observed once."
- **Luna** uses an **evidence-class taxonomy** (Confirmed Working / Scaffold-Dependent / Partially Tested / Untested / Confirmed Gap / Interpretive Gap / GM-Required / Content Dependency) — richer but does not encode lineage-count the way Claude does.
- **Grok** uses a **status classification key** (Functional / Scaffolded / Interpretive / Idle / Absent) — concise but coarser.
- **OpenCode v1** uses a **Ready / Gapped / Missing / Deferred legend** with line-by-line lineage marking.

**Assessment:** No scheme is "wrong." Claude's is the most precise for *confidence*, Luna's is the most useful for *development sequencing*, Grok's is the most useful for *a quick status board*. A unified report should combine all three axes (lineage-count, evidence-class, priority). [Recommendation]

### 3.2 Whether the gated-Effect / Wound / Location pathway is 1-of-2 or 2-of-2 confirmed
- **Claude is the only collation to surface the decisive nuance:** the Wound/Location/gated-Effect pathway was exercised in **only the Claude→Luna lineage** (Lineage A). Grok's 22-round run never selected a gated Eff(Wound) — it stayed in the Base tier. **Therefore that pathway is 1-of-2 confirmed, not 2.**
- Luna and Grok present the Wound/Location pathway as "exercised" without foregrounding that it was exercised in only one lineage. [Novel analytical contribution — Claude]

**This is an important catch and should carry forward:** the strongest "works" confidence for the gated consequence layer is only 1-of-2, weaker than the 2-of-2 Core engine.

### 3.3 Priority/sequencing models
- **Luna:** Phase 1 (close combat execution interface) → Phase 2 (complete consequence layer) → Phase 3 (expand beyond combat) → Phase 4 (full benchmark playtest); plus a P0/P1/P2 per-item ladder.
- **Grok:** P0/P1/P2/P3 priority-development sequence.
- **Claude:** P1/P2/P3 grouped readiness.
- **OpenCode v1:** Ordered recommendations by load-bearing priority (sequencing first).

**Divergence in *order* matters:** OpenCode v1 and Claude both put **combat sequencing** at the very top. Luna and Grok also put sequencing at P0 but group it with the magnitude items. There is **no disagreement on content**, only on whether sequencing is *singularly* first or co-equal with the magnitude rulings. [Recommendation]

### 3.4 What each collation uniquely surfaced (exclusive value-adds)
| Report | Item surfaced only by that collation |
|---|---|
| Claude | **G-11** (Attack1/Defence1 attribute-pair disclosure — the prompt's flat attribute presentation may under-serve the opposed-contest model); **G-12** (elevate the scaffold-formula conflict itself to a standalone tracked item rather than a footnote); the **D1/D2 Designer-Override label discrepancy** (§2.1: the "Round 1, Exchange 1" label is recorded against a mid-Round-2 resumption); prompt-level **initiative ambiguity** (scaffold vs GM-stop unresolved inside the prompt); Grok's **D3 silence on defender-wins** and the candidate-tracking asymmetry across lineages |
| Luna | The explicit **"no replacement Core engine"** verdict as a named project-state milestone; the full **15-item governance restriction list**; the richest per-layer verdict table; the cleanest **Phase 1–4** sequence; the explicit rule **against statistically combining the three results** |
| Grok | The consolidated **Unresolved Mechanics Register U-01–U-11**; the concise **Functional/Scaffolded/Interpretive/Idle/Absent** status board; **cross-lineage consistency observations** |
| OpenCode v1 | The **Cross-Report Conflict/Divergence Register** table; the explicit **"No true contradictions in ruled mechanics"** negative-finding framing; the line-by-line rule-DEC mapping in the working-systems table; the cleanest **8-item candidate DEC list** |

---

## 4. Unified Readiness Assessment (assembled from all four)

Legend: ✅ Ready · ⚠️ Gapped (scaffold needed) · ❌ Missing (blocker) · ➖ Untested (no data)

### 4.1 Ready / confirmed working (Core resolution layer) — all four agree
d100 roll-under · rounding · derived stats · Skill Cap/Starting Value · 9-step Core Test · Cost/Overflow · Recovery · Failure XP/Skill Roll Pool · S-1 Opposed Contest · Quality base-tier floor · Track A/B · Effect auto-apply · HP=0 incapacitation · Skill-Tier≥2 gate. **Verdict: READY for extended integration testing.** [Empirical finding]

### 4.2 Gapped — playable only with scaffold (magnitude/sequencing layer) — all four agree
Inflict Injury magnitude (C-01) ⚠️ · Active Defense mitigation (C-02) ⚠️ · Quality gated-threshold (C-07) ⚠️ · Location coarse-zone ranges (C-08) ⚠️ · Defender-wins consequence (C-09) ⚠️ · Creature defensive-skill basis (C-06) ⚠️ · Frightened magnitude (within S-3 vocabulary) ⚠️.

### 4.3 Missing — block a full un-scaffolded playtest — all four agree
**Combat sequencing / initiative (SC-04)** ❌ · **Passive/aura Frightened trigger (C-04/G-04)** ❌.

### 4.4 Untested — no data, defer — all four agree
Regeneration/Regrowth/healing vocabulary (C-05) · Armor (S-5) · complete Wound lifecycle · Location-Tier-2 subdivision (DEC-042) · environmental/hazard cadence (DEC-089–093) · equipment · magic · economy.

### 4.5 The one-voice verdict (synthesis of all four)
> **Tiwas's Core resolution engine has passed its first meaningful multi-exchange combat integration test and does not need to be replaced. What remains is the combat consequence and sequencing layer, which is not yet deterministic without non-canonical scaffolding. A full un-scaffolded *Beyond the Vale of Madness* playtest is therefore not yet ready; targeted, scaffolded combat integration testing remains valid and high-value empirical work.**

---

## 5. Consolidated Recommendation Set (unified across all four; no DEC numbers assigned)

Each is a **Recommendation** only; none is a ruling. All require Tiwa's per-item direction via the Promotion Rule.

1. **Rule combat sequencing / initiative (SC-04)** — the single highest-priority gap in every collation. Existing scaffolding/overrides (Luna's Designer Override) must not be promoted.
2. **Rule Inflict Injury magnitude (C-01)** — convergent Margin-based candidate (2 : 1).
3. **Rule Active Defense mitigation (C-02)** — convergent defender's-Margin candidate (2 : 1).
4. **Rule the passive/aura Frightened trigger (C-04/G-04)** — select one of the scoped options (won-Effect-only / Core-Test-on-encounter / DEC-088-style scene trigger / defer).
5. **Rule the Quality gated-tier threshold (C-07)** — convergent ≥1 Base / ≥10 gated candidate.
6. **Lock the Location-Tier-1 coarse-zone table (C-08)** — convergent quartile candidate; also close the 1-of-2 confirmation weakness by re-exercising Wound/location in a second lineage.
7. **Resolve the creature defensive-skill basis (C-06)** — Brawling converged 3/3; confirm as universal or add template defense skill.
8. **Rule the defender-wins counter-Effect question (C-09)** — convergent "attack fails, no counter-Effect" candidate.
9. **Address Claude's prompt-level items** — disclose Attack1/Defence1 pair treatment (G-11) and un-ambiguate initiative (scaffold vs GM-stop) in the playtest prompt (G-12 discipline).
10. **Preserve methodological discipline (all four)** — never combine the three HP trajectories; keep the DISC 1-of-2 vs 2-of-2 distinction for the gated consequence layer.

**Recommended DEC candidate list (for Tiwa's per-item ruling; no numbers assigned):** C-01, C-02, C-04, C-06, C-07, C-08, C-09, plus **SC-04 (NEW — combat sequencing)**, and possible C-10 for Frightened magnitude within the S-3 vocabulary.

---

## 6. Tiwa's Per-Item Rulings (recorded 2026-09-04)

All candidates in §5 were presented to Tiwa and ruled. Each was recorded as a **non-canonical designer ruling** in `_consolidation/decision-register.md` Section B (per the register's established recording practice). **No ruling here promotes anything to Canonical** — that requires the 8-step Promotion Rule, which has not been run. None of these entries has a DEC number assigned except where noted; all are logged with the register.

| Candidate | Tiwa ruling | Register (Section B) |
|---|---|---|
| C-04/G-04 Passive Frightened trigger | **Option C — scene-state / Condition-Clause trigger** (`Scene State → Condition Clause → Frightened`, reusing DEC-088 grammar; declarative, not probabilistic) | DEC-094 |
| C-10 Frightened magnitude | **Folded into C-04** — no independent magnitude architecture; DEC-079 governs (Value Z = −Y) | DEC-094 |
| SC-04 Combat sequencing / initiative | **Speed-based turn order; alternating turns; one S-1 combat exchange per turn; lower-Speed combatants may be interrupted/eliminated before acting** | DEC-095 |
| C-01 Inflict Injury magnitude | **ACCEPT — Winner's Margin** | DEC-096 |
| C-02 Active Defense mitigation | **ACCEPT — Defender's Margin** | DEC-097 |
| C-06 Creature defensive-skill basis | **CONDITIONAL ACCEPT — Brawling is the *default* defensive Skill for templates lacking an authored one; explicitly NOT a universal principle** | DEC-098 |
| C-07 Quality-gated tier threshold | **ACCEPT — Quality ≥1 Base / ≥10 Gated** | DEC-099 |
| C-08 Tier-1 Location zones | **ACCEPT — Quartile split** (1–25 Legs / 26–50 Torso / 51–75 Arms / 76–100 Head) | DEC-100 |
| C-09 Defender-wins consequence | **ACCEPT — attack fails, defender gains no counter-Effect** | DEC-101 |
| G-11 Attack1/Defence1 disclosure | **Methodology — NOT a DEC.** Track as playtest-reproducibility / prompt-disclosure requirement. **Amendment:** skill names should be `AttackX` / `DefenceX` where **X = the skill tier** | (no register entry; methodology note — see §6.1) |
| G-12 Scaffold-formula conflict | **Methodology/audit — NOT a DEC.** Belongs in the playtest methodology audit, not the game rules | (no register entry; methodology note — see §6.1) |

### 6.1 Methodology/audit dispositions (G-11, G-12)

Per Tiwa, G-11 and G-12 are **playtest methodology / audit items, not game mechanics, and not DECs**. They are therefore recorded as methodology notes here and tracked in the playtest-methodology audit, **not** added to the decision register:

- **G-11 — Playtest reproducibility / prompt disclosure requirement.** The playtest prompt must disclose how the Attack/Defence attribute pair is presented and named. **Amendment (Tiwa, 2026-09-04):** the skill name should be **`AttackX` / `DefenceX`** where **X = the skill tier** of the skill (e.g., `Attack1`, `Defence1` for a Tier-1 skill; `Attack2`/`Defence2` for Tier-2), so the tier is self-describing in the name. This applies to the playtest prompt and derived documentation.
- **G-12 — Scaffold-formula conflict.** The cross-lineage divergence in scaffold formulas (Lineage A Margin-based vs Lineage B flat-values for Injury/Defense) is a **methodology/audit issue** to be tracked in the playtest methodology audit, not encoded as a game rule. It underscores that cross-lineage magnitude figures are not directly comparable and must never be averaged/statistically combined.

These two items are the only candidates from the collated list that Tiwa classified as non-game-mechanic; all others became register rulings (DEC-094…DEC-101).

---

## 7. What Was and Was Not Changed

**Changed by this document:** this meta-collation advisory artifact in `investigations/`, plus the documentarian-verification annotation on the three previously stored collation reports. As the synthesis vehicle for the candidate list, this document now also records Tiwa's per-item adjudication (Section 6) and the G-11/G-12 methodology dispositions (Section 6.1).

**Changed separately (register):** the decision register `_consolidation/decision-register.md` gained **DEC-094 … DEC-101** — Tiwa's non-canonical designer rulings for C-04/C-10 (DEC-094), SC-04 (DEC-095), C-01 (DEC-096), C-02 (DEC-097), C-06 (DEC-098), C-07 (DEC-099), C-08 (DEC-100), and C-09 (DEC-101). These are recorded as **non-canonical designer rulings** per the register's Section B practice. **They do NOT promote anything to Canonical** — the 8-step Promotion Rule has not been run; the Canonical Rules & Changelog is untouched; no mechanical authority changed.

**Not changed:** the canonical ruleset and its changelog, governance documents, the underlying three source execution reports, `claude-playtest-prompt-version2.md`, the Ice Troll v0.2 conversion file, and the three collation reports' substantive content (only provenance/verification notes appended). G-11 and G-12 were **not** added to the register (methodology/audit only, per Tiwa).

**Source confirmation:** this document draws solely from the four listed collation reports, the shared empirical corpus, and Tiwa's 2026-09-04 ruling messages. Where one collation uniquely surfaced an item (e.g., Claude's G-11/G-12, the 1-of-2 Wound pathway nuance), that attribution is noted. No figure was invented; no lineage was indiscriminately combined.
