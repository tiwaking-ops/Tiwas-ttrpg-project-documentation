# OpenCode Project Documentation Report
## Tiwas TTRPG — Multi-LLM Comparative Analysis of Tags / Effects / Conditions Unification

| Field | Value |
|---|---|
| **Document Title** | Tiwas TTRPG — Multi-LLM Comparative Analysis and Collation: Tags / Effects / Conditions Unification |
| **Document Type** | Formal Project Documentation Report |
| **Document Version** | 1.0 |
| **Document Status** | Internal Analytical Report — Non-Canonical |
| **Report Date** | 2026-09-06 |
| **Author (LLM)** | OpenAI — GPT-5.6 Luna |
| **Project** | Tiwas TTRPG |
| **Primary Source** | `merge-tags-findings1.md` |
| **Assessment Basis** | All identifiable reports contained within the supplied merge file |
| **Authority** | No ruling authority; no mechanics promoted or changed |
| **Confidence** | High for the principal convergence/divergence findings; moderate where the source merge contains internally incomplete/truncated report material |

---

# 1. Executive Summary

This report compares, contrasts, assesses, and collates the LLM reports contained in `merge-tags-findings1.md`.

The reports show **strong convergence on the architectural objective but disagreement about how far the unification should extend**.

The most important finding is that the reports are **not actually divided over whether a shared representation is useful**. They converge on that point. The substantive disagreement concerns whether Tags should become mechanically equivalent to Effects and Conditions, particularly regarding:

- numeric Tier/Magnitude;
- Tag-to-Tag counters;
- removal;
- persistence;
- Condition semantics;
- whether the three concepts should remain functionally distinct.

The strongest common conclusion is:

> **Use one underlying state representation while retaining distinct semantic/functional profiles for Tags, Effects, and Conditions.**

This is materially different from literal full unification.

The reports broadly converge on the following architecture:

```text
                    ONE STATE REPRESENTATION
                             │
             ┌───────────────┼───────────────┐
             │               │               │
             ▼               ▼               ▼
            TAG            EFFECT         CONDITION
          metadata        payload          state
          /predicate      /transaction     /detriment
```

The principal recommendation of this comparative assessment is therefore:

> **Adopt a Data-Unified / Functionally-Split architecture as the leading design direction, but do not yet promote it to Canonical and do not implement the disputed runtime behaviours until their governance and mechanical semantics are explicitly resolved.**

This conclusion is more defensible than either extreme:

```text
THREE SYSTEMS REMAIN COMPLETELY SEPARATE
```

or:

```text
TAGS = EFFECTS = CONDITIONS
```

The evidence supports **shared representation, preserved semantics**.

The reports also expose an important methodological problem: several recommendations introduce additional mechanics—`Duration`, `Removal`, `Counters`, `StackRule`, precedence hierarchies, etc.—while simultaneously claiming to reduce complexity. That trade-off must be measured rather than assumed. A unified schema can reduce *representation duplication* while increasing *semantic rule complexity*.

---

# 2. Source Corpus and Report Inventory

`merge-tags-findings1.md` contains multiple LLM-produced reports and decision drafts concerning the same unification hypothesis. The identifiable substantive reports are:

| Report / Author | Primary Position | Overall Direction |
|---|---|---|
| **Claude Sonnet 5 — Tags / Effects / Conditions Unification Decision Draft** | Partial merge; strongest distinction between Tag and Condition semantics | Conservative |
| **Perplexity AI — Tag-Condition-Effect Unification Draft Execution Report** | Unified `StateRecord`, with explicit counters/removal mechanisms | Broad unification |
| **Gemini 2.5 Pro — Tag-Condition-Effect Unification Evaluation** | Data-unified, functionally split | Conservative |
| **Microsoft Copilot — Unified State Architecture / Multi-LLM Consolidation** | Unified state architecture while preserving functional boundaries | Moderate/conservative |
| **Unified State Record Decision Draft** | Conditional adoption of shared backbone with three Types | Moderate |
| **Additional embedded comparative material** | Strong emphasis on keeping backbone small and preventing a second engine | Conservative |

