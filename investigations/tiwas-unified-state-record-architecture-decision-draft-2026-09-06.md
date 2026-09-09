---
document:
  title: "Tiwas Decision Draft — Unified State Record Architecture for Tags, Effects, and Conditions"
  version: "1.0"
  status: "Advisory designer ruling draft (not canonical)"
provenance:
  author_llm: {name: "GPT-5.6 Luna", version: "GPT-5.6 Luna"}
  assessor_llm: []
  last_modified_by_llm: {name: "GPT-5.6 Luna", version: "GPT-5.6 Luna"}
  created_date: "2026-09-06"
  last_modified_date: "2026-09-06"
---

# 1. Executive Verdict

**Recommendation: adopt the architectural unification, but reject a literal semantic collapse.**

1. Tags, Effects, and Conditions should share **one mechanical state-record schema** rather than three record architectures.
2. They should remain distinct **Types** because their production, persistence, interpretation, and consumers are materially different.
3. `Tier Y`, `Magnitude Z`, and optional `Location X` are sufficient as the common mechanical payload.
4. The existing `Z = -Y` convention should be retained for **negative mechanical states**; it should not automatically be imposed on descriptive Tags.
5. Tags should remain **stateless with respect to resources**: no HP, MP, Energy, XP, Overflow, or pool modification.
6. A Tag may participate in a **relational predicate** such as "Tag A counters Tag B", but this is not the same thing as a Tag modifying a resource or performing an Effect.
7. Persistence should be treated as **Type-specific lifecycle behaviour**, not as a new record field: Tags default persistent; Effects default temporary; Conditions follow their defined removal semantics.
8. The principal complexity reduction is real: one record grammar, one Tier/Magnitude model, one location model, one storage model, and one generic state-processing vocabulary.
9. The principal cost is also real: the unified backbone requires a **typed lifecycle/interaction layer**. If that layer becomes elaborate, the proposed simplification merely relocates complexity.
10. Therefore the recommended target is **one record architecture + three semantic Types**, not "everything is a Tag."

This is a **designer ruling draft only**. It does not alter Canonical Rules v1.3 or promote/supersede DEC-058, DEC-060, DEC-079, DEC-080, DEC-088, or DEC-025.

---

# 2. What "One Mechanical Backbone" Actually Means

## 2.1 Unified Record

The proposed mechanical record is:

```text
[Type:] [Location X] Tier-Y [Name] Z
```

Where:

| Variable | Definition | Constraint |
|---|---|---|
| `Type` | Fiction/mechanical category: Tag, Effect, or Condition | Exactly one |
| `X` | Optional Location Index | Present only when the state is location-scoped |
| `Y` | Tier | Non-negative integer; Tier 0 means no tiered state where applicable |
| `Name` | Named semantic state | Must belong to the relevant Type vocabulary |
| `Z` | Magnitude / numerical value | Interpreted according to Type; negative-state default is `Z = -Y` |

Examples:

```text
Tag: creature:type_beast
Tag: env:darkness

Effect: Tier-2 Grappled -2
Effect: Location 73 Tier-2 Wound -2

Condition: Tier-1 Frightened -1
Condition: Location 52 Tier-2 Wounded -2
```

The precise display syntax can be changed during formal documentation, but the **underlying record must not diverge by Type**.

## 2.2 Type Is Semantically Necessary

The mistake would be assuming that a shared record means the three concepts have become interchangeable.

They have not.

| Type | Primary meaning | Typical producer | Typical lifetime |
|---|---|---|---|
| Tag | Classification, property, permission, identity, relational predicate | Authoring / state transition / equipment | Persistent by default |
| Effect | Declared consequence produced by successful resolution | Successful S-1 / other authorised mechanism | Temporary by default |
| Condition | Applied adverse/beneficial state affecting capability | Effect or authorised state binding | Defined lifecycle |

This preserves the useful fiction-level distinction while eliminating three different data structures.

The existing DEC-080 Tag model is already namespace-based and extensible, while DEC-079 gives Conditions a parallel structured form.

---

# 3. Impact Analysis

## 3.1 Idea 1 — "Tags are like Effects, but Tags are Permanent"

### Proposed change

Replace an absolute conceptual distinction with:

> **Tags default to persistent. They remain present until an authorised removal or replacement operation removes them. Effects default to temporary unless their production rule establishes persistence.**

This is the correct direction.

The important correction is that **permanence should not be encoded as a fourth universal mechanical dimension**.

Do not add:

```text
Persistence = Permanent
```

to every record.

