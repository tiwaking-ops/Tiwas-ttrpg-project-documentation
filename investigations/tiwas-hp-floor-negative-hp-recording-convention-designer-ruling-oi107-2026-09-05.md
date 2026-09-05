---
document:
  title: "HP Floor / Negative-HP Recording Convention Design Ruling (OI-107) — Option C: uncapped HP (wound-healing revival path retracted)"
  version: "1.1"
  status: "Advisory recording of a designer ruling. Non-canonical. Assigns DEC-108 in the decision register."
provenance:
  author_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
  ruling_origin: "Human designer (Tiwa), in-session ruling, 2026-09-05, resolving open item OI-107 (HP floor / negative-HP recording convention) carried over as v3 OI-003"
  recorded_in: "_consolidation/decision-register.md DEC-108"
---

# HP Floor / Negative-HP Recording Convention Design Ruling (OI-107) — Option C: uncapped HP

## 1. Purpose

This document records Tiwa's designer ruling resolving **OI-107** — the HP floor /
negative-HP recording convention. OI-107 was carried over from the v3 Ice Troll Combat
Playtest (v3 OI-003, 2026-09-04), where three runs produced three different conventions
(GPT-5.6 Luna uncapped −29; Grok clamped with pre-clamp preserved; Claude landed exactly
on 0, clamping untested). The v4 prompt scaffolded **"clamp to 0, preserve pre-clamp value
in log"** (Gap 6.3) and all v3/v4 run reports carried it as unresolved.

The ruling establishes **Option C: HP is uncapped** — HP may go negative and the negative
value persists as the record. DEC-052 (HP = 0 forced incapacitation) is **preserved
unchanged** as the incapacitation trigger. **Version history:** v1.0 provisionally recorded
a wound-healing revival path; **v1.1 retracts it** (§4.4) — healing Wounds restores the HP
*maximum*, not the current pool, so it cannot revive a negative-HP character.

**Authority status:** Non-canonical designer ruling (real decision; promotion requires the
8-step Promotion Rule, REQ-021 / Proposals/WIP §21).

## 2. Open item resolved

| ID | Issue | Source |
|---|---|---|
| OI-107 | HP floor / negative-HP recording convention | v3 Cross-Report Synthesis (2026-09-04) §6.3 as v3 OI-003; v4 Cross-Report Synthesis (2026-09-05) OI-107 |

## 3. The ruling — verbatim (Tiwa, 2026-09-05)

> **RULING — Option C (uncapped).** HP is not clamped; negative HP persists.
>
> **Original reason:** "If driven to negative HP due to Wounds then healing Wounds (not HP)
> may be an easier way to revive the character. Also adds a counter or extra difficulty
> modifier to reviving characters."
>
> **Retraction, same session:** "Wounds can affect HP minimum by affecting the underlying
> Attribute. Oh I see, even if you heal the Attribute it will not bring back the HP damage,
> it will increase the new HP maximum. Revive via Wound healing will not work. I was
> mistaken."

The three candidate conventions offered for decision (from the OI-107 prompt):

- **A. Clamp to 0** (v4 convention): HP records and holds at 0 minimum; pre-clamp value
  preserved in the log for auditability; overkill has no mechanical effect.
- **B. Clamp but track overkill separately:** pool at 0, overkill logged as separate data.
- **C. Uncapped (negative HP persists):** raw arithmetic retained. — **CHOSEN.**

## 4. Structured restatement (for execution)

### 4.1 Convention

- **HP is uncapped.** Every HP-loss step (Inflict Injury contest-delta, DEC-104; Overflow,
  DEC-007) is recorded at its raw arithmetic value. HP may be negative; **the negative value
  is the record** — there is no clamp and no floor.
- The v4 test-scaffold convention ("clamp to 0, preserve pre-clamp value in log", Gap 6.3)
  is **superseded**. No clamping; raw value IS the record throughout.
- **DEC-052 preserved unchanged:** forced incapacitation triggers at **HP = 0**, no roll.
  Under uncapped HP the record may continue negative below 0 once the trigger has fired.

