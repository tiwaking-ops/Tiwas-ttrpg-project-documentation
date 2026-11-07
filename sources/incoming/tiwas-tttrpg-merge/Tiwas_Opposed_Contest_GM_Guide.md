# Tiwas — Opposed Contest: Situational Selection Guide (for GM or LLM)

**Status:** Reference / operational guidance, not a design document. Margin, Blackjack, and Hybrid
Committed are all permanently part of Tiwas — per Roadmap Phase 1's own Objective, *"create one contest
primitive that supports all three candidate quality measures without selecting one globally,"* and its
"Configurable situation flag" deliverable. This document **is** that configuration guidance.

---

## 1. Quick Reference

| Stakes | Both participants < Skill 99 | At least one participant ≥ Skill 99 |
|---|---|---|
| **Routine** — story barely changes either way | **Margin** | **Margin** |
| **Significant** — matters, not the climax | **Margin** (default) — Blackjack for cost/risk flavor | **Blackjack** — keeps tension alive between experts |
| **Climactic** — the dramatic set-piece | **Hybrid Committed** (adds tactical drama) — Margin if speed matters more | **Hybrid Committed** — tactical choice at the exact point Skill alone stops deciding it; Blackjack for the same tension without the extra step |

**One-line rule:** Routine → Margin, always. Non-routine and both under Skill 99 → Margin, upgrade only
for flavor. Non-routine and at least one side ≥ Skill 99 → actively choose.

**Formula cheat-sheet:**

| System | Quality (on success) | Range at Skill S | Extra procedure |
|---|---|---|---|
| Margin | `Skill − Roll` | 0 to S−1, uncapped as S grows | None |
| Blackjack | `Roll` | 1 to `min(S, 99)` — capped once S ≥ 99 | None |
| Hybrid Committed | `Roll` if Committed / `Skill − Roll` if Guarded | Player's choice, declared pre-roll | Declare stance before rolling; a failed Committed roll in an Inconclusive round forces Guarded next round |

*(This heuristic pairs with, but doesn't replace, the still-reserved Difficulty/Task-Adjudication and
GM-Procedure subsystems — see §7.)*

---

## 2. Why These Two Axes

### 2.1 Skill 99 — mechanically real, not a house rule

At Skill ≥ 99, a roll only fails on a 100 (the mandatory Fumble) — every roll 1–99 succeeds no matter how
far past 99 Skill climbs. Consequence:

- **Margin** (`Skill − Roll`) keeps climbing linearly as Skill rises past 99 — Skill is unbounded, Roll
  is still just 1–99.
- **Blackjack** (`Roll`) is capped at `min(Skill, 99) = 99` once Skill ≥ 99 — a Skill-99 character and a
  Skill-150 character draw Quality from the *identical* 1–99 range.

Simulated consequence (50,000 trials, Skill 99 vs. Skill 150 — a 51-point gap): Margin gives the
Skill-150 side an **87.0%** win rate. Blackjack gives it **49.4%** — a coin flip. Hybrid Committed (which
defaults to Blackjack-scoring) gives **49.0%**. Full data: `Tiwas_S1_Opposed_Contest_Candidates.md` §7.

This is the one claim in this document that isn't a judgment call — it's the 100-Fumble rule plus
arithmetic, confirmed by simulation.

### 2.2 Stakes — a GM heuristic, not a Tiwas subsystem

Everything else in this document is a proposal for organizing that mechanical fact into usable guidance
— not locked Tiwas text. "Routine / Significant / Climactic" is a judgment call about a specific contest,
not a numeric modifier system, and it does not resolve Core Rules v2 §9's reserved Difficulty/Task-
Adjudication or GM-Procedure scope. Treat it as a starting heuristic, replace it with your own if a
better one emerges from play.

---

## 3. Full Decision Procedure

1. **Is this contest Routine** — would the story barely change regardless of who wins? → **Margin.**
   Stop; the nuance below isn't worth table time on a contest this minor.
2. **Not routine. Are both participants under Skill 99?** → The three systems are statistically
   indistinguishable at this band (§2.1). Default **Margin** for speed. Switch to **Blackjack** if you
   want the roll-cost/quality tension for flavor this scene, or **Hybrid Committed** if it's climactic
   and you want a real pre-roll choice from the player.
3. **Not routine. Is at least one participant Skill ≥ 99?** — the choice now actually changes the odds:
   - Want raw mastery to keep deciding the outcome, even between two highly advanced characters? →
     **Margin.**
   - Want the outcome to stay genuinely uncertain once both sides are "reliable," so the result feels
     earned rather than predetermined? → **Blackjack.**
   - Is this the climax, and should the acting side make a bold-vs-careful choice as part of the drama? →
     **Hybrid Committed.**

