---
provenance:
  author_llm: {name: "GPT-5.6 Luna", version: "GPT-5.6 Luna"}
  assessor_llm: []
  last_modified_by_llm: {name: "GPT-5.6 Luna", version: "GPT-5.6 Luna"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
rng_method: "Python secrets.SystemRandom() using OS entropy"
computation_method: "Python-computed arithmetic and state tracking"
engine_runtime: "Not captured during execution; exact wall-clock duration cannot be reconstructed without inventing a value"
---

# Tiwas TTRPG — Ice Troll Combat Playtest v4
## Comprehensive Playtest Report

## 1. Purpose / Scope

This report documents the execution of:

`tiwas-ice-troll-combat-playtest-prompt-v4-2026-09-04.md`

Version 4 was created following the v3 Cross-Report Synthesis and was specifically intended to determine whether the newly ruled combat procedures could resolve deterministically without further unauthorised invention. The v4 prompt explicitly targeted:

| Target | Governing ruling / status |
|---|---|
| Combat sequencing | DEC-095 |
| Winner's Margin injury magnitude | DEC-096 |
| Active Defense mitigation | DEC-097 |
| Creature default defensive Skill | DEC-098 |
| Quality thresholds | DEC-099 |
| Location quartile mapping | DEC-100 |
| Defender-wins behaviour | DEC-101 |
| Passive Frightened | DEC-094 |
| Location/Wound exercise | Mandatory v4 test requirement |
| Attack selection | Explicit non-canonical scaffold |
| Quality → Wound Tier | Explicit non-canonical scaffold |
| HP floor | Explicit non-canonical test convention |

The v4 prompt also requires a genuine GM stop rather than invention when an unresolved subjective/procedural mechanic is encountered.

### Execution Result

**Status: ABORTED**

The combat reached the mandatory Location/Wound pathway, but execution could not continue because the supplied executable corpus did not deterministically specify:

1. which Attribute or Skill the resulting Wound targets; and
2. how Active Defense's Defender's Margin modifies a Wound Tier/magnitude.

Continuing would therefore have required inventing mechanics.

---

# 2. Character & Opponent Summary

## 2.1 Adventurer-1

All 24 Attributes were fixed at 50.

| Statistic | Value |
|---|---:|
| HP | 600 |
| MP | 600 |
| Physical Energy | 150 |
| Speed | 150 |
| Energy Regen | 100 |
| MP Regen | 100 |
| Movement Speed | 6 |
| Tier-1 Skills | 25 |
| Attack2 | 25 |
| Defence2 | 25 at combat start |
| Attack2 Cap | 50 |
| Defence2 Cap | 50 |

The v4 prompt explicitly uses `Attack2` and `Defence2` as the pre-built Tier-2 skills for this test.

### DEC-012 Exception Provenance

> **Provenance of the DEC-012 exception:** the two pre-built Tier-2 skills on Adventurer-1 (Attack2, Defence2) were granted under a **prompt-level scaffold** (Tiwa's authorization, 2026-09-04) for this playtest only. They are **NOT backed by a PC-scoped register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates and preserves DEC-012's failed-Double origin for player-character skill advancement generally. Therefore: this exception is **non-register-backed**, creates **no new precedent**, grants the PC **no canonical authority** from these skills, and must **not** be cited in any future DEC or proposal as evidence that PCs can receive pre-authored Tier-2 skills outside DEC-012.

---

## 2.2 Ice Troll

The supplied v4 stat block gives the following values.

| Statistic | Value |
|---|---:|
| HP | 705 |
| MP | 420 |
| Physical Energy | 220 |
| Speed | 175 |
| Energy Regen | 140 |
| MP Regen | 75 |
| Movement Speed | 7 |
| Icy Claws | 67 |
| Sharktoothed Maw | 75 |
| Brawling | 37 |
| Camouflage | 30 |
| Stealth | 30 |
| Tracking | 30 |

### Defensive Skill

The Ice Troll has no dedicated authored defensive Skill. DEC-098 therefore specifies Brawling as its default defensive Skill:

**Brawling = 37.**

This did not become necessary during the actual execution because the combat stopped before the PC attacked.

---

# 3. Pre-Combat State

## 3.1 RNG and Computation

The execution disclosed:

- **RNG:** Python `secrets.SystemRandom()` using OS entropy.
- **Arithmetic/state tracking:** Python-computed.
- No LLM-generated pseudo-random values were used.

This satisfies the v4 requirement that RNG and computation methodology be disclosed before execution.

## 3.2 Frightened Scene State

The v4 prompt declares the Ice Troll's `Appearance: Hideous` as an active fear-source binding.

Therefore, from combat start:

| Condition | Value | Source |
|---|---:|---|
| Frightened | Tier-1, −1 to all Skills | DEC-094 scene-state binding |

No roll or resource transaction is required for this passive application. The v4 prompt explicitly distinguishes this scene-state pathway from a Frightened Effect produced by a won S-1 contest.

---

# 4. Rulings Applied

| DEC | Intended application | Result in this execution |
|---|---|---|
| DEC-094 | Passive Frightened | **Exercised successfully** |
| DEC-095 | Highest-Speed-first sequencing | **Exercised successfully** |
| DEC-096 | Winner's Margin as Injury magnitude | **Not exercised** |
| DEC-097 | Active Defense mitigation by Defender's Margin | **Not deterministically completed; exposed gap** |
| DEC-098 | Troll defensive Skill = Brawling | **Not exercised** |
| DEC-099 | Quality ≥1 / ≥10 gating | **Exercised successfully** |
| DEC-100 | Location quartile split | **Exercised successfully** |
| DEC-101 | Defender wins → no counter-Effect | **Not exercised** |

### Observed sequencing

The Speed values were:

- Ice Troll: **175**
- Adventurer-1: **150**

Therefore the Ice Troll acted first.

This conforms to the v4 specification that the highest current Speed acts first and that one substantive combat action constitutes one S-1 exchange.

---

# 5. Scaffold Values Used

The following were used strictly as non-canonical, test-only scaffolds.

## 5.1 Attack Selection

The v4 prompt explicitly pre-authorises:

| Round | Attack |
|---|---|
| Odd rounds | Icy Claws |
| Even rounds | Sharktoothed Maw |

Round 1 therefore used Icy Claws.

This remains an open system issue and is not a creature-AI rule.

**Status:** Used.

---

## 5.2 Quality → Wound Tier

The v4 test scaffold specifies:

| Quality | Wound Tier |
|---:|---:|
| 1–9 | Tier 1 |
| 10–19 | Tier 2 |
| 20–29 | Tier 3 |
| 30+ | Tier 4 |

The actual winning Quality was 30.

Therefore:

**Quality 30 → Wound Tier 4.**

This table is explicitly non-canonical and was introduced solely to make the test executable.

**Status:** Used.

---

## 5.3 HP Floor Convention

The v4 prompt specifies that HP reaching zero or below is recorded as zero while preserving the raw pre-clamp value.

**Status:** Not exercised.

---

## 5.4 DEC-012 Exception

The pre-built PC Tier-2 skills were used as expressly authorised for this test.

**Status:** Used.

They remain non-register-backed and create no precedent.

---

# 6. Live Combat Log

## 6.1 Round 1 — Turn Order

| Combatant | Speed | Order |
|---|---:|---:|
| Ice Troll | 175 | 1 |
| Adventurer-1 | 150 | 2 |

### Scaffold declaration

> **SCAFFOLD: Attack selection.** SC-XX remains open. The Ice Troll's attack alternation pattern (Icy Claws odd / Sharktoothed Maw even) is a **prompt-level scaffold** for this test only. It is not a rule, not a precedent, and not a creature AI.

---

## 6.2 Core Test 1 — Troll Attack

| Field | Result |
|---|---|
| Round | 1 |
| Turn | Troll |
| Step | Attack |
| Actor | Ice Troll |
| Skill Used | Icy Claws 67 |
| d100 Roll | **37** |
| Success/Fail | **Success** |
| Margin | **30** |
| Quality | **30** |
| Cost | **37 PE** |
| PE Before | 220 |
| PE After Cost | 183 |
| Overflow | 0 |
| HP Overflow Damage | 0 |
| Recovery | 70 |
| PE Final | 220 |
| Effect Selected | Gated/Wound pathway |
| Location Index | **32** |
| Location Zone | **Torso** |
| Wound Tier | **4** |
| Condition Applied | None at this step |
| Active Defense | Triggered by exchange, but subsequent resolution became blocked |
| Net HP Change | Not resolved |

### Calculations

**Margin:**

`67 − 37 = 30`

**Quality:**

`30`

**Resource cost:**

`37`

**Recovery:**

`floor(140 / 2) = 70`

**PE path:**

`220 → 183 → 220`

No Overflow occurred.

### Quality gate

Quality 30 satisfies the gated threshold.

The v4 scaffold therefore maps Quality 30 to Wound Tier 4.

### Location

Location Index roll:

`32`

Quartile mapping:

`26–50 → Torso`

Therefore:

**Location = Torso.**

The v4 prompt requires this Location/Wound pathway to be exercised at least once.

---

## 6.3 Core Test 2 — Adventurer-1 Defence

The PC's Defence2 base value was 25.

The active Frightened condition applies −1 to all Skills.

Therefore:

`25 − 1 = 24`

Effective Defence2:

**24**

| Field | Result |
|---|---|
| Round | 1 |
| Turn | Troll exchange |
| Step | Defense |
| Actor | Adventurer-1 |
| Skill Used | Defence2 24 effective |
| d100 Roll | **73** |
| Success/Fail | **Failure** |
| Margin | 0 |
| Quality | 0 |
| Cost | **73 PE** |
| PE Before | 150 |
| PE After Cost | 77 |
| Overflow | 0 |
| HP Overflow Damage | 0 |
| Recovery | 50 |
| PE Final | 127 |
| Effect Selected | None |
| Location Index | N/A |
| Location Zone | N/A |
| Wound Tier | N/A |
| Condition Applied | Frightened already active from scene-state binding |
| Active Defense | Defender failed |
| Net HP Change | Blocked before consequence resolution |

### Failure XP

`73 − 24 = 49 XP`

The 49 XP was applied immediately to Defence2.

The first increase costs the current value:

`25 XP`

Remaining XP:

`49 − 25 = 24`

The next increase would require 26 XP.

Therefore only one increase could be purchased.

Post-test Defence2:

**26**

The remaining 24 XP did not purchase the next level.

### PE path

`150 → 77 → 127`

No Overflow occurred.

---

# 7. Wound Pathway Failure / GM Stop

At this point the combat had established:

1. Troll won the S-1 contest.
2. Quality = 30.
3. Quality ≥ 10.
4. Winning Skill was Tier-2.
5. Location Index was required.
6. Location Index = 32.
7. Location = Torso.
8. Test scaffold maps Quality 30 to Wound Tier 4.

However, the executable corpus did not provide a deterministic answer to two subsequent questions:

### Gap A — Wound Target

It did not specify which Attribute or Skill is reduced/affected by the Tier-4 Wound at the Torso location.

### Gap B — Active Defense vs Wound

It did not provide a deterministic conversion from the Defender's Margin/Active Defense result into a modification of the Wound Tier or Wound magnitude.

The v4 specification requires stopping rather than inventing such a procedure.

### Verbatim GM Stop

> **GM REQUIRED STOP:** The Troll has won with Quality 30, triggering Location Index 32 → Torso → Wound Tier 4. The executable corpus does not specify which Attribute or Skill the Wound targets, nor how Active Defense's Defender's Margin modifies a Wound Tier/magnitude. Continuing would require inventing a mechanic. Await Tiwa's ruling.

**Reason:** Genuine unresolved mechanical/procedural gap. No authorised numeric scaffold existed for either decision.

---

# 8. Systems Confirmed Working

## 8.1 Combat Sequencing

**Result: Confirmed for exercised case.**

The system correctly selected the Troll first because:

`175 > 150`

The execution therefore demonstrated that Speed-based sequencing is mechanically usable for this case.

---

## 8.2 Passive Frightened

**Result: Confirmed for exercised case.**

The scene-state binding applied:

`−1 to all Adventurer-1 Skills`

This directly affected Defence2:

`25 → 24 effective`

No additional roll or resource transaction was introduced.

---

## 8.3 Core d100 Resolution

**Result: Confirmed.**

Troll:

`37 ≤ 67 → success`

PC:

`73 > 24 → failure`

Both results were mechanically unambiguous.

---

## 8.4 Resource Cost = Roll

**Result: Confirmed.**

Troll:

`220 − 37 = 183`

PC:

`150 − 73 = 77`

No Overflow occurred.

---

## 8.5 Immediate Recovery

**Result: Confirmed.**

Troll:

`floor(140 / 2) = 70`

`183 + 70 = 253`, capped at 220:

`220`

PC:

`floor(100 / 2) = 50`

`77 + 50 = 127`

The PE paths were therefore:

| Combatant | Path |
|---|---|
| Troll | 220 → 183 → 220 |
| PC | 150 → 77 → 127 |

---

## 8.6 Failure XP

**Result: Confirmed.**

PC Defence2:

`73 − 24 = 49 XP`

One level was purchased:

`49 − 25 = 24 remainder`

Defence2:

`25 → 26`

This demonstrates the failure-XP cascade for the exercised case.

---

## 8.7 Quality Threshold

**Result: Confirmed for the exercised boundary.**

The Troll produced:

`Quality = 30`

This clearly exceeded the gated threshold of 10.

The resulting Wound pathway therefore activated.

---

## 8.8 Location Quartile Mapping

**Result: Confirmed for the exercised value.**

Location Index:

`32`

Quartile:

`26–50`

Result:

**Torso**

This exercised the required Location pathway.

---

# 9. Systems That Failed / Remained Gapped

## 9.1 Wound Target Selection

**Status: Open / blocking.**

The playtest could determine:

`Quality → Wound Tier → Location`

but could not determine:

`Location + Wound Tier → affected Attribute/Skill`

No deterministic target-selection rule was available.

---

## 9.2 Active Defense Mitigation of Wounds

**Status: Open / blocking.**

The test could invoke the defensive contest, but the executable corpus did not provide the required transformation:

`Defender's Margin → Wound consequence modification`

The v3 synthesis had specifically identified Active Defense mitigation as an area requiring operational validation. The v4 prompt was intended to test it, but this run demonstrates that the Wound branch still does not fully close the chain.

---

## 9.3 Combat Completion

**Status: Failed test objective.**

The v4 success criterion required combat to reach:

- incapacitation, or
- an explicit abort.

The second condition occurred.

Therefore the execution is valid as an **aborted diagnostic playtest**, but it does not constitute a successful end-to-end combat validation.

---

# 10. Edge Cases Observed

| Edge Case | Observed? | Result |
|---|---|---|
| Frightened modifies defensive Skill | Yes | Effective Defence2 = 24 |
| High resource-cost roll | Yes | PC cost = 73 |
| Failure XP cascade | Yes | 49 XP → +1 Defence2 |
| PE recovery after test | Yes | Correctly applied |
| PE Overflow | No | Not exercised |
| Margin 0 | No | Not exercised as a successful roll |
| Advanced Skill creation | No | Not exercised |
| Defender wins / no counter-Effect | No | Not exercised |
| HP reaches 0 | No | Not exercised |
| HP floor convention | No | Not exercised |
| Location Index | Yes | 32 → Torso |
| Wound Tier scaffold | Yes | Quality 30 → Tier 4 |
| Wound target selection gap | Yes | Forced GM stop |
| Active Defense/Wound interaction gap | Yes | Forced GM stop |

---

# 11. Coverage Matrix

| System / Pathway | Exercised | Deterministically completed |
|---|---:|---:|
| Speed initiative | Yes | Yes |
| One combat turn | Yes | Yes |
| Troll attack | Yes | Yes |
| PC defence | Yes | Yes |
| Passive Frightened | Yes | Yes |
| d100 success/failure | Yes | Yes |
| Margin calculation | Yes | Yes |
| Quality calculation | Yes | Yes |
| PE cost | Yes | Yes |
| PE recovery | Yes | Yes |
| Overflow | No | N/A |
| Failure XP | Yes | Yes |
| XP cascade | Yes | Yes |
| Gated Quality threshold | Yes | Yes |
| Location Index | Yes | Yes |
| Location quartile | Yes | Yes |
| Wound Tier | Yes | Scaffold only |
| Wound target selection | Yes | **No** |
| Active Defense mitigation | Partially reached | **No** |
| Winner's Margin Injury | No | N/A |
| Defender-wins branch | No | N/A |
| Advanced Skill creation | No | N/A |
| HP floor | No | N/A |
| Incapacitation | No | N/A |
| Full combat conclusion | No | **No — aborted** |

---

# 12. Total Core Tests

## 12.1 Count

**Total Core Tests executed: 2**

| Core Test | Actor | Step | Roll | Result |
|---:|---|---|---:|---|
| 1 | Ice Troll | Attack | 37 | Success |
| 2 | Adventurer-1 | Defense | 73 | Failure |

The Location Index roll of 32 was a subsidiary location resolution and is **not counted as a separate Core Test**.

## 12.2 Repeat Count

**Repeats: 0**

No repeat occurred.

---

# 13. Duration

## 13.1 Round Count

| Measure | Result |
|---|---:|
| Rounds started | 1 |
| Complete rounds | 0 |
| Combat status | Aborted during Round 1 |

The PC never reached its normal independent combat turn because the Troll's exchange could not be completed.

## 13.2 Real-Time Duration

**Not captured.**

The v4 prompt requires actual wall-clock runtime. No reliable timestamp pair was recorded during execution, and therefore no duration is supplied here.

A fabricated runtime would violate the audit/provenance requirement.

---

# 14. GM-Required Moments

## GM Stop 001

> **GM REQUIRED STOP:** The Troll has won with Quality 30, triggering Location Index 32 → Torso → Wound Tier 4. The executable corpus does not specify which Attribute or Skill the Wound targets, nor how Active Defense's Defender's Margin modifies a Wound Tier/magnitude. Continuing would require inventing a mechanic. Await Tiwa's ruling.

### Trigger

- Troll won.
- Quality = 30.
- Tier-2 attack.
- Wound pathway triggered.
- Location = Torso.
- Wound Tier = 4 under test-only scaffold.

### Blocking questions

| Question | Current state |
|---|---|
| What does a Torso Wound Tier 4 mechanically target? | Unspecified |
| How does Defender's Margin modify Wound Tier/magnitude? | Unspecified |

No further combat action was taken.

---

# 15. Comparison Against the v3 Cross-Report

The v4 prompt was explicitly constructed in response to the three-way v3 comparison between Claude Sonnet 5, GPT-5.6 Luna and Grok 4.5. It added explicit scaffolds for attack selection, Quality → Wound Tier, HP flooring, mandatory Location/Wound exercise, PE-path logging, RNG disclosure, Core Test counting, runtime reporting and structured data.

## 15.1 v3 Problems Addressed by v4

| v3 finding | v4 response | Result |
|---|---|---|
| Silent attack-selection invention | Explicit scaffold | **Resolved for test governance** |
| Inconsistent Wound Tier assumptions | Numeric scaffold | **Resolved for test execution** |
| Inconsistent HP floor | Explicit convention | Not exercised |
| Location/Wound often not exercised | Mandatory exercise | **Successfully exercised** |
| PE tracking inconsistent | Mandatory path columns | **Implemented** |
| RNG provenance absent | Mandatory disclosure | **Implemented** |
| Core Test counts absent | Mandatory count | **Implemented** |
| Repeat logging underspecified | Explicit repeat rows | No repeat occurred |
| Edge-case reporting absent | Explicit section | **Implemented** |
| Runtime absent | Mandatory field | **Could not be populated because runtime was not captured** |
| Structured raw data absent | Required JSON | **Produced conceptually from execution state** |

---

# 16. v3 Gaps That Remain

The most important result is that the v4 scaffolds successfully carried the test farther into the Wound pathway than the earlier runs, but they also exposed a deeper unresolved dependency.

The execution reached:

`Attack → Defence → Win → Quality → Gated Effect → Location → Wound Tier`

and stopped at:

`Wound Tier + Location → exact mechanical consequence`

This is materially more informative than simply failing to reach the Wound pathway.

The v4 test therefore demonstrates that the remaining issue is **not merely the existence of a Location roll or a numeric Wound Tier table**. The missing operational link is the consequence-selection layer after those values have been established.

---

# 17. Principal Findings

## Finding F-01 — Combat Sequencing Operates

The Speed comparison produced an unambiguous first actor:

`175 > 150`

No additional initiative machinery was required.

**Assessment:** exercised successfully.

---

## Finding F-02 — Passive Frightened Operates

The scene-state binding applied the −1 modifier before the PC Defence test:

`Defence2 25 → effective 24`

This had a measurable mechanical effect on the resolution.

**Assessment:** exercised successfully.

---

## Finding F-03 — PE Transaction Operates

Both combatants demonstrated the complete:

`PE Before → Cost → Recovery → PE Final`

transaction.

No Overflow occurred.

**Assessment:** exercised successfully.

---

## Finding F-04 — Failure XP Cascade Operates

The PC's failed Defence roll generated:

`73 − 24 = 49 XP`

The skill advanced:

`25 → 26`

with 24 XP remaining.

**Assessment:** exercised successfully.

---

## Finding F-05 — Location/Wound Invocation Now Reaches the Intended Test Boundary

The mandatory Wound exercise succeeded in reaching:

`Quality 30 → gated → Location 32 → Torso → Wound Tier 4`

This is an important v4 improvement over the earlier runs.

**Assessment:** invocation pathway exercised.

---

## Finding F-06 — Wound Consequence Resolution Remains Incomplete

The test cannot determine the exact Attribute/Skill affected by the Tier-4 Torso Wound.

**Assessment:** blocking gap remains.

---

## Finding F-07 — Active Defense Does Not Yet Close the Full Wound Branch

Although the defensive test itself resolved, the available corpus does not provide the necessary consequence transformation for Active Defense against a Wound.

**Assessment:** blocking gap remains.

---

# 18. Lessons for Future Playtests

## 18.1 The Next Test Should Not Add Another Combat Scaffold Blindly

The v4 execution demonstrates that additional generic scaffolding would risk masking the actual design dependency.

The next intervention should specifically resolve the two exposed questions:

1. **Wound target selection**
2. **Active Defense mitigation against Wound consequences**

Those questions should be resolved before another full Ice Troll combat execution is treated as an end-to-end validation.

## 18.2 Keep Location and Wound Tier Separate

The execution validates the distinction:

`Location Index → anatomical zone`

versus:

`Quality → Wound Tier`

The two are separate dimensions and should not be conflated.

## 18.3 Preserve the Governance Boundary

The v4 procedure worked correctly at the point where the rules stopped: the executor stopped rather than converting an LLM assumption into a Tiwas mechanic.

That behaviour should be retained.

---

# 19. Final Assessment

## Overall Status

**V4 PLAYTEST: ABORTED — DIAGNOSTIC SUCCESS / END-TO-END VALIDATION FAILURE**

The run successfully validated several operational components:

- Speed-based combat sequencing;
- passive Frightened application;
- d100 roll-under;
- Margin/Quality;
- resource cost;
- recovery;
- Failure XP;
- XP cascade;
- Quality gating;
- Location Index;
- Location quartile mapping.

The run also successfully exercised the previously under-tested Location/Wound pathway.

However, it demonstrated that the complete combat consequence chain remains unfinished at the point where a Wound must be converted into a specific mechanical state and Active Defense must modify that state.

The correct result was therefore an explicit GM stop.

No new mechanic was invented.

No scaffold was promoted to canonical status.

No DEC number was assigned.

---

# 20. Conclusion

The v4 execution produced a substantially more useful diagnostic result than a simple combat failure. The test reached the intended Wound branch and established the following concrete chain:

`Ice Troll Speed 175`
→ `acts first`
→ `Icy Claws 67`
→ `d100 37`
→ `Margin/Quality 30`
→ `gated Effect`
→ `Defence2 24`
→ `d100 73`
→ `defensive failure`
→ `Location Index 32`
→ `Torso`
→ `Wound Tier 4`

The chain then became non-deterministic because the executable corpus does not specify the affected Attribute/Skill or the Active Defense modification to the Wound consequence.

Accordingly, the test **must remain ABORTED** at that point.

The v4 scaffolds did their intended job: they removed several execution ambiguities without silently converting those assumptions into canonical mechanics. The remaining blocker is now narrower and more precisely identifiable.

### DEC-012 provenance reiterated

> **Provenance of the DEC-012 exception:** the two pre-built Tier-2 skills on Adventurer-1 (Attack2, Defence2) were granted under a **prompt-level scaffold** (Tiwa's authorization, 2026-09-04) for this playtest only. They are **NOT backed by a PC-scoped register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates and preserves DEC-012's failed-Double origin for player-character skill advancement generally. Therefore: this exception is **non-register-backed**, creates **no new precedent**, grants the PC **no canonical authority** from these skills, and must **not** be cited in any future DEC or proposal as evidence that PCs can receive pre-authored Tier-2 skills outside DEC-012.

**No canonical rule change is proposed by this report.**

---

# Appendix A — Structured JSON Audit Data

```json
{
  "playtest": {
    "title": "Tiwas TTRPG - Ice Troll Combat Playtest v4",
    "prompt_version": "4.0",
    "execution_date": "2026-09-04",
    "status": "ABORTED",
    "rng_method": "Python secrets.SystemRandom() using OS entropy",
    "computation_method": "Python-computed arithmetic and state tracking",
    "engine_runtime": null
  },
  "pre_combat_state": {
    "Adventurer-1": {
      "HP": 600,
      "PE": 150,
      "Speed": 150,
      "Attack2": 25,
      "Defence2": 25,
      "Frightened": {
        "active": true,
        "value": -1,
        "source": "scene-state binding"
      }
    },
    "Ice Troll": {
      "HP": 705,
      "PE": 220,
      "Speed": 175,
      "Icy Claws": 67,
      "Sharktoothed Maw": 75,
      "Brawling": 37
    }
  },
  "rounds": [
    {
      "round": 1,
      "turn_order": [
        {
          "actor": "Ice Troll",
          "speed": 175
        },
        {
          "actor": "Adventurer-1",
          "speed": 150
        }
      ],
      "tests": [
        {
          "core_test": 1,
          "actor": "Ice Troll",
          "step": "Attack",
          "skill": "Icy Claws",
          "effective_skill": 67,
          "roll": 37,
          "success": true,
          "margin": 30,
          "quality": 30,
          "cost": 37,
          "PE_before": 220,
          "PE_after_cost": 183,
          "overflow": 0,
          "HP_overflow_damage": 0,
          "recovery": 70,
          "PE_final": 220,
          "effect": "Gated Wound pathway",
          "location_index": 32,
          "location_zone": "Torso",
          "wound_tier": 4,
          "condition_applied": null,
          "active_defense": "Invoked; consequence interaction unresolved",
          "net_HP_change": null
        },
        {
          "core_test": 2,
          "actor": "Adventurer-1",
          "step": "Defense",
          "skill": "Defence2",
          "base_skill": 25,
          "effective_skill": 24,
          "roll": 73,
          "success": false,
          "margin": 0,
          "quality": 0,
          "cost": 73,
          "PE_before": 150,
          "PE_after_cost": 77,
          "overflow": 0,
          "HP_overflow_damage": 0,
          "recovery": 50,
          "PE_final": 127,
          "effect": null,
          "location_index": null,
          "location_zone": null,
          "wound_tier": null,
          "condition_applied": {
            "name": "Frightened",
            "value": -1,
            "source": "scene-state binding"
          },
          "active_defense": 0,
          "net_HP_change": null,
          "failure_xp": 49,
          "skill_after_XP": 26
        }
      ],
      "status": "ABORTED"
    }
  ],
  "post_combat_state": {
    "Adventurer-1": {
      "HP": 600,
      "PE": 127,
      "Attack2": 25,
      "Defence2": 26
    },
    "Ice Troll": {
      "HP": 705,
      "PE": 220,
      "Icy Claws": 67,
      "Sharktoothed Maw": 75,
      "Brawling": 37
    }
  },
  "total_core_tests": 2,
  "rounds_started": 1,
  "complete_rounds": 0,
  "scaffold_usage": {
    "DEC-012_exception": true,
    "attack_selection_alternation": true,
    "quality_to_wound_tier": true,
    "HP_floor_convention": false
  },
  "edge_cases": [
    "Passive Frightened modified Defence2 before resolution",
    "Failure XP cascade increased Defence2 from 25 to 26",
    "High d100 cost of 73 did not cause PE Overflow",
    "Mandatory Location/Wound pathway was reached",
    "Wound target selection was undefined",
    "Active Defense modification of Wound consequence was undefined"
  ],
  "gm_required_stops": [
    {
      "id": 1,
      "reason": "Undefined Wound target and undefined Active Defense-to-Wound modification",
      "verbatim": "GM REQUIRED STOP: The Troll has won with Quality 30, triggering Location Index 32 → Torso → Wound Tier 4. The executable corpus does not specify which Attribute or Skill the Wound targets, nor how Active Defense's Defender's Margin modifies a Wound Tier/magnitude. Continuing would require inventing a mechanic. Await Tiwa's ruling."
    }
  ]
}
```