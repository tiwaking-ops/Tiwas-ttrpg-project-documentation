# Tiwas — Implementation Roadmap & Project Governance

**Document Version:** v1.4.2  
**Document Status:** Authoritative Project/Implementation Guidance  
**Rule Authority:** None — this document does not create game mechanics  
**Supersedes:** Implementation Roadmap & Project Governance v1.4.1 (Phase 2 / §9 and the S-2 row of §4 only; all other content carried forward unchanged)  
**Purpose:** Define dependencies, implementation sequencing, simulation gates, regression requirements and governance for completing Tiwas  
**Important:** Implementation guidance must never be mistaken for a design ruling.

**Change note (v1.4.2):** Phase 2 (§9) updated with the S-2 Design Investigation v1–v5 candidate invocation/warrant policy — implementation guidance only, non-canonical. §4's S-2 row updated to match. Structural Weak Points is classified **State 2** (Established, Not Yet Resolvable), not State 1 — a designer ruling made after this document's first draft, per Proposals/WIP v1.4.2 §23. See that section for the full revision record of the underlying design material.

---

# 0. Purpose

This document governs how the Tiwas ruleset progresses from its current locked Core and S-1 state toward a complete universal RPG system.

It exists separately from the rules so that:

- project sequencing does not become game law;
- candidate mechanics can be implemented without being declared final;
- future LLM sessions have a stable development process;
- regression requirements remain visible; and
- unresolved decisions are not accidentally promoted.

---

# 1. Authority Boundary

The implementation hierarchy is:

```text
CANONICAL RULES
      ↓
PROPOSALS / WIP
      ↓
IMPLEMENTATION ROADMAP
```

The Roadmap may explain what should be implemented, what depends on what, what should be simulated, and what acceptance tests should exist. It may not independently decide numerical thresholds, final Quality rules, wound severity, death triggers, armour mechanics, defence costs, Extended Test progress, or other unresolved designer decisions.

---

# 2. Locked Core Invariants

Every implementation must preserve:

- d100 = 1–100;
- `00` = 100;
- Roll-under resolution;
- mandatory 100-Fumble;
- 100 as a failed Double;
- floor rounding;
- Tier/attribute Cap system;
- Cost = Roll;
- Overflow → HP;
- Failure XP;
- temporary Skill Roll Pool;
- Skill Roll Pool Cap ceiling;
- General XP above Cap;
- Advanced Skill creation;
- Advanced Skill full-formula Cap recomputation;
- Advanced Skill lineage resource domain;
- live derived statistics;
- unconditional final recovery; and
- no competing primary resource/progression economy.

The canonical Core Test Transaction is:

```text
Roll
→ Outcome
→ Natural Roll Cost
→ Overflow
→ Failure XP / Advanced Skill effects
→ Recovery
```

Universal Play modules must call this transaction rather than duplicate or replace it.

---

# 3. Development Priorities

All implementation decisions should preserve the current priority order:

1. Granular physical simulation where warranted.
2. Heroic resilience / low permanent character loss.
3. Minimum resolution steps without sacrificing Priority 1.

---

# 4. Residual Decision Roadmap

| Priority | ID | Decision | Current status | Decision dependency |
|---:|---|---|---|---|
| 1 | S-1 | Opposed Quality | **Locked** | Core |
| 2 | S-2 | Hit-location architecture | **Tier-1 provider: Locked (Zero-Step). Invocation/warrant policy: Candidate accepted, non-canonical (S-2 Design Investigation v1–v5) — governs whether a Location Index is warranted for a given resolution. Tier policy (which tier a scene/campaign uses), anatomical mapping, non-attack-resolution scope, and Tier 2 procedure: all still fully Open, not narrowed by the candidate policy.** | S-1 |
| 3 | S-3 | Outcome Effects | Open | S-1 |
| 4 | S-4 | Wound activation/severity | Open | S-2 and S-3 |
| 5 | S-5 | Armor | Open | S-3 and S-4 |
| 6 | S-6 | Defense | Open | S-1 |
| 7 | S-7 | Incapacitation/death | Open | S-4 |
| 8 | S-8 | Difficulty/task adjudication | Open | Core |
| 9 | S-9 | Extended Test progress | Open | S-1 |
| 10 | S-10 | Extended Test failure loss | Open | S-9 |
| 11 | S-11 | Rest/healing | Open | S-4 and S-7 |
| 12 | S-12 | NPC compression | Open | Preceding systems |

