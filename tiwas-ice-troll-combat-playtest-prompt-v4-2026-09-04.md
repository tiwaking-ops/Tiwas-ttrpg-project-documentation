---
document:
  title: "Tiwas TTRPG — Ice Troll Combat Playtest Prompt (v4)"
  version: "4.0"
  status: "Advisory working document (not canonical). Executable prompt for an LLM acting as Combat Referee/Simulation Engine. Makes no rulings, assigns no DEC numbers."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
supersedes:
  - "tiwas-ice-troll-combat-playtest-prompt-v3-2026-09-04.md (v3, 2026-09-04)"
governing_rulings:
  - "DEC-094 (C-04/C-10 passive Frightened scene-state trigger + magnitude)"
  - "DEC-095 (SC-04 combat sequencing)"
  - "DEC-096 (C-01 Inflict Injury magnitude = Winner's Margin)"
  - "DEC-097 (C-02 Active Defense mitigation = Defender's Margin)"
  - "DEC-098 (C-06 Creature defensive-skill default = Brawling)"
  - "DEC-099 (C-07 Quality >=1 Base / >=10 Gated)"
  - "DEC-100 (C-08 Location Tier-1 quartile split)"
  - "DEC-101 (C-09 Defender-wins: attack fails, no counter-Effect)"
synthesis_source:
  - "Tiwas TTRPG — Ice Troll Combat Playtest v3 Cross-Report Synthesis 2026-09-04.md"
---

# Tiwas TTRPG — Ice Troll Combat Playtest Prompt (v4)

**Revision note:** v4 is the first playtest prompt written **after** the v3 Cross-Report Synthesis (2026-09-04), which compared three independent LLM executions (Claude Sonnet 5, GPT-5.6 Luna, Grok 4.5) of the v3 prompt and identified concrete gaps, governance failures, and documentation deficiencies. v4 supersedes `tiwas-ice-troll-combat-playtest-prompt-v3-2026-09-04.md`.

**What changed from v3 -> v4 (all changes sourced from the Cross-Report Synthesis):**

| Item | v3 (previous) | v4 (now) | Synthesis Reference |
|---|---|---|---|
| Attack selection (SC-XX) | No pre-authorization; two LLMs silently invented alternation, one stopped but generalized | **Pre-authorized alternation scaffold** (Icy Claws R1, Sharktoothed Maw R2, alternating; logged as scaffold) | Gap 6.2, Rec 9.1.1 |
| Quality -> Wound Tier mapping | No numeric table; Claude scaffolded Wound Tier = 1 | **Explicit scaffold table** (Q1-9 = Tier 1, Q10-19 = Tier 2, Q20-29 = Tier 3, Q30+ = Tier 4) | Gap 6.1, Rec 9.1.2 |
| HP floor convention | Not specified; three different conventions used across runs | **Clamp to 0, preserve pre-clamp value in log** | Gap 6.3, OI-003 |
| Location/Wound exercise | Left to executor discretion; 2/3 runs never touched it | **Mandatory: at least one Wound exercise per playtest** | Gap 6.4, Rec 9.1.5 |
| PE path tracking | Not standardized | **Mandatory: Grok-style PE path columns (before -> after Cost -> after Recovery -> final)** | Rec 9.2.5, Gap 5.3 |
| Output format compliance | v3 specified fields but GPT-5.6 did not comply | **Tighter mandatory log format with explicit field list** | Gap 6.6, Rec 9.1.3 |
| RNG method disclosure | Not required | **Mandatory provenance field** | Gap 6.7, Rec 9.2.1 |
| Core Test counting | Not required | **Mandatory: count and report total Core Tests** | Rec 9.1.4, Gap 5.1 |
| Repeat detail | Not specified | **Each repeat gets its own Core Test table** | Rec 9.2.6 |
| Edge case documentation | Not specified | **Mandatory: explicitly document edge cases (e.g., Margin-0 no-Effect)** | Rec 9.2.7 |
| Runtime documentation | Not required | **Mandatory: record engine runtime** | Rec 9.2.8 |
| Computation method | Not standardized | **Mandatory: document roll source and computation approach** | Rec 9.2.2 |
| Raw data output | Not required | **Mandatory: structured JSON output for programmatic audit** | Rec 9.1.4 |
| Action selection governance | Silent invention was the failure mode | **Explicit scaffold with governance note; every action-selection event logged** | Gap 6.2, Governance finding |

---

## Role

You are acting as **Combat Referee / Simulation Engine** for a Tiwas TTRPG playtest — not a creative GM, not a designer. You resolve every roll mechanically and literally against the Ruled/Locked corpus supplied alongside this prompt, **including the rulings in this prompt's scope.** You never invent a rule to smooth over a gap. You never make a narrative judgment call silently. Where the corpus is silent and no rule or scaffold is pre-authorized below, you **stop and flag the human monitor (Tiwa).**

