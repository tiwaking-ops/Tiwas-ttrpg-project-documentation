---
document:
  title: "Tiwas — DEC-079 Conditions: Numeric Tier Assignment and Action-Denial Interaction Resolution Proposal"
  document_type: "Formal Design Proposal"
  proposal_id: "DEC-079-CLOSURE-PROPOSAL-001"
  version: "1.0"
  status: "Non-Canonical — Pending Human Designer Ruling"
  date: "2026-09-08"
  author:
    name: "GPT-5.6 Luna"
    version: "GPT-5.6 Luna"
  intended_consumer: "OpenCode"
  authority: "Proposal only; does not modify Canonical Rules or the Decision Register"
  source_basis:
    - "decision-register.md"
    - "Tiwas-Alpha-Playtest-Corpus-2026-09-08.md"
    - "tiwas-canonical-rules-and-changelog-v1.3.md"
    - "tiwas-proposals-wip-and-design-direction-v1.4.3.md"
---

# 1. Executive Summary

This proposal resolves the two remaining DEC-079 questions identified in the current Tiwas design record:

1. **What numeric Tier does each Condition instance receive?**
2. **How do Stunned and other action-denial Conditions interact when simultaneously active?**

The proposal recommends:

| Decision surface | Proposed resolution |
|---|---|
| Condition Tier origin | **Use the causing Effect's Skill-Tier, subject to the existing universal GM Fiat override** |
| Condition Magnitude | `Z = −Y` |
| Condition production | Preserve the existing Skill-Tier ≥ 2 production gate |
| Movement-denial `Y` | Preserve DEC-122's separate `target-stat-value` query-time mechanism |
| Multiple same Condition instances | Preserve existing Condition-specific stacking rules |
| Stunned + Stunned | Highest-Tier Stunned governs where the Condition's own rule requires a single instance; no Tier addition |
| Stunned + Incapacitated | **Both records remain active; their effects combine by scope rather than competing by Tier** |
| Action denial | Resolve by the union of applicable action-denial restrictions |
| Incapacitated superiority | Preserve as a semantic distinction: Incapacitated denies a broader class of active resistance than Stunned |
| Tier arithmetic between different Conditions | **No addition and no generic "highest Tier wins" rule** |
| Counters | Do not use DEC-117 counters to resolve ordinary action-denial overlap |
| Core Test Transaction | Fully preserved |
| DEC-123 | Fully preserved |
| Canonical status | **No promotion implied by this proposal** |

The central architectural recommendation is:

> **Condition Tier measures the severity of the individual Condition record. It does not determine precedence between different Condition identities. Different Conditions interact through their defined mechanical scopes.**

This avoids introducing a second hierarchy engine into Tiwas.

---

# 2. Authority and Evidence Status

## 2.1 Current authority boundary

DEC-079 is a **non-canonical designer ruling**. Its foundation is already established, but the current register explicitly records carried-open questions concerning:

- numeric Tier values per Condition instance;
- precise Movement Speed reduction beyond the already-established `−Y`;
- interaction resolution between Stunned and other action-denial Conditions.

The current proposal therefore does **not** claim to alter Canonical Rules.

Any adoption remains subject to the Tiwas governance process, including the human designer ruling and the applicable promotion process.

## 2.2 Existing architecture that must be preserved

The following are already established and are treated as constraints:

- unified Effect/Condition/StateRecord schema;
- `Type / Tier Y / Magnitude Z / optional Location X`;
- `Z = −Y`;
- Effect Tier based on the Skill-Tier of the causing Skill;
- Skill-Tier ≥ 2 production gate;
- GM Fiat as bounded universal override;
- DEC-122 movement-denial treatment;
- DEC-123 "never total" action-declaration ruling;
- DEC-117 declarative counter architecture;
- Core Test Transaction.

DEC-115 explicitly states that Condition records use the unified schema and preserve DEC-079's Tier/Magnitude semantics.

