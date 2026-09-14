---
document:
  title: "Is Tiwas TTRPG Robust Enough to Adapt Wurm Online's Crafting System? — A Technical Gap-Analysis Report"
  version: "v0.1"
  status: "Advisory / Non-canonical. No DEC assigned. An analytical assessment, not a design proposal and not a ruling. Pending Tiwa's review."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-14"
  research_source: "Wurmpedia (wurmpedia.com) and wurm.wiki.gg / wurm.fandom.com mirrors, retrieved via web search, 2026-09-14"
  related_documents:
    - "tiwas-wurm-online-crafting-adaptation-2026-09-14.md (Part 1 — content adaptation)"
    - "tiwas-wurm-online-crafting-adaptation-part2-2026-09-14.md (Part 2 — expanded item catalog)"
    - "tiwas-crafting-system-proposal-v0.1-2026-09-12.md (prior stored advisory proposal)"
    - "tiwas-tier1-primitive-item-catalog-v0.1-2026-09-12.md (prior stored advisory catalog)"
---

# Is Tiwas TTRPG Robust Enough to Adapt Wurm Online's Crafting System?

## 0. Governance Notice

This is an **analytical assessment**, not a ruling and not a new design proposal. It
answers one question — *does Tiwas's currently-Ruled and Canonical rule set have enough
load-bearing structure to support a Wurm Online-fidelity crafting system, and where
exactly does it not* — using the same DEC-cited discipline as every other advisory
document in this project. No DEC is assigned. Nothing here promotes, locks, or resolves
any open item; it inventories what is already resolved and what is not, then renders a
reasoned verdict. Only Tiwa rules; only OpenCode records a ruling.

This report should be read alongside the two-part content adaptation delivered
previously (see `related_documents` above), which took the opposite approach — assuming
adaptability and drafting content. This report interrogates the assumption itself.

---

## 1. Executive Verdict

**Partially, and unevenly.** Tiwas's **core resolution and item-record architecture**
(the Core Test Transaction, Item Tier/Magnitude, Extended-Test creation, Repair-to-Tier,
the Tags ontology) is **already structurally sufficient** to represent the *shape* of
Wurm's crafting system — materials, components, quality-gated creation, and
improvement — without inventing a second resolution engine. That is a genuinely strong
result: five of Wurm's seven core crafting primitives (see §4–5) already have a ruled
or near-ruled Tiwas home.

However, Wurm's crafting system is not actually a standalone subsystem in the source
game — it is **structurally fused to three other subsystems that Tiwas has never ruled
and, on inspection, should not try to import wholesale**:

