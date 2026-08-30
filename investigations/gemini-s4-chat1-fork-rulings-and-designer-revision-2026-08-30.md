# Gemini 3.6 Flash — S-4 Session Chat 1 (Fork Rulings & Designer Revision)

**Date:** 2026-08-30
**Model:** Gemini 3.6 Flash
**Status:** Non-canonical design evidence — LLM session transcript record

---

Based on my analysis of the key files, I now have a comprehensive understanding of the S-4 decision forks. Let me rule on S-4 by resolving the decision forks in order, starting with F1 (activation trigger).

## S-4 (Wound Activation/Severity) Decision

### F1: What triggers a Wound vs. plain Overflow→HP?

**Ruling: (a) Location-gated — fires only if a Location Index was active for the hit.**

**Evidence and Reasoning:**

1. **S-3/S-4 Boundary Ruling (DEC-029/Q-S3-4):** The S-3 designer rulings explicitly state: "No S-3/S-4 interface is currently prototyped because base-tier Injury is HP-only. The Roadmap §10 boundary holds and is dormant. The **S-4 direction** (location-based injury from repeated hits; no Location Index → no Injury; per-location hit-history by GM adjudication; healing open) is a **steer for a future S-4 investigation**, not an S-3 ruling and not Canonical."

2. **S-3 Designer Rulings and Handoff (2026-08-29):** The direction captured for the future S-4 investigation states: "A **location-based injury system** is the preferred future direction for S-4: localized, lasting (non-HP) injury should emerge from **repeated hits to the same body location**, using the Zero-Step Location Index as the natural rarity control — this supports Core Priority 2 (heroic resilience / low permanent character loss) by making significant injury a product of accumulated bad luck rather than a single tunable threshold."

3. **Explicit Constraint:** "**No Location Index → no Injury Effect, ever, full stop.** Tier-0 scenes (which generate no Location Index, per Proposals §2.3) can never produce localized injury."

4. **S-2 Non-Attack Deferral Connection:** The S-2 non-attack deferral ruling (DEC-020) explicitly ties its reopening to S-4 reaching "a design stage where localized non-attack injury becomes relevant." This creates a logical dependency where S-4 must establish location-gated wound activation before non-attack hazards can produce wounds.

5. **Consistency with S-3 Effect Menu:** The base-tier S-3 Effect "Inflict Injury" is explicitly HP-only (plain damage; does not touch S-4 wounds). This confirms that wound generation is separate from basic injury and requires additional gating.

6. **Alternative Rejected:** The margin/tag-gated alternative (F1b) is inconsistent with:
   - The explicit S-4 direction stating "location-based injury system is the preferred future direction"
   - The requirement that "no Location Index → no Injury Effect"
   - The S-3 ruling that base Injury is HP-only and does not produce wounds
   - The need to maintain heroic resilience by making significant injury dependent on accumulated location-specific hits rather than single high-margin hits

**F1 Resolution: Location-gated activation is ruled in.**

### F2: Do Track A and Track B resolve exclusively, or can both apply from one hit?

**Status: OPEN**

**Reasoning:**
- The Roadmap and proposals describe Track A (Resources/Global HP) and Track B (Localized Wounds/Conditions) as separate tracks but do not specify their interaction.
- The S-4 direction mentions "two-track harm" but does not clarify exclusivity.
- No designer ruling or canonical rule addresses whether both tracks can apply simultaneously from one hit.
- Resolving this requires explicit designer input to avoid assumptions that could imbalance the system.

### F3: Severity formula for Light/Serious/Critical

**Status: OPEN** (requires simulation gate before locking)

**Required Simulation Gate:**
Before any numeric threshold can be locked for wound severity, the following must be measured:
- Effect frequency (how often wounds are generated)
- Exchange length (average combat duration)
- Resource expenditure (PE/MP consumption patterns)
- Wound frequency (rate of wound generation)
- Severe-injury rate (progression to Serious/Critical states)

No numerical threshold may be locked without this simulation gate + explicit designer ruling.

### F4: Wound-state consequences (Conditions/Disability per state)

**Status: OPEN**

**Reasoning:**
- No candidate recorded for consequences per wound state.
- The S-4 direction mentions Wound states are "Light / Serious / Critical — names only, no thresholds defined."
- Consequences remain entirely undecided in the corpus.

### F5: Anatomical mapping dependency

