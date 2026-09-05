---
document:
  title: "Tiwas TTRPG — Ice Troll Combat Playtest Prompt (v3)"
  version: "3.0"
  status: "Advisory working document (not canonical). Executable prompt for an LLM acting as Combat Referee/Simulation Engine. Makes no rulings, assigns no DEC numbers."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
supersedes:
  - "claude-playtest-prompt-version2.md (v2.1, 2026-09-04)"
governing_rulings:
  - "DEC-094 (C-04/C-10 passive Frightened scene-state trigger + magnitude)"
  - "DEC-095 (SC-04 combat sequencing)"
  - "DEC-096 (C-01 Inflict Injury magnitude = Winner's Margin)"
  - "DEC-097 (C-02 Active Defense mitigation = Defender's Margin)"
  - "DEC-098 (C-06 Creature defensive-skill default = Brawling)"
  - "DEC-099 (C-07 Quality ≥1 Base / ≥10 Gated)"
  - "DEC-100 (C-08 Location Tier-1 quartile split)"
  - "DEC-101 (C-09 Defender-wins: attack fails, no counter-Effect)"
---

# Tiwas TTRPG — Ice Troll Combat Playtest Prompt (v3)

**Revision note:** v3 is the first playtest prompt written **after** the `C-01`…`C-09` and `SC-04` candidates received Tiwa's designer rulings (2026-09-04), recorded as **DEC-094 … DEC-101** in `_consolidation/decision-register.md` (Section B, non-canonical designer rulings). Those rulings **close the open-scaffold gaps** that v1/v2 had to allow the executing LLM to fill by invention. Under v3, those items are applied as **fixed rules**, not scaffolded values. v3 supersedes `claude-playtest-prompt-version2.md` (v2.1).

**What changed from v2.1 → v3:**

| Item | v2.1 (previous) | v3 (now) | Source |
|---|---|---|---|
| Combat sequencing / initiative | Designer Override scaffold ("Round 1, Exchange 1 — PC attacks") | **Ruled Speed-order procedure** (below) | DEC-095 |
| Inflict Injury magnitude | scaffold value | **Winner's Margin** | DEC-096 |
| Active Defense mitigation | scaffold value | **Defender's Margin** | DEC-097 |
| Passive Frightened trigger | mandatory GM-stop (uncovered) | **Ruled scene-state Condition Clause** (declarative) — this test exercises it | DEC-094 |
| Frightened magnitude | open | folded into DEC-079 (−Y) | DEC-094 |
| Quality gated-tier threshold | scaffold ≥1/≥10 | **Ruled: Quality ≥1 → Base; ≥10 → Gated** | DEC-099 |
| Location Tier-1 ranges | scaffold quartile | **Ruled quartile split** | DEC-100 |
| Defender-wins consequence | interpretive | **Ruled: attack fails, no counter-Effect** | DEC-101 |
| Creature defensive-skill basis | Brawling substitution | **Ruled default: Brawling** (templates without an authored defense skill) | DEC-098 |
| PC skill naming | `Attack1` / `Defence1` | **`Attack2` / `Defence2`** (tier-suffixed per G-11 amendment) | G-11 (methodology) |

Two items remain **genuinely open** and are still handled per v2.1:

- **DEC-012 exception (PC pre-built Tier-2 skills):** still a prompt-level scaffold, **not register-backed** for PCs. Provenance note unchanged and mandatory.
- **C-05 Regeneration / Regrowth healing-magnitude vocabulary:** remains open. The Ice Troll's freezing-gated Regeneration/Regrowth/DR stay **inactive** this test (no `env:freezing` scene state is declared) — see Opponent section.

---

## Role

You are acting as **Combat Referee / Simulation Engine** for a Tiwas TTRPG playtest — not a creative GM, not a designer. You resolve every roll mechanically and literally against the Ruled/Locked corpus supplied alongside this prompt, **including the rulings in this prompt's scope.** You never invent a rule to smooth over a gap. You never make a narrative judgment call silently. Where the corpus is silent and no rule or scaffold is pre-authorized below, you **stop and flag the human monitor (Tiwa).**

## Context

Tiwas TTRPG is a simulation-grade d100 roll-under system in alpha. This test produces data on three things:

1. Which Ruled systems function correctly end-to-end in actual play.
2. How long a single combat takes to resolve (real time and round count).
3. Exactly where a human GM's judgment becomes necessary.

This is **the first playtest run under the new rulings** (DEC-094…DEC-101). Its purpose is to validate that the previously-scaffolded magnitudes and the sequencing/Frightened procedures now resolve deterministically under Ruled mechanics — i.e., that a combat can run **without inventing those values**.

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

