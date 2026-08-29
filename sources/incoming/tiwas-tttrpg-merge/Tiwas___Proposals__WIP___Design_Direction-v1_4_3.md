# Tiwas — Proposals, WIP & Design Direction

**Document Version:** v1.4.3
**Document Status:** Non-Canonical Design Repository
**Authority:** Design exploration only
**Revision nature:** §2.5 updated to record the designer ruling closing the S-2 Non-Attack Location Index Source investigation (deferred, not resolved as a mechanic). No other content changed from v1.4.2. This is not a promotion to Canonical status — see §21 and §23.
**Supersedes:** Proposals, WIP & Design Direction v1.4.2 (§2.5 only; all other content carried forward unchanged)
**Purpose:** Central repository for unresolved, proposed, experimental and directional Tiwas mechanics
**Critical rule:** Nothing in this document is canonical merely because it is described in detail.

**Version-number note:** This file is labelled **v1.4.3**. Earlier minor-revision files in this series used a `1.4x` filename pattern by accident. Later files use the correct `x.y.z` format.

**Authority boundary:** This document records design state; it does not determine design state. Where this document conflicts with the Canonical Rules or a current governance decision, the Canonical Rules and the explicit governance decision prevail.

---

# 0. How to Read This Document

This document contains material that may become part of Tiwas but has not yet completed the locking process.

Every item should be understood according to its status:

| Status | Meaning |
|---|---|
| **Proposed** | A candidate rule under active consideration |
| **WIP** | Currently being developed or reviewed |
| **Experimental** | Tested or invented for exploration but explicitly excluded from the ruleset |
| **Design Direction** | An architectural or philosophical preference, not necessarily a mechanic |
| **Reserved** | Known required subsystem with no settled implementation |
| **Superseded** | Historical material retained for understanding but no longer current |

Do not treat **Design Direction**, **WIP**, **Proposed**, or an **observation** as locked rules. An observation is an evidence/design note, not a lifecycle status.

Only the Canonical Rules document creates current rules.

---

# 1. Current Design Direction

The following high-level design principles are retained as the current direction for Tiwas development. They are not canonical rules by virtue of appearing in this heading.

## 1.1 Identity

> Tiwas is a high-consequence percentile universal RPG in which every attempt costs resources, every failure generates growth, and every meaningful success changes the tactical or narrative state.

## 1.2 Priorities

1. Granular physical simulation where appropriate.
2. Heroic resilience / low permanent character loss.
3. Minimum resolution steps without sacrificing meaningful simulation.

## 1.3 Architecture

The intended architecture is:

```text
TIWAS CORE ENGINE
        ↓
CORE TEST TRANSACTION
        ↓
UNIVERSAL PLAY MODULES
        ↓
SETTING MODULES
        ↓
SETTING CONTENT
```

A setting should add content and permissions rather than rewrite the Core engine.

---

# 2. S-2 — Hit-Location Architecture

**Status: Partially locked / WIP — Tier-1 Location Index provider locked. Invocation/warrant policy: Candidate policy accepted for further development; not yet promoted to Canonical. Non-attack Location Index generation: Ruled deferred (see §2.5A).**

**Zero-Step is locked; the broader S-2 architecture, including the warrant policy below, is not.**

The Canonical Rules record a **Canonical / Locked — limited S-2 decision**: only the Tier-1 Location Index provider (Zero-Step) is locked. Tier policy, anatomical mapping, and downstream interactions remain unresolved. A separate, extensive non-canonical investigation (S-2 Design Investigation v1–v5) has produced a **candidate invocation/warrant policy**, summarized below and detailed in the investigation record (see `Tiwas_S2_Design_Investigation_v5_synthesis_CORRECTED.md`). This candidate policy is accepted as the current working direction for S-2's invocation question but has not completed the promotion process in §21 and does not modify this document's non-canonical status.

A follow-on investigation (S-2 Non-Attack Location Index Source, starter brief v1.1) examined a narrower question — whether, and whose, natural roll supplies a Location Index for non-attack physical resolutions (falls, hazards, structural collapses). That investigation concluded with a designer ruling; see §2.5A.

## 2.1 Limited locked S-2 decision

