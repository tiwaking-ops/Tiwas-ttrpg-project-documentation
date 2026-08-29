# Tiwas S-2 Experiment — Analysis, Review & Recommendations

**Source reviewed:** `Tiwas_S2_Experiment_ChatGPT_Response_v1-claude.md`  
**Related authorities:** Tiwas Canonical Rules & Changelog v1.1; Tiwas Proposals, WIP & Design Direction v1.1; Tiwas Implementation Roadmap & Project Governance v1.1  
**Review status:** Independent cross-review of ClaudeAI's S-2 experiment  
**Conclusion:** Strong experiment and materially useful evidence, but **not yet sufficient by itself to lock Zero-Step**.

---

## 1. Executive Summary

ClaudeAI's experiment is well executed and, importantly, it has produced a **genuinely useful new finding** rather than merely confirming the expected mathematical difference between Zero-Step and Units-Digit.

The most significant result is:

> **Units-Digit's 10-value resolution domain cannot faithfully represent arbitrary fine-grained anatomical weights, and the resulting discretisation can create an unintended left/right anatomical asymmetry.**

The Fixture C result is particularly important:

- R Leg intended: **14%**
- L Leg intended: **14%**
- Units-Digit result: **R Leg 20%, L Leg 10%**

This is not merely a poor tie-break rule. The underlying problem is that 14% of a 10-slot domain is **1.4 slots**. An integer 10-slot system cannot represent both zones as 14%. Some distortion is mathematically unavoidable.

ClaudeAI then strengthens the finding by showing that the asymmetry can move when table order changes. That demonstrates that the resulting asymmetry can be an artefact of the mapping/apportionment process rather than an authored anatomical distinction.

My overall assessment is therefore:

**The experiment is methodologically sound enough to materially change the S-2 decision landscape. However, the correct conclusion is not yet simply "Zero-Step wins." The stronger conclusion is that Units-Digit has a structural expressiveness limitation that conflicts with Tiwas's Priority 1 whenever the location table requires granularity finer than 10% or requires arbitrary weighted symmetry.**

That distinction matters.

---

# 2. What ClaudeAI Did Well

## 2.1 It did not prematurely lock S-2

This is exactly correct.

The experiment explicitly states that it:

- does not lock S-2;
- does not select Zero-Step;
- leaves S-2 as the next decision awaiting cross-review.

That conforms to the Roadmap requirement that S-2 remain open until the location architecture and candidate methods have been experimentally evaluated.

This is especially important because the Roadmap defines the S-2 simulation gate in terms of:

- resolution steps;
- wound frequency;
- location distribution;
- lethality;
- Priority-1 simulation fidelity.

ClaudeAI has addressed **location distribution** very well, but not yet the downstream wound/lethality dimensions—which it correctly says cannot meaningfully be evaluated until S-4 exists.

That is a limitation of the experiment, not a flaw in the experiment.

---

## 2.2 It correctly identified the Fixture C neutrality problem

This is one of the strongest methodological points in the report.

The original Fixture C was expressed directly as 1–100 ranges. Since Zero-Step itself produces a 1–100 Location Index, testing Zero-Step against those ranges essentially gives Zero-Step the same representational domain as the fixture.

ClaudeAI correctly observes that a literal implementation would make Zero-Step's 0% error largely tautological.

Recasting the ranges as weights and then independently apportioning them into each method's domain is therefore a defensible correction.

This produces a much better comparison:

```text
Same anatomical intention
        ↓
Different native location domains
        ↓
Independent mapping
        ↓
Compare resulting distributions
```

That is much more informative than simply asking which method reproduces a table already written in its own native domain.

### Important caveat

ClaudeAI is also correct to flag this as a **methodological choice**, not something specified by the original experiment.

The weights were inferred from the ranges. That means Fixture C is no longer literally "the original Fixture C"; it is a normalized interpretation of it.

That is acceptable for an experiment, provided we keep calling it an experimental fixture rather than canonical evidence.

