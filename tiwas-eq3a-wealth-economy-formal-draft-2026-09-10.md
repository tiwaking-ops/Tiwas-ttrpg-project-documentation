---
document:
  title: "EQ-3A — Wealth/Economy Model: Formal Rule-Text Candidates"
  version: "v1.0"
  status: "Advisory-only. Non-canonical. Not a ruling. Pending Tiwa's review. Modeled on the EQ-1/EQ-2 draft format (tiwas-eq1-eq2-item-creation-upgrade-repair-draft-2026-09-07.md)."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-10"
  last_modified_date: "2026-09-10"
---

# EQ-3A — Wealth/Economy Model: Formal Rule-Text Candidates

**How to use this document.** Each of the three options below is written as adoptable
formal rule text — specific enough to paste into Proposals/WIP (and, after promotion,
Canonical) directly, the way the EQ-1/EQ-2 draft presented Creation/Upgrade/Repair
mechanics before Tiwa ruled on them as DEC-128/DEC-129. Numbers, formulas, and Skill
names marked *illustrative* are placeholders, not proposed final values. Each option
ends with its own open-question checklist (Q-A/Q-B/Q-C numbering), and a consolidated
Q-0 sits at the top: **which option is the base model** is the prerequisite ruling —
none of the sub-questions can be closed before that selection is made.

This document assigns no DEC number and records no ruling.

---

## Q-0 — Base model selection (prerequisite to everything below)

Before any sub-question in §A/§B/§C can be closed, Tiwa must select which option is the
operative base model for Tiwas's economy. The three options are **mutually exclusive**
foundations, not layers that stack.

---

## §A — Option A: No Formal Economy (GM Fiat / Narrative Wealth)

### A.1 Core statement
Wealth is not tracked as a numeric character resource of any kind. No Attribute, Skill,
Tag, or record field represents wealth.

### A.2 Acquisition procedure
1. When a character seeks to acquire an item, the GM first adjudicates availability
   directly from the fiction (the character's established station, location, current
   plot state, item rarity as authored content).
2. If the GM judges acquisition **uncertain** rather than automatic, resolve it as an
   **ordinary Skill Test** (Core Test Transaction, DEC-006) using a GM-selected
   domain-appropriate Skill — reusing the DEC-043 precedent of the GM/table choosing a
   substitute Skill when no dedicated one exists.
3. **Success:** the GM narrates the acquisition; any "cost" (debt, favor, depleted
   savings, a called-in obligation) is fiction only and creates no persistent numeric
   record.
4. **Failure:** the item is not acquired on this attempt; ordinary Failure XP is
   generated per DEC-009 as with any failed Skill Test. The GM may allow a retry
   later in the fiction, at their discretion.

