# Tiwas — Open Decisions Snapshot (2026-08-31)

**Type:** Dated, task-scoped SNAPSHOT for a cold-reading advisory model. Not part of the project corpus.
**Compiled by:** OpenCode (documentarian), with live repository access, 2026-08-31.
**For:** Claude (advisory design assistant). No prior memory. No repository access while this file is loaded.
**Usage:** Tiwa uploads this file; Claude reads it cold and gives **advisory opinions only** on the Open decisions below. Tiwa verifies anything it acts on against the real repository, separately, with OpenCode.
**Purpose:** Enough context that Claude can state, for every currently-Open decision: (a) what is locked/ruled upstream, (b) what forks remain, (c) what governance constraints apply.

---

## 0. Status and standing exception (read first)

> **This file is a task-scoped snapshot, not the authoritative corpus, and supersedes nothing.**
> All design material in this file is **non-canonical** unless explicitly labelled Canonical/Locked. The repository
> itself (`canonical/`, `proposals/`, `roadmap/`, `investigations/`, `governance/`, `_consolidation/`) is the only
> authoritative source. Every claim below carries a repo path so it can be verified.

**Standing instruction overruled — one session only.**
The handoff report `sources/incoming/opencode-handoff-report.md` §6 says: *"Do not create a new single
'mega-merge' file. Keep documents separable and individually inventoried."* The human designer (Tiwa) explicitly
overruled this **for this single task (2026-08-31)** so a cold-reading model can receive one self-contained file.
This is a **one-session exception**: it does not repeal the standing prohibition generally, and generating this file
does not establish that any other merged file may be created. This file is disposable working material; it may be
deleted after use and is not a repository artifact.

**How to use this file (constraints binding your advice):**

- You may **inspect, compare, explain, identify contradictions, present evidence and possible interpretations,
  and recommend**. You may **not** resolve any Open decision, promote anything to Canonical, or reclassify any
  document — authority changes only through the project's formal 8-step Promotion Rule (§1.4) and a human ruling.
- Evidence is recorded with scope and limitations (evidence class discipline, §1.3). An empirical finding is not a
  designer ruling; a design direction is not a rule; a proposal is not canonical just because it is detailed.
- Hash-indexed / raw evidence files are **pointer-referenced, not reproduced inline** (§5). Do not treat them as
  rules; do not treat a pointer as a copy of the content.

---

## 1. Governance framework (what determines status)

All four files below are the repository's own governance/authority model (reconstructed during consolidation from the
five source documents' self-declared status headers; see `_consolidation/document-inventory.md` and
`_consolidation/relationship-map.md`).

### 1.1 Authority hierarchy (`governance/authority.md`)

```
CANONICAL RULES  (canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md = "D1")
      ↓
PROPOSALS / WIP  (proposals/tiwas-proposals-wip-and-design-direction-v1.4.3.md = "D3")
      ↓
IMPLEMENTATION ROADMAP  (roadmap/tiwas-implementation-roadmap-and-project-governance-v1.4.3.md = "D2")
```

- **D1** is the sole source of locked game mechanics.
- **D3** is "Non-Canonical Design Repository... Design exploration only." It contains **real designer rulings** (see
  `_consolidation/decision-register.md` §B, §D) but those rulings govern **candidate, non-canonical** material, not the
  Canonical ruleset.
- **D2** explicitly disclaims rule authority ("Rule Authority: None — this document does not create game mechanics").
  It governs sequencing, dependencies, simulation gates, regression requirements, and LLM/process rules.
- **`investigations/`** (D4/D5 evidence and analysis) is **never self-executing** — it requires a designer ruling
  before anything it contains affects even the non-canonical Proposals/WIP layer.

### 1.2 Status vocabulary (`governance/status-model.md`)

D1's own header statuses: **Canonical / Locked**, **Reserved** (known required subsystem, no settled
implementation), **Historical / Superseded**.

D3 §0 expanded vocabulary (none of these is a locked rule):

| Status | Meaning |
|---|---|
| Proposed | Candidate rule under active consideration |
| WIP | Currently being developed or reviewed |
| Experimental | Tested/invented for exploration but explicitly excluded from the ruleset |
| Design Direction | Architectural/philosophical preference, not necessarily a mechanic |
| Reserved | Known required subsystem with no settled implementation |
| Superseded | Historical material retained for understanding but no longer current |

Subsystem status labels in the Open register (§3) never promote anything to Locked.