1. A **persistent, real-clock decay/upkeep economy** (items and buildings lose quality
   against real-world elapsed time unless a settlement's coffers are paid), which
   presupposes a persistent always-on game world Tiwas does not have and is not designed
   to have (Tiwas is a session-based TTRPG; G3, the duration/time-unit scale, remains
   explicitly open — DEC-133/DEC-138).
2. A **server-tick-based Rarity system** (a literal once-per-second background dice roll
   against the live server clock, independent of any player action), which has no
   coherent analog in a turn-based Core Test model without being redesigned from first
   principles rather than "adapted."
3. A **large, separately-metered resource economy** (currency, merchants, trader prices,
   settlement upkeep funds) that the existing EQ-3A open fork already flags as
   unaddressed and this report does not resolve.

None of these three are *crafting* mechanics in the narrow sense — they are the
**MMO-persistence layer Wurm's crafting happens to live inside**. Stripped of that
layer, Wurm's actual creation/improvement/material/quality logic is a close structural
cousin of what Tiwas already has ruled. The honest verdict is therefore two-layered:

> **Tiwas is robust enough to adapt Wurm's *crafting logic*. It is not, and arguably
> should not try to be, robust enough to adapt Wurm's *persistent-world economy* that
> crafting is embedded in — and conflating the two would smuggle a second, unruled
> resource/progression layer into Tiwas in violation of Invariant 17.**

See §7 for the full scored breakdown and §8 for a recommended adoption boundary.

---

## 2. Methodology

1. Research Wurm Online's crafting system comprehensively via Wurmpedia and its
   community mirrors (wurm.wiki.gg, wurm.fandom.com), going beyond the materials/items
   coverage of the prior two-part adaptation to include the **mechanical formulas and
   systemic dependencies** underneath creation and improvement: the skill-to-quality
   curve, decay, rarity, and the action/favor economy.
2. Decompose Wurm's crafting system into a small number of **independent mechanical
   primitives** — the minimum set of distinct rules a system needs in order to be
   recognizably "Wurm-style crafting" rather than generic crafting.
3. For each primitive, audit the live Tiwas decision register for a Ruled or Canonical
   equivalent, citing the governing DEC(s).
4. Classify each primitive as **Structural** (crafting cannot function recognizably
   without it) or **Peripheral** (adds fidelity/flavor but is separable).
5. Render a verdict per primitive, then an overall verdict, then non-binding
   recommendations for how far adoption should reasonably go.

---

## 3. Wurm Online Crafting System — Technical Findings

### 3.1 Quality Level and "The Curve"

Every material, component, and item in Wurm carries a single **Quality Level (QL)**,
1–100. A gathering or crafting skill does not map to QL linearly — Wurm uses a published
formula, **"The Curve"**:

```
y = 2x − (x / 10)²
```

where `x` is the raw skill number and `y` is the **effective skill**, which becomes the
practical ceiling on the QL a character can produce. At raw skill 50, effective skill is
`2(50) − (50/10)² = 100 − 25 = 75` — i.e., a 50-skill miner can produce at most
**75 QL** ore, not 50 QL. The curve is concave: it rewards early skill gains heavily and
flattens hard near the 100 cap, meaning the last 20–30 raw skill points yield
proportionally far less effective-skill gain than the first 20–30.

### 3.2 Creation and Improvement Resolution

Creating an item is a single skill-check action gated by: (a) the actor's raw skill
(curved per §3.1) against the item's difficulty, (b) the QL of the input material(s),
and (c) the QL of any required tool. A successful creation produces an item whose
starting QL is a function of all three. **Improving** ("imping") an existing item is a
repeated-action process: each attempt can raise the item's QL toward — but rarely past
in a single action — the improver's own effective skill ceiling; a failed improve
attempt **damages** the item instead of improving it (this is the source of Wurm's
well-known "sweet spot" player strategy: imping with a tool/skill deliberately near the
item's current QL to bias toward small, reliable gains rather than large, risky ones).
There is no published closed-form success-probability formula on Wurmpedia comparable
to a d100 roll-under table; the mechanic is implemented as a server-side probability
curve tuned around the skill/QL/difficulty gap, not a transparent player-facing formula.

### 3.3 Material Hierarchy and Alloying

Already covered exhaustively in the prior two-part adaptation (wood/metal/stone/
leather/cloth/clay, plus the four ruled alloy recipes: Steel, Brass, Bronze, Electrum).
Not repeated here except as a primitive in §4.

### 3.4 Decay and the Real-Time Upkeep Economy

This is the most consequential finding of this report. Wurm items **passively lose
quality against elapsed real-world time**, independent of any player action:

- Off-settlement ("off-deed"), decay is fast — community-reported figures put a log at
  roughly 20% damage within about six real-world hours of being left on the ground.
- On a settlement ("deed"), decay is suppressed proportionally to how much real-money-
  or resource-backed **upkeep** the settlement's coffers hold: partial suppression below
  30 days of banked upkeep, **complete suppression of building/fence/decorative-item
  decay** above 30 days banked.
- Items **in a character's inventory** generally do not decay at all (food is the
  notable exception), which is itself a structural design choice — decay is a
  world-persistence mechanic, not a possession mechanic.
- Bulk storage containers (crates, bins) exempt their contents from decay entirely but
  impose a flat 5%-of-contents loss per real-world month if the settlement's upkeep
  lapses.
- Material type modulates the rate (cedar decays slower; oak/steel take 20% less
  **usage** damage specifically, a related but distinct mechanic from decay).

Every one of these figures is denominated in **real-world clock time** and **requires a
persistent, always-simulating game world** with a settlement/upkeep-fund economy behind
it. There is no version of this mechanic that functions in a session-based tabletop
game without either (a) inventing an entirely new "how much real time has passed
between sessions" bookkeeping layer bolted onto the campaign calendar, or (b)
abandoning the real-time basis and re-deriving decay as a function of **in-fiction
elapsed time or Extended-Test intervals** instead — which is a redesign, not an
adaptation.

### 3.5 The Rarity System

Rarity (Rare / Supreme / Fantastic) is layered on top of QL as a fully independent
axis. Mechanically, it is **not** a function of the crafting roll at all:

> "On average once an hour a lucky window of 20 seconds in duration is created… any
> actions done during this window get a rarity roll. Specifically, it's a 1-in-3600
> chance roll done every second."

That is: the server runs a **background, per-second, per-player dice roll against the
live clock**, independent of skill, material, or the action being performed. If a
player happens to be performing a creation (or, with a further nested 1-in-5 check, an
improvement) action during one of these server-generated windows, the resulting item
becomes Rare (or, on a second nested check, Supreme, or a third, Fantastic). Rarity then
grants small permanent functional bonuses (10–19% reduced usage damage; small stat
bonuses on weapons/armor/tools; slower enchantment decay).

This is architecturally a **real-time Poisson-process background event**, not a
crafting-roll outcome. It has no natural expression inside a discrete, player-initiated
Core Test (DEC-006) without discarding the "background timer" mechanism entirely and
replacing it with something else — e.g., re-triggering off a qualifying failed Double
(which Tiwas already uses for Advanced Skill creation, DEC-012) — which would be a
**new Tiwas mechanic inspired by Wurm's rarity, not an adaptation of Wurm's rarity**.

### 3.6 The Action/Favor Economy

Wurm actions consume real-world seconds (an action queue), and priest characters draw
on a **Favor** resource (gained via prayer/sacrifice, spent on divine-crafting-adjacent
effects such as enchanting) that is entirely separate from the Wurm equivalent of
Stamina. This is a second metered resource pool layered specifically onto the crafting-
adjacent enchanting subsystem. Real-world action-second timers are explicitly excluded
from this report's scope per the standing instruction that Tiwas has no ruled duration
system (G3 open). Favor-as-a-second-pool is flagged separately in §4/§5 because,
independent of timing, it is a **second primary resource** of the kind Invariant 17
already forbids introducing without explicit designer approval.

### 3.7 Skill System and Characteristics

Wurm's skill list runs to roughly 130 individual skills with a shared 1–100 cap and a
use-based (not failure-based) gain model: skill increases probabilistically **on
success**, at a rate that itself diminishes as skill rises (a second, independent
diminishing-returns curve layered on top of The Curve). This is the **opposite** of
Tiwas's already-Canonical growth model (DEC-009/DEC-010: Tiwas grows explicitly from
**failure**, via Failure XP and the Skill Roll Pool — Canonical §9–§10). This is not a
missing Tiwas primitive; it is a **direct philosophical conflict** between the two
systems' progression models, addressed in §5.

