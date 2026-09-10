---
document:
  title: "Tiwas — Repeated-Defense Fatigue and Reaction Architecture — Chat Results / OpenCode Handoff"
  version: "1.0"
  status: "NON-CANONICAL ADVISORY — OpenCode handoff; no authority-changing action authorized"
  authority: "Design advisory only"
  author: "GPT-5.6 Luna"
  author_version: "GPT-5.6 Luna"
  date: "2026-09-10"
  scope: "Results and design conclusions from the 2026-09-10 Tiwas design discussion concerning DEC-075, DEC-079, DEC-132, Active Defense, repeated-defense fatigue, and reaction architecture"
  canonicality: "No new mechanic in this report is Canonical / Locked"
---

# Tiwas — Repeated-Defense Fatigue and Reaction Architecture
## Chat Results / OpenCode Handoff

## 1. Purpose

This document records the complete substantive results of the current design discussion concerning:

1. the previously rejected repeated-Defense fatigue mechanism;
2. the designer's subsequent revocation of that rejection;
3. integration of repeated-Defense fatigue with the existing Effect/Condition architecture;
4. interaction with DEC-079's existing `Fatigued` Condition;
5. interaction with DEC-132's reaction framework;
6. the remaining decisions required before a superseding DEC can be drafted and potentially promoted.

This document is **NON-CANONICAL ADVISORY**.

It does not itself amend, supersede, reopen, promote, or demote any DEC.

---

# 2. Authority and Existing State

## 2.1 Canonical baseline

The Canonical Rules establish the Core Test as the mandatory resolution transaction. Every Skill Test:

1. rolls 1d100;
2. determines resource domain;
3. determines Success/Failure;
4. pays Cost equal to the natural roll;
5. resolves Overflow;
6. resolves Failure XP;
7. resolves failed-Double / Advanced Skill effects;
8. performs Recovery;
9. ends.

No Universal Play subsystem may replace this transaction. fileciteturn1file0L1-L20

Overflow is additionally immutable: no Tag, Trait, Effect, Condition, or subsystem may reduce, redirect, absorb, or otherwise modify Overflow. fileciteturn1file4L1-L15

These constraints remain binding on all proposals in this report.

---

# 3. Existing Active Defense Architecture

## 3.1 Active Defense is already established

The current non-canonical designer rulings establish:

| Decision | Existing rule |
|---|---|
| DEC-044 | Active Defense is the Defense architecture |
| DEC-045 | Defender makes the Defense roll |
| DEC-046 | Defense is voluntary; defender may decline |
| DEC-047 | Active Defense is uncapped |
| DEC-048 | Active Defense is post-hoc Effect mitigation, not a gate |
| DEC-049 | Each Effect receives an independent Defense roll |
| DEC-050 | Any auto-applied Effect may be defended against, including positive Effects |
| DEC-097 | Successful Defense mitigation uses Defender's Margin |
| DEC-103 | Effect mitigation uses Skill-Tier shred followed by Margin de-escalation |

The defender therefore already performs genuine Core Tests when using Active Defense, including normal resource expenditure and normal Core consequences. fileciteturn3file1L1-L20

## 3.2 Important consequence

Repeated Defense is therefore not currently a free or abstract defensive permission.

Each Active Defense already carries:

- natural-roll Cost;
- Physical Energy / MP expenditure;
- possible Overflow;
- Failure XP;
- failed-Double eligibility;
- Recovery.

This existing Cost model remains the first layer of repeated-defense pressure.

---

# 4. Original DEC-075 Position

## 4.1 Previous ruling

DEC-075 closed OPEN-010 by rejecting a separate repeated-Defense fatigue/exhaustion subsystem.

The recorded decision was:

> no fatigue/exhaustion penalty beyond existing Cost/Overflow.

The same record explicitly stated that if fatigue were implemented in the future, it should be represented as a selectable Condition-tier Effect rather than as a standalone subsystem. fileciteturn3file13L1-L4

The Alpha Playtest Corpus likewise records OPEN-010 as closed through DEC-075. fileciteturn3file0L1-L15

## 4.2 Designer change established during this discussion

The designer has now explicitly **revoked the earlier rejection of repeated-defense fatigue**.

The reason is architectural rather than conceptual:

- the original objection was substantially a **bookkeeping objection**;
- Tiwas now has a unified Effect/Condition/StateRecord architecture;
- therefore repeated-defense fatigue can be represented as an ordinary existing state record rather than requiring a hidden counter, separate resource pool, or separate fatigue subsystem.

This is a **new design direction**, not an automatic amendment of DEC-075.

A superseding DEC is required.

---

# 5. Existing Fatigued Condition

## 5.1 DEC-079 definition

The current Conditions architecture defines `Fatigued` as an existing Condition.

The alpha vocabulary records:

| Condition | Existing mechanical scope |
|---|---|
| `Fatigued` | `−Y` to **all Body Skills** |
| Removal | Rest / recovery |
| Record architecture | Tier / Magnitude Condition system |

The Condition architecture defines Condition magnitude as:

`Z = −Y`

and DEC-079 gives Fatigued global scope across Body Skills. fileciteturn3file8L1-L20

## 5.2 Critical conflict identified

A proposed repeated-defense rule cannot redefine Fatigued as:

> “−Y to Active Defense only”

without changing DEC-079.

That would directly conflict with DEC-079's established global scope:

`Fatigued → −Y to all Body Skills`

Therefore, any superseding DEC must either:

1. use DEC-079's existing Fatigued semantics; or
2. explicitly supersede/amend DEC-079.

The preferred architecture from this discussion is **Option 1**.

---

# 6. Effect / Condition Architecture Now Available

The later StateRecord work materially changes the bookkeeping analysis.

DEC-115/117 establish a unified state-record shape covering Tags, Effects and Conditions:

```text
Type
Tier Y
Magnitude Z
Location X [optional]
id
source
duration
removal_tags
counters
```

For Effects and Conditions:

`Z = −Y`

The architecture is explicitly intended to unify existing state representation rather than introduce a new state engine. fileciteturn2file3L1-L20

DEC-127 formally names the relevant systems:

- **Effect Tier Magnitude System**
- **Effect Heal System**

The latter reduces applicable records stepwise toward zero, subject to the existing healing-gate rules. fileciteturn2file8L1-L10

This means repeated-defense fatigue can now be recorded as ordinary Condition state.

---

# 7. Recommended Repeated-Defense Fatigue Architecture

## 7.1 Design objective

The proposed mechanism should:

1. preserve uncapped Active Defense;
2. preserve voluntary Defense;
3. preserve the existing Core Test;
4. avoid a hidden numerical counter;
5. avoid a new resource pool;
6. use the existing `Fatigued` Condition;
7. allow repeated Defense to create increasing mechanical pressure;
8. use the existing Effect/Condition bookkeeping architecture.

---

# 8. Trigger

## 8.1 Recommended trigger

**Recommended rule:**

> The first Active Defense in a continuous defensive sequence does not generate Fatigued. Each subsequent qualifying Active Defense in that same sequence applies or increases the character's `Fatigued` Condition.

Formally, for a continuous sequence containing `n` qualifying Defense rolls:

```text
Fatigue additions = max(0, n − 1)
```

This is a **design recommendation**, not a current rule.

## 8.2 What counts as a qualifying Defense

A qualifying Defense is a Defense Core Test performed under the Active Defense architecture.

The fatigue trigger should therefore attach to the **Defense transaction**, not to every reaction generically.

A reaction that independently performs a defensive Core Test should qualify if the reaction is mechanically functioning as another Active Defense.

A reaction that performs a different combat function should not automatically generate Defense fatigue.

---

# 9. Continuous Defensive Sequence

## 9.1 Recommended boundary

The phrase **“continuous defensive sequence”** is intentionally preferred over:

- “per round”;
- “per scene”;
- “per encounter”;
- “after N rolls.”

The latter options would introduce a temporal bookkeeping dependency that is not currently defined by Tiwas.

DEC-133 explicitly leaves broader duration/time-unit scale open, while DEC-082 does not establish a universal real-world duration for rounds, scenes, or other intervals. fileciteturn3file10L1-L15

## 9.2 Required definition

Before this mechanism can become fully executable, the superseding DEC must define exactly when the sequence starts and ends.

**This remains an unresolved design parameter.**

The report therefore does **not** authorize an arbitrary scene/round reset.

---

# 10. Mechanical Effect

## 10.1 Recommended implementation