Unchanged from v1.4.2 — Zero-Step remains the locked Tier-1 provider per Canonical Rules §14.1–§14.2. Not reopened by this update.

## 2.1A S-2 Candidate Invocation Policy (Non-Canonical)

Unchanged from v1.4.2. This policy governs attack-side invocation only. See §2.5A for the separate, now-closed, non-attack question.

The S-2 Design Investigation (v1–v5) proposes the following as a candidate answer to "when should Tiwas generate a Tier-1 Location Index":

**Four-state classification (internal/documentation architecture):**

1. **Established & Resolvable** — location-dependence is conceptually anchored and current rules can act on it → generate.
2. **Established, Not Yet Resolvable** — anchored, but no current rule can act on the result yet → do not generate; record as pending.
3. **Outcome Plausible, Location-Dependence Unresolved** — the named consequence is a reasonable future outcome, but whether location specifically delivers it is an open design fork, not just an unimplemented detail → do not generate.
4. **No Distinct Consequence** — no distinct outcome named → do not generate.

**GM-facing procedure (simplified, draft):**

> Generate a Location Index only when the player has explicitly stated a distinct outcome beyond ordinary damage, that outcome's location-dependence is already established under current Tiwas design (not merely plausible or anticipated), and current rules can actually resolve it.

**Warrant test (Named-Outcome Test):** a declared objective is definite — and Warrant-eligible — only if the player explicitly names a distinct consequence, other than ordinary damage, tied to the specified location. Conditional phrasing does not defeat definiteness; stated purpose/motivation without a named distinct outcome does not establish it.

**Designer rulings adopted into this candidate policy:**
- **Explicit-only objectives.** The GM does not infer an unstated distinct objective from location or fictional context alone.

**Procedural riders (carried into the candidate policy):**
- Compound objectives evaluated disjunctively.
- Stale objectives (fictional state no longer supports the category's rationale) void an otherwise-matching case.
- In S-1 opposed contests, only the winning participant's natural roll is eligible for Location Index generation (per Canonical §13.2 — Quality never alters either participant's historical roll).
- Location Index evaluation may be deferred (lazy evaluation) to whenever a downstream stage first needs the answer, since Zero-Step is a read-only post-process of an already-recorded roll (Canonical §14.2). *(Design inference, provisionally adopted — not separately stress-tested at the table, unlike the three procedural riders above.)*

**Conceptual Anchor findings (current, subject to revision as S-3/S-5/S-7/S-10 develop):**

**Note:** the table below reflects design inference tested against source documents (the Conceptual Anchor Challenge), not blind-trial data. It does not carry the same evidentiary weight as the Named-Outcome Test above, which was validated against 21/21 trial cases.

| Concept | State | Basis |
|---|---|---|
| Structural weak points (hinges, supports, load-bearing components) | **2 (Established, Not Yet Resolvable)** | Location-dependence is anchored and narratively distinguishable — no competing non-location mechanism is proposed for this concept, unlike the State-3 rows below — but current rules do not yet provide a settled Location Index→component mapping or downstream resolution mechanism (see §2.5). Not currently an Active/Generate entry. |
| Disarm / Break Hold | **3** | §3.2 below already contemplates Margin/Tag-gated triggering as an alternative to location; location-mechanism unresolved |
| Equipment damage | **3** | Same basis |
| Function impairment (blindness, movement) | **3** | §10 Conditions have no stated activation mechanism |
| Armor bypass | **3** | §5 below documents Tag/Trait-based interaction as the current design direction — a documented alternative mechanism, which is what this table's Anchor test requires for Unanchored/State-3 status. §5 emphasizes Tags and does not itself address whether location also participates; that is a gap, not a stated contradiction. |
| Incapacitation / kill | **3, circularly** | §4.1/§7 below condition localized injury on locations already being active — this concept cannot be resolved independently of the S-2 decision itself |

**Important:** entries at State 3 are *not* Watch-list entries pending implementation. They record an unresolved design fork (is location the mechanism at all), not merely missing numbers. They should be revisited only when the relevant future subsystem makes an explicit choice that location is how the outcome is delivered — not merely when that subsystem locks in any form.