These are **decision dependencies**, not a mandatory calendar or implementation order. S-2 and S-3 are parallel workstreams after S-1; their respective unresolved decisions converge at S-4. The Roadmap must always reflect current status rather than preserve obsolete labels.

---

# 5. Universal Play Subsystems

| ID | System | Purpose | Main dependency |
|---|---|---|---|
| U-01 | Opposed Contest | Universal contests | S-1 |
| U-02 | Contest Outcome | Converts test results into contest result | S-1 |
| U-03 | Difficulty | Universal task difficulty | S-8 |
| U-04 | Stakes Gate | Determines when testing is meaningful | S-8 |
| U-05 | Outcome Effects | Converts success into state change | S-3 |
| U-06 | Quality/Advantage Interface | Controls additional Effects | S-3 |
| U-07 | Two-Track Harm | Resources/HP plus wounds | S-3/S-4 |
| U-08 | Wound Engine | Injury states | S-4 |
| U-09 | Location Provider | Tier 0/1/2 location architecture | S-2 |
| U-10 | Armor | Equipment/harm interaction | S-5 |
| U-11 | Defense | Passive/active defence | S-6 |
| U-12 | Conditions | Reusable state effects | S-3/S-4 |
| U-13 | Time/Action | Unified temporal framework | S-6/S-9/S-11 |
| U-14 | Equipment Tags | Interaction metadata | S-3/S-5 |
| U-15 | Extended Tests | Multi-interval tasks | S-9/S-10 |
| U-16 | Hazards | Environmental resolution | S-8 |
| U-17 | Rest/Healing | Recovery beyond normal test recovery | S-11 |
| U-18 | Death/Incapacitation | Completes harm loop | S-7 |
| U-19 | NPC Compression | Practical encounter construction | S-12 |
| U-20 | GM Procedure | Universal adjudication | S-8 |
| U-21 | Magic/Special Abilities | Setting power grammar | Advanced Skills |
| U-22 | Setting Interface | Isolate setting rules | Architecture |

---

# 6. Dependency Architecture and Implementation Sequencing

## 6.1 Decision architecture

```text
LOCKED CORE
    ↓
CORE TEST TRANSACTION
    ↓
S-1 / OPPOSED CONTEST
    ↓
    ┌────────────────────────┐
    ▼                        ▼
S-2 / HIT LOCATIONS     S-3 / OUTCOME EFFECTS
    │                        │
    └───────────┬────────────┘
                ▼
     S-4 / WOUNDS + TWO-TRACK HARM
                ↓
        S-5 / ARMOR and S-6 / DEFENSE
                ↓
    TIME / ACTION, CONDITIONS, TAGS, EQUIPMENT
                ↓
  S-7 / INCAPACITATION + DEATH; S-8 / ADJUDICATION
                ↓
         S-9 / S-10 EXTENDED TESTS
                ↓
     S-11 / REST + HEALING; POWERS; S-12 / NPCs
                ↓
         SETTING INTERFACE → FULL INTEGRATION
```

S-2 is not a prerequisite for the general S-3 Effect design, and S-3 is not a prerequisite for the general S-2 architecture. A location-selecting Effect may consume a location-provider interface, but that local interface dependency does not make either whole workstream sequential.

## 6.2 Implementation sequencing

Implementation may sequence, interleave, or prototype parts of S-2, S-3, and their interfaces according to practical need. A useful sequence is: establish the interface contracts; implement non-location-dependent Effects; implement the location provider and tier policy; then integrate the location-dependent Effects and test the combined harm path.

Interface prototypes between S-3 and S-4 are permitted and encouraged where they expose requirements. They are not a ruling on S-4 wound activation, severity, disability, death, or other unresolved S-4 design. Prototype values and behaviours remain WIP unless separately accepted through the governance process.

Cross-cutting dependencies:

- Time is required for durations, Rest, and ongoing Effects.
- Conditions and Tags support Effects, wounds, equipment, and powers.
- NPC compression depends on the completed state model.
- Setting modules must consume the completed Universal Play layer.

---

# 7. Phase 0 — Regression Harness

Before extending the system, establish deterministic regression tests for the Core.

Required cases: successful low and high rolls; ordinary failure; 100-Fumble; failed Double; sufficient, insufficient, and zero resource; Skill 0, at Cap, above Cap, and above 100; Advanced Skill creation and Cap recomputation; mixed-domain Advanced Skill; live derived-stat changes; and final recovery.

> **Acceptance criterion:** No Universal Play implementation may bypass the Core regression suite.

---

# 8. Phase 1 — S-1 Opposed Contest

**Status: Complete / Locked**

S-1 has completed validation and acceptance. Its implementation requires two independent Core Tests; the success/failure matrix; selectable Quality; Margin; Blackjack; Hybrid Committed; Failure/Failure Repeat; exact Quality-tie Repeat; and no second resource pool. The natural roll remains authoritative for Cost and all Core consequences.

No further S-1 development is planned unless new evidence triggers formal reopening.

---

# 9. Phase 2 — S-2 Hit Locations

**Status: Tier-1 provider locked (Zero-Step, evidence-backed) / Invocation policy: candidate accepted, non-canonical / Tier 0/2 policy and broader architecture: WIP**

Unchanged: the Tier-1 Location Index provider (Zero-Step) remains complete and locked as previously documented.

**Invocation/Warrant Policy (Candidate, Non-Canonical):**

The S-2 Design Investigation (v1–v5) produced a candidate policy for when a Location Index is generated at all, summarized in Proposals/WIP §2.1A. Implementation-relevant summary:

- Location Index generation requires an explicitly stated, distinct outcome beyond ordinary damage, whose location-dependence is already established under current design (not merely anticipated), and which current rules can resolve.
- A four-state internal classification (Established & Resolvable / Established, Not Yet Resolvable / Outcome Plausible but Location-Dependence Unresolved / No Distinct Consequence) underlies this test but is not intended as a GM-facing procedure — implementation should expose the single collapsed question, not the four states, at the point of play.
- A W3 reference cache exists as a maintained shorthand, not an independent authorization source; implementation should ensure novel/uncached cases still route through the underlying test rather than defaulting to "no" for lack of a cache entry.
- **Confirmed procedural rules to implement (empirical finding, replicated across independent trial rounds):** disjunctive compound-objective evaluation; stale-objective invalidation (re-check the fictional state against the category's rationale at time of use, not just at declaration); S-1 winner-only Location Index eligibility.
- **Additional procedural rule to implement, different evidence class** *(design inference, provisionally adopted — not separately stress-tested at the table, unlike the three rules above)*: lazy evaluation. Location Index may be derived at the point a downstream stage needs it, not mandatorily at declaration time, since Zero-Step only needs the already-recorded natural roll. The reasoning is sound architecturally (Zero-Step is a read-only post-process of an already-recorded roll), but implementation should not treat this rule as carrying the same confidence as the three replicated rules above.

**Acceptance tests:**

- Zero-Step exchanges the percentile digits, including `00`/100 handling.
- Tier 1 requires no mandatory additional die.
- Zero-Step has no player-choice branch.
- Tier selection and Location Index derivation never alter the original roll or Core Test consequences.
- Tier 0 creates no location state.
- Location data can be consumed by later Effects/Wound/Armor systems without becoming an alternate Core resolution engine.
- The Named-Outcome Test correctly separates bare location narration from stated distinct consequences.
- Conditional phrasing does not defeat definiteness of a stated objective.
- Compound objectives are evaluated disjunctively.
- A stale objective (fictional state no longer supports the category) voids an otherwise-matching case.
- Only the S-1 contest winner's natural roll is eligible for Location Index generation.
- No currently-State-3 concept (Disarm, Equipment Damage, Function Impairment, Armor Bypass, Incapacitation) generates a Location Index under the current candidate policy, regardless of declaration frequency or plausibility, until a future subsystem (S-3/S-5/S-7/S-10) makes an explicit design choice that location is the delivery mechanism for that outcome — not merely until that subsystem locks in any form.
- Novel, uncached structural cases resolve correctly via the underlying test rather than requiring literal cache membership.

E9 usability evidence is complete **for the tested physical two-d10 method only**: 50 participants (25 new to RPGs and 25 RPG players new to Tiwas) reported no difficulty with rolling or digit exchange and gave positive feedback. A single d100, digital roller, verbally announced result, and other input methods remain untested; do not treat E9 as evidence for them.

The comparative derivation-cost residual is recorded separately from E9: across the examined rolling modes, Units-Digit required 0–1 additional derivation operations and Zero-Step required 1–2. This is a structural comparison, not a second E9 result or a substitute for input-method-specific usability testing.

**Remaining implementation and design work:**

- Tier 0 and Tier-2 interface — open.
- Scene/campaign tier policy — **partially informed by the candidate invocation policy, but still open.** The candidate policy determines when a location result is warranted for a given resolution; it does not determine whether a scene or campaign uses Tier 0, Tier 1, or Tier 2 in the first place. That selection question remains unresolved and is not narrowed to "Tier 2 only" by this policy.
- Anatomical mapping from Location Index to zone — open, untouched. Structural Weak Points is classified **State 2** (Established, Not Yet Resolvable), precisely because this mapping doesn't exist yet: location-dependence is anchored, but no Location Index currently generates for this category in play until the mapping is built.
- Downstream interfaces for Effects, Wounds, Armor, and Defence — open; directly informed by the investigation's State-3 findings, which flag that Disarm, Equipment Damage, Function Impairment, Armor Bypass, and Incapacitation are not currently anchored to location as a mechanism, and that S-3/S-5/S-7/S-10 each contain at least one plausible design path (Margin/Tag-gated triggering) that would not require location at all. Future subsystem design work should treat this as an open fork, not a settled assumption in either direction.
- Whose roll (if any) supplies a Location Index for non-attack physical resolutions (hazards, falls, structural interactions without an adversarial "attacker") — flagged by the investigation as a distinct open question requiring its own design pass, not covered by the current candidate policy.

The broader tier policy, anatomical mapping, and downstream interaction remain open and require their own design and validation gates. Do not treat the completed Tier-1 provider decision, or the candidate invocation policy, as closure of S-2 as a whole.

---

# 10. Phase 3 — S-3 Outcome Effects and S-3/S-4 Interface Prototyping

**S-3 status: Open. S-4 status: Open.**

Implement the structural Effect interface first. Candidate Effects include Injury; Condition; Disarm / Break Hold; Movement / Position; Tempo; Guard Break; Bleed / Drain; Retreat / Yield; Equipment Damage; and Location selection.

S-3 work may prototype how an Effect passes harm or state information to a prospective S-4 Wound Engine. Such a prototype is an architectural exercise, not a lock on S-4. In particular, it must not silently establish wound severity thresholds, activation triggers, disability effects, or death checks.

The prospective two-track harm interface is:

```text
Track A                         Track B
PE / MP                         Location
   ↓                               ↓
Overflow                        Wound
   ↓                               ↓
Global HP                       Condition / Disability / Death Check
```

Acceptance criteria:

- Effects create real state changes.
- Effects do not alter historical rolls.
- Empty PE/MP is not automatic defeat.
- Overflow remains HP damage.
- HP = 0 is not automatically death.
- Wounds are not a second HP pool.

Simulation gate: measure Effect frequency, exchange length, resource expenditure, wound frequency, severe injury, and state-change density. Do not lock numerical thresholds without required evidence and a designer ruling.

---

# 11. Phase 4 — Armor and Defense

## 11.1 Armor

Implement Armor Traits and Tags, Bypass and Sunder interfaces, location interaction, and equipment damage. Compare candidates for bookkeeping, tactical value, simulation fidelity, and resolution steps.

## 11.2 Defense

Implement passive and active defense interfaces, defense as a normal contest participant, resource interaction, and timing. Compare candidates for PE/MP drain, number of rolls, survivability, tactical decision density, and resolution steps.

No candidate should be promoted to Canonical merely because it is convenient to implement.

---

# 12. Phase 5 — Incapacitation and Death

Implement HP-zero state, incapacitation, stabilization, survival, permanent injury, death, and recovery from incapacitation.

> **Simulation target:** Preserve heroic resilience while retaining meaningful physical consequences.

The permanent character-loss rate must be measured. No proposed death threshold becomes Canonical until the decision gate is passed.

---

# 13. Phase 6 — Difficulty and Task Adjudication

Implement difficulty grades, Skill-side modification, Stakes Gate, meaningful-uncertainty test, Skill selection, and opposed/unopposed selection. Verify interaction with Cost, Failure XP, 100-Fumble, Doubles, and Advanced Skills. Difficulty must not alter the natural die face.

---

# 14. Phase 7 — Extended Tests

Implement Extended Tests as repeated ordinary Tiwas tests. Each interval preserves Cost = Roll, Overflow → HP, Failure XP, failed Doubles, Advanced Skills, and Recovery.

Candidate progress models are Margin accumulation and Success count. Candidate failure models are stall, progress loss, and complication. Compare task completion time, resource depletion, failure frequency, growth, Overflow, and Advanced Skill generation. Progress must never become a second currency.

---

# 15. Phase 8 — Cross-Cutting Architecture

Define Time (rounds, turns, actions, reactions, movement, intervals, ongoing timing); Conditions (application, stacking, duration, removal, interaction); Tags (weapon, armour, Effect, location, power, creature, setting); and Equipment (records, Traits, damage, carrying, encumbrance, repair/replacement).

Hazards use:

```text
Trigger
→ Existing Test
→ Cost
→ Outcome
→ Existing Effect / Condition / Harm
```

No subsystem-specific currency should be created.

---

# 16. Phase 9 — Rest and Healing

Implement the attrition loop after harm and death rules are sufficiently stable: Rest, resource recovery, wound recovery, healing time, ongoing conditions, and recovery from incapacitation. Evaluate against the requirement that Rest must not trivialize the resource identity.

---

# 17. Phase 10 — Magic and Special Abilities

Implement a setting-facing power grammar around Advanced Skills. Verify Body-rooted and Mind-rooted powers, mixed-domain Advanced Skills, Overflow, failed Doubles, Conditions, Effects, and Extended Tests. Fixed spell lists may exist as setting content but must not be required by the Core.

---

# 18. Phase 11 — NPC Compression

NPC construction should compress the same underlying mechanics rather than introduce a separate NPC engine. Evaluate encounter construction time, mathematical compatibility, resource behaviour, survivability, and challenge curves. NPC packages must still resolve through the same Universal Play architecture.

---

# 19. Phase 12 — Setting Interface

A setting module may add content, permissions, creatures, equipment, powers, technology, magic, Tags, and Effects. It may not redefine d100, roll-under, 100-Fumble, Cost = Roll, Overflow → HP, Failure XP, Skill Roll Pool, Advanced Skill construction, or Core recovery.

> **Acceptance criterion:** A new setting can be implemented without modifying the Core Engine.

---

# 20. Phase 13 — Full Integration Simulation

## 20.1 Opposed exchanges

Test low versus high and equal Skill; Skill > 99; both succeed, one succeeds, and both fail; 100-Fumble; failed Doubles; and resource exhaustion.

## 20.2 Combat

Test locations on/off and location tiers; armour; defense; Effects; Conditions; wounds; incapacitation; and death.

## 20.3 Extended Tests

Compare progress and failure models, resource drain, Overflow, Failure XP, and Advanced Skill creation.

## 20.4 Powers

Test Mind-rooted, Body-rooted, and mixed-domain powers; Overflow; failed Doubles; Conditions; and Effects.

## 20.5 Non-combat

Test social contests, research, crafting, travel, hazards, stealth, and technical tasks.

---

# 21. Mandatory Regression Matrix

| Invariant | Required result |
|---|---|
| Cost = Roll | Resource expenditure equals natural roll |
| 100-Fumble | 100 always fails |
| 100 Double | 100 always qualifies as failed Double |
| Overflow → HP | Resource shortfall becomes HP damage |
| Failure XP | Failed tests generate XP |
| Failure-XP clamp | XP never becomes negative |
| Skill Roll Pool | Resolved within the same failed test |
| Cascading | Multiple increases possible where affordable |
| Cap ceiling | Skill Roll Pool cannot exceed Cap |
| General XP above Cap | Above-Cap Skill advancement remains possible |
| Advanced Skill trigger | Only qualifying failed Doubles trigger |
| Advanced Tier | Tier + 1 |
| Advanced Attribute | No duplicate attribute |
| Advanced Cap | Full formula recalculation |
| Resource lineage | Original Tier-1 domain controls resource |
| Live statistics | Attribute changes propagate immediately |
| Recovery | Always last |
| No parallel currencies | No competing primary resource/progression system |

---

# 22. Acceptance Standard for a Complete Universal System

Tiwas should not be considered mechanically complete until every meaningful test uses the common Core transaction; opposed actions use the universal contest primitive; successful contests can create meaningful state change; harm supports both resource attrition and meaningful injury; location granularity is configurable; the completed death model preserves heroic resilience; combat and Extended Tests share coherent time architecture; Conditions and Tags are reusable; progression remains failure-driven; Extended Tests do not create a second currency; powers use the universal Skill architecture; NPCs use compressed versions of the same mechanics; settings can be added without modifying Core invariants; and the full regression suite passes.

---

# 23. Project Governance

## 23.1 Status transitions

```text
Idea
 ↓
Proposal
 ↓
WIP
 ↓
Independent Review
 ↓
Simulation / Analysis
 ↓
Designer Ruling
 ↓
Accepted
 ↓
Locked / Canonical
```

An item may return to WIP if evidence exposes a substantive problem.

## 23.2 Evidence classes

Design documentation should distinguish:

- **Mechanical fact:** directly follows from existing locked rules.
- **Empirical finding:** supported by simulation, playtesting, or other explicit evidence.
- **Designer ruling:** a deliberate choice not mathematically forced by the system.
- **Recommendation:** a proposed preference not yet accepted.
- **Architectural constraint:** governs how systems interact rather than what a mechanic numerically does.

Evidence must be recorded with its scope and limitations. An empirical finding does not itself establish a designer ruling; an architectural constraint does not establish a numerical mechanic. Future documents should label these categories wherever confusion is likely.

---

# 24. LLM Governance Rules

Future LLM sessions must:

1. Treat Canonical Rules as authoritative.
2. Treat Proposals/WIP as non-canonical.
3. Treat Roadmap recommendations as implementation guidance.
4. Never promote a proposal because it appears repeatedly in documentation.
5. Never infer a numerical threshold from an example unless explicitly locked.
6. Never silently resolve an open designer fork.
7. Identify contradictions between current and historical documents.
8. Prefer the current locked ruling over superseded source wording.
9. Preserve the distinction between empirical evidence and designer judgement.
10. State clearly when an answer depends on a proposal rather than a Canonical rule.
11. Never create a parallel Core resolution engine merely to implement a subsystem.
12. Never create a new primary resource or progression currency without explicit designer approval.
13. Treat an interface prototype as non-canonical unless a formal ruling says otherwise.
14. When a subsystem is locked, update the Canonical document and its changelog.
15. When a proposal is superseded, retain its historical significance but clearly mark it Superseded.
16. If new evidence materially challenges a locked rule, recommend reopening it rather than silently changing it.

---

# 25. Documentation Maintenance Rule

The three consolidated documents should remain synchronized.

## When a rule becomes locked

Update Canonical Rules, the Canonical Changelog, Proposal status, Roadmap status/dependencies, and regression requirements if applicable.

## When a proposal changes

Update Proposals/WIP and the relevant Roadmap dependency or phase. Do not modify Canonical Rules.

## When an implementation decision changes

Update the Roadmap and any relevant WIP note if it affects a design proposal. Do not modify Canonical Rules unless the actual game mechanic has changed through formal governance.

---

# 26. Core Project Principle

The implementation target is not merely “complete combat.” The target is:

> **A universal state-resolution architecture in which combat, social conflict, hazards, crafting, research, travel, magic and other activities reuse the same Tiwas Core transaction.**

The central architectural rule is:

> **Every Universal Play Module must be an adapter around the locked Tiwas Core transaction, never a competing resolution, resource, progression, or recovery engine.**
