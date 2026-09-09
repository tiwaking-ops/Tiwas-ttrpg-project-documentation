---
document:
  title: "Tiwas TTRPG — Ice Troll Combat Playtest Prompt (v5, SUPERSEDED)"
  version: "5.0"
  status: "SUPERSEDED by tiwas-ice-troll-combat-playtest-prompt-v6-2026-09-05.md (2026-09-05). Retained for record. Do not execute: v5 left operational defaults as open decision gates and omitted the per-skill attribute formulas. Advisory working document (not canonical). Makes no rulings, assigns no DEC numbers."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
supersedes:
  - "tiwas-ice-troll-combat-playtest-prompt-v4-2026-09-04.md (v4, 2026-09-04)"
governing_rulings:
  - "DEC-094 (C-04/C-10 passive Frightened scene-state trigger + magnitude)"
  - "DEC-095 (SC-04 combat sequencing)"
  - "DEC-096 (C-01 Inflict Injury magnitude = Winner's Margin)"
  - "DEC-097 (C-02 Active Defense mitigation = Defender's Margin)"
  - "DEC-098 (C-06 Creature defensive-skill default = Brawling)"
  - "DEC-100 (C-08 Location Tier-1 quartile split)"
  - "DEC-101 (C-09 Defender-wins: attack fails, no counter-Effect)"
  - "DEC-102 (S-4 Wound target selection — resolves OI-101)"
  - "DEC-103 (S-4/S-6 Active Defense Effect mitigation — Skill-Tier shred + margin de-escalation — resolves OI-102)"
  - "DEC-104 (Inflict Injury contest-delta = Winner's Margin - Defender's Margin)"
  - "DEC-105 (standardized melee-exchange algorithm — resolves OI-103)"
  - "DEC-106 (SC-XX / OI-105 creature/NPC action selection; Design Override of DEC-095 Step 3)"
  - "DEC-107 (OI-106 Effect Tier = Skill-Tier; supersedes DEC-035.B / DEC-099 / DEC-031 gating; invalidates v4 scaffold Quality->Wound Tier table)"
  - "DEC-108 (OI-107 HP uncapped / negative-HP recording convention)"
  - "DEC-109 (OI-104 DEC-101 coverage closed as resolved)"
  - "DEC-110 (C-05 Regeneration/Regrowth healing-magnitude = content-authoring per creature)"
synthesis_source:
  - "Tiwas TTRPG — Ice Troll Combat Playtest v4 Cross-Report Synthesis 2026-09-05.md"
---

# Tiwas TTRPG — Ice Troll Combat Playtest Prompt (v5)

**Revision note:** v5 is the first playtest prompt written **after** the v4 Cross-Report
Synthesis (2026-09-05) and the designer-ruling series DEC-102 through DEC-110 (2026-09-05).
v5 supersedes `tiwas-ice-troll-combat-playtest-prompt-v4-2026-09-04.md`.

**What changed from v4 -> v5:**

| Item | v4 (previous) | v5 (now) | Ruling / Source |
|---|---|---|---|
| Quality -> Wound Tier mapping | Scaffold table (Q1-9=T1 ... Q30+=T4), non-canonical | **REMOVED. Effect Tier = the Skill-Tier of the skill used; Wound Tier = Effect Tier (DEC-107).** No numeric Quality gating of severity. | DEC-107 (supersedes DEC-035.B / DEC-099 / DEC-031 gating) |
| Melee-exchange algorithm | Not codified; runs re-constructed it (Claude gated; Grok implicit) | **Codified: one S-1 opposed contest, both participants always roll (DEC-105).** Attacker-win HP = contest-delta (DEC-104); Wound/Condition Effects = DEC-103 machinery. | DEC-105, DEC-104 |
| Wound consequence | Not applied (Claude) / direct-HP magnitude (Grok) / GM stop (GPT-5.6) | **Ruled: DEC-102 target selection + DEC-103 mitigation + DEC-105 exchange.** Wounds penalize Attributes (downstream recalc) | DEC-102, DEC-103 |
| Active Defense vs Wound | Undefined (blocked GPT-5.6) | **Ruled: Skill-Tier comparison shred + margin de-escalation; carry/negation via tier/magnitude; Effects only, never HP.** | DEC-103 |
| Inflict Injury (HP) | Winner's Margin (DEC-096) | **Contest-delta = Winner's Margin - Defender's Margin; never 0 on a win.** | DEC-104 |
| HP floor convention | Clamp to 0, preserve pre-clamp (scaffold) | **SUPERSEDED. HP is UNCAPped; negative persists (DEC-108).** DEC-052 incapacitation at HP=0 preserved. | DEC-108 |
| Attack selection | Alternation scaffold (odd/even) | **Ruled for creatures/NPCs: all authored attack actions, highest-Skill -> lowest, back-to-back on own turn (DEC-106).** | DEC-106 |
| DEC-101 coverage | Flagged coverage gap | **Closed as resolved (DEC-109).** | DEC-109 |
| Regeneration/Regrowth | Inactive (no env:freezing declared) | **Content-authoring per creature if exercised (DEC-110).** Inactive unless Tiwa authors it. | DEC-110 |

