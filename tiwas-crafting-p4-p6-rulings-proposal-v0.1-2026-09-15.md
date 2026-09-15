---
document:
  title: "Tiwas — Crafting P4/P6 Rulings Proposal: Tier-combination formula & Skill-Tier gate"
  version: "v0.1"
  status: "Non-canonical proposal. Rulings received 2026-09-15: Ruling I (P4) = Option A, Ruling II (P6) = Option A — recorded as DEC-141 and DEC-142 in the Decision Register. Design exploration only; not itself a DEC or a ruling. Pending promotion before any canonical status, OpenCode handoff, or playtest."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-15"
  last_modified_date: "2026-09-15"
scope_note: >
  This document consolidates, into two candidate rulings, the two decisive open items
  (P4 — Tier-combination formula; P6 — Skill-Tier gate) identified by the Wurm crafting
  robustness assessment Part 1 and empirically confirmed by Part 2's worked stress test.
  It reuses the Option A/B/C candidate set already carried by the stored crafting
  proposal v0.1 (section 5) and proposes gate text for P6 that mirrors the DEC-041
  pattern-precedent. It is a decision-support document, and it proposes; it does not
  rule. Sections are labelled REUSED (cites an existing DEC or stored proposal,
  unmodified) or PROPOSED (new, requires a ruling). Nothing in this document is
  Canonical, Ruled, or binding until Tiwa rules on it; any resulting ruling must pass
  the repository's formal promotion mechanism (the 8-step Promotion Rule, REQ-021)
  before acquiring canonical status.
---

# Tiwas — Crafting P4/P6 Rulings Proposal v0.1

## 0. Purpose, Scope, and Authority Status

**Rulings received (2026-09-15).** Tiwa ruled **Ruling I (P4) = Option A** and
**Ruling II (P6) = Option A**, both on the ground of simplification — verbatim:
*"Simplification. Can be expanded on later."* Neither ruling resolves P5 (out of scope),
the DEC-128 Q-R1 vs DEC-129 repair-ceiling reading (§5), or Ruling I-a's one-level-down
record-shape extension (§2.4) — those remain open. This document's own §2.3/§3.4 draft
text is now the operative statement of the adopted Option A content as ruled; the rulings
are recorded as **DEC-141** and **DEC-142** (non-canonical designer rulings) in the
Decision Register, and the register text takes precedence over this document's §2/§3 if
they ever diverge.

**Purpose.** Put before Tiwa, as a single decision document, the two crafting rulings the
robustness assessment identified as the highest-leverage open items blocking a determinate
crafting pipeline:

| Ruling | Open item (Part 1) | Consequence of not ruling |
|---|---|---|
| I. Tier-combination formula | P4 | No crafted result has a determinate Tier wherever two input Tiers combine; alloy/composite recipes stay illustrative only |
| II. Skill-Tier gate for crafting attempts | P6 | Nothing rules out a tier-ineligible crafter attempting any recipe today; the gate is house convention, not rule |

**Scope.** Covers P4 and P6 only. P5 (tool/fixture Tag preconditions) is identified but
deferred here — its pattern-precedent (DEC-114 R2) is noted in §5 for completeness, per
the user's scoping of this proposal. The DEC-128 Q-R1 vs DEC-129 repair-ceiling reading is
flagged in §5 but not resolved here.

**Authority status.** This document is advisory and non-canonical. It recommends; it does
not rule. Adopting either candidate requires Tiwa's explicit ruling, recorded per the
established designer-ruling practice, and any subsequent canonical status requires the
formal promotion mechanism. Recommendation language below is analysis, not authority.

---

## 1. Evidence Base

