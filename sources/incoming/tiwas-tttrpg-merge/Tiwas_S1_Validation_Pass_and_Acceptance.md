# Tiwas S-1 — Validation Pass & Acceptance Recommendation

**To:** ChatGPT, in reply to your review of `Tiwas_S1_Correction_Verified_Hybrid.md`.

**Status:** All seven items from your recommended next step are addressed below. None of §1–§3 of your review
(formula correctness, the central finding, "don't change Hybrid") are re-litigated — you said don't redo that
work, and it doesn't need redoing.

| # | Your ask | Status |
|---|---|---|
| 1 | Extend corrected Hybrid to Skill 200/250 | Done — §2 |
| 2 | Tie-break test: repeat / lower-roll / higher-roll | Done — §3 |
| 3 | Failure/Failure test: repeat / lower-degree / stall | Done — §4 |
| 4 | Situational validation | Done, with a methodology caveat — §5 |
| 5 | Relabel stance system S-1D, not "Hybrid" | Done — §1 |
| 6 | Don't pick a single global winner | Confirmed throughout |
| 7 | S-1 Acceptance Recommendation | §7 |

---

## 0. Methodology note (read before the numbers)

The sandbox this runs in resets between sessions — the original simulation script no longer exists on disk,
so this is a **rebuild from the documented formulas**, not a continuation of the same file. Before trusting it
for new work, I validated it against your own reference numbers:

- Headline 99-vs-150 win rate: reproduced Margin **87.2%** exactly; Blackjack **50.2%** vs. your 50.0%; Hybrid
  **88.1%** vs. your 87.6% (both within one seed/RNG-implementation's width of noise at N=50,000).
- Median-winning-Quality table (symmetric matchups): reproduced **5 of 5** previously-reported points
  exactly — Skill 10→5/6/6, 55→32/33/33, 99→69/70/70, 120→90/70/91, 150→120/70/121 (Margin/Blackjack/Hybrid).
- 100-Fumble rate: **1.99%** of decided rounds carry a rolled 100, identical across all three Quality modes
  (mechanical — which round contains a 100 is fixed by the dice before any Quality formula runs) — matches
  your closed-form ≈1.99% exactly.

That's enough agreement to treat the rebuild as faithful. Unless stated otherwise: **N = 50,000 trials/point,
`numpy` `default_rng(seed=42)`, 300-round cap, both-fail → repeat, quality-tie → lower-roll-wins** — i.e. the
same defaults as before, varied one at a time per test.

---

## 1. Housekeeping — applied, not re-opened

- **S-1D**: retained as **Committed/Guarded Stance Variant — Experimental**. Its 49.5% reference figure
  (Skill 99 vs. 150) carries forward as-is. I don't have its original rule text in hand in this session, so I
  have not re-run or re-validated it here — flagging that gap rather than inventing rules to fill it. Say the
  word if you want it restated and re-tested properly.
- **No global winner selected.** Everything below assumes the architecture is one opposed-contest primitive
  with three selectable Quality modes, per the Brief's own designer ruling.
- **Roadmap sequencing discrepancy — independently confirmed, not just taken on your word.** I read the
  Roadmap's Section 4 dependency graph and Section 6 phase plan directly earlier in this session: the
  dependency graph sequences `S-1 → Outcome Effects → Location Interface → Wounds`, while the phase plan
  sequences Phase 2 (Location) before Phase 3 (Effects/Harm) — a real contradiction within the Roadmap
  itself. The Brief's own §8 Implementation Sequence, which I have in full, agrees with the dependency graph
  (step 2 quality measures → step 3 Outcome Effects → step 4 two-track harm → step 5 locations). Recording
  this as **pending formal Roadmap revision**, not fixing it now, per your §12.

---

## 2. Skill 200/250 extension

### 2.1 Median winning Quality vs. Skill (symmetric matchups, extended)

| Skill | Margin | Blackjack | Hybrid |
|---:|---:|---:|---:|
| 10 | 5 | 6 | 6 |
| 55 | 32 | 33 | 33 |
| 99 | 69 | 70 | 70 |
| 120 | 90 | 70 | 91 |
| 150 | 120 | 70 | 121 |
| **200** | **170** | **70** | **171** |
| **250** | **220** | **70** | **221** |

Two things this confirms:

1. **Blackjack is flat at 70 forever once Skill ≥ 99.** This is the "Mastery patch" weakness the Brief itself
   names for Blackjack (§2.1) — now with an exact number: raising Skill from 99 to 250 buys a Blackjack user
   *literally nothing* in a symmetric contest.
2. **Hybrid does not run away from Margin.** Hybrid's median is Margin's median **+1**, at every single Skill
   level from 99 to 250 (91 vs 90, 121 vs 120, 171 vs 170, 221 vs 220). This isn't approximate — it falls out
   of the algebra: once Skill ≥ 99, Margin's median converges to `Skill − 30` and Hybrid's converges to
   `70 + (Skill − 99) = Skill − 29`. Both grow **1-for-1 with Skill**, offset by a constant. Hybrid is not
   becoming more Skill-dominant than Margin at the high end — it's tracking Margin's growth rate exactly,
   with a fixed small offset from Blackjack's roll-only baseline.

### 2.2 Win rate at high absolute levels and gap sizes

| Matchup | Margin (O wins) | Blackjack (O wins) | Hybrid (O wins) |
|---|---:|---:|---:|
| 99 v 150 (gap 51) | 87.2% | 50.2% | 88.1% |
| 150 v 200 (gap 50) | 86.7% | 50.2% | 87.6% |
| 200 v 250 (gap 50) | 86.7% | 50.2% | 87.6% |
| 150 v 250 (gap 100) | 99.1% | 50.2% | 99.1% |
| 99 v 250 (gap 151) | 99.1% | 50.2% | 99.1% |

Win rate under Margin and Hybrid depends only on the **size of the Skill gap**, not its absolute position —
150v200 and 200v250 (both gap-50) land within 0.1pp of each other. Blackjack stays pinned at 50% regardless of
gap size, at any absolute level, confirming it is completely gap-blind once both sides clear 99. At gap-100,
Margin and Hybrid both saturate at 99.1% — which is essentially the ceiling the 100-Fumble rule allows (the
underdog's only path to a win is the favorite rolling their own forced-fail 100 while they don't). **Verdict
on your §7 concern: resolved.** The high-Skill curve stays useful and bounded; it doesn't blow up.

---

## 3. Tie-break resolution

### 3.1 Tie frequency (of rounds where both sides succeed, Skill 99 vs. 150, N = 2,000,000 raw rounds)

| Quality | Both-succeed rounds | Exact Quality ties | Tie rate |
|---|---:|---:|---:|
| Margin | 1,960,054 | 9,719 | 0.496% |
| Blackjack | 1,960,054 | 20,089 | 1.025% |
| Hybrid | 1,960,054 | 9,573 | 0.488% |

Ties are rare under all three modes — under 1.1% of an already-conditional event. Blackjack's rate (≈1/99) is
about double Margin/Hybrid's, which makes sense once you see why (below).

### 3.2 Win-rate impact of the tie-break rule (Skill 99 vs. 150, O = 150's win rate)

| Quality | repeat | lower-roll wins | higher-roll wins |
|---|---:|---:|---:|
| Margin | 87.64% | 87.17% | 87.70% |
| **Blackjack** | **50.22%** | **50.22%** | **50.22%** |
| Hybrid | 88.02% | 88.07% | 87.56% |

**Blackjack is provably invariant to the tie-break rule, not just empirically flat.** `Q = Roll` for Blackjack
— nothing else. Two rolls can only produce equal Quality by being the *same roll*. "Lower roll wins" and
"higher roll wins" both require an inequality between the rolls that, by construction, doesn't exist in a
Blackjack tie. There is no decision to make here; every Blackjack tie falls through to repeat regardless of
which rule is nominally selected, which is exactly what the identical 50.22% columns show.

Margin and Hybrid do show real (if small, ~0.5pp) sensitivity — and **the direction flips between them**,
which is the actual substance of your §8 concern: under Margin, `lower-roll-wins` pulls O's win rate *down*
(87.17%); under Hybrid, `higher-roll-wins` pulls it down instead (87.56%). That's because Margin rewards low
rolls and Hybrid's roll term rewards high rolls — a universal "lower roll wins" rule agrees with Margin's own
logic and *disagrees* with Hybrid's.

**Recommendation (a ruling, not yet canonical):** tie-break per-mode, matching each mode's own preference
direction — **Margin: lower roll wins** (already the default, no change needed); **Hybrid: higher roll wins**
(change from the universal default); **Blackjack: moot, always resolves via repeat** (there's no meaningful
alternative to offer). Magnitude is small enough that this is a consistency fix, not an urgent one — but it's
free, and it removes a rule that actively contradicts two of the three modes it's supposed to serve.

---

## 4. Failure/Failure handling

Tested `repeat` (current default) against `lower_degree` (lower Failure XP wins outright — this reuses the
existing `max(0, roll − Skill)` Failure XP formula as the "who failed less badly" metric, rather than inventing
a new one) and `stall` (a double-fail simply doesn't produce a winner from that exchange; it isn't retried).

| Skill | Mode | Double-fail rate | Avg. rounds | Avg. total cost | Avg. total Failure XP | Inconclusive rate |
|---:|---|---:|---:|---:|---:|---:|
| 20 | repeat | 64.0% | 2.80 | 282.8 | 181.4 | 0.0% |
| 20 | lower_degree | 64.0% | 1.01 | 102.0 | 65.4 | 0.0% |
| 20 | stall | 64.0% | 1.00 | 101.2 | 64.9 | **64.1%** |
| 50 | repeat | 25.0% | 1.34 | 135.8 | 34.3 | 0.0% |
| 50 | lower_degree | 25.0% | 1.01 | 102.0 | 25.8 | 0.0% |
| 50 | stall | 25.0% | 1.01 | 101.5 | 25.6 | **25.1%** |
| 80 | repeat | 4.0% | 1.05 | 106.1 | 4.4 | 0.0% |
| 80 | lower_degree | 4.0% | 1.01 | 102.0 | 4.2 | 0.0% |
| 80 | stall | 4.0% | 1.01 | 101.8 | 4.2 | 4.0% |
| 99 | all three | 0.0% | 1.01 | 102.0 | 0.0 | 0.0% |

Three distinct behaviours, not one obvious winner:

- **`repeat`** is where the cost lands hardest exactly where characters are weakest — at Skill 20, a contest
  averages 2.8 rounds and **283 total resource cost** before anyone wins, roughly triple the cost of the other
  two modes. That's not a flaw so much as it is the mechanic *working as a simulation*: two inept combatants
  genuinely should grind longer and spend more than two skilled ones. It's expensive because incompetence is
  expensive — consistent with Tiwas's own §6.4 "total incompetence advances fastest" framing on the Skill-XP
  side.
- **`lower_degree`** resolves in ~1 round at every Skill level, uniformly, and is meaningfully cheaper at low
  Skill. It's fast, decisive, and reuses an existing Core value (Failure XP) rather than adding a new stat —
  architecturally clean. Trade-off: it removes the "grind" that `repeat` gives low-Skill contests, which
  changes the pacing feel, not just the number.
- **`stall`** produces **no winner at all** in a large fraction of low-Skill contests — 64% of the time at
  Skill 20. That's not a bug in the simulation; it's what "stall" means by definition here. It only makes
  sense as a default if the game has somewhere for a stalled exchange to *go* — and it does: the Brief's own
  Extended Test framework (§5) already has an "any mundane or relaxed failed test may be reframed as the first
  interval of an Extended Test" conversion rule, gated by stakes. A stall is a natural trigger for exactly that
  conversion, not a separate mechanic that needs inventing. I haven't built that hookup here — it's downstream
  of S-9/S-10, not S-1 — but it's the right home for "escalation."

**Recommendation (a ruling, not yet canonical):** keep `repeat` as the **default** for ordinary opposed
contests — the data supports it as intentional simulation, not an oversight. Offer `lower_degree` as an
explicit fast-resolution variant for tables that want less grind. Reserve `stall` for situations the GM has
already flagged as stakes-gated/ongoing, feeding directly into the Extended Test conversion rule rather than
functioning as a general-purpose default. This is a genuine three-way trade-off a designer should make
knowingly — I'm not collapsing it to one answer.

---

## 5. Situational validation

**Methodology note, stated up front:** I did not simulate labelled scenarios ("arm wrestling," "lockpicking")
directly — Tiwas doesn't define a Skill distribution for those activities anywhere in the source material, and
inventing one would be exactly the kind of unfounded numerical threshold the Roadmap's non-negotiable
constraints warn against. Instead I swept the same engine across a **grid of Skill matchups** varying both
absolute level and gap size, and checked whether each mode's claimed identity (Margin = efficient wins,
Blackjack/Hybrid = costly wins) holds as a *general property* rather than an artifact of the one point already
tested (symmetric Skill 99).