### 1.3 Evidence classes (`governance/status-model.md`, restating D2 §23.2)

- **Mechanical fact** — directly follows from existing locked rules.
- **Empirical finding** — supported by simulation, playtesting, or other explicit evidence (e.g., E9 usability playtest;
  Named-Outcome 21/21 trial).
- **Designer ruling** — a deliberate choice not mathematically forced by the system.
- **Recommendation** — a proposed preference not yet accepted.
- **Architectural constraint** — governs how systems interact, not what a mechanic numerically does.

An empirical finding does **not** by itself establish a designer ruling; an architectural constraint does **not**
establish a numerical mechanic. The source material is unusually careful about labeling evidence class — preserve that
discipline.

### 1.4 Status lifecycle and the only promotion path

Lifecycle (D2 §23.1): `Idea → Proposal → WIP → Independent Review → Simulation/Analysis → Designer Ruling →
Accepted → Locked/Canonical`. An item may return to WIP if evidence exposes a substantive problem.

The **8-step Promotion Rule** (D3 §21, restated in `governance/status-model.md`) is the **only** path from
non-canonical to canonical. For a proposal to become canonical ALL of these must happen:

1. its design question is explicitly identified;
2. competing alternatives have been considered where appropriate;
3. relevant simulation/analysis has been completed;
4. the human designer has accepted the ruling;
5. the mechanic is documented as a formal rule;
6. the Canonical Rules & Changelog document is updated;
7. the former proposal is marked Superseded or Locked in its source document;
8. implementation documentation is updated.

No current `proposals/` or `investigations/` item has completed this process. This is also registered as REQ-021 in
`_consolidation/requirement-register.md`.

### 1.5 LLM Governance Rules (D2 §24 — binding on any LLM working in this repo; relevant excerpts)

1. Treat Canonical Rules as authoritative.
2. Treat Proposals/WIP as non-canonical.
3. Treat Roadmap recommendations as implementation guidance.
5. Never infer a numerical threshold from an example unless explicitly locked.
6. **Never silently resolve an open designer fork.**
8. Prefer the current locked ruling over superseded source wording.
9. Preserve the distinction between empirical evidence and designer judgement.
10. State clearly when an answer depends on a proposal rather than a Canonical rule.
11. Never create a parallel Core resolution engine merely to implement a subsystem.
12. Never create a new primary resource or progression currency without explicit designer approval.
13. Treat an interface prototype as non-canonical unless a formal ruling says otherwise.
16. If new evidence materially challenges a locked rule, recommend reopening it rather than silently changing it.

Provenance rules (`governance/provenance.md`): `author_llm` is the original creator and is never overwritten;
`assessor_llm` may be a list (multiple assessment passes, earliest first — the 2026-08-31 independent second-model
assessment is appended as a second entry on audited docs); `last_modified_by_llm` is the most recent substantive
editor. Assessment is review, not promotion. Authorship for D1–D5 source documents is **not established**.

---

## 2. Locked upstream (what every Open decision builds on)

### 2.1 Canonical Core (D1 §2–§12; DEC-001…DEC-012 in `_consolidation/decision-register.md` §A)

d100 roll-under on 1–100 (`00` = 100); 100 always fails and is always a failed Double; all fractions floor;
24-attribute matrix; live derived statistics; Skill Tier/Cap/Starting Value; fixed 9-step **Core Test Transaction**
(`Roll → Outcome → Natural Roll Cost → Overflow → Failure XP / Advanced Skill effects → Recovery`);
Cost = natural roll; insufficient resource → Overflow → HP damage; unconditional final recovery; Failure XP =
`max(0, Roll − Skill)`; temporary Skill Roll Pool capped at Cap (remainder → General XP); Advanced Skills created
only by qualifying failed Doubles, Tier+1, full-formula Cap recompute, lineage-based resource domain.

### 2.2 Core Architectural Invariants (D1 §16; DEC-016)

18 invariants bind all future subsystems. Two are frequently decisive in open-subsystem reasoning:

- **Invariant 17:** No Universal Play subsystem may introduce a competing primary resource or progression economy.
- **Invariant 18:** Universal Play modules must build on the Core Test Transaction rather than replace it
  (a.k.a. "no parallel Core resolution engine").

### 2.3 S-1 Universal Opposed Contest (D1 §13; DEC-013) — **Canonical / Locked**, Complete

