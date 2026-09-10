---
document:
  title: "Encumbrance Capacity Formula — Options Brief (DEC-078 Residual)"
  version: "1.0"
  status: "Advisory options analysis — Non-Canonical. Not a ruling. No DEC assigned."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-09"
  last_modified_date: "2026-09-10"
handoff:
  from: "Claude Sonnet 5 (advisory session with Tiwa)"
  to: "OpenCode (big-pickle) — for joint review with Tiwa; no recording action requested at this time"
  decision_owner: "Tiwa (human designer/ruling authority)"
  register_dependency: "_consolidation/decision-register.md — DEC-078 (Encumbrance Model)"
---

> **Assessment & Storage record (added 2026-09-10 by OpenCode / big-pickle):** Stored at
> `investigations/tiwas-encumbrance-capacity-formula-options-brief-2026-09-09.md` per Tiwa's
> instruction. Assessment pass (factual/documentary consistency against the live repository):
> all cited DEC-078 sub-rulings (R1 `C = HP/6`; R2 band cut-points 0.30/0.60/0.90/1.20/1.50;
> R3 ladder −1…−5), the "Carried-open items ruled 2026-09-06" annotation, the consequence
> flag, the supersession of `C = floor((bpe+bee)/2)`, the ENC-F01 annotation, the arithmetic
> tables (all-X attributes → C = 40/100/200 kg for X = 20/50/100), and the canonical
> references (§4 HP = sum of 12 Body attributes; §11.2 no fixed upper bound; Invariant 11;
> bpe/bee/bsx/bex) were verified accurate. No material errors found. Minor note: the register
> records R1 as "C = HP/6" with flooring applied globally (DEC-002 / Invariant 4); the brief's
> `C = floor(HP/6)` rendering is equivalent. Storage and assessment confer no authority: this
> document remains a non-canonical advisory input; no DEC is inferred and no ruling is made by
> its recording.

# Encumbrance Capacity Formula — Options Brief

## 0. Status and Authority

This document is an **advisory synthesis** produced by Claude Sonnet 5 at Tiwa's request, consolidating the full findings of a single chat session concerning the DEC-078 encumbrance capacity formula. It contains **no ruling, no DEC number, and no recording action**. Per standing project governance (`governance/authority.md`, `governance/status-model.md`, Roadmap §24 LLM Governance Rules), this document:

- does not modify, supersede, or reopen DEC-078 or any of its sub-rulings (R1, R2, R3) on its own authority;
- presents evidence-classed options only (per the Mechanical Fact / Empirical Finding / Designer Ruling / Recommendation / Architectural Constraint vocabulary);
- is intended as **input to a joint Tiwa + OpenCode decision session**, per Tiwa's stated intent ("I will decide this with OpenCode"). OpenCode should treat this file as a discussion aid and verify all cited register content against the live repository before any ruling is recorded.

## 1. Background

DEC-078 (Encumbrance Model) closed its carried-open items on 2026-09-06 with three sub-rulings:

| Sub-ruling | Content |
|---|---|
| R1 | Capacity formula: `C = floor(HP/6)` kg, where HP = sum of all 12 Body attributes |
| R2 | Six relative-`E` bands (`E = L/C`) at cut-points 0.30 / 0.60 / 0.90 / 1.20 / 1.50 |
| R3 | Skill-side penalty ladder per band (Tier-1 → −1 ... Tier-5 → −5), expressed as the Encumbered Condition |

R1 superseded an earlier candidate formula, `C = floor((bpe+bee)/2)`, which the R2 cut-points were originally calibrated against. The DEC-078 register entry itself flags, in its own "Consequence flag" annotation, that this substitution was never re-checked: R1 and R2 were closed as separate sub-rulings in the same session without confirming that the cut-points still carry their intended real-world correspondence once the underlying capacity roughly doubled.

This document addresses that residual, plus a follow-on question raised by Tiwa during the session: whether the capacity formula should continue to target a literal "body weight in kg" plausibility check at all, and if not, what alternative formula designs are available.

## 2. Arithmetic Verification

For a character with every Body attribute equal to average value `X`: `HP = 12X`, so `C = HP/6 = 2X`.

| Average Body attribute (X) | HP | C = HP/6 |
|---:|---:|---:|
| 20 | 240 | 40 kg |
| 50 (existing playtest calibration reference, v6 scaffold) | 600 | 100 kg |
| 100 | 1200 | 200 kg |

