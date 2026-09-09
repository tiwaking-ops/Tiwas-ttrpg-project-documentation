# OI-SU-08 / EQ-1 — Updated Item Creation & Upgrade (Revised)

## 1. Item Creation (Simplified)

| Field | Rule |
|---|---|
| Item Tier (Y) | = Skill Tier of Creating Skill |
| Item Magnitude (Z) | = Skill Tier of Creating Skill (**same value as Y**, not Margin) |

Note: this makes `Z = Y` for items — structurally distinct from Effect/Condition's `Z = −Y` (DEC-035.A/DEC-079). Two different Types, two different magnitude formulas. Fine, but should be stated explicitly in rule text so it isn't misread as a DEC-115 R2 violation.

DEC-081 amendment still required (items now have independent Tier/Magnitude outside the Tag/Condition system) — unresolved from last turn.

## 2. Item Upgrade (Simplified)

| Field | Rule |
|---|---|
| Gate | Skill Tier > Item Tier |
| On success | Item Tier +1, Item Magnitude +1 |
| On failure | (still open — "its" ambiguity from last turn unresolved) |

Cleaner than the Margin-accumulation version — no progress-tracking needed, single-roll-per-step.

## 3. Repair (Option C) — Unaffected

Repair still targets the **Equipment Damage / Sunder record's own Tier**, separate from this Item Tier/Magnitude track. §3 mechanism from previous turn stands unchanged.

## Still Open (carried forward)

1. DEC-081 amendment (items get independent state-tracker)
2. Failed-Upgrade "its" meaning
3. Repair-Progress reset across Tier steps (Q-R1)
4. Independent-tracks confirmation (Q-R3)
5. Mid-combat/downtime (Q-R5)

Ready to draft formal rule text whenever you want — say the word and I'll produce the OpenCode-ready handoff block.