Use the existing `Fatigued` Condition.

Do **not** create:

- `Defense Fatigue`;
- `Repeated Defense Fatigue`;
- a separate fatigue counter;
- a Defense Exhaustion pool;
- a Defense-specific resource.

The mechanical effect remains the DEC-079 Fatigued effect:

`−Y to all Body Skills`

This preserves DEC-079 rather than creating a conflicting local interpretation.

## 10.2 Important consequence

Repeated-defense fatigue therefore affects more than Active Defense.

For example, if the resulting Condition is:

```text
Tier-1 Fatigued
Magnitude = −1
```

the −1 applies to all Body Skills under DEC-079.

It is **not** correct to document this as:

```text
−1 Active Defense only
```

unless DEC-079 itself is explicitly amended.

---

# 11. Stacking and Escalation

## 11.1 Recommended model

Fatigue should accumulate as ordinary Condition magnitude/Tier state.

Conceptually:

| Qualifying Defense count in sequence | Result |
|---:|---|
| 1 | No new Fatigued |
| 2 | Fatigued Tier 1 / Magnitude −1 |
| 3 | Fatigued Tier 2 / Magnitude −2 |
| 4 | Fatigued Tier 3 / Magnitude −3 |
| 5 | Fatigued Tier 4 / Magnitude −4 |

This table is a **proposed progression**, not current canonical mechanics.

## 11.2 Why this model is preferred

It converts the formerly rejected hidden counter:

```text
Defense count = 1, 2, 3, 4...
```

into visible existing game state:

```text
Fatigued Tier 1
Fatigued Tier 2
Fatigued Tier 3
...
```

No separate bookkeeping subsystem is required.

The existing StateRecord architecture already supports Tier and Magnitude state. fileciteturn2file3L1-L20

## 11.3 Important unresolved question

The project must still explicitly determine whether repeated applications:

- increase the existing Fatigued Tier;
- create multiple same-Tier Fatigued records;
- or use another existing Condition stacking rule.

The recommendation is **Tier escalation of the existing Fatigued state**, because this most directly represents cumulative fatigue without creating multiple parallel fatigue records.

---

# 12. Duration and Removal

## 12.1 Recommended principle

Fatigue should **not automatically reset at the end of a round**.

Doing so would introduce a new round-reset mechanic and would make the condition a hidden temporal counter again.

## 12.2 Recommended removal

Use the existing Effect Heal System / Condition recovery architecture.

The Fatigued record therefore remains until an existing permitted recovery/removal mechanism reduces or removes it.

This preserves the existing distinction between:

- applying a state;
- healing/removing a state;
- tracking the state.

## 12.3 No new recovery resource

The mechanism must not introduce:

- Fatigue Points;
- Defense Exhaustion Points;
- Defense counters that regenerate;
- scene-reset tokens.

That would conflict with the project's established no-new-pool architecture.

DEC-115/117 explicitly preserve the rule that StateRecords do not directly modify HP, Overflow, or resource pools. fileciteturn2file11L1-L15

---

# 13. Interaction with Core Test

Repeated-defense fatigue must not modify the Core Test transaction.

The sequence remains:

```text
Defense Skill
    ↓
Core Test
    ↓
natural d100 roll
    ↓
Success / Failure
    ↓
Cost = natural roll
    ↓
Overflow if applicable
    ↓
Failure XP
    ↓
failed Double / Advanced Skill
    ↓
Recovery
```

The Fatigued Condition modifies the **effective Skill value available to the test** according to DEC-079.

It does not modify:

- natural roll;
- Cost;
- Overflow;
- Failure XP formula;
- Double qualification;
- Recovery.

This preserves DEC-006/007/009 and the Overflow immutability clause.

---

# 14. Interaction with Active Defense

## 14.1 Active Defense remains uncapped

The fatigue mechanism must **not** reinstate a Defense-roll ceiling.

DEC-047 remains:

> Active Defense is uncapped.

Repeated-defense fatigue creates an accumulating state consequence rather than an explicit prohibition.

## 14.2 Defense remains voluntary

The defender can still decline Active Defense.

Fatigue therefore creates a genuine decision:

```text
Defend again
    ↓
pay another Core Test Cost
    +
accept/increase Fatigued state
```

or:

```text
Decline Defense
    ↓
avoid another Defense transaction and its fatigue trigger
    ↓
accept the incoming Effect according to existing rules
```

This preserves DEC-046.

---

# 15. Interaction with DEC-103 Effect Mitigation

DEC-103 establishes that Active Defense is a voluntary mitigation roll against an already-applied Effect.

The Defense process performs:

1. Skill-Tier comparison / shred;
2. Margin de-escalation;
3. Tier/Magnitude carry;
4. possible Effect negation.

The system applies to Effects, not HP. fileciteturn3file16L1-L15

Repeated-defense fatigue should therefore occur **as a consequence of making another qualifying Defense transaction**, not as a modification of the Effect-mitigation mathematics.

The following remain independent:

```text
Effect magnitude
        ↓
DEC-103 mitigation
        ↓
Defense result
```

and:

```text
Number of repeated Defense transactions
        ↓
Fatigued Condition
```

No Fatigued rule should modify DEC-103's Skill-Tier shred or Margin mathematics directly.

---

# 16. Interaction with Reactions — DEC-132

## 16.1 Existing reaction framework

DEC-132 adopted structured tag-triggered reactions.

A reaction is permitted when:

1. a defined trigger occurs during another combatant's turn;
2. the character possesses a specific reaction-granting Tag;
3. the reaction resolves as a full S-1 combat exchange with the normal Core Test, Cost, Overflow and Failure XP consequences.

Reactions do not create extra turns or a new action-point economy. PCs and automated characters have equal eligibility. fileciteturn3file5L1-L20

## 16.2 Recommended reaction principle

Reactions should remain a **framework**, not a universal action list.

Specific trigger definitions and reaction-granting Tags remain content-authoring. The Alpha Corpus explicitly records those items as not yet table-ready. fileciteturn3file2L1-L15

---

# 17. Reaction vs Active Defense

## 17.1 Current unresolved DEC-132 question

DEC-132 explicitly carries:

> whether a reaction replaces or stacks with Active Defense on the same incoming Effect

as an open question. It also carries reaction frequency limits as open. fileciteturn3file10L1-L15

## 17.2 Recommendation from this discussion

The recommended architecture is:

> A qualifying Reaction does not automatically replace Active Defense. If both are independently eligible, they may stack, subject to the specific reaction's trigger and permission.

This preserves the distinction between:

- Active Defense as the universal/default defense mechanism;
- a separate reaction granted by an explicit Tag.

However, this recommendation remains **NON-CANONICAL** until the designer rules on the DEC-132 carry.

---

# 18. Reaction Frequency

## 18.1 Rejected direction

Do not introduce a universal:

```text
one Reaction per round
```

rule merely because other RPGs use that model.

It would introduce a new global action-economy restriction not required by DEC-132's architecture.

## 18.2 Recommended direction

Do not impose a universal scene/round Reaction limit at framework level.

Instead, specific reaction-granting content should define its own trigger and, where required, its own frequency.

This keeps the framework lightweight and avoids another universal counter.

The exact content-authoring mechanism remains open.

---

# 19. External Comparative Research Used During the Discussion

The discussion considered several existing RPG approaches as comparative design evidence.

These were treated as **comparative references**, not as sources of Tiwas rules.

| System | Relevant observation | Tiwas implication |
|---|---|---|
| D&D | Explicit Reaction resource, normally one Reaction between turns | Demonstrates clear reaction permission/frequency architecture |
| Pathfinder 2e | Explicit reaction triggers and frequency restrictions | Supports precise trigger definitions and content-authored frequency |
| World of Darkness / V20 | Multiple-action / repeated-defense mechanics can impose declining defensive effectiveness | Demonstrates one possible repeated-defense pressure model, but does not fit Tiwas directly |
| Exalted | Highly permissive reflexive reactions | Demonstrates the opposite extreme; repeated reactions can become difficult to constrain |
| Savage Worlds | Lightweight reactions can sometimes be comparatively permissive | Shows that universal reaction limits are not intrinsically necessary |

The conclusion was **not** to copy any of these systems.

The relevant Tiwas-specific constraint is that a Tiwas Reaction is a full Core/S-1 transaction rather than a lightweight abstract permission.

---

# 20. Bookkeeping Analysis

## 20.1 Original problem