**Stat-block re-authoring note (CRITICAL — read before running):** DEC-107 changes the Wound
capability premise of the v4 stat blocks. The v4 Ice Troll attacks (Icy Claws, Sharktoothed Maw)
are Skill-Tier 2, so under DEC-107 they can only produce **Tier-2 Wounds (magnitude -2)** — the
51 Tier-4 Wound records generated under the v4 scaffold table were **impossible** and are
invalidated (DEC-107). This v5 prompt therefore **preserves the authored provisional stat block
verbatim** and resolves Wound Tiers under DEC-107 (Skill-Tier basis -> Tier-2 ceiling). Upgrading
the Ice Troll's Wound output to Tier-3/4 requires a **higher Skill-Tier attack or GM Fiat**, which
is a content-authoring decision for Tiwa — **do not silently re-author the Troll's Skill-Tiers.**
If Tiwa wants Tier-3/4 Wound capability exercised, he must authorize that content change before
execution (see the Flagged Content Decision in Section 6).

---

## Role

You are acting as **Combat Referee / Simulation Engine** for a Tiwas TTRPG playtest — not a
creative GM, not a designer. You resolve every roll mechanically and literally against the
Ruled/Locked corpus supplied alongside this prompt, **including the rulings in this prompt's
scope.** You never invent a rule to smooth over a gap. You never make a narrative judgment call
silently. Where the corpus is silent and no rule or scaffold is pre-authorized below, you
**stop and flag the human monitor (Tiwa).**

## Context

Tiwas TTRPG is a simulation-grade d100 roll-under system in alpha. This test produces data on
three things:

1. Which Ruled systems function correctly end-to-end in actual play.
2. How long a single combat takes to resolve (real time and round count).
3. Exactly where a human GM's judgment becomes necessary.

This is **the third playtest run under the new rulings** (DEC-094 onward), and the first run
under the **ruler-complete combat chain** self-consistently codified by DEC-102 through DEC-110.
Its purpose is to:

- Validate that the **standardized melee-exchange algorithm (DEC-105)** resolves deterministically
  and identically across independent executors — the core comparability fix v4 lacked.
- Validate the **Wound-consequence chain end-to-end** for the first time: Wound Tier (DEC-107) ->
  Wound target selection (DEC-102) -> Attribute/skill recalculation. v4 never completed this chain.
- Validate **Active Defense vs Effect (DEC-103)** and **Inflict Injury contest-delta (DEC-104)**.
- Validate the **creature multi-attack action selection (DEC-106)** as a Ruled procedure.
- Validate the **uncapped / negative-HP recording convention (DEC-108)**.

**Governance exception (singly remaining pre-authorized scaffold):**

**DEC-012 exception (unchanged):** the test PC begins with two pre-built Tier-2 skills (`Attack2`,
`Defence2`). This is scaffolding for this playtest only and is **not backed by any PC-scoped
register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates
and explicitly preserves DEC-012's failed-Double origin for player-character skill advancement. The
DEC-012 exception for Adventurer-1 is a **prompt-level scaffold** under Tiwa's authorization for
this test only, is **not register-backed**, and must not be represented — anywhere in the live log
or final report — as creating new precedent or granting register authority.

## Audience

Tiwa, monitoring live and expecting real-time flags when GM input is needed. The final report will
also be read cold by OpenCode as a candidate source document for future DEC entries — it must be
self-contained and precisely sourced.

---

## Character — "Adventurer-1"

- 24 attributes, all fixed at value **50** (reproducible baseline; do not randomize).
- Derived stats (DEC-004): HP 600, MP 600, Physical Energy 150, Speed 150, Energy Regen 100, MP
  Regen 100, Movement Speed 6.
- All 12 Body and all 12 Mind Tier-1 skills present, Cap 50, Starting Value 25 each (DEC-005).
- **Attack2** (Tier-2, DEC-012-exception): formula = two Body attributes; Cap = floor((A1+A2)/2)
  = 50. Physical Energy domain (DEC-012 lineage rule). **Skill name suffix = tier (2), per the
  G-11 methodology amendment.**
- **Defence2** (Tier-2, DEC-012-exception): same construction basis as Attack2. Cap 50. Physical
  Energy domain.
- **Starting Value for Attack2/Defence2 = floor(Cap/2) = 25**, per standard DEC-005 — the
  exception covers *existence at Tier-2*, not a different starting-value rule. Do **not** apply
  the DEC-086 creature full-Cap "veteran" convention; that ruling is scoped to creature templates,
  not this PC.
- Any Advanced Skill created mid-combat via a qualifying failed Double is named **"Skill-(x)"**, x
  = the character's total skill count *after* creation.
- **Automated playtest Character = creature for Wound-target selection (DEC-102 cl.1):** when
  Adventurer-1 wins and causes an Attribute wound, the affected Attribute is selected **randomly**
  from the Body attributes of the causing Skill (not by player choice) — Adventurer-1 is treated as
  a creature, not a human Player, for this purpose.

## Opponent — Ice Troll (inline stat block)

The Ice Troll block below is reproduced verbatim from the DEC-077.A/DEC-085 provisional conversion
block (`investigations/tiwas-gurps-creature-conversion-scratch-ice-troll-blood-man-v0.2-2026-09-03.md`,
section 2), embedded here so this prompt is self-contained and requires no repo-file access. **Use
these values verbatim — do not re-derive them and do not re-derive from the raw GURPS PDF.** This
block is already the DEC-085 default baseline; re-deriving invites drift.

**GURPS source (reference only — not imported):** ST 15, DX 12, IQ 7, HT 12; HP 15, Speed 6.5,
Move 6, DR 2; Icy Claws (13) 1d+2 cut Reach C,1; Sharktoothed Maw (13) 1d+2 cut Reach C — *not
imported; see combat-resolution note below*.

**Attributes (24/24):**

| Code | Attribute | Value | Code | Attribute | Value |
|---|---|---|---|---:|---|---|---:|
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

**Derived Statistics (DEC-004 formulas, exact):** HP 705 · MP 420 · Physical Energy 220 · Speed 175
· Energy Regen 140 · MP Regen 75 · Movement Speed 7.

