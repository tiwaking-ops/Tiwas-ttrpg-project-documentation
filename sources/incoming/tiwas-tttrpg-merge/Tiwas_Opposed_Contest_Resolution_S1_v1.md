# Tiwas — Opposed Contest Resolution (S-1, v1)

**Status:** First canonical version of this subsystem. Core Rules v2 §9 lists "Opposed tests / contested
rolls" as Reserved / Not Yet Defined — this document closes that gap. It does not modify Core Rules v2;
every rule below builds on the existing Test Resolution Procedure (Core Rules v2 §5) unchanged. Validated
by simulation (N = 50,000 trials/point unless noted, `numpy` `default_rng(seed=42)`, 300-round cap) across
Skill 10–250 and gaps up to 151; see `Tiwas_S1_Validation_Pass_and_Acceptance.md` for full results and
methodology. Sections D and G distinguish empirically-tested claims from designer rulings and from
by-construction guarantees — do not treat them as equally certain.

---

## A. Relationship to Core Rules v2

Each participant's roll in an opposed contest is an **ordinary, unmodified Core Test Transaction**
(Core Rules v2 §5) — same Cost = roll, same 100-Fumble, same Failure XP formula, same Double-eligibility,
same Recovery. The contest layer only adds a *comparison* on top of two independently-resolved tests. It
introduces no second resource pool and never alters the historical die value used by Cost, Failure XP, or
Advanced Skill triggers.

## B. The Universal Opposed Contest Procedure

Both participants (A and O) roll simultaneously against their own relevant Skill, following Core Rules v2
§5 steps 1–4 independently and in full (each pays Cost = their own roll; each generates Failure XP on a
failure; a qualifying failed Double is eligible for Advanced Skill creation exactly as in any solo test).
Then:

| A's result | O's result | Outcome |
|---|---|---|
| Success | Failure | A wins |
| Failure | Success | O wins |
| Success | Success | Compare Quality (§C) — higher Quality wins |
| Failure | Failure | Repeat (§D.2) |

Recovery (Core Rules v2 §5 step 6) applies to both sides after every round, exactly as in any other test.

```
     Core Test A          Core Test B
   (Core Rules §5)       (Core Rules §5)
          │                    │
          └─────────┬──────────┘
                     │
              Outcome Matrix
          ┌──────┬───────┬──────┐
      Succ/Fail  Succ/Succ  Fail/Fail
          │          │          │
   Non-failing    Compare     Repeat
    side wins     Quality    (§D.2)
                     │
              higher Quality
                   wins
                     │
              exact tie → Repeat (§D.1)
```

## C. Quality Measures (selectable per contest)

| Mode | Formula | Rewards |
|---|---|---|
| Margin | `Q = Skill − Roll` | Efficiency — a lower roll among successes scores higher |
| Blackjack | `Q = Roll` | Commitment — a higher roll among successes scores higher |
| Hybrid Committed | `Q = Roll + max(0, Skill − 99)` | Commitment, plus unbounded reward for Skill above 99 |

All three preserve Cost = Roll and the 100-Fumble rule; the Quality formula only ranks successes against
each other, it never changes what was rolled, paid, or fumbled.

## D. Designer Rulings (canonical for this version — explicitly rulings, not derived facts)

### D.1 Exact Quality tie
**Ruling: repeat the contest.** Both sides roll again as a fresh round (new Cost, new Failure XP
exposure, new Double eligibility) rather than resolving via a secondary criterion.

This was a genuine two-way call, not a forced one — a per-mode deterministic tiebreak (lower roll for
Margin, higher roll for Hybrid) is equally mathematically sound and was the original candidate. It's
being set aside in favor of "repeat" because the numeric stakes are negligible (the two approaches differ
by under 0.5 percentage points in overall win rate, in an event affecting under 1.1% of an already
conditional subset of rounds — see validation doc §3) and "repeat" is the simpler rule to teach and
remember: one universal fallback instead of three mode-specific sub-cases, one of which (Blackjack) never
actually fires, since a Blackjack tie is provably always an identical-roll event (`Q = Roll`, so
`Q_A = Q_O` requires `Roll_A = Roll_O`) and has no "lower/higher" distinction to apply in the first place.

### D.2 Failure/Failure
**Ruling: repeat.** Both sides pay Cost, generate Failure XP, and remain eligible for Advanced Skill
creation on that round; then both roll again.

This is intentional, not a default nobody examined: at low Skill, `repeat` measurably makes contests
between weak combatants take longer and cost more (validation doc §4 — Skill 20 symmetric averages 2.8
rounds and 283 total resource cost under `repeat`, versus ~1 round and ~102 cost under the alternatives
tested). That's the simulation-grade identity working as intended — two inept combatants should grind
longer than two skilled ones, consistent with Core Rules v2 §6.4's "total incompetence advances fastest"
framing.

**Not part of the canonical rule, but tested and worth keeping on record for GMs who want them:**
- A *lower-degree-of-failure-wins* variant (reuses the existing Failure XP formula as the tiebreak metric)
  resolves in ~1 round at any Skill level and is meaningfully cheaper at low Skill — a valid option for
  tables that want less grind.
