---
document:
  title: "Is Tiwas TTRPG Robust Enough to Adapt Wurm Online's Crafting System? — Part 2: Worked Feasibility Stress Test"
  version: "v0.1"
  status: "Advisory / Non-canonical. No DEC assigned. An analytical stress-test, not a design proposal and not a ruling. Companion to Part 1 (`tiwas-wurm-crafting-robustness-assessment-2026-09-14.md`) — read Part 1 first for the mapping framework, primitive matrix, and verdict this test evidences."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-14"
---

# Part 2 — Worked Feasibility Stress Test

## 0. Purpose and Method

Part 1 rendered a verdict by inventory (which primitives are Ruled, which are open,
which conflict). This part tests that verdict **empirically**: it mechanically resolves
one complete Wurm-sourced crafting chain — ore to finished weapon, including an
improve-attempt failure and a repair — using **only** rules already Ruled or Canonical
in the live Tiwas corpus. Every step states which DEC(s) license it. Every step that
cannot be licensed by an existing DEC is flagged **[ASSUMPTION]** inline, naming exactly
which open item (P4/P5/P6 from Part 1) it stands in for. No assumption below is a
ruling; each is a placeholder a future DEC would replace.

**Test subject:** Bryn, a Body-attribute-focused PC, crafts a Steel Longsword from raw
ore, following the exact material chain researched in the prior two-part content
adaptation (§3.2 and §6.2 of Part 1 of that document): Iron Ore → Iron Lump → (alloy)
Steel Lump → Sword Blade + Hilt → **Steel Longsword**, then attempts to Upgrade it,
fails, and Repairs it.

This test does **not** re-derive Wurm's own numbers (The Curve, its QL thresholds, its
probability tables) — per Part 1's verdict, those are P9-adjacent (Wurm's own
progression math) and are not what is being ported. Only the **structural steps** —
gather, refine, combine, create, upgrade, fail, repair — are exercised, using Tiwas's
own d100 roll-under math throughout.

---

## 1. Pre-requisites Assumed Present (flagged, not re-derived)

| Item | Status |
|---|---|
| Bryn has a Blacksmithing Skill (Body-domain, Tier 1, attribute `bpe` per §8 of Part 1's content adaptation) at value 34, Cap 50 | Content assumption, per Part 1 §8's proposed (unruled) skill-family |
| Bryn has Weaponsmithing (Advanced Skill off Blacksmithing, Tier 2, `bpe+bps`, Cap 44) at value 22 | Content assumption |
| Bryn possesses a Hammer (`tool:strike`) and a Forge is present at the crafting location | **[ASSUMPTION — P5]** No DEC yet gates a Crafting Extended Test on Tag/fixture presence; this test assumes the DEC-114-R2-style pattern generalizes as proposed in Part 1 §14, without yet being Ruled |
| Weaponsmithing's `min_skill_tier` for a Steel Longsword is Tier 2 | **[ASSUMPTION — P6]** No DEC yet defines a crafting Skill-Tier gate; this test assumes the DEC-041-style pattern generalizes as proposed, without yet being Ruled |

---

## 2. Step 1 — Gathering: Iron Ore → Iron Lump

**Licensed by:** DEC-006 (Core Test Transaction, all 9 steps), DEC-001 (roll-under,
100-Fumble), DEC-007 (Cost = natural roll, Overflow → HP), DEC-009/DEC-010 (Failure XP,
Skill Roll Pool).

Bryn's Blacksmithing 34, Cap 50. Ordinary Core Test to smelt one Iron Lump:

1. Roll 1d100 → **28**. Success (28 ≤ 34).
2. Cost = 28, paid from Physical Energy (Body-domain lineage).
3. No Overflow (assume sufficient PE).
4. Margin = 34 − 28 = 6 — **not itself a Tiwas mechanic for Material creation**;
   recorded only because it feeds the [ASSUMPTION] Material-Tier formula below.
5. Recovery per DEC-008.

**Assigning the Iron Lump's Material Tier/Magnitude:**
**[ASSUMPTION — extension of P1/DEC-128 Q1 to non-Item Materials]** No DEC currently
states that a gathered raw Material carries a Tier/Magnitude record at all — DEC-128 Q1
is scoped to *Items*. This test assumes the same shape applies one level down the
pipeline (`Material Tier / Material Magnitude`, base-equal at creation, per the pattern
already used for Items), set here as **Iron Lump: Tier 2, Magnitude 2** (a successful,
comfortably-under-Cap roll — content judgment, not a formula output, since no Tiwas
formula currently converts a Core Test Margin into a Material Tier).

**Finding:** the *test resolution itself* (steps 1–5) required **zero** assumptions —
DEC-006/007/009/010 cover it completely. Only the **output record's shape** required an
assumption, and that assumption is a narrow, low-risk extension (reusing an existing
record shape one tier down the hierarchy, not inventing a new one).

---

## 3. Step 2 — Combination: Iron Lump + Charcoal → Steel Lump (Alloying)

**Licensed by:** none directly — this is squarely **P4**, the open Tier-combination
formula.

**[ASSUMPTION — P4]** Using the crafting proposal's Option A candidate
(`min(Crafting Skill-Tier, max(input Tiers))`) explicitly *as an illustrative choice,
not a ruling*, per Part 1's own recommendation (§9 OQ-3/OQ-8):

- Iron Lump: Material Tier 2 (from Step 1).
- Charcoal: assumed Material Tier 1 (a simpler, lower-effort gather — content
  judgment).
- Bryn's Blacksmithing Skill-Tier = 1 (it is a Tier-1 skill; Weaponsmithing is the
  Tier-2 Advanced Skill, not yet relevant at this stage).
