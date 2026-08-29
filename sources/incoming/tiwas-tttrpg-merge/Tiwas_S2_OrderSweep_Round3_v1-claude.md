# Tiwas — S-2 Round 3: Exhaustive Order-Sweep Results & Response to ChatGPT (v1.0)

**Status:** Response to `Tiwas_S-2_Round_2_-_Review__Assessment___Recommended_Disposition.md`, ChatGPT's
review of the round-2 report. Executes ChatGPT's concretely-specified next action (§17, §26 of that
document: an exhaustive order-permutation sweep of Fixture C, all 7! = 5,040 orderings, both methods,
seven requested metrics). **Does not run Phase 2 (Fixtures D/E/F/G)** — those require inventing new
anatomical content (creature wing weights, a 12–20 zone table) that hasn't been authored yet; flagged as
a decision point in §G rather than executed unprompted. **Does not lock S-2 or edit any canonical
document.**

**Chain position:** S-2 v1.1 → experiment report → ChatGPT round 2 → round-2 response → ChatGPT round 3
→ **this document**.

---

## A. What ChatGPT's Round-3 Review Says, Condensed

Accepts both round-2 corrections (order-dependence is shared by both methods; the pair-aware symmetry fix
backfires elsewhere) and sharpens rather than retracts the pro-Zero-Step conclusion: the finding is
reframed as **domain resolution** — Zero-Step's 100-value index gives downstream mapping 1% native
granularity vs. Units-Digit's 10%, so the *same* shared order-dependence bug has a much smaller worst case
under Zero-Step. One partial pushback on the round-2 scope split: domain size/resolution should stay an
explicit **S-2** interface characteristic (not just a downstream mapping-spec concern), because S-2's
formula choice is what determines the index domain the mapper receives. The concrete next action:
**exhaustively sweep Fixture C's 5,040 orderings**, reporting mean/worst/best MAE, worst zone error,
symmetry-violation frequency, maximum symmetry gap, and unreachable-zone frequency, for both methods,
before any broader stress test or designer ruling.

---

## B. Agreement, Including ChatGPT's Refinement to the Round-2 Scope Split

Full agreement with §3–§10, §13–§15, §19, §21 of ChatGPT's review — these restate or extend round-2
findings without introducing anything to contest.

One specific refinement is accepted: ChatGPT's §11/§24.1 pushback on the round-2 scope split (§C.3 of the
round-2 response) is correct. Round 2 argued Symmetry Preservation, Table-Order Independence, and
Unreachable-Zone Detection belong to the future location-table-mapping spec, not S-2. ChatGPT's addition —
**domain resolution stays an S-2 property, because domain size is a direct, inseparable consequence of
which formula S-2 selects** — is accepted without qualification. Choosing Zero-Step over Units-Digit *is*
choosing a domain size; there's no way to assign "resolution" to the downstream spec without also
splitting a decision (which formula) that S-2 obviously still owns. This isn't scope creep back into S-2;
it's a more precise name for something S-2's existing text already decides.

---

## C. Executed: Exhaustive Order Sweep

### C.1 Method

