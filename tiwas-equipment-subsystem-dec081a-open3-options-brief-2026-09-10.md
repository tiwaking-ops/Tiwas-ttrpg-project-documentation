---
document:
  title: "Equipment Subsystem (Proposals §13) — Options Brief for DEC-081.A Open 3"
  version: "v1.0"
  status: "Advisory-only. Non-canonical. Not a ruling. Pending Tiwa's review."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-10"
  last_modified_date: "2026-09-10"
---

# Equipment Subsystem — Options Brief (DEC-081.A Open 3)

**Scope boundary.** This document identifies options only. It assigns no DEC number,
records no ruling, and is not binding. Any adoption requires Tiwa's explicit ruling and,
per the Promotion Rule (Proposals §21 / REQ-021), remains non-canonical until formally
promoted. OpenCode should take no recording action against this document except to store
it as an advisory reference, pending Tiwa's direction.

---

## 0. Framing — what Open 3 actually is

DEC-081.A closed two of DEC-081's three carried-open items:

- **Open 1** (Equipment-tier Effect interaction) — closed, confirmed complete by the
  existing DEC-023.A/DEC-114/DEC-128 stack.
- **Open 2** (damage beyond Sunder) — closed, confirmed complete by DEC-118–121/DEC-129.
- **Open 3** — explicitly **not touched**: *"the full Equipment subsystem (Proposals §13,
  Reserved) remains open."*

Proposals §13 lists ten required areas for a complete Equipment subsystem. Most of them
are already covered by rulings scattered across other subsystems (Armor, Tags,
Conditions, Encumbrance, Item records). Open 3 is not a single design fork — it's a
**residual scope statement** that needs to be decomposed before it can be ruled on at
all. Section 1 does that decomposition. Sections 3–6 present option forks for the pieces
that are genuinely undecided.

---

## 1. Coverage map — Proposals §13 vs. the live register

| §13 required area | Status | Governing DEC(s) | Residual gap |
|---|---|---|---|
| Armour | **Ruled** | DEC-058–062 (S-5) | Content only (specific armor items) — DEC-077 authoring path |
| Equipment records | **Ruled** | DEC-081/081.A, DEC-128, DEC-129 | None at framework level |
| Equipment Traits | **Ruled** (framework) | DEC-080 T1, DEC-088 Condition Clause | Content only |
| Tags | **Ruled** | DEC-080, DEC-114 | Extensible by design; no gap |
| Encumbrance | **Ruled** | DEC-078 (+2026-09-06 closure) | None |
| Equipment damage | **Ruled** | DEC-060, DEC-118, DEC-119 | None |
| Repair | **Ruled** | DEC-120, DEC-121, DEC-128 Q-R1–R5, DEC-129 | None |
| Weapons | **Partially ruled** | Tags (`damage:*`, `offense:*`, `handling:*`) | **Ranged weapon range/ammo mechanism — open** (Fork EQ-3C) |
| Carrying | **Partially ruled** | Encumbrance (weight); `slot:`/`state:` Tags (identity) | **No ruled slot-occupancy/swap-cost model — open** (Fork EQ-3B) |
| Replacement | **Partially ruled** | Item Creation = Extended Test (DEC-128 Q2) covers *crafting* a replacement | **Buying a replacement has no mechanism — open** (Fork EQ-3A) |
| Wealth/economy hooks | **Entirely open** | None | **No currency, pricing, or wealth mechanic exists anywhere in the corpus** (Fork EQ-3A) |

**Conclusion:** seven of ten required areas are already closed in substance (content
population aside). Three areas resolve into four genuinely open decision forks, listed
below. A fifth item — equipment content itself — isn't a design fork at all; it's
content-authoring under the existing DEC-077 precedent.

---

## 2. The four open forks (proposed working names, not DEC numbers)

| Working ID | Subject | Why it's still open |
|---|---|---|
| EQ-3A | Wealth / economy model | No mechanism exists; directly touches Invariant 17 |
| EQ-3B | Slot / loadout occupancy & swap cost | `slot:`/`state:` Tags exist as vocabulary only; no occupancy or swap-timing rule |
| EQ-3C | Ranged weapons — range bands & ammunition | No range-band model; no ammo-tracking mechanism ruled anywhere |
| EQ-3D | Starting equipment allocation | Minor; likely resolves as a short GM-discretion default |