**Status: OPEN** (inherently tied to F1a)

**Reasoning:**
- Any location-gated Wound model (F1a) inherits the blocker from OPEN-003 (anatomical mapping).
- Structural Weak Points is stuck at State 2 precisely because no Location Index → body-component mapping exists.
- Anatomical mapping table (Location Index → body/structural component) is still open and untouched.

### F6: Interaction with S-2 non-attack deferral (DEC-020)

**Status: CONDITIONALLY RESOLVED**

**Reasoning:**
- Under F1a (location-gated), hazards could never produce Wounds until S-4 explicitly reopens DEC-020.
- The S-2 non-attack deferral ruling states it should be "explicitly reopened, not silently inherited, when: S-4 (Wound activation/severity) reaches a design stage where localized non-attack injury becomes relevant."
- Since we have ruled F1a (location-gated), this creates the condition for reopening DEC-020 when S-4 wound activation design progresses to include non-attack physical resolutions.
- **However, reopening DEC-020 is not being done now** - it remains a deferral pending explicit future work on S-4 that includes non-attack hazard wound generation.

---

## Summary of S-4 Decision

### RULED (Can be closed now):
- **F1**: Location-gated activation — Wounds trigger only if a Location Index was active for the hit (rejected margin/tag-gated alternative)

### REMAIN OPEN:
- **F2**: Track A/Track B interaction (exclusive or concurrent application)
- **F3**: Severity formula (requires simulation gate first)
- **F4**: Wound-state consequences
- **F5**: Anatomical mapping dependency (inherent blocker for F1a)
- **F6**: S-2 non-attack deferral interaction (conditionally resolved - DEC-020 remains deferred but will be reopened when S-4 includes non-attack hazard wound generation)

---

## Implementation Requirements

Any future S-4 work must:
1. Implement location-gated wound activation (F1a ruling)
2. Preserve the anatomical mapping dependency (OPEN-003 blocker)
3. Not lock any numeric thresholds (F3) without completing the required simulation gate
4. Treat DEC-020 (S-2 non-attack deferral) as remaining closed until explicitly reopened for non-attack hazard wound generation
5. Maintain strict separation between Track A (Overflow → HP damage) and Track B (Localized Wounds) pending F2 resolution
6. Not modify historical die rolls or violate any Canonical/Core invariants

---

---

# Designer Decision (inserted after Gemini's initial ruling)

**Designer decision:** overflow will never cause wounds.
From what I understand, injury / wound is a possible selectable effect from a successful skill check.
No location index, no injury / wound.
In fact, we should rule on terminology here. Injury is hit point damage. Wound is a lasting effect not hit point damage.
S-3 has ruled for effects from a success which are gated.
Localized wound is recorded. Caused by an action which caused an effect.
Intended wound states should only be recorded numerically. More wounds = more severe. A single wound might not bother an adult, but would be dangerous to a child. Each individual wound is functionally equivalent. Healing wounds is a numerical process.
It would be possible for greater wounds to be inflicted, but these would be chosen as an effect and would be independent of a normal wound. Compare to an effect of frost, fire, shock. Serious frost, serious fire, serious shock could be chosen as an effect, but would not change the state of the lower versions of the effect.
This would also mean healing might not be able to cure higher levels of effects.
Because S-3 ruled for gated effects, the "repeated hits to the same body location" idea no longer applies. Effects are a choice.
S-2 Non Attack Deferral Connection should no longer be an issue as an effect is a choice now. Non attack hazards are capable of causing damage or wounds.

---

# Gemini 3.6 Flash — Revised S-4 Ruling (Post-Designer Decision)

Understood — revising S-4 per the designer decision. Yes, I understand:

- Overflow is exclusively Track A/HP damage; it never causes Wounds. This is a global rule.
- Injury = HP damage.
- Wound = localized, lasting state, counted numerically (e.g., number of wounds), not HP. Each individual Wound is functionally equivalent in its base form.
- Severity of Wounds is numerical (more wounds = more severe), and healing is a numerical process.
- Greater Wounds are "Effect" choices, independent of normal wounds, and do not change the state of lower versions of the effect (e.g., "Serious Frost" is a distinct Effect, not an upgrade to "Frost"). Healing might not cure higher levels of such Effects.
- This fundamentally changes the S-4 architecture.

---

# Gemini 3.6 Flash — Revised S-4 (Wound Activation/Severity) Decision