---

# 3. The Most Important Finding: Units-Digit Has a Granularity Ceiling

This is the key result.

Units-Digit produces exactly ten equally probable Location Index values:

```text
1 → 10%
2 → 10%
...
10 → 10%
```

ClaudeAI independently reconfirmed that distribution over all 100 rolls.

This creates a hard representational limit.

A location table using Units-Digit can only assign probabilities in increments of:

**10 percentage points**

unless some additional mechanism is introduced.

That means it cannot natively represent:

- 3%;
- 5%;
- 7%;
- 12%;
- 14%;
- 17%;
- 23%;
- etc.

without approximation.

This is more significant than simply saying "Units-Digit is less accurate."

It means:

> **Units-Digit does not merely produce less precise results; it restricts the vocabulary of location distributions that a generic location table can express.**

That is an architectural property.

---

# 4. Fixture A: The 10× Error Difference Is Useful

Fixture A contains six equal-weight locations.

The intended probability is:

`100 / 6 = 16.666...%`

Zero-Step gives:

- four zones at 17%;
- two at 16%.

Units-Digit gives:

- four zones at 20%;
- two at 10%.

The resulting mean absolute errors are:

- Zero-Step: **0.444pp**
- Units-Digit: **4.444pp**

Maximum errors:

- Zero-Step: **0.667pp**
- Units-Digit: **6.667pp**

The experiment establishes that the ratio is exactly 10×.

This is strong evidence for the intuitive proposition:

> A 100-value location domain has ten times the probability resolution of a 10-value domain.

That is not surprising mathematically, but the experiment converts it into concrete anatomical consequences.

More importantly, this result demonstrates that the problem isn't restricted to exotic weighted tables.

Even the extremely ordinary case of **six equally probable locations** already causes substantial distortion under Units-Digit.

---

# 5. Fixture B: Units-Digit's Real Advantage Is Simplicity

This part of ClaudeAI's analysis is also correct.

With ten equally weighted locations:

```text
Units-Digit:
1 → Head
2 → Face/Neck
...
10 → Legs
```

No second lookup operation is needed.

Zero-Step still needs the location index mapped into the anatomical table.

Yet both achieve exactly:

**10% per location.**

So Units-Digit's advantage here is not accuracy.

It is:

> **structural simplicity / direct indexing.**

ClaudeAI appropriately narrows the claim rather than overstating it.

This is important because S-2's design priorities include minimum resolution steps, but only **after** Priority 1 has been respected. The Canonical Rules explicitly rank granular physical simulation first and minimum resolution steps third.

Therefore Fixture B establishes a legitimate Units-Digit advantage, but only in a relatively narrow circumstance.

---

# 6. Fixture C Reveals the Real Architectural Problem

Fixture C is where the experiment becomes much more consequential.

The intended table is:

| Location | Intended |
|---|---:|
| Head | 5% |
| Neck | 3% |
| Torso | 40% |
| R Arm | 12% |
| L Arm | 12% |
| R Leg | 14% |
| L Leg | 14% |

Zero-Step reproduces all seven exactly.

Units-Digit produces:

| Location | Intended | Units-Digit |
|---|---:|---:|
| Head | 5% | 10% |
| Neck | 3% | **0%** |
| Torso | 40% | 40% |
| R Arm | 12% | 10% |
| L Arm | 12% | 10% |
| R Leg | 14% | **20%** |
| L Leg | 14% | **10%** |

The particularly serious results are:

### Neck becomes unreachable

The intended 3% probability cannot be represented in ten equal buckets.

It gets zero buckets.

So Units-Digit does not merely make the neck slightly less likely.

It makes:

> **Neck impossible.**

That is a much stronger failure.

### The legs become asymmetric

The two legs were authored identically.

Yet:

```text
R Leg = 20%
L Leg = 10%
```

One leg is twice as likely to be struck as the other.

This is precisely the kind of result that conflicts with Tiwas's stated priority of granular physical simulation.

