---
document:
  title: "Tiwas S-3 Outcome Effects — Investigation (Draft, non-canonical)"
  version: "v0.1-draft"
  status: "Non-canonical investigation proposal — S-3 remains Open. No item herein is a Tiwas rule."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
---

# Tiwas S-3 — Outcome Effects: Design Investigation (Draft)

**Status: Open.** This draft opens the S-3 (Outcome Effects) design investigation. It
compiles existing evidence, states the design question explicitly, and identifies the
unresolved designer forks. It does **not** promote any candidate to Canonical status —
per the 8-step Promotion Rule (Proposals/WIP §21) and the LLM governance rules
(Roadmap §24, especially Rule 6), it presents options and escalates the real designer
decisions rather than silently resolving them.

Governing routing:
- S-3 is the first open subsystem in the Residual Decision Roadmap after the locked
  S-1 (Roadmap §4 row 3, dependency: S-1). S-2 is a parallel workstream, partially
  locked / WIP, converging with S-3 at S-4 (Roadmap §4 note, §6.1).
- Canonical branch: S-3 must build on the Core Test Transaction (REQ-018) and must not
  introduce a competing primary resource/progression economy (REQ-017).

---

## 1. Why this investigation is opened

Tiwas resolves opposed contests into "meaningful state change rather than simple HP
attrition" (Proposals/WIP §3). The Outcome Effects subsystem (S-3) is the mechanism
that converts a contest result into that state change. It is the first open subsystem
whose only decision dependency (S-1, the contest primitive and its Quality measures) is
already locked.

The project itself has already recorded a short candidate Effect menu, a candidate
purchasing model, and one non-negotiable architectural constraint (Proposals/WIP
§3.1–§3.3). What is missing and unresolved: the final menu, the trigger rules, the
purchasing rules, and every numerical threshold (Proposals/WIP §3.1, §20 row S-3;
Roadmap §4 row S-3).

---

## 2. Locked basis S-3 builds on (Canonical)

The following are Canonical and constrain all S-3 work:

- **S-1 Opposed Contest** (Canonical Rules §13, DEC-013), including:
  - Outcome matrix (Success/Failure/Quality-compare/Repeat) — §13.1.
  - Quality measures selected by contest type: **Margin** = `Skill − Roll`;
    **Blackjack** = `Roll`; **Hybrid Committed** = `Roll + max(0, Skill − 99)` —
    §13.2. Quality "only compares already-rolled successful tests."
  - Quality never modifies the historical roll, Cost, Failure XP, Double eligibility,
    or Recovery — §13.2. This is the authoritative statement of the invariant that
    Proposals/WIP §3.3 restates as "Effects must never modify the historical die roll."
  - Quality selection guidance and GM override — §13.3.
  - Failure/Failure repeat and exact-Quality-tie repeat — §13.4, §13.5.
- **Core resolution invariants** (Canonical Rules §16 / requirement register
  REQ-001–018): roll-under success, `00`=100, 100 always fails and is always a
  qualifying failed Double, all fractions floor, Cost = natural roll, Overflow → HP
  damage, Failure XP = max(0, Roll − Skill), Recovery always last, live derived stats,
  and the two Universal Play constraints (REQ-017 no competing economy, REQ-018 build
  on the Core Test Transaction).

**Consequences for S-3:**
- Any "Advantage" that S-3's Effect purchasing consumes is derived from the S-1 Quality
  measures (or other already-locked contest outputs), not a new currency (REQ-017).
- The natural roll remains authoritative for Cost and all Core consequences. No Effect
  may rewrite it (Canonical §13.2; REQ-018).

---

## 3. Existing evidence (non-canonical, evidence-class labelled)

### 3.1 Candidate Effect menu — Proposals/WIP §3.1 (Evidence class: Design Direction / Proposed)

The project already prefers a **short universal Effect menu**. Ten candidates are listed:

1. Inflict Injury
2. Impose Condition
3. Disarm / Break Hold
4. Force Movement / Seize Position
5. Seize Tempo
6. Guard Break
7. Bleed / Ongoing Drain
8. Open Retreat / Compel Yield
9. Damage Equipment
10. Choose Location

**Not resolved:** which of these survive the final menu, their trigger rules, and their
mutual relationships.

### 3.2 Candidate purchasing model — Proposals/WIP §3.2 (Evidence class: Proposal)

> - one successful contest may produce a basic/free effect;
> - additional effects may require Net Advantage / Quality bands;
> - some effects may be gated by Tags;
> - some exceptional effects may be tied to qualifying successes.

Explicitly "not canonical." This is the *only* sketched purchasing direction and is
under-specified (no band boundaries, no "Net Advantage" definition beyond the S-1
Quality measures).

### 3.3 Non-negotiable constraint — Proposals/WIP §3.3 (restated Canonical §13.2)

> Effects must never modify the historical die roll.

This is a restatement of a Canonical invariant (see §2), so it is effectively locked
regardless of S-3 status.

### 3.4 S-3/S-4 interface and Phase 3 acceptance — Roadmap §10 (Evidence class: Architectural / implementation guidance)

Roadmap Phase 3 (S-3) states:
- Status: S-3 Open, S-4 Open.
- Implement the **structural Effect interface first**; candidate Effects include Injury;
  Condition; Disarm / Break Hold; Movement / Position; Tempo; Guard Break; Bleed /
  Drain; Retreat / Yield; Equipment Damage; and Location selection.
- S-3 may prototype how an Effect passes harm/state information to a prospective S-4
  Wound Engine — **an architectural exercise, not a lock on S-4**. It must not silently
  establish wound-severity thresholds, activation triggers, disability effects, or
  death checks.
- **Prospective two-track harm interface** (Track A: PE/MP → Overflow → Global HP;
  Track B: Location → Wound → Condition/Disability/Death Check).
- **Phase 3 acceptance criteria:** Effects create real state changes; Effects do not
  alter historical rolls; empty PE/MP is not automatic defeat; Overflow remains HP
  damage; HP = 0 is not automatic death; Wounds are not a second HP pool.
- **Simulation gate:** measure Effect frequency, exchange length, resource expenditure,
  wound frequency, severe injury, and state-change density. "Do not lock numerical
  thresholds without required evidence and a designer ruling."

### 3.5 S-2 State-3 findings relevant to S-3 — Roadmap §9 / Proposals §2.5 (Evidence class: Empirical finding / designer inference)

The completed S-2 investigation flagged that several candidate Effects are **currently
unanchored to location**:
- Disarm, Equipment Damage, Function Impairment, Armor Bypass, Incapacitation are all
  currently **State 3** (Outcome Plausible but Location-Dependence Unresolved).
- S-3 has **at least one plausible design path (Margin/Tag-gated triggering) that would
  not require location at all** for these outcomes.
- The Roadmap explicitly forbids treating this as a settled assumption: "Future
  subsystem design work should treat this as an open fork, not a settled assumption in
  either direction." (Roadmap §9; see Roadmap §24 Rule 6.)

**Relevance:** whether an Effect like Disarm or Equipment Damage consumes a Location
Index is an **open S-3 design fork**. It is also coupled to the broader S-2 non-attack
deferral / location architecture, which is itself gated on S-4/S-7/S-8. S-3 must not
silently assume location is the delivery mechanism.

### 3.6 Adjacent subsystems — early status (Evidence class: Design Direction)

S-3 interacts with subsystems that remain Open:
- **S-4 Wounds (Track B):** Wound states Light/Serious/Critical are intended but all
  activation thresholds/formulas/consequences unresolved (Proposals/WIP §4). S-3 must
  not lock these.
- **S-5 Armor:** Bypass-style vs tag-gated Sunder; prefers Tags over a second durability
  economy (Proposals/WIP §5).