The merge file itself contains overlapping material from these reports, including repeated sections and recommendations. Consequently, this report treats **distinct architectural positions**, rather than repeated prose, as the unit of comparison.

The source material explicitly identifies Claude's report as advisory-only and non-ruling, while Perplexity and the other reports likewise classify their outputs as non-canonical decision material. 

---

# 3. Existing Tiwas Architectural Baseline

The comparison must be made against the existing Tiwas architecture, not against an abstract RPG design.

The supplied canonical rules establish:

- a fixed Core Test Transaction;
- resource expenditure through the natural roll;
- Overflow directly to HP;
- S-1 as the universal opposed contest;
- Zero-Step as the locked Tier-1 Location Index provider;
- 18 Core Architectural Invariants;
- no subsystem may silently replace the Core resolution architecture.

The current documentation also distinguishes Canonical material from non-canonical proposals and investigations. The Project Context explicitly describes Tags, Conditions and several downstream systems as Reserved/Open in the broader architecture. 

This matters because the unification reports are **design proposals against an already constrained architecture**, not greenfield design.

---

# 4. The Five Hypotheses Under Review

All reports are ultimately evaluating five related propositions:

| # | Hypothesis | Core Question |
|---:|---|---|
| 1 | Tags are like Effects but permanent; Effects arise from Skill Rolls | Can lifecycle distinguish the concepts? |
| 2 | Tags have Tier Y, Magnitude Z and possibly Location X | Should Tags carry mechanical potency data? |
| 3 | Tags can counter Tags | Should Tags participate in relational mechanics? |
| 4 | Tags and Conditions are not distinct | Can the semantic boundary be eliminated? |
| 5 | Tags can be removed | Should Tags have a general lifecycle/removal grammar? |

The Perplexity report characterises the five ideas as a candidate unified `StateRecord` architecture, including duration, removal and counter concepts. 

The more conservative reports decompose these propositions and find that they do **not all have the same architectural value**.

That decomposition is the critical improvement over treating "unification" as one indivisible decision.

---

# 5. Comparative Executive Verdicts

| LLM / Report | Shared Schema | Preserve Type Distinction | Tag Tier/Magnitude | Tag Counters | General Tag Removal | Full Merge |
|---|---:|---:|---:|---:|---:|---:|
| **Claude Sonnet 5** | **Yes** | **Yes** | Optional | Reject generic primitive | Yes, with explicit trigger | **No** |
| **Perplexity** | **Yes** | Yes, fiction-level | Yes | Yes, declarative | Yes | Conditional |
| **Gemini 2.5 Pro** | **Yes** | **Yes** | Optional / mostly inert | Reject active system | Highly constrained | **No** |
| **Microsoft Copilot** | **Yes** | **Yes** | Optional / controlled | Predicate/access interpretation | Restricted | **No** |
| **Unified State Record Draft** | **Yes** | **Yes** | Optional | Restricted | Yes | Conditional |
| **Consolidated direction** | **Yes** | **Yes** | **Optional** | **Read-only predicate only** | **Controlled** | **No** |

There is therefore a clear majority position:

> **Shared representation: strongly supported.**

> **Literal semantic merger: not supported.**

---

# 6. Report-by-Report Assessment

## 6.1 Claude Sonnet 5

### Position

Claude gives the strongest argument for **partial rather than full unification**.

Its central finding is:

> Effects and Conditions are sufficiently structurally similar to share a backbone, while Tags remain materially different because they are primarily vocabulary/metadata.

Claude specifically points to the existing Sundered precedent as evidence that a state can already carry both Tag identity and Condition-like mechanical structure without proving that Tags and Conditions are identical. 

### Strongest contribution

Claude identifies the key distinction between:

```text
shared representation
```

and:

```text
shared semantics
```

This is the most important conceptual distinction in the entire report set.

### Tag assessment

Claude argues that imposing Tier/Magnitude on all Tags would create schema noise because most Tags are boolean vocabulary items. It specifically cites the large existing Tag population versus the very small number of genuinely graded cases. 

### Counter assessment

Claude distinguishes:

- a Tag being **read by another mechanic**;
- a Tag **actively modifying another Tag**.

It accepts read-only predicates but rejects generic Tag-vs-Tag arithmetic as a new resolution mechanism. 

### Assessment

**Strength: Very high.**

Claude most clearly protects the architectural boundary against accidental creation of a second rules engine.

---

# 7. Perplexity AI

## 7.1 Position

Perplexity takes the most permissive interpretation.

It proposes a fairly complete `StateRecord`:

```text
StateRecord {
    type
    subtype
    id
    tier
    magnitude
    location
    source
    duration
    removal_tags
    counters
}
```

It explicitly recommends shared records for Tags, Effects and Conditions and proposes declarative counter/removal machinery. 

### Strongest contribution

Perplexity is strongest at **concrete operationalisation**.

It does not stop at:

> "These things could share a schema."

It attempts to specify:

- fields;
- defaults;
- lifecycle;
- counters;
- removal;
- production;
- governance;
- open questions.

That makes it useful as an implementation-oriented design exploration.

### Weakness

The architecture risks becoming exactly what the more conservative reports warn against:

```text
StateRecord
 + Duration
 + Removal
 + Counters
 + Stack Rules
 + Precedence
 + Type semantics
 + lifecycle rules
 + interaction rules
```

At that point the shared record is no longer merely a schema. It becomes a **general-purpose rule language**.

Perplexity itself acknowledges this risk: additional fields increase record size, and counter relationships can become a web of pairwise rules. 

### Assessment

**Strength: High for implementation exploration; lower as a final architecture.**

Perplexity's report is valuable for exposing what full unification actually costs.

---

# 8. Gemini 2.5 Pro

## 8.1 Position

Gemini's verdict is unusually clear:

> **Full unification is mechanically net-negative; partial data-layer unification is strongly positive.**

It proposes:

```text
Record Schema =
<ID, Type, Subtype, Tier Y, Magnitude Z, Location X, State Flags>
```

while retaining functional distinctions. 

### Strongest contribution

Gemini separates:

```text
data architecture
```

from:

```text
runtime execution architecture
```

This is an important distinction for Tiwas implementation.

A common data representation does **not** imply a common execution path.

### Major contribution

Gemini explicitly identifies the risk of turning Tags from:

```text
read-only metadata
```

into:

```text
active runtime participants
```

and warns that this can create a parallel state-tracking pipeline.

### Assessment

**Strength: Very high.**

Gemini's "Data-Unified, Functional-Split" formulation is one of the strongest candidate architectural descriptions in the source set.

---

# 9. Microsoft Copilot

## 9.1 Position

The Copilot material converges strongly on:

```text
THREE CONCEPTS
      ↓
ONE STATE REPRESENTATION
      ↓
THREE SEMANTIC PROFILES
```

rather than:

```text
EVERYTHING IS A TAG
```



### Strongest contribution

Copilot provides a useful architectural middle ground:

- common record;
- separate functional semantics;
- Tag predicates rather than active Tag-vs-Tag resolution;
- preserved Condition semantics;
- explicit protection against DEC-025 reopening.

It also correctly identifies that a generic unified backbone should contain **only mechanics genuinely common to all three**. 

### Assessment

**Strength: High.**

The principal weakness is that portions of the report appear to inherit conclusions from the other reports rather than independently deriving all of them. Therefore it is better treated as corroborating evidence than as independent proof.

---

# 10. Unified State Record Decision Draft

The dedicated State Record draft is more balanced than the broadest Perplexity architecture.

It proposes:

```text
StateRecord {
    Type
    Identity
    Tier
    Magnitude
    Location
    Source
    Duration
    StackRule
}
```

and explicitly says that the shared backbone does not eliminate Type-specific rules. 

Its strongest observation is:

> A shared backbone reduces record duplication, but does not eliminate production, stacking, counter, lifecycle or semantic rules.

That is mechanically important.

The draft also describes the reduction as approximately:

```text
3 mechanical grammars
        ↓
1 mechanical grammar
+
3 semantic profiles
```