### 3.8 Enchanting (Adjacent, Not Core Crafting)

Wurm's priest-cast item enchantments (e.g., "Circle of Cunning," "Nimbleness," damage-
type imbues) sit adjacent to crafting — they modify a finished item's QL-independent
properties, are cast (not crafted), consume Favor (§3.6), and decay in potency per
action performed with the item unless mitigated by Rarity (§3.5) or a dedicated
decay-reduction rune. This is flagged as **out of scope for a crafting-system
adaptation** — it is Tiwas's eventual Magic/Special-Abilities subsystem's territory
(Canonical §15, Reserved) if adapted at all, not Blacksmithing's.

### 3.9 Economy (Currency, Trading, Merchants)

Explicitly out of scope, consistent with the standing EQ-3A open fork
(`tiwas-equipment-subsystem-dec081a-open3-options-brief-2026-09-10.md`), which this
report does not touch or presume to close.

---

## 4. Requirements Matrix — Independent Mechanical Primitives

| # | Primitive | Structural or Peripheral? | Why |
|---|---|---|---|
| P1 | Single-axis material/item quality scale (QL) | **Structural** | Without it, nothing distinguishes a crude item from a masterwork one — the entire point of the system |
| P2 | Skill-vs-material-vs-tool gated creation resolution | **Structural** | This is the actual "crafting roll" |
| P3 | Skill-vs-current-quality gated improvement resolution, with failure = damage not just "no gain" | **Structural** | This is what makes improvement a genuine risk/reward loop rather than free upgrading |
| P4 | Material → Component → Item hierarchy, incl. multi-input combination (alloying) | **Structural** | This is the actual "crafting tree" |
| P5 | Tool/fixture preconditions (required-but-not-consumed items) | **Structural** | Without it, every item is craftable from bare hands, which is not Wurm's design |
| P6 | Skill-tier/level hard gates on what can be attempted at all | Peripheral | Adds progression texture; a pure probability-only model (no hard gate) is a legitimate simplification |
| P7 | Passive real-time decay tied to a persistent-world settlement/upkeep economy | Peripheral **to crafting itself**, but Structural **to Wurm's actual play experience** | Decay is what makes crafted goods a renewable, tradeable economy rather than permanent possessions — but it is a world-persistence mechanic, not a crafting-roll mechanic |
| P8 | Rarity as an independent, real-clock-driven bonus axis | Peripheral | Adds excitement/collectability; the base system functions completely without it |
| P9 | Use-based (not failure-based) skill progression | **Structural to Wurm**, but **directly conflicts with Tiwas's own Canonical growth model** | Not something to "add" — something that would have to *replace* an existing Canonical rule (DEC-009/010), which this report does not recommend (see §5) |
| P10 | Favor/enchanting as a second resource pool | Peripheral to crafting; Structural to Wurm's enchanting subsystem specifically | Separable — a crafting adaptation does not require adopting enchanting |
| P11 | Currency/trader economy | Peripheral | Already flagged and deferred by EQ-3A |

