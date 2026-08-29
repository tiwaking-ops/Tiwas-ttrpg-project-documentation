# Tiwas — S-3 Outcome Effects: Round 1 Candidate Analysis

**Document Version:** v1.0 (new document)
**Document Status:** Non-canonical design investigation — Round 1 of N
**Rule Authority:** None. This document creates no game mechanics and modifies no other document.
**Methodology:** Replicates the S-2 Non-Attack Location Index Source investigation's Round 1 discipline (see `Tiwas___S3_Handoff_Context-for_new_chat.md` §4).
**Governing hierarchy:** Canonical Rules & Changelog v1.3 (authoritative) → Proposals/WIP v1.4.3 (this work's home once accepted) → Implementation Roadmap v1.4.3 (sequencing only).
**Promotion status:** Nothing in this document is canonical or accepted. Promotion requires the full eight-step process (Proposals §21).

---

## 0. Scope Guards

This round does **not**:

- reopen S-1 (Opposed Contest — Canonical §13, locked);
- reopen S-2's Tier-1 provider (Zero-Step — Canonical §14.1–§14.2, locked);
- reopen or modify S-2's attack-side invocation/warrant policy (Proposals §2.1A, candidate/non-canonical);
- reopen the S-2 non-attack Location Index deferral (Proposals §2.5A / Closure Record v1.2 — ruled, closed pending S-4/S-7/S-8);
- decide S-4 wound activation, severity, or thresholds (may prototype the Effect→Wound interface only, per Roadmap §10);
- decide S-5 (Armor) or S-6 (Defense) mechanics, even where a candidate Effect (Damage Equipment, Guard Break) touches those subsystems;
- lock any numerical threshold — Quality bands, Tag requirements, XP costs, effect counts. Candidate **structure** only.

This round **does**:

- separate the trigger question from the menu/purchasing question, per the handoff's core methodological requirement;
- explicitly surface — without resolving — the location-vs-Margin/Tag delivery-mechanism fork for each S-3 candidate Effect that overlaps S-2's State-3 table (handoff §6);
- tag every claim with an evidence class per Roadmap §23.2.

---

## 1. Locked Inputs (Restated, Not Reopened)

### 1.1 Canonical invariants binding on any S-3 candidate

*[Mechanical fact — directly follows from Canonical Rules]*

| Invariant | Source | Constraint on S-3 |
|---|---|---|
| Cost = natural roll | Canonical §7 | An Effect cannot change what the triggering test cost. |
| Overflow → HP | Canonical §7 | Unaffected by Effect selection. |
| Failure XP = max(0, Roll − Skill) | Canonical §9 | Unaffected by Effect selection. |
| Recovery occurs last, unconditionally | Canonical §8, Invariant 16 | An Effect cannot delay, skip, or reorder Recovery. |
| Quality never alters the historical roll, Cost, Failure XP, Double eligibility, or Recovery | Canonical §13.2 | Any Quality-gated Effect-purchasing candidate may only *read* Quality, never feed back into it. |
| No competing primary resource/progression economy (Invariant 17) | Canonical §16 | Any candidate introducing a spendable/persistent "Effect Points" pool is prohibited unless proven non-persistent and non-transferable (see §3.5 below). |
| Universal Play modules call the Core Test Transaction, never replace it (Invariant 18) | Canonical §16 | A candidate that resolves Effects via an independent resolution mechanism (a second, non-Core roll standing outside the Test Transaction) is prohibited unless that roll is itself a full Core Test Transaction. |
| Effects must never modify the historical die roll | Proposals §3.3 | Explicit S-3-specific non-negotiable, restated here as binding on every candidate below. |

### 1.2 S-1 status (locked, informs but is not reopened)

*[Mechanical fact]* S-1 provides: independent Core Tests per participant; a Success/Failure outcome matrix; three Quality measures (Margin, Blackjack, Hybrid Committed) selected per contest type; exact-tie and Failure/Failure repeat rules (Canonical §13). Quality is available as a **read-only** input to any S-3 trigger/purchasing candidate that wants to use it, subject to §13.2 above.

### 1.3 S-2 status (locked/candidate, informs but is not reopened)

*[Mechanical fact + design inference, distinguished]*

- **Locked:** Zero-Step Tier-1 Location Index provider (Canonical §14.1–§14.2) — deterministic, read-only post-process of the natural roll.
- **Non-canonical candidate, accepted for further development:** attack-side invocation/warrant policy (Proposals §2.1A) — four-state model; Location Index generation requires an explicitly named distinct outcome, anchored location-dependence, and a resolving mechanism.
- **Ruled (non-canonical governing position):** non-attack physical resolutions generate no Location Index (Proposals §2.5A).
- **State-3 finding (candidate, non-canonical):** Disarm/Break Hold, Equipment Damage, Function Impairment, Armor Bypass, and Incapacitation/Kill are currently classified as *"Outcome Plausible, Location-Dependence Unresolved"* — i.e., whether location is even the delivery mechanism for these outcomes is an open fork, explicitly handed to S-3 (and S-5/S-7/S-10) to resolve (Proposals §2.1A).

---

## 2. The Two-Part Question, Restated and Kept Separate

Per the handoff methodology, these are treated as **independent questions** throughout this document. No candidate below is permitted to answer one by silently assuming an answer to the other.

| Question | What it asks | What it explicitly does not ask |
|---|---|---|
| **Q1 — Trigger** | Does a given resolved contest/test grant *any* Effect at all, and if so, under what condition? | Which Effect, how many, or what it requires beyond the trigger condition itself. |
| **Q2 — Menu / Purchasing** | Given that an Effect is available, which Effect(s) from the candidate menu (Proposals §3.1) may be selected, and what — if anything — gates access to specific ones? | Whether an Effect is granted at all in the first place. |

A third, narrower question is inherited directly from S-2 and must not be quietly folded into either Q1 or Q2:

| Question | What it asks |
|---|---|
| **Q3 — Delivery mechanism (per-Effect)** | For each candidate Effect that overlaps S-2's State-3 table, does *triggering that specific Effect* require a Location Index (location as delivery mechanism), or does it trigger off Margin/Quality/Tags (a location-independent mechanism)? |

Q3 is not "does S-3 need location" in general — it is a **per-Effect** fork, since some candidate Effects (e.g., Choose Location itself) are self-evidently location-related while others (e.g., Seize Tempo) plausibly never touch location at all.

---

## 3. Candidate Trigger Models (Q1)

Each candidate is evaluated against the Canonical invariants in §1.1. A candidate that fails this check is **excluded outright**, mirroring how S-2 Round 1 excluded Candidate B (ad-hoc GM roll) for violating Invariant 18.

### 3.1 Candidate T1 — Universal Free Effect on Any Success

*[Design inference, carried from existing non-canonical Proposal wording, Proposals §3.2 bullet 1]*

Every successful Core Test or S-1 contest automatically grants exactly one basic/free Effect, with no additional gate.

- **Invariant check:** Passes. Uses the existing Success outcome directly; introduces no new roll, no new resource, no alteration of Cost/Overflow/XP/Recovery.
- **Consequence:** Maximizes Priority 3 (minimum resolution steps) at the possible cost of Priority 1 (granular simulation) — every success becomes tactically identical in *access*, differentiated only by which Effect is chosen.

### 3.2 Candidate T2 — Quality-Threshold Gate

*[Design inference]*

An Effect is granted only if the contest's Quality (Margin/Blackjack/Hybrid, per Canonical §13.2) meets or exceeds a threshold. Ordinary successes below threshold produce no Effect, only the base outcome (e.g., damage).

- **Invariant check:** Passes, provided the threshold check only *reads* Quality and never modifies the historical roll, Cost, or XP (Canonical §13.2 explicitly permits Quality to be read; it does not permit Quality to become a second write-channel into the Core Test).
- **Consequence:** Ties Effect access to precision/force/commitment (whichever Quality mode governs the contest), which raises Skill-scaling questions the Quality-mode guidance in Canonical §13.3 already flags (Blackjack/Hybrid distinctiveness "becomes meaningful primarily once relevant Skills are sufficiently high"). At low Skill this could make Effects rare-to-absent, which may or may not be the intended design feel — flagged, not resolved, in §8.

### 3.3 Candidate T3 — Hybrid (Free Basic + Quality/Tag-Scaled Additional)

*[Design inference, restates the current Proposal §3.2 draft in full]*

- One successful contest grants one basic/free Effect unconditionally (as T1).
- Additional Effects beyond the first may be granted where Net Advantage/Quality bands are met.
- Some specific Effects are Tag-gated regardless of Quality (weapon/power/creature must carry the relevant Tag).
- Some exceptional Effects require a qualifying success (e.g., a Double, or Quality above a high band).

- **Invariant check:** Passes, for the same reasons as T1 and T2 combined; the "additional" layer is strictly additive and never subtracts from or reorders the base Core Test Transaction.
- **Consequence:** This is the current non-canonical Proposal draft (§3.2) — Round 1 does not need to invent it, only formalize and stress-test it against T1/T2/T4 as genuine alternatives, per the handoff's requirement not to let a pre-existing draft masquerade as an unreviewed default.

### 3.4 Candidate T4 — Opposed-Contest-Exclusive Trigger

*[Architectural constraint, drawn directly from Proposals §3's framing]*

Effects are granted only from S-1 opposed contests, never from unopposed Core Tests. Rationale: Proposals §3 states the design intent as *"Tiwas is intended to resolve opposed contests into meaningful state change"* — a narrower claim than "every successful test."

- **Invariant check:** Passes on its own terms; it is a *restriction* of T1/T2/T3's scope, not a new mechanism.
- **Consequence:** This is not a trigger model in the same sense as T1–T3 — it is an orthogonal scope question ("which category of test is Effect-eligible at all") that must be answered *in addition to* choosing T1, T2, or T3, not instead of them. Flagged as a compound decision, not a fourth alternative on the same axis. See §8, Decision Point 5.

### 3.5 Candidate T5 — Dedicated "Effect Points" Resource *(Excluded)*

*[Architectural constraint — hard exclusion]*

A candidate under consideration during drafting proposed a persistent, spendable "Effect Points" pool: successes deposit points into the pool; players later spend accumulated points to purchase Effects across multiple exchanges.

- **Invariant check: FAILS.** This is a second progression/resource economy in the Invariant 17 sense (Canonical §16; Roadmap §2) — it persists across tests, accumulates, and is spendable independently of the triggering test's own Cost/Overflow/XP, which is precisely the shape Invariant 17 excludes. It is structurally identical to the kind of "second advancement economy" the Extended-Test Progress rule (Canonical/Proposals §9.4) is explicitly barred from becoming, applied here to Effects instead of Extended Tests.
- **Disposition:** Excluded outright, mirroring S-2 Round 1's exclusion of ad-hoc GM rolls (Candidate B) for violating Invariant 18. Retained here only as a record of a rejected candidate, per Roadmap §24 Rule 15 (superseded/rejected material is retained, not deleted).
- **Note — narrower, non-excluded variant:** An **ephemeral, single-test-scoped** count derived directly from that test's own Quality (e.g., "this success's Margin determines how many Effects *this exchange* may draw from the menu, discarded at the end of the transaction") does **not** fail the invariant check, since it is a formula output, not a stored/transferable currency — structurally analogous to how Quality itself is read-only and non-persistent (Canonical §13.2). This variant survives as part of Candidate T2/T3's threshold mechanics, not as a standalone T5.

### 3.6 Candidate T6 — Independent "Effect Roll" *(Excluded as stated; conditionally salvageable)*

*[Architectural constraint — hard exclusion of the stated form]*

A candidate proposed a second, dedicated d100 roll — separate from the Core Test that produced the Success — used solely to determine whether/which Effect is granted.

- **Invariant check: FAILS as stated.** A free-standing bonus roll outside the Core Test Transaction is exactly the "competing... resolution" Invariant 18 excludes (Canonical §16) — it duplicates rather than calls the Transaction.
- **Conditionally salvageable form:** If the "second roll" were reformulated as a genuine, independent Core Test in its own right (own Cost, own Overflow exposure, own Failure XP, own Recovery — i.e., not a free roll, but an actual additional Test Transaction the character pays for), it would no longer violate Invariant 18, since it would *be* the Core Test Transaction rather than compete with it. This reformulation is structurally close to T2/T3's Quality-gating and is not separately pursued as its own candidate; noted for completeness only, mirroring how S-2 Round 1 recorded a rejected candidate's salvageable core rather than discarding it entirely.

### 3.7 Trigger-Model Comparison Table

*[Design inference — comparative summary, not a ruling]*

| Candidate | Invariant check | Resolution-step cost (Priority 3) | Granularity (Priority 1) | Status |
|---|---|---|---|---|
| T1 — Free on any success | Pass | Lowest | Lowest | Live candidate |
| T2 — Quality threshold | Pass | Low–Medium | Medium–High | Live candidate |
| T3 — Hybrid (current draft) | Pass | Medium | Medium–High | Live candidate; current Proposal default |
| T4 — Opposed-only scope restriction | Pass (orthogonal) | N/A (modifier, not alternative) | N/A | Compound with T1/T2/T3 |
| T5 — Persistent Effect Points | **Fail (Invariant 17)** | — | — | Excluded |
| T6 — Free-standing bonus roll | **Fail (Invariant 18)** | — | — | Excluded as stated |

---

## 4. Candidate Purchasing / Gating Models (Q2)

These candidates assume some Q1 trigger model (T1, T2, or T3) has already granted Effect access; they answer *which* Effect(s) from the ten-item candidate menu (Proposals §3.1) become available.

### 4.1 Candidate P1 — Flat Menu, No Gating

*[Design inference]* Any granted Effect may be freely selected from the full ten-item menu, with no per-Effect restriction.

- **Invariant check:** Passes.
- **Consequence:** Simplest possible purchasing layer; provides no mechanism to differentiate Effects by narrative/mechanical weight (Disarm and Seize Tempo would be equally accessible), which may understate Priority 1.

### 4.2 Candidate P2 — Tag-Gated Menu

*[Design inference]* Certain Effects require a matching Tag on the triggering weapon, power, or creature (e.g., Disarm requires a weapon/technique Tag permitting grip-breaking; Damage Equipment requires a Tag permitting that interaction). Untagged sources cannot select the gated Effect.

- **Invariant check:** Passes — Tags are already an established Reserved/Architectural category (Proposals §11) intended as consumer metadata; this is a straightforward consumer relationship, not a new primitive.
- **Consequence:** Requires the Tags subsystem (Proposals §11) to have enough definition to support per-Effect gating before this can be implemented; currently Tags themselves remain Reserved/undefined in detail.

### 4.3 Candidate P3 — Quality-Banded Menu

*[Design inference]* The menu is stratified into bands (e.g., "any success," "Margin ≥ some value," "near-Cap/qualifying success only"), with higher-impact Effects requiring higher bands.

- **Invariant check:** Passes, subject to the same §13.2 read-only constraint as Candidate T2.
- **Consequence:** This is Q2's analogue of T2; using both T2 (trigger) and P3 (menu) together would double-gate on Quality, which may be desirable (more granular) or redundant (more resolution steps) — flagged as a combination question, not resolved here.

### 4.4 Candidate P4 — Hybrid Menu (Tag + Quality, per-Effect)

*[Design inference, restates Proposals §3.2's fuller draft]* Some Effects are Tag-gated (P2), some are Quality-banded (P3), some are available at baseline (P1), assigned per-Effect rather than uniformly.

- **Invariant check:** Passes, as a composition of P1–P3, each individually compliant.
- **Consequence:** Highest design flexibility, but requires a per-Effect gating decision for all ten menu items before it is usable — this Round 1 does not make those ten decisions (out of scope per §0; numerical/threshold-adjacent).

### 4.5 Purchasing-Model Comparison Table

*[Design inference]*

| Candidate | Requires Tags subsystem definition? | Requires Quality-band numbers? | Compatible trigger models |
|---|---|---|---|
| P1 — Flat, no gating | No | No | T1, T2, T3 |
| P2 — Tag-gated | Yes | No | T1, T2, T3 |
| P3 — Quality-banded | No | Yes | T2, T3 (redundant with T1 alone) |
| P4 — Hybrid (per-Effect) | Yes | Yes | T3 (matches current draft shape) |

---

## 5. The State-3 Cross-Reference — Q3, Surfaced Not Resolved

*[Design inference — cross-document synthesis; the underlying S-2 State-3 classifications are themselves non-canonical candidates, per Proposals §2.1A]*

This section is the one place, per the handoff (§6, §8), where S-3 Round 1 must directly engage with S-2's findings rather than deferring them again.

| Candidate S-3 Effect | Overlapping S-2 State-3 concept | Location-dependent candidate mechanism | Location-independent candidate mechanism (already documented elsewhere) | Fork status |
|---|---|---|---|---|
| Disarm / Break Hold | Disarm / Break Hold (State 3) | Effect requires a Location Index landing on a "grip/weapon-bearing" zone | Margin/Quality-band trigger, or Tag-gated trigger (Proposals §3.2, and explicitly cited as the alternative in the S-2 Conceptual Anchor table, Proposals §2.1A) | **Open — S-3's to decide** |
| Damage Equipment | Equipment damage (State 3) | Effect requires Location Index landing on the equipped item's carried location | Margin/Quality-band trigger, or Tag-gated trigger (same basis as Disarm) | **Open — S-3's to decide** |
| Impose Condition (where the Condition represents function impairment — blindness, movement) | Function impairment (State 3) | Effect requires Location Index landing on the relevant anatomical zone | Quality-band or Tag trigger; Conditions (§10) currently have **no** stated activation mechanism at all, location-based or otherwise | **Open — S-3's to decide, and currently the least-constrained of the three** |
| *(no direct menu entry — boundary case)* | Armor bypass (State 3) | A Bypass mechanism gated on Location Index (striking an unarmored zone) | Tag/Trait-based interaction — already the stated current design direction for S-5 (Proposals §5) | **Open, but lives at the S-3/S-5 boundary, not squarely inside S-3's own menu** — flagged for cross-reference to S-5 Round 1 if/when that occurs, not resolved here |
| Choose Location | *(Not itself a State-3 concept — this Effect IS the location-selection primitive)* | N/A — this Effect's entire function is to select/confirm the location result | N/A | **Distinct question, see §5.1 below — not the same fork as the rows above** |

**Explicit non-resolution:** Per Proposals §2.1A, none of the State-3 rows above may be quietly defaulted to either mechanism. Doing so — in either direction — would violate Roadmap §24 Rule 6 (never silently resolve an open designer fork). This table exists to make the fork visible per-Effect, not to recommend a uniform answer across all three rows; the three rows are not required to resolve the same way as each other.

### 5.1 A Distinct, Adjacent Question: What Does "Choose Location" as a Menu Item Actually Mean?

*[Design inference — flagged as a genuinely separate question from the Q3 fork above]*

The candidate Effect menu (Proposals §3.1, item 10) already includes **Choose Location** as a candidate Effect in its own right. This raises a question the State-3 cross-reference table does not answer:

- If "Choose Location" is itself an S-3 Effect that a successful contest can purchase, does *purchasing* it constitute the "current rules provide a mechanism to act on the result" condition that S-2's State 1 definition requires (Proposals §2.1A: *"Established & Resolvable... current rules provide a mechanism to act on the result"*)?
- If so, does adopting "Choose Location" as a live, purchasable S-3 Effect change **Structural Weak Points'** classification from State 2 back toward State 1 — since State 2's blocking factor was explicitly "no current rule can act on the result yet" (Proposals §2.1A), and "Choose Location" would be exactly such a rule?

**This document does not answer either question.** It flags them because failing to notice the connection would risk exactly the kind of silent cross-subsystem resolution Roadmap §24 Rule 6 prohibits — S-3 defining "Choose Location" without reference to S-2's State-2 ruling could inadvertently reopen that ruling by implication, without anyone having explicitly decided to. This is recorded as Decision Point 3 in §8.

---

## 6. Scope-Guard Compliance Check

*[Mechanical fact — verification against §0]*

| Guard | Compliance |
|---|---|
| S-1 not reopened | Confirmed — S-1 treated as fixed input (§1.2); no candidate above proposes altering the outcome matrix, Quality formulas, or repeat rules. |
| S-2 Tier-1 provider not reopened | Confirmed — Zero-Step untouched; no candidate above proposes an alternate Location Index derivation. |
| S-2 attack-side invocation policy not reopened | Confirmed — treated as a fixed, non-canonical candidate input (§1.3); §5's cross-reference table surfaces the fork S-2 explicitly deferred to S-3, it does not alter S-2's own four-state model or Named-Outcome Test. |
| S-2 non-attack deferral not reopened | Confirmed — not referenced or touched by any candidate above; non-attack resolutions remain outside S-3's Round 1 scope entirely. |
| S-4 wound severity/activation not decided | Confirmed — §7's interface note (below) is architectural only, per Roadmap §10's explicit permission to prototype the S-3/S-4 interface without deciding S-4 content. |
| S-5/S-6 mechanics not decided | Confirmed — Armor Bypass and Damage Equipment are flagged as boundary cases (§5) and explicitly not resolved; Guard Break's S-6 interaction is not addressed in this round at all. |
| No numerical thresholds locked | Confirmed — no Quality band value, Tag list, or XP cost is specified anywhere above; only structural shapes are compared. |

---

## 7. S-3/S-4 Interface Note (Architectural Only)

*[Architectural constraint — explicitly non-binding on S-4 content, per Roadmap §10]*

Whichever trigger/purchasing combination is eventually chosen, the Effect layer's output to a prospective S-4 Wound Engine should be a **discrete, named Effect result** (e.g., "Disarm succeeded," "Injury Effect selected"), not a raw Location Index or raw Quality value — S-4 would then interpret that named result under its own (still fully open) severity rules. This mirrors the two-track interface diagram already on record (Roadmap §10):

```text
Track A                         Track B
PE / MP                         Location
   ↓                               ↓
Overflow                        Wound
   ↓                               ↓
Global HP                       Condition / Disability / Death Check
```

This note does not decide wound severity, activation thresholds, disability rules, or death checks — those remain fully open per Proposals §4 and Roadmap §10's explicit warning against silently establishing them via interface prototyping.

---

## 8. Designer Input Required

*[Presented as trade-off tables per the handoff's requirement — Recommendation only where explicitly labeled, never disguised as a default]*

### Decision Point 1 — Trigger Model (T1 / T2 / T3)

| Option | Favors | Costs |
|---|---|---|
| T1 — Free on any success | Priority 3 (fewer resolution steps); every success feels consequential | Priority 1 (less granularity); no differentiation between marginal and decisive successes |
| T2 — Quality threshold only | Priority 1 (granularity tied directly to performance) | Priority 3 (adds a check every success); may make Effects rare at low Skill per Canonical §13.3's own caveat about Blackjack/Hybrid needing high Skill to differentiate |
| T3 — Hybrid (current draft) | Balances both priorities; already partially drafted (Proposals §3.2) | Highest resolution-step count of the three; requires both a trigger check and a menu-gating layer to be separately specified |

### Decision Point 2 — Per-Effect Delivery Mechanism (§5 table)

Not a single decision — **three independent decisions**, one per overlapping row (Disarm, Equipment Damage, Impose Condition/impairment). Each may be answered "location," "Margin/Quality," "Tag," or some combination, independently of the others. Recorded as open in §5; this document takes no position.

### Decision Point 3 — "Choose Location" as an S-3 Effect vs. an S-2 State-1 Trigger (§5.1)

| Option | Consequence |
|---|---|
| Treat "Choose Location" as an ordinary S-3 menu Effect, no cross-reference to S-2's Structural Weak Points State-2 ruling | Keeps S-3 and S-2 cleanly separated, but risks the two subsystems developing incompatible assumptions about what "a mechanism to act on the result" means |
| Treat adopting "Choose Location" as an explicit, flagged trigger for reopening S-2's Structural Weak Points State-2 classification | Keeps the subsystems consistent, but means S-3 Round 1 cannot fully resolve "Choose Location" without formally touching an S-2 ruling — which would need to be done explicitly, as its own governance step, not as a byproduct of this document |

This document takes no position between the two rows above; it only asserts that *one of them* must eventually be chosen deliberately.

### Decision Point 4 — Ephemeral In-Test Effect Count vs. Any Persistent Resource

*[Confirms §3.5's non-excluded variant remains available]* If a numeric "how many Effects this exchange" value is wanted, it must be computed fresh from that test's own Quality/Roll and discarded at the end of the Core Test Transaction — never stored, accumulated, or carried to a later test. This is a hard constraint (Invariant 17), not a preference, and is listed here only so the designer decision (if any numeric scaling is wanted at all) is made with the constraint visible up front.

### Decision Point 5 — Effect Eligibility Scope (Opposed-Only vs. All Successes)

| Option | Consequence |
|---|---|
| Opposed-contest-exclusive (Candidate T4) | Matches Proposals §3's literal framing ("resolve opposed contests into meaningful state change"); keeps unopposed Core Tests (e.g., a solo Extended Test interval) mechanically simpler |
| All successful Core Tests, opposed or not | Broader, more uniform application of Effects across the system; raises the question of what an "Effect" even means for a non-contest success (e.g., a solo lockpicking success) — not explored in this round |

---

## 9. Summary Table — What Round 1 Established vs. What Remains Open

*[Mechanical fact — index of this document's own content]*

| Item | Status after this round |
|---|---|
| T5 (persistent Effect Points) | **Excluded** — violates Invariant 17 |
| T6 as stated (free-standing bonus roll) | **Excluded as stated** — violates Invariant 18; salvageable only as a full independent Core Test |
| T1 / T2 / T3 trigger candidates | Live, unresolved — Decision Point 1 |
| T4 (opposed-only scope) | Live, orthogonal to T1–T3 — Decision Point 5 |
| P1 / P2 / P3 / P4 menu candidates | Live, unresolved, none excluded |
| Disarm/Equipment/Impairment delivery mechanism (location vs. Margin/Tag) | **Explicitly surfaced, not resolved** — Decision Point 2 |
| Armor Bypass as an S-3/S-5 boundary case | Flagged for a future S-5-adjacent round, not resolved here |
| "Choose Location" vs. S-2's Structural Weak Points State-2 ruling | **Explicitly surfaced as a cross-subsystem consistency question, not resolved** — Decision Point 3 |
| S-3/S-4 interface shape | Architectural note only (§7); S-4 content untouched |
| Any numerical threshold | Out of scope for this round, as instructed |

**No candidate in this document is canonical, accepted, or ruled.** All items above require explicit designer input (§8) before a Round 2 analysis, a designer ruling, or promotion under Proposals §21 can proceed.