---

# 7. The Table-Order Test Is Particularly Valuable

This is arguably the best piece of evidence in the entire experiment.

ClaudeAI changes the order of Fixture A while keeping the underlying weights identical and observes that the L/R allocation changes.

That demonstrates that the asymmetry is not fundamentally anatomical.

It arises because:

```text
fractional quota
       ↓
integer apportionment
       ↓
tie
       ↓
table-order tie-break
       ↓
anatomical asymmetry
```

Therefore table ordering becomes mechanically significant.

That is dangerous for a generic RPG subsystem.

A GM or designer should not accidentally change the probability of hitting someone's right leg simply because they reordered a table for readability.

ClaudeAI correctly identifies this as a **structural discreteness problem**, not something that can be solved merely by choosing a different tie-break rule.

---

# 8. One Important Refinement to ClaudeAI's Claim

I agree with ClaudeAI's conclusion, but I would phrase one part more carefully.

It says:

> "No tie-break rule avoids this."

That is true **under the generic ten-slot proportional-apportionment model being tested**.

But it should not be interpreted as:

> "No Units-Digit system could ever preserve symmetry."

A specially designed Units-Digit location algorithm could introduce additional rules, such as:

- paired-zone handling;
- weighted bucket duplication;
- secondary deterministic selection;
- conditional remapping;
- another die or roll property.

However, every such solution introduces additional machinery.

That matters because it changes the comparison.

The actual question is not:

> "Can Units-Digit theoretically be made to represent arbitrary anatomical distributions?"

Of course it can, if enough additional machinery is added.

The correct question is:

> **Can Units-Digit provide the required location fidelity while retaining its claimed near-zero-step simplicity?**

The experiment strongly suggests **no**.

The moment Units-Digit requires special handling to repair its coarse domain, much of its architectural advantage begins to disappear.

---

# 9. A Deeper Finding: The Choice Is Really Between Two Design Philosophies

The experiment reveals that Zero-Step and Units-Digit aren't merely two formulas.

They embody different philosophies.

### Units-Digit

```text
Small domain
↓
Simple lookup
↓
Very low mapping complexity
↓
Coarse probability resolution
```

### Zero-Step

```text
Large domain
↓
Slightly more mapping work
↓
Fine probability resolution
↓
Arbitrary weighted anatomical tables
```

This makes the choice much easier to reason about.

The real S-2 question becomes:

> **Does Tiwas value a universally expressive anatomical mapping domain more than eliminating one lookup operation?**

Given the current Canonical priorities, I believe the answer is increasingly clear.

Priority 1 is:

> Granular physical simulation where the situation warrants it.

Priority 3 is:

> Minimum resolution steps per exchange without sacrificing Priority 1.

Therefore simplicity cannot be purchased by sacrificing the ability to represent meaningful anatomical distinctions.

---

# 10. The Experiment Does Not Yet Prove Zero-Step Is the Universal Default

This distinction is important.

The evidence supports:

### Strongly supported

**Zero-Step is the superior candidate for arbitrary weighted anatomical tables.**

### Strongly supported

**Units-Digit is superior in directness when the table has exactly ten equally weighted locations.**

### Strongly supported

**Units-Digit has a hard 10%-bucket granularity limitation under the tested generic mapping model.**

### Not yet demonstrated

That Zero-Step should necessarily be the **universal default location policy**.

Why?

Because S-2 has three location tiers:

- Tier 0 — no location;
- Tier 1 — lightweight derivation;
- Tier 2 — full location/armour/surgery model.

And the current design direction favours situation-dependent granularity rather than forcing one level everywhere.

So the experiment answers an important sub-question:

> **Which Tier-1 location derivation better interfaces with arbitrary anatomical tables?**

The evidence strongly favours Zero-Step.

It does **not by itself** answer:

> **Should every Tiwas scene use Tier 1?**

That remains a separate architectural decision.

---