- Each participant performs an ordinary Core Test independently. Contest layer does not alter the underlying test.
- Outcome matrix: Success/Failure → A wins; Failure/Success → B wins; Success/Success → compare Quality;
  **Failure/Failure → Repeat contest** (both participants have already incurred all normal Core consequences).
- Quality measures (selected by contest type): **Margin** (`Skill − Roll`), **Blackjack** (`Roll`),
  **Hybrid Committed** (`Roll + max(0, Skill − 99)`). Quality only compares already-rolled successful tests and never
  modifies the historical roll, Cost, Failure XP, Double eligibility, or Recovery.
- Exact Quality tie → contest repeats (fresh round).
- Validated by simulation across Skill 10–250, Skill gaps up to 151. No further S-1 development planned.

### 2.4 S-2 Tier-1 Location Index provider — Zero-Step (D1 §14; DEC-014) — **Canonical / Locked, LIMITED**

- **§14.1 Zero-Step:** when a rule calls for a Tier-1 Location Index, exchange the tens and units digits of the
  attacker's **natural d100 roll** (37 → 73; 10 → 1; 1 → 10; 100/`00` → 100/`00`).
- **§14.2** Deterministic; no player choice; natural roll remains authoritative for every Core consequence; the
  transformed result is used **only** as the Tier-1 Location Index (read-only post-process).
- **§14.3 — What this lock does NOT establish (all still open):**
  - whether/when a scene uses Tier 0, Tier 1, or Tier 2 granularity;
  - Tier-0 and Tier-2 procedures;
  - **anatomical mapping from a Location Index to a zone**;
  - wound/armor/defense/Outcome-Effect interaction;
  - whether any later rule may select, modify, or consume a Location Index.
- **§15 Reserved Systems** (D1; DEC-015) locks only a *scope* statement: hit-location rules beyond Tier-1, wound
  activation/severity, Outcome Effects, armor, defense, incapacitation, death, healing, Rest, equipment,
  encumbrance, conditions, environmental hazards, difficulty grades, task/stakes adjudication, Extended Tests, NPC
  construction, magic/special-ability implementation, GM procedure, campaign procedures, setting content all remain
  outside the locked Core.

### 2.5 What "Ruled" means here (CRITICAL)

Decisions labelled **Ruled** below are **non-canonical designer rulings** recorded in
`_consolidation/decision-register.md` §B/§D and mirrored in Proposals/WIP. They are real human/designer rulings, but
they govern **candidate, non-canonical** material. **None has completed the 8-step Promotion Rule.**
Locked = Canonical (D1); **Ruled = non-canonical designer ruling; Open = no decision exists.**

---

## 3. The Open decision set (the deliverable)

Source of truth for what is "Open": `_consolidation/decision-register.md` §C (OPEN-001…OPEN-008, of which 006/007/008
are now closed) and Proposals/WIP §20 residual register. Everything in §3 is reproduced from the register/roadmap, not
from evidence files.

### Recently closed — do not treat as open

- **OPEN-006** (S-4 wound-severity "thresholds") — **Closed via DEC-035 (corrected).** Severity comes from the S-3
  gated Effect, not from an accumulated count; the old "numerical Light/Serious/Critical thresholds" framing was an LLM
  misreading and is superseded.
- **OPEN-007** (S-4 wound consequences) — **Ruled:** individual mechanical attribute penalties; magnitudes per wound
  (e.g. −1, −5, −30, −80, −100); more/more-severe wounds → more negatives; too many → "game overed" (faster for
  weaker characters); healing cost scales with magnitude.
- **OPEN-008** (S-4 non-attack Location Index generation) — **Ruled / Closed via DEC-037** (see §2.6/§3.1).

---

### OPEN-001 — H0 Rider B's two sub-options (S-2 non-attack provenance tie-break)

| | |
|---|---|
| **Register row** | Decision-register §C OPEN-001 |
| **What it is** | The S-2 Non-Attack Location Index Source investigation proposed a candidate provenance rule **H0** ("derive the Location Index from an existing governing Core Test's natural roll, or generate none") plus two riders. **Rider B** covers multi-test causal chains and has **two sub-options** which were **identified but "never adjudicated against each other"**: (1) governing test = the one that determines the affected character's own outcome, vs (2) the first causally-relevant test. Only sub-option (1) was drafted as a candidate. |