---

## 5. Tiwas Capability Audit

| # | Primitive | Tiwas Status | Governing DEC(s) | Assessment |
|---|---|---|---|---|
| P1 | Quality scale | **Ruled** | DEC-128 Q1 (Item Tier/Magnitude, `Z = Y`, base-equal at creation); DEC-129 (Magnitude repairable up to Tier) | Direct, clean fit. Tiwas's Tier/Magnitude pair is functionally isomorphic to Wurm's single QL number split into a coarse/fine pair — arguably an improvement in granularity, not a gap. |
| P2 | Creation resolution | **Ruled** | DEC-006 (Core Test Transaction); DEC-128 Q2 (Creation is an Extended Test, DEC-067/068/070 margin-accumulation) | Fully covered — no new resolution engine required, which is itself an Invariant-18 win. |
| P3 | Improvement resolution (incl. failure-damages-item) | **Ruled** | DEC-128 Q3 (failed Upgrade → `Tier+1, Magnitude unchanged`, i.e., an imbalanced, "damaged" item requiring Repair); DEC-129 (Repair mechanism) | Directly and cleanly analogous to Wurm's failed-imp-damages-item rule — arguably a **more elegant version** of the same idea (a structured Tier/Magnitude imbalance rather than a separate "damage %" stat). |
| P4 | Material → Component → Item + combination | **Partially ruled / mostly open** | DEC-128 Q1 places the Item-family record *outside* DEC-115/117's unified schema, but the **multi-input combination formula itself** (how two input Tiers produce one output Tier — Option A/B/C) remains an **open, unruled fork** carried by the stored crafting proposal and restated as OQ-8 in the prior adaptation report | The record shape exists; the arithmetic that would drive an alloying-style recipe does not yet have a ruling. This is the single largest **genuine** gap for content authors, not a structural absence — content can be drafted (as the prior two-part report did) but cannot be called final. |
| P5 | Tool/fixture preconditions | **Unruled — new territory** | DEC-080 T1 (Tags ontology is explicitly open/extensible) supplies the *namespace mechanism*; no ruling has ever gated a Crafting Extended Test on Tag *presence as a precondition* the way DEC-114 R2 gates Disarm/Equipment Damage on Tag presence at a struck location | Structurally trivial to add (the Tags system was designed to be extensible, DEC-080 T1) but **not yet done** — flagged as OQ-5 in the prior report. Low-risk, high-confidence gap: the pattern to copy already exists in the corpus (DEC-114 R2). |
| P6 | Skill-tier hard gates | **Precedent exists, not yet applied to crafting** | DEC-041(1) (Skill-Tier ≥ 2 gate for location-referencing combat Effects) is the exact reusable pattern | Same situation as P5 — a proven pattern sitting one small ruling away from being generalized to crafting. |
| P7 | Real-time decay / settlement upkeep | **Not ruled, and not obviously desirable to rule as designed** | No Tiwas equivalent exists; closest adjacent concept is DEC-078's load/encumbrance bulk-tracking (a *static*, non-time-based bookkeeping precedent) and the still-open G3 duration/time-unit scale (DEC-133/DEC-138 leave it open) | This is the report's central finding: **Tiwas has no persistent, always-running world-clock**, and building one solely to host item decay would be a disproportionate architectural addition relative to what it buys a session-based TTRPG. See §6. |
| P8 | Rarity (real-clock background rolls) | **Structurally incompatible as designed; a reinterpretation exists** | None currently; DEC-012's qualifying-failed-Double mechanism is a plausible **re-derivation point** (a rare, already-existing "something special just happened" trigger) but adopting it would be new content, not adaptation | Cannot be ported as specified (§3.5); can be reinvented using existing Tiwas primitives. This distinction matters for the verdict in §7. |
| P9 | Use-based skill progression | **Directly conflicts with Canonical §9–§10** | DEC-009 (Failure XP), DEC-010 (Skill Roll Pool) — both explicitly **failure-driven**, the opposite of Wurm's success-driven gain | Not a gap to be filled — an **irreconcilable design-philosophy difference**. Adopting Wurm's model would require *reopening Canonical material*, which is outside any content-authoring session's authority and is not recommended. |
| P10 | Favor / enchanting resource | **Would conflict with Invariant 17 as a literal second pool** | Invariant 17 (Core Architectural Invariant list, D1 §16 / DEC-016 item 17: "No Universal Play subsystem may introduce a competing primary resource or progression economy") | A literal Favor pool is pre-empted by an already-Canonical invariant. Any priest/divine-crafting content would need to route through MP (the existing Mind resource) rather than a new pool — solvable, but constrains any future adaptation attempt. |
| P11 | Currency/economy | **Explicitly open (EQ-3A)** | — | Not this report's to resolve; noted for completeness only. |

