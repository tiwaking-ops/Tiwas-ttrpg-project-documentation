# Tiwas — S-2 Round 2: Response to ChatGPT's Review of the Experiment (v1.0)

**Status:** Response to `Tiwas_S-2_Experiment___Analysis__Review___Recommendations-v1-chatgpt.md`, ChatGPT's
22-section review of `Tiwas_S2_Experiment_ChatGPT_Response_v1.md` (this project's own prior experiment
report). This document analyzes and assesses that review, and adds two newly-verified checks that refine
two of its claims. **It does not lock S-2, does not run the new stress-test fixtures ChatGPT proposes
(§18), and does not edit S-2 v1.1 or the prior experiment report.** Per the task scope this round
("analyze, assess, explain" rather than "execute"), the two checks below are small, targeted verifications
of specific claims — not a new full-fixture experiment. That remains available as a next action (§G).

**Chain position:** S-2 v1.1 → Claude's experiment report → ChatGPT's review (this document's subject) →
this document → (next) awaiting further review or a decision to run ChatGPT's proposed stress test.

---

## A. What ChatGPT's Review Says, Condensed

ChatGPT's overall verdict: the experiment is methodologically sound and produced a genuinely new finding
(§1), not just confirmation of the expected accuracy gap. Its own headline claim: **Units-Digit's 10-value
domain is a hard representational ceiling** — it can only express probabilities in 10-point increments,
which it frames as an architectural limitation on "vocabulary," not merely reduced precision (§3). It
praises the Fixture-C-neutrality catch (§2.2) and the table-order reordering test (§7) as the two strongest
pieces of methodology, offers one direct refinement to the "no tie-break rule avoids this" claim (§8),
raises a fair critique of the "mapping operations" metric (§11), proposes Symmetry Preservation and
Table-Order Independence as new formal acceptance criteria (§13, §18, §20), and concludes with a
recommendation to treat Zero-Step as the "leading Tier-1 candidate" without locking S-2 (§17, §22), plus a
proposed four-fixture stress test (D/E/F/G, §18) before any designer ruling.

---

## B. Where This Document Agrees Outright

| ChatGPT § | Claim | Agreement |
|---|---|---|
| §2.1 | Correctly avoided locking S-2 | Agree |
| §2.2 | Fixture C neutrality catch was a genuine methodological strength | Agree — this was flagged as this project's own §B.1 in the prior report; ChatGPT independently confirms it holds up |
| §3 | Units-Digit's 10-point granularity is architectural, not just "less accurate" | Agree, and independent of apportionment algorithm — see §C.1 |
| §4 | Fixture A's exact 10× error ratio is real and meaningful even for an "ordinary" uniform table | Agree, algebraically exact (prior report §E.1) |
| §5 | Units-Digit's Fixture B advantage is step-count, not accuracy | Agree — matches prior report §B.2 exactly |
| §6 | Neck-unreachable and Leg-asymmetry are the two serious Fixture C results | Agree |
| §9 | Zero-Step vs. Units-Digit is a domain-size/mapping-complexity trade-off, not just "two formulas" | Agree as a useful frame, minor caveat in §C.3 |
| §10 | The experiment does not prove Zero-Step should be the universal *tier* default (Tier 0/1/2 selection is a separate question from Tier-1 formula selection) | Agree — important distinction, correctly kept separate from Recommendation 1 |
| §14 | Aggregate stats should not be the primary reporting unit | Agree — matches prior report §E.3 exactly |
| §21 | Experimental findings should stay in the S-2 WIP/review chain, not merge into canonical docs | Agree, unchanged from prior report's own position |

No disagreement on any of the above. The remainder of this document is where independent judgment adds
something ChatGPT's review did not already establish.

---

## C. Independent Assessment — Refinements

### C.1 Table-order dependence is a property of the apportionment algorithm, not of Units-Digit specifically — verified

ChatGPT's §7 frames the reordering result (prior report §E.2) as evidence specifically about Units-Digit:
*"table ordering becomes mechanically significant... dangerous for a generic RPG subsystem"* in the context
of Units-Digit. That's true as far as it goes, but it understates something worth making explicit: **the
same vulnerability exists under Zero-Step too**, at a smaller magnitude. Verified directly by applying the
identical reordering used in the prior report's Fixture A check (Head, L Leg, R Arm, L Arm, R Leg, Torso)
to both methods:

| Method | Domain N | R Leg | L Leg | Gap | Symmetric? |
|---|---|---|---|---|---|
| Zero-Step | 100 | 16 | 17 | **1.00pp** | No |
| Units-Digit | 10 | 1 | 2 | **10.00pp** | No |

Both break symmetry under the same reordering. The gap scales with domain size exactly as §E.1 of the
prior report predicts (10×). This means "table-order independence" (ChatGPT §18 item 5, §20's "Add" list)
is not a property that distinguishes Zero-Step from Units-Digit as derivation formulas — it's a property
of the **largest-remainder-with-table-order-tie-break apportionment algorithm**, which both methods were
tested through identically (§C.3 of the prior report). What *does* distinguish the two methods is how
severe the consequence is when the (shared) vulnerability triggers: a 1pp accident is usually
inconsequential; a 10pp accident (one limb struck twice as often as its mirror) is not. This sharpens
rather than weakens the case for Zero-Step — its advantage isn't immunity to the bug, it's that the bug's
worst case is small enough not to matter in practice.

### C.2 "Additional machinery" can restore symmetry — but the first natural attempt makes overall accuracy worse

ChatGPT §8 is right to push back on over-reading "no tie-break rule avoids this" as "no Units-Digit system
could ever preserve symmetry" — with added machinery (its own list: paired-zone handling, weighted bucket
duplication, secondary deterministic selection, conditional remapping, another die/roll property),
symmetry is recoverable in principle. §8 stops at the conceptual claim; this section tests one concrete
version of it.

**Method tested:** a symmetric-pair-aware apportionment rule — each declared-equal pair (R Arm/L Arm,
R Leg/L Leg) is individually floored and forced equal, and the slots this frees up are redistributed
proportionally among the *remaining* zones (Head, Neck, Torso) by ordinary largest-remainder. Applied to
Fixture C / Units-Digit:

| Zone | Intended % | Plain largest-remainder (prior report) | Pair-aware (this check) |
|---|---|---|---|
| Head | 5.00 | 10.00 (+5.00) | 10.00 (+5.00) |
| Neck | 3.00 | 0.00 (−3.00, unreachable) | 0.00 (−3.00, unreachable) |
| Torso | 40.00 | 40.00 (+0.00) | **50.00 (+10.00)** |
| R Arm | 12.00 | 10.00 (−2.00) | 10.00 (−2.00) |
| L Arm | 12.00 | 10.00 (−2.00) | 10.00 (−2.00) |
| R Leg | 14.00 | 20.00 (+6.00) | 10.00 (−4.00) |
| L Leg | 14.00 | 10.00 (−4.00) | 10.00 (−4.00) |
| **Mean abs error** | | **3.143pp** | **4.286pp** |
| **R Leg = L Leg?** | | No | **Yes** |
| **Neck reachable?** | | No | **No** |

The fix does exactly what it was designed to do — legs are symmetric. But mean absolute error across the
table gets *worse* (4.286pp vs. 3.143pp), Torso's error becomes the single largest error in either version
(+10pp — worse than the original leg asymmetry it replaced), and Neck is still unreachable; forcing the leg
pair to its floor freed up a slot, but proportional redistribution sent nearly all of it to Torso (already
the largest zone) rather than to Neck (the zone that actually needed it). This is a stronger, more concrete
version of ChatGPT's own conclusion — *"the moment Units-Digit requires special handling to repair its
coarse domain, much of its architectural advantage begins to disappear"* — it's not just that machinery is
required, it's that the first reasonable-looking piece of machinery can trade one visible problem for a
worse one elsewhere. This is one candidate fix, not an exhaustive search; a Neck-aware or jointly-optimized
redistribution rule might do better. That search is exactly what ChatGPT's Fixture G (§E below) would be
useful for.

### C.3 Where the new acceptance criteria should actually attach

ChatGPT's §13 (Symmetry Preservation) and §18/§20 (Table-Order Independence, Unreachable-Zone Detection)
are good criteria and this document agrees with adding them somewhere. The precision worth adding: S-2 v1.1
§B's own pipeline table already assigns ownership —

```
S-2 (this document)         Roll → Location Index              Resolved here
Setting / location table    Location Index → named zone         Not yet built — likely Setting-Module scope
```

Everything both C.1 and C.2 above exercise is the **second** stage (index-to-zone mapping via an
apportionment/binning scheme), not the first (which formula produces the index). §C.1 shows the
vulnerability these criteria are meant to catch is a property of that second stage's algorithm, triggered
identically regardless of which S-2 formula feeds it. So: **Symmetry Preservation, Table-Order
Independence, and Unreachable-Zone Detection are correctly proposed criteria, but they are acceptance
criteria for the future location-table-mapping spec, not for S-2's own Zero-Step-vs-Units-Digit choice.**
S-2 still owns a related but distinct fact worth keeping as its own criterion: *domain size*, which
determines how expensive a downstream mapping mistake is allowed to be before it becomes anatomically
significant (1pp vs. 10pp, per §C.1). That distinction matters for exactly the reason ChatGPT's own first
review of S-2 v1.1 warned about — not letting S-2 "become an accidental combat subsystem containing
everything anatomical" by absorbing scope that belongs to the location-table stage.

### C.4 What "leading candidate" should and shouldn't be read as claiming

ChatGPT's own §10 already hedges this correctly — the evidence answers *"which Tier-1 formula interfaces
better with arbitrary weighted tables,"* not *"should every scene use Tier 1."* Worth stating the same
hedge from the other direction, using this experiment's own results: Fixture B showed the two methods tied
exactly on accuracy (§D.3 of the prior report), and mapping-stage count still favors Units-Digit there. So
"leading candidate" should be read narrowly — leading specifically for tables that are non-uniform, or
uniform but not exactly 10 zones, which is most tables a designer would actually author. It is not a claim
that Units-Digit has no legitimate niche (ChatGPT's own Recommendation 2 already gets this right) or that
step-count stops mattering (Priority 3 is still in the priority ranking, just behind Priority 1).

---

## D. Disposition of ChatGPT's §22 Action List

| # | ChatGPT recommendation | Disposition |
|---|---|---|
| 1 | Accept the experiment as valid evidence | N/A — self-referential to the prior report |
| 2 | Record Zero-Step as leading Tier-1 candidate | Agree, scoped per §C.4 |
| 3 | Retain Units-Digit as an optional coarse/specialized mode | Agree |
| 4 | Add symmetry + table-order independence to acceptance criteria | Agree in substance; **attach to the location-table-mapping spec, not S-2 itself** (§C.3) |
| 5 | Run a final multi-table stress test (Fixtures D/E/F/G) | Reasonable next step; assessed but not executed this pass (§E) |
| 6 | Formal designer ruling if Zero-Step passes | Matches the multi-stage lock process both S-1 and S-2 already follow |
| 7 | Update S-2 v1.2 and the Roadmap | Consistent with this project's "log for v1.2, don't touch canon yet" approach |
| 8 | Only then promote into canonical architecture | Agree — matches governance discipline throughout |

§20's **Reword** item (rename "number of mapping operations" → "additional mapping stage" or
"mapping-stage count") is also accepted — ChatGPT's §11 critique is fair: the original metric measured
whether an intermediate lookup stage exists at all, not actual computational cost (which depends on
implementation choice — array access, range comparison, binary search). Folded into §F below.

---

## E. Assessment of the Proposed Stress-Test Fixtures (§18) — Not Executed This Pass

| Fixture | Assessment |
|---|---|
| **D** (9-zone symmetric combat table) | Well-specified enough to run as-is; a natural extension combining A's zone-splitting with B's zone count. |
| **E** (asymmetric creature: Head/Neck/Torso/Wing A/Wing B/Tail/R Leg/L Leg) | Under-specified — doesn't state whether Wing A/Wing B carry equal or different weights, so "intentional asymmetry" isn't runnable without a designer first supplying actual numbers. |
| **F** (12–20 zone granular table) | Reasonable direction; the listed zones (shoulders, upper-arms, forearms, etc.) aren't explicitly marked as paired-per-side in ChatGPT's list, so which pairs count as "declared symmetric" would need to be fixed before running. |
| **G** (systematic order-variation stress test) | The most directly actionable of the four — a generalization of §C.1's single manual reordering into an exhaustive or large-sample sweep over permutations, for a given fixture. Most efficient way to actually validate "table-order independence" as a criterion rather than spot-check it. |

If a stress-test pass is wanted next, **G run against Fixture C** (or D) is the highest-value single
addition — it would convert §C.1's one-reordering demonstration into a full distribution of how often and
how badly naive apportionment breaks symmetry across all possible zone orderings, for both methods.

---

## F. Updated Ready-for-v1.2 Log

Extends the prior report's §F. Still not applied to any canonical document.

| Item | Source | Status |
|---|---|---|
| Provider signature, boundary wording, Tier-2 criterion reinterpretation, optional title rename | Prior report §F.1–F.4 | Unchanged, still logged |
| Rename "number of mapping operations" → "additional mapping stage" | ChatGPT §11, §20 | **New** — accepted, see §D above |
| Add Symmetry Preservation, Table-Order Independence, Unreachable-Zone Detection as formal acceptance criteria | ChatGPT §13, §18, §20 | **New** — accepted, attach to the future location-table-mapping spec per §C.3, not to S-2 itself |
| Per-zone error as the primary distribution metric (not aggregates) | ChatGPT §14; prior report §E.3 | **New** — both documents independently reached this; log as confirmed |

---

## G. Recommended Next Action

Two independent options, not mutually exclusive:

1. **Run Fixture G-style order-sweep** (§E) against Fixture C or D to turn §C.1's single demonstration into
   a full distribution — cheapest, highest-value next computational step.
2. **Specify Fixtures D/E/F fully** (fill in E's wing weights, F's L/R pairing) and run ChatGPT's complete
   stress test (§18) before any designer ruling, per ChatGPT's own recommended sequencing (§22, items 5–6).

Either is available on request; neither is executed here, consistent with this round's "explain" rather
than "execute" scope.

---

## H. Proposed for Cross-Review

1. Does §C.3's scope split — symmetry/order-independence criteria belong to the location-table-mapping
   stage, domain-size sensitivity stays an S-2 property — hold up, or does it draw the S-2/downstream
   boundary in the wrong place?
2. Is the pair-aware fix tested in §C.2 worth treating as a cautionary example (a plausible-looking fix
   that backfires) worth keeping on record, or was it too naive a first attempt to be representative of
   what "additional machinery" could actually achieve?
3. Given §C.1's finding, should S-2's own eventual write-up say anything about domain size as a
   risk-multiplier for downstream mapping errors — or does that reasoning belong entirely to whichever
   document ends up owning the location-table-mapping spec?

**Next:** per §G, either the order-sweep or the full D/E/F/G stress test, on request.
