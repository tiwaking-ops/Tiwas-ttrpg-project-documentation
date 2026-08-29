# Tiwas S-2 Non-Attack Roll Location Resolution — Position Paper v1

**Context:** This paper addresses the open scope gap identified in v5 synthesis §7: how to supply a Tier-1 Location Index for non-attack physical resolutions (falls, environmental hazards, etc.) where there is no "attacker" whose natural d100 roll Zero-Step consumes.

## 1. Problem Statement

Zero-Step (Canonical §14.1) derives the Location Index by exchanging the tens and units digits of **"the attacker's natural d100 roll."** This definition presumes an adversarial impact with a clear attacker/defender distinction.

However, non-attack physical resolutions — such as environmental hazards (rope bridges, falling rock, traps), extended test intervals involving physical risk, or other scene-based physical resolutions — lack this attacker/defender dyad. Applying Zero-Step literally to these cases creates a categorical error: there is no "attacker" roll to transform.

The v5 synthesis confirmed this gap remains open and should be treated as a distinct, narrower rules-architecture question, not folded into the warrant policy investigation.

## 2. Survey of Existing Framework

### 2.1 Canonical Rules & Changelog v1.3
- **Zero-Step definition**: Explicitly tied to "attacker's natural d100 roll" (§14.1, §14.2)
- **Core Test Transaction**: Every Skill test involves a roll that determines Cost, Outcome, etc. (§6)
- **Universal Play constraint**: Modules must build on Core Test Transaction, not replace it (Core Architectural Invariant #18)
- **Environmental hazards**: Referenced in Proposals/WIP but not detailed in Canonical Rules

### 2.2 Proposals/WIP v1.4.1
- **S-9/S-10 Extended Tests**: Explicitly list "environmental hazards" as an intended use case (§9)
- **S-8 Difficulty/Task Adjudication**: Governs when tests are meaningful (§8)
- **Environmental Hazards section**: Shows Preferred Structure using "Existing Test" → "Natural Cost" → "Outcome" → "Existing Effect/Condition/Harm" (§14)
- **Key insight**: The Preferred Structure implies environmental hazards resolve through an ordinary Core Test Transaction, not a special mechanic

### 2.3 Implementation Roadmap v1.4.1
- **U-16 Hazards**: Maps to Environmental resolution, depends on S-8 (§5)
- **Phase 20.3**: Testing includes hazards as part of Non-combat evaluation (§20)
- **S-9/S-10 status**: Open decisions regarding progress and failure models (§4)

## 3. Analysis of Requirements

Any solution must satisfy:

### 3.1 Non-Negotiable Constraints (from Core Architectural Invariants)
- **Cost = Roll** must remain invariant (Invariant #6)
- **No competing primary resource/progression economy** (Invariant #17)
- **Universal Play modules must build on Core Test Transaction** (Invariant #18)
- **d100 produces 1–100; 100 always fails; fractions floor; success is roll-under** (Invariants #1-5)

### 3.2 Functional Requirements
- Supply a Location Index when Zero-Step is called for by a rule
- Maintain compatibility with existing Tier-1 Location Index provider contract
- Support environmental hazards, extended test physical intervals, and other non-attack physical resolutions
- Presume location is already warranted (per prior investigation's Four-State Model) — this paper addresses only the Index *source*, not whether to generate it

## 4. Evaluation of Alternatives

### 4.1 Default to a Fixed Value (e.g., 50)
- **Pros**: Simple, deterministic
- **Cons**: 
  - Violates spirit of hit-location system (removes variability)
  - No basis in existing mechanics
  - Would require special-casing Zero-Step, breaking its uniformity

### 4.2 Use the Environmental/Scene Roll
- **Pros**: 
  - Aligns with Preferred Structure in Hazards section (Existing Test → Natural Cost)
  - Uses existing Core Test Transaction mechanism
  - Preserves Cost = Roll invariant
  - Each hazard resolution gets its own meaningful roll
- **Cons**: 
  - Requires clarifying what constitutes the "environmental roll" in various contexts
  - May need roll attribution rules (who/what makes the roll?)

### 4.3 Defer to Consuming Subsystem
- **Pros**: 
  - Avoids defining environmental roll semantics
  - Lets wounds/armour/etc. decide how to handle missing location data
- **Cons**: 
  - Pushes complexity downstream inconsistently
  - Violates Zero-Step's contract as a provider
  - Could create conflicting interpretations across subsystems

### 4.4 Reuse the Most Recent Relevant Roll
- **Pros**: 
  - Uses existing die rolls already made at table
  - No additional rolls required
- **Cons**: 
  - Highly context-dependent and ambiguous
  - Violates determinism and predictability
  - Risk of manipulation or confusion

## 5. Proposed Solution

**For non-attack physical resolutions requiring a Tier-1 Location Index, use the natural d100 roll from the Core Test Transaction that resolves the hazard or physical event itself.**

### 5.1 Mechanism
1. When a non-attack physical resolution (environmental hazard, extended test physical interval, etc.) is determined to require a test:
   - Conduct an ordinary Core Test Transaction using the most relevant Skill
   - This test produces a natural d100 roll per standard procedure
2. If the test warrants location generation (per Four-State Model from prior investigation):
   - Apply Zero-Step to **this test's natural d100 roll** to generate the Location Index
3. Proceed with remainder of Core Test Transaction (Cost, Overflow, etc.) as normal
4. Pass the Location Index to consuming subsystems (wounds, armour, effects) as normal

### 5.2 Alignment with Existing Framework
- **Preserves Core Test Transaction**: Each hazard resolution is itself a standard Skill test
- **Maintains Cost = Roll**: The natural roll still pays Cost exactly as defined
- **Uses existing Zero-Step**: No modification to the Location Index provider needed
- **Follows Preferred Structure**: Matches Environmental Hazards section's "Existing Test → Natural Cost" flow
- **Deterministic and uniform**: Same mechanism applies whether resolution is attack-based or environmental
- **No new rolls**: Uses the roll already made for hazard resolution

### 5.3 Examples

#### 5.3.1 Environmental Hazard (Roof Collapse)
- GM determines roof collapse requires an Athletics test to avoid damage
- Player rolls d100: natural roll = 42
- If Athletics test succeeds/fails per roll-under rule, proceed normally
- If location is warranted (per Four-State Model): Zero-Step(42) = 24 → Location Index = 24
- Cost = 42 paid from Physical Energy
- Location Index 24 passed to wound/armour systems for location-specific effect

#### 5.3.2 Extended Test (Mountain Climbing)
- Each climbing interval requires a Climbing test
- On interval 3, player rolls d100: natural roll = 68
- Zero-Step(68) = 86 → Location Index = 86
- Cost = 68 paid from Physical Energy
- Location Index 86 consumed by hazard/wound systems for that interval

#### 5.3.2 Contrast with Attack Resolution (Sword Swing)
- Attacker rolls d100: natural roll = 73
- Zero-Step(73) = 37 → Location Index = 37
- Cost = 73 paid from Physical Energy  
- Location Index 37 passed to wound/armour systems
- **Same mechanism**: Zero-Step applied to natural roll of the resolving test

## 6. Governance Implications

### 6.1 No Canonical Rule Changes Required
- Zero-Step remains unchanged: still derives Location Index by exchanging tens/units digits of input roll
- Core Test Transaction unchanged: still Roll → Outcome → Natural Roll Cost → etc.
- Only clarification needed: the "attacker's natural d100 roll" in Zero-Step definition refers to the natural roll of the test resolving the physical event, whether that event is an attack or environmental hazard

### 6.2 Documentation Updates
**Proposals/WIP Section 2 (S-2)**:
- Clarify that Zero-Step's input roll is the natural d100 from the Core Test Transaction resolving the physical event requiring location
- Add examples showing non-attack resolutions (hazards, extended tests) using same mechanism as attacks

**Proposals/WIP Section 14 (Environmental Hazards)**:
- Explicitly note that hazard resolution tests supply the natural roll for Zero-Step when location is warranted
- Reference this mechanism in the Preferred Structure explanation

**Implementation Roadmap**:
- Add test cases for non-attack physical resolutions in Phase 20 validation
- Confirm hazard resolution tests follow standard Core Test Transaction

### 6.3 Acceptance Criteria
- Zero-Step generates Location Index from natural roll of test resolving physical event (attack or non-attack)
- Cost = Roll invariant preserved for all tests
- No additional rolls required solely for location generation
- Mechanism works uniformly for attack and non-attack physical resolutions
- Compatible with existing consuming subsystems (wounds, armour, effects)

## 7. Why This Approach Is Correct

### 7.1 Parsimony
- Uses exactly one roll per physical resolution attempt (attack or environmental)
- No new mechanics, currencies, or special cases
- Applies Zero-Step uniformly as intended

### 7.2 Consistency with Design Direction
- Honors Universal Play axiom: modules build on Core Test Transaction
- Environmental Hazards Preferred Structure already shows this flow
- Extended Tests defined as "ordinary Tiwas tests" preserving Core Transaction

### 7.3 Preserves Human Experience
- Players make one meaningful roll per attempt, whether swinging sword or dodging falling rock
- No ambiguity about "whose roll" — it's the roll just made to resolve the attempt
- Maintains tension and consequence of each action through standard roll-under resolution

## 8. Open Questions for Further Investigation

This paper assumes location is already warranted per prior investigation's Four-State Model. If future work changes when location is warranted:
- The mechanism (Zero-Step applied to resolving test's natural roll) remains valid
- Only the warrant decision changes, not the Index source

Related but separate questions:
- How should extended test intervals determine when to make hazard tests? (S-9/S-10 territory)
- What Skill is appropriate for various environmental resolutions? (S-8/task adjudication)
- Should some hazards use fixed difficulty vs. opposed rolls? (S-8 difficulty system)

These do not affect the Location Index source mechanism proposed here.

---
**Conclusion**: For non-attack physical resolutions requiring a Tier-1 Location Index, the natural d100 roll from the Core Test Transaction that resolves the hazard or physical event itself should be supplied to Zero-Step. This approach preserves all Core invariants, uses existing mechanics uniformly, and requires no new systems — only clarification that Zero-Step's "attacker's natural d100 roll" refers to the roll resolving the physical event in question, whether attack-based or environmental.