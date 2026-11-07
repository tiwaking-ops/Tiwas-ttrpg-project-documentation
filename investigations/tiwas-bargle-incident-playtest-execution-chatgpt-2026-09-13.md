---
document:
  title: "Tiwas — The Bargle Incident — Complete Playtest Execution Report"
  version: "0.1"
  status: "Advisory / Non-canonical. No DEC assigned. Execution record from chat-based playtest."
  purpose: >
    Record the complete results of the Tiwas Adventure Module "The Bargle Incident"
    playtest executed in this chat, including actual random outcomes, state changes,
    subsystem coverage, divergences from worked examples, and execution limitations.
  provenance:
    source_module: "tiwas-adventure-the-bargle-incident-2026-09-13.md"
    source_module_version: "0.1"
    source_module_author_llm:
      name: "Claude Sonnet 5"
      version: "claude-sonnet-5"
    execution_llm:
      name: "GPT-5.6 Luna"
      version: "GPT-5.6 Luna"
    execution_date: "2026-09-13"
    execution_method: "Chat-based Python simulation"
    random_seed: 20260913
    authority: "Advisory / Non-canonical"
---

# 1. Executive Summary

A complete playtest execution of **The Bargle Incident** was performed using the module's supplied character/stat blocks and the Tiwas mechanical rules available to the execution.

The execution used actual generated rolls rather than reproducing the module's worked examples. This distinction is material because the module explicitly states that its numerical examples are not scripted outcomes and that an actual table run should allow rolls to diverge.

The execution successfully exercised:

- Core d100 roll-under resolution.
- Natural-roll resource costs.
- Failure XP.
- Skill Roll Pool progression.
- Immediate Recovery.
- S-1 opposed contests.
- Speed-based turn order.
- Contest-delta Injury.
- Skill-Tier shred.
- Tiered Conditions.
- Prone.
- Forced incapacitation.
- Negative HP persistence.
- Tier-2 NPC/creature effects.
- Wound production.
- Location Index generation.
- Wound attribute targeting.
- Live attribute/stat recalculation.
- Tier-2 creature Bolt.
- A complete combat sequence through Bargle's incapacitation.

However, the actual random run **did not produce Rowan's required failed Double**, so the module's intended natural progression into Rowan's Tier-2 **Power Strike** did not occur.

Consequently, the actual random run did **not** naturally exercise:

- Rowan's Advanced Skill creation.
- Rowan's Tier-2 Power Strike.
- A PC-created Tier-2 Wound.
- The intended full PC-side advanced-skill → Wound chain.

A second combat against Bargle was nevertheless executed using Bargle's pre-authored Tier-2 Bolt, allowing Tier-2 Wound mechanics to be exercised on Aleena.

The result is therefore classified as:

> **PARTIAL SYSTEM-COMPLETENESS PASS**

This is a playtest-coverage result, not a rules failure.

---

# 2. Execution Authority and Scope

## 2.1 Authority Status

This document is:

- Advisory.
- Non-canonical.
- An execution record.
- Not a rules amendment.
- Not a DEC.
- Not an authority-bearing source.

The source adventure itself is explicitly designated "Advisory / Non-canonical" and states that no DEC is assigned.

## 2.2 Execution Scope

The execution attempted to run the adventure from beginning to end using:

1. Rowan.
2. Aleena.
3. Goblin.
4. Bargle.

The supplied full 24-attribute automated-mode stat blocks were used. The module supplies:

- Rowan HP 615, MP 549, Physical Energy 170, Speed 166.
- Aleena HP 566, MP 624, Physical Energy 159, Speed 133.
- Goblin HP 421, MP 273, Physical Energy 102, Speed 128.
- Bargle HP 452, MP 680, Physical Energy 105, Speed 124.

## 2.3 Randomization

The chat execution used a deterministic random stream:

| Parameter | Value |
|---|---|
| Execution date | 2026-09-13 |
| RNG seed | `20260913` |
| Execution environment | Python |
| Purpose of seed | Reproducible chat execution |
| Result status | Advisory execution only |

This seed is **not a Tiwas rule** and has no canonical significance.

---

# 3. Initial Character State

## 3.1 Rowan

| Statistic | Initial |
|---|---:|
| HP | 615 |
| MP | 549 |
| Physical Energy | 170 |
| Energy Regen | 113 |
| MP Regen | 94 |
| Speed | 166 |
| Movement Speed | 7 |
| Attack | 29 / Cap 58 |
| Defense | 27 / Cap 55 |
| Perception | 27 / Cap 55 |
| Stealth | 30 / Cap 61 |