This table corrects an arithmetic slip raised mid-session (a claim that avg-100 attributes yields C ≈ 50 kg). The verified value is 200 kg. The direction of the concern reverses accordingly: linear scaling under R1 does not produce an implausibly *low* value at the high end — it produces a value that grows without limit as attributes advance, since Body attributes have no fixed ceiling (Canonical Rules §11.2 / Invariant 11: General XP may raise a Skill or Attribute above its generation-time Cap with no fixed upper bound).

## 3. Reframing: Body-Weight Plausibility Is No Longer the Design Target

Tiwa confirmed in-session that the "does C read as a plausible adult body weight in kg" framing is retired. The residual therefore splits into two independent, still-open design questions, addressed by the options below:

1. **Shape** — should carrying capacity scale linearly, faster-than-linearly, slower-than-linearly, or not continuously at all, as attributes/Skills advance?
2. **Input** — should capacity draw on all 12 Body attributes (current `HP`, which includes attributes with no conceptual link to load-bearing, e.g. bsx Grace, bex Poise), a narrower Power/Endurance subset (restoring the original A1 "Endurance-coded" direction), or a Skill rather than raw attributes at all?

## 4. Research Basis

The following existing tabletop and video-game systems were consulted for precedent. This is background research only; no external system's numeric values are imported into Tiwas (consistent with the standing non-import discipline established for the BToV-Madness GURPS conversion work, DEC-085 cl.3).

| System | Formula / Model | Shape | Input |
|---|---|---|---|
| GURPS — Basic Lift | `BL = ST² / 10` (kg) | Quadratic | Single stat |
| GURPS house-rule "Quad ST" | Same shape; adopted specifically to widen the spread between weak and strong characters at the high end | Quadratic | Single stat |
| D&D 5e (variant encumbrance) | `Capacity = STR score × 15` (lb) | Linear, no floor | Single stat |
| Dark Souls (I–III) | `Max Equip Load = 40 + Endurance`; `Encumbrance % = carried / max`, banded at 25/50/70/100% | Flat base + linear | Single stat |
| Blades in the Dark / Forged in the Dark | `Load = 1–9` abstract slots; each item costs 1–3 slots by authored/GM judgment; no kg value exists anywhere in the system | Discrete, non-numeric | Authored per item, no formula |
| Pathfinder 1e / BRP / Mythras (Call of Cthulhu lineage) | STR (± SIZ) lookup table | Table-driven, non-linear | 1–2 stats, no closed-form formula |

Two findings are directly load-bearing (no pun intended) for the options below:

- **Dark Souls already implements a structure nearly identical to Tiwas's existing `E = L/C` banded-percentage model** — the closest external precedent to what DEC-078 R1/R2 already do. Its low-end floor problem is solved with a flat additive offset, not a curve.
- **Blades in the Dark demonstrates a fully viable, well-tested alternative that abandons continuous mass entirely.** This is presented as a paradigm-shift option, not a refinement.

## 5. Options

Five options are presented. Options 1–4 were identified and evaluated across the session; Option 5 is an original design proposal (not sourced from an external system) that reuses an idiom already established elsewhere in Tiwas's own ruled content (DEC-107, DEC-112). Per Tiwa's explicit framing, compatibility with the current DEC-078 text is **not** a constraint on Option 5 or on any option below — all five are presented on their design merits, with compatibility cost noted separately per option.

All kg-based options are anchored so that the existing 50-average playtest baseline (HP = 600) continues to yield approximately C = 100 kg, to keep the "typical adventurer" reference point stable across candidates for comparison purposes only. Anchoring is not a constraint on the eventual choice.

### 5.1 Option 1 — Status Quo (`C = HP/6`), Recalibrate Bands Only

No change to R1. Only R2's cut-points would be revisited, re-anchored against what `HP/6` actually outputs.

| Avg Body attribute (X) | HP | C |
|---:|---:|---:|
| 20 | 240 | 40 kg |
| 50 | 600 | 100 kg |
| 100 | 1200 | 200 kg |

- **Resolves:** the R1/R2 consistency gap (Section 1), via a band recalibration pass — no formula change.
- **Leaves open:** attribute-dilution (Section 3, Input axis); unbounded high-end growth (Section 3, Shape axis).
- **Compatibility cost:** lowest of all five — amends R2 only, R1 stands.

