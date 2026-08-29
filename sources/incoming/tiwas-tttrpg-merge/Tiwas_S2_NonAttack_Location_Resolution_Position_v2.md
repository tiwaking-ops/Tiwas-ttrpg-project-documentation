# Tiwas S-2 Non-Attack Roll Location Resolution — Position Paper v2

**Context:** This paper addresses the open scope gap identified in v5 synthesis §7: how to supply a Tier-1 Location Index for non-attack physical resolutions (falls, environmental hazards, etc.) where there is no "attacker" whose natural d100 roll Zero-Step consumes. This version incorporates corrections from ClaudeAI analysis regarding Contact Branch sourcing and warrant attribution.

## 1. Problem Statement

Zero-Step (Canonical §14.1) derives the Location Index by exchanging the tens and units digits of **"the attacker's natural d100 roll."** This definition presumes an adversarial impact with a clear attacker/defender distinction.

However, non-attack physical resolutions — such as environmental hazards (rope bridges, falling rock, traps), extended test intervals involving physical risk, or other scene-based physical resolutions — lack this attacker/defender dyad. Applying Zero-Step literally to these cases creates a categorical error: there is no "attacker" roll to transform.

The v5 synthesis confirmed this gap remains open and should be treated as a distinct, narrower rules-architecture question.

## 2. Key Corrections from Analysis

### 2.1 Contact Branch Sourcing (Not Just Any Test Roll)

Zero-Step does not consume "the natural roll of whichever test is resolving the hazard" indiscriminately. Instead:

> **Where a genuinely attacker-less hazard warrants a Location Index, Zero-Step consumes the natural roll from the Contact Branch of the affected character's Existing Test — the outcome-branch in which the hazard's impact is actually realized against the character, as opposed to avoided or absorbed.**

This specification resolves the polarity issue:
- **Avoidance-framed tests** (success = avoid, failure = struck): Contact Branch = Failure
- **Endurance/resistance-framed tests**: Contact Branch = Ambiguous (depends on S-3/S-4 defining "severity")
- **Uniform-consequence tests**: No Contact Branch → No Location Index (matches v5 §6 State-4)

### 2.2 Warrant Attribution Shifts to GM (Not Affected Character)

The explicit-only objective boundary rule applies, but the declaring party changes:

> **For a non-attack physical hazard, a declared objective is definite — and Warrant-eligible — if and only if the GM, in authoring or framing the hazard, has explicitly named a distinct consequence, other than ordinary damage, whose resolution depends on where the hazard's Contact Branch roll lands.**

This aligns with the asymmetries in existing rules:
- **Named-Outcome Test**: Attacking player declares; defending player never does
- **S-1 winner-only**: Winning participant's roll sources; losing participant's never does

The affected character occupies the receiving/target role (like a defending PC in melee), not the declaring/sourcing role.

## 3. Combined Working Solution

### 3.1 Source Determination Logic
1. **Identifiable contemporaneous triggering agent** (NPC cuts rope in real time):  
   → Ordinary §14.1 sourcing from agent's attack roll (no extension needed)
2. **Otherwise (truly attacker-less hazard)**:  
   → Apply Four-State Model unmodified  
   → Warrant via GM-declared explicit objective (B1)  
   → Anchor table unchanged  
   → Warrant established → Source via Contact-Branch sourcing  
   → No Existing Test or no identifiable Contact Branch → No Location Index

### 3.2 Examples

#### 3.2.1 Environmental Hazard (Roof Collapse - Avoidance Framed)
- GM frames hazard: "If you fail Reflexes, you're struck by falling debris and may suffer broken bones"
- Player rolls Reflexes test: natural roll = 33 (failure)
- Contact Branch = Failure (where impact occurs)  
- If location warranted: Zero-Step(33) = 33 → Location Index = 33  
- Cost = 33 paid from Physical Energy  
- Location Index 33 passed to wound/armour systems

#### 3.2.2 Environmental Hazard (Generic Gas - Uniform Consequence)
- GM frames hazard: "The chamber fills with poisonous gas"  
- Player rolls Endurance test: natural roll = 67  
- No Contact Branch (same effect regardless of roll)  
- → No Location Index generated (matches v5 §6 uniform-consequence State-4)  
- Cost = 67 paid normally  
- Hazard resolved via standard Effect/Condition application