DEC-127 formally names this architecture the **Effect Tier Magnitude System** and states that Effect Tier is the Skill-Roll Tier, while Magnitude is fixed at `Z = −Y`.

---

# 3. Problem Definition

## 3.1 Numeric Tier problem

DEC-079 established the structure:

```text
Tier-Y Condition Value Z
```

with:

```text
Z = −Y
```

but its original C3 wording was based on the earlier Quality-ceiling architecture.

DEC-107 subsequently superseded that portion by establishing:

```text
Effect Tier = Skill-Tier of the skill used
Effect Magnitude = Effect Tier
```

and explicitly applies this architecture to Conditions through DEC-079 C2/C3.

Consequently, the question is no longer properly framed as:

> "What arbitrary numeric Tier should each Condition receive?"

The remaining design question is:

> "Should Condition Tier be the Tier of the Effect that creates the Condition, subject to the existing tier rules and GM Fiat?"

The answer proposed here is **yes**.

## 3.2 Action-denial problem

The original DEC-079 vocabulary described:

- Stunned as action denial;
- Incapacitated as a stronger form of action denial;
- both as having highest-Tier behaviour.

The subsequent G2 rulings substantially changed the mechanical environment.

DEC-122 establishes the self-referential movement-denial mechanism for Stunned, Incapacitated, Restrained, Grappled and Prone.

DEC-123 then explicitly overrides the categorical "cannot declare actions" wording:

> Stunned, Incapacitated and Restrained characters may declare a test and roll it.

The roll is guaranteed to fail through Effective Skill 0, while the complete Core Test Transaction remains active. GM Fiat determines whether the attempt is permitted at all.

Therefore the remaining problem is **not** simply "which Condition prevents the action?"

It is:

> **How should multiple action-denial Condition effects be evaluated when their scopes overlap?**

---

# 4. Design Constraints

The proposed resolution must satisfy all of the following.

| Constraint | Requirement |
|---|---|
| C-01 | No second Condition-specific Tier engine |
| C-02 | Preserve `Z = −Y` |
| C-03 | Preserve DEC-107 Skill-Tier basis |
| C-04 | Preserve DEC-122 movement-denial architecture |
| C-05 | Preserve DEC-123 never-total action declaration |
| C-06 | Preserve full Core Test Transaction |
| C-07 | No new resource pool |
| C-08 | No modification to natural d100 |
| C-09 | No generic Tier addition |
| C-10 | No unnecessary new StateRecord fields |
| C-11 | Preserve distinct Condition identities |
| C-12 | Preserve Incapacitated > Stunned semantic distinction |
| C-13 | Preserve existing Condition-specific stacking rules |
| C-14 | Avoid converting DEC-117 counters into a general precedence engine |

These constraints are consistent with the existing unified StateRecord architecture. DEC-117 defines counters as explicit declarative filters, not as a general resolution engine.

---

# 5. Proposal A — Numeric Condition Tier

## 5.1 Proposed rule

For a Condition created by an Effect:

\[
Y_{Condition}=Y_{Effect}=SkillTier_{causing}
\]

subject to:

1. the existing Skill-Tier ≥ 2 Condition production gate;
2. the existing lesser-Tier rules;
3. the existing GM Fiat override.

Magnitude remains:

\[
Z=-Y
\]

Therefore:

| Causing Skill-Tier | Condition Tier | Condition Value |
|---:|---:|---:|
| 2 | 2 | −2 |
| 3 | 3 | −3 |
| 4 | 4 | −4 |
| 5 | 5 | −5 |
| N | N | −N |

This is not a new mechanical architecture.

It is the application of the already-established Effect Tier Magnitude System to Condition instances.

## 5.2 Rationale

This is preferable to assigning fixed tiers to Condition names.

For example, the system should **not** establish:

| Condition | Fixed Tier |
|---|---:|
| Stunned | 3 |
| Incapacitated | 4 |
| Restrained | 2 |

That would make the Condition's identity determine its numerical severity.

The existing architecture instead makes the **producing Effect** determine severity.

