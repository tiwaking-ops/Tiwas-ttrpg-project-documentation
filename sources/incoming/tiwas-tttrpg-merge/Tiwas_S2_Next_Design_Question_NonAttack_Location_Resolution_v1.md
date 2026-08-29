# Tiwas S-2 Next Design Question — Non-Attack Roll Location Resolution

**Purpose:** This brief kicks off investigation into how Location Index is supplied for non-attack physical resolutions (falls, environmental hazards, etc.) — the open scope gap identified in v5 synthesis §7 and Canonical Rules §14.3.

**Core Question:** When a rule calls for a Tier-1 Location Index in a non-attack physical resolution (where there is no "attacker" whose natural d100 roll Zero-Step consumes), whose roll, if any, supplies the Location Index?

**Documents to Reference (already available in this Project):**
1. `Tiwas TTRPG — Canonical Rules & Changelog-v1-3.md` (Canonical source)
2. `Tiwas — Proposals, WIP & Design Direction-v1.4.1.md` (Design exploration)
3. `Tiwas — Implementation Roadmap & Project Governance-v1.4.1.md` (Implementation guidance)
4. `Tiwas_S2_Location_Granularity_Policy_Investigation_v5_synthesis_3.md` (Prior investigation record — **do not re-summarize**)

**Key Constraints from Prior Work:**
- Zero-Step is locked as the Tier-1 Location Index provider (Canonical §14.1)
- Zero-Step derives Location Index by exchanging tens/units digits of the **attacker's** natural d100 roll
- S-2 tier policy (when to use Tier 0/1/2) remains unresolved (Canonical §14.3)
- Anatomical mapping and downstream interactions remain unresolved
- The non-attack-roll scope gap was explicitly called out as separate from warrant policy

**Investigation Scope:**
Focus strictly on the Location Index *source* for non-attack physical resolutions. Do not re-litigate:
- Whether location is warranted (that's the prior investigation's Four-State Model)
- Tier selection policy (when to use Tiers 0/1/2)
- Anatomical mapping (Location Index → zone)
- Downstream consumption (how wounds/armour/etc. use Location Index)

**Starting Point:**
The v5 synthesis confirmed that hazards and similar non-attack physical events (e.g., rope-bridge fall) have no natural "attacker" whose roll Zero-Step consumes. This question remains open and should be treated as a distinct, narrower rules-architecture question.

**Suggested Approach:**
1. Survey Canonical Rules for any existing non-attack physical resolution mechanics
2. Check Proposals/WIP for proposed mechanisms (e.g., environmental hazards, extended tests)
3. Consider whether a default roll (e.g., environmental roll, scene roll) could supply the index
4. Evaluate if Location Index generation could be deferred to a consuming subsystem
5. Assess impact on Core Test Transaction invariants (Cost = Roll, etc.)

**Output Expected:**
A position paper proposing how to supply Location Index for non-attack physical resolutions, citing specific document sections and identifying any gaps requiring new mechanics or governance decisions.