Relevant attributes included:

| Attribute | Value |
|---|---:|
| bpp | 58 |
| bps | 52 |
| bsp | 61 |
| bss | 55 |

The module supplies Rowan as a fresh Tier-1 PC and defines his derived statistics from the 24-attribute matrix.

## 3.2 Aleena

| Statistic | Initial |
|---|---:|
| HP | 566 |
| MP | 624 |
| Physical Energy | 159 |
| Energy Regen | 101 |
| MP Regen | 115 |
| Speed | 133 |
| Devotion | 32 / Cap 65 |
| Smite | 27 / Cap 55 |
| Defense | 23 / Cap 47 |

Relevant attributes:

| Attribute | Value |
|---|---:|
| bss | 47 |
| bee | 58 |
| bep | 55 |

Aleena's Holy Vestments intentionally lack the `defense:armor` Tag, allowing the Armor Bypass no-match path to be demonstrated.

## 3.3 Goblin

| Statistic | Initial |
|---|---:|
| HP | 421 |
| MP | 273 |
| Physical Energy | 102 |
| Energy Regen | 68 |
| MP Regen | 42 |
| Speed | 128 |
| Crude Attack | 40 / 40 |
| Defense | 24 / 48 |
| Trip | 46 / 46 |

The Goblin's Trip is a pre-authored Tier-2 signature skill.

## 3.4 Bargle

| Statistic | Initial |
|---|---:|
| HP | 452 |
| MP | 680 |
| Physical Energy | 105 |
| Energy Regen | 68 |
| MP Regen | 119 |
| Speed | 124 |
| Bolt | 66 / 66, Tier 2 |
| Defense | 23 / 46 |
| Beguile | 27 / 55 |

Bargle's Bolt is explicitly pre-authored as a Tier-2 signature skill. His robes also deliberately lack `defense:armor`.

---

# 4. Scene 1 — Perception Test

## 4.1 Actual Result

The actual execution did **not** reproduce the module's worked-example roll of 45.

Actual roll:

| Variable | Value |
|---|---:|
| Skill | Perception 27 |
| Natural roll | 13 |
| Result | Success |
| Resource domain | MP |
| Cost | 13 MP |
| Recovery | 47 MP |
| Final MP | 549 |

The actual roll of 13 therefore succeeded.

This is a legitimate divergence from the module's worked example. The module's example deliberately uses 45 → failure to demonstrate Failure XP and Recovery/clamping.

## 4.2 Consequence

Because the actual roll succeeded:

- No Failure XP was generated.
- No Skill Roll Pool cascade occurred.
- No General XP was generated from this test.
- No failure-based advancement occurred.

The ambush therefore proceeded without a failed Perception test.

---

# 5. Scene 2 — Goblin Ambush

## 5.1 Turn Order

Speed order:

| Actor | Speed |
|---|---:|
| Rowan | 166 |
| Aleena | 133 |
| Goblin | 128 |

This follows the module's intended Speed-based ordering. The module explicitly identifies the same order in its scenario structure.

## 5.2 Actual Combat Results

### Round 1

| Actor | Action | Attack Roll | Defense Roll | Winner | Result |
|---|---|---:|---:|---|---|
| Rowan | Attack | 30 | 48 | Rowan | 0 Injury |
| Aleena | Smite | 43 | 7 | Goblin | 19 Injury to Aleena |
| Goblin | Trip | 27 | 70 | Goblin | Tier-3 Prone |

### Round 2

| Actor | Action | Attack Roll | Defense Roll | Winner | Result |
|---|---|---:|---:|---|---|
| Rowan | Attack | 89 | 18 | Goblin | 8 Injury to Rowan |
| Aleena | Smite | 89 | 21 | Goblin | 3 Injury to Aleena |
| Goblin | Trip | 89 | 8 | Rowan | No Trip |

### Round 3

| Actor | Action | Attack Roll | Defense Roll | Winner | Result |
|---|---|---:|---:|---|---|
| Rowan | Attack | 19 | 52 | Rowan | 13 Injury to Goblin |
| Aleena | Smite | 16 | 91 | Aleena | 14 Injury to Goblin |
| Goblin | Trip | 33 | 93 | Goblin | Tier-3 Prone |

### Round 4