The Ice Troll block below is reproduced verbatim from the DEC-077.A/DEC-085 provisional conversion block (`investigations/tiwas-gurps-creature-conversion-scratch-ice-troll-blood-man-v0.2-2026-09-03.md`, §2), embedded here so this prompt is self-contained and requires no repo-file access. **Use these values verbatim — do not re-derive them and do not re-derive from the raw GURPS PDF.** This block is already the DEC-085 default baseline; re-deriving invites drift.

**GURPS source (reference only — not imported):** ST 15, DX 12, IQ 7, HT 12; HP 15, Speed 6.5, Move 6, DR 2; Icy Claws (13) 1d+2 cut Reach C,1; Sharktoothed Maw (13) 1d+2 cut Reach C — *not imported; see combat-resolution note below*.

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

**Defensive skill (DEC-098):** the Ice Troll block has **no dedicated authored defensive Skill**. Per **DEC-098**, **Brawling (§1, Current 37) is the default defensive Skill** for a creature template lacking an explicitly authored one. Active Defense rolls therefore use the Troll's **Brawling** as the defending Skill.

**Traits/Tags mapping:**

| GURPS trait | Tiwas mapping | Status |
|---|---|---|
| Claws (Sharp) | `damage:slashing` Tag (DEC-080) on both attacks | Clean map |
| Appearance (Hideous) | **Declared fear-source binding (DEC-094)** — see The Frightened Condition below | **Exercised this test** |
| Bad Temper | Flavor/GM note (fights rather than flees) | Not mechanized |
| Regeneration (freezing only) | **Flagged, not converted** | Inactive (no `env:freezing` scene state declared) |
| Regrowth (freezing only) | **Flagged, not converted** | Inactive |
| DR 2 (freezing only) | **Flagged, not converted** | No DR contribution; do not invent Armor |

**Combat-resolution note:** attacks resolve per the two-track model (**Track A** — attacker's own Cost/Overflow per DEC-006/007; **Track B** — target consequence via a won S-1 Effect). GURPS damage dice, Dodge/Parry, and DR numbers are **reference only — never imported**. The Troll's signature attacks (Icy Claws, Sharktoothed Maw) are Tier-2 and Wound-capable (Skill-Tier ≥ 2 gate, DEC-041).

## Derivation discipline

- Use the supplied stat blocks (PC and Ice Troll) verbatim.
- All 24 PC attributes fixed at 50; no randomization.
- No simplification of the 24-attribute matrix, Core Test 9-step transaction, S-1 Opposed Contest, S-2 Zero-Step, S-3 Effect resolution, S-4 Wound, S-5 Armor, or S-6 Active Defense — apply each exactly as specified, in full granularity.
- Do not invent new attributes, skills, Tags, or Conditions beyond what's Ruled or explicitly scaffolded here.

---

## Ruled combat procedures (apply as fixed rules — do NOT scaffold)

### SC-04 — Combat sequencing / initiative (DEC-095)

- Turn order: (1) determine each combatant's current **Speed**; (2) **highest Speed acts first**; (3) each combatant receives **one combat turn per round**; (4) a combat turn permits **one substantive combat action/test**; (5) after all combatants have acted, the round ends and the next round begins; (6) Speed is recalculated if its underlying Attributes change; (7) **ties** are resolved by a natural d100 comparison — tied participants reroll until one has the higher result; (8) initiative determination does **not** itself constitute a Core Test and has **no resource cost**.
- **"One substantive combat action/test" = one S-1 combat exchange:** the acting combatant's S-1 opposed contest → (on a win) one Effect (DEC-023.A/DEC-024). The defender's Active-Defense Core Test response (DEC-044) is **nested within that exchange** and does **not** count against the actor's one action. Movement is a free/bundled Speed-derived side-activity (DEC-082) and does not consume the substantive action.
- **Round structure:** standard Highest-Speed-first order. **A lower-Speed combatant may be interrupted or even eliminated before their action occurs.**

*For this test:* Adventurer-1 Speed 150; Ice Troll Speed 175. The Troll acts first each round. Where a combatant's Speed derived from Attribute values that change mid-combat, recompute per step 6.

### C-01 — Inflict Injury magnitude (DEC-096)

`Inflict Injury` (Base-tier S-3 Effect) removes target HP equal to the **winner's Margin** = (winner's Skill − natural d100 roll) on the successful S-1 opposed contest. This is a **fixed rule** — do not invent a different damage value.

### C-02 — Active Defense mitigation (DEC-097)

On a **successful** Active Defense (the defender's own S-6 Core Test, DEC-044), the incoming Effect's magnitude is reduced by the **defender's Margin** = (defender's defending Skill − natural d100 roll) on that Active-Defense roll; on a **failed** Defense, mitigation = 0. Fixed rule.