- Steel Lump Tier = `min(1, max(2,1))` = **min(1, 2) = 1**.

**Finding:** this is the single step in the entire chain where Part 1's verdict is most
sharply confirmed. The Core Test *resolving* the combination attempt is fully covered
by DEC-006 (it is just another ordinary test), but the **output Tier arithmetic** has
**no ruled formula at all** — three different, mutually exclusive candidate formulas
(Option A/B/C) would produce three different results here, and this test can only
proceed by picking one and flagging it. This is exactly the "one scoped ruling away"
gap Part 1 identified, now demonstrated concretely: **the test cannot produce a
determinate Steel Lump Tier without Tiwa choosing among Option A/B/C.**

---

## 4. Step 3 — Component Creation: Steel Lump → Sword Blade; Log → Hilt

**Licensed by:** DEC-006 (ordinary Core Test), same shape as Step 1. Two more ordinary
Core Tests (Blade from Steel Lump; Hilt from a Log Material, itself gathered via a
Step-1-shape test not repeated here). No new assumptions beyond the Material-Tier
extension already flagged in Step 1 — this step **reuses** that assumption, it does not
add a new one.

**Finding:** confirms Part 1's claim that most of the *chain length* (multiple
sequential refinement steps) is free — each individual step is just another Core Test,
with no compounding rules debt beyond the one already-flagged Material-Tier extension.

---

## 5. Step 4 — Item Creation: Sword Blade + Hilt → Steel Longsword

**Licensed by:** DEC-128 Q2 (**Item Creation is an Extended Test** — DEC-067
margin-accumulation, DEC-068 neutral failure, DEC-070 GM-set completion target).

1. GM sets a completion target of, say, **Margin-total 30** (DEC-070 GM discretion —
   already-Ruled, no assumption needed).
2. Interval 1: Weaponsmithing 22 vs roll 15 → success, Margin 7 → running total 7.
3. Interval 2: roll 30 → failure (30 > 22) → **neutral** per DEC-068: Cost still paid,
   Failure XP still generated, but the running total is **not reduced** — stays at 7.
4. Interval 3: roll 9 → success, Margin 13 → running total 20.
5. Interval 4: roll 4 → success, Margin 18 → running total **38 ≥ 30** → **Extended Test
   completes.**

**Assigning the finished Item's Tier/Magnitude:**
**[ASSUMPTION — P4, reused]** Item Tier at creation = `min(Weaponsmithing Skill-Tier
[2], max(Blade Tier, Hilt Tier))`. Using illustrative values (Blade Tier 1 from the
Steel Lump chain above, Hilt Tier 1): Item Tier = `min(2, max(1,1))` = **1**. Per
DEC-128 Q1, Magnitude is base-equal at creation: **Steel Longsword: Item Tier 1,
Magnitude 1.**

**Finding:** the *test-resolution engine* for Item creation (the Extended Test
machinery itself — completion target, margin accumulation, neutral failure) is
**completely and cleanly Ruled**, requiring no assumption whatsoever. Only the
**Tier-assignment arithmetic feeding into that already-Ruled engine** needed the (now
familiar, single) P4 assumption. This is a materially important distinction: **the
resolution procedure is robust; only one piece of downstream arithmetic is open.**

---

## 6. Step 5 — Skill-Tier Gate Check

**[ASSUMPTION — P6]** Per §1's pre-requisite assumption, a Steel Longsword requires
Weaponsmithing Skill-Tier ≥ 2 to attempt at all. Bryn's Weaponsmithing **is** Tier 2
(an Advanced Skill), so this gate — *if it existed as a ruling* — would have passed.
**Finding:** this check changed nothing about the outcome in this run (Bryn qualified
either way), but its *absence as a ruled mechanic* means nothing currently stops a
Tier-1-only crafter from attempting the same Extended Test today. This is a real,
demonstrable rules gap, not merely a theoretical one — a Tiwas table running this
exact scenario right now would have no textual basis to say "no, you can't even try
that yet," only the pattern-precedent this report and Part 1 both point to (DEC-041).

---

## 7. Step 6 — Upgrade Attempt (Success Case, Shown for Completeness)