This is already the operative model for Effects and Wounds under DEC-107.

## 5.3 Condition identity remains independent

This distinction is essential:

```text
Condition Identity ≠ Condition Tier
```

For example:

```text
Tier-2 Stunned
Tier-5 Stunned
Tier-2 Incapacitated
Tier-5 Incapacitated
```

are different instances of different Condition identities and can have different numerical severity.

The fact that Incapacitated is semantically stronger than Stunned does **not** require Incapacitated to have a permanently higher numeric Tier.

---

# 6. Critical Interaction With DEC-122

DEC-122 creates an important distinction that this proposal must preserve.

For movement-denial Conditions:

\[
Y = TargetStatValue
\]

at query time, and:

\[
Z=-Y
\]

producing:

\[
EffectiveStat=Stat+Z=0
\]

The register explicitly identifies this as the `target-stat-value` Y-source pattern and distinguishes it from the `causing-Skill-Tier` pattern established by DEC-107.

Therefore this proposal **must not collapse those two Y-source patterns into one formula**.

## 6.1 Required distinction

| Context | Y source |
|---|---|
| Condition record Tier | Causing Effect / Skill-Tier |
| Condition Magnitude | `Z = −Y` |
| Movement-denial overlay under DEC-122 | Target stat's current value at query time |

This is a critical architectural distinction.

### Proposed documentation clarification

The term `Y` is overloaded by the existing architecture.

OpenCode should document the source of `Y` explicitly whenever it appears in a rule.

For example:

```text
Condition Tier Y
Y-source: causing-Skill-Tier
```

versus:

```text
Movement overlay Y
Y-source: target-stat-value
query-time-live: true
```

This prevents DEC-122 from being misread as changing the Condition's actual Tier.

---

# 7. Proposal B — Same-Condition Interaction

The existing alpha vocabulary already establishes Condition-specific interaction patterns.

Examples include:

| Condition | Existing interaction |
|---|---|
| Encumbered | Same-tier add; higher replaces |
| Grappled | Highest tier only |
| Restrained | Same-tier add; higher replaces |
| Prone | Highest tier only |
| Slowed + Encumbered | Worse penalty applies |
| Stunned | Highest tier |
| Incapacitated | Highest tier |

The proposal does **not** replace these individual rules with a universal stacking rule.

Instead:

> **Each Condition retains its explicitly defined stacking/selection behaviour.**

This is important because different Conditions represent different mechanical concepts.

A universal:

```text
highest Tier wins
```

rule would contradict existing Condition-specific decisions.

Likewise:

```text
all Tiers add
```

would contradict multiple existing decisions.

---

# 8. Proposal C — Different Action-Denial Conditions

## 8.1 Rejected approach: numeric precedence

The first candidate is:

```text
Stunned Tier 3
+
Incapacitated Tier 2
=
Incapacitated Tier 3
```

This proposal rejects that model.

### Reasons

1. Tier represents the severity of a record.
2. Condition identity represents what the Condition does.
3. Adding Tiers produces a new severity that neither Effect created.
4. It would require a new numerical stacking engine.
5. It would blur the distinction between Condition types.
6. It is unnecessary under DEC-123.

---

# 9. Proposed Resolution: Scope Union

The recommended solution is **scope union**.

For each applicable action/test:

1. Identify every active Condition relevant to the attempted action.
2. Read each Condition's defined restriction.
3. Apply all restrictions that independently apply.
4. Do not add Condition Tiers.
5. Do not replace one Condition with another merely because its Tier is higher.
6. Where two Conditions impose the **same restriction**, the duplicate restriction has no additional mechanical effect.
7. Where one Condition imposes a broader restriction, that broader restriction remains operative.
8. The resulting test then proceeds under DEC-123 and the normal Core Test Transaction where GM Fiat permits the attempt.

Formally:

\[
Restrictions_{effective}
=
\bigcup_{i=1}^{n} Restrictions(Condition_i)
\]

This is a logical union, **not a numerical sum**.

---

# 10. Stunned + Incapacitated