## Terminology Lock
- **Injury:** Refers to Hit Point (HP) damage (Track A harm).
- **Wound:** Refers to a localized, lasting state, tracked numerically, distinct from HP damage (Track B harm). Each individual Wound is functionally equivalent at its base level.

## F1: What triggers a Wound vs. plain Overflow→HP?

**Revised Ruling:** Wounds are exclusively triggered as a selectable Effect from a successful S-1 contest.

**Evidence and Reasoning:**
- Designer Decision: "overflow will never cause wounds." This establishes that Overflow is solely for HP damage (Track A).
- S-3 Ruling (DEC-024): "Flat one-Effect-per-win." A successful S-1 contest earns exactly one Effect.
- S-3 Ruling (DEC-025): "Pure declared intent (no Skill-side gating)." Effects are granted solely by the declared outcome of a successful S-1 contest.
- S-3 Ruling (DEC-031): "Quality gates eligible Effects." Higher Quality unlocks access to more severe/narratively significant Effects, including those that might produce Wounds.
- Location Gating: "no location index, no injury / wound" (from designer input). This means that a Location Index is a prerequisite for choosing a Wound Effect, not the trigger for the Wound itself. The trigger is still the successful Effect selection.
- Rejection of "Repeated Hits": The designer clarifies that "because S-3 ruled for gated effects, the 'repeated hits to the same body location' idea no longer applies. effects are a choice." This supersedes the previous S-4 direction recorded in DEC-029.

**F1 Resolution:** Wounds are exclusively triggered as a selectable Effect from a successful S-1 contest. This Effect requires a Location Index if the Wound is localized.

## F2: Do Track A and Track B resolve exclusively, or can both apply from one hit?

**Ruling:** Both Track A (Overflow→HP) and Track B (Wound Effects) can apply from one hit.

**Evidence and Reasoning:**
- Designer Decision: "overflow will never cause wounds" clarifies that Overflow does not produce wounds, but does not preclude both types of harm from one hit.
- Core Test Transaction (D1 §6): This is locked and includes "Pay Cost... Apply Overflow if the resource pool cannot pay the full cost." This is the source of Track A harm.
- S-3 Effects (DEC-024): "one successful contest may produce a basic/free effect." This means a successful S-1 contest allows selection of an Effect.
- Sequential Resolution: The Core Test Transaction (D1 §6) is sequential. A hit resolves its resource cost and potential Overflow first. After that, if the attack was successful, an Effect is chosen and applied. There is no conflict in this sequence allowing both.
- No Mutual Exclusivity Constraint: No canonical or design direction document explicitly states mutual exclusivity.

**F2 Resolution:** Both Track A (Overflow→HP) and Track B (Wound Effects) can apply from one hit, resolving sequentially according to the Core Test Transaction and then S-3 Effect application.

## F3: Severity formula for Light/Serious/Critical

**Revised Ruling:** Wound severity is numerical (e.g., number of Wounds inflicted). The terms Light/Serious/Critical are descriptive categories for accumulations of these numerical Wounds, not distinct Wound states themselves. Formulas for these numerical thresholds require a simulation gate before locking.

**Evidence and Reasoning:**
- Designer Decision: "intended wound states should only be recorded numerically. more wounds = more severe. a single wound might not bother an adult, but would be dangerous to a child. each individual wound is functionally equivalent. healing wounds is a numerical process." This explicitly defines Wounds as numerical and equivalent at base.
- Designer Decision: "It would be possible for greater wounds to be inflicted, but these would be chosen as an effect and would be independent of a normal wound. compare to an effect of frost, fire, shock. serious frost, serious fire, serious shock could be chosen as an effect, but would not change the state of the lower versions of the effect." This clarifies that "greater wounds" (like Serious Frost) are distinct Effects, not more severe Wound counters.
- Simulation Gate Requirement (Roadmap §10): "Do not lock numerical thresholds without required evidence and a designer ruling." This still applies to the numerical thresholds for descriptive categories (Light, Serious, Critical).

**F3 Resolution:** Wound severity is numerical. Light/Serious/Critical are descriptive categories for accumulated numerical Wounds. Specific numerical thresholds for these categories require simulation.

## F4: Wound-state consequences (Conditions/Disability per state)