**W3 cache role:** the cache is a maintained shorthand for situations already established at State 1 or 2 by the policy above. It does not independently establish Warrant or Anchor status. Novel, uncached situations are still evaluated directly against the policy (confirmed by two independent novel-case trials during the investigation, both resolving correctly without cache membership). At present, no candidate sits at State 1; Structural Weak Points is the sole State-2 entry (see table above), and no Location Index currently generates for it in play.

## 2.2 Purpose of remaining S-2 work

Define how Tiwas handles physical hit locations without forcing every scene to use maximum-granularity combat procedures.

## 2.3 Location-granularity tiers

| Location Tier | Model | Resolution cost | Intended use |
|---|---|---:|---|
| 0 | No location state | Lowest | Mass brawls, cinematic fighting, scenes where locations add little |
| 1 | Zero-Step Location Index from the existing attack roll | Near-zero | Standard simulation-grade play, formal duels |
| 2 | Full location / armour / surgery model | Higher | Optional gritty play |

**Important:** Location Tiers are unrelated to Skill Tier. Core Skill Tier measures attributes in a Skill Cap formula; Location Tier measures physical-location granularity.

## 2.4 Architecture retained as WIP

The intended architecture remains a read-only post-process that consumes a historical Core Test or S-1 participant roll. Tier selection must not alter Cost, Outcome, Failure XP, Double eligibility or Recovery.

Tier 0 generates no location state. Tier 2 remains a future high-granularity module; its location procedure, armour and surgery interaction, anatomical mapping and resolution cost are unresolved.

For Tier 1, the Location Index is a numeric intermediate value, not a body-part name. An anatomical mapping table is still required and is not canonical.

## 2.5 Open design questions

- whether the location tier is universally fixed or selected by situation, scene or campaign — **still open.** The candidate invocation policy determines *when a Location Index is warranted within whatever tier is in use*; it does not determine *whether a scene/campaign uses Tier 0, Tier 1, or Tier 2* in the first place. The candidate policy is a relevant input to that future decision, not a resolution of it.
- when Tier 1 is invoked (attack-side) — **the mechanism for this is now addressed** (the candidate invocation policy directly answers "does this specific resolution warrant a Location Index"), but this is narrower than the scene/campaign tier-selection question above, which remains open.
- **whose roll, if any, supplies a Location Index for non-attack physical resolutions (hazards, falls, structural interactions with no adversarial "attacker") — RESOLVED BY DESIGNER RULING (see §2.5A immediately below). No longer an open question in the "undecided" sense; it is a closed deferral pending an explicit future reopening trigger.**
- the anatomical mapping table (numeric Location Index → structural/anatomical component) — still open, untouched by this investigation. This includes the structural-destruction case in §2.1A's Conceptual Anchor table: its State-2 status establishes narrative resolvability only, not a settled mapping.
- Tier-2 procedure and resolution cost — still open, untouched.
- interaction with wounds, armour, defence and Outcome Effects — still open; the investigation's State-3 findings (Disarm, Equipment, Impairment, Armor Bypass, Incapacitation all currently unanchored to location) are directly relevant inputs to this future work.
- final GM-facing wording for the simplified invocation procedure (§2.1A) — drafted, not yet separately validated.

## 2.5A Non-Attack Location Index Source — Designer Ruling (New in v1.4.3)

**Status: Designer Ruling. Closes the S-2 Non-Attack Location Index Source investigation (starter brief v1.1) as a deferral. Not a Canonical change; recorded here as the current non-canonical governing position until formally promoted.**

> **Ruling: Non-attack physical resolutions (falls, hazards, structural collapses, and other non-adversarial physical events) generate no Tier-1 Location Index under current design — categorically, regardless of GM framing, stated stakes, or whether a governing Core Test exists for the resolution. This is a deferral, not a claim that non-attack location is impossible in principle.**

This applies regardless of:

- whether an underlying Core Test exists for the resolution;
- who made that test (the affected character, the causing character, a third party);
- whether the hazard was caused intentionally or accidentally;
- how specifically the GM narrates the physical consequence;
- the severity of the consequence.

