---
document:
  title: "Quality → Wound Tier Resolution Design Ruling (OI-106) — Skill-Tier basis; Design Override"
  version: "1.0"
  status: "Advisory recording of a designer ruling. Non-canonical. Assigns DEC-107 in the decision register."
provenance:
  author_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
  ruling_origin: "Human designer (Tiwa), in-session ruling, 2026-09-05, resolving open item OI-106 (Quality→Wound Tier) carried over as v3 OI-001"
  recorded_in: "_consolidation/decision-register.md DEC-107"
---

# Quality → Wound Tier Resolution Design Ruling (OI-106) — Skill-Tier basis

## 1. Purpose

This document records Tiwa's designer ruling resolving **OI-106** — the Quality → Wound
Tier numeric table question. OI-106 was carried over from the v3 Ice Troll Combat Playtest
(v3 OI-001, 2026-09-04) and scaffolded in v4 with a numeric table (`Q1–9=T1, Q10–19=T2,
Q20–29=T3, Q30+=T4`) across 76 Wound exercises.

The ruling **supersedes the Quality-gating architecture** (DEC-035.B Quality hard ceiling;
DEC-099 Quality thresholds; DEC-031 Quality-gating clause) and establishes the **Skill-Tier
basis**: Effect Tier = the Skill-Tier of the skill used, Effect Magnitude = Effect Tier,
Wound Tier = Effect Tier.