#### 3.2.3 Botched Action Causes Fall
- Player attempts Climbing test, rolls natural roll = 91 (failure)  
- GM frames: "Your botched climb causes you to fall"  
- Contact Branch = Failure (the fall itself)  
- If location warranted: Zero-Step(91) = 19 → Location Index = 19  
- Cost = 91 paid from Physical Energy  
- Location Index 19 passed to wound/armour systems  

## 4. Why This Is Correct

### 4.1 Preserves Core Invariants
- **Cost = Roll**: Each hazard resolution is itself a standard Skill test
- **No competing economies**: Uses existing Core Test Transaction
- **Universal Play compliance**: Builds on, doesn't replace, Core Transaction

### 4.2 Aligns with Existing Asymmetries
- Matches S-1 winner-only: Acting party (GM/hazard) sources; receiving party (character) never does
- Matches Named-Outcome Test: Declaring party (GM) declares consequences; receiving party doesn't
- Maintains explicit-only: No inference from narrative alone; must be stated in advance

### 4.3 Architectural Value (Not Immediate Unlock)
As noted in analysis, resolving source doesn't unlock today's rope-bridge case (it's State 3 due to S-4 gaps), but:
- Prevents source from becoming a second blocker once S-3/S-4/S-7 clear Unanchored categories
- Provides clean architectural extension that mirrors attack-sourced logic
- Satisfies Roadmap §24.11 (no parallel Core resolution engine)

### 4.4 Minimal Mechanism Change
- Zero-Step unchanged: still exchanges tens/units digits of input roll
- Only clarification: defines what constitutes the valid input roll for attacker-less cases
- No new rolls, currencies, or resolution engines
- Read-only post-process property preserved (Canonical §14.2)

## 5. Governance Implications

### 5.1 Documentation Updates Needed
**Proposals/WIP Section 2 (S-2)**:
- Add Contact Branch concept for hazard resolution sourcing
- Clarify GM as declaring party for hazard warrant (vs. player for attacks)
- Show examples: avoidance-framed, endurance-framed, uniform-consequence hazards

**Proposals/WIP Section 14 (Environmental Hazards)**:
- Explicitly note Contact Branch sourcing for Zero-Step when location warranted
- Reference GM-as-declaring-party model for hazard objectives

**Implementation Roadmap**:
- Add Contact Branch test cases in Phase 20 hazard validation
- Confirm hazard resolution tests follow standard Core Test Transaction with branch awareness

### 5.2 Acceptance Criteria
- Zero-Step generates Location Index from natural roll of Contact Branch in hazard resolution test
- GM, not affected character, declares explicit objectives for hazard warrant
- Cost = Roll invariant preserved for all tests
- Mechanism distinguishes avoidance-framed vs. endurance-framed vs. uniform-consequence tests
- No additional rolls required solely for location generation

## 6. Open Questions Requiring Designer Input

### 6.1 Primary Fork: B1 vs. B2 Declaring Party
- **B1 (Recommended)**: GM as hazard author declares/consequences (aligns with existing asymmetries)
- **B2 (Rejected)**: Affected character declares own protective objective (inverts confirmed asymmetries)
- **Status**: Open designer fork requiring explicit ruling

### 6.2 Dependent Questions (Blocked on Subsystems)
- **Endurance/resistance hazards**: Contact Branch ambiguous until S-3/S-4 define "severity" mechanically
- **Multi-stage hazards**: Noticed but likely separate question (NPC action → delayed collapse)
- **Non-body targets**: Location on structures, etc. (noticed but out of scope for Person-focused S-2)

## 7. Conclusion

For non-attack physical resolutions requiring a Tier-1 Location Index:
1. **Source**: Zero-Step consumes from the Contact Branch of the affected character's Existing Test  
2. **Warrant**: GM, as hazard author, must explicitly declare distinct consequence depending on Contact Branch outcome  
3. **Mechanism**: Unchanged Zero-Step applied to correctly sourced natural roll  

This approach:
- Solves the architectural source question without modifying existing mechanics  
- Preserves all Core Test Transaction invariants  
- Aligns with proven asymmetries in S-1 and Objective Test rules  
- Requires only documentation clarification, not rule changes  
- Provides clean extension that won't become a second blocker once S-3/S-4/S-7 advance  

The rope-bridge case remains State 3 today due to S-4 wound-severity-location gaps (per v5 §7), but resolving source prevents additional blocking once those subsystems clear the general Unanchored category issue.