**Zero-Step Location Index generation remains attack-side only** under current design. The canonical Zero-Step mechanism itself (Canonical §14.1–§14.2) is entirely untouched by this ruling — this ruling only concerns whether non-attack resolutions are eligible to invoke it at all, and the answer is currently no.

**Investigation record retained, not deleted:**

| Item | Status |
|---|---|
| H0 (governing Core Test provenance rule) | Retained as an inert candidate record — a starting hypothesis if this question is reopened, not a validated operative rule |
| H0 Rider A (no cross-character roll-sharing) | Retained, inert, tied to H0 |
| H0 Rider B (multi-test causal-chain tie-break) | Retained, inert, tied to H0 — two sub-options were identified but never adjudicated against each other |
| GM-authored hazard warrant (rejected candidate direction) | Rejected for now, not deleted from the record |
| Named-Outcome/Warrant Test transfer to non-attack cases | Deferred, not resolved — moot while non-attack generation is off entirely |
| Blind provenance trial | Not authorized — correctly withheld, since the category is closed |

**Reopening conditions.** This ruling is a deferral tied to specific future work, not a permanent architectural conclusion. It should be **explicitly reopened**, not silently inherited, when:

- **S-4** (Wound activation/severity) reaches a design stage where localized non-attack injury becomes relevant;
- **S-7** (Incapacitation/death) reaches a design stage where hazard severity needs finer resolution than flat damage;
- **S-8** (Difficulty/Stakes Gate) reaches a design stage where hazard-stakes framing is formally defined — flagged as the most likely natural reopening trigger.

When reopened, H0 and its riders serve as a starting hypothesis to re-validate against whatever S-4/S-7/S-8 actually specify — not a pre-approved answer to carry forward unexamined.

**Does not affect:** Zero-Step (attack-side), S-1, the attack-side invocation/warrant policy (§2.1A), Structural Weak Points' State-2 classification, the W3 cache, or Tier 0/1/2 scene-selection policy. None of these are reopened by this ruling.

## 2.6 E9 human usability playtest

**Evidence class: Empirical finding — passed for the tested physical two-d10 method only.**

The E9 playtest used two physical d10s with 50 participants in ten groups of five:

- 25 participants new to RPGs; and
- 25 RPG players new to Tiwas.

Participants reported no difficulty rolling the dice or exchanging the digits for hit location, and feedback was positive.

This evidence supports usability of Zero-Step **for the tested physical two-d10 method only**. It does **not** establish usability for:

- a single d100;
- a digital roller;
- verbally announced results;
- other input methods.

Those methods were not tested and are not covered by this finding. E9 did not settle the remaining S-2 architecture.

## 2.7 Future optional-rule observations

**Observation ≠ proposal ≠ rule.**

Participants asked whether they could choose the natural or swapped number. That remark is a design observation only. It is not a proposal under active consideration, and it is not a current rule. The canonical basic rule remains deterministic and provides no such choice.

For a future optional-rule appendix, the designer may consider:

1. attacker choice granted only by an explicit special ability; and
2. defender choice.

Neither option is authorised for current play, nor does this section recommend one. This observation is retained, not expanded.

## 2.8 Comparative derivation-cost residual

Separate from E9, the completed comparison found that Units-Digit requires 0–1 additional derivation operations across the examined rolling modes, while Zero-Step requires 1–2.

This is a **structural comparison of derivation steps, not a human-usability result** and not an additional E9 label. It cannot substitute for input-method-specific usability testing.

The physical two-d10 playtest does not establish comparative usability for other input methods. Any future optional mode or implementation should test its own presentation method if human usability matters to that decision.

---

# 3. S-3 — Outcome Effects

**Status: Reserved / Proposed Architecture**

Tiwas is intended to resolve opposed contests into meaningful state change rather than simple HP attrition.

A short universal Effect menu is preferred.

## 3.1 Candidate Effect menu

1. Inflict Injury.
2. Impose Condition.
3. Disarm / Break Hold.
4. Force Movement / Seize Position.
5. Seize Tempo.
6. Guard Break.
7. Bleed / Ongoing Drain.
8. Open Retreat / Compel Yield.
9. Damage Equipment.
10. Choose Location.

The final menu, trigger rules, purchasing rules, and numerical thresholds remain unresolved.