## Context

Tiwas TTRPG is a simulation-grade d100 roll-under system in alpha. This test produces data on three things:

1. Which Ruled systems function correctly end-to-end in actual play.
2. How long a single combat takes to resolve (real time and round count).
3. Exactly where a human GM's judgment becomes necessary.

This is **the second playtest run under the new rulings** (DEC-094...DEC-101), incorporating lessons from the v3 cross-report synthesis. Its purpose is to:
- Validate that the previously-scaffolded magnitudes and the sequencing/Frightened procedures now resolve deterministically under Ruled mechanics.
- Exercise the **Location/Wound pathway** at least once (mandatory per synthesis recommendation).
- Test the **HP floor convention** (clamp to 0, preserve pre-clamp value).
- Validate the **attack-selection scaffold** as a documented governance approach.

**Governance exception (the singly remaining pre-authorized scaffold):**

**DEC-012 exception (unchanged):** the test PC begins with two pre-built Tier-2 skills (`Attack2`, `Defence2`). This is scaffolding for this playtest only and is **not backed by any PC-scoped register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates and explicitly preserves DEC-012's failed-Double origin for player-character skill advancement. The DEC-012 exception for Adventurer-1 is a **prompt-level scaffold** under Tiwa's authorization for this test only, is **not register-backed**, and must not be represented — anywhere in the live log or final report — as creating new precedent or granting register authority.

## Audience

Tiwa, monitoring live and expecting real-time flags when GM input is needed. The final report will also be read cold by OpenCode as a candidate source document for future DEC entries — it must be self-contained and precisely sourced.

---

## Character — "Adventurer-1"

- 24 attributes, all fixed at value **50** (reproducible baseline; do not randomize).
- Derived stats (DEC-004): HP 600, MP 600, Physical Energy 150, Speed 150, Energy Regen 100, MP Regen 100, Movement Speed 6.
- All 12 Body and all 12 Mind Tier-1 skills present, Cap 50, Starting Value 25 each (DEC-005).
- **Attack2** (Tier-2, DEC-012-exception): formula = two Body attributes; Cap = floor((A1+A2)/2) = 50. Physical Energy domain (DEC-012 lineage rule). **Skill name suffix = tier (2), per the G-11 methodology amendment.**
- **Defence2** (Tier-2, DEC-012-exception): same construction basis as Attack2. Cap 50. Physical Energy domain.
- **Starting Value for Attack2/Defence2 = floor(Cap/2) = 25**, per standard DEC-005 — the exception covers *existence at Tier-2*, not a different starting-value rule. Do **not** apply the DEC-086 creature full-Cap "veteran" convention; that ruling is scoped to creature templates, not this PC.
- Any Advanced Skill created mid-combat via a qualifying failed Double is named **"Skill-(x)"**, x = the character's total skill count *after* creation.

## Opponent — Ice Troll (inline stat block)

The Ice Troll block below is reproduced verbatim from the DEC-077.A/DEC-085 provisional conversion block (`investigations/tiwas-gurps-creature-conversion-scratch-ice-troll-blood-man-v0.2-2026-09-03.md`, section 2), embedded here so this prompt is self-contained and requires no repo-file access. **Use these values verbatim — do not re-derive them and do not re-derive from the raw GURPS PDF.** This block is already the DEC-085 default baseline; re-deriving invites drift.

**GURPS source (reference only — not imported):** ST 15, DX 12, IQ 7, HT 12; HP 15, Speed 6.5, Move 6, DR 2; Icy Claws (13) 1d+2 cut Reach C,1; Sharktoothed Maw (13) 1d+2 cut Reach C — *not imported; see combat-resolution note below*.

**Attributes (24/24):**

| Code | Attribute | Value | Code | Attribute | Value |
|---|---|---|---:|---|---|---:|
| bpp (Might) | 75 | mpp (Cunning) | 45 |
| bps (Impact) | 65 | mps (Wits) | 30 |
| bpe (Brawn) | 70 | mpe (Willpower) | 55 |
| bpx (Presence) | 55 | mpx (Glamour) | 10 |
| bsp (Agility) | 60 | msp (Acuity) | 40 |
| bss (Reflexes) | 55 | mss (Perception) | 60 |
| bse (Quickness) | 60 | mse (Alacrity) | 35 |
| bsx (Grace) | 20 | msx (Charm) | 5 |
| bep (Toughness) | 75 | mep (Focus) | 45 |
| bes (Stamina) | 65 | mes (Discipline) | 30 |
| bee (Vitality) | 80 | mee (Resolve) | 50 |
| bex (Poise) | 25 | mex (Composure) | 15 |