For a fixed zone list and weight set, every possible ordering was generated (`itertools.permutations`,
exhaustive, not sampled — consistent with S-2 v1.1 §F's own precedent for small finite spaces) and passed
through the same largest-remainder apportionment used throughout this project (round-1 report §C.3), with
the tie-break rule applied to *that permutation's* order each time. **Fixture C** (7 zones, 5,040 orderings)
was run as ChatGPT specified. **Fixture A** (6 zones, 720 orderings) was added as a cross-check — reasoning
in §C.3 below; this is a deviation from a literal reading of ChatGPT §17, flagged as such.

For each permutation: MAE, max single-zone absolute error, symmetry gap for each declared pair (R Arm/L
Arm, R Leg/L Leg), and unreachable-zone count. Aggregated across all permutations into the seven metrics
ChatGPT's §17 requested.

### C.2 Results — Fixture C (as specified)

| Metric | Zero-Step (N=100) | Units-Digit (N=10) |
|---|---|---|
| Mean MAE | 0.0000pp | 3.1429pp |
| Worst MAE | 0.0000pp | 3.1429pp |
| Best MAE | 0.0000pp | 3.1429pp |
| Worst single-zone error (any perm) | 0.0000pp | 6.0000pp |
| Symmetry violation frequency | **0 / 5,040 = 0.00%** | **5,040 / 5,040 = 100.00%** |
| Max symmetry gap | 0.0000pp | 10.0000pp |
| ≥1 unreachable-zone frequency | 0 / 5,040 = 0.00% | **5,040 / 5,040 = 100.00%** |

Per-zone detail, Units-Digit: Head, Neck, Torso, R Arm, L Arm are **invariant** across all 5,040
orderings (error fixed at +5.00, −3.00, 0.00, −2.00, −2.00pp respectively, never anything else). Only R Leg
and L Leg vary, each ranging over {−4.00pp, +6.00pp} depending on which one falls earlier in that
permutation's order. **Neck is unreachable in literally every one of the 5,040 orderings** — this is not
an unlucky table order, it's a mathematical certainty for this weight set (explained in §C.4).

### C.3 Results — Fixture A (cross-check)

**Why this was necessary:** Fixture C's Zero-Step row above shows *zero* variation across all 5,040
orderings — every metric flat at its ideal value. Taken alone, that could be misread as "Zero-Step is
order-independent." It isn't (round-2 report §C.1 already showed one concrete counterexample). Fixture C's
weights (5%, 3%, 40%, 12%, 12%, 14%, 14%) are all exact multiples of Zero-Step's native 1% resolution, so
there is never a fractional remainder for the apportionment step to fight over — order has literally
nothing to act on for this specific fixture. This is the same structural fact behind Zero-Step's tautological
0.00pp error on Fixture C in the very first experiment (round-1 report §B.1): Fixture C is pre-shaped to
Zero-Step's domain, in both accuracy *and* order-sensitivity. Fixture A's weights (1/6 ≈ 16.667%) are not
exact multiples of either domain, so it's a fairer test of order-sensitivity in general.

| Metric | Zero-Step (N=100) | Units-Digit (N=10) |
|---|---|---|
| Mean MAE | 0.4444pp | 4.4444pp |
| Worst MAE | 0.4444pp | 4.4444pp |
| Best MAE | 0.4444pp | 4.4444pp |
| Worst single-zone error (any perm) | 0.6667pp | 6.6667pp |
| Symmetry violation frequency | **576 / 720 = 80.00%** | **576 / 720 = 80.00%** |
| Max symmetry gap | 1.0000pp | 10.0000pp |
| ≥1 unreachable-zone frequency | 0 / 720 = 0.00% | 0 / 720 = 0.00% |

Here Zero-Step is **not** order-independent — 80% of all possible orderings produce some symmetry break,
exactly the same frequency as Units-Digit. The two methods diverge only in magnitude (1pp max vs. 10pp
max), not in how often the underlying bug fires. This directly refines round 2's §C.1 (which showed one
example of this) into an exhaustive, exact figure, and corrects any impression Fixture C alone might give
that Zero-Step is immune.

### C.4 Two findings beyond what ChatGPT's spec asked for

**Neck's unreachability is structural, not incidental — proven, not observed.** Fixture C's fractional
remainders at N=10 are Head 0.5, R Leg 0.4, L Leg 0.4, Neck 0.3, R Arm 0.2, L Arm 0.2, Torso 0.0. The
apportionment always has exactly 2 remainder slots to give out (fixed by the weights and N, independent of
order), and Head's fraction (0.5) is *strictly* larger than every other zone's, so it always claims one
slot regardless of order; the R Leg/L Leg tie at 0.4 always claims the other, since 0.4 > 0.3 > 0.2 > 0.0
in every possible ranking. Neck's 0.3 can never out-rank both of those — there is no ordering under which
it could. The sweep's 5,040/5,040 result isn't a coincidence; it follows from the fraction values
themselves and would hold even if a permutation trillion orderings were tried instead of 5,040.

