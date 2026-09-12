---
document:
  title: "Tiwas — Magic & Special Abilities Subsystem: Project Proposal"
  version: "0.1 (draft advisory proposal — not executed, not ruled)"
  status: "Advisory / Non-canonical. No DEC assigned. No promotion under the 8-step Promotion Rule (Proposals §21) has been sought or performed. Pending Tiwa's review."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  created_date: "2026-09-12"
  last_modified_date: "2026-09-12"
related_decisions:
  - "DEC-015 (Canonical §15 — Magic/Special Abilities is Reserved; Design Direction only)"
  - "DEC-114 R3 (magic:/ability: Tag namespace reserved, zero entries, requires authorization with the Magic subsystem)"
  - "Proposals/WIP v1.4.3 §15 (current non-canonical design direction: magic via Advanced Skills, no mandatory fixed spell list)"
  - "Invariants 1–18 (Canonical §16 / DEC-016)"
  - "DEC-007.A (Overflow immutability)"
  - "DEC-107 / DEC-115–117 / DEC-127 (Effect Tier Magnitude System, unified StateRecord schema)"
  - "DEC-130 (GM Fiat — bounded universality)"
---

# Tiwas — Magic & Special Abilities Subsystem: Project Proposal

> **STATUS DISCLAIMER.** This document is an **advisory design proposal only**. It is
> produced by Claude in its advisory capacity per the project's governance model
> (Claude: presents options, flags conflicts, drafts documents; never rules, never
> assigns DEC numbers, never records decisions). Nothing in this document is Canonical,
> Ruled, or binding. No promotion under the 8-step Promotion Rule (Proposals/WIP §21)
> has been sought. All numeric values, names, and architectural choices below are
> **candidates for Tiwa's review and ruling**, not settled design. Where an option
> conflicts with a Canonical Invariant or an existing non-canonical designer ruling,
> that conflict is flagged explicitly rather than silently resolved, per the standing
> LLM Governance Rules (Roadmap §24 Rule 6: never silently resolve an open designer
> fork).

---

## 0. Document Control