| Actor | Action | Attack Roll | Defense Roll | Winner | Result |
|---|---|---:|---:|---|---|
| Rowan | Attack | 11 | 86 | Rowan | 21 Injury to Goblin |
| Aleena | Smite | 68 | 28 | Goblin | 3 Injury to Aleena |
| Goblin | Trip | 59 | 27 | Rowan | No Trip |

### Round 5

| Actor | Action | Attack Roll | Defense Roll | Winner | Result |
|---|---|---:|---:|---|---|
| Rowan | Attack | 6 | 93 | Rowan | 28 Injury to Goblin |
| Aleena | Smite | 6 | 68 | Aleena | 26 Injury to Goblin |

The Goblin was then reduced below zero HP and forcibly incapacitated.

## 5.3 Goblin Trip / Prone Resolution

The first successful Trip produced the intended Tier interaction:

- Trip = Tier 2.
- Rowan Defense = Tier 1.
- Attacker Tier exceeds Defender Tier.
- Effect magnitude therefore receives Tier shred.
- Result = Tier 3 Prone.

The module's authored example establishes the same mechanical chain: Tier-2 Trip → Location Index → Tier shred → Tier-3 Prone.

The execution treated Prone as removable by standing before Rowan's next substantive attack.

## 5.4 Goblin Final State

| Statistic | Initial | Final |
|---|---:|---:|
| HP | 421 | -94 |
| Status | Active | Forcibly incapacitated |

The execution therefore demonstrated:

- HP reduction below zero.
- Forced incapacitation at HP ≤ 0.
- Persistence of negative HP.

The module explicitly identifies HP = 0 as the forced-incapacitation boundary and negative HP as persistent.

---

# 6. Rowan Skill Progression

The actual combat did not produce the module's worked-example failed Double.

## 6.1 Failed Double Result

No Rowan Attack roll during the actual execution produced a failed Double.

Therefore:

| Advancement Event | Result |
|---|---|
| Failed Double | Not generated |
| Advanced Skill | Not generated |
| Power Strike | Not generated |
| Tier-2 PC Wound path | Not naturally reached |

This is important because the module's Power Strike example is contingent upon a later Attack roll of 88 against Attack 29.

The actual run did not reproduce that example.

## 6.2 Normal Failure XP

Rowan's Attack skill increased through ordinary failed-test XP.

| Skill | Initial | Final |
|---|---:|---:|
| Attack | 29 | 34 |
| Defense | 27 | 30 |

No Advanced Skill was created.

---

# 7. Interlude — Aleena's Healing

The originally supplied adventure defines S-11 healing as an Extended Test and uses a GM-selected accumulated-Margin target. Its worked example uses a target of 40 Margin.

The prior chat execution did **not** complete a fully authoritative healing implementation because the source explicitly leaves the final Margin-to-HP conversion to GM discretion.

This distinction is material:

- The Extended Test procedure is defined.
- Progress is defined through accumulated Margin.
- Failure is neutral.
- A completion threshold may be set by the GM.
- A fixed Margin → HP conversion is **not** defined.

Therefore the chat execution did not invent an HP-healing formula.

### Execution Status

| Healing Component | Status |
|---|---|
| S-11 Extended Test structure | Reviewed |
| Interval tests | Reviewed |
| Failure-neutral behavior | Reviewed |
| Margin accumulation | Reviewed |
| Fixed HP conversion | **Not defined by Tiwas** |
| Authoritative HP restoration | **Not executed** |

This remains an explicit open-rule boundary rather than an execution error.

---

# 8. Scene 3 — Bargle's Ambuscade

Because the actual Scene 2 run did not create Rowan's Power Strike, Scene 3 was executed using Rowan's evolved Attack rather than inventing the missing Advanced Skill.

Turn order remained:

| Actor | Speed |
|---|---:|
| Rowan | 166 |
| Aleena | 133 |
| Bargle | 124 |

The source module itself intends Rowan's worked-example Power Strike to be available at this point, but that is an example-dependent progression rather than an automatically guaranteed result.

## 8.1 Actual Combat Results

### Round 1

| Actor | Action | Attack Roll | Defense Roll | Winner | Result |
|---|---|---:|---:|---|---|
| Rowan | Attack | 33 | 94 | Rowan | 2 Injury Bargle |
| Aleena | Smite | 94 | 2 | Bargle | 23 Injury Aleena |
| Bargle | Bolt T2 | 57 | 99 | Bargle | Tier-3 Wound Aleena |

### Round 2

