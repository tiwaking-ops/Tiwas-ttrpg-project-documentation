---
document:
  title: "DEC-078 Encumbrance Capacity Formula — Advisory Synthesis and Options Comparison"
  version: "1.0"
  status: "Advisory only — Non-Canonical. No ruling made. No DEC number assigned by this document."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-10"
  last_modified_date: "2026-09-10"
---

# Tiwas — DEC-078 Encumbrance Capacity Formula: Advisory Synthesis

**Document Version:** 1.0
**Document Status:** Advisory synthesis. **NOT a ruling. NOT canonical.**
**Author:** Claude Sonnet 5 (model string: `claude-sonnet-5`)
**Authority:** Advisory only. Tiwa retains sole ruling authority per `governance/authority.md`. This document issues no DEC number and closes no open item.
**Purpose:** Record, for OpenCode's repository and Tiwa's review, the complete advisory work product from the 2026-09-10 chat session addressing the open DEC-078 residual: exact capacity formula (bpe/bee direction vs. alternatives), numeric threshold values, and Skill-side modifier magnitudes.
**Relationship to prior material:** This document does not supersede, amend, or promote `investigations/tiwas-encumbrance-capacity-formula-options-brief-2026-09-09.md`. It is a follow-on synthesis building on that brief's five candidate options, adding elicited scope constraints, comparative-system research, quantitative modeling, and an advisory (non-binding) recommendation.
**Critical rule:** Nothing in this document is canonical or ruled merely because it is written up formally. Per Proposals/WIP §21 (8-step Promotion Rule) and the standing project governance model, any content here requires Tiwa's explicit ruling before OpenCode may record it as a DEC or modify the Decision Register beyond storing this document as a reference artifact.

---

## 1. Session Scope and Elicited Constraints

Before producing analysis, the author LLM elicited three clarifying answers from Tiwa to bound scope. These answers govern the framing of everything that follows and should be treated as session-scoping input, not rulings in themselves.

| # | Question | Tiwa's Answer |
|---|---|---|
| 1 | How open is this decision to redefining the capacity formula itself (R1), vs. only patching the R1/R2 calibration mismatch? | **Fully open to replacing the capacity formula entirely (may supersede R1).** |
| 2 | What is the intended play-feel for a typical adventuring load (light-medium armor + gear) on an average character? | **Moderate — noticeable penalty but forgiving, occasional Light/Moderate band.** |
| 3 | Is comparative research into other TTRPGs' encumbrance systems in scope? | **Yes — comparative research is expected and useful.** |

**Consequence for this document:** all five options from the 2026-09-09 brief remain live (none pre-eliminated by scope), comparative-system grounding is included below, and all quantitative tuning targets "moderate/forgiving, occasional Light/Moderate at average PC stat levels" as the design target — not the all-20 minimum-stat reference case alone.

---

## 2. Problem Restated

DEC-078's capacity sub-ruling (**R1**: `C = floor(HP/6)`) and threshold sub-ruling (**R2**: bands at cut-points 0.30 / 0.60 / 0.90 / 1.20 / 1.50) were both adopted in the same 2026-09-06 session, but R2's cut-points were calibrated against an **earlier candidate formula** (`C = floor((bpe+bee)/2)`), which produces roughly half the capacity that the actually-ruled R1 formula produces. This was recorded at the time as a "consequence flag" in the DEC-078 register cell, left open for the designer.

**Net effect:** real reference loads land roughly one full band lower than the R2 authors intended when they picked the cut-points.

A second, longer-horizon issue not previously flagged as part of this residual: HP has no fixed advancement ceiling (Invariant 11). A capacity formula that is **linear in HP** therefore grows without bound as a character advances, which will eventually make encumbrance mechanically irrelevant for sufficiently advanced characters regardless of where the bands sit today.

---

## 3. Comparative Research Summary

| System | Capacity basis | Growth shape | Relevance to Tiwas |
|---|---|---|---|
| GURPS | Basic Lift = ST² / 5 | **Superlinear** (quadratic in the governing stat) | Opposite direction from Tiwas' current concern — under GURPS, strength investment pays off *increasingly*. Notable because Tiwas' BToV-Madness creature conversions are GURPS-sourced (DEC-077.A). |
| D&D 5e | Carrying capacity = Strength score × 15 lb | Linear, but the governing stat is effectively capped (~20–30 in most play) | Structurally similar to Tiwas' current R1 (linear-in-stat), but safe *only* because the stat cannot run away. Tiwas' HP has no such cap. |
| Blades in the Dark | Fixed slot count (Light/Normal/Heavy = 3/4/5 slots) | None — flat, abstract, no weight math | Matches "Option D" (abstract slots) below. Represents the largest architectural departure from Tiwas' existing kg-based, granular design. |
| Dark Souls (video game) | Equip Load = percentage of a derived max, from a Vitality-like stat | Roughly linear-to-sub-linear, with soft breakpoints | Conceptually, Tiwas' existing `E = L/C` relative-band architecture **already matches this pattern**. The open question is the shape of `C(HP)`, not the band architecture itself, which needs no redesign. |