### A.3 Replacement
Replacing lost or destroyed gear (per Proposals §13's "repair/replacement" item) uses
the identical §A.2 procedure — no special-case rule.

### A.4 Invariant compliance
Trivially compliant. No resource, pool, or record is created; Invariant 17 and
Invariant 18 are not engaged at all.

### A.5 Open questions (Option A)
- **Q-A1:** Is a dedicated Skill lineage (e.g., "Commerce" or "Connections") ever
  defined for §A.2 step 2, or does the GM select a *different* existing Skill each
  time with no standing default? (Compare DEC-098's "Brawling is the *default*
  defensive Skill... not a universal principle" pattern — a similar conditional
  default could apply here.)
- **Q-A2:** Does §A.2 apply identically to acquiring a *brand-new* item versus
  *replacing* a specific lost item, or should replacement always succeed
  automatically between sessions (a softer, more heroic-resilience-aligned reading)?

---

## §B — Option B: Abstract Wealth Rating (Skill-gated, non-pool)

### B.1 Definition
Each character has a **Wealth Rating**, an integer (illustrative range 1–5, or reuse
the existing Tier idiom 1–5+). Wealth Rating is **not** a Core Test resource: it is
never spent to pay a Skill Test's Cost, is never subject to Overflow, and is never read
by any step of the Core Test Transaction (DEC-006) except as a Difficulty comparator
(§B.2).

### B.2 Acquisition procedure
1. To acquire an item of a given **Item Tier** `Y` (per DEC-128 Q1's Item Tier/Magnitude
   record), the character makes an ordinary Skill Test using **[Skill lineage — see
   Q-B1]**.
2. Difficulty is set by comparing Wealth Rating `W` to Item Tier `Y`, using the
   **existing DEC-063 fixed additive Skill-side modifier architecture** — no new
   resolution engine, no modification of the natural d100 roll. Illustrative
   comparison table (not locked):

   | Comparison | Difficulty Grade (DEC-063) |
   |---|---|
   | `Y ≤ W` | Trivial or Easy |
   | `Y = W + 1` | Standard |
   | `Y = W + 2` | Hard |
   | `Y ≥ W + 3` | Extreme |

3. **Success:** the item is acquired; any fictional cost is narrated (per §A.2 step 3's
   pattern), with no separate numeric ledger.
4. **Failure:** not acquired this attempt; ordinary Failure XP per DEC-009. Effective
   Skill for the test, and the Failure XP/cascade entry, follow the DEC-064 pattern
   used for S-8 difficulty (effective, difficulty-modified Skill drives the check, XP,
   and Skill Roll Pool cascade — clamped at Cap per DEC-065).

### B.3 Wealth Rating advancement
Two candidate sub-options — **mutually exclusive, requires selection (Q-B2):**
- **B.3(i):** Wealth Rating advances via **General XP** (DEC-011), treated exactly like
  an Attribute or Skill: cost to increase by 1 = current value, full cost required,
  no partial advancement.
- **B.3(ii):** Wealth Rating changes **only** via GM Fiat / narrative reward
  (inheritance, plunder, a patron) — no XP-spend path exists at all.

### B.4 Replacement
Identical procedure to §B.2 — no special-case rule required.

### B.5 Invariant compliance
Wealth Rating is consulted **only** as a Skill-side Difficulty comparator (§B.2 step
2), structurally identical to how Encumbrance (DEC-078) and Difficulty grades (DEC-063)
already modify Effective Skill without touching the natural roll, Cost, or Overflow.
It has **no income/expenditure dynamic against Cost/Overflow** — the same reasoning
DEC-069 used to clear Extended Test Progress of Invariant 17. This clearance should be
stated explicitly in any eventual ruling rather than assumed silently, per the DEC-069
precedent for how such clearances are recorded.

### B.6 Open questions (Option B)
- **Q-B1:** Which Skill Tier-1 lineage governs the acquisition test — a new dedicated
  Skill (e.g. "Commerce," rooted in a Mind attribute such as mpx/Glamour or msx/Charm),
  or reuse of an existing social Skill case-by-case (mirrors Q-A1)?
- **Q-B2:** Select B.3(i) or B.3(ii) for Wealth Rating advancement.
- **Q-B3:** Does Wealth Rating ever *regress* (e.g., a temporary penalty after a
  large acquisition), or is it a pure static gate with no depletion mechanism at all?
- **Q-B4:** Lock the exact Tier-vs-Wealth-Rating-to-Difficulty-Grade table (§B.2 step 2
  is illustrative only).

---

## §C — Option C: Concrete Currency + Tier-Based Pricing

### C.1 Definition
A single currency unit (name TBD — e.g. "Marks," "Crowns") is tracked as a plain
integer on the character sheet. Currency is **not** a Core Test resource: it is never
spent to pay a Skill Test's Cost, is never subject to Overflow, and is not read by any
step of the Core Test Transaction (DEC-006).

### C.2 Pricing
Every item has a `Price = f(Item Tier Y)`. Illustrative candidate formula (not locked):

`Price = 10 × Y²`

| Item Tier | Illustrative Price |
|---:|---:|
| 1 | 10 |
| 2 | 40 |
| 3 | 90 |
| 4 | 160 |
| 5 | 250 |

### C.3 Acquisition procedure
Two candidate sub-branches — **requires selection (Q-C1):**
- **C.3(i) — Funds-only:** if the character's currency ≥ Price, the item is acquired
  automatically; currency is reduced by Price. No Skill Test.
- **C.3(ii) — Funds-plus-gate:** sufficient currency is necessary but not sufficient;
  the character must also pass an ordinary Skill Test (per §B.2's structure, reusing
  DEC-063 difficulty grades) representing availability/negotiation. Currency is spent
  only on success.

### C.4 Currency acquisition
Characters gain currency via GM-awarded rewards (loot, payment, quest reward). No
formulaic drop table is mandated by this rule — mirrors the GM-discretion pattern
already locked for Extended Test completion targets (DEC-070/074).

### C.5 Selling
Selling an item for currency is permitted at a GM-set fraction of Price (illustrative
candidate: 50%). Exact fraction — **Q-C5**.

### C.6 Invariant compliance — REQUIRES EXPLICIT CLEARANCE
This option carries the highest Invariant 17/18 exposure of the three and must not be
treated as safe by default. Proposed clearance rationale, to be explicitly affirmed or
rejected by Tiwa (following the DEC-069 clearance-recording precedent):

1. Currency never modifies the natural d100 roll (Invariant 6) — preserved by
   construction (§C.1).
2. Currency never pays Skill Test Cost and is never read during Overflow application
   (Invariant 7 / DEC-007.A) — preserved by construction (§C.1).
3. Currency is **not** a progression/advancement currency: it does not increase
   Attributes, Skills, or Caps, and it is not a substitute for Failure XP or General
   XP (DEC-011) — this distinguishes it from a "competing progression economy" in the
   Invariant 17 sense. On this basis it functions as a narrative/logistics counter,
   analogous to the ammunition count sketched in Fork EQ-3C or to Extended Test
   Progress (DEC-069) — a record that changes over time but never enters the Core
   Test resource pipeline.
4. **This is a proposed rationale, not a self-clearing fact.** Unlike B, which reuses
   an already-locked Skill-side-modifier pattern outright, Option C introduces a
   literal second persistent number every character tracks — the closest of the three
   options to the "second pool" shape Invariant 17 was written against. It should not
   be adopted without Tiwa explicitly weighing and accepting (or rejecting) this
   rationale, the same way DEC-069 recorded its Invariant-17 assessment as a distinct,
   visible step rather than an assumption.

### C.7 Replacement
Literal purchase of a new item at Price, per §C.3 — no special-case rule.

### C.8 Open questions (Option C)
- **Q-C1:** Select C.3(i) (funds-only) or C.3(ii) (funds-plus-Skill-Test-gate).
- **Q-C2:** Lock the exact Price formula (§C.2's `10 × Y²` is illustrative only).
- **Q-C3:** Starting currency allotment at character creation (ties to Fork EQ-3D).
- **Q-C4:** Does the existing "Steal/Take Item" Effect (DEC-023.A, Equipment Tier)
  apply to currency as well as items, or is currency exempt from that Effect?
- **Q-C5:** Lock the sell-back fraction (§C.5's 50% is illustrative only).
- **Q-C6 (gating question, answer required before adoption):** Does Tiwa accept the
  §C.6 Invariant-17 clearance rationale as sufficient, or does Option C need further
  restructuring (e.g., collapsing toward Option B's non-pool shape) before it can be
  ruled safe?

---

## Consolidated checklist (all options)

| # | Question | Applies to |
|---|---|---|
| Q-0 | Select base model: A, B, or C | All |
| Q-A1 | Dedicated acquisition Skill vs. case-by-case | A |
| Q-A2 | Does replacement get a softer/automatic path | A |
| Q-B1 | Acquisition Skill lineage | B |
| Q-B2 | Wealth Rating advancement: XP-spend vs. GM Fiat only | B |
| Q-B3 | Does Wealth Rating ever regress | B |
| Q-B4 | Lock the Tier-vs-Rating difficulty table | B |
| Q-C1 | Funds-only vs. funds-plus-gate | C |
| Q-C2 | Lock the Price formula | C |
| Q-C3 | Starting currency allotment | C |
| Q-C4 | Does Steal/Take Item apply to currency | C |
| Q-C5 | Lock the sell-back fraction | C |
| Q-C6 | Accept or reject the Invariant-17 clearance rationale | C |

**Recommended reading order if reviewing in one pass:** Q-0 first (it determines which
of the rest even apply), then only the sub-block for the selected option.

---

## Required OpenCode Actions

None. This document is advisory-only and records no ruling. Once Tiwa selects a base
model and rules on that option's open-question checklist, the normal workflow applies:
Claude/advisory drafts the resulting formal rule text as a single consolidated block →
OpenCode verifies against the live register → Tiwa signs off → OpenCode records under a
new DEC number.