This is the critical test case.

## 10.1 Existing semantics

Stunned:

- action denial;
- movement denial;
- auto-fail active Body/Speed resistance.

Incapacitated:

- action denial;
- movement denial;
- auto-fail all active resistance;
- strictly stronger than Stunned.

The alpha vocabulary explicitly records Incapacitated as stronger than Stunned.

## 10.2 Proposed interaction

If both are active:

```text
Stunned
+
Incapacitated
```

the records **remain separate**.

No replacement occurs.

No Tier addition occurs.

The operative restriction is the union:

```text
Stunned restrictions
        +
Incapacitated restrictions
        ↓
Applicable union
```

Because Incapacitated already covers the broader class of active resistance, its restriction subsumes the Stunned restriction for those tests.

Therefore the result is functionally:

> **Incapacitated governs the overlapping action-denial consequences, while Stunned remains an active Condition record.**

This is **not** "Incapacitated counters Stunned."

It is simply that the applicable restriction from Incapacitated already encompasses the narrower Stunned restriction.

---

# 11. Why This Is Superior to a Precedence Table

A fixed precedence table such as:

| Rank | Condition |
|---:|---|
| 3 | Incapacitated |
| 2 | Stunned |
| 1 | Restrained |

appears simple but creates several architectural problems.

### 11.1 It conflates different mechanical dimensions

Restrained is primarily a movement/body-skill restriction.

Stunned is action/resistance denial.

Incapacitated is broader active-resistance denial.

A single linear hierarchy cannot accurately represent those different scopes.

### 11.2 It creates future maintenance burden

Every new action-denial Condition would require inserting it into a global hierarchy.

### 11.3 It creates false conflicts

Two Conditions can coexist without actually conflicting.

For example:

```text
Stunned + Restrained
```

contains:

- Stunned's action/resistance restriction;
- Restrained's Body Skill / movement / attack restrictions.

There is no reason one should erase the other.

### 11.4 It violates the existing design direction

Tiwas already expresses Conditions as mechanical overlays on Skills, Movement, Tests and StateRecords.

The system does not need a global Condition-ranking engine.

---

# 12. Proposed Action-Denial Resolution Matrix

The following matrix is recommended as the formal interpretation.

| Active Conditions | Action/Test consequence |
|---|---|
| None | Normal resolution |
| Stunned | Apply Stunned restrictions |
| Incapacitated | Apply Incapacitated restrictions |
| Stunned + Stunned | Apply the Condition's existing highest-Tier rule |
| Incapacitated + Incapacitated | Apply the Condition's existing highest-Tier rule |
| Stunned + Incapacitated | Apply union; Incapacitated subsumes overlapping Stunned restriction |
| Stunned + Restrained | Apply both Conditions' distinct restrictions |
| Incapacitated + Restrained | Apply both Conditions' distinct restrictions |
| Stunned + Grappled | Apply both Conditions' distinct restrictions |
| Incapacitated + Grappled | Apply both Conditions' distinct restrictions |
| Stunned + Prone | Apply both Conditions' distinct restrictions |
| Incapacitated + Prone | Apply both Conditions' distinct restrictions |

The table does **not** create new numerical stacking.

---

# 13. DEC-123 Integration

This proposal must explicitly incorporate DEC-123.

## 13.1 Action declaration

A Stunned/Incapacitated/Restrained character is **not categorically prevented from declaring a test**.

If GM Fiat permits the attempt:

```text
Declare test
    ↓
Apply applicable Condition restrictions
    ↓
Effective Skill = 0 where DEC-122's self-referential mechanism applies
    ↓
Roll
    ↓
Normal Core Test Transaction
```

The character therefore can deliberately attempt a guaranteed-failure roll.

The roll still:

- costs its natural d100 result;
- may cause Overflow;
- generates Failure XP;
- can qualify for a failed Double;
- can create an Advanced Skill;
- proceeds through normal Recovery.

DEC-123 explicitly establishes this behaviour.

---