---

## 6. Why the Decay/Upkeep Layer Is the Real Fault Line

It is worth stating plainly why P7 is treated differently from every other gap in this
report, since on the surface it looks like "just another open item, add it to the open-
questions list." It is not, for three reasons:

1. **Every other gap in §5 is a missing rule that a small, scoped ruling could close**
   (a Tier-combination formula choice, a Tag-precondition pattern, a Skill-Tier gate
   pattern) — each closes with a decision comparable in size to DEC-041 or DEC-114.
   Decay-and-upkeep is not that kind of gap: it presupposes a **standing simulation of
   elapsed real-world time across sessions**, which is a different *category* of design
   commitment from a combat-adjacent Effect rule. It would touch calendar-keeping,
   between-session bookkeeping, and (per Wurm's own design) a settlement/currency
   economy to make the upkeep half of the mechanic mean anything at all.
2. **It is not actually load-bearing for the crafting experience Tiwas would be
   adapting.** A player deciding whether to craft a sword, what materials to use, and
   whether to risk improving it further does not need the sword to also be quietly
   rotting in real time between game sessions for that decision to be meaningful. Wurm
   needs decay because Wurm is a persistent multiplayer economy that must recycle
   material sinks; Tiwas, as a session-based TTRPG, has no equivalent structural need
   unless a future campaign specifically wants one.
3. **Grafting it on anyway would risk violating Invariant 17 and Invariant 18
   in spirit even where not in letter** — a real-time decay/upkeep system that
   meaningfully gates play would function as a second progression/resource economy
   (upkeep funds) running in parallel to Tiwas's existing HP/PE/MP/XP economy, exactly
   the shape Invariants 17–18 exist to prevent, even though neither Invariant literally
   mentions "decay."

**Recommendation (non-binding):** if a future Tiwas campaign wants item degradation at
all, the already-Ruled Equipment-damage StateRecord machinery (DEC-118/119/121) already
provides a complete, session-scoped alternative — damage from *use and combat*, healed
by Repair — without needing a real-time clock. This is arguably **already Wurm-
equivalent in function** (a damaged item needs Repair before further Upgrade in both
systems) without any of the real-time/settlement baggage. This report recommends *not*
attempting to port passive real-time decay, and treating the existing damage/repair
cycle as the intentional, sufficient Tiwas analog.

---

## 7. Scored Verdict

| Primitive | Verdict |
|---|---|
| P1 Quality scale | ✅ Fully supported (Ruled) |
| P2 Creation resolution | ✅ Fully supported (Ruled) |
| P3 Improvement/failure-damages-item | ✅ Fully supported (Ruled) |
| P4 Material→Component→Item + combination | 🟡 Structure supported; combination *formula* open |
| P5 Tool/fixture preconditions | 🟡 Pattern exists elsewhere in corpus; not yet applied to crafting |
| P6 Skill-tier hard gates | 🟡 Pattern exists elsewhere in corpus; not yet applied to crafting |
| P7 Real-time decay/upkeep | 🔴 Not supported; not recommended for adoption (see §6) |
| P8 Rarity (real-clock rolls) | 🔴 Not portable as-specified; a same-*spirit* reinvention is feasible |
| P9 Use-based skill progression | 🔴 Conflicts with Canonical growth philosophy; not adoptable without reopening Canonical rules |
| P10 Favor/second resource pool | 🔴 Pre-empted by Invariant 17 as a literal pool; solvable only by routing through MP |
| P11 Economy | ⚪ Out of scope (EQ-3A) |

**Score: 3 of 6 Structural primitives (P1–P6) are fully Ruled; the remaining 3
Structural primitives (P4 formula, P5, P6) are one small, precedent-guided ruling each
away from being Ruled.** Every Peripheral primitive that touches real-world time,
real-clock randomness, or a second progression economy (P7–P10) is either
architecturally unwelcome or requires deliberate reinvention rather than adaptation.

---

## 8. Overall Answer

**Is Tiwas robust enough to adapt Wurm Online's crafting system?**

**Yes, for the part of Wurm's crafting system that is actually crafting** — the
material/component/item hierarchy, quality-gated creation, and risk-bearing
improvement. Tiwas's Extended-Test creation model, Item Tier/Magnitude record, and
Repair-to-Tier mechanism were independently arrived at (per DEC-128/129) and turn out,
on this research, to be a close structural match for Wurm's own Quality-Level/Curve/
Improving design — close enough that most of the remaining gaps (P4's combination
formula, P5's tool preconditions, P6's skill gates) are **one scoped ruling each**,
reusing patterns Tiwas has already validated elsewhere in the corpus (DEC-114 R2 for
P5's pattern; DEC-041 for P6's pattern), not open-ended design problems.

**No, for the part of Wurm's crafting system that is actually a persistent-world
economy wearing a crafting UI** — real-time decay, settlement upkeep, and the
background-timer Rarity system. These are not crafting mechanics that Tiwas is missing;
they are **MMO-specific infrastructure that a session-based TTRPG has no structural use
for**, and forcing them in would risk contradicting already-Canonical invariants
(no second resource/progression economy) for a payoff (real-time item decay between
sessions) that does not serve Tiwas's own stated design priorities (heroic resilience,
minimum resolution steps).