# 11. ClaudeAI's "Mapping Operations" Metric Needs Caution

This is the weakest methodological part of the experiment.

ClaudeAI defines:

- 0 operations when the index directly equals the zone number;
- 1 operation otherwise.



This is reasonable as a simplified comparison, but it is not a very robust measure of computational complexity.

For example:

```text
Zero-Step calculation:
floor + modulo + multiplication + addition + table lookup
```

versus:

```text
Units-Digit:
modulo + special-case handling + direct index
```

And an actual lookup implementation could be:

- an array access;
- a range comparison;
- a binary search;
- a switch;
- a precomputed table.

So "1 mapping operation" should not be treated as a literal computational-cost measurement.

I recommend renaming it to something like:

> **Mapping-stage count**

or:

> **Additional mapping stage**

rather than "number of mapping operations."

The important result remains valid:

**Units-Digit can directly identify a zone when there are exactly ten equally weighted zones.**

---

# 12. The Experiment Also Exposes a Design Requirement for the Location Table

There is a broader architectural lesson here.

The S-2 architecture currently treats the Location Index as an intermediate numeric value and requires a separate anatomical mapping table.

The experiment demonstrates that the mapping table should probably be treated as a **first-class design object**, rather than simply a list of names.

A location table needs to be able to express at least:

- zone identity;
- probability/weight;
- L/R pairing;
- anatomical grouping;
- possibly parent/child relationships;
- possibly location tags;
- possibly alternate tables for different creatures/settings.

This becomes especially important for Tier 2.

For example:

```text
Location Table
├── Head
├── Neck
├── Torso
├── R Arm
│   └── R Hand
├── L Arm
│   └── L Hand
├── R Leg
└── L Leg
```

That is much richer than simply:

```text
1 = Head
2 = Neck
3 = Torso
...
```

The S-2 architecture should therefore avoid defining the mapping mechanism so narrowly that later anatomical systems have to work around it.

---

# 13. Symmetry Should Become an Explicit Acceptance Criterion

This is my strongest recommendation arising from the experiment.

S-2 should not merely test:

> "Does the resulting distribution approximately match the intended weights?"

It should also test:

> **"Does the mapping preserve explicitly authored symmetry?"**

For example:

```text
R Arm = L Arm
R Leg = L Leg
R Hand = L Hand
```

If the table declares those pairs equal, a generic location provider should not silently make them unequal.

I would therefore add a formal acceptance test:

### Symmetry Preservation

> Where a location table explicitly assigns identical weights to paired anatomical zones, the location provider must preserve equal probability unless the table explicitly declares an intentional asymmetry.

This would turn ClaudeAI's discovery into a permanent regression test.

---

# 14. Aggregate Statistics Should Not Be the Primary Test

ClaudeAI makes an excellent observation here.

Units-Digit's Fixture C legs aggregate to:

**30%**

against intended:

**28%**

At first glance, +2 percentage points seems fairly minor.

But the actual result is:

```text
R Leg = 20%
L Leg = 10%
```

The aggregate hides the clinically/game-mechanically important difference.

For a physical simulation system, the relevant unit is the **anatomical zone**, not merely the body-region aggregate.

Therefore future S-2 experiments should report at least:

1. Per-zone probability.
2. Per-zone absolute error.
3. Maximum per-zone error.
4. Paired-zone symmetry.
5. Unreachable zones.
6. Aggregate anatomical-region error.

ClaudeAI has effectively established this reporting standard already.

---

# 15. What the Experiment Has Actually Established

I would summarize the evidence as follows:

| Question | Current evidence |
|---|---|
| Can Zero-Step represent arbitrary 1–100 weighted tables? | **Yes** |
| Can Units-Digit represent arbitrary weighted tables? | **No, not without approximation/additional machinery** |
| Does Zero-Step provide finer probability resolution? | **Yes — 1% native resolution vs 10%** |
| Does Units-Digit work perfectly for ten equal zones? | **Yes** |
| Does Zero-Step work perfectly for six equal zones? | Not exactly, but error is very small |
| Does Units-Digit work well for six equal zones? | **Poorly relative to Zero-Step** |
| Can Units-Digit make a location unreachable? | **Yes — Neck in Fixture C** |
| Can Units-Digit create unintended L/R asymmetry? | **Yes** |
| Is that asymmetry dependent on table ordering? | **Yes, demonstrated** |
| Is the problem fixable by merely changing the tie-break? | **No, not generically** |
| Does Units-Digit have an implementation simplicity advantage? | **Yes** |
| Does it have an accuracy advantage? | **No evidence of one** |
| Does the experiment prove Zero-Step should be universal? | **No** |
| Does it materially strengthen Zero-Step as the Tier-1 candidate? | **Yes** |

---

# 16. Relationship to Tiwas's Canonical Priorities

This is where the experiment becomes more than a mathematical exercise.

The locked Tiwas priorities are:

1. Granular physical simulation where warranted.
2. Heroic resilience.
3. Minimum resolution steps without sacrificing Priority 1.

S-2 is specifically responsible for location granularity.

Therefore the experiment should be judged primarily against **Priority 1**, then Priority 3.

On that basis:

### Zero-Step

- stronger anatomical fidelity;
- arbitrary weighted tables;
- 1% resolution;
- preserves authored symmetry more naturally;
- modest mapping complexity.

### Units-Digit

- simpler direct mapping;
- zero additional mapping stage for exactly ten zones;
- coarse 10% resolution;
- cannot represent many plausible anatomical weights;
- can make zones unreachable;
- can manufacture anatomical asymmetry.

That is a poor trade for the default Tier-1 mechanism.

---

# 17. My Recommendation

## Recommendation 1 — Treat Zero-Step as the leading Tier-1 mechanism

I would now move from:

> "Zero-Step and Units-Digit remain equally viable candidates."

to:

> **"Experimental evidence currently favours Zero-Step for Tier 1, subject to one final targeted validation pass."**

I would **not yet lock it**, because the Roadmap's governance process explicitly expects simulation and designer ruling before promotion.

---

## Recommendation 2 — Do not discard Units-Digit

Units-Digit still has a legitimate role.

It may be useful as:

- an optional simplified location mode;
- a cinematic/fast-play mapping;
- a setting-specific table;
- a deliberately coarse location system;
- a special ten-zone table where each zone is exactly 10%.

In other words:

> **Units-Digit appears better suited as a deliberately coarse mapping option than as Tiwas's general-purpose Tier-1 mapping primitive.**

That is a more useful disposition than simply declaring it "failed."

---

# 18. Recommended Final Validation Experiment

Before locking Zero-Step, I recommend **one focused experiment rather than another broad one**.

Use a larger set of deliberately authored location tables.

### Fixture D — Common symmetric combat table

Something like:

```text
Head
Neck
Torso
R Arm
L Arm
R Hand
L Hand
R Leg
L Leg
```

with explicitly symmetric pairs.

### Fixture E — Asymmetric creature

For example:

```text
Head
Neck
Torso
Wing A
Wing B
Tail
R Leg
L Leg
```

where asymmetry is intentional.

### Fixture F — Highly granular table

A 12–20-zone table including:

- face;
- skull;
- neck;
- upper torso;
- lower torso;
- shoulders;
- upper arms;
- forearms;
- hands;
- thighs;
- shins;
- feet.

### Fixture G — Symmetry stress test

Use deliberately identical weights for multiple paired locations and vary table order systematically.

The critical acceptance tests would be:

1. Probability fidelity.
2. Zero unreachable authored zones.
3. Preservation of declared symmetry.
4. Preservation of declared asymmetry.
5. Table-order independence.
6. Mapping-stage count.
7. Implementation complexity.

If Zero-Step passes those, I would consider the evidence sufficient for a designer ruling.

---

# 19. Recommended S-2 Decision State After That Experiment

