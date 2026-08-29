# Proposed replacement text — Implementation Roadmap, Phase 2 (S-2 Hit Locations) and related tables

**Target version: v1.4.2** (update to Implementation Roadmap v1.4.1). **Correction pass (this revision):** one fix applied after independent review and re-verification against the source synthesis — the "Confirmed procedural rules" list below previously included lazy evaluation alongside three genuinely replicated rules, but the source synthesis (§5) tags lazy evaluation as `[Design inference, ... not separately stress-tested]`, not confirmed. Split below so implementation doesn't carry that rule with the same confidence as the other three. No status, dependency, or acceptance-test content changed beyond that split.

**How to use this file:** drafted as an addition to the existing Phase 2 section (§9) and a light update to the §4 residual decision table. Implementation guidance only — creates no game mechanics, per this document's own stated authority limits.

---

# 9. Phase 2 — S-2 Hit Locations

**Status: Tier-1 provider locked (Zero-Step, evidence-backed) / Invocation policy: candidate accepted, non-canonical / Tier 0/2 policy and broader architecture: WIP**

Unchanged: the Tier-1 Location Index provider (Zero-Step) remains complete and locked as previously documented.

**New — Invocation/Warrant Policy (Candidate, Non-Canonical):**

The S-2 Design Investigation (v1–v5) produced a candidate policy for when a Location Index is generated at all, summarized in Proposals/WIP §2.1A. Implementation-relevant summary:

- Location Index generation requires an explicitly stated, distinct outcome beyond ordinary damage, whose location-dependence is already established under current design (not merely anticipated), and which current rules can resolve.
- A four-state internal classification (Established & Resolvable / Established, Not Yet Resolvable / Outcome Plausible but Location-Dependence Unresolved / No Distinct Consequence) underlies this test but is not intended as a GM-facing procedure — implementation should expose the single collapsed question, not the four states, at the point of play.
- A W3 reference cache exists as a maintained shorthand, not an independent authorization source; implementation should ensure novel/uncached cases still route through the underlying test rather than defaulting to "no" for lack of a cache entry.
- **Confirmed procedural rules to implement (empirical finding, replicated across independent trial rounds):** disjunctive compound-objective evaluation; stale-objective invalidation (re-check the fictional state against the category's rationale at time of use, not just at declaration); S-1 winner-only Location Index eligibility.
- **Additional procedural rule to implement, different evidence class** *(design inference, provisionally adopted — not separately stress-tested at the table, unlike the three rules above)*: lazy evaluation. Location Index may be derived at the point a downstream stage needs it, not mandatorily at declaration time, since Zero-Step only needs the already-recorded natural roll. The reasoning is sound architecturally (Zero-Step is a read-only post-process of an already-recorded roll), but implementation should not treat this rule as carrying the same confidence as the three replicated rules above.

**Acceptance tests — additions:**

- The Named-Outcome Test correctly separates bare location narration from stated distinct consequences.
- Conditional phrasing does not defeat definiteness of a stated objective.
- Compound objectives are evaluated disjunctively.
- A stale objective (fictional state no longer supports the category) voids an otherwise-matching case.
- Only the S-1 contest winner's natural roll is eligible for Location Index generation.
- No currently-State-3 concept (Disarm, Equipment Damage, Function Impairment, Armor Bypass, Incapacitation) generates a Location Index under the current candidate policy, regardless of declaration frequency or plausibility, until a future subsystem (S-3/S-5/S-7/S-10) makes an explicit design choice that location is the delivery mechanism for that outcome — not merely until that subsystem locks in any form.
- Novel, uncached structural cases resolve correctly via the underlying test rather than requiring literal cache membership.

**Remaining implementation and design work (unchanged in scope, updated status):**

- Tier 0 and Tier-2 interface — open.
- Scene/campaign tier policy — **partially informed by the candidate invocation policy, but still open.** The candidate policy determines when a location result is warranted for a given resolution; it does not determine whether a scene or campaign uses Tier 0, Tier 1, or Tier 2 in the first place. That selection question remains unresolved and is not narrowed to "Tier 2 only" by this update.
- Anatomical mapping from Location Index to zone — open, untouched. This includes the structural-destruction case: the candidate policy's State-1 classification for structural weak points establishes narrative resolvability only, not a settled Index-to-component mapping table.
- Downstream interfaces for Effects, Wounds, Armor, and Defence — open; directly informed by the investigation's State-3 findings, which flag that Disarm, Equipment Damage, Function Impairment, Armor Bypass, and Incapacitation are not currently anchored to location as a mechanism, and that S-3/S-5/S-7/S-10 each contain at least one plausible design path (Margin/Tag-gated triggering) that would not require location at all. Future subsystem design work should treat this as an open fork, not a settled assumption in either direction.
- **New:** whose roll (if any) supplies a Location Index for non-attack physical resolutions (hazards, falls, structural interactions without an adversarial "attacker") — flagged by the investigation as a distinct open question requiring its own design pass, not covered by the current candidate policy.

E9 usability evidence and the comparative derivation-cost residual are unchanged from v1.4.1 and not affected by this update.

---

# Proposed update to Section 4 (Residual Decision Roadmap)

| Priority | ID | Decision | Current status | Decision dependency |
|---:|---|---|---|---|
| 2 | S-2 | Hit-location architecture | **Tier-1 provider: Locked (Zero-Step). Invocation/warrant policy: Candidate accepted, non-canonical (S-2 Design Investigation v1–v5) — governs whether a Location Index is warranted for a given resolution. Tier policy (which tier a scene/campaign uses), anatomical mapping, non-attack-resolution scope, and Tier 2 procedure: all still fully Open, not narrowed by the candidate policy.** | S-1 |