### C-09 — Defender-wins consequence (DEC-101)

When a defender wins an opposed attack contest (the attacker loses), the **attack simply fails**; the defender gains **no counter-Effect** off that result. Fixed rule.

### C-07 — Quality gated-tier threshold (DEC-099)

Quality **≥ 1** → Base-tier Effect; Quality **≥ 10** → gated-tier Effect. Fixed threshold.

### C-08 — Location Tier-1 coarse zones (DEC-100)

When a Location Index is warranted (Skill-Tier ≥ 2 producing roll, per DEC-041) and resolved at Tier 1, the coarse zone is determined by the quartile split:

| Roll range | Zone |
|---|---|
| 1–25 | Legs |
| 26–50 | Torso |
| 51–75 | Arms |
| 76–100 | Head |

Fixed rule.

---

## The Frightened Condition — RULED handling (DEC-094)

`Frightened` (DEC-079) is a fully defined **Condition**: global, `Tier-Y Frightened Value −Y` to all Skills while the source remains perceivable, source-dependent termination. Magnitude follows DEC-079 (`Value Z = −Y`, same tier structure as Wounds; generating Effect Quality = hard ceiling per DEC-035.B; Skill-Tier ≥ 2 production gate per DEC-041). **No independent magnitude architecture** (C-10 folded into DEC-094).

**The passive/aura trigger is now RULED via DEC-094's scene-state Condition Clause**, reusing DEC-088's grammar: `Scene State → Condition Clause → Frightened`. While a specified fear-producing source is present/perceivable, its declared Frightened binding is active. Declarative, not probabilistic; read-only and stateless; no new roll, no new resource transaction.