**Ruled/locked upstream:** DEC-020 (non-attack deferral: no Location Index for non-attack resolutions under any
framing) → **REOPENED** by DEC-036 (non-attack resolutions CAN produce Wounds via an Effect, if a Location Index can be
generated) → mechanism defined by DEC-037 (below). The H0 family + riders remain an **inert candidate record**, "the
starting hypothesis if this question is reopened," **not validated operative rules** (D5 §1, §3).

**Forks remaining:** Rider B's two sub-options must be adjudicated against each other if/when the non-attack question
is reopened. Also non-blocking residual flagged in the DEC-037 stress-test re-run: **H0 Rider B tie-break for Extended
Tests** (governing-test selection in multi-test chains that produce physical consequences). Do not assume a default.

**Considerations for an advisory opinion:** candidate does not pre-judge; Open decision owneer is S-2 non-attack
(triggered by S-4/S-7/S-8 design stages, **S-8 Stakes Gate flagged as most likely natural trigger**, Roadmap §13);
discipline: keep provenance (whose roll) separate from warrant (when an index is generated at all).

---

### OPEN-002 — Scene/campaign Location Tier selection (Tier 0 vs 1 vs 2)

| | |
|---|---|
| **Register row** | Decision-register §C OPEN-002 |
| **What it is** | Which location granularity a scene/campaign uses. Explicitly stated as **not narrowed or resolved** by DEC-017 (attack-side invocation policy) or DEC-014 (Zero-Step lock). Roadmap §9: the candidate invocation policy "does not determine whether a scene or campaign uses Tier 0, Tier 1, or Tier 2 in the first place. That selection question remains unresolved and is not narrowed to 'Tier 2 only' by this policy." |

**Ruled/locked upstream:** DEC-014 (Zero-Step = Tier-1 provider only; §14.3 keeps tier policy open); DEC-015
(Reserved scope). Tier 0 = no location state (Roadmap Phase 2 acceptance test: "Tier 0 creates no location state").
Roadmap Phase 2 remaining work: "Tier 0 and Tier-2 interface — open. Scene/campaign tier policy — ... still open."

**Forks remaining:** which tier a scene/campaign uses; when/if tiers switch mid-scene; how tier selection interacts
with the attack-side invocation policy and with U-09 Location Provider; roadmap §22 acceptance target says "location
granularity is configurable." No candidate decision or analysis exists for any of these.

---

### OPEN-003 — Anatomical mapping (Location Index → body/structural component)

| | |
|---|---|
| **Register row** | Decision-register §C OPEN-003 |
| **What it is** | The table/mechanism that turns a numeric Location Index (e.g. 73) into a named zone/body component. Explicitly open, "untouched" by any investigation. D1 §14.3 lists it as unresolved; Proposals/WIP §2.5 lists it as open. |

**Ruled/locked upstream and downstream consequences (important):**
- Zero-Step produces the numeric index (locked, DEC-014) but does not map it.
- **DEC-033:** localized Wound Effects require a Location Index; without a location there is **no Wound** — but damage
  and many other Effects (frozen, burned, shocked, bleed, etc.) still apply without one. OPEN-003 does not gate all
  non-attack resolution.
- **DEC-037 (passive fallback):** a physical impact with no roll of any kind outputs a **numeric stub** Location Index
  (e.g. `00` or `50`) routed through Zero-Step, explicitly "deferring anatomical naming until OPEN-003 locks."
- **DEC-028:** the three Tag+Location-gated S-3 Effects (**Disarm/Break Hold, Equipment Damage, Armor Bypass**) list the
  "anatomical mapping table (Canonical §14.3, unbuilt)" as a dependency.
- **DEC-019:** Structural Weak Points is classified **State 2** (Established, Not Yet Resolvable) precisely because the
  mapping does not exist yet.

**Forks remaining:** content of the mapping table; which zones/components exist; Tier-2 interaction (see OPEN-004);
whether special abilities/optional rules may later let a player choose or modify a Location Index (D1 §14.4 leaves this
as future optional-rule observation only, not current design).

---

### OPEN-004 — Tier-2 procedure/cost

| | |
|---|---|
| **Register row** | Decision-register §C OPEN-004 |
| **What it is** | The Tier-2 location procedure and its cost. Explicitly open. D1 §14.3 (scope retained) and Proposals/WIP §2.3/§2.5. Roadmap §9: "Tier 0 and Tier-2 interface — open." |