rather than a simplistic 3 → 1 transformation. 

This is probably the most accurate complexity model in the corpus.

---

# 11. Areas of Strong Consensus

## 11.1 A Shared Representation Is Valuable

This is the strongest cross-report agreement.

The reports repeatedly identify duplication in:

- record format;
- Tier;
- Magnitude;
- Location;
- storage;
- lifecycle vocabulary.

The shared schema therefore has a legitimate architectural benefit.

---

## 11.2 Fiction-Level Distinctions Must Remain

All serious reports preserve the conceptual distinction between:

| Type | Primary Role |
|---|---|
| **Tag** | identity, classification, permission/context |
| **Effect** | outcome payload produced by resolution |
| **Condition** | persistent/ongoing mechanical state |

This is not cosmetic.

It controls:

- how records are produced;
- how they are consumed;
- whether they persist;
- whether they can stack;
- whether they can modify other systems.

---

## 11.3 Tags Must Not Become a Second Resolution Engine

This is the strongest architectural warning across the reports.

The reports consistently reject:

- Tag rolls;
- Tag resource expenditure;
- Tag arithmetic;
- Tag-driven alternative resolution;
- Tag modification of Core resources.

The concern is explicitly tied to the existing read-only/stateless Tag architecture and the single-resolution-engine constraint. 

---

## 11.4 DEC-025 Must Not Be Silently Reopened

The reports repeatedly identify the danger of Tags becoming sufficiently powerful that Skills eventually acquire Tag classifications.

The conservative position is:

```text
Skill
  ↓
does NOT acquire Tag-based Effect entitlement
```

The unified state representation itself does not require reopening DEC-025.

That boundary should remain explicit.

---

# 12. Major Areas of Disagreement

## 12.1 Should Tags Have Tier and Magnitude?

### Conservative position

Tags should have these fields **available but optional**.

Most Tags remain:

```text
Identity only
```

while exceptional Tags can become graded if separately authorised.

### Broad position

Tags can natively possess:

```text
Tier Y
Magnitude Z
Location X
```

as part of the common StateRecord.

### Assessment

The conservative position is stronger.

Making fields structurally available is not equivalent to making them mechanically meaningful.

Therefore:

```text
Tier/Magnitude:
    schema-capable
    ≠
    mandatory Tag mechanics
```

This preserves extensibility without forcing every boolean Tag to acquire meaningless numeric semantics.

---

# 13. Tag Countering

This is the **highest-risk disputed issue**.

## 13.1 Broad interpretation

A Tag contains:

```text
counters = [...]
```

and can suppress or defeat another Tag.

Perplexity explicitly proposes this form. 

## 13.2 Conservative interpretation

The consuming mechanic evaluates Tags.

Example:

```text
env:darkness
        ↓
permission requirement

trait:night-vision
        ↓
satisfies requirement
```

The Tags themselves do not fight each other.

The report explicitly describes this as a read-only predicate rather than Tag destruction or Tag modification. 

## 13.3 Assessment

The second architecture is superior.

The difference is:

```text
Tag A → modifies Tag B
```

versus:

```text
Consumer → evaluates Tag A and Tag B
```

The latter preserves statelessness.

### Recommendation

**Do not create a generic Tag-vs-Tag counter engine.**

Permit relational Tag predicates only when a consuming subsystem explicitly defines them.

---

# 14. Tag Removal

This issue is less dangerous than countering.

The reports agree that `Sundered` provides an existing precedent for permanent-until-repaired state. 

However, the reports disagree on whether general removal should be:

- a universal StateRecord property;
- a Tag-specific rule;
- an Effect-mediated operation;
- or restricted to explicitly authored Tags.

### Assessment

General removal is architecturally viable **provided it does not bypass the governing subsystem responsible for the state**.

A dangerous implementation would be:

```text
any action
    ↓
delete Tag
```

A safer implementation is:

```text
authorised removal mechanism
        ↓
normal state transition
        ↓
Tag removed
```

The distinction is essential.

---

# 15. Permanence

The reports largely converge on:

> **Permanent should be a lifecycle default, not an absolute ontological property.**

