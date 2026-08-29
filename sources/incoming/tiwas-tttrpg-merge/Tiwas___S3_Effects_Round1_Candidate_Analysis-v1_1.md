# Tiwas — S-3 Outcome Effects: Round 1 Candidate Analysis

**Document Version:** v1.1 (Correction pass — supersedes v1.0 as the working Round 1 baseline)
**Document Status:** Non-canonical design investigation — Round 1 of N
**Rule Authority:** None. This document creates no game mechanics and modifies no other document.
**Methodology:** Replicates the S-2 Non-Attack Location Index Source investigation's Round 1 discipline (see `Tiwas___S3_Handoff_Context-for_new_chat.md` §4).
**Governing hierarchy:** Canonical Rules & Changelog v1.3 (authoritative) → Proposals/WIP v1.4.3 (this work's home once accepted) → Implementation Roadmap v1.4.3 (sequencing only).
**Promotion status:** Nothing in this document is canonical or accepted. Promotion requires the full eight-step process (Proposals §21).

**Correction pass (this revision, supersedes v1.0):** Ten corrections applied after external review. **No candidate was excluded or accepted that wasn't already excluded or live in v1.0; no designer ruling is made here.** These are structural, terminological, and sequencing corrections. Each is marked inline with a `[Corrected this revision]` tag at point of change.

1. §3.4 — **Scope vs. trigger.** The former "Candidate T4" (opposed-contest-exclusive) was a fourth item on the same list as T1–T3, implying it was an alternative *trigger mechanism*. It is not — it is an orthogonal *eligibility scope* variable. Renamed to **SCOPE-A** and moved out of the trigger-candidate list into its own axis, with a scope × trigger matrix added.
2. §4 — **"Purchasing" terminology.** Q2 renamed from "Menu / Purchasing" to **"Effect Selection / Gating."** "Purchasing" implies a resource being spent, which risks quietly smuggling in exactly the kind of economy Invariant 17 excludes. The term "purchasing" is retained only where directly quoting Proposals §3.2's own historical wording.
3. §3.2 (Candidate T2) — **Quality-as-input wording softened.** The original phrasing ("ties Effect access to precision/force/commitment") risked implying Quality's identity labels (Canonical §13.2) already establish a Quality-to-Effect-potency relationship. Reworded to state only that Quality is a read-only input; whether higher Quality should mean a stronger Effect is itself an open S-3 design question, not an assumption.
4. §3.5 — **Ephemeral Effect-capacity caveat strengthened.** The non-excluded single-test-scoped count variant is not automatically prohibited by Invariant 17, but a governance caveat is added: a "compute and immediately spend" procedure can still constitute a de facto temporary points-allocation mechanic distinct from a simple Quality-band read, and needs to be evaluated on its own terms before adoption.
5. §5.1 — **"Choose Location" disambiguated into three interpretations** (A: select/declare a location before resolution; B: choose which Location Index result is used; C: convert an existing Location Index into a mechanically actionable result). Interpretation B is flagged as being in direct tension with Canonical §14.2's locked determinism provision and Proposals §2.7's confirmation that attacker/defender choice over Zero-Step's result is not currently authorized — B is treated as provisionally excluded pending an explicit S-2 reopening, not a live S-3 candidate alongside A and C.
6. §8 — **Decision Point 4 removed** (ephemeral count vs. persistent resource). The persistent-resource question is already closed by §3.5's exclusion of T5; the live question is whether Effects should scale numerically with Quality at all, which is premature to decide before Effect identities themselves are investigated (see correction 8).
7. New §2.1 — **Standardized pipeline terminology** introduced: Effect Eligibility → Effect Capacity → Effect Selection → Named Effect Result. Used consistently in place of the previously inconsistent "granted / selected / purchased" language.
8. §8 — **Sequencing correction.** The document no longer frames Decision Point 1 (T1/T2/T3) as ready for a designer ruling. Per Roadmap §10's instruction to implement the structural Effect interface first and gather simulation evidence (Effect frequency, exchange length, wound frequency, state-change density) before locking numbers, this revision adds an explicit recommended ordering: investigate the ten candidate Effects' relative mechanical/narrative weight *before* comparing trigger models, since the right trigger model is itself sensitive to how powerful an "Effect" turns out to be.
9. Confirmed (no change needed): the S-2 non-attack Location Index deferral (Proposals §2.5A) is not reopened anywhere in this document.
10. Confirmed (no change needed): §7 (S-3/S-4 interface) remains architectural only, per Roadmap §10.

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
- *[New this revision]* ask the designer to lock a trigger model (T1/T2/T3) yet — see correction 8 and §8 below.

This round **does**:

- separate the trigger question from the Effect Selection/Gating question, per the handoff's core methodological requirement;
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
| Quality never alters the historical roll, Cost, Failure XP, Double eligibility, or Recovery | Canonical §13.2 | Any Quality-gated Effect-selection candidate may only *read* Quality, never feed back into it. |
| No competing primary resource/progression economy (Invariant 17) | Canonical §16 | Any candidate introducing a spendable/persistent "Effect Points" pool is prohibited unless proven non-persistent and non-transferable (see §3.5 below). |
| Universal Play modules call the Core Test Transaction, never replace it (Invariant 18) | Canonical §16 | A candidate that resolves Effects via an independent resolution mechanism (a second, non-Core roll standing outside the Test Transaction) is prohibited unless that roll is itself a full Core Test Transaction. |
| Zero-Step is deterministic; the attacker does not choose between the natural and transformed result | Canonical §14.2 | *[New this revision]* Binding on any candidate Effect that touches an existing Location Index — see §5.1, Interpretation B. |
| Effects must never modify the historical die roll | Proposals §3.3 | Explicit S-3-specific non-negotiable, restated here as binding on every candidate below. |

### 1.2 S-1 status (locked, informs but is not reopened)

*[Mechanical fact]* S-1 provides: independent Core Tests per participant; a Success/Failure outcome matrix; three Quality measures (Margin, Blackjack, Hybrid Committed) selected per contest type; exact-tie and Failure/Failure repeat rules (Canonical §13). Quality is available as a **read-only** input to any S-3 trigger/selection candidate that wants to use it, subject to §13.2 above.

### 1.3 S-2 status (locked/candidate, informs but is not reopened)

*[Mechanical fact + design inference, distinguished]*

- **Locked:** Zero-Step Tier-1 Location Index provider (Canonical §14.1–§14.2) — deterministic, read-only post-process of the natural roll, with **no player choice** over the result (§14.2).
- **Non-canonical candidate, accepted for further development:** attack-side invocation/warrant policy (Proposals §2.1A) — four-state model; Location Index generation requires an explicitly named distinct outcome, anchored location-dependence, and a resolving mechanism.
- **Ruled (non-canonical governing position):** non-attack physical resolutions generate no Location Index (Proposals §2.5A).
- **State-3 finding (candidate, non-canonical):** Disarm/Break Hold, Equipment Damage, Function Impairment, Armor Bypass, and Incapacitation/Kill are currently classified as *"Outcome Plausible, Location-Dependence Unresolved"* — i.e., whether location is even the delivery mechanism for these outcomes is an open fork, explicitly handed to S-3 (and S-5/S-7/S-10) to resolve (Proposals §2.1A).

---

## 2. The Two-Part Question, Restated and Kept Separate

Per the handoff methodology, these are treated as **independent questions** throughout this document. No candidate below is permitted to answer one by silently assuming an answer to the other.

| Question | What it asks | What it explicitly does not ask |
|---|---|---|
| **Q1 — Trigger** | Does a given resolved contest/test grant *any* Effect at all, and if so, under what condition? | Which Effect, how many, or what it requires beyond the trigger condition itself. |
| **Q2 — Effect Selection / Gating** *[renamed this revision, correction 2]* | Given that an Effect is available, which Effect(s) from the candidate menu (Proposals §3.1) may be selected, and what — if anything — gates access to specific ones? | Whether an Effect is granted at all in the first place. |

A third, narrower question is inherited directly from S-2 and must not be quietly folded into either Q1 or Q2:

| Question | What it asks |
|---|---|
| **Q3 — Delivery mechanism (per-Effect)** | For each candidate Effect that overlaps S-2's State-3 table, does *triggering that specific Effect* require a Location Index (location as delivery mechanism), or does it trigger off Margin/Quality/Tags (a location-independent mechanism)? |

Q3 is not "does S-3 need location" in general — it is a **per-Effect** fork, since some candidate Effects (e.g., Choose Location itself) are self-evidently location-related while others (e.g., Seize Tempo) plausibly never touch location at all.

### 2.1 Standardized Pipeline Terminology *[New this revision, correction 7]*

*[Design inference — terminology standardization only, no mechanics implied]*

Prior drafting in v1.0 used "granted," "selected," and "purchased" inconsistently and sometimes interchangeably. This revision fixes four distinct pipeline stages, used consistently for the remainder of this document:

```text
Core Test / S-1 Contest
        ↓
     Outcome
        ↓
Effect Eligibility   — Q1: does this result qualify to produce an Effect at all?
        ↓
Effect Capacity      — how many Effect(s), if any, can this result produce? (may be fixed at 1, or variable)
        ↓
Effect Selection      — Q2: which specific Effect(s) from the menu are chosen, and what gates that choice?
        ↓
Named Effect Result
        ↓
S-4 / other downstream subsystem (see §7)
```

**Effect Capacity is named here as a distinct stage for the first time in this document.** In v1.0, "how many Effects" was folded into the T1/T2/T3 trigger discussion and the P1–P4 selection discussion inconsistently. Separating it out clarifies, for example, that Candidate T3's "additional Effects... where Quality bands are met" is really a **Capacity** rule (how many), layered on top of whatever **Eligibility** rule (T1/T2/T3) is chosen — not a third independent thing. This does not change any candidate's substance, only where it sits in the pipeline.

---

## 3. Candidate Trigger Models (Q1 — Effect Eligibility)

Each candidate is evaluated against the Canonical invariants in §1.1. A candidate that fails this check is **excluded outright**, mirroring how S-2 Round 1 excluded Candidate B (ad-hoc GM roll) for violating Invariant 18.

### 3.1 Candidate T1 — Universal Free Effect on Any Success

*[Design inference, carried from existing non-canonical Proposal wording, Proposals §3.2 bullet 1]*

Every successful Core Test or S-1 contest automatically grants Effect Eligibility, with Capacity fixed at one, and no additional gate.

- **Invariant check:** Passes. Uses the existing Success outcome directly; introduces no new roll, no new resource, no alteration of Cost/Overflow/XP/Recovery.
- **Consequence:** Maximizes Priority 3 (minimum resolution steps) at the possible cost of Priority 1 (granular simulation) — every success becomes tactically identical in *eligibility*, differentiated only by which Effect is selected.

### 3.2 Candidate T2 — Quality-Threshold Gate

*[Design inference]*

Effect Eligibility is granted only if the contest's Quality (Margin/Blackjack/Hybrid, per Canonical §13.2) meets or exceeds a threshold. Ordinary successes below threshold produce no Effect, only the base outcome (e.g., damage).

- **Invariant check:** Passes, provided the threshold check only *reads* Quality and never modifies the historical roll, Cost, or XP (Canonical §13.2 explicitly permits Quality to be read; it does not permit Quality to become a second write-channel into the Core Test).
- **Consequence:** *[Reworded this revision, correction 3]* Ties Effect Eligibility to the contest's selected Quality measure (Margin, Blackjack, or Hybrid, per Canonical §13.2–§13.3). Canonical §13.2 defines these measures only as "Efficiency/precision," "Commitment/force," and "Commitment with continued high-Skill scaling" respectively — those are the measures' own stated identities, not an established claim that any of them make a *good* or *intended* basis for Effect access. Whether higher Quality should correspond to easier or stronger Effect access — and whether that differs by Quality mode — is itself an open S-3 design question that this candidate raises but does not answer. Canonical §13.3 separately notes that Blackjack/Hybrid's distinctiveness "becomes meaningful primarily once relevant Skills are sufficiently high," which is a relevant constraint on this candidate's behavior at low Skill, not a design goal.

### 3.3 Candidate T3 — Hybrid (Free Basic Eligibility + Quality/Tag-Scaled Capacity)

*[Design inference, restates the current Proposal §3.2 draft in full]*

- One successful contest grants Effect Eligibility unconditionally, with Capacity 1 (as T1).
- Additional Capacity (further Effects beyond the first) may be granted where Net Advantage/Quality bands are met.
- Some specific Effects are Tag-gated at the Selection stage regardless of Quality.
- Some exceptional Effects require a qualifying success (e.g., a Double, or Quality above a high band) to be Selection-eligible.

- **Invariant check:** Passes, for the same reasons as T1 and T2 combined; the additional-Capacity layer is strictly additive and never subtracts from or reorders the base Core Test Transaction.
- **Consequence:** This is the current non-canonical Proposal draft (§3.2) — Round 1 does not need to invent it, only formalize and stress-test it against T1/T2 as genuine alternatives, per the handoff's requirement not to let a pre-existing draft masquerade as an unreviewed default. Per §2.1, this candidate is now explicitly recognizable as "T1's Eligibility rule + a Quality-scaled Capacity rule + a Tag/qualifying-success-gated Selection rule," rather than one undifferentiated hybrid.

### 3.4 SCOPE-A — Opposed-Contest-Exclusive Eligibility *[Renamed and re-axised this revision, correction 1]*

*[Architectural constraint, drawn directly from Proposals §3's framing]*

Effect Eligibility applies only to results from S-1 opposed contests, never from unopposed Core Tests. Rationale: Proposals §3 states the design intent as *"Tiwas is intended to resolve opposed contests into meaningful state change"* — a narrower claim than "every successful test."

**This is not a fourth trigger candidate alongside T1–T3.** It is an orthogonal **eligibility-scope** variable: it answers *which category of test may enter the Eligibility pipeline at all*, while T1/T2/T3 answer *what condition within that category grants Eligibility*. The two axes combine independently:

| Scope | + T1 (any success) | + T2 (Quality threshold) | + T3 (hybrid) |
|---|---|---|---|
| **SCOPE-A — Opposed contests only** | Every opposed success is Eligible | Only opposed successes clearing the Quality threshold are Eligible | Every opposed success gets base Eligibility; Quality/Tags scale Capacity/Selection |
| **SCOPE-B — All successful Core Tests** | Every success (opposed or solo) is Eligible | Any success (opposed or solo) clearing the Quality threshold is Eligible | Every success gets base Eligibility; Quality/Tags scale Capacity/Selection |

- **Invariant check:** Passes on its own terms; it is a *restriction or extension of scope*, not a new mechanism.
- **Consequence:** Six combinations exist, not four alternatives — this table should replace the earlier "T1 vs T2 vs T3 vs T4" framing wherever it appears in downstream discussion. See §8, Decision Point 5 (renumbered).

### 3.5 Candidate T5 — Dedicated "Effect Points" Resource *(Excluded)*

*[Architectural constraint — hard exclusion]*

A candidate under consideration during drafting proposed a persistent, spendable "Effect Points" pool: successes deposit points into the pool; players later spend accumulated points to purchase Effects across multiple exchanges.

- **Invariant check: FAILS.** This is a second progression/resource economy in the Invariant 17 sense (Canonical §16; Roadmap §2) — it persists across tests, accumulates, and is spendable independently of the triggering test's own Cost/Overflow/XP, which is precisely the shape Invariant 17 excludes. It is structurally identical to the kind of "second advancement economy" the Extended-Test Progress rule (Canonical/Proposals §9.4) is explicitly barred from becoming, applied here to Effects instead of Extended Tests.
- **Disposition:** Excluded outright, mirroring S-2 Round 1's exclusion of ad-hoc GM rolls (Candidate B) for violating Invariant 18. Retained here only as a record of a rejected candidate, per Roadmap §24 Rule 15 (superseded/rejected material is retained, not deleted).
- **Note — narrower, non-excluded variant, with strengthened caveat** *[Caveat strengthened this revision, correction 4]**:* An **ephemeral, single-test-scoped** Capacity value derived directly from that test's own Quality (e.g., "this success's Margin determines how many Effects *this exchange* may draw from the menu, discarded at the end of the transaction") does **not** automatically fail the invariant check, since a bare read-and-discard formula output is not a stored/transferable currency — structurally analogous to how Quality itself is read-only and non-persistent (Canonical §13.2).

  However, this variant is **not** simply cleared for adoption. There is a meaningful design distinction between:
  - **Clearly safe:** *"Margin = 17 → you qualify for Effect band X"* — a pure Quality read, no intermediate value created.
  - **Requires separate evaluation:** *"Margin = 17 → you receive 3 Effect Points for this exchange → you spend those points among Effects this exchange"* — even though the points vanish at the end of the transaction and never accumulate, this shape introduces an intermediate spend-allocation step (a de facto temporary points-allocation mechanic) that is not automatically the same thing as a threshold read, and may add resolution-step complexity T1's simplicity was meant to avoid.

  This document does not decide between these two shapes. If ephemeral Capacity scaling is pursued at all, it should be evaluated as its own architectural question — not waved through merely because it clears the Invariant 17 bar — and should not be decided before the Effect-identity investigation recommended in §8, Decision Point 1 (renumbered).

### 3.6 Candidate T6 — Independent "Effect Roll" *(Excluded as stated; conditionally salvageable)*

*[Architectural constraint — hard exclusion of the stated form]*

A candidate proposed a second, dedicated d100 roll — separate from the Core Test that produced the Success — used solely to determine whether/which Effect is granted.

- **Invariant check: FAILS as stated.** A free-standing bonus roll outside the Core Test Transaction is exactly the "competing... resolution" Invariant 18 excludes (Canonical §16) — it duplicates rather than calls the Transaction.
- **Conditionally salvageable form:** If the "second roll" were reformulated as a genuine, independent Core Test in its own right (own Cost, own Overflow exposure, own Failure XP, own Recovery — i.e., not a free roll, but an actual additional Test Transaction the character pays for), it would no longer violate Invariant 18, since it would *be* the Core Test Transaction rather than compete with it. This reformulation is structurally close to T2/T3's Quality-gating and is not separately pursued as its own candidate; noted for completeness only, mirroring how S-2 Round 1 recorded a rejected candidate's salvageable core rather than discarding it entirely.

### 3.7 Trigger-Model Comparison Table

*[Design inference — comparative summary, not a ruling]*

| Candidate | Invariant check | Resolution-step cost (Priority 3) | Granularity (Priority 1) | Status |
|---|---|---|---|---|
| T1 — Free Eligibility on any success | Pass | Lowest | Lowest | Live candidate |
| T2 — Quality-threshold Eligibility | Pass | Low–Medium | Medium–High | Live candidate |
| T3 — Hybrid Eligibility/Capacity/Selection (current draft) | Pass | Medium | Medium–High | Live candidate; current Proposal default |
| SCOPE-A/B — Eligibility-scope axis | Pass (orthogonal) | N/A (modifier, combines with T1/T2/T3 per §3.4 table) | N/A | Compound axis, not a fourth alternative |
| T5 — Persistent Effect Points | **Fail (Invariant 17)** | — | — | Excluded |
| T5-variant — Ephemeral in-test Capacity | Pass, with caveat | Low (if pure read) to Medium (if spend-allocation) | Medium | Live candidate, requires separate evaluation |
| T6 — Free-standing bonus roll | **Fail (Invariant 18)** | — | — | Excluded as stated |

---

## 4. Candidate Effect Selection / Gating Models (Q2) *[Section renamed this revision, correction 2]*

These candidates assume some Q1 Eligibility model (T1, T2, or T3, combined with a SCOPE-A/B choice) has already granted Effect Eligibility and some Capacity; they answer *which* Effect(s) from the ten-item candidate menu (Proposals §3.1) become Selection-eligible. Where source material (Proposals §3.2) is quoted directly, its original term "purchasing" is preserved in quotation; this document's own analysis uses "Selection / Gating."

### 4.1 Candidate P1 — Flat Menu, No Gating

*[Design inference]* Any Eligible Capacity may be freely applied to select from the full ten-item menu, with no per-Effect restriction.

- **Invariant check:** Passes.
- **Consequence:** Simplest possible Selection layer; provides no mechanism to differentiate Effects by narrative/mechanical weight (Disarm and Seize Tempo would be equally accessible), which may understate Priority 1.

### 4.2 Candidate P2 — Tag-Gated Menu

*[Design inference]* Certain Effects require a matching Tag on the triggering weapon, power, or creature (e.g., Disarm requires a weapon/technique Tag permitting grip-breaking; Damage Equipment requires a Tag permitting that interaction). Untagged sources cannot select the gated Effect.

- **Invariant check:** Passes — Tags are already an established Reserved/Architectural category (Proposals §11) intended as consumer metadata; this is a straightforward consumer relationship, not a new primitive.
- **Consequence:** Requires the Tags subsystem (Proposals §11) to have enough definition to support per-Effect gating before this can be implemented; currently Tags themselves remain Reserved/undefined in detail.

### 4.3 Candidate P3 — Quality-Banded Menu

*[Design inference]* The menu is stratified into bands (e.g., "any success," "Margin ≥ some value," "near-Cap/qualifying success only"), with higher-impact Effects requiring higher bands.

- **Invariant check:** Passes, subject to the same §13.2 read-only constraint as Candidate T2, and the same correction-3 caveat: banding Effects by Quality does not by itself establish that higher Quality *should* unlock more powerful Effects — that remains an open design question this candidate structurally enables but does not resolve.
- **Consequence:** This is Q2's analogue of T2; using both T2 (Eligibility) and P3 (Selection) together would double-gate on Quality, which may be desirable (more granular) or redundant (more resolution steps) — flagged as a combination question, not resolved here.

### 4.4 Candidate P4 — Hybrid Menu (Tag + Quality, per-Effect)

*[Design inference, restates Proposals §3.2's fuller draft]* Some Effects are Tag-gated (P2), some are Quality-banded (P3), some are available at baseline (P1), assigned per-Effect rather than uniformly.

- **Invariant check:** Passes, as a composition of P1–P3, each individually compliant.
- **Consequence:** Highest design flexibility, but requires a per-Effect gating decision for all ten menu items before it is usable — this Round 1 does not make those ten decisions (out of scope per §0; numerical/threshold-adjacent).

### 4.5 Selection-Model Comparison Table

*[Design inference]*

| Candidate | Requires Tags subsystem definition? | Requires Quality-band numbers? | Compatible Eligibility models |
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
| Choose Location | *(Not itself a State-3 concept — this Effect IS the location-selection primitive)* | N/A — see §5.1 below for the disambiguation this Effect actually requires | N/A | **Distinct question, see §5.1 — not the same fork as the rows above** |

**Explicit non-resolution:** Per Proposals §2.1A, none of the State-3 rows above may be quietly defaulted to either mechanism. Doing so — in either direction — would violate Roadmap §24 Rule 6 (never silently resolve an open designer fork). This table exists to make the fork visible per-Effect, not to recommend a uniform answer across all three rows; the three rows are not required to resolve the same way as each other.

### 5.1 "Choose Location" — Three Interpretations, Not One Question *[Expanded this revision, correction 5]*

*[Design inference — flagged as a genuinely separate question from the Q3 fork above, now disambiguated]*

v1.0 treated "Choose Location" (Proposals §3.1, item 10) as raising a single question about S-2's Structural Weak Points State-2 status. External review correctly identified that "Choose Location" is actually ambiguous between at least three distinct mechanics, which have different — in one case, disqualifying — implications:

**Interpretation A — Select/declare a target location before resolution.**
The player, as part of declaring the action (before or independent of the roll), states an intended target zone as flavor/intent. This is close to how the S-2 attack-side warrant policy's "named distinct outcome" already works (Proposals §2.1A) — it does not generate or alter a Location Index, it only frames intent. This interpretation does not touch Zero-Step at all and raises no invariant concern.

**Interpretation B — Choose which Location Index result is used.**
The player selects, overrides, or picks between possible Location Index values (e.g., rerolling, choosing digit order, or picking a result outright) rather than accepting Zero-Step's deterministic exchange of the natural roll's digits.

- **Invariant check: FAILS.** Canonical §14.2 states plainly that *"Zero-Step is deterministic. The attacker does not choose between the natural roll and the transformed result."* This is a **locked** Canonical provision, not a candidate. Proposals §2.7 separately confirms that attacker-choice and defender-choice over the Zero-Step result remain unauthorized design *observations* only, not current rules, and not even an active proposal under consideration.
- **Disposition:** Interpretation B is **provisionally excluded** as a live S-3 candidate — not because S-3 lacks the authority to design Effects, but because this specific interpretation would require *reopening a locked Canonical provision* (§14.2), which Proposals §21's eight-step promotion process and Roadmap §24 Rule 16 both require to happen explicitly and through governance, not as a side effect of an S-3 Effect-menu decision. If a future designer wants Effect-driven Location Index choice, that must be raised as an explicit Canonical §14.2 reopening request, separate from and prior to any S-3 ruling — mirroring how Proposals §2.7 already keeps attacker/defender choice clearly labeled as a non-authorized observation rather than a pending proposal.

**Interpretation C — Convert an existing Location Index into a mechanically actionable result.**
The Effect does not touch *which* Location Index value resulted (that remains Zero-Step's deterministic output) — it supplies the missing downstream mechanism that turns an already-generated Index into something the ruleset can act on (e.g., mapping the Index to a component/zone and applying a consequence there). This is squarely within S-3's remit: it is exactly the kind of "current rules provide a mechanism to act on the result" condition S-2's State 1 definition requires (Proposals §2.1A), and it touches no locked provision.

**Consequence for the Structural Weak Points question:** Only **Interpretation C** is relevant to whether adopting "Choose Location" as a live S-3 Effect could supply the missing mechanism that is currently keeping Structural Weak Points at S-2 **State 2** (Proposals §2.1A: State 2 is blocked only by "no current rule can act on the result yet"). If Round 2 develops "Choose Location" as Interpretation C, that development should be explicitly flagged as touching S-2's State-2 ruling — per Roadmap §24 Rule 6, not silently. Interpretation A does not touch it. Interpretation B does not reach this question at all, since it is excluded before the State-2 issue is even relevant.

**This document does not choose among A, B, or C.** It corrects v1.0 by establishing that they are not the same design object, that B is not on the same footing as A and C, and that only C carries the cross-reference risk to S-2's Structural Weak Points ruling that v1.0 flagged more vaguely. This is recorded as Decision Point 3 in §8.

---

## 6. Scope-Guard Compliance Check

*[Mechanical fact — verification against §0]*

| Guard | Compliance |
|---|---|
| S-1 not reopened | Confirmed — S-1 treated as fixed input (§1.2); no candidate above proposes altering the outcome matrix, Quality formulas, or repeat rules. |
| S-2 Tier-1 provider not reopened | Confirmed — Zero-Step untouched; no candidate above proposes an alternate Location Index derivation. Interpretation B (§5.1) is explicitly excluded rather than adopted precisely to preserve this guard. |
| S-2 attack-side invocation policy not reopened | Confirmed — treated as a fixed, non-canonical candidate input (§1.3); §5's cross-reference table surfaces the fork S-2 explicitly deferred to S-3, it does not alter S-2's own four-state model or Named-Outcome Test. |
| S-2 non-attack deferral not reopened | Confirmed — not referenced or touched by any candidate above; non-attack resolutions remain outside S-3's Round 1 scope entirely. |
| S-4 wound severity/activation not decided | Confirmed — §7's interface note (below) is architectural only, per Roadmap §10's explicit permission to prototype the S-3/S-4 interface without deciding S-4 content. |
| S-5/S-6 mechanics not decided | Confirmed — Armor Bypass and Damage Equipment are flagged as boundary cases (§5) and explicitly not resolved; Guard Break's S-6 interaction is not addressed in this round at all. |
| No numerical thresholds locked | Confirmed — no Quality band value, Tag list, or XP cost is specified anywhere above; only structural shapes are compared. |
| *[New]* No trigger model locked | Confirmed — §8 explicitly declines to ask for a T1/T2/T3 designer ruling this round; see correction 8. |

---

## 7. S-3/S-4 Interface Note (Architectural Only)

*[Architectural constraint — explicitly non-binding on S-4 content, per Roadmap §10]*

Whichever Eligibility/Capacity/Selection combination is eventually chosen, the Effect layer's output to a prospective S-4 Wound Engine should be a **discrete, Named Effect Result** (e.g., "Disarm succeeded," "Injury Effect selected"), not a raw Location Index or raw Quality value — S-4 would then interpret that named result under its own (still fully open) severity rules. This mirrors the two-track interface diagram already on record (Roadmap §10), and now aligns terminologically with §2.1's pipeline:

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

### Recommended Sequencing *[New this revision, correction 8]*

*[Recommendation — not a designer ruling]*

External review correctly identified that asking for a T1/T2/T3 designer ruling in this round is premature: whether "one free Effect per success" is the right Eligibility model depends heavily on how powerful an individual Effect turns out to be once the ten candidate Effects (Proposals §3.1) are actually defined — a question this round has not touched. Roadmap §10 itself directs that the structural Effect interface be implemented first and evaluated via simulation (Effect frequency, exchange length, resource expenditure, wound frequency, severe injury, state-change density) before locking thresholds.

Recommended ordering:

```text
Round 1 (this document)
Candidate Eligibility/Capacity/Selection architecture, invariant screening
        ↓
Round 2
Define and weight the ten candidate Effects themselves — relative mechanical/
narrative impact, which ones plausibly interact with S-2/S-4/S-5/S-6 boundaries
        ↓
Round 3
Compare Eligibility + Capacity + Selection models (T1/T2/T3 × SCOPE-A/B × P1–P4)
against the Round 2 Effect-weight findings
        ↓
Simulation (per Roadmap §10)
        ↓
Designer ruling
```

Decision Points 1–2 below are therefore recorded as **open candidate space to carry into Round 2**, not items requiring a ruling now.

### Decision Point 1 — Trigger/Eligibility Model (T1 / T2 / T3) — *carry forward, do not rule yet*

| Option | Favors | Costs |
|---|---|---|
| T1 — Free Eligibility on any success | Priority 3 (fewer resolution steps); every success feels consequential | Priority 1 (less granularity); no differentiation between marginal and decisive successes |
| T2 — Quality-threshold Eligibility | Priority 1 (granularity tied directly to performance) | Priority 3 (adds a check every success); may make Effects rare at low Skill per Canonical §13.3's own caveat about Blackjack/Hybrid needing high Skill to differentiate |
| T3 — Hybrid (current draft) | Balances both priorities; already partially drafted (Proposals §3.2) | Highest resolution-step count of the three; requires both an Eligibility check and a Capacity/Selection-gating layer to be separately specified |

### Decision Point 2 — Eligibility Scope (SCOPE-A / SCOPE-B) — *carry forward, do not rule yet*

| Option | Consequence |
|---|---|
| SCOPE-A — Opposed-contest-exclusive | Matches Proposals §3's literal framing ("resolve opposed contests into meaningful state change"); keeps unopposed Core Tests (e.g., a solo Extended Test interval) mechanically simpler |
| SCOPE-B — All successful Core Tests | Broader, more uniform application of Effects across the system; raises the question of what an "Effect" even means for a non-contest success (e.g., a solo lockpicking success) — not explored in this round |

### Decision Point 3 — "Choose Location": Which Interpretation(s) to Develop (§5.1)

| Option | Consequence |
|---|---|
| Develop only Interpretation A (declare intent) | Simplest, no cross-reference risk to S-2, but does not supply any new resolvability mechanism — Structural Weak Points remains State 2 |
| Develop Interpretation C (convert Index to actionable result) | Directly relevant to, and should be explicitly flagged as touching, S-2's Structural Weak Points State-2 ruling — must be raised as an explicit cross-subsystem note, not decided as a byproduct of S-3 alone |
| Interpretation B (choose the Index result) | **Not a live option absent an explicit Canonical §14.2 reopening** — recorded for completeness only (§5.1) |

This document takes no position among the live options; it only asserts that a choice — and, for Interpretation C, an explicit cross-reference step — must eventually be made deliberately.

### Decision Point 4 *(formerly "ephemeral count vs. persistent resource")* — Removed *[Correction 6]*

The persistent-resource question is already closed (T5 excluded, §3.5). The live residual question — whether Effect Capacity should scale numerically with Quality at all, and if so via a pure read or a spend-allocation shape (§3.5's two sub-variants) — is folded into the Recommended Sequencing above and should not be decided before Round 2's Effect-weighting work.

---

## 9. Summary Table — What Round 1 Established vs. What Remains Open

*[Mechanical fact — index of this document's own content]*

| Item | Status after this round |
|---|---|
| T5 (persistent Effect Points) | **Excluded** — violates Invariant 17 |
| T6 as stated (free-standing bonus roll) | **Excluded as stated** — violates Invariant 18; salvageable only as a full independent Core Test |
| "Choose Location" Interpretation B (choose the Index result) | **Provisionally excluded** — conflicts with locked Canonical §14.2; would require explicit reopening, not an S-3-level decision |
| T1 / T2 / T3 Eligibility candidates | Live, unresolved, **sequencing correction: not ready for a ruling until Round 2's Effect-weighting work is done** |
| SCOPE-A / SCOPE-B eligibility-scope axis | Live, unresolved, orthogonal to T1–T3 — Decision Point 2 |
| P1 / P2 / P3 / P4 Selection candidates | Live, unresolved, none excluded |
| Ephemeral in-test Effect Capacity (T5-variant) | Live, but requires separate evaluation between pure-read and spend-allocation shapes before adoption |
| Disarm/Equipment/Impairment delivery mechanism (location vs. Margin/Tag) | **Explicitly surfaced, not resolved** — Decision Point in §5 |
| Armor Bypass as an S-3/S-5 boundary case | Flagged for a future S-5-adjacent round, not resolved here |
| "Choose Location" Interpretations A and C vs. S-2's Structural Weak Points State-2 ruling | **Explicitly surfaced as a cross-subsystem consistency question, not resolved** — Decision Point 3 |
| S-3/S-4 interface shape | Architectural note only (§7); S-4 content untouched |
| Any numerical threshold | Out of scope for this round, as instructed |

**No candidate in this document is canonical, accepted, or ruled.** All items above require explicit designer input, in the sequencing recommended in §8, before a Round 2 Effect-weighting analysis, a designer ruling, or promotion under Proposals §21 can proceed.