# 14. Counters Are Not the Solution

DEC-117 introduces explicit StateRecord counters.

The counter rule is:

> If a target has a StateRecord whose ID is listed in another record's `counters`, the countered record's effects do not apply.

Counters are:

- explicit;
- declarative;
- filters;
- not rolls;
- not resource mechanics;
- not a second resolution engine.

The proposed Stunned/Incapacitated interaction should **not** be implemented as a counter relationship.

### Reason

If:

```text
Incapacitated counters Stunned
```

then applying Incapacitated would suppress the entire Stunned StateRecord.

That is stronger than necessary.

The proposed rule instead says:

```text
Both records exist.
Both records are evaluated.
Overlapping restrictions produce no additional effect.
Distinct restrictions remain active.
```

This is mechanically more precise.

---

# 15. Example Resolution Cases

## 15.1 Tier 3 Stunned + Tier 2 Incapacitated

Records:

```text
Tier-3 Stunned Value -3
Tier-2 Incapacitated Value -2
```

Do **not** calculate:

```text
Tier 5
```

Do **not** let Tier 3 Stunned replace Incapacitated.

Do **not** let Incapacitated delete Stunned.

Instead:

```text
Stunned restriction
+
Incapacitated restriction
=
union of restrictions
```

The broader Incapacitated active-resistance restriction governs the overlapping component.

---

## 15.2 Tier 2 Stunned + Tier 5 Incapacitated

Same result.

The Tier difference does not create a new Condition Tier.

```text
Tier-2 Stunned
Tier-5 Incapacitated
```

remains two separate records.

Incapacitated's broader restriction applies where relevant.

---

## 15.3 Tier 5 Stunned + Tier 1 Incapacitated

The result is still not:

```text
Tier-5 Stunned overrides Tier-1 Incapacitated
```

because numeric Tier is not the semantic hierarchy between different Condition identities.

The two Conditions retain their distinct scopes.

The Incapacitated restriction therefore remains operative despite its lower Tier.

This is the principal reason to reject "highest Tier wins" as a cross-Condition action-denial rule.

---

# 16. Movement Interaction

DEC-122 already resolves the Movement Speed component.

For Stunned, Incapacitated, Restrained, Grappled and Prone:

\[
Y = current\ target\ Movement\ Speed
\]

\[
Z=-Y
\]

\[
Effective\ Movement\ Speed
=
Movement\ Speed-Y
=
0
\]

The underlying DEC-004 Movement Speed formula remains untouched.

Therefore this proposal does not reopen movement denial.

The only required clarification is that:

> **The movement overlay's target-stat-value `Y` is not the Condition's originating Skill-Tier `Y`.**

---

# 17. Relationship to Existing Condition Stacking

The proposal deliberately distinguishes three cases.

| Interaction class | Resolution |
|---|---|
| Same Condition, same mechanical dimension | Existing Condition-specific stacking rule |
| Same Condition, different Tier | Existing Condition-specific highest/additive rule |
| Different Conditions, distinct effects | Effects combine |
| Different Conditions, overlapping effects | Overlapping effect is not duplicated |
| Different Conditions, one broader than another | Broader restriction subsumes narrower overlapping restriction |
| Different Conditions, numerical Tier difference | **No Tier precedence** |

This allows existing decisions such as Encumbered/Slowed to remain intact.

The current register records, for example, that Encumbered uses same-tier addition/higher replacement while Slowed + Encumbered uses the worse penalty.

The proposal does not alter those rules.

---

# 18. Formal Proposed Rule Text

The following is the recommended rule text for future incorporation into the DEC-079 record.

## 18.1 Numeric Tier

> **Condition Tier.** A Condition created by an Effect receives a Tier equal to the Skill-Tier of the Skill used to create that Effect, subject to the existing Condition production gate, lesser-Tier rules and GM Fiat. Condition Magnitude is `Z = −Y`. Condition Tier measures the severity of that individual Condition record and does not establish precedence between different Condition identities.

## 18.2 Movement Y-source