That would create another axis which the proposed simplification does not need.

Instead, persistence belongs to the **Type/lifecycle rule**.

### What it fixes

It provides a clean explanation for why:

- `env:darkness` persists while the scene remains dark;
- an equipment Tag persists while the property remains true;
- an Effect can exist only for a defined period;
- a persistent Effect can become a continuing state;
- `state:sundered` can persist until repaired.

DEC-060 already establishes `Sundered` as a permanent state until repaired.

### Conflict

There is no genuine conflict with the Core.

The existing Tag architecture, however, has been deliberately described as classification/permission metadata and read-only/stateless. The proposed lifecycle model therefore changes **what a Tag can represent**, even if it does not violate resource invariants.

**Assessment: acceptable architectural change, but not merely terminology.**

---

## 3.2 Idea 2 — "Effects are caused by a Skill Roll"

### Proposed change

Retain the existing Effect production architecture:

```text
Declared Effect
    ↓
S-1
    ↓
Win
    ↓
Effect applies
```

The unified record does **not** mean every record can spontaneously become an Effect.

This preserves DEC-023–030:

- Effects are declared;
- winning S-1 produces the Effect;
- one Effect is produced per win;
- gated Effects still require their existing conditions;
- auto-application remains the default.

DEC-027 explicitly establishes auto-application, while DEC-024 retains one Effect per win. 

### Recommendation

The unified backbone should therefore separate:

```text
Record structure
```

from:

```text
Production rule
```

That is the central architectural distinction.

---

## 3.3 Idea 3 — "Tags have Tier Y, Magnitude Z, and optional Location X"

### Recommendation

**Adopt, but with one restriction.**

Tags may carry Tier and Magnitude **when the Tag has mechanical state**, but purely descriptive/classificatory Tags need not acquire artificial numerical meaning.

For example:

```text
Tag: creature:type_beast
Tag: damage:slashing
Tag: env:darkness
```

do not become meaningfully different because they have a meaningless `Z = 0`.

By contrast:

```text
Tag: Tier-2 Ignore-Darkness
Tag: Location X Tier-2 Armour
```

can legitimately use the unified numerical state structure.

This distinction matters because DEC-080 currently defines Tags such as `damage:slashing`, `offense:melee`, and `env:darkness` as ontology/vocabulary entries.

**Do not force numerical state onto Tags that are inherently boolean classifications.**

That would increase complexity rather than reduce it.

### Decision

The unified schema therefore has:

```text
Tier Y = optional semantic field
Magnitude Z = optional semantic field
Location X = optional semantic field
```

The record architecture is unified; field utilisation is Type-defined.

---

# 4. Idea 4 — "Tags can Counter Other Tags"

This is the most important architectural issue.

## 4.1 The Proposed Relationship

Example:

```text
Environment:
    env:darkness

Creature:
    ignores:darkness
```

The intended result is:

```text
env:darkness
        ↓
    countered by
        ↓
ignores:darkness
```

Darkness remains present.

The counter-Tag simply prevents a particular consumer from treating darkness as mechanically active for that consumer.

## 4.2 This Does NOT Require a Resource Effect

The counter must be defined as a **relational predicate**, not as an Effect.

Formally:

```text
Active(Tag A, Consumer C)
    =
Present(Tag A)
AND NOT Countered(Tag B, Tag A, C)
```

where:

- `Tag A` = the tag being evaluated;
- `Tag B` = a counter-tag;
- `C` = the consuming subsystem/mechanic.

No HP, MP, Energy, XP, Overflow, roll, or pool is changed.

Therefore the mechanism remains compatible with the core architectural prohibition against new resource economies.

DEC-088 already demonstrates that Tag presence can be consulted declaratively and read-only through a Conditional-Trait Binding without creating or modifying a resource pool.

## 4.3 But It Does Violate the Strongest Existing "Read-Only Tag" Interpretation

This is a genuine conflict.

A Tag that merely says:

```text
env:darkness
```

is passive metadata.

A Tag that says:

```text
counter:env:darkness
```

is still not modifying a resource, but it **participates in mechanical interpretation**.

Therefore the old formulation:

> Tags carry identity/vocabulary only; mechanical effects live in consuming subsystems.

cannot remain literally unchanged if Tags themselves are now capable of expressing counter-relations.

### Recommended resolution

Do **not** say:

> Tags have mechanical effects.

Say:

> **Tags do not execute mechanics. Tags may be operands in mechanical predicates evaluated by consuming rules.**

That preserves statelessness while allowing relational semantics.

This is a critical distinction.