The original repeated-defense fatigue rejection was substantially motivated by bookkeeping.

A separate system would have required tracking something such as:

```text
Defense 1
Defense 2
Defense 3
Defense 4
...
```

and then determining when the counter resets.

## 20.2 Current architecture

The StateRecord architecture changes the implementation cost.

Instead of:

```text
Hidden Defense Counter = 4
```

the state can become:

```text
Fatigued
Tier = 4
Magnitude = −4
```

The condition itself becomes the visible bookkeeping state.

## 20.3 Result

The previous bookkeeping objection is no longer sufficient reason to reject repeated-defense fatigue.

This does **not** prove that fatigue is desirable.

It establishes only that the previous architectural objection has been substantially removed.

---

# 21. Design Assessment

## 21.1 Advantages

The recommended architecture has the following properties:

| Property | Result |
|---|---|
| Active Defense remains uncapped | Yes |
| Defense remains voluntary | Yes |
| Existing Core Test preserved | Yes |
| Existing Cost/Overflow preserved | Yes |
| No new resource pool | Yes |
| No hidden Defense counter | Yes |
| Existing Fatigued vocabulary reused | Yes |
| Existing Condition architecture reused | Yes |
| Existing Effect Heal System reused | Yes |
| Reactions remain tag-gated | Yes |
| No mandatory universal reaction frequency | Yes |
| No new action-point economy | Yes |

## 21.2 Primary risk

The principal design risk is **scope**.

Because DEC-079 defines Fatigued globally as:

`−Y to all Body Skills`

repeated Defense can eventually impair:

- attacks;
- physical movement-related Skills where applicable;
- other Body Skills;
- future Body Skill tests.

Therefore this mechanism is considerably broader than:

> “Repeated Defense becomes less effective.”

That broader consequence is intentional under the recommended architecture and must be accepted explicitly by the designer.

---

# 22. Mathematical / Logical Model

Define:

- `n` = number of qualifying Active Defense Core Tests in the current continuous defensive sequence.
- `F` = resulting Fatigued Tier.
- `Z` = Fatigued Magnitude.
- `S` = relevant Body Skill before Fatigued.
- `S_eff` = effective Skill after Fatigued.

Recommended model:

```text
F = max(0, n − 1)
```

and:

```text
Z = −F
```

therefore:

```text
S_eff = S − F
```

subject to the existing DEC-079 Condition architecture and all existing Skill/Test rules.

This mathematical model is **PROPOSED ONLY**.

It is not currently Canonical.

---

# 23. Worked Structural Example

Assume a character performs four qualifying Active Defense rolls during one continuous defensive sequence.

| Defense | Fatigued state after Defense | Body-Skill penalty |
|---:|---|---:|
| 1 | None added | 0 |
| 2 | Tier-1 Fatigued | −1 |
| 3 | Tier-2 Fatigued | −2 |
| 4 | Tier-3 Fatigued | −3 |

If the character originally has:

`Body Skill = 50`

then after the fourth qualifying Defense:

`Effective Skill = 50 − 3 = 47`

The next Defense remains a normal Core Test.

The natural roll remains the natural roll.

The Cost remains the natural roll.

Overflow remains immutable.

Failure XP remains:

`max(0, Roll − Effective Skill)`

No special Defense resource is introduced.

---

# 24. What This Discussion Does NOT Establish

The following are explicitly **not ruled by this report**:

| Item | Status |
|---|---|
| Exact repeated-defense trigger | Proposed |
| Definition of continuous defensive sequence | Open |
| Exact Fatigued Tier progression | Proposed |
| Whether Tier escalation or record stacking is used | Open |
| Exact Fatigued maximum | Open |
| Exact duration | Open |
| Exact healing/removal invocation | Existing-system dependent / requires confirmation |
| Whether Reaction + Active Defense may stack | Recommended, not ruled |
| Universal Reaction frequency limit | Recommended none, not ruled |
| Exact reaction Tag vocabulary | Open |
| Exact reaction trigger menu | Open/content-authoring |
| Amendment of DEC-075 | Required if supersession is adopted |
| Amendment of DEC-079 | Not required under the recommended architecture |
| Promotion to Canonical | Not performed |

---

# 25. Required Governance Action

If the designer accepts the direction, OpenCode should **not immediately modify Canonical Rules**.

