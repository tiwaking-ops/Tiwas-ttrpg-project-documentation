---
document:
  title: "Creature/NPC Action Selection Design Ruling (OI-105 / SC-XX)"
  version: "1.0"
  status: "Advisory recording of a designer ruling. Non-canonical. Assigns DEC-106 in the decision register."
provenance:
  author_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
  ruling_origin: "Human designer (Tiwa), in-session ruling, 2026-09-05, resolving open item OI-105 (SC-XX) from the v3/v4 Ice Troll Combat Playtest cross-report syntheses (2026-09-04 / 2026-09-05)"
  recorded_in: "_consolidation/decision-register.md DEC-106"
---

# Creature/NPC Action Selection Design Ruling (OI-105 / SC-XX)

## 1. Purpose

This document records Tiwa's designer ruling resolving **OI-105 / SC-XX** — creature/NPC
action selection. The gap was exposed by the v3 Ice Troll Combat Playtest: the Ice Troll has
two authored Tier-2 attack skills (Icy Claws 67, Sharktoothed Maw 75), and no rule existed
determining which legal combat action a creature uses on its turn. The ruling was given
in-session as a **Design Override Ruling** over DEC-095 Step 3 (one-substantive-action rule).

**Authority status:** Non-canonical designer ruling (real decision; promotion requires the
8-step Promotion Rule, REQ-021 / Proposals/WIP §21). This ruling **overrides DEC-095 Step 3
for creatures/NPCs** — the original DEC-095 text is preserved and annotated in the decision
register.

## 2. Open item resolved

| ID | Issue | Source |
|---|---|---|
| OI-105 | SC-XX — Creature/NPC action selection (carried over from v3 as OI-002) | v3 Cross-Report Synthesis (2026-09-04) §6.2; GPT-5.6 v3 companion document Q1–Q3; v4 Synthesis (2026-09-05) OI-105 |

## 3. The ruling — verbatim (Tiwa, 2026-09-05)

> **DESIGN OVERRIDE RULING:**
>
> **Original Rule:** Step 3 rules "one substantive combat action/test per turn for every
> combatant".
>
> **New Rule:** "Base one substantive combat action/test per turn for every combatant. If
> combatant has multiple applicable skills, GM fiat. Exception creature/NPC: GM fiat or if
> no GM present, creatures/NPCs with multiple legal combat actions use all of them — playing
> each authored attack action, in highest-applicable-Skill → lowest order. Targeting: each
> attack targets the nearest possible target (eligible = in range/reachable). An
> Area-of-Effect attack instead hits the most targets possible. Multi-action exception:
> creatures/NPCs with multiple attack actions may attack more than once per round by default
> - unlike Player Characters."
>
> **Reason:** "Combat system overhaul due to results of playtests. Additional new systems
> have made multiple attack scenarios viable and testable."

Supporting confirmations (same session):

> Q: DEC-095 multi-action exception — both PCs (one action) and creatures (N attacks at their
> authored skills) become co-ruled. Confirm?
>
> A: **"Ice Troll consequence: Yes. Two attacks a round. Energy Pool: Yes! NPC / Creature may
> exhaust itself due to its own multi-attacks."**
>
> Q: Multi-attack pacing — creature plays all attacks on its own turn, back-to-back, in
> highest→lowest Skill order, each its own S-1 exchange?
>
> A: **"Confirmed."**
>
> Q: Base-layer "If combatant has multiple applicable skills, GM fiat" — applies to any
> combatant including a PC with multiple applicable skills for its single action?
>
> A: **"Yes. Confirmed."**
>
> Q: DEC-095 record handling — original text preserved, Status annotated
> ("Modified for creatures/NPCs by DEC-106")?
>
> A: **"Approved."**
>
> On GM Fiat scope: "GM Fiat should be universal but I will rule on that once all the base
> systems have been designed and completed." — a **pending future ruling**, not decided here.

## 4. Clarifications — verbatim (Tiwa, 2026-09-05)

See §3. No additional clarifications beyond those recorded above.

## 5. Structured restatement (for execution)

### 5.1 Base rule (all combatants)

Every combatant has **one substantive combat action/test per turn** (DEC-095 preserved for
the base economy). When multiple **applicable skills** are candidates for that single action,
the **GM applies fiat** in live play.

### 5.2 Creature/NPC exception (multi-action)

If a GM is **present** (live play): **GM fiat** determines the creature's actions (SC-XX
resolved by GM choice).

If **no GM present** (automated playtest / delegated execution): a creature/NPC with
**multiple legal combat actions** uses **all of them**:

1. **Order:** each authored attack action is played in **highest-applicable-Skill → lowest**
   order.
2. **Pacing:** all attacks occur **on the creature's own turn, back-to-back**; each is its
   own S-1 combat exchange. They are **not** interleaved through the round.
3. **Targeting:** each attack targets the **nearest possible target** (eligible = in
   range / reachable). An **Area-of-Effect** attack instead targets **the most targets
   possible**.
4. **Energy Pool:** each attack is its own Core Test with its own Energy cost. **An NPC /
   Creature may exhaust itself due to its own multi-attacks** — self-Overflow is possible
   exactly as derived from the normal Energy/Overflow rules (DEC-007).

### 5.3 Player Characters

Player Characters do **not** gain multi-attack from this ruling — a PC retains the single
substantive action per turn (DEC-095 base), with GM fiat resolving multiple applicable-skill
cases.

### 5.4 Automated playtest characters

Automated playtest Characters are treated as **creatures** (DEC-102) and therefore acquire
the multi-attack behaviour (§5.2) when they possess multiple authored attack actions.

### 5.5 Pending (not ruled here)

**GM Fiat universality** — Tiwa intends GM Fiat as a general principle, but will rule on it
**after all base systems are designed and completed**. Recorded as pending, not decided.

## 6. Register entry

Recorded in `_consolidation/decision-register.md` (Section B, Non-canonical designer ruling):

| ID | Subject | Status |
|---|---|---|
| DEC-106 | Creature/NPC action selection (SC-XX / OI-105); Design Override of DEC-095 Step 3 for creatures/NPCs | Ruled (non-canonical) |

DEC-095's row is annotated in-place (original text preserved):
"Modified for creatures/NPCs by DEC-106 (2026-09-05) — creature multi-attack override; PC
single-action preserved."

## 7. Status

**Status:** Advisory recording — not canonical
**Authority:** Non-canonical designer ruling (real decision; promotion requires the
8-step Promotion Rule)
**Assigns:** DEC-106 (next sequential ID after DEC-105)
**Resolves:** OI-105 / SC-XX (creature/NPC action selection)
**Overrides:** DEC-095 Step 3 for creatures/NPCs only (base one-action economy and PC
single-action preserved)
**Applies to:** live play (GM fiat) and automated playtest execution (deterministic
multi-attack behaviour)
**Leaves open:** GM Fiat universality (pending all base systems), OI-104 (DEC-101
coverage), OI-106 (Quality → Wound Tier table context), OI-107 (HP floor convention)
**Canonical rule change:** None