---

# 5. Idea 5 — "Tags and Conditions Are NOT Distinct"

## Verdict: Reject the literal wording; adopt the architectural intent.

Conditions should **not** remain a separate mechanical record architecture.

But they should remain a distinct **Type**.

This is because DEC-079 currently contains substantial semantic machinery:

- global/localised scope;
- `Tier-Y Condition Value Z`;
- `Z = -Y`;
- stacking rules;
- replacement rules;
- condition-specific termination;
- specific exceptions such as Stunned, Incapacitated, Prone, Grappled;
- Slowed/Encumbered interaction;
- Sundered's hybrid Condition + Tag behaviour.



That is not merely a record format.

It is a **semantic lifecycle system**.

Trying to call Conditions simply "Tags with penalties" does not remove that machinery.

It hides it.

### Recommended formulation

> **Condition is a semantic Type of the unified state-record system. It is not a separate mechanical subsystem.**

That is materially better than:

> Conditions are Tags.

The former achieves the architectural objective.

The latter creates ambiguity over production, stacking, removal, and consumption.

---

# 6. The Sundered Case Is the Proof-of-Concept

`Sundered` is already evidence that the system naturally wants this architecture.

The current ruling describes Sundered as a Condition while applying a `state:sundered` Tag, and makes it permanent until repaired.

That is effectively two representations of one state.

The proposed architecture can collapse that duplication:

```text
State Record
    Type: Condition
    Name: Sundered
    Tier: Y
    Magnitude: -Y
    Location: X optional
    Lifecycle: persistent until authorised repair
    Projection: state:sundered
```

However, I recommend **not** retaining both a Condition and Tag record for the same state unless a consuming rule genuinely needs both.

Otherwise the architecture has failed to eliminate duplicate state.

---

# 7. Complexity Math

The unification has a genuine but bounded complexity benefit.

## 7.1 Current Architecture

Conceptually the rulebook currently contains:

| Component | Tags | Effects | Conditions |
|---|---:|---:|---:|
| Record format | 1 | 1 | 1 |
| Production rules | 1 | 1 | 1 |
| Tier/magnitude interpretation | limited | 1 | 1 |
| Location handling | partial | 1 | 1 |
| Removal/lifecycle | 1 | 1 | 1 |
| Stacking | limited | 1 | 1 |
| Interaction rules | 1 | 1 | 1 |
| Storage representation | 1 | 1 | 1 |

The problem is not simply the number of rules.

It is **three different grammars describing related state**.

## 7.2 Proposed Architecture

The shared layer becomes:

```text
ONE:
    record schema
    location representation
    tier representation
    magnitude representation
    state storage model
    generic application/removal vocabulary
```

Then the semantic layer becomes:

```text
THREE:
    Tag semantics
    Effect production semantics
    Condition lifecycle semantics
```

This is a real reduction.

But it is **not a 3 → 1 reduction**.

It is approximately:

```text
3 mechanical grammars
        ↓
1 mechanical grammar
+
3 semantic profiles
```

That is the honest complexity result.

## 7.3 Where Complexity Can Explode

The danger is adding:

- universal persistence rules;
- universal counters;
- universal stacking;
- universal replacement;
- universal removal;
- universal promotion;
- universal Type conversion.

If all of those become generic, the supposedly simple backbone becomes a mini programming language.

**That would be a failure.**

The unified backbone should therefore contain only the mechanics genuinely common to all three.

---

# 8. Conflicts and Honest Tensions

## 8.1 Tag Counter vs Statelessness

**Conflict level: REAL but resolvable.**

Current architecture treats Tags as read-only metadata. A counter relationship makes Tags mechanically queryable.

Recommended resolution:

> Tags remain stateless and non-executing. They may participate in read-only relational predicates evaluated by consuming mechanics.

No resource interaction is introduced.

This remains compatible with Invariant 17 and DEC-007.A.

DEC-007.A is particularly important: no unified state mechanism may modify Overflow.

---

## 8.2 Conditions vs Tags

**Conflict level: REAL architectural change.**

DEC-079 currently defines a distinct Condition grammar and extensive stacking/removal semantics.

The proposal intentionally replaces that architecture.

Because DEC-079 is non-canonical, this is permissible at the designer-ruling layer, but the departure must be explicit.

The correct statement is:

> DEC-079's Condition-specific record format is superseded by the unified State Record format; its semantic stacking, scope, and removal rules are retained only where still required.

---

## 8.3 Permanence

**Conflict level: LOW.**

The user's revised formulation is sound:

> Permanent is a default lifecycle state, not an absolute.

The crucial architectural rule is:

**Persistence is not a new universal field.**

Instead:

| Type | Default lifecycle |
|---|---|
| Tag | Persistent |
| Effect | Temporary |
| Condition | Defined by Condition semantics |

A specific record may override its Type default only through an authorised production/removal rule.

This handles `Sundered` without inventing a universal persistence mechanic.

---

## 8.4 DEC-025 and Skill Tags

**Conflict level: HIGH if implemented incorrectly.**

DEC-025 explicitly rejected formal Tags/categories on Advanced Skills because of the risk that players would optimise Skill selection around mechanical Effect entitlement.

The unification must **not** resurrect that system.

Therefore:

```text
Skill
  └── no Tag-based Effect entitlement
```

remains mandatory.

Tags can describe:

```text
weapon
creature
environment
equipment
state
```

but an Advanced Skill does not acquire a Tag that mechanically entitles it to an Effect.

The unified state architecture therefore **does not reopen DEC-025 by itself**.

A later proposal to tag Skills would be a separate decision requiring explicit reopening.

---

# 9. Concrete Recommended Design

## 9.1 Unified State Record

Adopt this as the working architecture:

```text
State Record
    Type       = Tag | Effect | Condition
    Name       = vocabulary identifier
    Tier       = Y, where applicable
    Magnitude  = Z, where applicable
    Location   = X, where applicable
```

No resource fields.

No duration field.

No HP/MP/Energy field.

No XP field.

No action-point field.

No alternate resolution engine.

## 9.2 Type Profiles

| Rule | Tag | Effect | Condition |
|---|---|---|---|
| Persistent by default | Yes | No | No fixed universal default |
| Produced by successful S-1 | No | Yes, where applicable | Usually through Effect |
| Can be location-scoped | Yes | Yes | Yes |
| Uses Tier | Where meaningful | Yes | Yes |
| Uses Magnitude | Where meaningful | Yes | Yes |
| May counter another Tag | Yes | No requirement | No requirement |
| Executes resource changes | **Never** | Only through already-authorised mechanics | **Never directly** |
| Requires separate resolution engine | No | No | No |

## 9.3 Counter Rule

The recommended exact rule is:

> **A Counter relation is a read-only predicate between state records. If a consuming rule declares Tag B as a counter of Tag A, the presence of B suppresses the mechanical applicability of A for that consuming rule. Neither Tag is removed. Counter evaluation creates no roll, cost, XP, resource transaction, HP change, or Overflow modification.**

Precedence:

```text
Presence
   ↓
Counter evaluation
   ↓
If counter exists → Tag has no effect on that consumer
   ↓
Otherwise → Tag is consumed normally
```

This is superior to removing the countered Tag because removal destroys information and creates lifecycle problems.

---

# 10. What Is Actually Being Removed

The proposal should explicitly claim these reductions:

### Remove

- Separate Tag record grammar.
- Separate Condition record grammar.
- Separate Wound/Condition mechanical record grammar where the same state schema suffices.
- Duplicate Location fields.
- Duplicate Tier fields.
- Duplicate Magnitude conventions.
- Duplicate generic storage rules.

### Retain

- Tag vocabulary.
- Effect vocabulary.
- Condition vocabulary.
- Effect production through S-1.
- Condition-specific stacking where necessary.
- Condition-specific removal.
- Tag relational consumption.
- Existing S-1/Core mechanics.
- DEC-007.A Overflow immutability.
- DEC-025 prohibition on Skill-side Effect entitlement.

This is the correct boundary.

---

# 11. Worked Architectural Cases

## 11.1 `env:darkness`

```text
Type: Tag
Name: env:darkness
Tier: none
Magnitude: none
Location: none
Lifecycle: scene-state
```

A consuming rule checks:

```text
env:darkness present?
    ↓
countered?
    ↓
apply darkness consequence or not
```

No roll.

No resource.

No Effect creation.

---

## 11.2 Darkness Immunity

```text
Type: Tag
Name: ignores:darkness
```

Relationship:

```text
ignores:darkness → counters → env:darkness
```

Neither Tag disappears.

---

## 11.3 Frightened

Current DEC-079 defines:

```text
Tier-Y Frightened Value -Y
```

with source-dependent termination.

Under the unified architecture:

```text
Type: Condition
Name: Frightened
Tier: Y
Magnitude: -Y
Location: none
Lifecycle: source/time/removal governed
```

The existing semantic rule survives; the record grammar changes.

---