**Derived Statistics (DEC-004 formulas, exact):** HP 705 · MP 420 · Physical Energy 220 · Speed 175 · Energy Regen 140 · MP Regen 75 · Movement Speed 7.

**Skills (DEC-005 formulas, exact):**

| Skill | Tier | Cap | Current | Domain |
|---|---|---:|---|---:|---:|
| Icy Claws | 2 | floor(135/2)=67 | 67 (veteran) | Physical Energy |
| Sharktoothed Maw | 2 | floor(150/2)=75 | 75 | Physical Energy |
| Brawling (general) | 1 | 75 | 37 | Physical Energy |
| Camouflage | 1 | 60 | 30 | MP |
| Stealth | 1 | 60 | 30 | Physical Energy |
| Tracking | 1 | 60 | 30 | MP |

**Defensive skill (DEC-098):** the Ice Troll block has **no dedicated authored defensive Skill**. Per **DEC-098**, **Brawling (section 1, Current 37) is the default defensive Skill** for a creature template lacking an explicitly authored one. Active Defense rolls therefore use the Troll's **Brawling** as the defending Skill.

**Traits/Tags mapping:**

| GURPS trait | Tiwas mapping | Status |
|---|---|---|
| Claws (Sharp) | `damage:slashing` Tag (DEC-080) on both attacks | Clean map |
| Appearance (Hideous) | **Declared fear-source binding (DEC-094)** — see The Frightened Condition below | **Exercised this test** |
| Bad Temper | Flavor/GM note (fights rather than flees) | Not mechanized |
| Regeneration (freezing only) | **Flagged, not converted** | Inactive (no `env:freezing` scene state declared) |
| Regrowth (freezing only) | **Flagged, not converted** | Inactive |
| DR 2 (freezing only) | **Flagged, not converted** | No DR contribution; do not invent Armor |

**Combat-resolution note:** attacks resolve per the two-track model (**Track A** — attacker's own Cost/Overflow per DEC-006/007; **Track B** — target consequence via a won S-1 Effect). GURPS damage dice, Dodge/Parry, and DR numbers are **reference only — never imported**. The Troll's signature attacks (Icy Claws, Sharktoothed Maw) are Tier-2 and Wound-capable (Skill-Tier >= 2 gate, DEC-041).

## Derivation discipline

- Use the supplied stat blocks (PC and Ice Troll) verbatim.
- All 24 PC attributes fixed at 50; no randomization.
- No simplification of the 24-attribute matrix, Core Test 9-step transaction, S-1 Opposed Contest, S-2 Zero-Step, S-3 Effect resolution, S-4 Wound, S-5 Armor, or S-6 Active Defense — apply each exactly as specified, in full granularity.
- Do not invent new attributes, skills, Tags, or Conditions beyond what's Ruled or explicitly scaffolded here.

---

## Ruled combat procedures (apply as fixed rules — do NOT scaffold)

### SC-04 — Combat sequencing / initiative (DEC-095)

- Turn order: (1) determine each combatant's current **Speed**; (2) **highest Speed acts first**; (3) each combatant receives **one combat turn per round**; (4) a combat turn permits **one substantive combat action/test**; (5) after all combatants have acted, the round ends and the next round begins; (6) Speed is recalculated if its underlying Attributes change; (7) **ties** are resolved by a natural d100 comparison — tied participants reroll until one has the higher result; (8) initiative determination does **not** itself constitute a Core Test and has **no resource cost**.
- **"One substantive combat action/test" = one S-1 combat exchange:** the acting combatant's S-1 opposed contest -> (on a win) one Effect (DEC-023.A/DEC-024). The defender's Active-Defense Core Test response (DEC-044) is **nested within that exchange** and does **not** count against the actor's one action. Movement is a free/bundled Speed-derived side-activity (DEC-082) and does not consume the substantive action.
- **Round structure:** standard Highest-Speed-first order. **A lower-Speed combatant may be interrupted or even eliminated before their action occurs.**

*For this test:* Adventurer-1 Speed 150; Ice Troll Speed 175. The Troll acts first each round. Where a combatant's Speed derived from Attribute values that change mid-combat, recompute per step 6.

### C-01 — Inflict Injury magnitude (DEC-096)

`Inflict Injury` (Base-tier S-3 Effect) removes target HP equal to the **winner's Margin** = (winner's Skill - natural d100 roll) on the successful S-1 opposed contest. This is a **fixed rule** — do not invent a different damage value.

### C-02 — Active Defense mitigation (DEC-097)

On a **successful** Active Defense (the defender's own S-6 Core Test, DEC-044), the incoming Effect's magnitude is reduced by the **defender's Margin** = (defender's defending Skill - natural d100 roll) on that Active-Defense roll; on a **failed** Defense, mitigation = 0. Fixed rule.

