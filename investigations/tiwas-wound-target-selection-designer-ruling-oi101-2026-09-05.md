---
document:
  title: "Wound Target Selection Design Ruling (OI-101)"
  version: "1.0"
  status: "Advisory recording of a designer ruling. Non-canonical. Assigns DEC-102 in the decision register."
provenance:
  author_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
  ruling_origin: "Human designer (Tiwa), in-session ruling, 2026-09-05, resolving open item OI-101 (v4 Cross-Report Synthesis 2026-09-05)"
  recorded_in: "_consolidation/decision-register.md DEC-102"
```

# Wound Target Selection Design Ruling (OI-101)

## 1. Purpose

This document records Tiwa's designer ruling resolving **OI-101** — the Wound target
selection question raised by the v4 Ice Troll Combat Playtest Cross-Report Synthesis
(2026-09-05, §6.1 / §10 OI-101) and first escalated by GPT-5.6 Luna in the aborted v4
run ("which Attribute or Skill a Wound Tier at a location affects").

The ruling was given in-session and is recorded verbatim in §3 and §4. It is recorded
here as the auditable source for the corresponding decision-register entry (DEC-102).

**Authority status:** This is a non-canonical designer ruling. It does not itself make
anything Canonical. Any promotion to Canonical would require the full 8-step Promotion
Rule (REQ-021 / Proposals/WIP §21).

## 2. Open item resolved

| ID | Issue | Source |
|---|---|---|
| OI-101 | Which Attribute or Skill a Wound Tier at a location affects (Wound target selection); whether Attribute or Skill wounds may be caused, and by whom | v4 Cross-Report Synthesis (2026-09-05) §6.1, §10; GPT-5.6 Luna v4 Finding F-06 (Gap A) |

## 3. The ruling — verbatim (Tiwa, 2026-09-05)

> **OI-101**
>
> Attribute affected will be body attribute associated with the Skill which caused the
> wound. If multiple body attributes are present in the affecting Skill then:
>
> 1. for creatures, the Attribute affected will be Random selection from the body
>    attributes present in the affecting Skill.
> 2. Player can choose which Attribute is affected from the body attributes present in
>    the affecting skill.
> 3. If the Player is an automated playtest Character then, like creatures, the Attribute
>    affected will be Random selection from the body attributes present in the affecting
>    Skill.
>
> If a Skill is affected then:
>
> Skill affected will be a skill which shares the most of the same Attributes as
> affecting skill. If there is are multiple valid skills then a list of the valid
> affected skills is created:
>
> 1. for creatures, the Skill affected will be Random selection from the possible
>    affected Skill list.
> 2. Player can choose which Skill is affected from the possible affected Skill list.
> 3. If the Player is an automated playtest Character then, the Skill affected will be
>    Random selection from the possible affected Skill list.
>
> Wound target selection: Attribute or Skill?
>
> 1. Creatures can only cause Attribute wounds.
> 2. Players can choose an Attribute or Skill wound.
> 3. Player in Automated Playtest is treated as a creature and can only cause Attribute
>    wounds.
>
> Some attack effects will only cause Skill wounds or only cause Attribute wounds.

## 4. Clarifications — verbatim (Tiwa, 2026-09-05)

Reply to clarification questions asked by OpenCode before recording:

> 1. Skill affected will be the skill with the highest numerical value. If there is a
>    tie then a randomly selected Skill from the list of skills with the equally highest
>    numerical value will be affected.
> 2. Mind-only affecting Skills cause Mind attribute wounds. Some Mind-only affecting
>    Skills may be able to cause Body wounds. This skills will have this possible Effect
>    noted with the Skill.
> 3. Yes. [Effect restriction to Skill-wound-only / Attribute-wound-only overrides the
>    creator-type rule.]
> 4. Attribute wounds can cause a recalculation of all Skill values and HP MP Energy
>    Pools. It reduces the base value with downstream cap recalculations.

Tiwa additionally approved entering the ruling in the standard way and updating the
v4 Cross-Report Synthesis open-item table to mark OI-101 resolved-by-ruling.

## 5. Structured restatement (for execution)

### 5.1 Target type — Attribute wound or Skill wound

| Causer class | Allowed wound type |
|---|---|
| Creatures | Attribute wounds only |
| Players | Attribute or Skill wound (player choice) |
| Automated playtest Characters | Treated as creatures → Attribute wounds only |
| Any class, where the causing attack Effect is restricted | Effect restriction overrides the class rule (e.g., a Skill-wound-only or Attribute-wound-only attack Effect forces that target type) |

### 5.2 Attribute wound — target selection

- The affected Attribute is the **Body attribute associated with the Skill that caused
  the wound**.
- Mind-only affecting Skills cause **Mind attribute wounds** (Body wound capability, where
  a Mind-only Skill may cause Body wounds, is noted on that Skill as a possible Effect).
- Multiple candidate Attributes in the affecting Skill:
  - Creatures: random selection from the candidate Attributes.
  - Players: choice from the candidate Attributes.
  - Automated playtest Characters: random selection, like creatures.

### 5.3 Skill wound — target selection

- The affected Skill is the skill sharing the **most of the same Attributes** as the
  affecting Skill.
- Among the valid candidates, the **highest numerical value** skill is affected.
- On a tie of equally-highest values, a **random** selection from that equally-highest
  list (creatures and automated playtest Characters); a Player may choose from the valid
  list where the Player's own wound is a Skill wound.

### 5.4 Consequence semantics

- **Attribute wounds** reduce the base Attribute value and trigger downstream
  recalculation: all Skill values, HP, MP, and Energy Pools recompute from the modified
  base, including cap recalculations.

## 6. Register entry

Recorded in `_consolidation/decision-register.md` as **DEC-102** (Section B,
Non-canonical designer ruling):

| ID | Subject | Status |
|---|---|---|
| DEC-102 | S-4 Wound target selection (Attribute vs Skill) — resolves OI-101 | Ruled (non-canonical) |

## 7. Status

**Status:** Advisory recording — not canonical
**Authority:** Non-canonical designer ruling (real decision; promotion requires the
8-step Promotion Rule)
**Assigns:** DEC-102 (next sequential ID after DEC-101)
**Resolves:** OI-101 (Wound target selection)
**Leaves open:** OI-102 (Active Defense vs Wound — Defender's Margin modification of a
Wound Tier/magnitude) remains unresolved and blocking for end-to-end validation
**Canonical rule change:** None