### 5.2 Option 2 — Flat Base + Narrow Linear Stat (Dark Souls model)

`C = Base + (bpe + bee)`, solved at the 50-average anchor with `Base = 40`, multiplier `1`, giving `C = 40 + 0.6 × (bpe + bee)`.

| Avg bpe = bee (X) | bpe + bee | C |
|---:|---:|---:|
| 1 (minimum roll) | 2 | 41.2 kg |
| 20 | 40 | 64 kg |
| 50 | 100 | 100 kg |
| 100 | 200 | 160 kg |

- **Resolves:** both axes. The flat base guarantees a non-degenerate floor without curve math; restricting the input to bpe/bee restores DEC-078's original A1 "Endurance-coded" direction and removes Grace/Poise/Reflexes dilution.
- **Leaves open:** growth is still linear past the base, so the ceiling remains technically unbounded at extreme advancement, only slower than Option 1.
- **Compatibility cost:** amends R1 (formula and input) and requires R2 recalibration; R3's penalty-ladder shape is unaffected.
- **Precedent:** direct structural match to Dark Souls' Equip Load formula — the most externally battle-tested option in this set.

### 5.3 Option 3 — Square-Root Damping of HP

`C = k × √HP`, solved at the 50-average anchor with `k ≈ 4.08`.

| Avg X | HP | C |
|---:|---:|---:|
| 20 | 240 | 63 kg |
| 50 | 600 | 100 kg |
| 100 | 1200 | 141 kg |
| 150 | 1800 | 173 kg |

- **Resolves:** the unbounded-growth axis directly — the only option in the 1–3 set where high-end growth decelerates. Also raises the low-end floor relative to Option 1.
- **Leaves open:** dilution — still built from all 12 Body attributes, unchanged input from R1.
- **Compatibility cost:** amends R1's formula only (same input source, HP); R2 recalibration still required.
- **Precedent:** no single named TTRPG source; this is the general diminishing-returns curve family used broadly for unbounded stat scaling in video-game design, not lifted from one specific system.

### 5.4 Option 4 — Discrete Abstract Load Slots (Blades in the Dark model)

Replaces `C` in kg with a small integer count of Load Slots derived from a Body-attribute band; items are authored with a slot cost (1–3) rather than a kg mass. Illustrative banding (final values are content-authoring, not fixed by this option):

| Avg Body attribute band | Load Slots |
|---|---:|
| Very Low (≤ 25) | 3 |
| Low–Average (26–60) | 5 |
| High (61–90) | 7 |
| Very High (91+) | 9 |

`E` and its band structure are replaced by named tiers (e.g. Light / Normal / Heavy / Encumbered) driven by slots-used vs. slots-available, rather than a computed ratio.

- **Resolves:** both axes permanently — with no continuous kg conversion, neither dilution nor unbounded scaling is expressible as a problem.
- **Leaves open:** this is a full rearchitecture, not an amendment. R1 (formula), R2 (bands), R3 (penalty ladder tied to `E`), and the `L`-in-kg framing (including ENC-F01, "clothing counts toward load") would all require fresh rulings, not amendments. Also forfeits whatever granular-simulation fidelity the kg model offered under Locked Priority 1 (granular physical simulation where warranted).
- **Compatibility cost:** highest of the five — effectively a new DEC-078 rather than a revision.
- **Precedent:** Blades in the Dark's Load system (Forged in the Dark SRD) — a shipped, widely-played design.

### 5.5 Option 5 (Original Proposal) — Skill-Tier-Gated Capacity Ladder

Not sourced from an external system. Sourced from Tiwas's own existing design idiom: DEC-107 ties Effect/Wound severity to the Skill-Tier of the causing skill; DEC-112 ties Location-Tier granularity to acting Skill-Tier via an authored ladder. No currently-ruled subsystem ties encumbrance to a Skill — it remains the one physical-simulation subsystem rooted purely in raw rolled Attributes rather than trained investment. This option closes that asymmetry by making capacity a function of a designated carrying Skill's Tier, using the same ladder shape as DEC-112:

