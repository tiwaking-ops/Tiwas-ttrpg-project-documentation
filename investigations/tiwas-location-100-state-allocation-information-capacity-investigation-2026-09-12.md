---
document:
  title: "100-State Location Index — Allocation and Information-Capacity Investigation"
  version: "1.0"
  status: "Investigation brief — Advisory / Non-canonical. Not a ruling. No DEC inferred. Produced 2026-09-12 per Tiwa's instruction following the DEC-136 rulings. Candidate allocations are reference material for Tiwa's content-authoring under DEC-077/DEC-112 L-009/L-010, not adopted content."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-12"
  last_modified_date: "2026-09-12"
---

# 100-State Location Index — Allocation and Information-Capacity Investigation

Covers the proposal's **Investigation 1 (Information Capacity)** and **Investigation 2
(Numerical Allocation)** (`investigations/Tiwas TTRPG — Proposed Hierarchical Location
Architecture Report.md` §30), the proposal's §25 "Numerical Allocation Is a Separate
Investigation" open questions, and **LOC-I16** ("Numerical Location Index allocation
requires separate probability investigation").

## 0. Governance Notice

- Advisory/non-canonical: **no DEC is inferred and nothing here is ruled or assigned.**
- Produced at Tiwa's instruction in the same session as the **DEC-136** designer rulings
  (recorded in `investigations/tiwas-hierarchical-location-architecture-open-items-designer-rulings-2026-09-12.md`).
- The candidate allocation tables are **reference material for Tiwa's content-authoring**
  (DEC-077/DEC-077.A). Advisory models do not author definitive templates; Tiwa authors,
  accepts, edits, or rejects. Adoption, if any, is a separate human/designer step.
- Anchor rulings already in force and treated as fixed here: **DEC-014** (Zero-Step
  provider, read-only, no player choice), **DEC-041** (Skill-Tier ≥ 2 gate,
  within-zone weighting intent), **DEC-100** (Tier-1 quartiles 1–25 Legs, 26–50 Torso,
  51–75 Arms, 76–100 Head), **DEC-112** (L-003 single-source; L-004 per-creature
  templates; L-005 no cap; L-008 parity laterality; L-010 allocation deferred to
  content-authoring), **DEC-136** (L-003/L-011 confirmed for all Effects; no secondary
  roll; unbounded Location Tier).

## 1. Purpose

Establish, for content-authoring and playtest use:

1. the **information-capacity bound** of the 100-state Location Index under the
   hierarchical address model;
2. a **candidate in-zone allocation** for the four Tier-1 zones, consistent with the
   locked quartiles and the no-secondary-roll constraint;
3. the resulting **probability layer** (what each state, node, address, and laterality
   share actually costs);
4. answers to the proposal §25 open questions and verification of LOC-I16.

## 2. Size of the problem

| Quantity | Value | Source |
|---|---|---|
| Index states | exactly 100 (`|Ω| = 100`), equiprobable | DEC-014 (d100) |
| Tier-1 zones | 4 (Head / Torso / Arms / Legs) | DEC-100 |
| States per Tier-1 zone | exactly 25 (frozen quartiles) | DEC-100 |
| Secondary roll | none (any tier) | DEC-136 R1 → DEC-112 L-011 |
| Laterality | parity decode of Zero-Step output (odd/left, even/right); **no state cost** | DEC-041(3), DEC-112 L-008 |
| Location Tier | unbounded (no architectural cap) | DEC-136 R2 → DEC-112 L-005 |
| Terminal leaves per template | ≤ 100 (see §3) | derived |

## 3. Information-capacity analysis

1. **Total budget = 100 equiprobable cells.** Under the single-source deterministic
   model, every resolution is a subset of the d100's 100 rows. No roll can ever encode
   more than 100 distinct outcomes, and no mechanism (secondary roll, re-roll,
   GM-modifier) may add outcomes without violating L-003/L-011/Invariant 18.

2. **Depth is free; leaves are not.** An internal (branching) node consumes **no**
   states — it re-partitions the states of its parent. Only the **terminal (leaf) level
   of a template** consumes probability mass. Therefore a template of Tiers 6–12 is
   structurally unproblematic **as long as the number of distinct terminal (leaf)
   addresses across the whole template is ≤ 100.** This directly answers proposal
   §25.9 and LOC-I16: the 100-state constraint is a **leaf-count constraint**, not a
   depth constraint.

3. **Leaf probability is uniform at full depth: 1% each.** When a resolution truncates
   at a node (Skill-Tier/Location-Tier produces a coarser address), the node's
   probability = (number of states under it) × 1%. Skill-Tier changes the **read
   depth**, never the state weights. Probabilities of an address are therefore
   **stable under changing Skill-Tier** — a property worth stating explicitly because
   DEC-113/DEC-036-era playtest assumptions predated the hierarchy.