**Ruled/locked upstream:** DEC-014 (nothing about Tier-2 is locked; only Tier-1 provider is); DEC-015 (Reserved scope).
The two-d10 E9 usability evidence is limited to the **tested physical two-d10 method**; a single d100, digital roller,
and verbally announced result are untested and not covered by it (D1 §14.5). Derivation-cost comparison is a
structural observation, not a usability result (D1 §14.6).

**Forks remaining:** what Tier-2 granularity is, what it costs, whether any later rule may select/modify/consume a
Location Index (open per D1 §14.3). No candidate procedure exists.

---

### OPEN-005 — S-5…S-12 subsystem content

| | |
|---|---|
| **Register row** | Decision-register §C OPEN-005 |
| **What it is** | All of S-5 through S-12 are explicitly "Open"/"Reserved"/"Proposed" — no locked mechanic for any of them (D1 §15; D3 §3–§17; §20 register). S-4 is now ruled (DEC-032–DEC-037). **Note:** the S-3 *non-canonical* design forks are all ruled (DEC-023–DEC-030), but the S-3 subsystem itself remains non-canonical/Reserved within OPEN-005. |

**Ruled/locked upstream (shared):** Locked Core + S-1 (§2) + S-4 rulings (DEC-032…DEC-037, §3.1 below) + S-3 rulings
(DEC-023…DEC-031, §3.2 below) + S-2 architecture status (§3.3). The roadmap's decision-dependency grid
(Roadmap §4) — **decision dependencies, not a mandatory calendar**:

| ID | Decision | Dependency | Status |
|---|---|---|---|
| S-5 | Armor | S-3, S-4 | Open |
| S-6 | Defense | S-1 | Open |
| S-7 | Incapacitation/death | S-4 | Open — reopening trigger for S-2 non-attack deferral |
| S-8 | Difficulty/task/stakes | Core | Open — flagged most likely reopening trigger for S-2 non-attack deferral |
| S-9 | Extended Test progress | S-1 | Open |
| S-10 | Extended Test failure loss | S-9 | Open |
| S-11 | Rest/healing | S-4, S-7 | Open |
| S-12 | NPC compression | Preceding systems | Open |

Per-subsystem status (Proposals/WIP + Roadmap):

- **S-5 Armor (§5):** candidates only — Bypass-style interaction; tag-gated Sunder. Intended architecture: Armor
  Traits/Tags rather than a second durability economy. Final interaction unresolved. Note: **Armor Bypass** is a
  State-3 gated Effect (Tag + Location Index; DEC-028/030).
- **S-6 Defense (§6):** candidates — passive defense; active defense; defense as a normal contest participant;
  resource-costed reactions. A "Passive Guard (half-Skill, no PE cost)" proposal is **candidate only**. Evaluate for
  resource drain, number of rolls, survivability, tactical choice, resolution-step count. **S-3 defers to S-6:**
  the second-Effect defensive roll (DEC-026) and any contested-application mechanic (DEC-027, optional modifier only).
- **S-7 Incapacitation/Death (§7):** direction favours heroic resilience; HP = 0 is **not** automatically death;
  incapacitation mechanically distinct from ordinary resource depletion; permanent character loss comparatively
  uncommon. Major-vital/death-check concepts are proposals only. **No final death threshold is locked.** Roadmap
  Phase 5 requires a measured permanent-character-loss rate; no death threshold becomes Canonical until the decision
  gate passes.
- **S-8 Difficulty/Task/Stakes (§8):** universal difficulty required; direction: difficulty operates on the **Skill
  side**, not the natural die face (natural roll must stay authoritative for Cost, Failure XP, Double status,
  Recovery). A **Stakes Gate** is proposed: test only where meaningful uncertainty and meaningful consequences exist;
  routine actions should not be converted into repetitive resource expenditure. Exact difficulty grades and Failure XP
  interaction unresolved. **Home of the S-8 third-party-adjudication candidate (§4.1) and flagged reopening trigger for
  the non-attack deferral.**
- **S-9/S-10 Extended Tests (§9):** every interval is an ordinary Tiwas test (preserves Cost = Roll; Overflow → HP;
  Failure XP; failed Doubles; Advanced Skill creation; Recovery). **Progress method unresolved** — candidates: Margin
  accumulation vs Success count. **Failure behaviour unresolved** — candidates: stall (current direction favours stall
  as default), progress loss (potentially an optional complication), complication, conversion into another task state.
  **Progress must never become** spendable points, transferable currency, an XP substitute, or a second advancement
  economy (§9.4). (H0 Rider B surface intersection: multi-interval chains producing physical consequences.)