This is well supported by the existing Sundered precedent.

The StateRecord therefore should not assume:

```text
Tag = permanently immutable
Effect = always temporary
Condition = always temporary
```

because the existing design already contains exceptions.

The better model is:

| Type | Default |
|---|---|
| Tag | Persistent |
| Effect | Temporary/transactional |
| Condition | Defined by Condition semantics |

But defaults should not automatically become universal hard rules.

---

# 16. Conditions and Wounds

This is another area where the reports expose useful evidence.

The source material observes that Conditions and Wounds already share:

```text
Tier
Magnitude
Location
```

structure.

That is strong evidence for a common representation.

However:

```text
Wound ≠ automatically Condition
```

The question of whether Wounds are represented as Conditions, a subtype, or a distinct semantic record remains a governance question.

The unified architecture should therefore not prematurely erase the Wound semantic boundary.

---

# 17. Complexity Analysis

## 17.1 The Three Different Kinds of Complexity

The reports sometimes use "complexity" differently.

For Tiwas, at least three measures should be distinguished:

| Complexity Type | Meaning |
|---|---|
| **Representation complexity** | Number of data structures |
| **Rule complexity** | Number of mechanics/rules |
| **Cognitive complexity** | Number of decisions the GM/player must make |

A unified schema clearly reduces the first.

It does **not automatically reduce the second or third**.

---

## 17.2 Current Architecture

Conceptually:

```text
Tags
 ├─ record grammar
 ├─ semantics
 └─ consumer rules

Effects
 ├─ record grammar
 ├─ production
 └─ application

Conditions
 ├─ record grammar
 ├─ lifecycle
 └─ stacking/removal
```

---

## 17.3 Proposed Architecture

A successful unified architecture becomes:

```text
ONE
 ├─ record representation
 ├─ shared Tier/Magnitude/Location representation
 └─ shared storage vocabulary

PLUS

THREE
 ├─ Tag semantic profile
 ├─ Effect semantic profile
 └─ Condition semantic profile
```

This is a **real reduction**, but not a total merger.

---

# 18. Complexity Failure Mode

The reports correctly identify a specific danger.

If the shared record accumulates:

- `Duration`;
- `Removal`;
- `Counters`;
- `StackRule`;
- `Precedence`;
- `StateFlags`;
- `Source`;
- conversion rules;
- Type overrides;
- universal lifecycle rules;

then:

```text
StateRecord
```

becomes a small programming language.

The Unified State Record report explicitly warns that universal persistence, counters, stacking, replacement, removal, promotion and Type conversion can make the backbone a "mini programming language." 

That is the principal architectural failure mode.

---

# 19. Conflict Assessment Against Existing Tiwas Decisions

| Existing Decision / Constraint | Unification Risk | Assessment |
|---|---|---|
| **DEC-007.A — Overflow immutability** | StateRecord could be given resource effects | **Must remain absolute** |
| **DEC-025 — Skill-tag prohibition** | Powerful Tags could migrate onto Skills | **Must remain closed** |
| **DEC-058 / related Tag rulings** | Active Tag behaviour conflicts with statelessness | **Primary conflict** |
| **DEC-079 — Conditions** | Unified schema may erase Condition-specific semantics | **Must explicitly preserve semantics** |
| **DEC-080 — Tags** | Numeric/active Tags conflict with vocabulary-first design | **Major constraint** |
| **DEC-088 — Tag predicates** | Counter architecture could exceed predicate model | **Use as conservative precedent** |
| **Invariant 17** | Tag interaction with resource economy | **No violation permitted** |
| **Invariant 18** | Alternative resolution engine | **No Tag engine permitted** |

The reports correctly identify these tensions, although some reports overstate them as direct conflicts with Canonical material. The decision register indicates that many of these later DEC numbers are **non-canonical designer rulings**, not all Canonical rules. 

This distinction must be preserved in any subsequent promotion package.

---

# 20. Important Correction to the Reports' Reasoning

One recurring weakness is the tendency to describe some non-canonical rulings as though they were immutable architectural laws.

