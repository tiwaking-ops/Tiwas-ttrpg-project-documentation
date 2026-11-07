---
document:
  title: "Tiwas — G5 Seven Consuming Mechanics: Drafter Sprint Instructions (2026-09-19)"
  version: "1.0"
  status: "Advisory working document (not canonical, not a ruling)"
provenance:
  author_llm: []
  assessor_llm:
    - {name: "not established", version: "not established"}
  last_modified_by_llm: {name: "opencode", version: "muse-spark-1.3-contributor-free"}
  created_date: "2026-09-19"
  last_modified_date: "2026-09-19"
  provenance_note: "Directions issued by Tiwa (human designer) on 2026-09-19 when ruling the five precision items; scribed and compiled by opencode / muse-spark-1.3-contributor-free. Section D items are previously recorded corrections from the stored upstage verification, included for completeness and NOT part of Tiwa's 2026-09-19 directions. This file directs drafting work only; it records no rulings and confers no authority."
---

# G5 Seven Consuming Mechanics — Drafter Sprint Instructions (2026-09-19)

**Status:** Advisory working document. Drafter directions from Tiwa's 2026-09-19 rulings on the five precision items (see `investigations/tiwas-g5-fusion-review-items-1-5-advisory-report-2026-09-19.md` and register entries DEC-147, DEC-148). **No new rulings herein. Nothing is canonical.**

## 0. Locked constraints update (new since the fusion draft)

- **DEC-147 (RULED):** Movement Distance is derived per turn from live effective MS; never stored, banked, or tracked per scene. Positions/bands are scene state, not allowance. Mid-turn MS change: remaining = effective MS at query − hexes spent, floored at 0; no debt; rises grant movement. Treat ephemerality as locked — stop flagging it as an assumption.
- **DEC-148 (RULED clarification):** DEC-133.A R3 means "consuming mechanics operating on the Position-tier substrate," not "added to the DEC-023.A alpha list." Do not route every mechanic through a Position-tier Effect selection unless its own design requires it.
- **Still open:** Z-A fork (U-1, deferred until Q2/Q10 settle); U-6/U-7/U-8/U-9; the 14 mechanics questions; SA-5/E5 provenance divergence. **Do not resolve any of these.**

## A. Z-A drafting fixes (Tiwa-directed)

1. Drop "second Cost channel." State Invariant 6 (Cost = natural roll) and Invariant 17 (no pool) separately.
2. Add a floor clause so DEC-125's Prone guarantee isn't defeated (advisory suggested form: a mover with unspent allowance ≥ 1 may always enter at least one hex — candidate, confirm before treating as settled).
3. State the order of operations: DEC-122/DEC-138 overlays fix effective MS first, then the Z-A multiplier applies.
4. State explicitly that ZoC is a StateRecord (DEC-117).

## B. P-A Grappled branch (Tiwa-directed)

Carry the real three-path mechanism, not the generic "zeros or penalises" sentence (which is removed):

| Path | Mechanism |
|---|---|
| Victim moves away | Contested Break Hold / Break Free (DEC-124, DEC-131): fail = Grapple persists, mover locked, no relocation; success = stepwise Heal-Effect-System Tier reduction gated on breaker Skill-Tier ≥ record Tier; `Y = 0` removes the record |
| Holder drags victim | Holder effective MS − record Tier Y, read live (DEC-143); victim moves along at no separate cost |
| Other Grappled movement | DEC-122 zero (provisional residual) |

Also required: state **how Pin/Hold Position differs from the existing Grappled Effect**. Fallback, only if no difference can be shown: limit P-A to the Restrained branch.

## C. P-0 citation direction (Tiwa-directed)

1. Cite **DEC-079** as the Condition-vocabulary source.
2. Cite **DEC-082.A R2** as a ruled constraint, labelled "inference to Pin/Hold."
3. Drop DEC-126 (terminology only).
4. Replace "must reuse" with: R2 rules no further movement-denial interaction mechanics, so any new Pin/Hold denial rule would be a new ruling.

## D. Previously recorded corrections (upstage §6.2 — for completeness, not Tiwa-directed)

1. Tag the §4(a) M-0 Cost claim individually (or make the block tag explicit).
2. Cite DEC-115 directly (plus DEC-117 for extension/counter/removal) instead of "DEC-115 style"; anchor P-B and Seize record proposals to the schema with field lists.
3. Split the §0.1 global evidence tag: invariant existence = mechanical fact; candidate-satisfies-invariant = recommendation/analysis.
4. Reconcile frontmatter `author_llm` with the §11 source-run attribution.

## E. Do-not-touch list

Z-A fork outcome (U-1/U-2), Q2/Q10 and the 14 mechanics questions, U-6 (Open/Close Lane), U-7 (Disengage mapping), U-9 (Restrained Break Free), U-10/U-11 interactions, C4 designer-awareness note. All remain open for Tiwa.