- **S-11 Rest/Healing (§11 status Reserved, Roadmap Phase 9):** Rest must not trivialize the resource identity; healing
  cost scales with wound magnitude (OPEN-007). Depends on S-4 + S-7.
- **S-12 NPC Compression (§16/Roadmap Phase 11):** NPCs use **compressed representations of the same system**, not a
  separate NPC engine; packages must resolve through the same Universal Play architecture. Exact grades/packages
  unresolved.

**Cross-cutting Reserved subsystems** (Reserved/Architectural Requirement, referenced by S-3 gated tiers): Conditions
(§10 — distinct from Tags), Tags (§11 — classification/permission metadata; not Conditions), Time/Action Economy
(§12 — unified temporal model serving combat and non-combat), Equipment (§13 — Traits/Tags, no second engine),
Environmental Hazards (§14), Magic/Special Abilities (§15 — emerge through Advanced Skills), Setting Modules (§17 —
may add content, must not redefine Core invariants).

**Forks remaining:** each subsystem's own candidate space as listed above; none will rule the next; sequencing between
open subsystems is a roadmap/implementation concern, not a design ruling.

---

### 3.1 Ruled upstream — S-4 (DEC-032…DEC-037) — the current Wound direction

Source: decision-register §B rows DEC-032…DEC-037 and Proposals/WIP §4. **Non-canonical designer rulings**
(2026-08-30). SUMMARY ONLY — the evidence files are pointer-referenced (§5).

- **DEC-032 (terminology):** **Injury** = HP damage (Track A). **Wound** = localized, lasting state, tracked
  numerically, distinct from HP (Track B). Each individual Wound functionally equivalent at base.
- **DEC-033 (activation):** Wounds are **exclusively** triggered as a selectable Effect from a successful S-1 contest;
  Wound realized as the **"Wounded" Condition** via S-3 Effect #2 (Impose Condition), not a standalone menu entry;
  **Overflow never causes Wounds**; localized Wound Effects require a Location Index; *Inflict Injury* and *Impose
  Condition: Wounded* both require a Location Index when selected as Effects; Overflow→HP is exempt (automatic).
- **DEC-034 (Track A/B):** both can apply from one hit, sequentially — Overflow resolves first, then Effect
  selection/application.
- **DEC-035 (severity, CORRECTED):** severity comes from the **S-3 gated Effect** (a "Serious wound" is a distinct
  Effect that by definition seriously wounds), **not** from an accumulated count. What varies by character is capacity
  to *endure* mechanical negatives. Prior "severity = accumulated count" recording was an LLM misreading and is
  superseded.
- **DEC-036 (reopen):** the S-2 non-attack deferral (DEC-020) is **reopened** for Wound Effects — non-attack
  resolutions can produce Wounds if an Effect is applied and a Location Index is generated.
- **DEC-037 (non-attack Location Index generation):** (1) **Primary provenance rule** — a character failing a
  governing Core Test against a hazard/obstacle/risk (Jump, Climb, Evasion, Spot Trap...) supplies that same **failed
  d100 roll** to Zero-Step for Tier-1 index generation; (2) the failure constitutes the hazard's "win" and a
  qualifying S-3 Effect (Inflict Injury or Impose Condition: Wounded) applies to the indicated location; (3) systemic
  threats (Drowning, Suffocation, Extreme Temperature, Poison) apply direct HP/Conditions with no Location Index;
  (4) passive fallback — no-roll physical impact outputs a numeric stub index (e.g. `00`/`50`) routed through
  Zero-Step, deferring anatomical naming until OPEN-003 locks. Stress-test re-run satisfied; non-blocking residuals:
  **H0 Rider B tie-break for Extended Tests** (→ OPEN-001) and **S-8 Stakes Gate dependency** for retroactive
  resolution.

### 3.2 Ruled upstream — S-3 (DEC-023…DEC-031) — the current Effect direction

Source: decision-register §D and Proposals/WIP §3.4. **Non-canonical designer rulings** (2026-08-29/30). All eight
session decisions ruled; **no S-3 design fork remains open**. SUMMARY ONLY — evidence pointer-referenced (§5).

- **DEC-023 (menu):** tiered menu. Base tier: **Inflict Injury (HP-only)** + **Open Retreat / Compel Yield**. Gated
  tiers unlock when their dependency locks: Position (Force Movement/Seize Position, Seize Tempo → Time/Action);
  Condition (Impose Condition, Bleed/Drain, Dizzy → Conditions); Equipment (Damage Equipment → Equipment); Defense
  (Guard Break → S-6); Location (Choose Location → S-2 invocation promotion). Disarm/Break Hold placed via Tag+Location
  gating (DEC-028).