**Revised Ruling:** Consequences of Wounds are tied to their numerical accumulation (e.g., reaching a "Serious" numerical threshold). Consequences of distinct "Greater Wound" Effects are tied to those specific Effects. Both require definition.

**Evidence and Reasoning:**
- Designer Decision: "more wounds = more severe." This implies that consequences scale with the numerical count of Wounds.
- Designer Decision: "greater wounds... would be chosen as an effect and would be independent of a normal wound." This means "Serious Frost" (an Effect) would have its own defined consequences, distinct from the numerical accumulation of generic Wounds.
- Still Open: No specific consequences or disabilities have been defined for either numerical Wound accumulation or the "Greater Wound" Effects.

**F4 Resolution:** Consequences are tied to numerical Wound accumulation and/or specific "Greater Wound" Effects. These consequences remain OPEN and require definition.

## F5: Anatomical mapping dependency

**Revised Ruling:** Anatomical mapping (Location Index → body/structural component) remains a blocker (OPEN-003) for any localized Wound Effect, as Wounds are location-gated.

**Evidence and Reasoning:**
- F1 Ruling: "no location index, no injury / wound" (from designer input). This explicitly makes a Location Index a prerequisite for a Wound Effect.
- Existing Blocker (OPEN-003): "Anatomical mapping (Location Index → body/structural component) is still open, untouched by this investigation."
- Structural Weak Points: Remains at State 2 ("Established, Not Yet Resolvable") precisely because this mapping is missing.

**F5 Resolution:** Anatomical mapping remains a critical dependency for localized Wound Effects.

## F6: Interaction with S-2 non-attack deferral (DEC-020)

**Revised Ruling:** The S-2 non-attack deferral (DEC-020) is reopened by the S-4 design. Non-attack physical resolutions can produce Wounds if a Wound Effect is successfully applied and a Location Index is generated.

**Evidence and Reasoning:**
- Designer Decision: "non attack hazards are capable of causing damage or wounds." This directly contradicts DEC-020's categorical exclusion of Location Index generation for non-attack physical resolutions.
- DEC-020 Reopening Condition: DEC-020 explicitly states it should be reopened when "S-4 (Wound activation/severity) reaches a design stage where localized non-attack injury becomes relevant." This condition has been met by the designer's explicit statement.
- New Mechanism: The mechanism for non-attack Wounds would be the successful application of a Wound Effect (F1 ruling), and the generation of a Location Index through a newly defined process for non-attack scenarios.

**F6 Resolution:** The S-2 non-attack deferral (DEC-020) is reopened. Non-attack physical resolutions can produce Wounds via a Wound Effect, provided a Location Index can be generated for such scenarios.

---

## New Open Fork

This now creates a new open fork related to DEC-020:

**OPEN-S4-A:** How is a Location Index generated for non-attack physical resolutions (e.g., hazards, falls) that lead to a Wound Effect?
- The previous H0 (governing Core Test provenance rule) and its riders in DEC-022 are "inert candidate records" and a "starting hypothesis to re-validate." They are not a pre-approved answer.
- The "Warrant-transfer question (Direction 1, or a new alternative)" also needs to be decided for non-attack cases.

---

## Summary of Revised S-4 Decisions

### RULED:
- Terminology: Injury = HP damage. Wound = localized, lasting numerical state.
- F1 (Wound Trigger): Wounds are exclusively triggered as a selectable Effect from a successful S-1 contest. Requires a Location Index if localized.
- F2 (Track A/B Interaction): Both Track A (Overflow→HP) and Track B (Wound Effects) can apply from one hit, sequentially.
- F3 (Severity): Wound severity is numerical. Light/Serious/Critical are descriptive categories for accumulated numerical Wounds.
- F6 (S-2 Non-Attack Deferral): DEC-020 (S-2 non-attack deferral) is reopened. Non-attack physical resolutions can produce Wounds if a Wound Effect is successfully applied and a Location Index is generated.

### REMAIN OPEN:
- F3 (Severity Thresholds): Specific numerical thresholds for Light/Serious/Critical categories (requires simulation).
- F4 (Consequences): Consequences of numerical Wound accumulation and/or specific "Greater Wound" Effects.
- F5 (Anatomical Mapping): Anatomical mapping (Location Index → body/structural component) (OPEN-003).
- OPEN-S4-A (Non-Attack Location Index Generation): How a Location Index is generated for non-attack physical resolutions when a Wound Effect is applied.