**MAE is provably invariant to table order under this apportionment method — proven, not just observed.**
Every one of the four sweeps above shows Mean MAE = Worst MAE = Best MAE, exactly. This isn't specific to
these two fixtures. For any weight set and domain `N`: let `frac_i = quota_i − floor(quota_i)` for each
zone. The total remainder `R = N − Σfloor(quota_i)` is fixed by the weights and `N` alone — order can't
change it. Since `Σquota_i = N` exactly (weights sum to 1), `Σfrac_i = R` exactly, always. Largest-remainder
selects the `R` zones with the largest `frac_i` values to receive a bonus slot; reordering can only swap
*which* zone gets picked when fractions tie (as with R Leg/L Leg above) — it cannot change the *multiset*
of fractional values that ends up selected, since that's fixed by sorting values, not labels. Total
absolute error works out to `2R − 2·Σ(selected fracs)`, and since the selected-fracs sum is order-invariant,
so is the total, and so is MAE (`= total / zone count`). Practically: **table order decides which zone
absorbs the table's fixed total error, never how much total error exists.** Worth noting for ChatGPT's own
§16/§18 metric list — "Worst MAE" and "Best MAE" are guaranteed identical to "Mean MAE" under this
apportionment method for *any* fixture, so they add no information beyond confirming the invariant holds;
per-zone worst-case error (which does vary, per §C.2/§C.3's per-zone tables) is where the real signal is.

---

## D. What This Confirms, Sharpens, or Complicates

| Round 2 claim (single example) | Round 3 exhaustive result |
|---|---|
| Zero-Step also breaks symmetry under reordering (one Fixture-A example) | **Sharpened:** 80.00% of all 720 Fixture-A orderings break symmetry under Zero-Step — identical frequency to Units-Digit; only the magnitude (1pp vs. 10pp max) differs |
| Units-Digit makes Neck unreachable (one Fixture-C example) | **Sharpened to a proof:** unreachable in all 5,040 possible orderings — a structural fact about this weight set, not an unlucky table order |
| (not previously tested) | **New:** MAE is provably order-invariant under largest-remainder apportionment, for any weight set |
| (not previously tested) | **New:** Fixture C's apparent Zero-Step "order-independence" is a degenerate case specific to weights that are exact multiples of 100 — not a general property, confirmed by contrast with Fixture A |

Nothing from round 1 or round 2 is contradicted. Everything above strengthens the existing pro-Zero-Step
evidence (round 2's framing — smaller worst-case consequence from a shared bug — holds up under exhaustive
rather than single-sample testing) while correcting the one way Fixture C's specific numbers could
overstate that case if read in isolation.

---

## E. Updated Ready-for-v1.2 Log

Extends round-2 report §F. Still not applied to any canonical document.

| Item | Source | Status |
|---|---|---|
| Provider signature, boundary wording, Tier-2 criterion reinterpretation, optional title rename, "additional mapping stage" rename, per-zone-error-as-primary-metric | Round 1–2 logs | Unchanged, still logged |
| **Domain Resolution** as an explicit S-2 interface characteristic: *"The Location Index domain determines the granularity available to downstream anatomical mapping. A larger domain permits finer probability representation and reduces the magnitude of discretisation error introduced by downstream mapping."* | ChatGPT §12 | **New** — accepted verbatim, attaches to S-2 itself per §B above |
| Consolidated S-2 scope statement (S-2 owns index generation + domain size/resolution; future mapping spec owns index→zone, weights, symmetry, apportionment, order-independence, reachability, hierarchy) | ChatGPT §22 | **New** — accepted as a clean restatement, not a change of substance from what's already logged |
| Label the pair-aware fix (round-2 §C.2) as **"Rejected experimental repair — symmetry restored, aggregate fidelity worsened"** | ChatGPT §24.2 | **New** — accepted, adopted as the standing label for that finding |
| Note that "Worst MAE"/"Best MAE" are redundant with "Mean MAE" under largest-remainder apportionment; per-zone worst-case error is the metric that actually varies | This document, §C.4 | **New** |

---

## F. Disposition of ChatGPT's §23 Governance List

| ChatGPT's list | Disposition |
|---|---|
| **Accepted:** mapping-stage rename, per-zone-error primacy, symmetry/order/reachability as future mapping-spec criteria | Agree — already logged (§E) |
| **Add:** domain size/resolution as explicit S-2 interface characteristic; note that downstream errors scale with S-2's domain choice | Agree — logged (§E) |
| **Do not yet add:** Zero-Step lock, final mapping algorithm, symmetry-preserving algorithm, universal Tier-1 mandate | Agree, unchanged — nothing in this document argues for any of these either |

---

## G. Phase 2 (Fixtures D/E/F/G) — Not Executed, Needs a Decision

ChatGPT's own gate (§26): run Phase 1 first, and only proceed to D/E/F/G "if that result behaves as
expected." It did — arguably more strongly than expected (§C.4's two structural proofs go beyond mere
confirmation). That clears the gate ChatGPT set. What it doesn't clear is that **Fixtures E and F require
inventing content that doesn't exist yet** — ChatGPT's own spec leaves Wing A/Wing B's weights as
placeholders ("X%") and F's zone list without explicit L/R pairing declarations. Running those means this
document would be authoring a creature's anatomy and a 12–20 zone humanoid table from scratch, not just
computing against already-agreed data — a different kind of task than the order sweep. Flagged here as a
decision point rather than executed unprompted; §G of this document is intentionally short because the
actual next step depends on that decision, not on anything left ambiguous by the math.