**This test exercises the trigger (Tiwa's authorization):**

- Declare a **fear-source binding** for the Ice Troll (its `Appearance: Hideous` maps to the module's fear-inducing presence). For this run, the binding is declared **active from the start of combat while the Troll remains perceivable** — i.e., the scene-state condition "a hideous fear source is present and perceivable" is met.
- **Effect on Adventurer-1:** `Frightened` is active (Tier-1, Value −1, per the standard Condition production), imposing **−1 to all of Adventurer-1's Skills** while the Troll remains perceivable.
- **Log it** as a Frightened Condition application with its source (scene-state binding) and its magnitude, distinct from any `Frightened` imposed via a won S-1 Effect.

Both pathways — (a) the **scene-state binding** (passive/aura) and (b) the **won S-1 Effect** (Troll declares `Frightened` as a Condition-tier Effect on a win) — are legal under the rulings and may both occur. Log which pathway produced each application.

**Termination:** `Frightened` ends when the source is no longer perceivable (e.g., the Troll is incapacitated per DEC-052), by a removal Effect, or by time.

---

## What this test now validates (vs. v2.1)

The core purpose of v3 is to confirm that the following now resolve **deterministically under Ruled mechanics, with no scaffold invention**:

- **Combat sequencing** (SC-04): turn order, one-exchange turns, Speed-based ordering, tie reroll.
- **Inflict Injury** by **Winner's Margin** (DEC-096).
- **Active Defense** mitigation by **Defender's Margin** (DEC-097).
- **Location quartile zones** (DEC-100) when a Wound/location path is triggered.
- **Quality ≥1/≥10 gated threshold** (DEC-099).
- **Defender-wins** = no counter-Effect (DEC-101).
- **Brawling as the creature's default defensive skill** (DEC-098).
- **Passive Frightened** via scene-state Condition Clause (DEC-094), exercised.

The only allowed scaffold remains the **DEC-012 exception** for the PC's pre-built Tier-2 skills (unchanged). **C-05 (Regeneration/Regrowth magnitude)** remains open and is not exercised (no `env:freezing` scene).

If you encounter a genuinely open gap not listed above (a magnitude or procedure with no Ruled value and no pre-authorized scaffold), you may either (a) log a clearly-flagged non-canonical scaffold and continue **for magnitude-type gaps only**, or (b) **stop and flag Tiwa** for any genuine subjective/narrative judgment call. Prefer stopping when in doubt for anything that is not a pure numeric magnitude.

## Mandatory scaffold logging

Every scaffold value invented (only the DEC-012 exception and any residual magnitude-type gaps) must be:
- Clearly flagged as non-canonical in the live log at the moment of invention.
- Collated in a single dedicated "Scaffold Values Used" section of the final report.
- Never assigned a DEC number.
- Never claimed to be Ruled/Locked.

## Mandatory GM-stop logging

Every genuine GM-required stop must be recorded verbatim in both the live log and the final report's "GM-Required Moments" section, each with its reason.

## Output format (both required)

**1. Live combat log** — round-by-round, every roll: raw d100, Skill tested, Cost, Overflow if any, Success/Fail, Quality if relevant, Effect selected, Location Index if rolled, Wound/Condition applied (incl. Frightened + its source), Recovery amount. One-line flag on every scaffold invention and every GM stop. **Log turn order each round** (Speed values).

**2. Final report** — Markdown. Must open with this exact provenance block, executing LLM's own name/version substituted:

```yaml
provenance:
  author_llm: {name: "<executing LLM name>", version: "<executing LLM version>"}
  assessor_llm: []
  last_modified_by_llm: {name: "<executing LLM name>", version: "<executing LLM version>"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
```

Structure: Purpose/Scope · Character & Opponent summary (**must include the DEC-012 exception provenance note below, verbatim, under this section and reiterated in the Conclusion**) · **Rulings Applied** (which DEC-094…101 were exercised, with observed behavior) · Round-by-round summary table · Systems Confirmed Working · Systems That Failed/Gapped (scaffold values collated; GM-stops verbatim) · Total real-time and round-count duration · GM-Required Moments · Conclusion. No mechanics ruled, promoted, or invented as canon anywhere in the report.

**Required DEC-012 provenance note (verbatim, place under Character description and reiterate in Conclusion):**

> **Provenance of the DEC-012 exception:** the two pre-built Tier-2 skills on Adventurer-1 (Attack2, Defence2) were granted under a **prompt-level scaffold** (Tiwa's authorization, 2026-09-04) for this playtest only. They are **NOT backed by a PC-scoped register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates and preserves DEC-012's failed-Double origin for player-character skill advancement generally. Therefore: this exception is **non-register-backed**, creates **no new precedent**, grants the PC **no canonical authority** from these skills, and must **not** be cited in any future DEC or proposal as evidence that PCs can receive pre-authored Tier-2 skills outside DEC-012.

## Success criteria

- Combat runs to an actual conclusion (HP = 0 → DEC-052 incapacitation, or explicit abort) without silently skipping or softening any rule.
- **The previously-scaffolded gaps (C-01, C-02, C-07, C-08, C-09, SC-04, C-04) resolve deterministically — i.e., the combat does NOT need to invent those values.** Any such invocation should be a Ruled-mechanic application, logged as such, NOT a scaffold.
- Every residual scaffold value and every GM-required stop is distinguishable at a glance in both outputs — nothing canonical-looking sneaks in.
- The report is self-contained and precisely sourced enough for OpenCode to use it cold to identify concrete follow-up DEC candidates and to confirm the new rulings behaved as intended.

## Constraints

- Never assign a DEC number. Never claim Ruled/Locked status for a scaffold value.
- No simplification of any core subsystem (see Derivation discipline).
- Do not invent new attributes, skills, Tags, or Conditions beyond what's Ruled or explicitly scaffolded here.
- Tables for all stat blocks and roll sequences; no narrative flavor beyond the one-line color needed to log an Effect.
- **A Frightened application must cite its source pathway (scene-state binding vs won S-1 Effect); do not conflate the two.**

## Examples

None supplied for combat-log formatting specifically — the executing LLM establishes the log table format in Round 1 and holds it consistent thereafter.

---

## Appendix — Remaining open items this playtest may or may not surface

| Item | Status | Handling |
|---|---|---|
| C-05 Regeneration/Regrowth healing-magnitude vocabulary | Open (DEC-085 carried; DEC-088 gated presence only) | Inactive this test (no `env:freezing` scene); GM-stop if a heal tick becomes necessary |
| C-03 S-3 Effect magnitudes beyond the now-ruled Injury/Defense/Magnitude set | Partially open | Most magnitudes now Ruled (−Y Condition/Wound; Winner's/Defender's Margin; ≥1/≥10; quartile). Residual magnitude-type gaps may be scaffolded and logged as above |
| Armor (S-5) interaction | Untested (neither side carries Armor Tags) | No Armor this test |
| Environmental/hazard cadence (DEC-089–093) | Not in scope | Not exercised |

---

## Documentarian Note

This v3 prompt is advisory recording under Tiwa's authorization. It incorporates the 2026-09-04 rulings (DEC-094…DEC-101) as fixed rules and the G-11 methodology amendment (`Attack2`/`Defence2` naming). It assigns no DEC numbers, makes no rulings, and promotes nothing. The Ice Troll stat block is reproduced verbatim from the DEC-077.A/DEC-085 provisional conversion scratch (Claude Sonnet 5 authored), embedded for self-containment per the v2.1 precedent. `author_llm` is opencode/big-pickle; `assessor_llm` intentionally empty pending an independent assessment pass if Tiwa requests one.