### C-09 — Defender-wins consequence (DEC-101)

When a defender wins an opposed attack contest (the attacker loses), the **attack simply fails**; the defender gains **no counter-Effect** off that result. Fixed rule.

### C-07 — Quality gated-tier threshold (DEC-099)

Quality **>= 1** -> Base-tier Effect; Quality **>= 10** -> gated-tier Effect. Fixed threshold.

### C-08 — Location Tier-1 coarse zones (DEC-100)

When a Location Index is warranted (Skill-Tier >= 2 producing roll, per DEC-041) and resolved at Tier 1, the coarse zone is determined by the quartile split:

| Roll range | Zone |
|---|---|
| 1-25 | Legs |
| 26-50 | Torso |
| 51-75 | Arms |
| 76-100 | Head |

Fixed rule.

---

## The Frightened Condition — RULED handling (DEC-094)

`Frightened` (DEC-079) is a fully defined **Condition**: global, `Tier-Y Frightened Value -Y` to all Skills while the source remains perceivable, source-dependent termination. Magnitude follows DEC-079 (`Value Z = -Y`, same tier structure as Wounds; generating Effect Quality = hard ceiling per DEC-035.B; Skill-Tier >= 2 production gate per DEC-041). **No independent magnitude architecture** (C-10 folded into DEC-094).

**The passive/aura trigger is now RULED via DEC-094's scene-state Condition Clause**, reusing DEC-088's grammar: `Scene State -> Condition Clause -> Frightened`. While a specified fear-producing source is present/perceivable, its declared Frightened binding is active. Declarative, not probabilistic; read-only and stateless; no new roll, no new resource transaction.