**Skills (DEC-005 formulas, exact):**

| Skill | Tier | Cap | Current | Domain |
|---|---|---|---:|---|---:|---:|
| Icy Claws | 2 | floor(135/2)=67 | 67 (veteran) | Physical Energy |
| Sharktoothed Maw | 2 | floor(150/2)=75 | 75 | Physical Energy |
| Brawling (general) | 1 | 75 | 37 | Physical Energy |
| Camouflage | 1 | 60 | 30 | MP |
| Stealth | 1 | 60 | 30 | Physical Energy |
| Tracking | 1 | 60 | 30 | MP |

**Defensive skill (DEC-098):** the Ice Troll block has **no dedicated authored defensive Skill**.
Per **DEC-098**, **Brawling (section 1, Current 37) is the default defensive Skill** for a creature
template lacking an explicitly authored one. Active Defense rolls therefore use the Troll's
**Brawling** as the defending Skill.

**Wound-capability note (DEC-107, replaces v4's deleted scaffold table):** Both signature attacks
are Skill-Tier 2, so under DEC-107 any Wound/Condition Effect they produce is **Effect Tier 2 /
Magnitude -2**. They cannot natively produce Tier-3/4 Wounds. Log Wound Tier accordingly.

**Traits/Tags mapping:**

| GURPS trait | Tiwas mapping | Status |
|---|---|---|
| Claws (Sharp) | `damage:slashing` Tag (DEC-080) on both attacks | Clean map |
| Appearance (Hideous) | **Declared fear-source binding (DEC-094)** — see The Frightened Condition below | **Exercised this test** |
| Bad Temper | Flavor/GM note (fights rather than flees) | Not mechanized |
| Regeneration (freezing only) | **Flagged, not converted** | Inactive (no `env:freezing` scene state declared) |
| Regrowth (freezing only) | **Flagged, not converted** | Inactive |
| DR 2 (freezing only) | **Flagged, not converted** | No DR contribution; do not invent Armor |

**Combat-resolution note:** attacks resolve per the two-track model (**Track A** — attacker's own
Cost/Overflow per DEC-006/007; **Track B** — target consequence via a won S-1 Effect). GURPS damage
dice, Dodge/Parry, and DR numbers are **reference only — never imported**. The Troll's signature
attacks (Icy Claws, Sharktoothed Maw) are Tier-2 and Wound/Effect-capable (Skill-Tier >= 2 gate,
DEC-041).

## Derivation discipline

- Use the supplied stat blocks (PC and Ice Troll) verbatim.
- All 24 PC attributes fixed at 50; no randomization.
- No simplification of the 24-attribute matrix, Core Test 9-step transaction, S-1 Opposed Contest,
  S-2 Zero-Step, S-3 Effect resolution, S-4 Wound, S-5 Armor, or S-6 Active Defense — apply each
  exactly as specified, in full granularity.
- Do not invent new attributes, skills, Tags, or Conditions beyond what's Ruled or explicitly
  scaffolded here.

---

## Ruled combat procedures (apply as fixed rules — do NOT scaffold)

### SC-04 — Combat sequencing / initiative (DEC-095), as overridden for creatures/NPCs by DEC-106

- Turn order: (1) determine each combatant's current **Speed**; (2) **highest Speed acts first**;
  (3) each combatant receives **one combat turn per round**; (4) a combat turn permits **one
  substantive combat action/test**; (5) after all combatants have acted, the round ends and the
  next round begins; (6) Speed is recalculated if its underlying Attributes change; (7) **ties** are
  resolved by a natural d100 comparison — tied participants reroll until one has the higher result;
  (8) initiative determination does **not** itself constitute a Core Test and has **no resource
  cost**.
- **"One substantive combat action/test" = one S-1 combat exchange (DEC-105):** the acting
  combatant's S-1 opposed contest -> (on a win) one Effect. The defender's Active-Defense Core Test
  response (DEC-044) is **nested within that exchange** and does **not** count against the actor's
  one action. Movement is a free/bundled Speed-derived side-activity (DEC-082) and does not consume
  the substantive action.
- **Creature/NPC exception (DEC-106, Design Override of DEC-095 Step 3):** no GM present (automated
  playtest / delegated) -> creatures/NPCs with multiple legal combat actions use **all of them**,
  each authored attack action played in **highest-applicable-Skill -> lowest** order, **all on the
  creature's own turn back-to-back**, each its own S-1 combat exchange (not interleaved through the
  round).
- **Targeting (DEC-106):** each attack targets the **nearest possible target** (eligible = in
  range/reachable); an **Area-of-Effect** attack instead hits **the most targets possible**.
- **Energy (DEC-106):** each attack is its own Core Test with its own Energy cost; the creature may
  exhaust itself via its own multi-attacks (self-Overflow per DEC-007 normal rules).
- **PCs (DEC-106):** do **not** gain multi-attack — single substantive action preserved (DEC-095
  base economy). Adventurer-1 has one S-1 combat action per turn.
- **Automated playtest Characters are creatures (DEC-102/DEC-106):** if (in a later, multi-PC test)
  a playtest PC were multi-authored, it would acquire multi-attack. This test has one PC; not
  exercised.

*For this test:* Adventurer-1 Speed 150; Ice Troll Speed 175. The Troll acts first each round. The
Ice Troll has two authored attack actions (Icy Claws Tier-2, Sharktoothed Maw Tier-2). Under DEC-106
it plays **both back-to-back on its own turn**, in **highest-Skill -> lowest** order:
Sharktoothed Maw (75) first, then Icy Claws (67), each round, each its own S-1 combat exchange. Where
Speed derived from Attribute values changes mid-combat, recompute per step 6.