**Conclusion of comparative research:** Tiwas is not missing an architecture. The `E = L/C` relative-band model with named tiers is sound and has genre precedent (Dark Souls-style). The open decision is narrowly the **shape of the capacity function** and its **matching cut-points**.

---

## 4. Quantitative Analysis

### 4.1 Diagnosed Miscalibration (Current Ruled State)

Using the currently ruled formula (`C = floor(HP/6)`) and currently ruled bands (0.30/0.60/0.90/1.20/1.50), against a representative 25 kg "typical adventuring load":

| Build | HP | Capacity C (current R1) | E at 25 kg load | Resulting Band (current R2) |
|---|---:|---:|---:|---|
| All-20 (weak) | 240 | 40 kg | 0.625 | Moderate |
| All-50 (average 1d100 roll) | 600 | 100 kg | 0.25 | **Unencumbered** |
| All-80 | 960 | 160 kg | 0.156 | Unencumbered |

**Finding:** an average-stat PC carrying a realistic adventuring load never leaves Unencumbered under the currently ruled formula/band pairing. This does not match the "moderate, occasional Light/Moderate" target elicited in §1.

### 4.2 Candidate Capacity Formulas

Five candidates, drawn from the 2026-09-09 options brief, computed across a common HP range including two "extreme advancement" reference points to expose long-term scaling behavior. **Coefficients marked ⚑ are illustrative inventions by the author LLM for this session — not sourced from any prior investigation — chosen only to land near a comparable mid-range value so the shapes are directly comparable. They carry no evidentiary weight and are starting points for Tiwa's own tuning, not proposals.**

| Option | Formula | All-20 (HP 240) | All-50 (HP 600) | All-80 (HP 960) | Extreme (HP 4800) | Growth shape |
|---|---|---:|---:|---:|---:|---|
| **A — Status-quo, recalibrate bands only** | `C = floor(HP/6)` (unchanged) | 40 | 100 | 160 | 800 | Linear, unbounded |
| **B — Flat base + linear** ⚑ | `C = 10 + 0.1×HP` | 34 | 70 | 106 | 490 | Linear, damped slope, still unbounded |
| **C — Square-root damping** ⚑ | `C = 2.857×√HP` | 44 | 70 | 89 | 198 | Sub-linear; self-limiting at high HP |
| **D — Abstract slots** (Blades-style) | Fixed slot count, no kg math | n/a | n/a | n/a | n/a | Flat — abandons the kg-based model entirely |
| **E — Skill-Tier ladder** (DEC-107/DEC-112 idiom) | Lookup table indexed by a causing skill's Tier | Content-dependent | Content-dependent | Content-dependent | Content-dependent | Step function; decoupled from Body attributes |

### 4.3 Growth-Shape Comparison (full data table)

An inline line chart comparing Options A, B, and C was rendered during the chat session. The underlying data is reproduced here for the written record, since options D and E are not expressible on this axis (D has no formula; E requires an unauthored content table).

| HP | A: `HP/6` | B: `10 + 0.1×HP` ⚑ | C: `2.857×√HP` ⚑ |
|---:|---:|---:|---:|
| 120 | 20 | 22 | 31 |
| 240 | 40 | 34 | 44 |
| 480 | 80 | 58 | 63 |
| 600 | 100 | 70 | 70 |
| 960 | 160 | 106 | 89 |
| 1200 | 200 | 130 | 99 |
| 2400 | 400 | 250 | 140 |
| 4800 | 800 | 490 | 198 |

**Observation:** Option A climbs without limit (an extremely advanced character could theoretically carry 800+ kg). Option B climbs more slowly but is still unbounded. Option C visibly flattens at high HP — late-game capacity growth self-limits without requiring a manually authored cap.

---

## 5. Candidate Packages (Formula + Matching Bands)

Because threshold cut-points must be tuned against whichever formula is chosen, formulas and bands are presented here as paired packages rather than independent choices. Band sets marked ⚑ are illustrative recalibrations by the author LLM, not sourced values.

| Package | Formula | Matching band cut-points (Unenc/Light/Mod/Heavy/Over/Extreme) ⚑ | 25 kg @ HP 600 → Band | Reopens R1? | Table/GM friction |
|---|---|---|---|---|---|
| **A′** | `floor(HP/6)` (unchanged) | 0.15 / 0.30 / 0.45 / 0.60 / 0.75 | E=0.25 → Light | No — only R2 reopens | Lowest — same arithmetic, new numbers |
| **B** | `10 + 0.1×HP` | 0.15 / 0.30 / 0.45 / 0.60 / 0.75 | E=0.357 → Moderate | Yes | Low — still floor + arithmetic |
| **C** | `2.857×√HP` | 0.15 / 0.30 / 0.45 / 0.60 / 0.75 | E=0.357 → Moderate | Yes | Medium — one-time sqrt per character sheet, not a per-roll operation |
| **D** | Abstract slots | N/A — different architecture | N/A | Yes | Lowest in play, but breaks the kg-based ENC-F01 ruling and departs from Priority 1 (granular simulation) |
| **E** | Skill-Tier ladder | N/A — requires an authored lookup table | Content-dependent | Yes | Highest — new content-authoring burden; raises an unresolved "which skill governs this?" question |