| Evidence | Source | What it establishes |
|---|---|---|
| P4 verdict: "one scoped, precedent-guided ruling" away | Part 1 §5 P4, §7, §8 | The Item-family record shape exists (DEC-128 Q1); only the multi-input Tier arithmetic is unruled |
| P4 empirical demonstration | Part 2 §3, §10 | "The test cannot produce a determinate Steel Lump Tier without Tiwa choosing among Option A/B/C" — mutually exclusive candidates, no determinate output without a ruling |
| P6 verdict: "precedent exists, not yet applied to crafting" | Part 1 §5 P6, §7, §8 | DEC-041(1) is the exact reusable pattern |
| P6 empirical demonstration | Part 2 §6 | The absence of a ruled gate means "a Tiwas table running this exact scenario right now would have no textual basis to say 'no, you can't even try that yet'" |
| Resolution-machinery robustness | Part 2 §4, §5, §10 | The Extended-Test creation engine is fully Ruled (DEC-128 Q2 / DEC-067/068/070); only the output arithmetic fed into it is open |
| Pattern-precedents | DEC-041(1)+(6); DEC-114 R2 | Both a Skill-Tier gate and a Tag-presence gate already exist in the corpus for other Effects |

---

## 2. Ruling I — P4: Tier-Combination Formula for Crafted Results (PROPOSED)

### 2.1 Where the gap lives

The Core Test **resolving** a crafting attempt is fully Ruled (DEC-006; margin-accumulation
Extended Test per DEC-128 Q2 / DEC-067/068/070; neutral-failure per DEC-068; GM-set
threshold per DEC-070). The unruled piece is only the **output arithmetic**: given the input
Material/Component Tiers and the acting Crafting Skill's Skill-Tier, what Tier does the
produced record receive? No existing DEC specifies this for any multi-input combination, and
Part 2 demonstrated empirically that the test cannot produce a determinate output Tier
without Tiwa picking one candidate (Part 2 §3).

### 2.2 Candidate set (REUSED — crafting proposal v0.1 §5)

| Option | Formula | Rationale | Risk |
|---|---|---|---|
| **A (recommended)** | `Result Tier = min(Crafting Skill-Tier, max(input Tiers))` | Mirrors the DEC-107 idiom (acting Skill-Tier as the hard ceiling on produced severity) and DEC-041's Skill-Tier gate discipline. Simple, one comparison. | A single high-Tier input with a low-Tier Skill wastes the input's Tier — may or may not be desired realism |
| B | `Result Tier = min(Crafting Skill-Tier, floor(average(input Tiers)))` | Mirrors DEC-005's Cap formula (floored average) — thematically consistent with the Core's own Tier math | Punishes mixing a high-Tier input with low-Tier filler |
| C | GM Fiat, guided by `max(input Tiers)` as a floor | Matches the DEC-130 / DEC-035.A cl.6 universal-Fiat override precedent | Least mechanically determinate; heaviest GM burden for a "simulation-grade" system |

The candidates are mutually exclusive and each is individually defensible; Part 2's finding
is that without a choice among them, the output Tier is undeterminate. This proposal (like
v0.1 and Part 2) **uses Option A as the working default** — a candidate, not a ruling.

### 2.3 Draft rule text (PROPOSED)

> A crafted Material, Component, or Item record's **Tier at creation** equals
> `min(acting Crafting Skill's Skill-Tier, max(contributing input Tiers))` – the acting
> Skill-Tier is the hard ceiling; the best single input bounds the floor.
>
> For a single-input step with no combination (e.g., smelting one Material stack),
> `max(input Tiers)` degenerates to that input's own Tier.
>
> Created records are base-equal: `Magnitude = Tier` at creation (DEC-128 Q1 / DEC-129,
> unchanged).

### 2.4 One-level-down record extension (PROPOSED — fold or defer)

Part 2 (Step 1) flagged that no DEC currently states a gathered raw **Material** carries a
Tier/Magnitude record at all — DEC-128 Q1 is scoped to *Items*. The stress test proceeded by
assuming the same record shape one level down the pipeline (a low-risk extension, per its own
finding). Two ways to close this:

- **(a) Fold** — rule that Materials and Components use the same Item-family record with a
  `Type: Material | Component | Item` classifier (v0.1 §2, itself PROPOSED). One ruling
  closes the record shape for the whole pipeline; the P4 formula then applies identically at
  every level.