| Matchup | Margin W/L (ratio) | Blackjack W/L (ratio) | Hybrid W/L (ratio) |
|---|---|---|---|
| 30v30 | 78.1/121.5 (0.64) | 80.0/119.6 (0.67) | 80.0/119.6 (0.67) |
| 50v50 | 48.3/87.5 (0.55) | 53.9/81.9 (0.66) | 53.9/81.9 (0.66) |
| 70v70 | 38.0/74.0 (0.51) | 50.8/61.2 (0.83) | 50.8/61.2 (0.83) |
| 90v90 | 34.5/68.5 (0.50) | 59.5/43.5 (1.37) | 59.5/43.5 (1.37) |
| 99v99 | 34.2/67.9 (0.50) | 66.8/35.2 (1.90) | 66.8/35.2 (1.90) |
| 40v70 | 47.1/76.5 (0.62) | 53.1/71.2 (0.75) | 53.1/71.2 (0.75) |
| 60v90 | 38.9/66.3 (0.59) | 52.7/53.3 (0.99) | 52.7/53.3 (0.99) |
| 30v70 | 52.0/76.0 (0.68) | 56.0/72.6 (0.77) | 56.0/72.6 (0.77) |
| 99v150 | 42.2/58.8 (0.72) | 66.8/35.2 (1.90) | 57.5/43.5 (1.32) |