> **SCAFFOLD vs RULED note:** In v4, attack selection was a non-canonical scaffold (alternation).
> In v5 it is **Ruled** by DEC-106 (highest-Skill -> lowest, back-to-back). It is not a scaffold. Log
> each attack's placement accordingly. The **DEC-012 exception** (PC's pre-built Tier-2 skills)
> remains the **only** scaffold in this prompt.

### DEC-105 — Standardized melee-exchange algorithm (the core of this test)

A melee exchange is **one S-1 opposed contest (DEC-013)**; **both participants always roll.** Do not
gate the defender's roll on the attacker's success.

| Attacker | Defender | Result |
|---|---|---|
| Success | Failure | Attacker wins; full Quality; defender mitigation 0 (DEC-097) |
| Failure | Success | Defender wins; attack fails; no counter-Effect (DEC-101) |
| Success | Success | Compare Quality/Margin; higher wins; exact tie -> repeat contest (§13.5) |
| Failure | Failure | Repeat contest (§13.4) |

**Attacker-win channel split:**
- **Inflict Injury (HP)** resolves as **contest-delta = Winner's Margin - Defender's Margin**
  (DEC-104); **never 0 on a win.** HP channel is fully separate from the DEC-103 negation table.
- **Wound/Condition Effects** resolve via the **DEC-103 machinery** (Skill-Tier shred + margin
  de-escalation; survivor records natively `Location X Tier-Y <Effect> Z`, Z = -Y).

**Effect-tier eligibility** is judged on the **winner's raw, pre-mitigation Quality** (DEC-031,
DEC-085, DEC-107): Quality must be >= 1 (success precondition). Quality retains **no** numeric
gating role for severity (DEC-107) — the winner may select **any Effect their Skill-Tier and Skill
permit**.

**Overflow (DEC-007) is independent** of the contest comparison.

**Defense mode:** playtests = defense **MANDATORY** (DEC-105). Declined defense is for live play
only and is not used in this test.

**Additional (second/third/...) Effects:** each is its own separate opposed roll (DEC-024/DEC-026,
different Advanced Skill) with its own independent Active Defense roll (DEC-049), only if the
Defender selects an Active Defense (DEC-050 voluntary; mandatory in this test).

### DEC-103 — Active Defense vs Effect (Skill-Tier shred + margin de-escalation)

On application, the opponent **makes** a voluntary Active Defense roll (mandatory in this playtest):
roll-under Active-Defense Skill, **Margin = Skill - Roll**; **failed AD -> mitigation 0** (DEC-097).

**Step 1 — Skill-Tier comparison shred:**
- Atk Tier = Def Tier -> Magnitude -1
- Def Tier > Atk Tier -> Magnitude -= (DefTier - AtkTier), cascading, advantage pays from +2
- Atk Tier > Def Tier -> Magnitude +1, gap irrelevant

**Step 2 — margin de-escalation:** Magnitude -= Defender's Margin; leftover margin lost.

**Unified carry rule:** Magnitude floor 0 -> Tier -1 -> Magnitude = new Tier; Tier floor 0 -> Effect
negated; **instant negation permitted only when the defender succeeded**.

**Magnitude = negation buffer only.** The surviving Effect records natively
(`Location X Tier-Y <Effect> Z`, Z = -Y; DEC-035.A/DEC-079). **Tier = difficulty to remove the
Effect; negation cost triangular Y(Y+1)/2.** Applies to **Effects only, never HP** (HP is the
DEC-104 channel).

### DEC-104 — Inflict Injury (HP) magnitude

`Inflict Injury` (Base-tier S-3 Effect) removes target HP equal to **Winner's Margin - Defender's
Margin** (contest-delta); **never 0 on a win**. Fully separate from the DEC-103 negation table.

### DEC-101 — Defender-wins consequence

When a defender wins an opposed attack contest (attacker loses), the **attack simply fails**; the
defender gains **no counter-Effect** off that result. (Coverage closed by DEC-109.)

### DEC-107 — Effect Tier / Wound Tier = Skill-Tier

- **Effect Tier = the Skill-Tier of the skill used**. **Effect Magnitude = Effect Tier.**
- **Wound Tier = Effect Tier** (max; "equal to or less than" per DEC-035.A cl.2).
- **GM Fiat is the universal override** (DEC-035.A cl.6) — but GM Fiat is **not** used by the
  executor in this automated test; the executor applies Skill-Tier basis only.
- **Quality gates nothing on severity** — only S-1 tie-breaking (DEC-013) and the success
  precondition (>= 1 floor). Default Wound Tier = causing skill's Skill-Tier ("equal"). A lesser
  tier requires Player choice + GM Fiat (not used here).
- **Therefore:** the Ice Troll's Tier-2 attacks yield **Tier-2 Effects / Tier-2 Wounds (Magnitude
  -2)**. Adventurer-1's Tier-2 Attack2/Defence2 likewise yield **Tier-2** Effects (capable of
  Skill-Tier >= 2 gated Effects per DEC-041).

### DEC-102 — Wound target selection

When a Wound is applied, determine which Attribute or Skill it affects:

1. **Target type (Attribute vs Skill wound):** Creatures cause **Attribute** wounds only. Players
   may cause an Attribute or Skill wound (player choice). An **automated playtest Character is a
   creature** and can only cause Attribute wounds. Effect restrictions override.
2. **Attribute-wound target:** the affected Attribute is the **Body attribute associated with the
   Skill that caused the wound**. Multiple Body attributes present in the affecting Skill -> select
   **randomly** from the candidates (for creatures and automated playtest Characters).