**Authority status:** Non-canonical designer ruling (real decision; promotion requires the
8-step Promotion Rule, REQ-021 / Proposals/WIP §21). This ruling is a **Design Override**
over DEC-035.B/DEC-099 (and DEC-031's gating clause): the original register text of those
decisions is preserved and annotated in-place.

## 2. Open item resolved

| ID | Issue | Source |
|---|---|---|
| OI-106 | Quality → Wound Tier numeric conversion | v3 Cross-Report Synthesis (2026-09-04) §6.1 (Claude finding) as v3 OI-001; v4 Cross-Report Synthesis (2026-09-05) OI-106 |

## 3. The ruling — verbatim (Tiwa, 2026-09-05)

> **RULING:**
>
> "Effect Tier = the Skill-Tier of the skill used; Effect Magnitude = Effect Tier; Wound
> Tier = Effect Tier (max; 'equal to or less than' per DEC-035.A cl.2); GM Fiat remains the
> universal override. Quality retains no numeric gating role for effect/wound severity."
>
> **Reason:** "Original DEC-035.B & DEC-099 were only ruled on to get through the
> playtests."
>
> **Correcting the earlier GM Fiat characterisation:** "GM Fiat can add complications, but
> decisions made in the game by players and automated actions by NPC's are the main causes
> for drama. GM Fiat is intended to enhance drama." — the Skill-Tier mechanic is **not**
> "advisory in practice"; player decisions and automated NPC actions carry the drama, GM Fiat
> enhances it.

## 4. Clarifications — verbatim (Tiwa, 2026-09-05)

On Quality's role:

> "Quality was used to actually get the Effect to be caused as the roll is a Contest. Quality
> used in S-1 tie-breaking (DEC-013). Winner able to select any Effect their Skill Tier and
> Skill permits."

On the default tier / lesser Effect:

> "equal to Skill Tier by default. 'Equal to or less than' is added if a Player character
> wanted to inflict a lesser Effect, maybe to prevent the death of the target but that would
> require GM Fiat."

On v4 data handling:

> "annotated as scaffold-invalid, add why and the date. We will have to alter create
> statblocks for future playtests but that is why we are having playtests."

On the three coverage points (confirmed in-session): **(1)** HP channel unchanged — Inflict
Injury remains contest-delta, DEC-104. **(2)** DEC-031 floor retained — a winning contest
always yields at least one Effect the winner's Skill Tier and Skill permit; Quality requires
success and breaks ties, with no numeric threshold anywhere. **(3)** DEC-107 assigned as next
ID; register annotations approved (status-note only, original text preserved) on DEC-031,
DEC-035.B, DEC-099, plus a light note on DEC-035.A cl.2 (default-equal refinement).

## 5. Structured restatement (for execution)

### 5.1 Effect Tier / Magnitude / Wound Tier all derive from Skill-Tier

- **Effect Tier = Skill-Tier of the skill used** (consistent with DEC-103's
  `Y = Attack Skill Tier`).
- **Effect Magnitude = Effect Tier** (Wound/Condition magnitude `Z = −Y` per DEC-035.A cl.3
  and DEC-079 C2).
- **Wound Tier = Effect Tier by default.** "Equal to or less than" (DEC-035.A cl.2) applies
  only when a **Player** chooses a lesser Effect (e.g., to spare a target's life), and that
  lesser tier still requires **GM Fiat**. Creatures/automated NPC actions run at
  **equal to** their Skill-Tier as the default.
- **GM Fiat remains the universal override** (DEC-035.A cl.6; pending the separate future
  ruling on GM Fiat universality).

### 5.2 Quality's role

- **S-1 tie-breaking** (DEC-013) — unchanged.
- **Success precondition** — Quality ≥ 1 (a success) is required to cause an Effect at all;
  the consistent floor from DEC-031/DEC-099 ("a winning contest always yields at least one
  Effect the winner's Skill Tier and Skill permits") is retained.
- **No numeric gating role** for effect/wound severity. No Quality → Tier table.

### 5.3 Selectable Effects

The winner of the contest may select **any Effect their Skill Tier and Skill permit**
(DEC-023.A gated-tier content enumeration; per-Skill capability via the Skill's authored
Effects). Skill-Tier retains its **production-gate function** (DEC-041: Skill-Tier ≥ 2
required to generate a Location Index / Wound at all).

### 5.4 Superseded materials

- **DEC-035.B** (Quality × Skill-Tier ceiling precedence): superseded — Quality is no longer
  a hard ceiling on Wound Tier; Skill-Tier is the ceiling.
- **DEC-099** (Quality-gated tier threshold ≥1/≥10): superseded — no numeric Quality
  thresholds gate Effect/Wound severity.
- **DEC-031** (S-3 Quality's role): the Quality-gating clause is superseded; Quality retains
  tie-break + success-precondition functions and the ≥ 1 floor; Effect selection is
  Skill-Tier/Skill-based.
- **v4 scaffold table** (`Q1–9=T1 … Q30+=T4`): invalidated as scaffold artifact (see §5.5).

### 5.5 v4 data status

The v4 Wound Tier records produced under the scaffold table — including the **51 Tier-4
records generated from the Ice Troll's Skill-Tier-2 attacks** — are **scaffold-invalid** for
Wound Tier purposes: they were produced by a non-canonical numeric scaffold that the 2026-09-05
Skill-Tier ruling supersedes. Annotated with why and the date in the v4 Cross-Report
Synthesis. Future playtest statblocks must author Skill-Tiers consistent with this rule
(e.g., a Tier-4 Wound requires a Skill-Tier-4 attack, or GM Fiat).

## 6. Register entry

Recorded in `_consolidation/decision-register.md` (Section B, Non-canonical designer ruling):

| ID | Subject | Status |
|---|---|---|
| DEC-107 | Quality→Wound Tier: Skill-Tier basis; Design Override of DEC-035.B/DEC-099/DEC-031 gating | Ruled (non-canonical) |

Register annotations applied in-place (original text preserved): DEC-031 (gating clause
superseded), DEC-035.B (superseded by DEC-107), DEC-099 (superseded by DEC-107), DEC-035.A
(light note: default-equal refinement for Wound Tier).

## 7. Status

**Status:** Advisory recording — not canonical
**Authority:** Non-canonical designer ruling (real decision; promotion requires the
8-step Promotion Rule)
**Assigns:** DEC-107 (next sequential ID after DEC-106)
**Resolves:** OI-106 (Quality → Wound Tier conversion) — closed as **not-a-gap** under the
Skill-Tier basis
**Overrides:** DEC-035.B, DEC-099, DEC-031's Quality-gating clause
**Preserves:** DEC-035.A cl.2/cl.3 (max = causing skill's Tier; magnitude Z = −Y), DEC-035.A
cl.6 (GM Fiat universal override; pending universal-GM-Fiat ruling), DEC-041 (Skill-Tier ≥ 2
production gate), DEC-013 (Quality tie-break), DEC-024 (one Effect per win), DEC-079 (C2/C3;
conditions magnitude = −Y), DEC-085/DEC-087 (creature Tier-2+ pre-authored skills),
DEC-103 (Skill-Tier base Effect), DEC-104 (HP contest-delta — unchanged)
**Leaves open:** OI-104 (DEC-101 coverage), OI-107 (HP floor convention), GM Fiat
universality, Effect selection per-Skill enumeration (content-authoring)
**Canonical rule change:** None