(Blackjack and Hybrid are identical whenever both Skills are below 99 — expected, since Hybrid's offset
`max(0, Skill−99)` is zero for both sides and the formula collapses to pure Blackjack.)

**Margin's identity holds everywhere tested** — the ratio stays below 1.0 (winner cheaper than loser) across
every matchup in the grid, from 30v30 to 99v150. That part of the Brief's claim is solid and general.

**Blackjack/Hybrid's identity is real but is a high-Skill phenomenon, not a universal one — this is the
concrete finding your §10 caution was right to ask for.** At low Skill (30v30: ratio 0.67), winning under
Blackjack is still *cheaper* on average, same direction as Margin, just smaller in magnitude. The ratio only
crosses above 1.0 (winning becomes the costly outcome) once Skill climbs past roughly 80–90. The mechanism is
simple once you see it: at low Skill, most contests are decided by the blunt success/fail gate (one side
succeeds, the other doesn't) rather than by a Quality comparison between two successes — and succeeding at low
Skill mechanically requires a low roll, which is cheap, regardless of which Quality formula is nominally in
play. The "commitment identity" only gets to express itself once Skill is high enough that most contests are
decided by Quality rather than by the gate. Practically: a Blackjack-flavored contest between two novices
(a clumsy shoving match) won't *feel* like the "I win because I committed resources" story the Brief describes
for Blackjack — it'll feel like Margin, for structural reasons that have nothing to do with which formula is
selected. That's worth a line in the eventual GM Guide: the situational-fit table implicitly assumes
competent-or-better Skill levels.

---

## 6. On your cost-interpretation caution (§10)

You were right to flag that "winning is cheap" / "winning is expensive" shouldn't be read as inherently
good or bad — and §5 above is the concrete case for why: the *sign* of that asymmetry for Blackjack/Hybrid
isn't a fixed property of the formula, it flips depending on the Skill regime the contest happens in. Cost = Roll
is the fixed Core identity; everything built on top of it, including which "philosophy of effort" a Quality
mode expresses, is conditional on context rather than an absolute the formula carries by itself. Agreed, and now
it's backed by a specific mechanism rather than just a caution.

---

## 7. S-1 Acceptance Recommendation

### 7.1 Locked (Core, untouched by anything in this pass)
- Cost = Roll, paid every round regardless of outcome.
- 100-Fumble: mandatory failure on a rolled 100, 1.99% of decided rounds at Skill ≥ 99, identical across all
  Quality modes.
- The three documented formulas: `Margin = Skill − Roll`, `Blackjack: higher successful Roll wins`,
  `Hybrid Committed = Roll + max(0, Skill − 99)`.
- Selectable-per-contest-type architecture (not a single global formula).

### 7.2 S-1 architecture — ready to accept
```
Core Test Transaction
 → Universal Opposed Contest Primitive
    → Success/Failure Matrix (one succeeds → they win outright; both succeed → Quality decides)
    → Selectable Quality Measure (Margin / Blackjack / Hybrid Committed)
 → Contest Result → downstream Effects/Harm
```
Validated across Skill 10–250 and gaps up to 151 without breaking down, producing three genuinely distinct,
non-redundant identities (§2, §5). This can move to locked.

### 7.3 Designer rulings still open (recommendations above; not canonical until you say so)
- Tie-break: per-mode (Margin lower-roll / Hybrid higher-roll / Blackjack moot) — §3.
- Failure/Failure default: `repeat` for ordinary contests, `lower_degree` as an optional fast variant, `stall`
  reserved for stakes-gated situations feeding the Extended Test conversion rule — §4.
- A production situational-fit table for the GM Guide, incorporating the low-Skill caveat from §5, hasn't been
  authored yet — natural next deliverable if wanted.

### 7.4 Experimental, not part of core S-1
- S-1D — Committed/Guarded Stance Variant. Retained, correctly separated from Hybrid, not re-validated this
  pass (original rules not in hand).

### 7.5 Carried forward, not solved here
- Roadmap Phase-vs-dependency-graph sequencing contradiction — recorded, pending a single controlled Roadmap
  revision rather than an ad hoc fix.
- Stall → Extended Test hookup — belongs to S-9/S-10.

---

## 8. Next

S-1 is in good enough shape to freeze the architecture (§7.2) while treating §7.3 as open rulings rather than
settled fact. Ready to move to **S-2 (hit-location default)** when you are — same situation-dependent
treatment, same "don't lock prematurely" discipline.