- A *stall* variant (a double-fail produces no winner at all, rather than repeating) produces a large
  fraction of genuinely unresolved contests at low Skill — 64% at Skill 20. It only makes sense paired
  with somewhere for that outcome to go; the natural landing spot is the Extended Test conversion rule
  already defined in the Comparative Design Direction Brief §5 ("any mundane or relaxed failed test may be
  reframed as the first interval of an Extended Test... subject to the stakes-gate principle"), not a
  general-purpose default. That hookup is S-9/S-10 scope, not S-1, and isn't built here.

## E. Selecting a Quality Measure

| Contest nature | Default Quality | Caveat |
|---|---|---|
| Precision / efficiency (shooting, lockpicking, stealth, research) | Margin | Identity holds across the full tested range (Skill 10–150+) — no caveat needed |
| Force / commitment (arm wrestling, shoving, grappling) | Blackjack | **Only reliable once both sides are roughly Skill 80+.** Below that, most rounds are decided by the success/fail gate rather than by Quality, and a Blackjack contest between two low-Skill characters won't feel like "commitment wins" — it'll feel indistinguishable from Margin, because the roll needed to succeed at low Skill is inherently low-cost regardless of which formula is nominally selected |
| Mixed / uncertain | Hybrid | Same Skill-gating as Blackjack — Hybrid is mathematically identical to Blackjack whenever both sides are below Skill 99 |

**Secondary consideration:** Skill level determines how much the Quality choice matters at all, not just
which flavor it produces. At low Skill, the success/fail gate dominates and Quality selection is close to
cosmetic; at high Skill (most rounds decided by both sides succeeding), Quality selection is doing real
work. GMs picking a mode for a low-Skill scene shouldn't expect much distinct flavor from the choice.

The GM retains override authority where fiction demands a different mode than this table suggests.

## F. Validated Properties (empirical — see validation doc for full tables and methodology)

- Blackjack provides **zero** benefit above Skill 99 in a symmetric contest — median winning Quality is
  flat at 70 from Skill 99 through Skill 250. This is the "Mastery patch" weakness the Comparative Design
  Direction Brief already named for Blackjack, now with an exact figure.
- Hybrid does not run away from Margin at high Skill. Both grow 1-for-1 with Skill once Skill ≥ 99; Hybrid's
  median winning Quality tracks Margin's, offset by a constant, at every tested point from 99 to 250.
- Margin and Hybrid win rate depends on the *size* of the Skill gap, not its absolute position — a 50-point
  gap produces the same win rate whether it's 150-vs-200 or 200-vs-250. At a 100-point gap, both saturate
  near 99%, essentially the ceiling the 100-Fumble rule allows.
- The 100-Fumble rate (1.99% of decided rounds, at Skill ≥ 99) is identical across all three Quality
  modes — mechanically guaranteed, since which round contains a rolled 100 is fixed before any Quality
  formula runs.
- Margin's "winning is cheap" identity holds across every matchup tested, from Skill 30 symmetric through
  Skill 99-vs-150. Blackjack/Hybrid's "winning is costly" identity is real but Skill-gated (see §E).

## G. By Construction (not separately instrumented, but guaranteed by the engine's structure)

- Failed Doubles remain eligible for Advanced Skill creation during a contest, exactly as in a solo test —
  each side's roll is processed as a full, unmodified Core Test Transaction; nothing in the contest layer
  suppresses or alters Double-eligibility.
- No second contest-layer resource pool exists — cost is only ever the accumulated natural rolls.
- The historical die roll is never modified by any Quality formula — Quality only ranks rolls that already
  happened.

## H. Experimental — not part of canonical S-1

**S-1D, Committed/Guarded Stance Variant.** An earlier invented tactical-commitment mechanic, distinct from
Hybrid Committed despite the name collision that originally caused it to be conflated with Hybrid. Reference
figure only (49.5% win rate, Skill 99 vs. 150) — not re-validated in this pass, since its rule text isn't
in hand this session. Kept clearly separated so it cannot contaminate canonical S-1. Candidate for a future
tactical-overlay module, not required by anything above.

## I. Acceptance Status

| Element | Status |
|---|---|
| Universal Opposed Contest Primitive (§A, §B) | **Accepted** |
| Three Quality formulas (§C) | **Accepted**, formulas locked |
| Exact-tie handling (§D.1) | **Ruling recorded**, recommended above, open to override |
| Failure/Failure handling (§D.2) | **Ruling recorded**, recommended above, open to override |
| Situational selection guidance (§E) | **Accepted** with Skill-gating caveat attached |
| Empirical findings (§F) | Validated, Skill 10–250, gaps to 151 |
| S-1D stance variant (§H) | **Experimental**, excluded from core |

**Next:** S-2, Hit-location default policy — same situation-dependent treatment, same "don't lock
prematurely" discipline that served S-1 well.