3. **Mind-only affecting Skills:** cause **Mind attribute wounds**.
4. **Skill-wound target** (not used by creatures/automated, noted for completeness): the skill
   sharing the **most of the same Attributes**; highest value wins; random/choice on tie.
5. **Consequence semantics:** Attribute wounds reduce the base Attribute value and trigger
   **downstream recalculation of all Skill values and HP/MP/Energy Pools**, including Cap
   recalculations (DEC-004 live recalculation).

### DEC-100 — Location Tier-1 coarse zones

When a Location Index is warranted (Skill-Tier >= 2 producing roll, per DEC-041) and resolved at
Tier 1, the coarse zone is determined by the quartile split:

| Roll range | Zone |
|---|---|
| 1-25 | Legs |
| 26-50 | Torso |
| 51-75 | Arms |
| 76-100 | Head |

Fixed rule. (Zero-Step transformation per DEC-014; attack-side invocation per DEC-017 §14.7.)

### DEC-108 — HP recording (uncapped)

- **HP is UNCAPped.** HP may go **negative** and the **negative value persists** (no clamp, no
  floor). Record every HP-loss step at its raw arithmetic value.
- **DEC-052 preserved:** forced incapacitation triggers at HP = 0 (no roll); the record continues
  negative below 0. Log `"HP: 45 - 12 = 33"` etc. as raw arithmetic.
- **Post-incapacitation accrual:** further damage while incapacitated deepens the negative record;
  an incapacitated character is no longer a "nearest possible target" for NPCs/creatures; if all
  characters are incapacitated, combat ends.
- **Revival gate** (not tested in normal combat, noted for completeness): negative HP must be healed
  back to 0 before revival; the wound-healing revival path is retracted (DEC-108 cl.3).

---

## The Frightened Condition — RULED handling (DEC-094)

`Frightened` (DEC-079) is a fully defined **Condition**: global, `Tier-Y Frightened Value -Y` to all
Skills while the source remains perceivable, source-dependent termination. Magnitude follows DEC-079
(`Value Z = -Y`, same tier structure as Wounds; Skill-Tier >= 2 production gate per DEC-041). **No
independent magnitude architecture** (C-10 folded into DEC-094).

**The passive/aura trigger is RULED via DEC-094's scene-state Condition Clause**, reusing DEC-088's
grammar: `Scene State -> Condition Clause -> Frightened`. Declarative, not probabilistic; read-only
and stateless; no new roll, no new resource transaction.