4. **The hard content bound.** `|Ω| = 100` means a template wanting **more than 100
   distinct terminal addresses cannot be represented faithfully** — it must coarsen, or
   adopt unequal probabilities (rejected: equiprobable natural results), or use a
   secondary roll (removed: DEC-136 R1). This is the operational form of proposal risk
   §34.2.1 ("the 100-state Location Index imposes a hard information limit") and §34.2.3
   ("Human anatomy may require more authored branches than the d100 can represent
   distinctly"). **Finding:** 100 leaves is ample for combat-relevant anatomy (see the
   candidate tables: ~70 anatomical leaves + reserves), and no Tier-1–12 semantic ladder
   currently planned exceeds it.

5. **Laterality costs zero states.** L-008 decodes side from the Zero-Step output's
   digit parity (odd/left, even/right). Each node's states partition implicitly into
   left (odd) and right (even) halves; **no separate left/right leaf duplication is
   needed.** Consequence: per-side granularity of a node = (node states)/2, and
   left + right together still sum to the node's full allocation. Laterality is a
   **partition of the existing budget, not an addition to it**.

6. **Midline structures need no side.** Heart, Spine, Sternum, and other midline organs
   occupy their own states and resolve as "central" regardless of the parity bit. The
   parity decode labels strike-side for lateral structures; it neither excludes nor
   duplicates midline states. Content-authoring nicety, not a rule change.

## 4. Candidate in-zone allocations (Tier 1 → Tier 2+)

Three constraints are honoured: each zone sums to **25**; states are contiguous within a
zone (`1–25`, `26–50`, `51–75`, `76–100`); the four zones partition all 100 states.
Values are counts of Index states; attached to a template, each count becomes a fixed
list of state numbers. **Candidate only — content-authoring reference, not adopted.**

### 4.1 Legs — states 1–25

| Structure | States | Sub-structure → states |
|---|---|---|
| Thigh | 4 | — |
| Lower Leg | 5 | — |
| Knee | 3 | — |
| Foot | 8 | Hallux 2 · 2nd–5th toes 4 · Midfoot/Heel 2 |
| Ankle | 1 | — |
| Femoral/internal | 2 | — |
| Reserve | 2 | — |
| **Zone total** | **25** | |

### 4.2 Torso — states 26–50

| Structure | States | Sub-structure → states |
|---|---|---|
| Chest | 10 | Heart 3 · Lungs 4 · Sternum/Ribs 1 · Spine 1 · reserve 1 |
| Abdomen | 9 | Liver 3 · Stomach 2 · Intestines 3 · Kidneys 1 |
| Pelvis | 3 | — |
| Groin | 1 | — |
| Spine/Back | 1 | — |
| Reserve | 1 | — |
| **Zone total** | **25** | |

### 4.3 Arms — states 51–75

| Structure | States | Sub-structure → states |
|---|---|---|
| Upper Arm | 4 | — |
| Elbow | 2 | — |
| Forearm | 5 | — |
| Wrist | 2 | — |
| Hand | 8 | Thumb 2 · Index 2 · Middle 1 · Ring 1 · Little 1 · Palm/Back 1 |
| Shoulder | 2 | — |
| Reserve | 2 | — |
| **Zone total** | **25** | |

### 4.4 Head — states 76–100

| Structure | States | Sub-structure → states |
|---|---|---|
| Skull | 8 | — |
| Face | 9 | Eyes 2 · Ears 2 · Nose 2 · Mouth/Jaw 3 |
| Neck | 2 | — |
| Internal | 4 | — |
| Reserve | 2 | — |
| **Zone total** | **25** | |

### 4.5 Whole-figure check

- 25 + 25 + 25 + 25 = **100 states** = `|Ω|` ✓
- Full-depth terminal leaves = 100 (each 1%) ✓
- Combat-relevant anatomical leaves ≈ 70, plus 7 reserve cells — comfortably within the
  bound, leaving headroom for creatures (four-armed, tails, multiple heads) that
  re-partition their own zones.

## 5. Probability audit (candidate tables)

| Resolution depth | Example | Probability |
|---|---|---|
| Tier 1 (coarse zone) | "Head" | 25% |
| Tier 2 (structure) | "Thigh" (4 states) | 4% |
| Tier 2 (structure) | "Heart" (3 states) | 3% |
| Sub-structure | "Hallux" (2 states) | 2% |
| Full depth (one state) | any single cell | 1% |
| Laterality | left = odd states of a node | node states × ½ (e.g., left Thigh = 2 states = 2%) |

Remarks:

- Within-zone anatomical weighting is **fully expressible** under the candidate tables
  (Heart/Lungs over-weighted; small joints under-weighted), satisfying DEC-041(2)'s
  "small/awkward zones narrower, large/central wider" intent **inside each zone**.