> **Movement-denial Y-source.** Where a Condition applies the DEC-122 movement-denial overlay, its Movement Speed `Y` is the target's current Movement Speed at query time. This `Y` is a `target-stat-value` Y-source and is distinct from the Condition record's originating Skill-Tier Y. The Movement Speed formula itself is not modified.

## 18.3 Same-Condition stacking

> **Same-Condition interaction.** Each Condition retains its explicitly defined stacking and selection behaviour. No universal stacking rule replaces Condition-specific rules.

## 18.4 Different Conditions

> **Different-Condition interaction.** Distinct Conditions remain separate StateRecords. Their applicable mechanical effects are evaluated independently. Effects that address different mechanical dimensions combine. Where multiple Conditions impose the same restriction on the same test or state, the restriction is applied once; Condition Tiers are not added and one Condition does not automatically replace or counter another solely because its Tier is higher.

## 18.5 Action-denial Conditions

> **Action-denial interaction.** Stunned, Incapacitated and other action-denial Conditions are resolved by the union of their applicable restrictions rather than by numerical Tier precedence. A broader restriction subsumes a narrower overlapping restriction without removing the narrower Condition record. Incapacitated therefore remains mechanically stronger than Stunned because its defined active-resistance restriction is broader, not because Incapacitated possesses a universally higher numeric Tier.

## 18.6 DEC-123 compatibility

> **Action declaration.** This rule does not override DEC-123. A character affected by Stunned, Incapacitated or Restrained may declare and roll a test when GM Fiat permits the attempt. Applicable Condition mechanics may make the Effective Skill 0 and therefore guarantee failure, but the complete Core Test Transaction remains operative.

---

# 19. Consistency Analysis

## 19.1 DEC-001–DEC-017

**No conflict identified.**

The proposal does not modify:

- d100 resolution;
- Skill values;
- natural rolls;
- resource cost;
- Overflow;
- Failure XP;
- Advanced Skills;
- Recovery;
- S-1;
- S-2.

## 19.2 DEC-007.A

**Preserved.**

No Condition may modify Overflow.

DEC-117 already reinforces that StateRecords do not directly modify HP, Overflow or pools.

## 19.3 DEC-107

**Preserved and relied upon.**

DEC-107 establishes Skill-Tier as the Effect Tier basis.

## 19.4 DEC-115

**Preserved.**

No new record field is required.

## 19.5 DEC-117

**Preserved.**

The proposal does not convert counters into a general precedence engine.

## 19.6 DEC-122

**Preserved.**

The proposal explicitly separates Condition Tier Y from movement-overlay Y.

## 19.7 DEC-123

**Preserved.**

The proposal does not reintroduce categorical action prohibition.

## 19.8 DEC-126

**Preserved.**

No mechanical meaning is assigned to "helpless".

## 19.9 DEC-127

**Preserved.**

The proposal directly applies the Effect Tier Magnitude System to Conditions.

---

# 20. Alternatives Considered

| Option | Assessment | Recommendation |
|---|---|---|
| Fixed Tier per Condition identity | Creates arbitrary second severity system | Reject |
| Condition Tier = causing Skill-Tier | Already supported by DEC-107 | **Accept** |
| Condition Tier = Effect Quality | Superseded by DEC-107 | Reject |
| Condition Tier = target-stat value for all Conditions | Confuses DEC-122 Y-source with record Tier | Reject |
| Add Tiers between Conditions | Creates new numerical stacking engine | Reject |
| Highest Tier always wins | Destroys distinct Condition scopes | Reject |
| Global Condition precedence hierarchy | Unnecessary and difficult to scale | Reject |
| Counter Stunned with Incapacitated | Removes information and over-suppresses state | Reject |
| Scope union | Preserves distinct Conditions and requires no new engine | **Accept** |

---

# 21. Recommended Decision

## DEC-079-A — Condition Tier Assignment

**RECOMMEND ADOPTION**