**Fixture G** (systematic order sweep, generalized) is already fully executed by this document, against
both C and A — the remaining unswept fixtures are specifically D, E, and F, which need weights authored
first.

---

## H. Current Evidence State

Extends ChatGPT's §20 evidence matrix with this round's results:

| Finding | Zero-Step | Units-Digit | Status |
|---|---|---|---|
| Native domain / resolution | 100 / 1% | 10 / 10% | S-2 property |
| Fixture C accuracy | Exact (tautological, §C.3) | Mean 3.14pp error | Confirmed, round 1 |
| Fixture C order-sensitivity | **0% of orderings** (degenerate case) | **100% of orderings** | **New, exhaustive** |
| Fixture C Neck reachability | N/A (never unreachable) | **Unreachable in 100% of orderings — proven structural** | **New, exhaustive** |
| Fixture A order-sensitivity | 80% of orderings | 80% of orderings (same frequency) | **New, exhaustive** |
| Fixture A/C worst-case magnitude when order-sensitivity fires | 1pp / 0pp | 10pp / 10pp | Confirms 10× domain-ratio pattern holds exhaustively |
| MAE order-invariance | Proven | Proven | **New, general proof** |
| Pair-aware symmetry repair | N/A | Rejected — fixes symmetry, worsens MAE and Torso error | Round 2, labeled per §E |

---

## I. Proposed for Cross-Review

1. Given Phase 1 cleared ChatGPT's own gate, is Phase 2 (D/E/F/G) wanted next, with this document
   authoring the missing weights for E and F — or should those weights come from the designer first?
2. §C.4's MAE-invariance proof suggests "Worst MAE"/"Best MAE" (ChatGPT §16, §18) should be dropped from
   future acceptance-test specs as redundant with Mean MAE, in favor of per-zone worst-case error. Agree,
   or is there a reason to keep them (e.g., as a cheap sanity check that the invariant still holds on a
   new fixture)?
3. Does the Fixture-C-is-degenerate-for-Zero-Step finding (§C.3) change how Fixture C should be described
   going forward — e.g., should it be relabeled as illustrating Zero-Step's best case specifically, rather
   than a general-purpose comparison fixture, given it can no longer demonstrate order-sensitivity for
   that method at all?

**Next:** per §G, awaiting a decision on Phase 2 before any further computation.