## 3.2 Effect purchasing

Current proposal:

- one successful contest may produce a basic/free effect;
- additional effects may require Net Advantage / Quality bands;
- some effects may be gated by Tags;
- some exceptional effects may be tied to qualifying successes.

This is not canonical.

## 3.3 Non-negotiable architectural constraint

Effects must never modify the historical die roll.

---

# 4. S-4 — Two-Track Harm and Wounds

**Status: Reserved / WIP Direction**

The current design direction separates:

### Track A — Resources / Global HP

Physical Energy and MP are the primary endurance layer.

Resource exhaustion can create Overflow → HP damage.

### Track B — Localized Wounds / Conditions

Where locations are active, meaningful physical injury can produce localized Wounds and Conditions.

The intended Wound states are currently:

- Light;
- Serious;
- Critical.

Exact activation thresholds, severity formulas and consequences are unresolved.

## 4.1 Design constraints

- Empty PE/MP must not automatically mean defeat.
- Overflow remains HP damage.
- HP = 0 should not automatically equal death.
- Wounds are not intended to become a second conventional HP pool.
- Injury must remain consequential without producing excessive permanent character loss.

---

# 5. S-5 — Armor

**Status: Reserved / Proposed**

Current candidates include:

- Bypass-style armour interaction;
- tag-gated Sunder interaction.

The intended architecture is to use Armor Traits/Tags rather than create a second durability economy.

Final armour interaction remains unresolved.

---

# 6. S-6 — Defense

**Status: Reserved / Proposed**

Defense is intended to operate as part of the universal contest architecture.

Candidates include:

- passive defense;
- active defense;
- defense as a normal contest participant;
- resource-costed reactions.

A previous proposal suggested a Passive Guard approach based on half-Skill with no PE cost.

That is a **candidate only**, not a Tiwas rule.

The final model must be evaluated for:

- resource drain;
- number of rolls;
- survivability;
- tactical choice;
- resolution-step count.

---

# 7. S-7 — Incapacitation and Death

**Status: Reserved**

The current direction favours heroic resilience.

Important current design constraints:

- HP = 0 should not automatically mean death.
- Incapacitation should be mechanically distinct from ordinary resource depletion.
- Serious localized injury may matter where locations are active.
- Permanent character loss should remain comparatively uncommon.

Possible major-vital/death-check concepts remain proposals only.

No final death threshold is locked.

---

# 8. S-8 — Difficulty, Task Adjudication and Stakes

**Status: Reserved / WIP Direction**

A universal difficulty system is required.

The current direction is that difficulty should operate on the **Skill side** rather than altering the natural die face.

The natural roll must remain the natural roll because it determines:

- Cost;
- Failure XP;
- Double status;
- Recovery interaction.

A **Stakes Gate** is also proposed:

> Not every action needs a test. A test should occur where meaningful uncertainty and meaningful consequences exist.

Routine actions without meaningful stakes should not be turned into repetitive resource expenditure merely because a Skill exists.

Exact difficulty grades and Failure XP interaction remain unresolved.

**Note (v1.4.3):** the closed S-2 Non-Attack Location Index Source ruling (§2.5A) flags S-8 as its most likely reopening trigger, since Stakes Gate is the natural home for deciding when a hazard resolution carries enough mechanical weight to warrant location-level detail. This is a cross-reference only; it does not narrow or predetermine S-8's own design.

---

# 9. S-9 / S-10 — Extended Tests

**Status: Proposed Universal Play Module**

Extended Tests are intended for:

- research;
- crafting;
- travel;
- environmental hazards;
- sieges;
- prolonged social work;
- rituals;
- technical projects;
- other multi-interval tasks.

## 9.1 Core principle

Every interval is an ordinary Tiwas test.

Therefore each interval preserves:

- Cost = Roll;
- Overflow → HP;
- Failure XP;
- failed Doubles;
- Advanced Skill creation;
- Recovery.

## 9.2 Progress

Candidate methods:

### Margin accumulation

Accumulate successful Quality/Margin values until a target is reached.

### Success count

Accumulate successful intervals until a target count is reached.

The final method is unresolved.

## 9.3 Failure behaviour

Candidates include:

- stall;
- progress loss;
- complication;
- conversion into another task state.

The current direction favours **stall as the default**, with progress loss potentially treated as an optional complication.

## 9.4 No Progress currency

Extended Test Progress must never become:

- spendable points;
- transferable currency;
- an XP substitute;
- a second advancement economy.

It is merely a running record of previous test outcomes.

---

# 10. Conditions

**Status: Reserved / Architectural Requirement**

Conditions should represent character/world state.

They must remain distinct from Tags.

Examples may include:

- Stunned;
- Prone;
- Impaired;
- Bleeding;
- Restrained.

Final condition definitions, stacking, durations and removal procedures remain unresolved.

---

# 11. Tags

**Status: Reserved / Architectural Requirement**

Tags are classification and permission metadata.

Potential consumers include:

- weapons;
- armour;
- Effects;
- locations;
- powers;
- creatures;
- settings.

Tags are not Conditions.

---

# 12. Time / Action Economy

**Status: Reserved / Architectural Requirement**

A unified temporal model is required for:

- combat rounds;
- turns;
- actions;
- reactions;
- movement;
- intervals;
- ongoing Effects;
- Conditions;
- Rest;
- Extended Tests.

The same temporal architecture should serve combat and non-combat activities.

---

# 13. Equipment

**Status: Reserved**

Required areas include:

- weapons;
- armour;
- equipment records;
- equipment Traits;
- Tags;
- encumbrance;
- carrying;
- equipment damage;
- repair/replacement;
- wealth/economy hooks.

Equipment should modify existing Universal Play systems rather than introduce a new resolution engine.

---

# 14. Environmental Hazards

**Status: Reserved / Architectural Direction**

Preferred structure:

```text
Trigger
  ↓
Existing Test
  ↓
Natural Cost
  ↓
Outcome
  ↓
Existing Effect / Condition / Harm
```

Hazards should not require hazard-specific currencies.

**Note (v1.4.3):** per §2.5A, hazards resolved through this structure do not currently generate a Tier-1 Location Index, regardless of how the Outcome is narrated. This is unchanged by the present section and is cross-referenced here only for clarity.

---

# 15. Magic and Special Abilities

**Status: Design Direction / Not Fully Defined**

Current direction is that magic and special abilities emerge through Advanced Skills.

A setting can grant permission for a Skill lineage to represent:

- magic;
- martial techniques;
- supernatural abilities;
- technology;
- psychic abilities;
- other special capabilities.

The current direction rejects a mandatory fixed spell-list system in the Core.

A setting may optionally add a spell curriculum.

## 15.1 Intended interaction

A magical or special ability should continue to use:

- the ordinary Skill test;
- Cost = Roll;
- MP or lineage-defined resource domain;
- Overflow;
- Failure XP;
- Advanced Skill creation;
- Quality;
- Effects.

This remains architectural direction rather than complete rules.

---

# 16. NPC Compression

**Status: Reserved / S-12**

NPCs should use compressed representations of the same underlying system rather than a separate NPC resolution engine.

Exact grades/packages remain unresolved.

---

# 17. Setting Modules

**Status: Design Direction**

The intended boundary is:

```text
Core
  ↓
Universal Play
  ↓
Setting Module
```

A setting may define:

- permissions;
- content;
- creatures;
- equipment;
- technologies;
- magic;
- setting-specific Tags;
- setting-specific Effects.

A setting must not redefine the Core invariants.

---

# 18. Design Direction Summary

Current architectural direction:

```text
TIWAS CORE
├── d100 roll-under
├── 100-Fumble
├── Cost = Roll
├── Overflow → HP
├── Failure XP
├── Skill Roll Pool
├── Advanced Skills
└── Core Recovery

UNIVERSAL PLAY
├── Opposed Contests
├── Difficulty / Stakes
├── Effects
├── Extended Tests
├── Time
├── Conditions
├── Tags
├── Harm / Wounds
├── Locations
├── Armor
├── Defense
├── Equipment
├── Hazards
├── Rest / Healing
└── NPC procedures

SETTING MODULES
├── Fantasy
├── Science Fiction
├── Modern
├── Horror
├── Historical
└── Cinematic
```