- **(b) Defer** — rule P4 for Items only and leave Material-Tier assignment to content
  judgment / GM Fiat (DEC-130) for now, as the stress test itself did.

**Recommendation:** (a) is near-free — the record shape already exists and DEC-128 Q1 already
placed the Item record outside the DEC-115/117 `Z = −Y` schema — and is recommended. It can
be ruled separately from 2.3 if Tiwa prefers to keep the two rulings decoupled.

---

## 3. Ruling II — P6: Skill-Tier Gate for Crafting Attempts (PROPOSED)

### 3.1 Where the gap lives

Part 2 (Step 5): no rule exists that a crafter may only attempt recipes within their
Skill-Tier reach. Its worked assumption — "a Steel Longsword requires Weaponsmithing
Skill-Tier ≥ 2 to attempt at all" — is house convention, not a rule. The consequences are a
*real, currently-absent guardrail*: nothing bars a Tier-1-only crafter from beginning the same
Extended Test.

### 3.2 Pattern-precedent to copy (REUSED — DEC-041 item (1))

> *(DEC-041 item (1), verbatim)* A Location Index is generated only when (a) the roll is
> promoted to Location-Tier 1/2+ per DEC-040/Item 3, **AND** (b) the promoting roll comes
> from a **Skill-Tier 2+ (Advanced)** skill. Base/untrained skills are **Skill-Tier 1** (per
> Canonical §5.1/§5.3) and can **never** trigger a location roll for any
> location-referencing Effect, under any circumstances.

DEC-041 item (6) further establishes that its gate "applies uniformly to **all**
location-referencing Effects." P6 generalizes the *same discipline* to crafting attempts —
which is new territory and therefore requires a new ruling, not a citation.

### 3.3 Candidate designs

| Option | Content | Effect |
|---|---|---|
| **A (recommended)** | Each recipe carries an authored `min_skill_tier` gate (recipes are content-authored per the DEC-077.A bar); the acting Crafting Skill's Skill-Tier must be ≥ the gate to attempt the Extended Test. A recipe with no gate authored is treated as gate 1, attemptable by any base/untrained skill (Skill-Tier 1) | Directly matches what both assessment reports and the v0.1 recipe shape already assume; no derived formula; reuses the DEC-077.A authoring discipline |
| B | Gate on the target/current output Tier instead: to craft at Tier Y, acting Skill-Tier ≥ Y | Fewer authored values, but conflates recipe complexity with output materiality — a Tier-1 item could still be arbitrarily hard to make |
| C | A and B combined (both `min_skill_tier` and `Skill-Tier ≥ output Tier`) | Most guardrails; most constraining; more verbose content-authoring |

**Recommendation:** Option A. It matches the assumption both assessment parts already made,
reuses the DEC-077.A content-authoring bar, imposes no derived formula, and leaves the
output-Tier ceiling to the P4 formula (§2.3) where it already lives statically. The Upgrade
attempt gate from v0.1 §8 — *acting Skill-Tier ≥ the record's current Tier* — can be folded
into the same ruling for a single, uniform gate statement.

### 3.4 Draft rule text (PROPOSED)