The correct next step is to draft a **superseding DEC-075** as a non-canonical designer ruling.

The new DEC should explicitly state:

1. DEC-075's previous “no repeated-Defense fatigue” ruling is superseded.
2. Active Defense remains uncapped.
3. Defense remains voluntary.
4. Repeated Defense uses the existing `Fatigued` Condition rather than a new Condition.
5. Fatigued retains DEC-079's global `−Y to all Body Skills` semantics.
6. No hidden counter or new resource pool exists.
7. Each qualifying Defense remains a complete Core Test.
8. Overflow remains immutable.
9. The exact trigger boundary is explicitly defined.
10. The exact Tier/Magnitude escalation is explicitly defined.
11. Duration/removal is explicitly defined.
12. Interaction with reactions is explicitly addressed or deliberately left to DEC-132.

---

# 26. Recommended OpenCode Handling

OpenCode should treat this document as:

```text
NON-CANONICAL DESIGN ADVISORY
```

and should **not**:

- edit `canonical/rules/` on the basis of this report;
- mark DEC-075 as superseded without a designer ruling;
- invent the missing trigger boundary;
- invent a maximum Fatigued Tier;
- narrow Fatigued to Active Defense only;
- introduce a Defense counter;
- introduce a new fatigue resource;
- introduce a universal Reaction-per-round pool;
- silently resolve the DEC-132 carried-open questions.

OpenCode may use this document to prepare a candidate superseding DEC for designer review.

---

# 27. Final Design Position From This Discussion

The strongest current architectural conclusion is:

> **Repeated Defense fatigue should be implemented, if adopted, as ordinary existing `Fatigued` Condition state rather than as a separate Defense-fatigue subsystem.**

The preferred structure is:

```text
Active Defense
    ↓
Full Core Test
    ↓
First Defense in sequence
    ↓
No Fatigue

Subsequent Defense
    ↓
Full Core Test
    ↓
Apply / increase existing Fatigued Condition
    ↓
Fatigued imposes −Y to all Body Skills
```

This approach resolves the original bookkeeping objection without creating a new engine or resource pool.

The principal remaining design question is **not whether Tiwas can represent repeated-defense fatigue**. The current StateRecord architecture can.

The principal remaining questions are:

1. **What precisely constitutes a continuous defensive sequence?**
2. **Does each subsequent Defense increase Fatigued Tier by exactly 1?**
3. **What exact mechanism removes/reduces the resulting Condition?**
4. **Can a Reaction and Active Defense both resolve against the same incoming Effect?**
5. **What frequency restrictions, if any, apply to individual reaction permissions?**

Until those questions are explicitly ruled, the mechanism remains **NON-CANONICAL**.

---

# 28. Source / Provenance Notes

This report was prepared from:

- `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md`;
- `_consolidation/decision-register.md`;
- `PROJECT_CONTEXT.md`;
- `Tiwas-Alpha-Playtest-Corpus-2026-09-08.md`;
- the design conclusions and comparative analysis conducted during the present Tiwas design discussion.

The Canonical Rules remain authoritative over any conflicting proposal. The Decision Register is a classification/working record and does not itself create Canonical authority. fileciteturn1file0L1-L20 fileciteturn1file4L1-L15

No new rule in this report has completed the Tiwas promotion process.

---

# 29. Status Summary

| Item | Current status |
|---|---|
| DEC-075 original rejection | **Designer-revoked direction; formal superseding DEC still required** |
| Repeated-defense fatigue | **Proposed** |
| Use existing `Fatigued` Condition | **Recommended** |
| Fatigued scope | **Existing DEC-079 global Body-Skill scope retained** |
| Hidden Defense counter | **Rejected** |
| New fatigue resource pool | **Rejected** |
| Active Defense ceiling | **Uncapped; preserved** |
| Defense voluntary | **Preserved** |
| Core Test | **Preserved** |
| Overflow | **Immutable; preserved** |
| Effect/Condition StateRecord architecture | **Existing foundation** |
| Reaction framework | **DEC-132 remains governing framework** |
| Reaction + AD stacking | **Recommended but still open** |
| Universal reaction frequency limit | **Recommended none; still open** |
| Canonical amendment | **Not authorized** |
| Promotion | **Not performed** |

**END OF REPORT**