For example, the reports sometimes describe DEC-058/079/080/088 collectively as a locked prohibition.

The supplied Decision Register instead classifies the relevant later decisions as **Non-canonical designer rulings**. 

Therefore the correct governance statement is:

> These are **existing designer rulings that a new proposal would need to supersede, preserve, or explicitly amend**, not necessarily Canonical rules that cannot be changed.

By contrast, the Core Architectural Invariants and Canonical rules are genuinely binding unless formally reopened.

This distinction is important for the eventual 8-step promotion process.

---

# 21. Collated Best Architecture

Based on the cross-report evidence, the strongest architecture is:

## 21.1 Common Record

```text
StateRecord {
    Type
    Identity
    Tier? 
    Magnitude?
    Location?
}
```

Where:

- `Type` is mandatory;
- `Identity` is mandatory;
- `Tier` is optional unless the Type-specific rule requires it;
- `Magnitude` is optional unless the Type-specific rule requires it;
- `Location` is optional unless the consuming subsystem requires it.

---

## 21.2 Type Profiles

| Type | Default Function | Numeric Fields | Production | State Behaviour |
|---|---|---|---|---|
| **Tag** | Metadata / predicate | Usually none | Assertion / Trait / Equipment / Environment | Read-only |
| **Effect** | Outcome payload | As defined by Effect | Successful S-1 pathway | Transactional |
| **Condition** | Ongoing state | Tier/Magnitude as defined | Effect/subsystem pathway | Stateful |

This is the cleanest synthesis of the reports.

---

# 22. Recommended Tag Architecture

## 22.1 Default Tag

```text
Tag {
    Type = Tag
    Identity = X
}
```

No Tier/Magnitude is required.

---

## 22.2 Graded Tag

A specific designer ruling may permit:

```text
Tag {
    Type = Tag
    Identity = X
    Tier = Y
    Magnitude = Z
}
```

This should be an **explicitly authored exception**, not a universal Tag requirement.

This directly generalises the Sundered precedent without forcing every Tag to carry numerical semantics.

---

# 23. Recommended Counter Architecture

Reject:

```text
Tag A
   ↓
calculates against
   ↓
Tag B
```

Adopt:

```text
Consuming Mechanic
       ↓
reads Tag predicates
       ↓
determines whether its own rule applies
```

For example:

```text
env:darkness
       ↓
consumer asks:
"Does actor possess required permission?"
       ↓
trait:night-vision
       ↓
permission satisfied
```

No Tag is destroyed.

No Tag is modified.

No roll occurs.

No resource is spent.

No alternative resolution engine exists.

This is the safest synthesis of the reports.

---

# 24. Recommended Removal Architecture

General Tag removal is acceptable only as an **authorised state transition**.

Recommended conceptual grammar:

```text
Authorised removal mechanism
        ↓
identifies target StateRecord
        ↓
removes / invalidates record
```

Not:

```text
any ordinary action
        ↓
delete arbitrary Tag
```

The exact removal authority remains a designer ruling.

---

# 25. Recommended Persistence Architecture

Use lifecycle defaults:

```text
Tag       → Persistent by default
Effect    → Temporary by default
Condition → Type-specific
```

Do not make persistence the fundamental discriminator between Types.

Existing evidence demonstrates that persistence crosses Type boundaries.

---

# 26. Recommended Handling of Sundered

Sundered should be treated as the key architectural precedent.

It demonstrates that:

```text
Tag identity
+
Condition-like mechanical state
```

can coexist.

Therefore the system does **not** need to choose between:

```text
Sundered = Tag
```

and:

```text
Sundered = Condition
```

as mutually exclusive ontologies.

The more powerful abstraction is:

```text
StateRecord
    Type = Tag
    Identity = state:sundered
    [mechanical body where explicitly authorised]
```

This should be treated as an architectural precedent, not automatically generalised to every Tag.

---

# 27. Recommended Governance Strategy

The reports should **not** be merged into one new ruling.

Instead, their conclusions should be converted into discrete decision questions.

## Proposed decision sequence

### Decision A — Shared State Representation

Determine whether:

> Tags, Effects and Conditions may use one underlying record representation.

**Recommendation:** YES.

### Decision B — Type Semantics

Determine whether:

> Type-specific production and consumption semantics remain distinct.

**Recommendation:** YES.

### Decision C — Tag Numeric Fields

Determine whether:

> Tier/Magnitude are optional capabilities for Tags rather than mandatory fields.

**Recommendation:** YES.

### Decision D — Tag Countering

Determine whether:

> Tag relationships are read-only predicates evaluated by consuming mechanics rather than a generic Tag-vs-Tag engine.

**Recommendation:** YES.

### Decision E — Tag Removal

Determine whether:

> Tags may be removed through explicitly authorised state-transition mechanisms.

**Recommendation:** YES, subject to exact removal grammar.

### Decision F — Skill Tags

Determine whether:

> The architecture leaves DEC-025 untouched.

**Recommendation:** YES.

---

# 28. What Should NOT Be Adopted

The comparative evidence supports rejecting the following as a generic architecture:

| Proposal | Assessment |
|---|---|
| Every Tag must have Tier | **Reject** |
| Every Tag must have Magnitude | **Reject** |
| Tags perform arithmetic against Tags | **Reject** |
| Tags modify HP/MP/Energy | **Reject** |
| Tags modify Overflow | **Reject absolutely** |
| Tags perform their own rolls | **Reject** |
| Tags become an alternate resolution engine | **Reject** |
| Skills acquire Tag-based Effect entitlement | **Reject / DEC-025 remains closed** |
| Universal precedence hierarchy across all Types | **Reject pending explicit need** |
| Universal StackRule for every StateRecord | **Reject pending explicit need** |
| Universal Duration engine | **Reject pending explicit need** |
| Universal Type conversion | **Reject** |

These exclusions are where the conservative reports provide the greatest value.

---

# 29. What Should Be Preserved From the Broad Reports

The broad reports nevertheless contain useful material that should not be discarded.

| Broad Proposal | Preserve? | Treatment |
|---|---|---|
| `StateRecord` | **Yes** | Core architectural candidate |
| `Type` | **Yes** | Mandatory semantic discriminator |
| `Identity` | **Yes** | Mandatory |
| `Tier` | **Yes** | Optional capability |
| `Magnitude` | **Yes** | Optional capability |
| `Location` | **Yes** | Optional capability |
| `Source` | **Potentially** | Provenance/data-layer field, not necessarily game mechanic |
| `Duration` | **Not yet** | Type-specific rule until proven common |
| `Removal` | **Potentially** | Type-specific lifecycle rule |
| `Counters` | **Not as generic runtime engine** | Read-only predicate concept only |
| `StackRule` | **Not yet** | Preserve existing Type-specific semantics |
| `StateFlags` | **Potentially** | Implementation metadata, not player-facing mechanic |

---

# 30. Overall Assessment of the LLM Reports

## Quality Ranking by Architectural Contribution

| Rank | Report | Reason |
|---:|---|---|
| **1** | **Claude Sonnet 5** | Best identification of the Tag/Condition semantic boundary and second-engine risk |
| **2** | **Gemini 2.5 Pro** | Best explicit Data-Layer vs Functional-Layer distinction |
| **3** | **Unified State Record Draft** | Best balanced complexity model |
| **4** | **Microsoft Copilot** | Strong synthesis and governance-aware middle position |
| **5** | **Perplexity AI** | Most concrete implementation proposal, but most likely to over-generalise |

This ranking is **analytical**, not an assessment of model capability generally.

It measures usefulness for this specific Tiwas architectural question.

---

# 31. Final Collated Verdict

## 31.1 Architecture

**ADOPT AS DESIGN DIRECTION:**

```text
THREE FICTION-LEVEL CONCEPTS
             ↓
     ONE STATE RECORD
             ↓
 THREE FUNCTIONAL PROFILES
```

Not:

```text
THREE CONCEPTS
       ↓
ONE UNIVERSAL MECHANIC
```

---

## 31.2 Tags

Tags remain:

- identity-oriented;
- vocabulary-oriented;
- read-only;
- non-resource;
- non-resolution-engine;
- generally non-numeric.

Tier/Magnitude/Location should be **available where explicitly authorised**, not mandatory.

---

## 31.3 Effects

Effects remain:

- resolution-produced;
- transactional;
- governed by the existing resolution architecture;
- semantically distinct from persistent state.

---

## 31.4 Conditions

Conditions remain:

- stateful;
- mechanically meaningful;
- Type-specific;
- governed by their own stacking/lifecycle semantics where required.

Their representation may share the StateRecord.

Their semantics should not be erased.

---

# 32. Required Human Decisions

The comparative exercise has reduced the original broad proposal to a much smaller set of genuine decisions.

| ID | Decision Required | Recommended Direction |
|---|---|---|
| **UR-01** | Adopt common StateRecord? | **Yes** |
| **UR-02** | Preserve three Types? | **Yes** |
| **UR-03** | Are Tag Tier/Magnitude optional? | **Yes** |
| **UR-04** | Generic Tag-vs-Tag counters? | **No** |
| **UR-05** | Read-only Tag predicates? | **Yes** |
| **UR-06** | General Tag removal? | **Yes, authorised only** |
| **UR-07** | Universal Duration field? | **Not yet** |
| **UR-08** | Universal StackRule? | **Not yet** |
| **UR-09** | Universal precedence hierarchy? | **No, unless separately justified** |
| **UR-10** | Preserve DEC-025? | **Yes** |
| **UR-11** | Can StateRecord directly affect resources? | **No** |
| **UR-12** | Can StateRecord alter Overflow? | **No — absolute** |
| **UR-13** | Replace Condition semantics wholesale? | **No** |
| **UR-14** | Treat Sundered as architectural precedent? | **Yes, cautiously** |

---

# 33. Governance Status

No report reviewed here has authority to modify Canonical Tiwas mechanics.

The source reports themselves consistently identify their proposals as non-canonical/advisory material. 

Accordingly:

```text
Current State
     │
     ▼
Multi-LLM Evidence
     │
     ▼
This Comparative Assessment
     │
     ▼
Human Designer Ruling
     │
     ▼
Formal Promotion Process
     │
     ▼
Canonical / Locked
```

No step should be skipped.

---

# 34. Recommended Next Action

**Do not yet implement the complete StateRecord proposed by the broadest reports.**

Instead, the next design artifact should be a **minimal StateRecord architectural specification** containing only:

```text
Type
Identity
Tier? 
Magnitude?
Location?
```

with explicit Type profiles for:

```text
Tag
Effect
Condition
```

Then separately specify:

1. production;
2. consumption;
3. persistence;
4. removal;
5. stacking;
6. Tag predicates;
7. Sundered;
8. Wound interaction.

This sequencing prevents lifecycle and interaction mechanics from contaminating the underlying data architecture before the data architecture itself is settled.

---

# 35. Final Conclusion

The multi-LLM evidence is substantially more convergent than the individual reports initially suggest.

The reports do **not** establish that Tags, Effects and Conditions should become one undifferentiated mechanic.

They establish something narrower and considerably stronger:

> **Tiwas has a credible case for one common state representation with three deliberately preserved semantic/functional profiles.**

The principal architectural win is therefore **schema unification**, not semantic homogenisation.

The principal architectural danger is converting the schema into a universal rules engine.

The recommended target is:

```text
                    STATE RECORD
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
       TAG             EFFECT          CONDITION
   read-only          transactional      stateful
   predicate          payload            detriment
   usually ungraded   resolution-bound   Type-specific
```

This preserves the strongest findings from all reports while rejecting the highest-risk extrapolations.

**Recommended disposition:**

> **Proceed with a minimal, Data-Unified / Functionally-Split StateRecord design as a non-canonical architectural candidate. Do not yet promote or implement generic counters, universal lifecycle fields, universal precedence, or full Tag/Condition semantic identity.**

The existing project governance should then treat the resulting architecture as a **new designer-ruling candidate**, with each material departure from existing non-canonical DEC rulings explicitly recorded rather than silently overwritten.