- **Zone-level weighting is NOT expressible without a formal re-open of DEC-100**: the
  locked quartiles force each zone to exactly 25%. DEC-041(2) (weighted zones) predates
  DEC-100 (equal quartiles); DEC-100 explicitly "supplies the numeric ranges DEC-041
  left directional/not locked". The operative reading is: weighting intent lives
  within zones. Any future move to e.g. Torso 30%/Head 15% is a **separate formal
  decision** — all annotations in this brief treat DEC-100 as frozen.

## 6. Answers to proposal §25 open questions

1. **States per Tier-1 region → ** ruled by DEC-100: 25 each. Not re-opened.
2. **Left/right division → ** parity decode of the Zero-Step output (DEC-112 L-008);
   no dedicated half-allocation; each node partitions by odd/even.
3. **States per branch → ** an authoring choice within a zone; any re-partition is free
   until content binds (node counts must sum to the zone's 25).
4. **Anatomical weighting → ** expressed **within** zones; zone weights are frozen at
   equality by DEC-100.
5. **Tactical relevance → ** not a probability factor. Weighting for tactical play
   would require reopening DEC-100; nothing adopted.
6. **Exposed surface area → ** used as a **drafting heuristic only** in the candidate
   tables; not adopted as a principle.
7. **Internal-structure weighting → ** internal organs occupy ordinary states (e.g.,
   Heart 3) and resolve without a side; no special mechanic (Invariant 17 safe).
8. **Different templates → ** yes: L-004 per-creature templates; allocation is content
   per type; state-zone alignment (the 25/25/25/25 quartile alignment) is currently the
   only universal constraint; a non-quartile template would require a ruling on DEC-100.
9. **100-state constraint vs Tiers 6–12 → ** depth-free; only the **leaf count** binds
   (≤ 100). Tiers 6–12 are feasible if leaves stay under the bound.
10. **Zero-Step still the best provider → ** outside scope. Determinism is required by
    DEC-014/L-002; no competing provider is proposed or adopted. Not re-opened.

## 7. Findings

- **F1 (capacity):** the 100-state Index supports any depth (including Tiers 3–12)
  while ≤ 100 terminal leaves exist. Depth is not the scarce resource; leaves are.
- **F2 (probabilities):** every full-depth cell = 1%; every Tier-1 zone = 25%;
  truncation is read-depth, so probabilities are Skill-Tier-stable.
- **F3 (laterality):** parity decode partitions an existing budget — laterality adds no
  states and cannot push a template over the 100-leaf bound.
- **F4 (content bound):** a template needing > 100 distinct terminals is infeasible
  without the (removed) secondary roll or unequal probabilities; it must coarsen. This
  is a content-authoring constraint for **all** creature types, not a rule gap.
- **F5 (weighting):** anatomical weighting is expressible within zones only; DEC-100
  freezes zone odds at equality. Zone-level weighting is a future formal decision if
  ever wanted.
- **F6 (DEC-136 interaction):** under the confirmed single-source, no-secondary-roll
  rule, Tier-2 Armor Bypass is **anchored but not yet resolvable** until this allocation
  (and the L-009 Human template) is authored — consistent with the DEC-019 State-2
  precedent already annotated in DEC-136.
- **F7 (parity micro-ambiguity):** DEC-041(3)/L-008 read "Zero-Step output digit-parity".
  Because Zero-Step is a tens/units exchange, the operative digit should be pinned in
  template content conventions — recommendation: **the units digit of the Zero-Step
  output**. Confirmed non-blocking; documentation nicety; not a rule change.

## 8. Non-Decisions

This brief does **not**: adopt any allocation (tables are candidates); author the L-009
Human Template or any creature template (Tiwa authors content per DEC-077/077.A);
re-open DEC-100, DEC-014, DEC-062, DEC-030, DEC-041, DEC-107; create Canonical text;
change probabilities of the natural roll (Invariant 1/6); or introduce any mechanism
resembling the removed secondary roll (L-003/L-011/DEC-136).

## 9. Next steps

1. **Tiwa reviews the candidate tables** and edits/accepts/rejects per zone (content
   authoring under DEC-077.A in-session standards).
2. **Human/Location Template investigation** (proposal §30 Investigation 3) — a complete
   candidate Human Template built on the adopted allocation; Tiwa-authored content.
3. **Laterality pinning** in the template conventions file (F7) once tables are adopted.
4. **Effect-compatibility pass** (proposal §30 Investigation 6) — Armor Bypass, Wound,
   Trip, Disarm/Break Hold, Equipment Damage against hierarchical addresses, using the
   adopted allocation.
5. Playtest exposure once an adopted allocation exists.