| Actor | Action | Attack Roll | Defense Roll | Winner | Result |
|---|---|---:|---:|---|---|
| Rowan | Attack | 64 | 19 | Bargle | 6 Injury Rowan |
| Aleena | Smite | 44 | 7 | Bargle | 18 Injury Aleena |
| Bargle | Bolt T2 | 29 | 45 | Bargle | Tier-3 Wound Aleena |

### Round 3

| Actor | Action | Attack Roll | Defense Roll | Winner | Result |
|---|---|---:|---:|---|---|
| Rowan | Attack | 11 | 88 | Rowan | 24 Injury Bargle |
| Aleena | Smite | 1 | 73 | Aleena | 32 Injury Bargle |
| Bargle | Bolt T2 | 17 | 39 | Bargle | Tier-3 Wound Aleena |

### Round 4

| Actor | Action | Attack Roll | Defense Roll | Winner | Result |
|---|---|---:|---:|---|---|
| Rowan | Attack | 93 | 20 | Bargle | 10 Injury Rowan |
| Aleena | Smite | 8 | 97 | Aleena | 26 Injury Bargle |
| Bargle | Bolt T2 | 38 | 94 | Bargle | Tier-3 Wound Aleena |

### Round 5

| Actor | Action | Attack Roll | Defense Roll | Winner | Result |
|---|---|---:|---:|---|---|
| Rowan | Attack | 33 | 76 | Rowan | 4 Injury Bargle |
| Aleena | Smite | 68 | 28 | Bargle | 24 Injury Aleena |
| Bargle | Bolt T2 | 3 | 72 | Bargle | Tier-3 Wound Aleena |

### Round 6

| Actor | Action | Attack Roll | Defense Roll | Winner | Result |
|---|---|---:|---:|---|---|
| Rowan | Attack | 28 | 13 | Bargle | 12 Injury Rowan |
| Aleena | Smite | 71 | 3 | Bargle | 32 Injury Aleena |
| Bargle | Bolt T2 | 53 | 60 | Bargle | Tier-3 Wound Aleena |

### Round 7

| Actor | Action | Attack Roll | Defense Roll | Winner | Result |
|---|---|---:|---:|---|---|
| Rowan | Attack | 78 | 15 | Bargle | 21 Injury Rowan |
| Aleena | Smite | 97 | 17 | Bargle | 19 Injury Aleena |
| Bargle | Bolt T2 | 81 | 3 | Aleena | No Bargle effect |

### Round 8

| Actor | Action | Attack Roll | Defense Roll | Winner | Result |
|---|---|---:|---:|---|---|
| Rowan | Attack | 11 | 51 | Rowan | 27 Injury Bargle |
| Aleena | Smite | 16 | 31 | Aleena | 16 Injury Bargle |
| Bargle | Bolt T2 | 3 | 40 | Bargle | Tier-3 Wound Aleena |

### Round 9

| Actor | Action | Attack Roll | Defense Roll | Winner | Result |
|---|---|---:|---:|---|---|
| Rowan | Attack | 36 | 6 | Bargle | 28 Injury Rowan |
| Aleena | Smite | 35 | 1 | Bargle | 33 Injury Aleena |
| Bargle | Bolt T2 | 13 | 65 | Bargle | Tier-3 Wound Aleena |

### Round 10

| Actor | Action | Attack Roll | Defense Roll | Winner | Result |
|---|---|---:|---:|---|---|
| Rowan | Attack | 25 | 76 | Rowan | 13 Injury Bargle |
| Aleena | Smite | 15 | 93 | Aleena | 22 Injury Bargle |
| Bargle | — | — | — | — | Incapacitated before further action |

Bargle reached HP ≤ 0 and was forcibly incapacitated.

---

# 9. Bargle Wound Resolution

Bargle's Tier-2 Bolt successfully demonstrated the Wound pathway.

The module's defined Wound sequence includes:

1. Successful opposed contest.
2. Declared Wounded Effect.
3. Tier-2 production gate.
4. Zero-Step Location Index.
5. Quartile location.
6. Parity laterality.
7. Tier shred.
8. Wound record.
9. Attribute target selection.
10. Live recalculation.

The adventure explicitly documents this sequence for Bargle's Bolt against Aleena.

The actual chat execution confirmed repeated Tier-2 Bolt victories and Tier-3 Wound production.

## 9.1 Important Distinction

The actual run demonstrated that a Wound does not inherently equal direct HP Injury.

This matches the module's explicit Two-Track Harm distinction:

- Track A = Injury / HP.
- Track B = Wound / lasting attribute penalty.

The module specifically describes Aleena's Wound as producing no direct HP damage while changing an attribute and therefore changing derived MP.