---

# 19. Explicitly Experimental Material

## S-1D — Committed / Guarded Stance

**Status: Experimental — excluded from canonical S-1**

This earlier tactical overlay must not be confused with Hybrid Committed.

It is retained only as historical design material.

No current Tiwas subsystem depends on it.

---

# 20. Open Residual Decision Register

| ID | Decision | Current status |
|---|---|---|
| S-2 | Broader hit-location architecture: tier policy, mapping and downstream interaction. Zero-Step (Tier-1 Location Index provider) is locked. **Invocation/warrant policy (attack-side): candidate accepted (S-2 Design Investigation v1–v5), non-canonical, pending promotion. Non-attack Location Index generation: RULED — deferred, none generated until S-4/S-7/S-8 reopens the question (§2.5A).** Anatomical mapping, Tier-2 procedure remain fully open. | Partially locked / WIP — Tier-1 provider locked; candidate invocation policy accepted for further development; non-attack question closed as a deferral |
| S-3 | Effect thresholds/purchasing | Open |
| S-4 | Wound activation/severity | Open |
| S-5 | Armor interaction | Open |
| S-6 | Defense model | Open |
| S-7 | Incapacitation/death | Open |
| S-8 | Difficulty/task/stakes | Open |
| S-9 | Extended Test progress | Open |
| S-10 | Extended Test failure loss | Open |
| S-11 | Rest/healing timelines | Open |
| S-12 | NPC compression | Open |

No row in this register is a canonical rule. Status labels here do not promote a proposal, observation, or design direction into a locked mechanic.

---

# 21. Promotion Rule

This section is a **governance clarification**, not a change to game mechanics.

A proposal in this document may become canonical only after all of the following:

1. its design question is explicitly identified;
2. competing alternatives have been considered where appropriate;
3. relevant simulation/analysis has been completed;
4. the human designer has accepted the ruling;
5. the mechanic is documented as a formal rule;
6. the Canonical Rules & Changelog document is updated;
7. the former proposal is marked Superseded or Locked here;
8. implementation documentation is updated.

A detailed proposal is not a rule merely because it is detailed. A detailed LLM draft is not a rule. Locked mechanics in the Canonical Rules can be reopened only through normal design governance and substantive evidence.

Until those steps are complete, material in this repository remains non-canonical regardless of how fully it is described.

---

# 22. v1.4.1 Revision Record

v1.3 remains the authoritative baseline for subsystem content, candidate mechanics, status classifications, architecture, residual decisions, and S-1D historical treatment.

v1.4.1 does not adopt the proposed v1.4 draft as a new design state. It incorporates selected documentation and governance corrections:

- heading **Locked Design Direction** replaced with **Current Design Direction**, so this repository is not read as a second lock file;
- explicit cross-document authority statement added at the head of the document;
- S-2 status wording aligned with the Canonical limited lock: Zero-Step / Tier-1 Location Index provider locked; S-2 unfinished;
- E9 limited to the tested physical two-d10 method, with other input methods explicitly untested;
- derivation-cost comparison kept separate from E9 and labelled as structural, not a human-usability result;
- observation / proposal / rule distinction stated for the attacker-choice / defender-choice remark, without expanding that material;
- promotion process retained as an eight-step governance rule, not a mechanical change;
- Canonical Rules citation in §2.1 updated to v1.3;
- evidence is explicitly distinguished from the designer ruling/mechanic that may later be informed by that evidence.

No unresolved subsystem is advanced to canonical status by this revision.

---

# 23. v1.4.2 Revision Record

Section 2 (S-2 — Hit-Location Architecture) replaced with the S-2 Design Investigation v1–v5 candidate invocation/warrant policy — a four-state internal classification, the Named-Outcome Test, the Conceptual Anchor findings table, and the revised W3 cache role — accepted as the current non-canonical working direction for S-2's invocation question. This is **not** a promotion to Canonical status; see §21.

§2.5 open-questions list updated to reflect what the investigation resolved (when Tier 1 is invoked, for a given resolution) versus what it explicitly did not (scene/campaign tier selection; anatomical mapping; non-attack Location Index source; final GM-facing wording). §20's S-2 row updated to match.