I recommend the eventual decision record look approximately like this:

```text
S-2 Tier-1 Location Provider
Status: Candidate accepted pending formal designer lock

Preferred mechanism:
Zero-Step

Reason:
The 1–100 location domain provides sufficient resolution to represent
arbitrary weighted anatomical tables while preserving authored
symmetry and avoiding unreachable zones caused by coarse 10-slot
quantisation.

Units-Digit:
Retained as an optional coarse/direct-index mapping method where a
10-zone equal-weight table is deliberately desired.

Tier 0:
Remains available where location information is unnecessary.

Tier 2:
Remains a future higher-granularity anatomical/armor/surgery module.
```

That preserves the architecture already established in the WIP documentation: Tier 0/1/2 are location-granularity mechanisms and must not be confused with Skill Tiers.

---

# 20. Important Documentation Corrections for the Next S-2 Revision

I would carry the following forward from ClaudeAI's report.

### Keep

- Provider signature clarification.
- Location Context abstraction.
- Explicit extension point for Tier 2.
- Explicit distinction between experimental evidence and canonical rule.
- Fixture methodology notes.
- Symmetry finding.
- Fine-grained probability limitation.
- Units-Digit's retained direct-index advantage.

### Add

**Symmetry preservation as an acceptance criterion.**

**Table-order independence as an acceptance criterion.**

**Unreachable-zone detection as an acceptance criterion.**

**Per-zone error as the primary distribution metric.**

### Reword

"Number of mapping operations" should be replaced with something like:

> **Additional mapping stage**

because the current metric is architectural rather than an actual computational-cost benchmark.

---

# 21. Governance Assessment

ClaudeAI has handled the governance correctly.

The report explicitly distinguishes:

- existing S-2 rules;
- experimental methodology;
- newly discovered evidence;
- proposed v1.2 wording;
- unresolved decisions.

That is consistent with the project's explicit rule that detailed experimental material must not become canonical merely because it is documented, and that promotion requires simulation/analysis followed by a designer ruling and canonical-document update.

The Roadmap likewise says implementation support and final rule selection are distinct.

So I would **not merge ClaudeAI's experimental conclusions directly into the Canonical Rules document**.

They belong in the S-2 WIP/review chain until the designer makes the ruling.

---

# 22. Final Verdict

### ClaudeAI's experiment: **Approved as useful experimental evidence**

I find no major mathematical or logical defect in the reported experiment.

The methodological assumptions are explicitly disclosed, which is important.

### Most valuable finding

**Units-Digit's coarse 10-slot domain can silently create anatomically meaningful distortions—including unreachable zones and unintended L/R asymmetry.**

### Most important architectural implication

The choice between Zero-Step and Units-Digit should no longer be framed primarily as:

> "Which formula is simpler?"

It should be framed as:

> **"What probability resolution and anatomical expressiveness does Tier 1 require, and how much mapping complexity are we willing to spend to obtain it?"**

Against Tiwas's current priorities, the evidence strongly favours **Zero-Step**.

### Current S-2 position I recommend

**Do not lock yet.**

Instead:

1. Accept ClaudeAI's experiment as valid evidence.
2. Record **Zero-Step as the leading candidate**.
3. Retain Units-Digit as a possible coarse/specialized mode.
4. Add symmetry and table-order independence to the S-2 acceptance criteria.
5. Run one final multi-table stress test.
6. If Zero-Step passes, make the formal designer ruling.
7. Update S-2 v1.2 and the Roadmap.
8. Only then promote the mechanism into the canonical architecture.

The experiment has therefore **substantially reduced the uncertainty in S-2**. It has not completely closed S-2, but the remaining uncertainty is now much narrower: it is primarily **validation and policy selection**, rather than uncertainty over which mechanism is technically capable of supporting Tiwas's granular-location objective.

In practical terms, I would now regard **Zero-Step as the presumptive Tier-1 mechanism unless the final stress test reveals a previously unidentified architectural problem.**