The honest, single-sentence verdict: **Tiwas's rule set is robust enough to absorb
Wurm's crafting *logic* almost completely, provided the adopter explicitly declines
Wurm's real-time persistence layer rather than trying to import it — the two-part
content adaptation delivered previously is evidence this can be done in practice, not
just in principle, though it correctly leaves the P4/P5/P6 formula/precondition/gate
questions open for Tiwa rather than silently resolving them.**

---

## 9. Non-Binding Recommendations

1. **Rule P5 and P6 first** — both are low-risk, pattern-complete (DEC-114 R2 and
   DEC-041 are directly reusable templates), and unlock the rest of the crafting
   content-authoring backlog without touching anything Canonical.
2. **Rule P4's Tier-combination formula next** — this is the single highest-leverage
   open item; every alloy/composite recipe in the prior two-part adaptation is
   currently only illustrative pending this choice.
3. **Deliberately decline P7 (real-time decay) and P9 (use-based progression)** as
   designed — not because they are unimplementable, but because importing them would
   mean overriding or sitting alongside already-Canonical material (the failure-driven
   growth model; the no-second-economy invariants) for no clear gain to a session-based
   game.
4. **If item degradation-over-time is ever wanted**, build it from the already-Ruled
   Equipment-damage StateRecord machinery (DEC-118/119/121) scoped to **in-fiction
   elapsed time or Extended-Test intervals**, not real-world clock time — this achieves
   Wurm's *design goal* (crafted goods are not permanent) without importing its
   *implementation* (a persistent server clock).