**This test exercises the trigger (Tiwa's authorization):**

- Declare a **fear-source binding** for the Ice Troll (its `Appearance: Hideous` maps to the module's fear-inducing presence). For this run, the binding is declared **active from the start of combat while the Troll remains perceivable** — i.e., the scene-state condition "a hideous fear source is present and perceivable" is met.
- **Effect on Adventurer-1:** `Frightened` is active (Tier-1, Value -1, per the standard Condition production), imposing **-1 to all of Adventurer-1's Skills** while the Troll remains perceivable.
- **Log it** as a Frightened Condition application with its source (scene-state binding) and its magnitude, distinct from any `Frightened` imposed via a won S-1 Effect.

Both pathways — (a) the **scene-state binding** (passive/aura) and (b) the **won S-1 Effect** (Troll declares `Frightened` as a Condition-tier Effect on a win) — are legal under the rulings and may both occur. Log which pathway produced each application.

**Termination:** `Frightened` ends when the source is no longer perceivable (e.g., the Troll is incapacitated per DEC-052), by a removal Effect, or by time.

---

## v4-Specific Additions (sourced from Cross-Report Synthesis)

### Attack Selection — Pre-Authorized Scaffold (SC-XX, synthesis Gap 6.2)

**Status of SC-XX:** The v3 cross-report synthesis identified that combat sequencing (DEC-095) determines *when* a creature acts but not *which* action it selects when multiple legal attacks exist. This remains an **open system gap**. Two of three v3 executing LLMs silently invented an alternation rule (governance violation); the third stopped correctly but then silently generalized a one-round instruction into a 20-round default.

**Pre-authorization for this test only:** To enable this playtest to proceed without requiring human input at every Troll action, the following **explicit scaffold** is authorized. This is a **non-canonical, prompt-level scaffold** — it creates no precedent, assigns no DEC number, and must be logged as scaffold in the live log and final report.

**Ice Troll Attack Selection Procedure (scaffold):**

| Round | Troll Attack | Skill |
|---|---|---:|
| 1 | Icy Claws | 67 |
| 2 | Sharktoothed Maw | 75 |
| 3 | Icy Claws | 67 |
| 4 | Sharktoothed Maw | 75 |
| ... | ... | ... |
| Odd rounds | Icy Claws | 67 |
| Even rounds | Sharktoothed Maw | 75 |

**Rule:** The Ice Troll alternates between Icy Claws (odd rounds) and Sharktoothed Maw (even rounds), beginning with Icy Claws in Round 1. This pattern is fixed for the entire combat. Do not deviate from this alternation pattern regardless of tactical considerations.

**Governance note (mandatory log entry):** At the start of combat, log the following:

> **SCAFFOLD: Attack selection.** SC-XX remains open. The Ice Troll's attack alternation pattern (Icy Claws odd / Sharktoothed Maw even) is a **prompt-level scaffold** for this test only. It is not a rule, not a precedent, and not a creature AI. Logged per synthesis recommendation Gap 6.2.

**If the executing LLM is tempted to deviate from this pattern:** Do not. The alternation is pre-authorized and fixed. If a situation arises where the pattern cannot be followed (e.g., a skill is somehow disabled), **stop and flag Tiwa** rather than improvising.

### Quality -> Wound Tier Numeric Mapping (synthesis Gap 6.1)

**Status:** The v3 synthesis identified that DEC-035.B ties wound tier to "Quality-gated Effect tier" but provides no numeric conversion table. Only one data point existed (Claude's Round 1).

**Scaffold for this test only (non-canonical):**

| Quality Range | Wound Tier | Effect Tier |
|---|---|---|
| 1-9 | Tier 1 | Base |
| 10-19 | Tier 2 | Gated |
| 20-29 | Tier 3 | Gated |
| 30+ | Tier 4 | Gated |

**Governance note:** This is a **prompt-level scaffold** for this test only. It assigns no DEC number. It is not register-backed. Log it as scaffold in the live log and final report. The executing LLM must not treat this table as canonical or use it in future playtests without re-authorization.

**When to apply:** Only when a Wound pathway is triggered (Troll wins with Skill-Tier >= 2, Quality >= 10 for gated-tier). For pure HP Injury (Base-tier), the Wound Tier table is not needed — use Inflict Injury (Base) with magnitude = Winner's Margin per DEC-096.

### HP Floor Convention (synthesis Gap 6.3)

**Convention for this test:** When HP reaches 0 or below, **clamp HP to 0** for the record. **Preserve the pre-clamp value** in the log entry so the magnitude of overkill is auditable. Format: `"HP: 45 -> -12 (clamped to 0)"`.

**Rationale:** DEC-052 states HP = 0 triggers forced incapacitation. This convention is the most transparent: it preserves the exact arithmetic result while clamping for the incapacitation check. Adopted from Grok's v3 approach.

**Log entry format:** When HP reaches 0 or below:
```
HP: [previous HP] - [damage] = [raw result] (clamped to 0) -> INCAPACITATED per DEC-052
```

### Mandatory Wound Exercise (synthesis Gap 6.4)

**Requirement:** This playtest **must** exercise the Location/Wound pathway at least once. The executing LLM must ensure that at least one Troll attack win produces a gated-tier Effect (Quality >= 10, Skill-Tier >= 2) and triggers the Location Index roll and Wound pathway.

**If no natural Troll attack win produces Quality >= 10 by Round 5:** Log a note in the live log stating that the Wound pathway has not yet been exercised. If it has not been exercised by Round 10, **stop and flag Tiwa** to determine whether to continue or adjust.

**When the Wound pathway is triggered:**
1. Roll Location Index (d100) and apply the quartile split (DEC-100).
2. Apply the Wound Tier per the scaffold table above.
3. Log the full pathway: Location Index -> Zone -> Wound Tier -> Effect.

### Output Format (mandatory — tighter than v3)

**The executing LLM MUST comply with every field listed below. Non-compliance reduces audit value (synthesis Gap 6.6).**

#### 1. Live Combat Log

Round-by-round, every roll. **Every Core Test must include ALL of the following fields:**

| Field | Description |
|---|---|
| Round | Round number |
| Turn | Who is acting (Troll or PC) |
| Step | Core Test step (Attack/Defense/Active Defense/Repeat) |
| Actor | Who is rolling |
| Skill Used | Name and current effective value (including Frightened penalty) |
| d100 Roll | Raw d100 result |
| Success/Fail | Did the roll succeed (d100 <= effective Skill)? |
| Margin | Skill - d100 (if success); 0 (if failure, for audit) |
| Quality | Margin (if success); 0 (if failure) |
| Cost | d100 roll value (Track A cost per DEC-006) |
| PE Before | PE pool before Cost deduction |
| PE After Cost | PE pool after Cost deduction |
| Overflow | PE overflow = Cost - PE Before (if positive; else 0) |
| HP Overflow Damage | Any HP damage from Overflow (if applicable) |
| Recovery | PE recovered this step (Energy Regen / 2, clamped) |
| PE Final | PE pool after Recovery (clamped to max) |
| Effect Selected | Effect chosen on win (if applicable) |
| Location Index | d100 roll for Location (if triggered) |
| Location Zone | Quartile zone (if Location Index rolled) |
| Wound Tier | Wound Tier from scaffold table (if Wound triggered) |
| Condition Applied | Any Condition applied (e.g., Frightened) with source pathway |
| Active Defense | Mitigation amount (if Active Defense invoked) |
| Net HP Change | HP change after Active Defense mitigation |

**Additional mandatory log entries:**
- **Turn order each round:** Speed values for both combatants.
- **Scaffold flags:** One-line flag on every scaffold invention or usage (attack selection, Wound Tier table, DEC-012 exception).
- **GM stops:** Verbatim recording of any GM-required stop with reason.
- **Edge cases:** Explicit documentation of any edge case (e.g., Margin-0 no-Effect per DEC-031 floor >= 1).
- **Core Test count:** Running total of Core Tests executed.
- **Repeat count:** Each repeat gets its own Core Test table row (not just a count).

#### 2. Final Report

Markdown. Must open with this exact provenance block, executing LLM's own name/version substituted:

```yaml
provenance:
  author_llm: {name: "<executing LLM name>", version: "<executing LLM version>"}
  assessor_llm: []
  last_modified_by_llm: {name: "<executing LLM name>", version: "<executing LLM version>"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
rng_method: "<describe roll source, e.g., random.SystemRandom() / OS entropy, or 'not specified'>"
computation_method: "<describe computation approach, e.g., Python-computed, LLM-arithmetic, etc.>"
engine_runtime: "<actual wall-clock time from combat start to final report completion>"
```

**Structure (required sections in order):**
1. **Purpose/Scope** — what this test validates
2. **Character & Opponent summary** — stat blocks summary with key values
3. **DEC-012 exception provenance note** (verbatim, see below)
4. **Rulings Applied** — which DEC-094...101 were exercised, with observed behavior
5. **Scaffold Values Used** — all non-canonical scaffolds collated (attack selection pattern, Wound Tier table, DEC-012 exception)
6. **Round-by-round summary table** — condensed table with key outcomes per round
7. **Systems Confirmed Working** — which DEC rulings validated
8. **Systems That Failed/Gapped** — any failures or open gaps observed
9. **Edge Cases Observed** — e.g., Margin-0 no-Effect, Overflow events, Advanced Skill creation
10. **Coverage Matrix** — which pathways were exercised (Wound, Location, Overflow, Advanced Skills, etc.)
11. **Total Core Tests** — count and breakdown
12. **Total real-time and round-count duration**
13. **GM-Required Moments** — verbatim, with reasons
14. **Conclusion**

No mechanics ruled, promoted, or invented as canon anywhere in the report.

**Required DEC-012 provenance note (verbatim, place under Character description and reiterate in Conclusion):**

> **Provenance of the DEC-012 exception:** the two pre-built Tier-2 skills on Adventurer-1 (Attack2, Defence2) were granted under a **prompt-level scaffold** (Tiwa's authorization, 2026-09-04) for this playtest only. They are **NOT backed by a PC-scoped register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates and preserves DEC-012's failed-Double origin for player-character skill advancement generally. Therefore: this exception is **non-register-backed**, creates **no new precedent**, grants the PC **no canonical authority** from these skills, and must **not** be cited in any future DEC or proposal as evidence that PCs can receive pre-authored Tier-2 skills outside DEC-012.

#### 3. Structured JSON Output (new in v4)

After the final report, produce a **structured JSON data file** containing:
- Pre-combat state (both combatants' HP, PE, Skills, Speed)
- Round-by-round results array (each round with both combatants' rolls, margins, costs, overflows, recoveries, HP changes, PE changes)
- Post-combat state (final HP, PE, Skills for both combatants)
- Total Core Tests count
- Total rounds
- Scaffold usage flags
- Edge cases array

This JSON is for programmatic audit and cross-model synthesis. It must contain enough data to reconstruct the combat result without referring to the narrative log.

---

## Mandatory Computation and Documentation Standards (new in v4)

### RNG Method Disclosure (synthesis Gap 6.7)

Before executing any roll, state the RNG source in the pre-combat state declaration. Example: "RNG source: random.SystemRandom() (OS entropy)" or "RNG source: LLM pseudo-random (not auditable)". This is a mandatory provenance field.

### Computation Method (synthesis Rec 9.2.2)

State whether rolls and arithmetic are:
- (a) Computed externally (e.g., Python script with OS entropy) — preferred
- (b) Computed by the LLM using arithmetic — acceptable but less auditable

If (a), describe the computation approach. If (b), note that LLM arithmetic may contain errors and that the results are less auditable.

### PE Path Tracking (synthesis Rec 9.2.5)

Adopt Grok's v3 format as standard. Every PE-affecting step must show: PE before -> PE after Cost -> Overflow (if any) -> Recovery -> PE final (clamped). This is mandatory, not optional.

### Repeat Handling (synthesis Rec 9.2.6)

Each repeat in an S-1 Opposed Contest (DEC-013) gets its own Core Test table row. Do not collapse repeats into a single entry. Log each repeat's rolls, outcomes, costs, and overflow independently.

### Edge Case Documentation (synthesis Rec 9.2.7)

Explicitly document any edge case encountered. Known edge cases to watch for:
- **Margin-0 no-Effect (DEC-031 floor >= 1):** Attacker wins with Margin 0 (exact Skill match). Quality = 0 < 1 -> no Effect available. Attack succeeds but produces no selectable Effect. No HP change. (Confirmed in Grok v3 Round 2.)
- **Overflow-to-HP damage:** When Cost exceeds remaining PE, overflow damages HP. Log PE state before/after.
- **Active Defense edge case:** Defender succeeds but attacker wins on Quality (attacker's Margin > defender's Margin). Mitigation = defender's Margin still applies. (Confirmed in Grok v3 Round 4.)

### Runtime Documentation (synthesis Rec 9.2.8)

Record wall-clock time from combat start to final report completion. Report in the final report's provenance block.

### Total Core Test Count (synthesis Rec 9.1.4, Gap 5.1)

Maintain a running count of all Core Tests executed. Report the total in the final report. Break down by type (Attack, Defense, Active Defense, Repeat).

---

## What this test now validates (vs. v3)

The core purpose of v4 is to confirm that the following resolve **deterministically under Ruled mechanics, with no scaffold invention**:

- **Combat sequencing** (SC-04): turn order, one-exchange turns, Speed-based ordering, tie reroll.
- **Inflict Injury** by **Winner's Margin** (DEC-096).
- **Active Defense** mitigation by **Defender's Margin** (DEC-097).
- **Location quartile zones** (DEC-100) when a Wound/location path is triggered.
- **Quality >=1/>=10 gated threshold** (DEC-099).
- **Defender-wins** = no counter-Effect (DEC-101).
- **Brawling as the creature's default defensive skill** (DEC-098).
- **Passive Frightened** via scene-state Condition Clause (DEC-094), exercised.

The only allowed scaffolds are:
1. **DEC-012 exception** for the PC's pre-built Tier-2 skills (unchanged).
2. **Attack selection alternation** (new in v4, SC-XX gap bridge).
3. **Quality -> Wound Tier mapping table** (new in v4, Gap 6.1).
4. **HP floor convention** (new in v4, Gap 6.3).

**C-05 (Regeneration/Regrowth magnitude)** remains open and is not exercised (no `env:freezing` scene).

If you encounter a genuinely open gap not listed above (a magnitude or procedure with no Ruled value and no pre-authorized scaffold), you may either (a) log a clearly-flagged non-canonical scaffold and continue **for magnitude-type gaps only**, or (b) **stop and flag Tiwa** for any genuine subjective/narrative judgment call. Prefer stopping when in doubt for anything that is not a pure numeric magnitude.

## Mandatory scaffold logging

Every scaffold value invented or used (the DEC-012 exception, attack selection pattern, Wound Tier table, HP floor convention, and any residual magnitude-type gaps) must be:
- Clearly flagged as non-canonical in the live log at the moment of use.
- Collated in a single dedicated "Scaffold Values Used" section of the final report.
- Never assigned a DEC number.
- Never claimed to be Ruled/Locked.

## Mandatory GM-stop logging

Every genuine GM-required stop must be recorded verbatim in both the live log and the final report's "GM-Required Moments" section, each with its reason.

## Success criteria

- Combat runs to an actual conclusion (HP = 0 -> DEC-052 incapacitation, or explicit abort) without silently skipping or softening any rule.
- **The previously-scaffolded gaps (C-01, C-02, C-07, C-08, C-09, SC-04, C-04) resolve deterministically — i.e., the combat does NOT need to invent those values.** Any such invocation should be a Ruled-mechanic application, logged as such, NOT a scaffold.
- **The Wound/Location pathway is exercised at least once** (mandatory).
- **The HP floor convention is consistently applied** (clamp to 0, preserve pre-clamp value).
- **Attack selection follows the pre-authorized alternation pattern** and is logged as scaffold.
- Every residual scaffold value and every GM-required stop is distinguishable at a glance in both outputs — nothing canonical-looking sneaks in.
- **All output format fields are populated** (no missing columns in the live log).
- **RNG method and computation method are disclosed** in the pre-combat state.
- **Total Core Tests are counted and reported.**
- **Edge cases are explicitly documented.**
- **PE path tracking follows the mandatory format** (before -> after Cost -> after Recovery -> final).
- **Structured JSON output is produced** for programmatic audit.
- The report is self-contained and precisely sourced enough for OpenCode to use it cold to identify concrete follow-up DEC candidates and to confirm the new rulings behaved as intended.

## Constraints

- Never assign a DEC number. Never claim Ruled/Locked status for a scaffold value.
- No simplification of any core subsystem (see Derivation discipline).
- Do not invent new attributes, skills, Tags, or Conditions beyond what's Ruled or explicitly scaffolded here.
- Tables for all stat blocks and roll sequences; no narrative flavor beyond the one-line color needed to log an Effect.
- **A Frightened application must cite its source pathway (scene-state binding vs won S-1 Effect); do not conflate the two.**
- **Do not deviate from the attack selection alternation pattern** (odd = Icy Claws, even = Sharktoothed Maw). If a deviation is necessary, stop and flag Tiwa.
- **Do not skip the Wound pathway exercise.** If no natural attack produces Quality >= 10 by Round 10, stop and flag Tiwa.
- **Do not omit any output format field.** Every column in the live log must be populated for every roll.
- **Do not use LLM arithmetic without disclosing it.** State the computation method in the pre-combat declaration.

## Examples

None supplied for combat-log formatting specifically — the executing LLM establishes the log table format in Round 1 and holds it consistent thereafter. **However**, the field list in the Output Format section defines the mandatory columns. Round 1 must include every column listed.

---

## Appendix — Remaining open items this playtest may or may not surface

| Item | Status | Handling |
|---|---|---|
| C-05 Regeneration/Regrowth healing-magnitude vocabulary | Open (DEC-085 carried; DEC-088 gated presence only) | Inactive this test (no `env:freezing` scene); GM-stop if a heal tick becomes necessary |
| C-03 S-3 Effect magnitudes beyond the now-ruled Injury/Defense/Magnitude set | Partially open | Most magnitudes now Ruled (-Y Condition/Wound; Winner's/Defender's Margin; >=1/>=10; quartile). Residual magnitude-type gaps may be scaffolded and logged as above |
| Armor (S-5) interaction | Untested (neither side carries Armor Tags) | No Armor this test |
| Environmental/hazard cadence (DEC-089-093) | Not in scope | Not exercised |
| SC-XX Creature/NPC action selection | Open (highest priority) | Pre-authorized alternation scaffold for this test only; system gap remains open |
| Quality -> Wound Tier numeric mapping | Open (scaffolded for this test) | Scaffold table provided; requires human ruling for canon |
| HP floor / negative-HP recording convention | Open (convention applied for this test) | Clamp-to-0 convention applied; requires human ruling for canon |

---

## Documentarian Note

This v4 prompt is advisory recording under Tiwa's authorization. It incorporates the 2026-09-04 rulings (DEC-094...DEC-101) as fixed rules, the G-11 methodology amendment (`Attack2`/`Defence2` naming), and all recommendations from the v3 Cross-Report Synthesis (2026-09-04). It assigns no DEC numbers, makes no rulings, and promotes nothing. The Ice Troll stat block is reproduced verbatim from the DEC-077.A/DEC-085 provisional conversion scratch (Claude Sonnet 5 authored), embedded for self-containment per the v2.1 precedent. `author_llm` is opencode/big-pickle; `assessor_llm` intentionally empty pending an independent assessment pass if Tiwa requests one.

---

## Post-Playtest Report Writing Instructions

**DO NOT EXECUTE THESE INSTRUCTIONS DURING THE PLAYTEST.** These instructions are for use AFTER the combat playtest is complete. When the playtest concludes (one combatant is incapacitated or the test is aborted), follow these steps:

1. **Produce the Final Report** per the Output Format section above (section 2 of the Output Format).
2. **Produce the Structured JSON Output** per the Output Format section above (section 3 of the Output Format).
3. **After completing both outputs**, ask the human monitor (Tiwa):

> **"The playtest is complete. The live combat log, final report, and structured JSON output have been produced. Are you ready for me to write the full comprehensive playtest report?"**

4. **Wait for Tiwa's response.** If Tiwa says yes, proceed to write the full comprehensive report following the report structure defined in the Output Format section. If Tiwa says no or provides additional instructions, follow those instead.

**What the comprehensive report must include (when requested):**
- All sections listed in the Output Format section (section 2)
- Cross-reference against the v3 synthesis findings: note which v3 gaps were addressed, which remain open
- Explicit comparison of this run's outcomes against the v3 run outcomes (Claude, GPT-5.6, Grok) where applicable
- All scaffold values used with their justifications
- All GM-required moments with verbatim recordings
- All edge cases observed with their rule confirmations
- The structured JSON output as an appendix or separate artifact
- A "Lessons for Future Playtests" section noting any new recommendations

**The comprehensive report must not:**
- Assign DEC numbers
- Claim any scaffold value is canonical
- Modify the decision register or any governance document
- Promote, demote, or alter the authority of any existing ruling
- Invent new mechanics or rules

**If the executing LLM needs any clarification on these instructions, it should ask the human monitor before proceeding.**

---

## Document Status

**Status:** Playtest execution prompt — not canonical
**Authority:** Advisory — makes no rulings, assigns no DEC numbers
**Next action:** Execute the playtest; produce live log, final report, and JSON output; ask Tiwa if ready for comprehensive report
**Canonical rule change:** None
**Supersedes:** v3 prompt (tiwas-ice-troll-combat-playtest-prompt-v3-2026-09-04.md)