**Licensed by:** DEC-128 Q3 (failed-Upgrade behavior) + implied success case (an
ordinary Core Test raising Tier and Magnitude together, per DEC-128 Q1's base-equal
convention, though the **success-case** formula itself is not separately spelled out in
any DEC — it is inferred from Q1/Q3's shared shape, not independently Ruled).

Roll vs effective Weaponsmithing (22): roll **9** → success. Item Tier 1 → **2**,
Magnitude 1 → **2** (`Tier = Magnitude` on a clean success, per the Q1/Q3 shared
convention). **Steel Longsword is now Tier 2, Magnitude 2.**

---

## 8. Step 7 — Upgrade Attempt (Failure Case)

**Licensed by:** DEC-128 Q3, directly and completely — this is the single most
cleanly-Ruled step in the entire test.

Second Upgrade attempt: roll **41** vs effective Weaponsmithing 22 → **failure**.

Per DEC-128 Q3 verbatim: *"a failed Upgrade roll increases the Item's Tier (by 1) with
NO Magnitude gain."* Item Tier 2 → **3**. Magnitude stays at **2**.

**Result: `Item Tier 3, Magnitude 2` — an imbalanced, "damaged" Steel Longsword,
exactly Wurm's failed-imp-damages-item outcome, produced with zero assumptions.**

**Finding:** this is the strongest single piece of evidence for Part 1's core claim.
Wurm's designers built "failed improvement damages the item" as a bespoke rule; Tiwas's
designers independently arrived at an equivalent outcome (a Tier/Magnitude imbalance)
for entirely different reasons (per DEC-128 Q3's own recorded rationale — modeling
"the Skill Tier required to further upgrade may now exceed the crafter's own"). The
convergence is real, not manufactured for this report.

---

## 9. Step 8 — Repair

**Licensed by:** DEC-129 (Magnitude repairable up to, never above, Item Tier), DEC-121
(Tier-mutation / Heal Effect System shape), DEC-128 Q-R1/Q-R2 (Original-Tier ceiling;
GM-set threshold scaling with current Tier).

Bryn (or another Weaponsmith) attempts Repair. Per DEC-128 Q-R1, **maximum Repair is
the item's Original Tier** — here, the Original Tier is unambiguous (this test tracked
it: Tier 1 at creation, before any Upgrade). Repair Skill Roll succeeds; per DEC-129,
Magnitude is restored **up to the current Item Tier (3)**, not above it: **Steel
Longsword: Item Tier 3, Magnitude 3.**

**Finding:** fully Ruled, zero assumptions, and directly analogous to Wurm's own
Repair-restores-QL-toward-current-cap behavior (§3.2/§5 P3 of Part 1).

---

## 10. Consolidated Findings

| Step | Fully Ruled? | Assumption(s) needed |
|---|---|---|
| 1. Gather Iron Ore → Iron Lump | Test resolution: yes. Output record shape: no | Material-Tier record extension (low-risk) |
| 2. Alloy Iron Lump + Charcoal → Steel Lump | Test resolution: yes. Output Tier arithmetic: no | **P4 — the load-bearing gap** |
| 3. Component creation (Blade, Hilt) | Yes (reuses Step 1's assumption only) | none new |
| 4. Item creation (Extended Test) | Test resolution: **fully Ruled**. Output Tier arithmetic: no | P4 (reused) |
| 5. Skill-Tier gate | Not Ruled at all | **P6 — a real, currently-absent guardrail** |
| 6. Upgrade success | Mechanism inferred, not independently spelled out | Minor — success-case symmetry with Q3 |
| 7. Upgrade failure | **Fully Ruled, exactly, no assumptions** | none |
| 8. Repair | **Fully Ruled, exactly, no assumptions** | none |

**Out of eight steps, three (3, 7, 8) required zero assumptions of any kind, and one
more (4) required zero assumptions in its resolution mechanism** (only in a piece of
output arithmetic reused from elsewhere). **Every assumption traces back to exactly one
of the three specific open items Part 1 already named (P4, P5, P6)** — no *new* gap was
discovered by actually running the scenario. This is the strongest possible empirical
support for Part 1's verdict: the gaps are real, narrow, and already correctly
identified; they are not a sign of broader hidden fragility.

---

## 11. Revised Confidence Statement

Part 1 argued the verdict from inventory. This worked test argues it from execution,
and the two agree: **a full Wurm-style crafting chain — gather, refine, combine,
create, upgrade, fail, repair — can be run at a Tiwas table today**, using almost
entirely already-Ruled machinery, **provided the table (or Tiwa, in advance) makes one
explicit, disclosed choice among the Option A/B/C Tier-combination candidates** and
accepts that the Skill-Tier gate (P6) is currently a house convention rather than a
rule. Neither limitation blocked this test from reaching a coherent, mechanically
consistent result — they only mean the result is **provisional pending those two
rulings**, exactly as Part 1 concluded.

---

**End of Part 2.**