5. **If Rarity-style "something special happened" content is wanted**, tie it to the
   already-Ruled qualifying-failed-Double trigger (DEC-012) rather than a new
   background-timer mechanic — this is a reinvention using native Tiwas primitives, and
   should be presented to Tiwa as new content requiring its own ruling, not mislabeled
   as an adaptation of Wurm's Rarity system.

---

## Appendix — Source Pointers (this report)

- The Curve (skill-to-QL formula): `wurmpedia.com/index.php/The_curve`
- Decay: `wurmpedia.com/index.php/Decay`, `wurmpedia.com/index.php/Damage`,
  `wurmpedia.com/index.php/Settlement`, `wurmpedia.fandom.com/wiki/Settlements`
- Rarity system: `wurmpedia.com/index.php/Rarity_system`, `wurm.wiki.gg/wiki/Rarity`,
  `wurm.fandom.com/wiki/Rarity`, `wurm.fandom.com/wiki/Spell_enchantment`
- (Materials/items/skills sourcing carried forward from the prior two-part adaptation's
  own appendices — not re-cited here.)

**No content from these pages is reproduced verbatim beyond short attributive
paraphrase (one quoted clause on the Rarity "lucky window," under the 15-word limit);
all figures, formulas, and systemic descriptions are restated in Claude's own words per
standing copyright discipline.**
