---
document:
  title: "Seven Consuming Mechanics — P0 Spec Card (DEC-133.A R3)"
  version: "0.1"
  status: "Non-canonical advisory record — Spec card for P1 drafting; no authority-changing action authorized"
  provenance:
    author_llm: {name: "nemotron-3-super-120b-a12b", version: "nvidia/nemotron-3-super-120b-a12b"}
    assessor_llm: {name: "not established", version: "not established"}
    last_modified_by_llm: {name: "nemotron-3-super-120b-a12b", version: "nvidia/nemotron-3-super-120b-a12b"}
    created_date: "2026-09-19"
    last_modified_date: "2026-09-19"
  note: "This spec card outlines the locked invariants, open questions, and dependencies for the P1 corrected re-run draft of the seven consuming mechanics (DEC-133.A R3). It is non-canonical advisory material and does not confer authority."
---

# Seven Consuming Mechanics — P0 Spec Card (DEC-133.A R3)

## Purpose
This spec card defines the locked constraints and open questions for the seven consuming mechanics (DEC-133.A R3) to guide the P1 corrected re-run draft.

## Canonical-vs-Proposal Status
The seven consuming mechanics are Position-tier Effects under DEC-023.A, carried open by DEC-133.A R3. They are not canonical rules; they are advisory proposals subject to designer ruling.

## Dependency Chain
- Depends on DEC-023.A (Position-tier Effect content enumeration) [DEC-023.A: line 219]
- Depends on DEC-095 (Combat sequencing / initiative) [DEC-095: line 127]
- Depends on DEC-133 (Movement resolution granularity) [DEC-133: line 170]
- Depends on DEC-133.A R3 (confirmation of deferred items) [DEC-133.A: line 171]
- Depends on Core Invariants 6, 17, 18 [Invariant 6: line 621, Invariant 17: line 632, Invariant 18: line 633]

## Locked Invariants (from P0 spec card and sprint instructions)
- Invariant 6: Cost equals the natural roll (canonical) [line 621]
- Invariant 17: No Universal Play subsystem may introduce a competing primary resource or progression economy (canonical) [line 632]
- Invariant 18: Universal Play modules must build on the Core Test Transaction rather than replace it (canonical) [line 633]
- DEC-147: Movement Distance is derived per turn from live effective MS; never stored, banked, or tracked per scene. Mid-turn MS change: remaining = effective MS at query − hexes spent, floored at 0; no debt; rises grant movement. [DEC-147: line 193]
- DEC-148: DEC-133.A R3 means "consuming mechanics operating on the Position-tier substrate," not "added to the DEC-023.A alpha list." [DEC-148: line 194]

## Open Questions
- U-1: Z-A: per-hex accounting rule on a zone-scoped record vs Tier-Y overlay on the mover
- U-2: Z-A floor clause preserving the DEC-125 guarantee (mover with A ≥ 1 may always enter one hex)
- U-6: Whether Open/Close Lane is a silent eighth consuming mechanic
- U-7: Whether Disengage is a distinct Effect or maps to Base-tier Open Retreat / Compel Yield
- U-8: How Pin/Hold Position differs from Grappled (drafter to show, else Pin/Hold limited to Restrained)
- U-9: Definition of Restrained's "Break Free" mechanism
- U-10: Relationship between ZoC and the `reaction:vigilant` movement-trigger Reaction
- U-11: Whether Z-A and Disengage double-charge the same movement
- The 14 mechanics questions (as per the verification chat report §3.3):
  1. Disengage shape
  2. Zone of Control shape
  3. Chase shape
  4. Generic movement contest
  5. Forced Movement magnitude
  6. Pin/Hold vector
  7. Seize/Deny shape
  8. Fork C (contested-movement consumption)
  9. Fork T (extra Skill-Tier gate on Position-tier Effects)
  10. ZoC ↔ Seize/Deny relationship
  11. Default Skill families for movement contests
  12. Duration defaults for pins and ground claims
  13. ZoC Z-A distance multiplier invariant status
  14. Pin/Hold Condition-stack reference precision
- SA-5/E5 provenance divergence (unresolved)

## DEC+Line Links
- DEC-013: line 37
- DEC-023.A: line 219
- DEC-079: line 107
- DEC-095: line 127
- DEC-107: line 140
- DEC-122: line 157
- DEC-124: line 159
- DEC-125: line 160
- DEC-131: line 166
- DEC-133: line 170
- DEC-133.A: line 171
- DEC-143: line 186
- DEC-145: line 190
- DEC-147: line 193
- DEC-148: line 194
- Invariant 6: line 621 - Canonical Rules
- Invariant 17: line 632 - Canonical Rules
- Invariant 18: line 633 - Canonical Rules