> A Crafting Extended Test for a given recipe requires the acting Crafting Skill's
> **Skill-Tier to be ≥ the recipe's authored `min_skill_tier`**. Recipes are content-authored
> (DEC-077.A discipline); a recipe with no `min_skill_tier` authored defaults to gate 1,
> attemptable by any base/untrained skill (Skill-Tier 1). Base/untrained skills are Skill-Tier
> 1 (Canonical §5.1/§5.3).
>
> Attempting to **Upgrade** a record requires the acting Skill's Skill-Tier ≥ the record's
> **current Tier** (reusing v0.1 §8's wording).
>
> GM Fiat remains available per DEC-130 ("bounded universality"): gates like these are not
> part of the Locked Canonical Core, so Fiat may waive or adjust them; it may not override
> the Core disciplines (Cost = natural roll, Overflow, HP=0, no-DoT) that DEC-130 itself binds.

---

## 4. Interaction Checks — Why the Two Pair Cleanly

| Check | Vertex DEC | Result |
|---|---|---|
| Produced Tier ceiling | DEC-107, DEC-041 | P4/Option A already makes acting Skill-Tier a static ceiling on produced Tier; P6 adds the *attempt* control. Together they reproduce the dual layer — gate on attempt, ceiling on result — without a second engine |
| GM Fiat | DEC-130 | Both rules sit outside the Locked Canonical Core; Fiat can waive/adjust them (bounded universality), and this is stated explicitly rather than left implicit |
| Invariant 6 (natural roll) | Invariant 6 | Neither ruling modifies, adds to, or subtracts from the natural d100 roll — all arithmetic is applied to Tiers and records after the roll resolves |
| Invariants 17/18 | Invariants 17–18 | No second resource/progression economy (Tier arithmetic post-processes the already-Ruled Core Test) and no parallel resolution engine (the Extended Test remains DEC-067/068/070 machinery); consistent with Part 1 §7 and v0.1 §7 |
| Upgrade / Repair cycle | DEC-128 Q3, DEC-129 | P4-relevant Tiwas: a clean Upgrade keeps `Tier = Magnitude`; a failed Upgrade (DEC-128 Q3) breaks equality; the Part-2 chain showed Repair-restores-to-Tier with zero assumptions (pending the Q-R1/DEC-129 reading note in §5) |

---

## 5. What This Document Does NOT Rule

| Item | Reason | Pointer |
|---|---|---|
| P5 — tool/fixture Tag preconditions | Out of scope per the user's scoping of this proposal; pattern-precedent exists | Part 1 §5 P5, §9 rec 1; DEC-114 R2 |
| DEC-128 Q-R1 vs DEC-129 — Original-Tier vs current-Tier Magnitude-repair ceiling | Interpretive nuance surfaced by the Part-2 assessment; not a P4/P6 item; flagged for Tiwa separately | Part 2 §9; advisory annotation on DEC-081.A |
| Material acquisition / EQ-3A wealth-economy fork | Already explicitly open; independent of these two rulings | v0.1 §11 item 3; DEC-081.A Open 3 |
| Completion-threshold scaling for the crafting Extended Test | DEC-070 already leaves the threshold to GM discretion; v0.1 §11 item 2 | v0.1 §6, §11 |
| Recipe authorship cadence / universal input-count formula | Confirmed as pure content-authoring (DEC-077.A), not derivable by formula | v0.1 §9, §11 item 4 |

---

## 6. Required Rulings Checklist (for Tiwa)

Each line is a separate designer ruling; DEC assignment and register recording follow only
if and as Tiwa directs.

- [x] **Ruling I (P4):** Option A adopted — `min(Crafting Skill-Tier, max(input Tiers))` (§2.3). **Recorded as DEC-141 (2026-09-15).**
- [ ] **Ruling I-a (P4 extension):** fold the Material/Component record-shape extension
      (§2.4 Option a) or defer it (§2.4 Option b) — **not ruled; remains open**
- [x] **Ruling II (P6):** Option A adopted — recipe-authored `min_skill_tier` gate
      (§3.3/§3.4), with the v0.1 §8 Upgrade-gate wording folded in. **Recorded as DEC-142 (2026-09-15).**
- [ ] *(adjacent, flagged — not this proposal's item)* confirm or defer the Q-R1 vs DEC-129
      Magnitude-repair-ceiling reading (§5) — **not ruled; remains open**

**What happens if Tiwa rules:** assign DEC number(s) per established recording practice;
record the outcome in the Decision Register under the Equipment/crafting context,
cross-referencing DEC-081.A (Open 3), DEC-128/129, DEC-041, DEC-114 R2, DEC-107, DEC-130;
if promotion to Canonical is desired, run the formal promotion mechanism (the 8-step
Promotion Rule, REQ-021 in `governance/status-model.md`); do **not** mark any part of this
document Canonical before that process.