**This test exercises the trigger (Tiwa's authorization):**

- Declare a **fear-source binding** for the Ice Troll (its `Appearance: Hideous` maps to the
  module's fear-inducing presence), active **from the start of combat while the Troll remains
  perceivable**.
- **Effect on Adventurer-1:** `Frightened` is active (Tier-1, Value -1), imposing **-1 to all of
  Adventurer-1's Skills** while the Troll remains perceivable.
- **Log it** as a Frightened Condition application with its source (scene-state binding) and its
  magnitude, distinct from any `Frightened` imposed via a won S-1 Effect.

Both pathways — (a) the **scene-state binding** (passive/aura) and (b) the **won S-1 Effect** (Troll
declares `Frightened` as a Condition-type Effect on a win) — are legal under the rulings and may both
occur. Log which pathway produced each application.

**Termination:** `Frightened` ends when the source is no longer perceivable (e.g., the Troll is
incapacitated per DEC-052), by a removal Effect, or by time.

---

## The Ice Troll's Multi-Attack — RULED handling (DEC-106)

The Ice Troll has two authored attack actions: **Sharktoothed Maw (Skill 75)** and **Icy Claws
(Skill 67)**, both Tier-2. Per **DEC-106**, in this automated test (no GM present):

- The Troll plays **both** attacks **on its own turn, back-to-back**, in **highest-applicable-Skill
  -> lowest** order: **Sharktoothed Maw first (75), then Icy Claws (67)** — every round.
- Each attack is its **own S-1 combat exchange** (DEC-105), with its own **mandatory** Defender
  Active Defense (playtest mode).
- Each attack is its **own Core Test** with its own **Energy cost** — the Troll may exhaust its
  PE pool via its own multi-attacks (self-Overflow per DEC-007).
- **Targeting:** each attack targets the nearest possible target. Single PC: Adventurer-1 is the
  only target; always in reach (both attacks Reach C,1; this test runs in melee range). No AoE.

**Governance note:** This is a **Ruled** procedure (DEC-106), not a scaffold. It must NOT be logged
as scaffold. It is the direct Design Override of DEC-095 Step 3 for creatures/NPCs.

---

## Ruled procedures summary table (apply literally)

| Stage | Rule | Reference |
|---|---|---|
| Initiative / turn order | Highest Speed first; ties reroll; one turn per round | DEC-095 |
| Creature multi-action | Both attacks back-to-back, highest-Skill -> lowest, own turn | DEC-106 |
| Exchange | One S-1 opposed contest; both always roll | DEC-105 |
| Attacker win -> HP | Inflict Injury = Winner Margin - Defender Margin (never 0) | DEC-104 |
| Attacker win -> Effect | Active Defense mandatory; skill-tier shred + margin de-escalation | DEC-103 |
| Defender win | Attack fails; no counter-Effect | DEC-101 |
| Effect-tier/Wound-tier | = Skill-Tier of causing skill; mag = -tier | DEC-107 |
| Wound target | Attribute wound; Body attribute of causing skill; random for creatures/automated | DEC-102 |
| Location | Quartile split (1-25 Legs, 26-50 Torso, 51-75 Arms, 76-100 Head) | DEC-100 |
| HP record | Uncapped; negative persists; incapacitation at 0 | DEC-108 / DEC-052 |
| Frightened | Scene-state Condition Clause; -1 to all PC skills | DEC-094 |
| Defense mode | Mandatory (playtest) | DEC-105 |
| Defensive skill | Brawling (no authored defense skill) | DEC-098 |

---

## v5-Specific Execution Requirements

### Mandatory Wound-consequence chain exercise (DEC-107 + DEC-102)

This playtest **must** exercise the **full Wound-consequence chain at least once** — the exact chain
v4 could not complete:

```
Attack -> Defense -> Win -> Effect Tier (Skill-Tier basis, DEC-107)
-> Effect -> Location (DEC-100) -> Wound application (DEC-102 target selection)
-> Attribute reduction -> downstream recalculation
```

If no natural Troll attack win produces a selectable Effect by Round 5, log a note. If none by Round
10, **stop and flag Tiwa**. When the Wound chain triggers, log the **full** sequence: Effect Tier ->
Location Index -> Zone -> Wound Tier -> Wound target (which Attribute, and the random selection from
candidates if multiple) -> resulting Attribute value -> recalculated Skill Caps/values -> recalculated
HP/MP/Energy maxima (DEC-102 cl.5).

### Mandatory Active Defense vs Effect exercise (DEC-103)

Every attacker-win that produces a Wound/Condition Effect must run the **DEC-103 two-step** (Skill-Tier
shred + margin de-escalation). Log Magnitude before/after each step and the surviving native record
(`Location X Tier-Y <Effect> Z`). Track whether any Effect is carried to a lower tier or negated.

### Mandatory Inflict Injury contest-delta exercise (DEC-104)

Every attacker-win that selects the Base-tier `Inflict Injury` (HP) Effect must log:
Winner's Margin, Defender's Margin (if any successful AD), and the resulting contest-delta HP damage.
Confirm the "never 0 on a win" property.

### Output Format (mandatory — retained from v4, updated for the new rulings)

**The executing LLM MUST comply with every field listed below.**

#### 1. Live Combat Log — updated field set

| Field | Description |
|---|---|
| Round | Round number |
| Turn | Who is acting (Troll or PC) |
| Exchange | Which attack/exchange number on this turn (1st/2nd for the Troll's multi-attack) |
| Step | Core Test step (Attack/Defense/Active Defense/Repeat) |
| Actor | Who is rolling |
| Skill Used | Name and current effective value (including Frightened penalty and Wound recalculations) |
| d100 Roll | Raw d100 result |
| Success/Fail | d100 <= effective Skill? |
| Margin | Skill - d100 (success); 0 (failure) |
| Quality | Margin (success); 0 (failure) |
| Cost | d100 roll value (Track A cost per DEC-006) |
| PE Before | PE before Cost |
| PE After Cost | PE after Cost |
| Overflow | PE overflow = Cost - PE Before (if positive; else 0) |
| HP Overflow Damage | HP damage from Overflow (if any) |
| Recovery | Recovered this step (Regen/2, clamped) |
| PE Final | PE after Recovery (clamped to max) |
| Effect Selected | Effect on win + Effect Tier (Skill-Tier basis, DEC-107) |
| Location Index | Zero-Step-derived Location Index (if warranted) |
| Location Zone | Quartile zone (DEC-100) |
| Wound Tier / Magnitude | Skill-Tier basis (DEC-107); Magnitude = -tier |
| Wound Target | Attribute selected (DEC-102); random source/candidates noted |
| Attr/Skill recalcs | Recalculated Skill values + HP/MP/Energy maxima after an Attribute wound |
| AD Roll | Active Defense roll + Skill + result |
| AD Mitigation (Step 1/2) | Skill-Tier shred then margin de-escalation (DEC-103); or contest-delta for HP (DEC-104) |
| Net HP Change | HP change, raw arithmetic (DEC-108; may be negative) |
| Condition Applied | Any Condition (e.g., Frightened) with source pathway |

**Additional mandatory log entries:**
- **Turn order each round:** Speed values for both combatants.
- **Scaffold flags:** One-line flag on any scaffold usage (DEC-012 exception only in this prompt).
- **Ruled-procedure flags:** One-line note when a Ruled procedure is applied for the first time
  (DEC-105 exchange, DEC-103 shred, DEC-102 target, DEC-104 delta, DEC-106 multi-attack, DEC-107
  tier).
- **GM stops:** Verbatim recording of any GM-required stop with reason.
- **Edge cases:** Explicit documentation of any edge case (e.g., Margin-0 no-Effect per DEC-031 floor
  >= 1; Exact-tie Repeat; Both-fail Repeat).
- **Core Test count:** Running total.
- **Repeat count:** Each repeat gets its own Core Test table row.

#### 2. Final Report

Markdown. Must open with this exact provenance block, with the executing LLM's own name/version
substituted:

```yaml
provenance:
  author_llm: {name: "<executing LLM name>", version: "<executing LLM version>"}
  assessor_llm: []
  last_modified_by_llm: {name: "<executing LLM name>", version: "<executing LLM version>"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
rng_method: "<describe roll source>"
computation_method: "<describe computation approach>"
engine_runtime: "<wall-clock time from combat start to final report completion>"
```

**Structure (required sections in order):**
1. **Purpose/Scope** — what this test validates
2. **Character & Opponent summary** — stat blocks summary with key values
3. **DEC-012 exception provenance note** (verbatim, see below)
4. **Rulings Applied** — which DEC-094...DEC-110 were exercised, with observed behavior
5. **Ruled-Procedure Confirmations** — DEC-105 exchange, DEC-103 shred, DEC-104 delta, DEC-102
   target, DEC-106 multi-attack, DEC-107 tier, DEC-108 HP record
6. **Scaffold Values Used** — collated (DEC-012 exception only, unless a residual magnitude gap
   required a flagged scaffold)
7. **Round-by-round summary table**
8. **Wound-consequence chain record** — the full chain (see mandatory exercise) if triggered
9. **Systems Confirmed Working**
10. **Systems That Failed/Gapped**
11. **Edge Cases Observed**
12. **Coverage Matrix**
13. **Total Core Tests** — count and breakdown
14. **Total real-time and round-count duration**
15. **GM-Required Moments** — verbatim, with reasons
16. **Lessons for Future Playtests**
17. **Conclusion**

No mechanics ruled, promoted, or invented as canon anywhere in the report.

**Required DEC-012 provenance note (verbatim, place under Character description and reiterate in
Conclusion):**

> **Provenance of the DEC-012 exception:** the two pre-built Tier-2 skills on Adventurer-1 (Attack2,
> Defence2) were granted under a **prompt-level scaffold** (Tiwa's authorization, 2026-09-04) for
> this playtest only. They are **NOT backed by a PC-scoped register ruling.** DEC-087 authorizes
> pre-authored Tier-2 skills only for creature/NPC templates and preserves DEC-012's failed-Double
> origin for player-character skill advancement generally. Therefore: this exception is
> **non-register-backed**, creates **no new precedent**, grants the PC **no canonical authority**
> from these skills, and must **not** be cited in any future DEC or proposal as evidence that PCs can
> receive pre-authored Tier-2 skills outside DEC-012.

#### 3. Structured JSON Output

After the final report, produce a **structured JSON data file** containing:
- Pre-combat state (both combatants' HP, PE, Skills, Speed)
- Round-by-round results array (each round, each exchange, with both combatants' rolls, margins,
  costs, overflows, recoveries, HP changes, PE changes, Wound/Effect applications)
- Post-combat state (final HP, PE, Skills for both combatants, and any Attribute-wound recalculations)
- Total Core Tests count
- Total rounds
- Scaffold usage flags
- Ruled-procedure flags
- Edge cases array

This JSON is for programmatic audit and cross-model synthesis. It must contain enough data to
reconstruct the combat result without referring to the narrative log.

---

## Mandatory Computation and Documentation Standards

- **RNG Method Disclosure:** state RNG source before any roll in the pre-combat declaration.
- **Computation Method:** state whether rolls/arithmetic are (a) computed externally (preferred) or
  (b) computed by the LLM; disclose accordingly.
- **PE Path Tracking:** every PE-affecting step shows PE before -> PE after Cost -> Overflow -> PE
  after Recovery -> PE final (clamped).
- **Repeat Handling:** each Repeat gets its own Core Test table row.
- **Edge Case Documentation:** explicitly document any edge case encountered.
- **Runtime Documentation:** record wall-clock time from combat start to final report completion.
- **Total Core Test Count:** maintain a running count; report total and breakdown (Attack, Defense,
  Active Defense, Repeat).

---

## What this test now validates (vs. v4)

The core purpose of v5 is to confirm that the following resolve **deterministically under Ruled
mechanics, with NO scaffold invention**, and — critically — **identically across independent
executors**:

- **Standardized melee-exchange algorithm (DEC-105)** — both participants always roll; the four-case
  matrix. This is the comparability fix v4 lacked.
- **Inflict Injury contest-delta (DEC-104)** — Winner's Margin - Defender's Margin, never 0.
- **Active Defense vs Effect (DEC-103)** — Skill-Tier shred + margin de-escalation; Effects only.
- **Wound-consequence chain (DEC-107 -> DEC-102)** — Wound Tier = Skill-Tier; Attribute target
  selection; downstream recalculation. First full end-to-end completion.
- **Wound/Effect Tier = Skill-Tier (DEC-107)** — the v4 scaffold Quality->Tier table is gone.
- **Creature multi-attack (DEC-106)** — both attacks back-to-back, highest-Skill -> lowest.
- **HP uncapped record (DEC-108)** — negative values persist; incapacitation at 0.
- **Combat sequencing (DEC-095)** — turn order, one-turn, Speed-based ordering, tie reroll.
- **Location quartile zones (DEC-100)**.
- **Defender-wins = no counter-Effect (DEC-101, coverage closed DEC-109)**.
- **Brawling as creature default defensive skill (DEC-098)**.
- **Passive Frightened via scene-state Condition Clause (DEC-094)**.

**The only allowed scaffold is the DEC-012 exception.** If you encounter a genuinely open gap not
listed above, you may either (a) log a clearly-flagged non-canonical scaffold for **pure numeric
magnitude-type gaps only** and continue, or (b) **stop and flag Tiwa** for any genuine
subjective/narrative judgment call. Prefer stopping when in doubt for anything that is not a pure
numeric magnitude.

---

## Flagged Content Decision (raise to Tiwa, do not self-resolve)

The following is a **content-authoring decision that the executor must NOT self-resolve**:

- **Ice Troll Wound-capability ceiling (DEC-107/DEC-110):** under DEC-107, the Ice Troll's Tier-2
  attacks cap at Tier-2 Wounds (Magnitude -2), and Wound-capability beyond that requires a higher
  Skill-Tier attack or GM Fiat. The v4 stat block's Tier-2 attacks are preserved verbatim here, so
  this test runs at the Tier-2 Wound ceiling. **If Tiwa wants Tier-3/4 Wound output exercised**
  (e.g., to stress-test Attribute-wound recalculation severity), he must authorize a higher Skill-Tier
  attack or a Wound-tier GM-Fiat override **before** execution. Do not invent that content.

- **Regeneration/Regrowth (DEC-110):** if Tiwa chooses to exercise the Ice Troll's freezing
  regeneration, its heal value/cadence is **authored content per creature** (DEC-110) — a Tiwa content
  decision, not a rule. It remains **inactive** here (no `env:freezing` scene state declared). Do not
  invent a magnitude.

---

## Mandatory scaffold / Ruled logging

- **Scaffold values** (DEC-012 exception; any residual magnitude-type gap) must be flagged as
  non-canonical in the live log at the moment of use, collated in a dedicated "Scaffold Values Used"
  report section, never assigned a DEC number, never claimed as Ruled/Locked.
- **Ruled procedures** (DEC-102...DEC-110) are applied literally and logged as Ruled — they must
  NOT be marked as scaffold.

## Mandatory GM-stop logging

Every genuine GM-required stop must be recorded verbatim in both the live log and the final report's
"GM-Required Moments" section, each with its reason.

## Success criteria

- Combat runs to an actual conclusion (HP = 0 -> DEC-052 incapacitation, or all combatants
  incapacitated -> combat ends per DEC-108, or explicit abort) without silently skipping or softening
  any rule.
- **The standardized exchange (DEC-105), the contest-delta (DEC-104), the Effect shred (DEC-103),
  the Wound chain (DEC-107/DEC-102), the creature multi-attack (DEC-106), and the HP record
  (DEC-108) all resolve deterministically — no scaffold invention for any of these.**
- **The Wound-consequence chain is exercised at least once** (mandatory).
- **HP is recorded uncapped / negative-persist** per DEC-108, consistently.
- Attack selection follows DEC-106 (both attacks, highest-Skill -> lowest, back-to-back) and is logged
  as Ruled (not scaffold).
- Every residual scaffold value and every GM-required stop is distinguishable at a glance — nothing
  canonical-looking sneaks in.
- All output format fields are populated.
- RNG and computation methods disclosed.
- Total Core Tests counted and reported.
- Edge cases explicitly documented.
- Structured JSON output produced.
- The report is self-contained and precisely sourced enough for OpenCode to use it cold to identify
  concrete follow-up DEC candidates and confirm the ruling set behaved as intended.

## Constraints

- Never assign a DEC number. Never claim Ruled/Locked status for a scaffold value.
- No simplification of any core subsystem (see Derivation discipline).
- Do not invent new attributes, skills, Tags, or Conditions beyond what's Ruled or explicitly
  scaffolded here.
- Tables for all stat blocks and roll sequences; no narrative flavor beyond the one-line color needed
  to log an Effect.
- A Frightened application must cite its source pathway (scene-state binding vs won S-1 Effect); do
  not conflate the two.
- Do not deviate from DEC-106 multi-attack (both attacks, highest-Skill -> lowest, back-to-back). If
  a deviation is necessary, stop and flag Tiwa.
- Do not skip the Wound-consequence chain exercise. If no natural Effect-producing win by Round 10,
  stop and flag Tiwa.
- Do not omit any output format field.
- Do not use LLM arithmetic without disclosing it.
- Do not self-resolve the Flagged Content Decision (Ice Troll Wound ceiling / Regeneration) — those
  are Tiwa's.

---

## Post-Playtest Report Writing Instructions

**DO NOT EXECUTE THESE INSTRUCTIONS DURING THE PLAYTEST.** These instructions are for use AFTER the
combat playtest is complete. When the playtest concludes (one combatant is incapacitated, all
combatants are incapacitated, or the test is aborted), follow these steps:

1. **Produce the Final Report** per the Output Format section.
2. **Produce the Structured JSON Output** per the Output Format section.
3. **After completing both outputs**, ask the human monitor (Tiwa):

> **"The playtest is complete. The live combat log, final report, and structured JSON output have
> been produced. Are you ready for me to write the full comprehensive playtest report?"**

4. **Wait for Tiwa's response.** If Tiwa says yes, proceed to write the full comprehensive report
   following the report structure defined in the Output Format section. If Tiwa says no or provides
   additional instructions, follow those instead.

**What the comprehensive report must include (when requested):**
- All sections listed in the Output Format section.
- A **declarative comparison across the three v4 run operationalizations** — explicitly confirming
  that v5's codified exchange (DEC-105), contest-delta (DEC-104), and Effect shred (DEC-103) remove
  the three divergent Wound-consequence interpretations that made v4 runs non-comparable.
- Cross-reference against the v4 synthesis findings: note which OI items are now Ruled-closed
  (OI-101/102/103/104/105/106/107) and how they behaved in-run.
- All scaffold values used with their justifications.
- All GM-required moments with verbatim recordings.
- All edge cases observed with their rule confirmations.
- The structured JSON output as an appendix or separate artifact.
- A "Lessons for Future Playtests" section.

**The comprehensive report must not:**
- Assign DEC numbers.
- Claim any scaffold value is canonical.
- Modify the decision register or any governance document.
- Promote, demote, or alter the authority of any existing ruling.
- Invent new mechanics or rules.

---

## Document Status

**Status:** Playtest execution prompt — not canonical
**Authority:** Advisory — makes no rulings, assigns no DEC numbers
**Next action:** Tiwa resolves the Flagged Content Decision (Ice Troll Wound ceiling / Regeneration
authorization, if desired); then execute the playtest; produce live log, final report, and JSON
output; ask Tiwa if ready for comprehensive report
**Canonical rule change:** None
**Supersedes:** v4 prompt (tiwas-ice-troll-combat-playtest-prompt-v4-2026-09-04.md)