| Skill Tier | Capacity |
|---:|---:|
| 1 (base/untrained) | 30 kg |
| 2 (Advanced) | 60 kg |
| 3 | 100 kg |
| 4 | 160 kg |
| 5+ | 250 kg (GM Fiat may extend further, consistent with DEC-130's bounded-universality treatment) |

Implementation would require designating a governing Skill — either reusing an existing Tier-1 Body skill (e.g. Brawn, from bpe) or authoring a new lineage (e.g. "Hauling").

- **Resolves:** both axes, and additionally shifts encumbrance capacity onto the same "earned through play" axis (Failure XP, Advanced Skill creation) that governs the rest of Tiwas's Tier-driven subsystems, rather than raw attribute-roll luck.
- **Leaves open:** which Skill governs the ladder; authoring the ladder's exact values (a content-authoring task of the same kind as DEC-112's granularity ladder).
- **Compatibility cost:** medium — structurally different from R1 (Skill-based, not Attribute-based) but reuses an already-Ruled mechanical pattern (Tier-to-value lookup) rather than inventing a new one.

## 6. Comparative Summary

| # | Option | Resolves dilution | Resolves unbounded growth | Compatibility cost | Precedent |
|---|---|---|---|---|---|
| 1 | Status quo (`HP/6`), bands only | No | No | Lowest — R2 only | D&D 5e (linear, no floor) |
| 2 | Flat base + narrow linear | Yes | Partial (slower, still unbounded) | Low — amends R1 input/shape, R2 | Dark Souls |
| 3 | `k√HP` | No | Yes | Low — amends R1 shape only, R2 | Diminishing-returns curve family (video games) |
| 4 | Abstract Load Slots | Yes | Yes | Highest — reopens R1/R2/R3/ENC-F01 | Blades in the Dark |
| 5 | Skill-Tier ladder | Yes | Yes | Medium — new input axis (Skill, not Attribute), reuses Tiwas's own Tier-lookup idiom | Original proposal (DEC-107/DEC-112 pattern) |

## 7. Cross-Cutting Dependency

Options 1–3 all still require the R2 band-recalibration pass identified in Section 1 — none of the three changes to R1's formula shape resolve the cut-point mismatch on their own; they only change what gets fed into `E = L/C`. Options 4 and 5 do not have this dependency in the same form: each replaces the existing `E`/band structure with its own threshold design (slot counts for Option 4; capacity-per-tier for Option 5), so whichever is chosen would need its own threshold-setting pass rather than a recalibration of the existing one.

## 8. Required OpenCode Actions

1. **No recording action requested at this time.** This document is discussion input only.
2. When Tiwa and OpenCode select an option (or a hybrid, or a sixth alternative not listed here), OpenCode should verify this document's citations against the live register (`_consolidation/decision-register.md` DEC-078 cell) before drafting any formal ruling text, since this document was authored from conversational context and has not itself been cross-checked against the live repository.
3. Any adopted option should be recorded as an amendment to DEC-078 (or, if Option 4 is selected, potentially as a new DEC given the scale of the rearchitecture — OpenCode's judgment, per the DEC-035.A/DEC-035.B/DEC-077.A amendment-row precedent for amendments, vs. the DEC-118/DEC-135-style new-DEC precedent for supersessions), following the standard 8-step Promotion Rule if and when canonical status is ever sought — DEC-078 as a whole remains non-canonical regardless.
4. If a hybrid is selected (e.g., Option 2's flat-base-plus-narrow-input combined with Option 3's square-root shape — `C = Base + k√(bpe+bee)` — raised as a possibility during the session but not independently tabulated here), OpenCode should flag that as a sixth, unworked candidate requiring its own numeric table before recording.

## 9. Reconfirmation Checklist (for the Tiwa + OpenCode session)

- [ ] Confirm which axis (Shape, Input, both, or neither) is the actual design priority.
- [ ] Confirm whether unbounded high-end growth (a consequence of uncapped Attribute/Skill advancement, Canonical §11.2) is an accepted feature (heroic-power-fantasy framing, Locked Priority 2) or a defect to be damped.
- [ ] Confirm whether Encumbrance should remain Attribute-driven or move to Skill-driven (Option 5's premise).
- [ ] If Option 1, 2, or 3 is selected: schedule the R2 band-recalibration pass as a follow-on item.
- [ ] If Option 4 or 5 is selected: confirm scope as a DEC-078 amendment vs. a new DEC.