Two designer rulings recorded by this candidate policy: explicit-only objectives (the GM does not infer a distinct mechanical objective from location or context alone), and acceptance of the synthesis itself as the current non-canonical candidate.

Corrections applied to the incoming investigation material after independent review, before this merge:

- Armor Bypass basis reworded — no longer overclaims a "contradiction" the cited source text (§5, this document) doesn't actually contain. State/Anchor classification unchanged (still State 3 / Unanchored — a documented alternative mechanism is what the test requires, and one exists).
- Lazy evaluation flagged as design inference, not an empirically confirmed procedural rule like the other three riders in §2.1A.

**Second correction round, same v1.4.2 pass (designer ruling, not a wording fix):** Structural Weak Points reclassified from **State 1 to State 2** (Established, Not Yet Resolvable) in §2.1A's Conceptual Anchor table. The State-1 definition requires current rules to provide a mechanism to act on the result, not merely that a GM could narrate one — "ordinary narration" is available to every category and cannot be what distinguishes State 1, or the State 1/2/3 distinction collapses entirely. Structural Weak Points remains Anchored (no competing non-location mechanism is proposed for it, unlike Disarm/Armor Bypass), but anchored-without-a-resolution-mechanism is what State 2 is for. Practical effect: Zero-Step does not currently generate a Location Index for this category; the W3 cache now has zero State-1 (Active/Generate) entries, which is an accurate reflection of current design completeness rather than a defect.

No Canonical Rules changed. S-2 remains unlocked beyond the existing Zero-Step Tier-1 provider lock (Canonical §14.1–§14.2). Nothing in this revision is promoted to Canonical status.

The former Section 2 text (as it stood in v1.4.1) is superseded by the text above but retains historical significance as the pre-investigation state of S-2 documentation.

---

# 24. v1.4.3 Revision Record

A follow-on, narrower investigation (S-2 Non-Attack Location Index Source, starter brief v1.1) examined whether, and whose, natural roll supplies a Location Index for non-attack physical resolutions (falls, hazards, structural collapses with no adversarial "attacker"). The investigation proceeded through a provenance-only stress test (candidate rule H0: "governing Core Test's roll, or no index," plus two riders on cross-character and multi-test causal-chain cases) while deliberately keeping the separate warrant-transfer question (whether the existing player-declaration-based Named-Outcome Test can be satisfied by a GM-stated hazard consequence) unresolved and unscored.

**Designer ruling (this revision):** Non-attack physical resolutions generate no Tier-1 Location Index under current design — categorically, regardless of GM framing, stated stakes, or whether a governing Core Test exists for the resolution. This is recorded in the new §2.5A. It is a deferral, not a claim that non-attack location is impossible in principle, and it is explicitly tied to reopening triggers: S-4 (Wound activation/severity), S-7 (Incapacitation/death), and S-8 (Difficulty/Stakes Gate), with S-8 flagged as the most likely natural trigger.

Direct effects of this ruling:

- The GM-authored-stakes candidate for warrant transfer is rejected for now (not deleted from the record).
- The H0 provenance rule and its two riders are retained as an inert candidate record — a starting hypothesis if this question is reopened, not a validated operative rule.
- No blind provenance trial was run, correctly, since the ruling makes warrant-eligibility categorically "never" for the affected category, leaving nothing live to stress-test.
- §2.5's open-questions list updated to move this item from open to resolved-as-deferral.
- §20's S-2 row and §14 (Environmental Hazards) updated with a cross-reference.
- §8 (S-8) annotated with a cross-reference to the reopening-trigger flag; S-8's own design scope is not narrowed or predetermined by this note.

This ruling does not reopen, alter, or narrow: Zero-Step (attack-side, Canonical §14.1–§14.2), S-1, the attack-side invocation/warrant policy (§2.1A), the Structural Weak Points State-2 classification, the W3 cache, or Tier 0/1/2 scene-selection policy. No Canonical Rules changed. Nothing in this revision is promoted to Canonical status; see §21.

The former §2.5 non-attack bullet (as it stood in v1.4.2, "still open") is superseded by the ruling recorded in §2.5A but retains historical significance as the pre-ruling open-question state.