### 4.2 Post-incapacitation handling (confirmed)

- **Damage while already incapacitated continues to accrue** — further HP loss deepens the
  negative record.
- **Targeting exclusion:** an incapacitated character is **no longer counted as a "nearest
  possible target"** by NPCs/creatures — they are not required to be attacked as the nearest
  target. Comfort-tagged: **if all characters are incapacitated, combat ends.**

### 4.3 Revival — gate C (confirmed)

- **Negative HP functions as a counter / extra difficulty modifier to reviving the
  character** (DEC-054/055 revival framework context). The negative magnitude is the
  counter: deeper negative = more HP to heal = harder revival.
- **Gate:** negative HP must be **healed back to 0 before revival is possible**. The gate is
  passed by **HP healing** (via the S-11 Rest/Healing pipeline, DEC-071–074),
  not by Wound healing.

### 4.4 Wound-healing revival path — RETRACTED

- **Retracted:** "healing Wounds is a valid/easier revival path" is **not** part of this
  ruling. Rationale (from Tiwa's realization): a Wound penalizes the underlying Attribute
  (DEC-102), which recalculates the HP **maximum** downward; healing the Wound restores the
  **maximum**, **not** the current HP pool. A negative-HP character **stays negative** after
  Wound healing — only HP healing can reach the 0 gate.
- **Consequence:** the interaction this ruling would have had with **DEC-056** (S-11 healing
  independence from incapacitation) **does not arise**. **DEC-056 is not annotated, not
  superseded, and not touched by DEC-108.**

### 4.5 Preserved

- DEC-052 (HP = 0 forced incapacitation, no roll) — trigger unchanged.
- DEC-053 (HP-driven incapacitation, Wound/incapacitation independence).
- DEC-054 (two-branch permanent loss), DEC-055 (stabilization GM discretion).
- DEC-056 (S-11 healing/incapacitation independence) — untouched.
- DEC-071/DEC-072/DEC-073/DEC-074 (S-11 Rest/Healing pipeline = the mechanism that heals HP
  back toward the 0 gate; wound-magnitude Skill penalty; Extended-Test instance;
  completion target GM discretion).
- DEC-102 (Attribute wounds recalculate HP maximum — the basis of the retraction).
- DEC-104 (HP channel = contest-delta), DEC-007 (Overflow).

### 4.6 Carried open (recorded, NOT ruled)

- **Targeting niche:** whether the post-incapacitation targeting exclusion (4.2) applies to
  PCs/player characters as well as NPCs/creatures, and how it composes with `AoE = most
  targets possible` (DEC-106 §3) — the nearest-target rule is settled for creatures/NPCs;
  the AoE composition corner is unruled.
- GM Fiat universality (global open item; Tiwa to rule after base systems are designed).

## 5. Register entry

Recorded in `_consolidation/decision-register.md` (Section B, Non-canonical designer ruling):

| ID | Subject | Status |
|---|---|---|
| DEC-108 | HP floor / negative-HP recording convention (OI-107): Option C — HP uncapped; DEC-052 trigger preserved; post-incapacitation accrual + target exclusion; revival gate = heal HP back to 0; wound-healing revival path retracted | Ruled (non-canonical) |

## 6. Status

**Status:** Advisory recording — not canonical
**Authority:** Non-canonical designer ruling (real decision; promotion requires the
8-step Promotion Rule)
**Assigns:** DEC-108 (next sequential ID after DEC-107)
**Resolves:** OI-107 (HP floor / negative-HP recording convention) — closed; HP is uncapped
**Supersedes:** the v4 test-scaffold HP clamp-to-0/pre-clamp-preservation convention
**Preserves:** DEC-052 (trigger), DEC-053, DEC-054, DEC-055, DEC-056 (untouched), DEC-071–074
(S-11 pipeline), DEC-102, DEC-104, DEC-007
**Retracts (in v1.1):** the wound-healing revival path provisionally drafted in v1.0
**Leaves open:** OI-104 (DEC-101 coverage), GM Fiat universality, and the AoE-composition
corner in §4.6
**Canonical rule change:** None