---

## 6. Advisory Recommendation (Non-Binding)

**This section is the author LLM's advisory lean only. It is not a ruling, carries no authority, and should not be recorded as one.**

- **Package A′** (recalibrate bands only, keep R1's formula unchanged) is the lowest-friction fix and reaches the "moderate/occasional Light" target for typical loads at average PC stats. It does **not** address the unbounded late-game capacity growth identified in §2 and §4.3, which will likely resurface as a fresh residual once a high-advancement playtest character is fielded.
- **Package C** (square-root damping) addresses both the near-term calibration gap and the long-term unbounded-growth concern simultaneously, at the cost of a formula that is not pure floor-and-divide. Since it is computed once per character sheet rather than per roll, this does not add a resolution step to the Core Test Transaction.
- **Package B** sits between the two: fixes the immediate calibration gap, delays but does not eliminate the unbounded-growth concern.
- **Packages D and E** are not recommended for this closure pass: D abandons the already-ruled ENC-F01 kg-based clothing rule and the Priority-1 granularity commitment; E reintroduces the "new derived stat / new lookup table" pattern that DEC-078's original A1 sub-ruling explicitly rejected, and creates unresolved content-authoring dependencies.

---

## 7. Skill-Side Modifier Magnitudes (R3)

Not substantively re-examined in this session. The existing flat `−1 … −5` per-band ladder (DEC-078 R3) was convergent across the original 2026-09-01/02 advisory sessions and is not directly implicated by the capacity/threshold mismatch diagnosed here. **Advisory recommendation:** treat R3 as a separable, lower-priority decision unless Tiwa's chosen formula/band package changes the number of bands or their intended severity spacing.

---

## 8. Explicit Flags — Sourced vs. Invented Values

| Item | Status |
|---|---|
| R1/R2 calibration mismatch diagnosis | Sourced — DEC-078 register cell, 2026-09-06 closure annotation |
| Reference loads (10.8 kg / 19.5 kg military reference) | Sourced — Grok 4 rev1 investigation, cited in DEC-078 |
| Five option names (A–E) | Sourced — `tiwas-encumbrance-capacity-formula-options-brief-2026-09-09.md` |
| Coefficient `10 + 0.1×HP` (Option B) | **Invented this session** — illustrative only |
| Coefficient `2.857×√HP` (Option C) | **Invented this session** — illustrative only |
| Recalibrated band set `0.15/0.30/0.45/0.60/0.75` | **Invented this session** — illustrative only |
| Comparative-system figures (GURPS Basic Lift, D&D carrying capacity, Blades load, Dark Souls Equip Load) | Author LLM's general knowledge of published systems; not independently re-verified against primary rulebooks during this session |

---

## 9. Open Items — Not Resolved by This Document

- Final selection of capacity formula (A′ / B / C / D / E / other).
- Final numeric threshold cut-points, contingent on the formula selected.
- Whether R3 (Skill-side modifier magnitudes) is revisited as part of this closure or left as-is.
- Whether this closure formally reopens R1 (true for B/C/D/E; false for A′).
- Verification of the comparative-system figures in §3/§8 against primary sources, if Tiwa wants that level of rigor before deciding.

---

## 10. Required OpenCode Actions

1. Store this document verbatim under `investigations/` alongside `tiwas-encumbrance-capacity-formula-options-brief-2026-09-09.md`, cross-referenced from the DEC-078 register cell as a second stored advisory synthesis.
2. Annotate the DEC-078 register cell to note that this synthesis exists and remains **unruled** — do not infer, assign, or record any DEC number from this document's contents.
3. Before recording anything to the Decision Register on this topic, run the reconfirmation checklist in §11 past Tiwa explicitly, per standing OpenCode practice.
4. Do not treat §6's advisory lean as a designer ruling under any circumstance, including partial adoption.

## 11. Reconfirmation Checklist (OpenCode to run past Tiwa before any recording action)

- [ ] Confirm capacity formula selection: A′ (recalibrate only) / B (flat+linear) / C (sqrt-damped) / D (abstract slots) / E (Skill-Tier ladder) / a synthesis not listed here.
- [ ] Confirm exact numeric threshold cut-points for the chosen formula (the values in §5 are illustrative, not final).
- [ ] Confirm whether Skill-side modifier magnitudes (R3) are being revised in the same ruling or left unchanged.
- [ ] Confirm whether this ruling formally supersedes/reopens R1 as previously recorded (2026-09-06).
- [ ] Confirm the DEC number to be assigned and the exact register cell(s) to update.

---

**End of document.**