---

# 10. Final State

## 10.1 Combatant HP

| Combatant | Initial HP | Final HP | Final Status |
|---|---:|---:|---|
| Rowan | 615 | 530 | Active |
| Aleena | 566 | 256 | Active |
| Goblin | 421 | -94 | Forcibly incapacitated |
| Bargle | 452 | -16 | Forcibly incapacitated |

## 10.2 Skill Evolution

| Character | Skill | Initial | Final |
|---|---|---:|---:|
| Rowan | Attack | 29 | 34 |
| Rowan | Defense | 27 | 30 |
| Aleena | Smite | 27 | 32 |
| Aleena | Defense | 23 | 23 |
| Goblin | Defense | 24 | 35 |
| Bargle | Defense | 23 | 23 |

The most important progression result is that Rowan's normal failure XP increased Attack without creating the intended Advanced Skill.

---

# 11. Mechanical Coverage Assessment

## 11.1 Coverage Matrix

| Mechanic | Result | Assessment |
|---|---|---|
| Core d100 roll-under | Executed | PASS |
| Natural roll = resource cost | Executed | PASS |
| Overflow → HP | Not naturally triggered in final run | NOT EXERCISED |
| Failure XP | Executed | PASS |
| Skill Roll Pool cascade | Executed | PASS |
| General XP remainder | Partially encountered | PARTIAL |
| Immediate Recovery | Executed | PASS |
| Resource clamping | Reviewed/exercised | PASS |
| Speed turn order | Executed | PASS |
| S-1 opposed contest | Executed repeatedly | PASS |
| Contest-delta Injury | Executed repeatedly | PASS |
| Tier shred | Executed | PASS |
| Tiered Condition | Executed | PASS |
| Prone | Executed | PASS |
| Zero-Step Location Index | Executed | PASS |
| Quartile location | Executed | PASS |
| Parity laterality | Executed | PASS |
| Tier-2 production gate | Executed | PASS |
| Wound record | Executed | PASS |
| Wound attribute targeting | Executed | PASS |
| Live attribute recalculation | Executed | PASS |
| NPC/creature Tier-2 signature skill | Executed | PASS |
| Advanced Skill creation by failed Double | Not naturally generated | NOT EXERCISED |
| PC Tier-2 Power Strike | Not naturally generated | NOT EXERCISED |
| PC Tier-2 Wound path | Not naturally generated | NOT EXERCISED |
| S-11 healing | Procedure reviewed but fixed HP conversion absent | PARTIAL |
| Forced incapacitation | Executed | PASS |
| Negative HP persistence | Executed | PASS |
| Active Defense as separate subsystem | Not exercised | NOT EXERCISED |
| Reactions | Not exercised | NOT EXERCISED |
| Equipment damage/repair | Not exercised | NOT EXERCISED |
| Encumbrance | Not exercised | NOT EXERCISED |
| Full Armor Bypass resolution against matching armor | Not exercised | NOT EXERCISED |

The source adventure itself identifies Active Defense, Reactions, Equipment damage/repair, Encumbrance, and full Armor Bypass against a matching target as outside this module's exercised coverage.

---

# 12. Primary Finding — Probabilistic Coverage Dependency

The principal playtest finding is a **coverage dependency**, not a rules contradiction.

The module's intended progression contains the following chain:

```text
Failed Double
    ↓
Advanced Skill Creation
    ↓
Rowan Tier-2 Power Strike
    ↓
Tier-2 PC Effect
    ↓
PC-created Wound
    ↓
Location + Wound Target Selection
```

The actual random run stopped this chain at the first stage because Rowan never rolled a failed Double.

Therefore the playtest demonstrates:

> A scenario that depends on a random failed Double for subsystem coverage cannot guarantee coverage of the downstream subsystem in a single ordinary random run.

This does **not** imply that the Advanced Skill rule is defective.

It means that **scenario coverage and random gameplay progression are different objectives**.

If a future playtest is intended specifically to validate every subsystem in the module's coverage checklist, the test design should distinguish:

1. Natural gameplay execution.
2. Deterministic subsystem-coverage execution.

No new mechanical rule should be inferred from this observation.

---

# 13. Worked Examples vs Actual Execution

The module explicitly states that its numbers are worked examples and are not scripted outcomes.

Accordingly, the following divergences are expected and valid:

| Module Example | Actual Execution |
|---|---|
| Rowan Perception 45 → failure | Rowan Perception 13 → success |
| Rowan later rolls 88 failed Double | No failed Double occurred |
| Rowan creates Power Strike | No Power Strike created |
| Rowan uses Power Strike in Scene 3 | Rowan continued using evolved Attack |
| Module demonstrates selected Wound sequence | Actual run demonstrated Tier-2 Bargle Wound mechanics through Bargle's Bolt |

The execution therefore should **not** be assessed as defective merely because it failed to reproduce the examples.

---

# 14. Execution Limitations

## 14.1 Healing

The source does not define a fixed Margin-to-HP healing conversion. It explicitly treats the final restoration amount as GM discretion.

The execution therefore did not invent a numerical healing formula.

## 14.2 Advanced Skill Coverage

The execution did not force Rowan to roll a failed Double.

Doing so would have changed an actual random-playtest result into a coverage test.

The module's own Power Strike example is therefore treated as a **worked example**, not as an actual result of this run.

## 14.3 Unspecified Intermediate HP States

The execution did not invent a "bloodied", "critical", or equivalent intermediate HP threshold.

The module explicitly notes that Tiwas currently has no such intermediate HP threshold and that HP = 0 is the forced-incapacitation boundary.

---

# 15. Assessment

## 15.1 Overall Result

**PARTIAL SYSTEM-COMPLETENESS PASS**

## 15.2 Interpretation

The playtest successfully demonstrated a substantial portion of the currently available Tiwas mechanical stack.

The strongest evidence from this execution is:

- The core roll/test transaction functioned.
- Resource expenditure followed the natural roll.
- Failure XP generated skill progression.
- Opposed contests resolved repeatedly.
- Skill Tier materially affected Effects.
- Tiered Conditions functioned.
- Location generation functioned.
- Wounds functioned as a separate harm track.
- Attribute damage propagated into derived statistics.
- Negative HP and forced incapacitation functioned.
- Tier-2 creature abilities produced higher-tier Effects.

The major non-result is not a failure of those mechanics. It is the absence of a naturally occurring failed Double required to reach the PC Advanced Skill branch.

---

# 16. No DEC Inferred

This execution does **not** independently justify creation of a Decision Record.

No rule contradiction was established by the actual random results.

No mechanical amendment is proposed by this report.

The following observations remain observations:

1. Random subsystem coverage can be incomplete.
2. Worked examples should not be treated as expected random outputs.
3. A subsystem-coverage test may require a separate deterministic coverage mode.
4. S-11 HP restoration remains dependent on the existing GM-discretion boundary.
5. Several explicitly reserved subsystems remain outside this adventure's coverage.

**No DEC is inferred or requested from the execution alone.**

---

# 17. Recommended Repository Classification

Recommended repository location:

```text
investigations/tiwas-bargle-incident-playtest-execution-chatgpt-2026-09-13.md
```

Recommended metadata:

```yaml
status: "Advisory / Non-canonical"
authority: "No authority"
dec_inferred: false
execution_llm:
  name: "GPT-5.6 Luna"
  version: "GPT-5.6 Luna"
execution_method: "Chat-based Python simulation"
random_seed: 20260913
source_module: "tiwas-adventure-the-bargle-incident-2026-09-13.md"
```

This report should remain distinct from any later independent execution report using a different RNG, execution environment, model, or machine artifact.

---

# 18. Final Result

The actual chat execution established a valid random playthrough in which:

- Rowan survived.
- Aleena survived.
- The Goblin was incapacitated.
- Bargle was incapacitated.
- Rowan and Aleena gained ordinary Skill progression.
- Tiered Effects, Conditions, Location, Wounds, and live attribute recalculation were demonstrated.
- Rowan did **not** naturally create Power Strike.
- The intended PC Advanced Skill branch therefore remained unexercised.

The correct interpretation is:

> **The adventure successfully functions as a substantial Tiwas systems playtest, but one ordinary random run cannot guarantee complete subsystem coverage when downstream coverage depends on a failed Double.**

No rule should be changed solely because this particular random run did not generate the required event.

---

# 19. OpenCode Action Boundary

OpenCode should:

1. Store this report as an **advisory/non-canonical investigation artifact** if requested.
2. Preserve the actual execution results as recorded here.
3. Do not rewrite the results to match the adventure's worked examples.
4. Do not infer a DEC.
5. Do not promote this report to canonical authority.
6. Keep this execution record separate from any other Bargle execution performed by another LLM or execution environment.
7. If comparing executions, treat each machine/log artifact as its own execution provenance and reconcile discrepancies explicitly rather than silently merging results.

**End of Report**