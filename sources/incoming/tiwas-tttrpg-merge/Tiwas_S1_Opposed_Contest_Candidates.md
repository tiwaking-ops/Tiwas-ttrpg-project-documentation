# Tiwas — S-1: Universal Opposed Contest Primitive (Candidate Comparison)

**Status:** OPEN. None of the three candidates below is canonical. Per Roadmap §9 Constraint 1 and §6
Phase 1: *"Do not lock S-1 before this comparison."* This document formalizes all three candidates from
scratch (their names and general intent are the only things that survived from the source "Comparative
Design Direction Brief," which is not accessible) and reports results from an actual, runnable
simulation. The lock decision is reserved for the designer.

---

## 0. Scope and Assumptions

| # | Assumption | Reason |
|---|---|---|
| 1 | Skill is held fixed for the duration of one simulated contest (no mid-contest Skill Roll Pool growth modeled). | Isolates the quality-measure choice from advancement dynamics. A full Phase 13 integration pass should re-test with live advancement. |
| 2 | "PE/MP expenditure" is reported as gross cumulative natural-roll cost paid per side, not netted against pool size or Regen. | Pool max and Regen are functions of an attribute array, which is outside S-1's scope — S-1 defines the contest, not a character. |
| 3 | Skill = 0 is excluded from the simulated bands. | At fixed Skill 0, success is impossible (`roll ≤ 0` never holds), so a non-advancing contest would never resolve. Core §6.4's free bump off Skill 0 is exactly what prevents this in real play; it's disabled here by Assumption 1. |
| 4 | Simulation: `numpy` RNG, seed 42, 30,000–50,000 trials per data point, capped at 300 rounds/contest (0 unresolved trials observed anywhere in this run). | Reproducibility; see companion script. |
| 5 | Skill bands tested: 10, 25, 40, 55, 70, 85, 99, 120, 150 (symmetric); six representative mismatches (asymmetric). | Spans low/mid/at-cap/above-cap per the Roadmap's explicit request to test Skill > 99. |

---

## 1. Universal Opposed Contest Primitive (shared procedure — not itself a candidate)

This procedure is common to all three candidates. Only the **Quality function** (§2–§4) differs between
them.

**Inputs:** Actor A (Skill_A) vs. Opponent O (Skill_O), one skill per side, either Body- or Mind-rooted
independently.

**Per round:**

1. Both sides roll 1d100 independently: `Roll_A`, `Roll_O`.
2. Each side resolves its **own** roll through the unmodified Core Test Transaction (Core Rules v2 §5),
   independently: success iff `Roll ≤ Skill` and `Roll ≠ 100`; pay Cost = Roll from the correct pool;
   Overflow → HP if insufficient; if failure, compute Failure XP = `max(0, Roll − Skill)` and check for a
   qualifying failed Double → Advanced Skill creation; Recovery last. **Nothing here is new** — it is the
   existing per-character procedure invoked twice, unmodified.
3. Determine the round outcome from `(outcome_A, outcome_O)`:

| Combination | Result |
|---|---|
| Success vs. Failure | Succeeding side wins the contest. Decisive. |
| Success vs. Success | Compute Quality for each side (§2–§4). Higher Quality wins. Tie in Quality → lower raw Roll wins (a lower roll is never a worse success under Tiwas's core resolution). Decisive. |
| Failure vs. Failure | Inconclusive. Both sides already fully resolved their own Failure XP / Doubles / Recovery this round. **Contest repeats**: both roll again next round. |

4. Duration = number of rounds until a decisive result.

**Compliance with Roadmap §6 Phase 1 acceptance criteria:**

| Criterion | How this procedure satisfies it |
|---|---|
| Both rolls retain natural die-face costs | Step 2 runs the unmodified Core transaction for both sides, every round |
| Failure XP independently generated | Step 2, per side, unconditionally |
| Failed Doubles remain eligible for Advanced Skill creation | Step 2, per side, unconditionally |
| 100 remains a mandatory failure | Step 2 uses the unmodified success test |
| Quality does not modify the historical die face | Quality is computed *from* `Roll`/`Skill`, never written back to them |
| No second resource cost from the contest layer | Only Step 2's natural Cost = Roll is ever paid; the contest layer adds nothing |

---

## 2. Candidate A — Margin

**Quality (on success):**
```
Q_margin = Skill − Roll
```
Range on success: `0` to `Skill − 1` (uncapped as Skill grows — see §7 finding).

**Worked example:** Skill 60, Roll 45 (success, since 45 ≤ 60) → `Q = 60 − 45 = 15`.

**Both-fail tie-break:** not applicable — both-fail is always inconclusive (§1), not scored.

---

## 3. Candidate B — Blackjack

**Quality (on success):**
```
Q_blackjack = Roll
```
Rewards rolling as close to the Skill ceiling as possible without busting — and, because Cost = Roll is
immutable Core law, a high-quality Blackjack success is inherently the more expensive one. The risk/reward
is: chase quality, pay more.

**Worked example:** Skill 60, Roll 45 (success) → `Q = 45`. Skill 60, Roll 58 (success, more expensive at
58 PE/MP) → `Q = 58` (higher quality).

**Structural note:** since success requires `Roll ≤ Skill` **and** `Roll ≠ 100`, the maximum achievable
quality is `min(Skill, 99)`. Once Skill ≥ 99, Quality is capped at 99 regardless of how much higher Skill
climbs. This is not a simulation artifact — it falls directly out of the 100-Fumble invariant (§1 Core
Rules v2) applied to this formula. See §7.

---

## 4. Candidate C — Hybrid Committed

Before rolling, the acting side declares a **Stance**:

- **Guarded** — scored as Margin (§2) on success.
- **Committed** — scored as Blackjack (§3) on success.

**Commitment consequence (the only new rule Hybrid adds):** if a **Committed** roll fails *and* the round
is Inconclusive (both sides failed), that side is compelled to declare **Guarded** on the immediately
following round. No numeric penalty is invented (Roadmap §9 Constraint 3 forbids that); the consequence is
purely procedural and costs no extra resource (satisfies "no second resource cost," §1).

Default stance in this simulation: **always Committed unless mechanically forced Guarded** — the
aggressive-by-default policy, since "always Guarded" degenerates to plain Margin and isn't a distinct
candidate worth testing.

**Worked example:** Declare Committed. Skill 60, Roll 45 → success, `Q = 45` (Blackjack-scored). Had the
roll instead been 65 → failure; if the opponent also fails this round (Inconclusive), this side must
declare Guarded next round.

---

## 5. Simulation Methodology

Companion script: `Tiwas_S1_Simulation.py` (two files: the reusable simulator and the full-battery
runner). `numpy`-vectorized, RNG seed 42. Sanity check before the full run: symmetric Skill 55 vs. 55,
5,000 trials, all three candidates landed at 50.2–50.6% win rate for the first side (expected ≈50%, no
structural bias) with **zero** unresolved contests and **zero** unscored decisive rounds. Mean rounds at
Skill 55 (1.253–1.257) matches the closed-form prediction `1 / (1 − 0.45²) = 1.254` exactly, confirming
the round-repeat logic is implemented correctly before trusting the larger run.

Full run: 50,000 trials per symmetric skill/candidate combination (27 combinations), 50,000 per
asymmetric pair/candidate (18 combinations), 50,000 per high-skill Fumble-impact combination (9
combinations).

---

## 6. Results — Symmetric Matchups (Skill_A = Skill_O)

### 6.1 Margin

| Skill | Win% A | Mean Rounds | Mean Cost/side | Quality p10 | p50 | p90 | Fumble-anywhere rate |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 50.1% | 5.27 | 265.9 | 1 | 5 | 9 | 9.5% |
| 25 | 50.2% | 2.29 | 115.5 | 2 | 13 | 22 | 4.3% |
| 40 | 50.1% | 1.56 | 78.7 | 5 | 22 | 36 | 3.1% |
| 55 | 50.4% | 1.25 | 63.1 | 8 | 32 | 50 | 2.5% |
| 70 | 50.4% | 1.10 | 55.5 | 12 | 43 | 65 | 2.2% |
| 85 | 50.8% | 1.02 | 51.5 | 19 | 56 | 80 | 2.0% |
| 99 | 50.4% | 1.00 | 50.5 | 30 | 69 | 93 | 2.0% |
| 120 | 50.4% | 1.00 | 50.3 | 52 | 90 | 114 | 2.0% |
| 150 | 50.6% | 1.00 | 50.5 | 81 | 120 | 144 | 2.1% |

### 6.2 Blackjack

| Skill | Win% A | Mean Rounds | Mean Cost/side | Quality p10 | p50 | p90 | Fumble-anywhere rate |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 49.9% | 5.27 | 267.0 | 2 | 6 | 10 | 9.6% |
| 25 | 50.3% | 2.29 | 115.6 | 3 | 14 | 23 | 4.4% |
| 40 | 50.0% | 1.57 | 79.3 | 6 | 23 | 37 | 3.0% |
| 55 | 50.5% | 1.25 | 63.1 | 9 | 33 | 51 | 2.6% |
| 70 | 50.5% | 1.10 | 55.5 | 13 | 44 | 66 | 2.1% |
| 85 | 50.6% | 1.02 | 51.9 | 21 | 57 | 81 | 2.1% |
| **99** | 50.9% | 1.00 | 50.6 | 31 | **70** | 94 | 1.9% |
| **120** | 50.1% | 1.00 | 50.5 | 31 | **70** | 94 | 2.0% |
| **150** | 50.5% | 1.00 | 50.6 | 31 | **70** | 94 | 2.1% |

### 6.3 Hybrid Committed

| Skill | Win% A | Mean Rounds | Mean Cost/side | Quality p10 | p50 | p90 | Fumble-anywhere rate |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 50.0% | 5.27 | 266.0 | 1 | 5 | 9 | 9.7% |
| 25 | 50.3% | 2.28 | 115.2 | 3 | 14 | 23 | 4.4% |
| 40 | 50.5% | 1.56 | 79.0 | 5 | 23 | 37 | 3.1% |
| 55 | 50.3% | 1.26 | 63.5 | 8 | 33 | 51 | 2.3% |
| 70 | 50.4% | 1.10 | 55.6 | 13 | 44 | 66 | 2.2% |
| 85 | 50.4% | 1.02 | 51.8 | 20 | 57 | 80 | 2.0% |
| **99** | 50.3% | 1.00 | 50.5 | 31 | **70** | 94 | 2.0% |
| **120** | 50.8% | 1.00 | 50.7 | 31 | **70** | 94 | 2.2% |
| **150** | 50.4% | 1.00 | 50.5 | 31 | **70** | 94 | 2.0% |

### 6.4 Headline comparison — median winning Quality by Skill

| Skill | Margin | Blackjack | Hybrid |
|---:|---:|---:|---:|
| 10 | 5 | 6 | 5 |
| 55 | 32 | 33 | 33 |
| 99 | 69 | 70 | 70 |
| **120** | **90** | **70** | **70** |
| **150** | **120** | **70** | **70** |

![Median winning Quality vs Skill](quality_vs_skill.png)

All three candidates track each other closely below Skill 99. Above it, Margin keeps climbing linearly
with Skill while Blackjack and Hybrid flatline at 70 — the direct, exact consequence of the `min(Skill,
99)` ceiling identified analytically in §3.

---

## 7. Results — Asymmetric Matchups (win probability of the higher-Skill side, O)

| Skill A | Skill O | Margin | Blackjack | Hybrid |
|---:|---:|---:|---:|---:|
| 40 | 70 | 75.3% | 75.6% | 75.2% |
| 25 | 99 | 96.5% | 96.6% | 96.6% |
| 70 | 99 | 74.3% | 74.2% | 74.6% |
| 70 | 150 | 97.4% | 74.1% | 74.2% |
| 40 | 150 | 99.6% | 91.2% | 91.3% |
| **99** | **150** | **87.0%** | **49.4%** | **49.0%** |

**This is the load-bearing finding.** At Skill 99 vs. Skill 150 — a 51-point Skill gap — Margin still gives
the higher-Skill side an 87% win rate, consistent with a huge advantage. Under Blackjack and Hybrid, that
same 51-point gap produces a **statistical coin flip** (49.0–49.4%, within Monte Carlo noise of 50%).

The mechanism: once both sides clear Skill 99, both succeed 99% of the time regardless of exactly how
far past 99 they are (only a rolled 100 fails), so the round is decided almost entirely by the
Quality tie-break. Under Blackjack, both sides' Quality on success is capped at `min(Skill, 99) = 99` —
**identical ranges for both sides** — so the tie-break degenerates to "who rolled closer to 99 this
round," independent of the underlying Skill gap. Under Margin, Quality keeps scaling with Skill, so the
gap keeps mattering.

Whether that's desirable is a designer call, not a bug — see §9.

---

## 8. Results — 100-Fumble Impact at High Skill

Fraction of **decisive** rounds in which a rolled 100 appeared on at least one side:

| Skill | Margin | Blackjack | Hybrid |
|---:|---:|---:|---:|
| 99 | 1.89% | 1.92% | 1.98% |
| 120 | 1.93% | 2.00% | 2.00% |
| 150 | 2.09% | 1.95% | 2.05% |

Closed-form check: at Skill ≥ 99, each side fails only on a rolled 100 (p = 0.01). `P(at least one 100 |
round is decisive) ≈ 1 − 0.99 × 0.99 = 1.99%`, since `P(decisive)` is itself ≈ 0.9999 at these Skill
levels (matches Mean Rounds = 1.00 in §6). All nine simulated values land within noise of 1.99%,
independent of candidate — confirming the 100-Fumble rule's frequency is untouched by the choice of
Quality measure, as required by §1's compliance table.

---

## 9. Findings (decision support — not a ruling)

- **Below Skill 99, the three candidates are nearly indistinguishable** on every axis measured — win
  probability, rounds, cost, and quality all track within simulation noise. The candidate choice mostly
  doesn't matter for ordinary-competence characters.
- **Above Skill 99, Margin and Blackjack diverge sharply.** Margin preserves Skill advantage indefinitely
  as characters advance past 100. Blackjack (and Hybrid, which defaults to Blackjack-scoring) caps
  Quality at 99, which **erases high-Skill advantage entirely** in Skill-vs-Skill contests once both
  parties clear that line (§7).
- **Resource cost (PE/MP expenditure) is materially set by contest duration, not by the candidate.** All
  three show the same cost curve at a given Skill (§6) — duration is governed by success/fail odds
  (identical across candidates, since it depends only on Skill, not Quality), not by which side wins a
  both-succeed tie-break.
- **The 100-Fumble rule's frequency of deciding an outcome is candidate-independent** (§8) — confirms the
  contest layer doesn't accidentally interact with or dampen/amplify the Core invariant.
- **Hybrid Committed behaves almost identically to pure Blackjack** under an always-Committed policy,
  because the forced-Guarded consequence only ever fires after a Committed failure in an Inconclusive
  round — a narrow trigger. Its distinct value is a per-roll strategic choice for players, not a
  distinct statistical profile at the table level; that tactical-choice value isn't something this
  aggregate simulation can measure and would need a different (player-decision-modeling) test.

---

## 10. Open Questions for Designer Ruling

These are exactly the kind of forks Roadmap §9 Constraint 4 reserves for an explicit ruling — none are
resolved by this document:

1. Is Margin's **unbounded** high-Skill scaling the intended long-term power curve, or does the system
   want the Blackjack/Hybrid **ceiling-at-99** behavior — where raw Skill stops mattering in
   Skill-vs-Skill contests once both sides are reliable?
2. If the ceiling is undesired, should Blackjack's formula be revised (e.g., quality relative to
   Skill rather than an absolute roll) rather than discarding the candidate outright?
3. Is Hybrid Committed's added procedural complexity (stance declaration, one forced-Guarded rule)
   justified given it statistically resembles Blackjack under the tested policy? A different Stance
   policy (e.g., threshold-based: Committed only when Skill − likely-Roll margin is comfortable) might
   produce a more distinct profile and is not yet tested.
4. The both-fail tie-break (lower raw Roll wins) and the both-succeed exact-tie rule (lower raw Roll
   wins, negligible-probability convention) are this document's inventions, consistent with existing
   Core logic but not sourced from any prior Tiwas text — these need explicit sign-off, not just
   simulation.

---

## Appendix: Reproducing These Results

Companion files: `Tiwas_S1_Simulation.py` (simulator + full battery) and `quality_vs_skill.png` (Fig. 1).
Run with `python3 Tiwas_S1_Simulation.py` — completes in well under a minute; all tables above were
generated directly from its output, not hand-estimated.