---

## 3. Fork EQ-3A — Wealth / Economy Model

### Why this is the highest-stakes fork
This is the only completely unaddressed item in the entire corpus. It also directly
implicates **Invariant 17** ("No Universal Play subsystem may introduce a competing
primary resource or progression economy") — the same test DEC-069 explicitly ran against
Extended Test Progress before clearing it. Any wealth mechanism needs the same explicit
clearance, not a silent assumption that "money" is obviously fine.

### Option A — No formal economy (GM Fiat / narrative wealth)
Wealth is never numerically tracked. Access to equipment is adjudicated the same way
DEC-076 Ruling A handles non-automated creature stat generation: **GM discretion, no
system-authored mechanism.**

- **Example:** A player wants a masterwork longsword. The GM decides, based on the
  character's established station in the fiction (noble, guard captain, pauper),
  whether it's available, and may require a Skill test (Persuasion/Commerce/Social
  Presence) to represent the negotiation — an ordinary Core Test, not a new economy.
- **Pros:** Zero new mechanics; zero Invariant 17 risk; consistent with the
  GM-discretion precedent already used for stabilization (DEC-055), Extended Test
  targets (DEC-070/074), and creature generation (DEC-076).
- **Cons:** Contradicts Priority 1 ("granular physical simulation where the situation
  warrants it") for players who want simulation-grade logistics; provides no numeric
  handle for "replacement" gear after loss, which was one of the §13 required areas.

### Option B — Abstract Wealth Rating (Skill-gated, not a pool)
A character has a **Wealth Rating** (e.g., 1–5, or reuse the existing Tier idiom).
Acquiring an item of a given Item Tier (DEC-128 Q1) requires an ordinary Skill Test
(Commerce/Connections/whatever Skill lineage fits) whose difficulty is set by comparing
Wealth Rating to Item Tier, using the **existing DEC-063 fixed additive Skill-side
modifier architecture** — no new resolution engine, no new pool.

- **Example:** Wealth Rating 2 character wants a Tier-4 item. GM applies a Hard or
  Extreme difficulty grade (DEC-063) to the acquisition Skill Test. Success = the item
  is acquired (at a fictional cost the GM narrates — debt, favor, depleted savings);
  failure = not acquired this scene, ordinary Failure XP still generated.
- **Mechanically:** This is structurally identical to DEC-043's third-party adjudication
  pattern and DEC-063's difficulty-grade pattern — no new machinery, just a new
  Skill-comparison axis. Wealth Rating itself never enters the Core Test Transaction as
  a Cost, so it cannot create Overflow, cannot violate DEC-007.A, and is not a
  "progression currency" in the Invariant 17 sense (it doesn't accumulate/spend inside
  the Cost=Roll transaction — same reasoning DEC-069 used to clear Extended Test
  Progress).
- **Pros:** Numeric enough to be simulation-adjacent without inventing a full currency;
  reuses two already-locked patterns (DEC-063 difficulty, Skill Test resolution);
  naturally answers "replacement" (a failed Repair or lost item becomes a re-roll
  opportunity, not a dead end).
- **Cons:** Still requires deciding what Skill lineage governs acquisition, and whether
  Wealth Rating itself advances (if it does via ordinary XP spending on a "Wealth"
  Attribute/Skill, that's Invariant-17-safe since it's just General XP DEC-011 applied
  to a new Skill; if it's meant to model liquid currency that depletes and replenishes
  session-to-session, that reintroduces the "second pool" question and needs the same
  explicit Invariant 17 clearance as Option C).

### Option C — Concrete currency + Tier-based pricing
A literal currency unit exists; items have prices; prices scale by Item Tier.

- **Example pricing table (illustrative only, not proposed as final numbers):**

  | Item Tier | Suggested base price (currency units) |
  |---:|---:|
  | 1 | 10 |
  | 2 | 40 |
  | 3 | 90 |
  | 4 | 160 |
  | 5 | 250 |

  This reuses the **triangular-formula idiom already established in DEC-103**
  (`Y(Y+1)/2`-style scaling for negation cost) — here shown as `Tier² × 10` for
  illustration; the exact curve is a numbers question for a future ruling, not this
  brief.
- **Pros:** Most simulation-grade; directly answers "replacement" and "wealth/economy
  hooks" as literally as possible; gives GMs a concrete loot/reward lever.
- **Cons:** Highest risk of violating the *spirit* of Invariant 17 if currency is ever
  allowed to modify a Core Test outcome (it must not — currency can only gate
  *access* to items, never buy Skill successes, never offset Cost/Overflow, per
  DEC-007.A's "no subsystem may modify Overflow" and the general no-parallel-resource
  discipline). Requires its own bookkeeping (a literal second number every character
  tracks) — the exact "second pool" shape Invariant 17 was written to prevent, unless
  explicitly scoped as *not* a Core Test resource (comparable to how Extended Test
  Progress is a running record, not a spendable pool, per Proposals §9.4). This
  needs the same explicit DEC-069-style clearance before being treated as safe.

### Comparative precedent (for context only — not a rule import)
- **GURPS** uses an abstract "Wealth" trait (Poor/Average/Wealthy/Filthy Rich) that
  gates starting equipment and is rarely spent turn-to-turn — closest analogue to
  Option B.
- **Blades in the Dark** uses Tier + a small per-job "Coin" spend with no persistent
  itemized inventory economy — a hybrid of B and C at a much smaller numeric scale.
- **D&D-style gp economies** are the closest analogue to Option C, and are also the
  most frequently criticized for turning into bookkeeping overhead disconnected from
  play — a relevant risk given Priority 3 (minimum resolution steps).

None of these are being proposed as imports; they're offered only as calibration
points, consistent with how DEC-132.A used GURPS "Double Defense" and Pathfinder 2e's
reaction model as comparative precedent without adopting either system's numbers.

---

## 4. Fork EQ-3B — Slot / Loadout Occupancy & Swap Cost

The DEC-080 alpha Tag vocabulary already has the *identity* layer (`slot:main_hand`,
`slot:off_hand`, `slot:two_hand`, `slot:body`, `slot:head`, `slot:shield`,
`state:held`/`worn`/`sheathed`/`stowed`), but nothing rules **how many items may
occupy a slot at once**, or **what it costs to change state** (draw a sheathed weapon,
swap a held item, don armor mid-scene).

### Option A — Slots are exclusive; swapping is the turn's one substantive action
One item per `slot:*` tag at a time. Changing what occupies a slot (draw, sheathe,
swap held item) **consumes the character's one substantive combat action for that
turn** (DEC-095) — it does not get a special exemption the way Movement does
(DEC-095's "movement is a free/bundled side-activity" carve-out is explicitly NOT
extended to gear swaps under this option).

- **Example:** A fighter whose weapon is Sundered (DEC-060) must spend their entire
  turn drawing a backup weapon from `state:stowed` to `state:held` before they can
  make an S-1 attack exchange next turn.
- **Pros:** No new mechanic — reuses the existing action economy exactly as ruled;
  maximizes tactical weight of losing/swapping gear (consistent with Priority 1).
- **Cons:** Can feel punishing in fast combat; two-handing (`slot:two_hand`) vs.
  one main + one off-hand item creates edge cases (is switching from a two-hander to
  a sword-and-board one swap or two?) that would need explicit sub-rulings.

### Option B — Swaps are free/bundled like Movement, gated by GM Fiat only
Weapon/gear swaps are treated the same as Movement under DEC-095/DEC-082 — a free
side-activity that never consumes the substantive action, subject to GM Fiat
(DEC-130) if the fiction makes a specific swap implausible in one turn (e.g., donning
full plate mid-fight).

- **Pros:** Simplest; lowest resolution-step cost (Priority 3); no new rule text
  beyond "gear swaps are Movement-class, per DEC-082/095."
- **Cons:** Removes essentially all tactical cost from losing/being disarmed of a
  weapon, which weakens the payoff of the Disarm/Break Hold Effect (DEC-023.A) and
  the Sunder Condition (DEC-060) — those Effects currently have real teeth only if
  re-equipping costs something.

### Option C — Tiered swap cost by gear class
A `Skill-side` penalty (reusing the Encumbered/DEC-078 overlay idiom) applies for the
remainder of the turn if a swap is attempted **and** an action is also taken that
turn — i.e., swapping is technically free, but doing so while also attacking imposes
a flat `−Y` penalty (Y = a fixed small constant, e.g. 2, not scaled by anything) to
represent split attention, expressed exactly like every other Condition-style overlay
already in the corpus (`Tier-Y Condition Value Z`, `Z = −Y`).
- **Pros:** A middle path; reuses the exact record shape from DEC-079/DEC-115 instead
  of inventing new plumbing; preserves *some* teeth for Disarm/Sunder without a full
  lost-turn cost.
- **Cons:** Introduces a new named Condition (`Distracted`/`Fumbling`-equivalent) that
  needs its own alpha-vocabulary entry (DEC-079-style) — more moving parts than A or B.

---

## 5. Fork EQ-3C — Ranged Weapons: Range Bands & Ammunition

Two sub-questions bundle here: (1) how ranged attacks interact with the DEC-133
abstract distance-band model, and (2) whether ammunition is tracked at all.

### 5.1 Range bands
DEC-133 already locks four abstract zones (Engagement/Short/Medium/Far). The open
question is only whether ranged weapons impose a Skill-side penalty/bonus by zone
(reusing DEC-063's fixed additive modifier architecture) or whether range is purely
narrative gating (can/cannot attempt the shot at all, GM Fiat). This is a small,
low-risk decision — likely resolvable in one sentence once Tiwa picks a direction,
and doesn't need its own multi-option deep-dive here.

### 5.2 Ammunition — does tracking it violate Invariant 17?

**Option A — No ammunition tracking (abstracted).** Ranged weapons never run out
mechanically; narrative/GM Fiat only for running-out drama (mirrors Option A of
EQ-3A).
- **Pros:** Zero new mechanics, zero Invariant 17 exposure.
- **Cons:** Weakens granular-simulation Priority 1 for a weapon class that GURPS-style
  play typically simulates closely (relevant given the BToV-Madness GURPS conversion
  workflow, DEC-077.A).

**Option B — Ammunition as a stateless count, never entering the Core Test Transaction.**
A simple integer the player tracks on the character sheet (like GURPS "shots" or
D&D "arrows"), decremented on each ranged attack **outside** the Cost/Overflow
pipeline — it is never spent as Physical Energy/MP, never causes Overflow, and never
modifies the d100. Running out only gates *future* attempts (no ammo = no ranged
Skill Test available), the same way an Unusable item is excluded from valid targets
of negative Effects (DEC-119) rather than mechanically penalized.
- **Example:** A character with `Item Tier 2 Shortbow` and "12 arrows" makes an S-1
  ranged attack; ammo count drops to 11 regardless of hit/miss (each attack expends
  physical ammunition, distinct from the Energy Cost=Roll which is unaffected).
- **Invariant 17 check:** This is structurally the same shape DEC-069 cleared for
  Extended Test Progress — a monotonically-changing record with **no
  income/expenditure dynamic against the Core resource pools**, so it doesn't read as
  a competing primary resource. This needs the same explicit clearance sentence in
  any future ruling, not silent assumption.
- **Pros:** Closest to genre-standard simulation without touching Cost/Overflow;
  reuses the "count-gates-availability" pattern already established for Unusable
  items.
- **Cons:** Adds one more thing to track per character; needs a restock/"replacement"
  hook back into Fork EQ-3A (buying/crafting more ammunition).

**Option C — Ammunition as a Condition-style banded resource** (mirrors Encumbrance's
relative-band model, DEC-078 R2). E.g., Full/Low/Empty bands with a Skill-side
penalty at Low (representing rationing shots) and hard gate at Empty.
- **Pros:** Reuses the exact banded-penalty idiom already locked for Encumbrance;
  avoids a literal per-shot integer.
- **Cons:** Loses simulation granularity (exact arrow count) that some tables may
  want; adds a new banding table to design and justify calibration for.

---

## 6. Fork EQ-3D — Starting Equipment Allocation

This is the lowest-stakes item in Open 3 and likely doesn't need a multi-option
fork. Precedent already exists: DEC-076 Ruling A resolves an almost identical
question (how creature stats are generated in non-automated play) as **"GM discretion,
no system-authored alternate mechanism."** The same default — starting gear is a GM/
setting-module decision (Proposals §17, Setting Modules, already reserves this kind
of content to settings) — closes this cleanly without inventing anything. Flagged
here mainly so it isn't silently forgotten inside "Open 3," not because it needs
deep analysis.

---

## 7. Non-fork item: Equipment content catalog

Actual weapon/armor stat blocks (a "Longsword," a "Composite Bow," specific Tier/Tag
loadouts) are **not a design fork** — they're content, governed by the existing
DEC-077 precedent ("content deferred to the designer's own playtesting") or, where
sourced from the BToV-Madness GURPS material, the DEC-077.A conversion workflow. No
ruling is needed here beyond what already exists; flagged only for completeness of
the §13 checklist.

---

## 8. Cross-cutting conflict checks (apply to every option above)

| Constraint | Applies to | Check |
|---|---|---|
| Invariant 17 (no competing resource/progression economy) | EQ-3A (all options), EQ-3C Option B/C | Must be explicitly cleared, not assumed — see DEC-069 precedent for the clearance pattern |
| Invariant 18 / no parallel resolution engine | EQ-3A Option B/C, EQ-3C all | Acquisition/reload must resolve via ordinary Skill Tests, never a bespoke roll type |
| DEC-007.A (Overflow immutability) | EQ-3A, EQ-3C | No wealth/ammo mechanism may reduce, redirect, or absorb Overflow |
| DEC-082 (Skill-side/Movement-penalty only Time/Action model) | EQ-3B, EQ-3C range | No new action-point pool may be introduced by a swap-cost or reload rule |
| DEC-025 (no Skill-side Tag gating / no Advanced-Skill entitlement) | EQ-3A Option B | A "Commerce" Skill must not become a disguised tag-gate on Effects |

None of the options above, as sketched, appear to violate these on their face — but
each needs the explicit clearance sentence in its eventual ruling, following the
DEC-069 precedent, rather than silent assumption.

---

## 9. Procedural options for how to proceed on Open 3 itself

Separate from *which* mechanical option to pick, there's a prior question: how should
Tiwa want to handle the scope of Open 3 as a whole?

1. **Leave fully Reserved.** Do nothing now; revisit only if a playtest scenario
   forces the question (mirrors how the S-2 non-attack deferral sat dormant until
   S-4 reopened it, DEC-036). Lowest effort, but leaves "replacement," ranged combat,
   and any loot/reward logistics unusable at the table indefinitely.
2. **Commission a dedicated multi-LLM advisory session (an "EQ-3" package)**, scoped
   specifically to Forks A–C, mirroring the EQ-1/EQ-2 process that produced DEC-118–
   129. This is the highest-fidelity path if Tiwa wants comparative multi-model
   analysis before ruling, consistent with established practice.
3. **Rule narrowly now.** Close EQ-3D immediately (GM discretion, per §6 — very low
   risk, no real debate) and defer A–C as a single remaining Open-3 residual, rather
   than treating all four as one monolithic blocker.

---

## 10. Open questions for Tiwa

- Which Wealth/Economy option (A/B/C) fits the intended play experience — is
  logistics-as-drama a goal for this system, or is equipment meant to stay mostly
  narrative?
- Should ammunition tracking exist at all, given the granular-simulation Priority 1
  vs. minimum-resolution-steps Priority 3 tension?
- Is a new Condition-style "swap penalty" (EQ-3B Option C) worth the added
  vocabulary, or should this stay as simple as Option A/B?
- Should Open 3 be tackled as one combined advisory package, or split into
  independently rulable pieces (as suggested in §9, Option 3)?

---

## Required OpenCode Actions

None. This document is advisory-only and records no ruling. If Tiwa selects a
direction from any fork above, OpenCode's action at that point is to record the
resulting ruling under a new DEC number in the normal register, per the established
workflow (Tiwa rules → Claude/advisory drafts formal text → OpenCode verifies against
the live register → Tiwa signs off → OpenCode records).