- **S-6 Defense:** passive/active candidates, one resource-costed "Passive Guard"
  candidate (Proposals/WIP §6), all Open.
- **Conditions (U-12), Tags (U-14), Equipment (U-10/U-14), Time/Action (U-13):** each
  Open; S-3's "Impose Condition" and "Damage Equipment" Effects will interface with
  these but none of them are locked.

---

## 4. Design questions — RULED and OPEN

Consistent with Roadmap §24 Rule 6 ("never silently resolve an open designer fork") and
REQ-021, the items below are recorded with their current state. Q-S3-1 through Q-S3-4
have been **ruled by the human** (2026-08-29, recorded in
`_consolidation/decision-register.md` §D, DEC-023–DEC-030, and filed in `proposals/` §3.4).
The remaining items are **open** and are surfaced for human/designer ruling.

### Q-S3-1 — Final Effect menu scope — **RULED (DEC-023)**
**Tiered Effect menu**: base tier = **Inflict Injury (HP-only)** + **Open Retreat /
Compel Yield**; five gated tiers keyed to their owning subsystem's lock status
(Position → Time/Action; Condition → Conditions; Equipment → Equipment; Defense → S-6;
Location → S-2 invocation promotion). **Disarm / Break Hold** is placed via Q-S3-3's
combined Tag+Location gating (DEC-028); its specific tier and partial-match behaviour
depend on Q-S3-3a.

### Q-S3-2 — Purchasing / Advantage basis — **RULED (DEC-024)**
**Flat one-Effect-per-win.** No Quality-based scaling, no purchasing of additional
Effects off a single win. A second/additional Effect requires a **separate opposed roll**
— mechanism not yet designed, deferred to the Effect Identity & Multi-Effect Opposition
thread (Q-S3-2b).

> This supersedes the Proposals/WIP §3.2 candidate (Quality/Net-Advantage bands) as the
> basis for effect multiplicity. The two-track/Quality machinery remains relevant only
> as the *identity* of a single Effect, not as a multiplicity ladder.

### Q-S3-3 — State-3 Effects — **RULED (DEC-028)**
**Combined Location + Tag gating** for the in-scope S-3 Effects (**Disarm/Break Hold,
Equipment Damage, Armor Bypass**): triggering requires both a matching Tag **and** a
supporting Zero-Step Location Index (Tier 1+). **Function Impairment and Incapacitation
are deferred OUT of S-3 scope** (Incapacitation → S-7; Function Impairment →
S-4/Condition). Dependencies: starter Tag vocabulary (Tags §11, Reserved); anatomical
mapping table (Canonical §14.3, unbuilt); S-2 invocation policy (§2.1A) unaffected.

### Q-S3-4 — S-3/S-4 boundary — **RULED (DEC-029)**
Confirmed prototype-only; **no S-3/S-4 interface work needed yet** (base-tier Injury is
HP-only, no wound produced). Roadmap §10 boundary holds, dormant until a
wound-producing Effect is proposed. The S-4 *direction* (location-based injury from
repeated hits; no Location Index → no Injury; per-location hit-history by GM
adjudication; healing open) is recorded as a **steer for a future S-4 investigation**,
not an S-3 ruling and not Canonical.

### Q-S3-2a, Q-S3-2b, Q-S3-5, Q-S3-3a — Effect identity, gating & multi-effect opposition — **OPEN**
These are split into a dedicated non-canonical investigation thread:
`investigations/tiwas-s3-effect-identity-and-multi-effect-opposition-investigation-v0.1-open.md`
(status Open, no rulings yet on its open items). It tracks:
- **Q-S3-2a** (DEC-025) — Effect naming identity/gating (tag/category system vs.
  declared intent).
- **Q-S3-2b** (DEC-026) — Second-Effect opposed-roll mechanism (same/different/flat
  Skill; target defensive roll gated on S-6 being Open).
- **Q-S3-5** (DEC-027) — Auto-apply vs. contested application (only auto-apply is
  buildable while S-6 is unlocked).