- **DEC-024 (multiplicity):** flat **one-Effect-per-win**, no Quality-based scaling/purchasing; additional Effect needs
  a separate opposed roll (mechanism deferred).
- **DEC-025 (identity):** Effects granted **solely by declared outcome** of a successful S-1 contest; Skill name
  carries no mechanical weight; formal Skill-side tag/category system **rejected**.
- **DEC-026 (second-Effect roll):** separate opposed roll uses a **different, domain-appropriate Advanced Skill**; full
  9-step Core Test Transaction applies; target gets **no defensive roll until S-6 locks**; provisional resistance is
  non-canonical scaffolding only; no residual Advantage/Margin/state carries.
- **DEC-027 (application):** **auto-apply**, no secondary application contest; gate checks evaluated once, post-win;
  contested application rejected as default (deferred to S-6 as optional modifier).
- **DEC-028 (gating):** in-scope gated Effects (**Disarm/Break Hold, Equipment Damage, Armor Bypass**) require **both**
  a matching gear/ability Tag **and** a supporting Zero-Step Location Index (Tier 1+). Function Impairment and
  Incapacitation deferred out of S-3 scope (→ S-4/Condition, → S-7).
- **DEC-029 (S-3/S-4 boundary):** prototype-only; no interface work needed yet (base Injury is HP-only).
- **DEC-030 (partial match):** fail-and-fall-back — partial Tag/Location match fails the declared Effect entirely and
  applies Base Inflict Injury (HP-only); no partial/reduced/residual outcome.