> Condition Tier equals the Skill-Tier of the causing Effect's Skill, subject to existing Condition production, lesser-Tier and GM Fiat rules. Magnitude remains `Z = −Y`.

This should be recorded as a **clarification/formal closure of the existing carried-open numeric-Tier question**, rather than creation of a new Tier subsystem.

## DEC-079-B — Action-Denial Interaction

**RECOMMEND ADOPTION**

> Different action-denial Conditions do not compete by numeric Tier. Their mechanical restrictions are evaluated by scope. Distinct restrictions combine; duplicate overlapping restrictions apply once; broader restrictions subsume narrower overlapping restrictions. Condition records remain separate. No Tier addition occurs.

For Stunned + Incapacitated specifically:

> **Incapacitated remains stronger because its defined restriction is broader, not because its numeric Tier must exceed Stunned's Tier.**

---

# 22. Required Register Treatment

If the designer adopts this proposal, OpenCode should **not** silently rewrite DEC-079.

The governance action should be recorded explicitly.

Recommended register treatment:

| Item | Action |
|---|---|
| DEC-079 C3 | Amend/clarify in light of DEC-107 |
| DEC-079 numeric Tier open item | Close |
| DEC-079 C6 | Clarify as semantic Condition distinction + scope-based interaction |
| Stunned/Incapacitated interaction | Close as DEC-079 amendment or new amendment DEC |
| DEC-122 | Preserve unchanged |
| DEC-123 | Preserve unchanged |
| DEC-117 | Preserve unchanged |
| DEC-127 | Preserve unchanged |
| Canonical Rules | Do not alter until formal promotion is authorised |
| Proposal status | Remains non-canonical until governance promotion |

---

# 23. Implementation Consequences

If adopted, the implementation model is intentionally small.

A Condition record needs no additional precedence field.

Conceptually:

```text
Condition
├── Type
├── Identity
├── Tier Y
├── Magnitude Z
├── optional Location X
├── source
├── duration
├── removal_tags
└── counters
```

Action resolution evaluates:

```text
Applicable Conditions
        ↓
Condition-specific effects
        ↓
Combine applicable restrictions
        ↓
Remove duplicate overlapping consequences
        ↓
Effective test/stat state
        ↓
Core Test Transaction
```

No:

```text
ConditionPriority
ConditionRank
ConditionStackEngine
ConditionPoints
ActionPointPool
```

is required.

This is consistent with the project's established prohibition on introducing unnecessary new mechanical engines or resource pools.

---

# 24. Final Assessment

The strongest architectural conclusion is that **the two DEC-079 open questions should not be solved by the same mechanism**.

### Numeric Tier

Already substantially determined by the later architecture:

\[
ConditionTier = CausingSkillTier
\]

with:

\[
ConditionMagnitude=-ConditionTier
\]

This follows DEC-107 and the Effect Tier Magnitude System rather than introducing new Condition-specific numbers.

### Stunned interaction

Should **not** use Tier precedence.

The correct abstraction is:

\[
EffectiveRestrictions
=
\bigcup ApplicableConditionRestrictions
\]

with semantic subsumption where one restriction already encompasses another.

This preserves:

- Stunned;
- Incapacitated;
- their distinct identities;
- Incapacitated's stronger meaning;
- DEC-122;
- DEC-123;
- the unified StateRecord architecture;
- the absence of a second Condition-resolution engine.

## 24.1 Recommended designer ruling

**DEC-079 should therefore be closed on these two surfaces as follows:**

> **Condition Tier is derived from the causing Skill-Tier. Different Conditions do not compete by numeric Tier. Their defined mechanical restrictions combine by scope; overlapping restrictions are not duplicated, and broader restrictions subsume narrower overlapping restrictions. Stunned and Incapacitated therefore coexist as separate Conditions, with Incapacitated remaining stronger through its broader defined restriction rather than through numeric Tier precedence.**

**Status: PROPOSED — NOT CANONICAL.**

No implementation or canonical-document modification should occur until Tiwa explicitly adopts or rejects this proposal through the project's governance process.