| Field | Value |
|---|---|
| Document ID | (unassigned — advisory draft, no DEC) |
| Subsystem | Magic / Special Abilities (Canonical §15; Reserved) |
| Namespace dependency | `magic:` / `ability:` (reserved, zero entries — DEC-114 R3) |
| Author | Claude Sonnet 5 (advisory) |
| Reviewer | Tiwa (ruling authority) — review pending |
| Recording authority | OpenCode ("big-pickle") — only after Tiwa rules |
| Distribution | Tiwa (sole intended reader per this task's brief) |

---

## 1. Executive Summary

Tiwas currently has **no ruled magic mechanic**. Canonical §15 states only a Design
Direction: magic and special abilities should emerge through the existing **Advanced
Skill** architecture (Canonical §12) rather than a bespoke spell-list, and a setting may
grant permission for a Skill lineage to represent magic, martial techniques, psychic
ability, technology, etc. The Canonical Rules explicitly **reject** a mandatory
fixed-spell-list Core requirement. The `magic:`/`ability:` Tag namespace is reserved
with **zero entries** (DEC-114 R3) pending a Magic-subsystem design.

This proposal surveys seven architectural patterns drawn from published TTRPG magic
systems, maps each onto Tiwas's existing Core invariants and unified mechanical
architecture (Core Test Transaction, Skill-Tier/Cap system, Failure XP, Advanced Skills,
Overflow, the Effect Tier Magnitude System, and the unified StateRecord schema), and
scores each against Tiwas's Locked Invariants and its three Locked Design Priorities.

**Headline finding:** three of the seven researched patterns (Advanced-Skill-native
casting, a Technique×Form combinatorial naming layer over that same Advanced-Skill
engine, and Extended-Test-based ritual casting) require **zero new subsystems** and
are directly buildable today against already-Locked material. Two patterns (a
dedicated mana/spell-point pool; a fixed Vancian spell-slot list) **structurally
conflict** with Invariant 17 (no competing primary resource/progression economy) as
commonly implemented, and are retained here only as researched reference points, not
as recommendations. Two further patterns (a corruption/miscast risk track; a
GM-adjudicated paradox/reality-bending freeform mode) are **conditionally compliant**
but each opens a genuine, currently-unruled design fork that this document flags
rather than resolves.

This document recommends, as a Draft Direction (not a ruling), layering
**Options 1 + 2 + 3** as the base architecture, with **Option 5 (Corruption)** offered
as an optional escalation module contingent on a specific ruling (§8, Q-M3), and
**Options 4, 6, and 7** retained as rejected/reference patterns unless Tiwa's intent for
Tiwas's magic diverges from its stated crunch-forward, simulation-first identity.

---

## 2. Purpose & Scope

### 2.1 Purpose

To provide Tiwa with a structured, invariant-checked comparison of candidate magic
system architectures for Tiwas, sufficient to support a designer ruling on:

1. which base architecture (or combination) the Magic subsystem should adopt;
2. what, if anything, needs to be added to the Core Test Transaction, the Effect Tier
   Magnitude System, or the Tag/Condition/StateRecord schema to support it;
3. the starter `magic:`/`ability:` Tag vocabulary (deferred to a follow-on draft
   pending this ruling, per DEC-114 R3's "requires authorization together with the
   Magic subsystem").

### 2.2 In Scope

- Comparative research on seven magic-system archetypes from published TTRPGs.
- Mapping of each archetype onto Tiwas's existing Locked mechanics.
- An Invariant Compliance Matrix.
- Cross-cutting integration analysis against already-Ruled non-canonical subsystems
  (S-3 Effects, S-4 Wounds, Conditions, Tags, the unified StateRecord schema).
- A list of open design questions requiring Tiwa's ruling.

### 2.3 Out of Scope

- Any specific spell/ability content (setting-authored, per Canonical §15 and the
  DEC-077/DEC-077.A content-authoring precedent — not an advisory-model task absent a
  specific conversion mandate like DEC-077.A's).
- Any DEC assignment, promotion, or Canonical Rules edit.
- Balancing/numeric calibration beyond what is needed to demonstrate Invariant
  compliance (calibration is simulation/playtest work, per Roadmap §7/§9 precedent).

---

## 3. Governing Constraints

Any candidate architecture is checked against the following binding material. These
are restated, not re-derived — see the cited sections for full text.

| # | Constraint | Source | Binding? |
|---|---|---|---|
| C1 | d100 roll-under; 100 always fails and is always a qualifying Double; floor rounding | Canonical §2 (Invariants 1–4) | Locked |
| C2 | Cost = natural roll, paid from the Skill's resource domain (PE for Body, MP for Mind) | Canonical §7 (Invariant 6) | Locked |
| C3 | Overflow → direct HP damage; **immutable** — no Tag/Trait/Effect/Condition/subsystem may reduce, redirect, absorb, or modify Overflow | Canonical §7; DEC-007.A | Locked |
| C4 | Failure XP = max(0, Roll − Skill); Skill Roll Pool; General XP | Canonical §9–§11 (Invariant 8) | Locked |
| C5 | Advanced Skills created only by a qualifying failed Double; Tier+1; full-formula Cap recompute; resource domain follows Tier-1 lineage | Canonical §12 (Invariants 12–14) | Locked |
| C6 | No Universal Play subsystem may introduce a **competing primary resource or progression economy** | Canonical §16 Invariant 17 | Locked |
| C7 | Universal Play modules must build on the Core Test Transaction, never replace or parallel it | Canonical §16 Invariant 18 | Locked |
| C8 | Magic/Special Abilities is **Reserved**; current Design Direction (non-canonical) favors Advanced-Skill-emergent magic; setting grants permission per Skill lineage; **no mandatory fixed spell list in Core** | Canonical §15; Proposals §15 | Design Direction (non-canonical, but the only standing direction) |
| C9 | `magic:`/`ability:` namespace reserved, **zero entries**; any list requires authorization together with the Magic subsystem | DEC-114 R3 | Non-canonical designer ruling |
| C10 | Skills are explicitly forbidden from requiring Tags (no Tag-gated Skill entitlement); DEC-025 not reopened by any unification work | DEC-025; DEC-115 R4; DEC-116 R5; DEC-117 R7 | Non-canonical designer ruling, repeatedly reaffirmed |
| C11 | Unified StateRecord schema: `Type` / `Tier Y` / `Magnitude Z` / optional `Location X`, `Z = −Y` for Effect/Condition records; Effect Tier = causing Skill's Skill-Tier (DEC-107) | DEC-107; DEC-115–117; DEC-127 | Non-canonical designer ruling |
| C12 | GM Fiat is universal in scope but does not override the Locked Canonical Core (Overflow immutability, Cost = natural roll, HP=0 incapacitation, no-DoT policy) | DEC-130 | Non-canonical designer ruling |
| C13 | No damage-over-time / persistent-damage Effects; all HP loss is Base-tier Inflict Injury only | DEC-023.A | Non-canonical designer ruling |

**Reading note:** C1–C7 are Canonical/Locked and cannot be contradicted by any option
below without flagging a Core conflict. C8–C13 are non-canonical designer rulings —
strong precedent, still open to Tiwa's revision, but this proposal treats them as the
default frame unless a specific option is presented as deliberately breaking one (each
such case is flagged, never silently assumed compliant).

---

## 4. Comparative Research: Existing Magic-System Archetypes

Seven archetypes were surveyed. Sourced systems are cited; all descriptions below are
paraphrased mechanical summaries, not reproductions of copyrighted rules text.

| Archetype | Representative system(s) | Core mechanism | Resource model | Risk/failure model |
|---|---|---|---|---|
| A. Fire-and-forget slot casting | Dungeons & Dragons (all editions), loosely descended from Jack Vance's *Dying Earth* stories | Caster "prepares" a fixed number of discrete spells into level-banded slots; each casting consumes one slot; slots refresh on a long rest | A **second, spell-specific currency** (slots), independent of any other resource pool | None inherent — a prepared spell simply works when slotted; failure is rare/edition-dependent |
| B. Stamina/fatigue-fueled skill casting | GURPS Magic (standard) | Casting a known spell is a **skill roll**; on success, the caster pays an energy cost (Fatigue Points) proportional to the spell's power; skill improves like any other skill | Reuses an **existing general-purpose attribute-derived pool** (Fatigue), shared with all strenuous activity | Failure wastes the attempt (and sometimes partial energy); no corruption/backlash by default |
| C. Percentile skill-as-spell (d100) | Chaosium Basic Roleplaying / RuneQuest (Spirit/Rune/Sorcery magic) | Each spell (or magic "system") is itself a **d100 skill**, rolled under exactly like any mundane skill, sometimes augmented by other skills or ritual time | Varies by sub-system: some spend a POW-derived pool per casting, some (Rune magic) are pool-and-recharge, some (Sorcery) are skill-only | Ordinary skill failure; some variants add fumble tables |
| D. Combinatorial Verb×Noun art matrix | Ars Magica (Techniques × Forms) | A spell is authored by combining one "Technique" (verb: create/perceive/change/destroy/control) and one "Form" (noun: fire, mind, body, etc.); the caster's rating in *both* arts sums into the casting roll; **formulaic** (known, reliable, cheap) vs **spontaneous** (improvised on the spot, weaker, costs more) vs **ritual** (slow, most powerful) are three casting modes over the same matrix | A fatigue-like resource is spent on riskier/spontaneous casting; formulaic casting is comparatively cheap | Missing the target by a margin still succeeds at a fatigue cost; missing badly fails outright; critical fumbles ("botches") scale with danger |
| E. Belief/paradigm reality-bending | Mage: The Ascension | A caster combines ratings in nine open-ended "Spheres" to declare a freeform effect; the GM adjudicates plausibility; effects that visibly violate consensus reality ("Vulgar," witnessed) risk a backlash resource ("Paradox") that can erupt in unpredictable consequences | A dice-pool skill roll gated by a general magical aptitude attribute; a separate quasi-resource ("Quintessence") can buy down difficulty; **Paradox** functions as an escalating risk counter, not a spendable resource | Explicit GM-adjudicated risk/backlash system; higher-impact or more-witnessed effects generate more risk |
| F. Ambient-power channelling with corruption/miscast | Warhammer Fantasy Roleplay ("Winds of Magic") | No pre-existing spell-point pool: a caster makes a casting/"Channelling" test against ambient magical energy; failure (or optional over-channelling for power) risks a **miscast**, resolved on a severity table; miscasts and other exposure accumulate as a **Corruption** track with escalating narrative/mechanical consequences | No dedicated numeric mana pool at all in the modern edition — the roll itself is the resource gate | Explicit escalating risk/consequence table (miscast severity, Corruption accumulation, eventual character loss to Chaos) |
| G. Fixed point-buy fixed spell list | Classic point-buy universal systems (e.g., GURPS's own spell-as-skill list bought with character points; also see Vancian's academic bookkeeping tradition) | Spells are individually purchased/learned discrete abilities from an enumerated master list; no combinatorial generation | Character-build currency (points) at creation/advancement, separate from any in-fiction resource | Ordinary roll-to-cast failure; no systemic corruption |

**Sources consulted (paraphrased, not reproduced):** Dungeons & Dragons Vancian-magic
discussion and history (D&D Lore Wiki; EN World forums; TV Tropes; *In Defense of
Vancian Magic*, The Socratic Dungeon); GURPS Magic, Fatigue Points, and Mana rules
(GURPS Wiki/Fandom; SJGames Pyramid articles on Limited/Unlimited Mana); RuneQuest and
Basic Roleplaying magic overview (Chaosium product and blog pages; RuneQuest Wiki;
Frank Mitchell's *Magic in RuneQuest and Its Descendants*; BRP SRD); Ars Magica
Techniques/Forms and formulaic/spontaneous/ritual casting (Ars Magica Wiki; EN World
*Game Design Masterclass*; *Ars Magica 5e Rules Summary*; TTRPG-Games power-scaling
article; Project: Redcap); Mage: The Ascension Spheres/Paradox/Quintessence (White
Wolf Wiki; 1d6chan; Onyx Path forums; Andrew J. Luther's HeroQuest port); Warhammer
Fantasy Roleplay Winds of Magic, Channelling, Miscast, and Corruption (Cubicle 7
product page; 1d6chan; Anima beginner's-guide summary; WFRP4 Chaos Dice document
summary).

---

## 5. Design Options for Tiwas

Each option is expressed **in Tiwas's own terms** (Skills, Tiers, the Core Test
Transaction, the Effect Tier Magnitude System, the unified StateRecord schema) so it
can be checked mechanically, not just thematically, against the Locked Core. Options
are numbered for cross-reference, not priority-ranked until §7.

### 5.1 Option 1 — Advanced-Skill-Native Casting (baseline; Archetype B/C hybrid)

**Mechanism.** A "spell" is simply an **Advanced Skill** whose Tier-1 root is a normal
attribute-linked skill and whose formula has been extended per Canonical §12 (a
qualifying failed Double on a mundane or magical skill can create it, exactly as any
other Advanced Skill). No new creation path is introduced. A setting grants
**permission** (a Tag or fictional gate, not a new mechanic) for specific Skill
lineages to be treated as "magical" in fiction — mechanically, resolution is
identical to any other Skill test.

- **Resolution:** ordinary Core Test Transaction (Canonical §6), unmodified.
- **Cost:** the natural roll, from PE (Body-rooted lineage) or MP (Mind-rooted
  lineage) per Canonical §12.3 — **no new pool.**
- **Effect delivery:** the caster selects an S-3 Effect on a successful contest (solo
  Skill tests may use the existing Difficulty/Stakes framework, S-8, for non-opposed
  casting) exactly as a combat Skill does; Effect Tier = casting Skill's Skill-Tier
  (DEC-107); Magnitude = −Tier (DEC-115 R2).
- **Growth:** ordinary Failure XP / Skill Roll Pool / General XP; new "spells" (new
  Advanced Skills) emerge only from qualifying failed Doubles (Canonical §12), exactly
  like a fighter discovering a new combat technique.
- **Fit to C8:** this **is** the standing Proposals §15 direction, made mechanically
  explicit rather than left as prose.

**Invariant check:** fully compliant with C1–C7 by construction — it introduces no new
mechanism whatsoever, only a fictional label on existing Advanced Skills.

### 5.2 Option 2 — Technique × Form Combinatorial Naming Layer (Archetype D)

**Mechanism.** Layers a **naming/organizing convention** over Option 1's engine,
inspired by Ars Magica's Technique×Form matrix, without adding new dice mechanics.
Define two closed catalogs at the setting level:

- **Verbs** (Techniques): e.g., Create, Perceive, Transform, Destroy, Control.
- **Domains** (Forms): e.g., Flame, Flesh, Mind, Metal, Spirit — each Domain is
  pre-associated with one Body or Mind attribute (a setting-authoring choice, not a
  new mechanic).

A "magical Skill" is a normal Tier-2 Advanced Skill whose two component attributes are
drawn one from a Verb-associated attribute and one from a Domain-associated attribute
(per Canonical §12's ordinary "add one new attribute, recompute Cap" rule — this
option changes nothing about *how* the Advanced Skill is built, only about how the
*designer chooses which attribute pair to combine* and how the result is *named* in
play, e.g. "Destroy-Flame" instead of an arbitrary skill name). Higher-Tier magic
(Tier-3+) adds further Verb/Domain-linked attributes exactly as any Tier-3+ Advanced
Skill does today.

- **Formulaic vs. spontaneous distinction (optional sub-rule):** a caster may attempt
  an **unlearned** Verb×Domain combination as a normal Skill test at Skill value 0
  (per Canonical §5.3, "a Skill may legitimately begin at 0") using the closest
  attribute pair — this reproduces Ars Magica's "spontaneous magic" without a new
  mechanic, since Tiwas already allows any Skill to be attempted from 0 and to grow
  from Failure XP on the first failed attempt (Canonical §10.1).
- **Ritual/formulaic distinction:** deferred to Option 3 (Extended Tests) for the
  "slow but powerful" casting mode Ars Magica calls Ritual.

**Invariant check:** fully compliant — this is Option 1 with a taxonomy, not a new
mechanic. Its only cost is design/documentation overhead (§6).

### 5.3 Option 3 — Extended-Test Ritual Casting (Archetype D's "Ritual" mode)

**Mechanism.** For deliberately slow, high-Magnitude magical workings (setting-defined:
wards, mass enchantments, divinations spanning hours), a casting "session" is resolved
as a literal **S-9/S-10 Extended Test** (already Ruled, DEC-067–070): each interval is
an ordinary Core Test on the relevant magical Skill; Margin accumulates
(DEC-067); failed intervals are neutral (DEC-068); the GM sets the completion target
(DEC-070, no formula, GM discretion precedent). On completion, the ritual applies a
single Effect whose Tier is set by GM Fiat within the bounds of DEC-107/DEC-130 (the
accumulated Margin total is *evidence* the GM may use to justify a higher Tier — not a
new formula this proposal invents).

**Invariant check:** fully compliant — reuses S-9/S-10 verbatim, per the Roadmap's own
instruction that Universal Play modules must be **adapters** around already-locked
machinery, not parallel engines (C7).

### 5.4 Option 4 — Dedicated Mana/Spell-Point Pool (Archetype B's "Limited Mana"
variant; Archetype G's build-point variant)

**Mechanism.** A caster has a separate numeric pool ("Mana") independent of PE and MP,
spent per spell and recovering on its own schedule.

**Invariant check — CONFLICT.** This is a **textbook violation of Invariant 17** (no
Universal Play subsystem may introduce a competing primary resource/progression
economy) as literally stated. It is retained here only because the user's brief
explicitly asked for options "even ones which do not obviously fit," and because it is
the most common pattern in published fantasy heartbreakers, so its rejection should be
recorded rather than silently omitted (per Roadmap §24 Rule 6, an explicit rejection,
not silence, closes off a design fork the corpus has not yet closed).

**Compliant sub-variant:** if "Mana" is defined as **nothing but a fictional relabeling
of existing MP** (i.e., Mind-rooted magical Skills spend ordinary MP, per Canonical
§12.3's existing lineage rule) — this collapses into **Option 1** exactly, and is not
actually a fourth option; it is flagged here specifically so Tiwa can see that the two
are easy to conflate and are **not** mechanically identical unless the "Mana pool"
proposal is *deliberately* only MP under a new name.

### 5.5 Option 5 — Corruption / Miscast Risk Track (Archetype F)

**Mechanism.** Casting failure (or, in a harsher variant, casting *success* above a
Tier/Magnitude threshold) can impose a **Condition-tier StateRecord**, e.g.
`Corrupted Tier-Y Magnitude Z` (`Z = −Y`, per the existing DEC-079/DEC-115 Condition
format — no new record shape). This Condition escalates on repeated qualifying
triggers (same-tier-stacking or Tier-replace, per existing Condition stacking rules,
DEC-079) and, per setting-authored content, may eventually gate access to further
magical Advanced Skills, impose escalating Skill-side penalties, or (GM Fiat, bounded
per DEC-130) end a character's usable career as a caster — **never** HP loss, since
DEC-023.A's no-damage-over-time / no-persistent-damage prohibition and DEC-007.A's
Overflow immutability both remain untouched (a Corrupted Condition penalizes Skill
values or imposes narrative gates, exactly like Encumbered or Fatigued already do — it
does not create a new HP-adjacent damage channel).

**Invariant check — conditionally compliant.** Using the existing Condition/StateRecord
machinery (C11) rather than a new pool keeps this inside Invariant 17. **The genuine
open fork** (not an Invariant violation, but an unruled design choice) is: **does the
trigger for Corrupted use the same "qualifying failed Double" gate that creates
Advanced Skills (Canonical §12), or an independent trigger (e.g., any failed cast
above a Tier threshold)?** If Corrupted fires on the *same* failed-Double event that
also creates an Advanced Skill, the two consequences (growth and risk) are coupled —
a substantive design decision this proposal does not make (see §8, Q-M3).

### 5.6 Option 6 — GM-Adjudicated Paradigm/Reality-Bending Freeform Magic
(Archetype E)

**Mechanism.** A caster declares an open-ended intended effect; the GM assigns a
Difficulty grade (reusing the already-Ruled S-8 architecture, DEC-063–066) based on how
far the effect strains the setting's established rules, and resolves it as a single
Core Test at that effective Skill. No enumerated spell list, no Verb×Form matrix —
purely declarative, GM-mediated content.

**Invariant check — conditionally compliant, but a poor fit to Tiwas's stated
identity.** Mechanically this can be built as "an ordinary Core Test with a
GM-assigned Difficulty grade" and therefore does not, by itself, violate any
Invariant — it uses only Locked/Ruled machinery (S-8). However:

- It runs directly against Tiwas's **Locked Design Priority 1** ("granular physical
  simulation where the situation warrants it") and Priority 3 ("minimum resolution
  steps without sacrificing Priority 1") in the opposite direction from every other
  Tiwas subsystem so far: it *replaces* mechanical granularity with GM narrative
  judgment at the point of greatest player-facing impact (what the spell *does*),
  rather than resolving it through the same Effect/Tier/Magnitude machinery every
  other Skill uses.
- A literal "Paradox" backlash-pool-as-published (Mage's Quintessence/Paradox
  interaction) **would** violate Invariant 17 if implemented as a genuinely new
  spendable resource; a Tiwas-compliant version would have to be re-expressed as a
  Corrupted-style Condition per Option 5, at which point Option 6 is really "Option 1
  plus Option 5 plus a much looser GM-fiat Effect-declaration step," not a distinct
  architecture.
- Included per the brief's explicit invitation to propose options that "do not
  obviously fit" — **not recommended** as Tiwas's primary magic architecture, given
  the system's crunch-forward identity (see Canonical §1's Core Identity statement).

### 5.7 Option 7 — Fixed Enumerated Spell List with Point-Buy Slots (Archetype A/G)

**Mechanism.** A closed, GM/designer-authored list of named spells, each with a fixed
level/cost; characters purchase known spells with character-creation or
advancement-time points; casting consumes a "slot" for that spell's level, refreshed
on a Rest.

**Invariant check — CONFLICT.** This is the **most incompatible** archetype
researched:

1. **Spell slots are, definitionally, a second progression/resource economy**
   independent of PE/MP/Skill advancement — a direct Invariant 17 violation.
2. **Discrete spell purchase with build points** is a **second XP/advancement
   currency** parallel to Failure XP → Skill Roll Pool → General XP (Canonical
   §9–§11), again conflicting with Invariant 17's "no competing... progression
   economy" clause, and with the standing rejection (DEC-025) of any Skill-side
   tag/category entitlement system, since a fixed spell list functions exactly like
   the rejected "formal tag/category system on Advanced Skills" in spirit (gatekeeping
   *what* a Skill can produce by a list external to the Skill-Tier/Cap formula).
3. A "Rest to refresh slots" mechanic has **no analogue** in Tiwas's Recovery model
   (Canonical §8: Recovery is `floor(Regen/2)` after every test, unconditionally, on
   the resource *pool*, never on a discrete per-ability counter).

**Not recommended under any variant.** Retained in this proposal only as the clearest
negative reference point — the pattern most GMs coming from D&D-adjacent systems will
instinctively reach for, and the one most worth explicitly rejecting on the record so
it is not silently re-proposed later.

---

## 6. Cross-Cutting Integration Analysis

| Tiwas subsystem | Interaction for Options 1–3 (recommended base) | Interaction for Option 5 (Corruption, conditional) | Interaction for Options 4/6/7 (rejected/non-fit) |
|---|---|---|---|
| Core Test Transaction (§6) | Unmodified; magic Skills are ordinary Skills | Unmodified | Options 4/7 require a second cost-payment step outside the 9-step transaction — conflict |
| Overflow (§7; DEC-007.A) | Unmodified — a magic Skill that overflows its PE/MP pool damages HP exactly like any Body/Mind Skill | Unmodified — Corrupted never touches Overflow | Option 7's slot system has no Overflow analogue at all — a structural gap, not just a style choice |
| Failure XP / Advanced Skills (§9–§12) | Primary growth path for new "spells" | Same trigger event is the open fork (§5.5, §8 Q-M3) | Option 7 replaces this path entirely with point-buy — conflict |
| S-2 Location Index / §14.7 | A magic Skill's location-referencing Effects (e.g., a bolt that can "cripple a limb") follow the same W1/W2/W3 gates and Skill-Tier ≥ 2 gate (DEC-041) as any other Skill — no special case needed | Unaffected | Unaffected structurally, but Option 6's freeform declaration style tends to bypass the explicit-objective Warrant Test in practice — a GM-discipline risk, not a rules conflict |
| S-3 Effects (DEC-023.A / DEC-107) | Magic Skills select from the same Effect menu; Tier/Magnitude from Skill-Tier exactly as combat Skills (no "spell-specific" Effect menu is needed, though setting content may add Tag-flavored variants, e.g. `damage:fire`, already in the DEC-114 R4 vocabulary) | A `Corrupted` Condition is just another Condition-tier Effect target | Option 7's fixed list is itself effectively a closed, parallel "Effect menu," duplicating rather than reusing DEC-023.A |
| S-4 Wounds (DEC-032–042) | Magic-caused Wounds use the identical `Location X Tier-Y Wound Z` record and Skill-Tier ceiling (DEC-107) as any other Wound source | Unaffected | Unaffected |
| Conditions / Tags / unified StateRecord (DEC-079/080/114–117) | `magic:`/`ability:` namespace entries would be ordinary Tags (vocabulary-only by default, DEC-116) used for setting-level *permission* gating (e.g., `magic:tradition_hermetic`) — never a Skill-side gate (preserves DEC-025, C10) | `Corrupted` is a normal Condition-typed StateRecord; no schema change | Option 6's "Paradox" is exactly the case DEC-116/117 were built to prevent becoming a numeric engine if implemented naively |
| GM Fiat (DEC-130) | Available for Tier assignment on Extended-Test rituals (Option 3) and for permission-gating narrative fit; never overrides Overflow immutability or Cost=roll | Available for Corrupted severity/consequence content, bounded per DEC-130 | Option 6 leans on GM Fiat as its *primary* resolution mechanism rather than an occasional override — a scope mismatch with DEC-130's "not a mechanic substitute" clause (C12) |

---

## 7. Invariant & Priority Compliance Matrix

Legend: **✅** compliant by construction · **⚠** conditionally compliant (depends on
an unruled choice) · **❌** conflicts as commonly implemented.

| Option | Inv. 6 (Cost=roll) | Inv. 7 (Overflow) | Inv. 17 (no competing economy) | Inv. 18 (no parallel engine) | DEC-025 (no Skill-Tag gating) | Priority 1 (granular sim) | Priority 3 (min. steps) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1. Advanced-Skill-Native | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2. Technique×Form layer | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3. Extended-Test Ritual | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (fewer steps than a bespoke ritual engine) |
| 4. Dedicated Mana Pool | ✅ | ✅ | ❌ (unless it collapses into Option 1) | ⚠ | ✅ | n/a | ❌ (extra bookkeeping pool) |
| 5. Corruption/Miscast | ✅ | ✅ | ✅ (if built on existing Conditions) | ✅ | ✅ | ✅ | ⚠ (extra record to track) |
| 6. Paradigm/Freeform | ✅ | ✅ | ⚠ (✅ only if "Paradox" is re-expressed as Option 5) | ⚠ | ⚠ (risk of de facto Skill gating via GM narrative fiat) | ❌ | ⚠ |
| 7. Fixed Spell List/Slots | ❌ | n/a (no Overflow analogue) | ❌ | ❌ | ❌ (functions as rejected Skill-side entitlement list) | n/a | ❌ (adds a bookkeeping layer, not fewer steps) |

---

## 8. Recommended Path Forward (Draft Direction — Not a Ruling)

This is a **recommendation for Tiwa's consideration**, explicitly not self-executing:

1. Adopt **Option 1** as the mandatory mechanical base: magic is Advanced-Skill-native,
   full stop. This alone satisfies Canonical §15's Design Direction and requires no new
   rule text beyond a namespace/permission convention.
2. Adopt **Option 2** as a documentation/authoring convention layered on Option 1, to
   give setting content a coherent naming grammar (Verb×Domain) without inventing new
   dice mechanics. This is where most of the "flavor" work for a Tiwas magic system
   should live.
3. Adopt **Option 3** for any setting content that wants slow, high-Magnitude "ritual"
   magic, reusing S-9/S-10 verbatim.
4. Hold **Option 5 (Corruption)** as an optional escalation module, gated on Tiwa's
   ruling of Q-M3 below — it is compliant, but its trigger-coupling question is a real
   fork, not a detail.
5. Do **not** adopt Options 4, 6, or 7 as currently researched; retain them in this
   document as the negative reference set.

---

## 9. Open Design Questions Requiring Tiwa's Ruling

| ID | Question | Why it matters |
|---|---|---|
| Q-M1 | Which option(s) from §5 should form the ruled base architecture? | Nothing below can be built without this |
| Q-M2 | Does a setting's "permission" for a Skill lineage to be magical (Canonical §15) need a formal Tag (e.g. `magic:permission_hermetic`) checked at character creation, or is it purely a fictional/GM-adjudicated gate with no mechanical Tag at all? | Determines whether `magic:` namespace entries (DEC-114 R3) gate anything mechanically or remain flavor-only |
| Q-M3 | If Option 5 (Corruption) is adopted: does the Corrupted-Condition trigger fire on the **same** qualifying failed Double that creates an Advanced Skill (coupling risk to growth), or on an **independent** trigger (e.g., any failed cast, or casting above a Tier threshold)? | A genuine unruled fork, not a detail — changes the entire risk/reward shape of magic |
| Q-M4 | Should Mind-rooted and Body-rooted magical lineages be permitted to mix within one Advanced Skill (per the existing general Advanced-Skill rule that a Body-rooted lineage may add a later Mind attribute and vice versa, Canonical §12.3), or should setting-level "traditions" restrict this for magic specifically? | Affects whether "Body-and-Mind hybrid casters" are possible by default |
| Q-M5 | Should location-referencing magical Effects (an "eldritch bolt that can cripple a limb") require the same Skill-Tier ≥ 2 gate as physical Effects (DEC-041), or is a lower/no gate desired for magic specifically? | If unaddressed, DEC-041's existing universal-scope wording already answers this as "same gate applies" — Tiwa may want to confirm or override |
| Q-M6 | Does learning a wholly new "spell" ever require anything beyond the existing mechanical trigger (qualifying failed Double, Canonical §12) — e.g., narrative gating such as finding a grimoire or a tutor — or is the mechanical trigger sufficient and narrative framing purely GM color? | Affects whether Magic needs any new *acquisition* rule at all, or only naming/flavor conventions |
| Q-M7 | What is the starter `magic:`/`ability:` Tag vocabulary (DEC-114 R3's authorization step)? | Blocked until Q-M1/Q-M2 are answered; scoped as a follow-on deliverable, not this document |
| Q-M8 | Should Extended-Test ritual magic (Option 3) require a minimum Skill-Tier to attempt at all, mirroring DEC-041's Skill-Tier ≥ 2 gate for location-referencing Effects? | Prevents a Tier-1 caster from ever legally attempting "ritual-scale" workings, if that is desired |
| Q-M9 | If a Corrupted Condition (Option 5) is adopted, what removal/healing route applies — the existing Effect Heal System (DEC-121/DEC-127) alone, or a setting-specific "purification" narrative action analogous to DEC-135.A's dual removal-route pattern for Fatigued? | Precedent exists (DEC-135.A) for a Condition having two coexisting removal routes; whether Corrupted should follow that pattern is a separate ruling |
| Q-M10 | Is a Tiwas-native re-expression of Mage's "Paradox" (Option 6) — i.e., Option 5's Corrupted Condition, specifically triggered by *unwitnessed-vs-witnessed* or *subtle-vs-overt* casting distinctions — worth pursuing as a later, separate proposal, or is that distinction out of scope for Tiwas's tone? | Determines whether any part of Option 6 survives as a flavor input into Option 5, rather than being fully rejected |

---

## 10. Risks & Non-Recommendations Recorded for the Record

- **Risk:** silently treating "Mana" as a new pool because it *sounds* like standard
  fantasy-genre vocabulary, when it is mechanically MP under a new label (Option 4's
  compliant sub-variant) or a genuine new resource (non-compliant). Recording this
  distinction explicitly here is intended to prevent that drift during later drafting.
- **Risk:** a fixed spell list (Option 7) creeping back in piecemeal, spell-by-spell,
  as "just a few named effects for flavor" — each individual named spell is harmless,
  but the *pattern* of gating what a Skill can do by an external enumerated list
  reproduces the rejected DEC-025 architecture one spell at a time. Flagged so any
  future draft can be checked against this specific failure mode.
- **Non-recommendation:** Option 6 (paradigm/freeform) is not recommended as Tiwas's
  primary magic architecture. It is retained in this document, per the task brief, as
  a deliberately-researched option that does not fit Tiwas's stated identity, not as a
  live candidate.

---

## 11. Appendix A — Summary Table for Quick Reference

| Option | One-line description | Recommended? |
|---|---|---|
| 1 | Magic = Advanced Skills, no new mechanics | **Yes — base** |
| 2 | Ars-Magica-style Verb×Domain naming over Option 1 | **Yes — authoring layer** |
| 3 | Slow rituals = S-9/S-10 Extended Tests | **Yes — for ritual-scale content** |
| 4 | Dedicated Mana pool | No — Invariant 17 conflict unless it collapses into Option 1 |
| 5 | Corruption/miscast Condition track | Conditional — pending Q-M3 |
| 6 | GM-freeform paradigm/reality-bending | No — poor fit to Priority 1/3; risks Invariant 17 if "Paradox" is literal |
| 7 | Fixed enumerated spell list + slots | No — multiple direct Invariant/DEC-025 conflicts |

## 12. Appendix B — Bibliography (Consulted, Paraphrased Only)

- *Vancian magic system*, Dungeons & Dragons Lore Wiki.
- *Vancian Magic?*, EN World D&D & Tabletop RPG News & Reviews forum thread.
- *Vancian Magic*, TV Tropes.
- *Advanced d20 Magic* (Dynamic Spellcasting variant), Wikipedia.
- *In Defense of Vancian Magic*, The Socratic Dungeon.
- *A Brief History of Vancian Magic*, The Evil GM.
- *Clarifications to the GURPS Magic System*, GURPS Wiki/Fandom.
- *Fatigue Points*, GURPS Wiki/Fandom.
- *GURPS magic systems in D&D*, GURPS Wiki/Fandom.
- *Mana*, GURPS Wiki/Fandom.
- *Pyramid: Limited Mana* and *Pyramid: Unlimited Mana*, Steve Jackson Games.
- *RuneQuest — Roleplaying in Glorantha*, Chaosium/DriveThruRPG product page.
- *Best magic system for BRP/d100?*, RPGnet forums.
- *BASIC ROLEPLAYING System Reference Document*, Chaosium.
- *WHAT IS RUNEQUEST? — PART TWO*, Chaosium blog.
- *Magic*, The RuneQuest RPG Wiki.
- *Magic in RuneQuest and Its Descendants*, Frank Mitchell's Blog.
- *GURPS - Ars Magica*, RPG Wiki/Fandom (cross-system port reference).
- *Review of Ars Magica Fifth Edition*, RPGnet.
- *Game Design Masterclass: Ars Magica*, EN World.
- *Hermetic Arts*, Ars Magica Wiki/Fandom.
- *Ars Magica*, Project: Redcap.
- *How Ars Magica Handles Power Scaling*, TTRPG Games blog.
- *Ars Magica - Academic Kids* encyclopedia entry.
- *Best RPGs with Custom Magic Options*, TTRPG Games blog.
- *Ars Magica 5e: Rules Summary, Part 2*, System sans Setting.
- *Mage: The Ascension Core Rules* (Advanced Magick System excerpt summary), via Scribd.
- *Mage: The Ascension*, 1d6chan/Miraheze.
- *The Paradox Sphere — Wyld Magick*, Onyx Path Forums.
- *Mage: The Ascension*, White Wolf Wiki/Fandom.
- *Mage: The Ascension in HeroQuest*, Andrew J. Luther.
- *Mage: The Ascension (Alternate Rules)*, V5 Homebrew Wiki.
- *Working on v1.2 update* (IronSpheres devlog), itch.io.
- *Chaos Dice Rules for WFRP 4th Edition* (summary), Scribd.
- *Warhammer Fantasy Roleplay*, 1d6chan/Miraheze.
- *Warhammer Fantasy Roleplay*, Cubicle 7 Games product page.
- *Welcome to Warhammer Fantasy Roleplay*, Noble Knight Gaming Hall.
- *Warhammer Fantasy Roleplay 4e: Beginner's Guide*, Anima.
- *Magic system info — Winds of Chaos*, community forum.

---

*End of document. No DEC assigned. Awaiting Tiwa's review and, if any option is
selected, formal handoff for OpenCode recording only after an explicit ruling.*