## 11.4 Wound

The current Wound format is:

```text
Location X Tier-Y Wound Z
```

with `Z = -Y` under DEC-035.A.

Under the unified architecture:

```text
Type: Condition
Name: Wounded
Location: X
Tier: Y
Magnitude: -Y
```

This is particularly attractive because Wounded is already realised through the Condition pathway.

---

## 11.5 Sundered

Instead of maintaining:

```text
Condition: Sundered
+
Tag: state:sundered
```

as two independent records, use one unified state record whose consuming rules expose the relevant Tag identity:

```text
Type: Condition
Name: Sundered
Tier: Y
Magnitude: -Y
Location: X
```

with the `state:sundered` namespace identity available as its Tag-facing semantic representation.

The exact projection mechanism should be documented during implementation, but **duplicate state records should not be required merely because two subsystems currently refer to the same state.**

---

# 12. Recommended Adoption Boundary

The proposal should **not** attempt to rewrite all three systems simultaneously.

The architectural ruling should initially be:

> **Tags, Effects, and Conditions are three semantic Types implemented through one State Record architecture. Their existing production, consumption, stacking, and lifecycle rules remain independently governed until explicitly replaced.**

This gives the designer the complexity reduction immediately without accidentally deleting mechanics that have already been carefully resolved.

The second phase can selectively collapse duplicated rules.

That sequencing matters because DEC-079 contains more than a format; it contains condition-specific semantics.

---

# 13. Open Questions Requiring Human Ruling

1. **Is `Tier Y` mandatory on every unified record, or optional where the Type has no meaningful tier?**
2. **Is `Magnitude Z` mandatory on every unified record, or optional for boolean/descriptive Tags?**
3. **Is `Sundered` represented as one Condition record with Tag identity, or literally converted into a Tag-type state?**
4. **Should all persistent Effects become Tags automatically, or only Effects explicitly authored as persistent?**
5. **Can a Tag counter another Tag universally, or must every counter relationship be declared by the consuming mechanic?**
6. **If multiple counter-Tags apply, is the result simply boolean suppression, or can Tier/Magnitude influence the counter relationship?**
7. **Can Conditions directly counter Tags, or must all counter relationships be Tag-to-Tag?**
8. **Does a removed Tag require an explicit removal Effect, or may ordinary state changes invalidate it?**
9. **Does "temporary Effect" mean time-based only, or may an Effect be removed by state transition without a timer?**
10. **Are Wounds formally `Condition: Wounded`, or should Wound remain a fourth Type despite sharing the same record backbone?**
11. **Does the unified architecture supersede DEC-079's separate Condition format immediately at the proposal layer, or only after a replacement Condition semantic audit?**
12. **Should the unified architecture explicitly supersede the old Tag statement "mechanical effects live in consuming subsystems", replacing it with the narrower "Tags never execute mechanics but may participate in read-only predicates"?**
13. **Should the unified architecture be recorded as one architectural DEC with subsequent Type-specific amendments, or as separate DEC rulings for the three Types?**

---

# 14. Final Recommendation

**Adopt the architecture, not the literal identity claim.**

The winning formulation is:

> **Tags, Effects, and Conditions are three fiction-level Types sharing one mechanical State Record architecture. The common record consists of a Type, Name, and, where applicable, Tier Y, Magnitude Z, and Location X. Type-specific rules determine production, interpretation, persistence, stacking, and removal. Tags remain stateless and never modify resources, rolls, HP, or Overflow. Tags may participate in read-only relational predicates, including counter relationships, when explicitly consumed by a governing mechanic.**

This achieves the actual design objective:

```text
THREE CONCEPTS
      ↓
ONE STATE REPRESENTATION
      ↓
THREE SEMANTIC PROFILES
```

rather than the riskier:

```text
THREE CONCEPTS
      ↓
EVERYTHING IS A TAG
```

The first removes duplicated mechanical grammar.

The second removes distinctions that currently carry real semantic load.

**I recommend the first.**

The strongest evidence supporting the architectural direction is already inside Tiwas: Conditions and Wounds already share `Tier/Magnitude/Location` structure, Sundered already crosses Condition/Tag boundaries, and `env:freezing` already demonstrates Tags functioning as read-only predicates consumed by other mechanics. 

The remaining question is therefore not whether the three systems *can* share a backbone. They clearly can.

The real design question is whether the lifecycle and interaction rules can be kept sufficiently **Type-local** that the shared backbone produces a net reduction in rulebook weight.

**My assessment is yes — provided the backbone stays deliberately small.**