- **DEC-031 (Quality's role):** Quality gates eligible Effects (threshold lookup post-win); every winning Quality ≥ 1
  guarantees at least one baseline-tier Effect; no Effect scaling by Quality; no additional Effect.

### 3.3 Ruled upstream — S-2 architecture status

- **Attack-side invocation/warrant policy (DEC-017, 018, 019):** candidate four-state model + Named-Outcome Test +
  W3 reference cache accepted as the current non-canonical working direction for *when* a Location Index is warranted
  (attack-side only). Procedural rules: disjunctive compound-objective evaluation; stale-objective invalidation;
  S-1 winner-only eligibility (empirical, replicated); **lazy evaluation is a design inference with a lower evidence
  class** (D3 §2.1A / v1.4.2 revision record). Explicit-only objectives (DEC-018). Structural Weak Points = State 2
  (DEC-019).
- **Non-attack deferral (DEC-020/021/022), status as of 2026-08-30:** REOPENED by DEC-036; mechanism defined by
  DEC-037 (§3.1). The categorical "no index under any framing" deferral is therefore **superseded for wound-producing
  non-attack resolutions** and now routed through the DEC-037 model; the H0 family is inert (§ OPEN-001). Full record:
  `investigations/tiwas-s2-non-attack-location-source-closure-record-v1.2.md` (pointer; closure record, not rules).

---

## 4. Additional open items surfaced this session

### 4.1 S-8 candidate — Third-Party Adjudication of Mutual-Failure Opposed Contests

Source: `investigations/tiwas-s8-third-party-adjudication-mutual-failure-candidate-v1.md`
(pointer; provisional candidate, NOT a ruling, NOT to be implemented as active logic).

**Problem identified:** S-1's locked outcome matrix (D1 §13.1) shows Failure/Failure → **Repeat contest**. When both
participants of an opposed contest fail, no rule currently determines a winner of the *contest itself* — each resolves
Core Failing Forward independently, leaving the competition without an outcome. Confirmed as a genuine open gap (no
Locked rule contradicts it).

**Proposed candidate** (for advisory discussion only): a **Failure Margin** term (`Roll − Skill`; lower = failed by
less) + a third-party adjudication roll against an appropriate Skill (GM/NPC/party). Adjudicator succeeds → winner =
lower Failure Margin; adjudicator fails → fallback unresolved among GM fiat / coin-flip / declared draw.

**Open sub-questions (not resolved by the candidate — these are live items an advisory opinion may address):**

1. Which skill(s) are valid for the adjudication roll — fixed to one, or GM/table choice?
2. Does the adjudicator's own Quality modulate the outcome (confidence/detail), or is success purely binary
   (can-distinguish / cannot-distinguish)?
3. On adjudicator failure, which fallback (GM fiat / coin-flip / declared draw) is the default — or is this left fully
   to table discretion?
4. Edge case: if the adjudicator's own roll is a **failed Double**, do they unlock an Advanced Skill mid-adjudication?
   Desirable, or should adjudication rolls be exempted from the Advanced Skill trigger?
5. Does this mechanic generalize beyond crafting competitions to any mutual-failure opposed contest, or is it scoped
   narrowly to non-combat/task-based contests?

**Constraint surfacing for an opinion:** the candidate reuses existing primitives (mirrors locked Margin; reuses
d100 roll-under; does not modify historical rolls). It adds a **procedure layer**, not a new roll type — hence it needs
its own ruling rather than inheriting S-1's Locked status. Structurally adjacent to S-3's open Quality-role question
(which the DEC-031 ruling resolved for Effects); a ruling on one may inform the other but neither should resolve the
other silently.

### 4.2 DEC-037 residual flags (non-blocking, cross-subsystem)

- **H0 Rider B tie-break for Extended Tests** → joins OPEN-001.
- **S-8 Stakes Gate dependency** for retroactive resolution of hazard events → relevant to OPEN-005/S-8 and the
  non-attack deferral reopening triggers (Roadmap §13: S-8 Stakes Gate is the most likely reopening trigger).

---

## 5. Pointer-referenced evidence (do NOT treat as rules; verify before trusting them as facts)

These are the evidence/narrative files behind the rulings above. They are **not** reproduced inline by design. Each is
listed as **path + one-line status**. Originals of many live under `sources/incoming/` (raw / unprocessed); the
processed/consolidated copies referenced by the registers live under `investigations/`.

- `investigations/tiwas-s3-designer-rulings-and-handoff-2026-08-29.md` — in-session S-3 rulings record (DEC-023…DEC-030).
- `investigations/tiwas-s3-documentarian-handoff-report-dec028-2026-08-30.md` — dec028/DEC-031 handoff report (Quality's
  role; includes 8-model LLM survey meta-analysis pointer).
- `_consolidation/requirement-register.md` REQ-021 — the Promotion Rule as a tracked requirement.
- `investigations/tiwas-s4-documentarian-handoff-report-2026-08-30.md` — S-4 ruling thread handoff (DEC-032…DEC-037 source text).
- `investigations/tiwas-s4-dec035-original-wording-and-correction-2026-08-30.md` — verbatim designer wording + correction for DEC-035.
- `investigations/tiwas-s4-dec037-stress-test-rerun-2026-08-30.md` — literal 14-scenario re-run of the S-2 non-attack
  stress set against DEC-037 (non-blocking flags noted).
- `investigations/tiwas-s2-non-attack-location-source-closure-record-v1.2.md` — closure record for the non-attack
  investigation; H0/Rider A/Rider B inert-candidate details; reopening conditions; stress-test scenario set.
- `investigations/tiwas-s2-hit-location-investigation-v5-synthesis.md` — S-2 invocation/warrant candidate source.
- `investigations/gemini-s4-chat3-deepseek-response-and-decision-request-2026-08-30.md` and sibling gemini/deepseek
  files in `investigations/` — multi-model survey/assessment trail for S-4 and S-3 (survey transcripts, advisory).
- `sources/incoming/opencode-handoff-report.md` — handoff + the standing "no single merged file" instruction (overruled
  for this one file only, §0 above).

Also present but **excluded from this snapshot by scope**: `sources/incoming/tiwas-tttrpg-merge/` (the historical
draft trail — closed/superseded material, included only as an exclusion); closed investigation drafts for already-ruled
subsystems; raw chat exports under `sources/incoming/` summarised by the consolidated registers.

---

## 6. What a good advisory response looks like

For any Open decision you are asked about:

1. State the upstream locked/ruled constraints (§2, §3.1–3.3) that the new material must not violate.
2. State the forks that genuinely remain open (do not invent closures; do not pick a fork and call it the ruling).
3. Hedge every design proposal as **a proposal toward a designer ruling**, with the evidence class it would rest on,
   and note where simulation would be required before a ruling should be accepted (8-step Rule, §1.4).
4. Flag any tension you notice between source documents as a conflict for the human to resolve — do not resolve it.
5. Remember: nothing here is Canonical unless labelled Canonical/Locked; the human rules; OpenCode verifies.