---

## 4. Per-System Field Notes

### 4.1 Margin
**Feels like:** the core resolution, extended — rolling well under your Skill already feels good; Margin
makes that matter for Quality too. Nothing new to teach.
**Shines:** routine and significant contests below Skill 99; any scene where the more skilled side should
reliably matter.
**Mismatched:** never overkill (simplest option) — but at Skill ≥ 99 climactic moments, a large Skill gap
can make the outcome feel predetermined, which may undercut the drama you wanted.
**Worked example:** Skill 60 vs. Skill 45; rolls 40 and 30 — both succeed. Quality: `60−40=20` vs.
`45−30=15`. The Skill-60 side wins despite rolling numerically *higher* than the other side — Margin
compares performance against your own Skill, not the raw roll.

### 4.2 Blackjack
**Feels like:** risk-taking. Rolling high and still succeeding pays off in Quality — and costs more,
since Cost = Roll always applies. Good where "going for it" should visibly cost something.
**Shines:** significant-to-climactic contests once both sides clear Skill 99, where the drama needs to
stay alive; a fine flavor pick at any Skill level if you want risk/cost tension without the full Hybrid
procedure.
**Mismatched:** adds no real value below Skill 99 beyond flavor — statistically equivalent to Margin
there (§2.1). Don't reach for it out of habit.
**Worked example:** Skill 99 vs. Skill 150; rolls 40 and 85 — both succeed. Quality: 40 vs. 85 — the
Skill-150 side wins, but their 51-point Skill advantage bought nothing extra: a Skill-99 character
rolling 85 (still ≤ 99) would have generated the identical Quality.

### 4.3 Hybrid Committed
**Feels like:** a tactical pre-roll decision — Guarded plays it safe (Margin-scored), Committed goes for
broke (Blackjack-scored); a failed gamble that doesn't lose outright forces caution next round.
**Shines:** the single climactic contest of a scene — a duel, a decisive confrontation — where the extra
step (declare a stance) is worth the drama it buys.
**Mismatched:** routine or most significant contests — the declaration step is real table overhead, and
under an always-Committed policy it behaves statistically like plain Blackjack anyway (§9 of the
Candidate Comparison doc); its distinct value is the choice itself, not a different outcome distribution.
**Worked example:** Declares Committed, Skill 70, rolls 72 → fails. If the opponent also fails this round
(Inconclusive), this character must declare Guarded next round.

---

## 5. Consistency Rules for Switching

- **Between contests:** switch freely, scene to scene — this is exactly what "Configurable situation
  flag" means. No consistency penalty for varying it.
- **Within a single contest:** once chosen, a system holds for that contest's full duration, including
  every round if it repeats via the Inconclusive rule. **This is this document's own ruling, not sourced
  from the roadmap** — the shared Opposed Contest Primitive assumes one active Quality function per
  round, and switching mid-contest was never specified. Flagging it as a guess, not a locked fact.

---

## 6. If You're an LLM Running This

Apply in order, stop at the first match:

```
IF contest_stakes == "routine":
    USE Margin
ELIF skill_A < 99 AND skill_O < 99:
    USE Margin   # statistically equivalent; override only on explicit request for flavor
ELIF contest_stakes == "climactic":
    USE Hybrid Committed   # default; Blackjack if less procedure is wanted
ELSE:  # significant, and at least one skill >= 99
    USE Blackjack
```

Do not switch the active system mid-contest once rolling has started (§5). Do not infer a `stakes` value
silently — if fictional stakes aren't clear from context, ask, or default to `"significant"` rather than
guessing `"climactic"`.

---

## 7. Scope & Relationship to Reserved Subsystems

| This document does | This document does not do |
|---|---|
| Help choose among the three already-defined S-1 Quality measures, per contest | Define difficulty modifiers or task adjudication (Core Rules v2 §9 — still reserved) |
| Cite the Skill-99 threshold as an empirical, simulation-confirmed fact | Introduce any new numeric threshold beyond Skill 99, which was already established, not invented here |
| Propose a qualitative Stakes heuristic for this narrow purpose | Lock that heuristic as a general Tiwas subsystem, or resolve GM Procedure (Core Rules v2 §9 — still reserved) |
| Stand alone for at-the-table or LLM-runtime use | Require cross-referencing another file mid-session |

---

## Appendix: Source

Formulas, full derivation, and simulation methodology: `Tiwas_S1_Opposed_Contest_Candidates.md` and
`Tiwas_S1_Simulation.py` (prior working session). Every empirical claim in §2.1 traces to that
simulation; nothing here re-derives it independently.
