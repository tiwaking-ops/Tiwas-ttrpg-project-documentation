# Proposed replacement text — Implementation Roadmap, Phase 2 (S-2 Hit Locations) and related tables

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
- Confirmed procedural rules to implement: disjunctive compound-objective evaluation; stale-objective invalidation (re-check the fictional state against the category's rationale at time of use, not just at declaration); S-1 winner-only Location Index eligibility; lazy evaluation (Location Index may be derived at the point a downstream stage needs it, not mandatorily at declaration time, since Zero-Step only needs the already-recorded natural roll).

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
- Scene/campaign tier policy — **substantially addressed by the candidate invocation policy** (consequence-driven rather than scene-fixed); remaining scope is limited to Tier 2 specifically, once Tier 2 has an articulated purpose.
- Anatomical mapping from Location Index to zone — open, untouched.
- Downstream interfaces for Effects, Wounds, Armor, and Defence — open; directly informed by the investigation's State-3 findings, which flag that Disarm, Equipment Damage, Function Impairment, Armor Bypass, and Incapacitation are not currently anchored to location as a mechanism, and that S-3/S-5/S-7/S-10 each contain at least one plausible design path (Margin/Tag-gated triggering) that would not require location at all. Future subsystem design work should treat this as an open fork, not a settled assumption in either direction.
- **New:** whose roll (if any) supplies a Location Index for non-attack physical resolutions (hazards, falls, structural interactions without an adversarial "attacker") — flagged by the investigation as a distinct open question requiring its own design pass, not covered by the current candidate policy.

E9 usability evidence and the comparative derivation-cost residual are unchanged from v1.4.1 and not affected by this update.

---

# Proposed update to Section 4 (Residual Decision Roadmap)

| Priority | ID | Decision | Current status | Decision dependency |
|---:|---|---|---|---|
| 2 | S-2 | Hit-location architecture | **Tier-1 provider: Locked (Zero-Step). Invocation/warrant policy: Candidate accepted, non-canonical (S-2 Design Investigation v1–v5). Tier policy, anatomical mapping, non-attack-resolution scope, and Tier 2: still Open.** | S-1 |