- **Q-S3-3a** (DEC-030) — Partial Tag/Location match behavior: fail-and-fall-back-to-
  plain-damage vs. partial/reduced outcome.
- **Disarm/Break Hold** specific tier assignment (carried from Q-S3-1), informed by
  Q-S3-3a.

---

## 5. Recommended next steps (not performed — require approval / further rulings)

These follow the promotion lifecycle (Idea → Proposal → WIP → Review → Simulation →
Ruling → Accepted → Locked) and are **recommendations only**:

1. **Ruled:** Q-S3-1 (Tiered menu, DEC-023), Q-S3-2 (Flat one-Effect-per-win, DEC-024),
   Q-S3-3 (Combined Tag+Location gating, DEC-028), Q-S3-4 (S-3/S-4 boundary, DEC-029) —
   recorded in `_consolidation/decision-register.md` §D and filed in `proposals/` §3.4.
2. **Still open:** Q-S3-2a (DEC-025), Q-S3-2b (DEC-026), Q-S3-5 (DEC-027), Q-S3-3a
   (DEC-030), and the Disarm/Break Hold tier placement, all in the dedicated Effect
   Identity & Multi-Effect Opposition thread.
3. Once the open forks are ruled, formalize a **non-canonical S-3 proposal variant** in
   `proposals/` (either replacing/amending Proposals/WIP §3 or as a companion),
   preserving provenance metadata.
4. Design the **structural Effect interface** first (per Roadmap §10), scoped to the
   ruled tiered menu.
5. Prototype the **S-3/S-4 harm hand-off** as an architectural exercise only — no S-4
   thresholds locked.
6. Run the **Phase 3 simulation gate** (Effect frequency, exchange length, resource
   expenditure, wound frequency, severe injury, state-change density) before any
   numerical threshold is proposed for lock.
7. Only after the full 8-step Promotion Rule — including human acceptance and Canonical
   update — would any of this become Canonical.

---

## 6. Known limitations of this draft

- **No simulation or playtest data yet.** The Roadmap's Phase 3 simulation gate has not
  been run for S-3; no empirical findings exist to support any numerical threshold here.
- **Draft authored in this session; rulings externally reviewed.** This draft was
  authored and assessed by the same LLM, but the designer rulings it records
  (Q-S3-1–Q-S3-4) were produced in a separate conversation (human + Claude Sonnet 5)
  and independently reviewed by opencode/big-pickle before filing. An independent
  second review of the draft itself is still recommended per `governance/provenance.md`.
- **Adjacent subsystems are Open.** S-4, S-5, S-6, Conditions, Tags, Equipment, and
  Time/Action are all unresolved; any S-3 interface assumptions toward them are
  provisional.
- **Provenance of underlying S-3 content (Proposals/WIP §3) is not established** — the
  source corpus's own authorship was recorded as `not established` in the original
  consolidation.

---

## 7. Status of this document

- Status: **Non-canonical investigation proposal (draft).**
- It does **not** alter Canonical Rules.
- Q-S3-1 (Tiered menu, DEC-023), Q-S3-2 (Flat one-Effect-per-win, DEC-024), Q-S3-3
  (Combined Tag+Location gating, DEC-028), and Q-S3-4 (S-3/S-4 boundary, DEC-029) are
  **ruled** (non-canonical), recorded in `_consolidation/decision-register.md` §D and
  filed in `proposals/` §3.4.
- Q-S3-2a (DEC-025), Q-S3-2b (DEC-026), Q-S3-5 (DEC-027), Q-S3-3a (DEC-030), and the
  pending Disarm/Break Hold tier placement remain **open**, tracked in the dedicated
  Effect Identity & Multi-Effect Opposition thread.
- It is placed in `investigations/` as evidentiary/analytical work product feeding the
  Proposals/WIP layer, consistent with how D4/D5 (the S-2 investigations) are handled.
