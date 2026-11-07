# Tiwas S-1: Correction — the Documented Hybrid Formula Is Real

**To:** ChatGPT, follow-up to `Tiwas_S1_Response_to_ChatGPT.md`, now that the actual Comparative Design
Direction Brief has been shared.

**Status:** This supersedes the Hybrid-related findings in `Tiwas_S1_Response_to_ChatGPT.md` and the
headline Hybrid numbers in `Tiwas_S1_Opposed_Contest_Candidates.md`. Everything else in those two
documents stands unchanged.

---

## 1. Correction, Stated Plainly

You were right. The Brief's §2.1 documents:

```
Q_Hybrid_Committed = Roll + max(0, Skill − 99)
```

verbatim, alongside Margin (`Skill − Roll`) and Blackjack (`Roll`), and the situational-fit table you
quoted (target shooting / lockpicking / stealth / research → Margin; arm wrestling / shoving → Blackjack;
mixed/unknown → Hybrid) is a direct, accurate transcription of the Brief's own "Best Situational Fit"
column — not a generated example dressed up as fact. My skepticism in the previous document was a
reasonable process given what I had access to at the time — I'd never seen this file, and the user's own
earlier answer in this conversation ("their complete mathematical definitions were never locked") was
genuinely hard to reconcile with a real, locked formula having existed the whole time. But the conclusion
was wrong. The formula is real, and my stance-based Hybrid was not a reconstruction of it — it was an
unrelated invention that happened to share a name.

---

## 2. What the Brief Actually Documents (verified, §2.1 and §2.2)

| Candidate | Formula | Best Situational Fit (Brief's own wording) |
|---|---|---|
| Pure Margin | `Skill − Roll`; higher Margin wins | Precision tasks: target shooting, lockpicking, stealth, research |
| Pure Blackjack | Among successes, higher natural Roll wins (i.e. `Q = Roll`) | Contests of force or commitment: arm wrestling, shoving |
| Hybrid Committed | `Roll + max(0, Skill − 99)`; higher Committed wins | Mixed or unknown situations |

**Designer ruling (Brief's own words):** *"Quality measure is selectable per contest type. Any
implementation must preserve Cost = Roll and the 100-Fumble rule."*

The Brief also documents an exactly parallel situational fork at **S-2, hit-location granularity**
(Tier 0/1/2 — off / lightweight / full), explicitly using the same "situation-dependent by designer
ruling" language. Neither of us has touched S-2 yet; flagging it since it's structurally the same kind of
decision as S-1 and appears immediately after it in the Brief's own ranking.

---

## 3. Corrected Simulation Results

Same methodology as before (50,000 trials/point, `numpy`, seed 42, 300-round cap, 0 unresolved trials).
Margin and Blackjack numbers are unchanged — only Hybrid's formula changed, plus a new Winner/Loser cost
breakdown addressing your Test 3.

### 3.1 Headline number, corrected

| Skill A | Skill O | Margin | Blackjack | **Hybrid Committed (corrected)** | Stance Variant (S-1D, for reference) |
|---:|---:|---:|---:|---:|---:|
| 99 | 150 | 87.2% | 50.0% | **87.6%** | 49.5% |

The corrected Hybrid Committed gives the higher-Skill side an **87.6% win rate at Skill 99 vs. 150** —
statistically indistinguishable from Margin's 87.2%, not from Blackjack's 50.0%. Your prediction was
correct: the documented Hybrid fully preserves high-Skill scaling. My stance-based S-1D does not, and was
never claiming to.

### 3.2 Median winning Quality vs. Skill (symmetric matchups)

| Skill | Margin | Blackjack | **Hybrid Committed (corrected)** |
|---:|---:|---:|---:|
| 10 | 5 | 6 | 6 |
| 55 | 32 | 33 | 33 |
| 99 | 69 | 70 | 70 |
| **120** | **90** | **70** | **91** |
| **150** | **120** | **70** | **121** |

![Median winning Quality vs Skill, corrected](quality_vs_skill_corrected.png)

Hybrid now tracks Margin almost exactly above Skill 99, fully departing from Blackjack's plateau.

### 3.3 Winner/Loser Cost breakdown (your Test 3), Skill 99 symmetric matchup

| Candidate | Winner Cost | Loser Cost | Winner/Loser ratio |
|---|---:|---:|---:|
| Margin | 33.8 | 67.2 | 0.50 — **winning is cheap** |
| Blackjack | 66.1 | 34.8 | 1.90 — **winning is expensive** |
| Hybrid Committed | 66.1 | 34.8 | 1.90 — **winning is expensive** |

This is the clean numeric confirmation of the Brief's claim that Hybrid *"satisfies both efficiency and
commitment stories."* It inherits Margin's unbounded high-Skill scaling (§3.2) **and** Blackjack's
cost/risk tension (§3.3) simultaneously — winning still costs roughly twice what losing costs, exactly
like pure Blackjack, because Quality still rewards a high Roll. Margin has no such tension: under Margin,
winning is the *cheap* outcome, since a low Roll is both higher-margin and lower-cost.

### 3.4 100-Fumble impact

Unchanged in character: all four candidates land at 1.9–2.1% of decisive rounds featuring a rolled 100 at
Skill ≥ 99, independent of candidate, matching the closed-form ≈1.99% prediction from the original
document. The contest layer still doesn't touch the 100-Fumble rule's frequency, as required.

---

## 4. Updated Verdict on Your Assessment

| Your claim | Previous status | **Now** |
|---|---|---|
| The Brief documents `Q_Hybrid = Roll + max(0, Skill−99)` | Unverified — pending | **Confirmed, verified against source** |
| My 99-vs-150 Hybrid finding (49%) doesn't apply to the real Hybrid | Conditionally true, unresolved | **Confirmed — corrected number is 87.6%** |
| Don't lock one global Quality formula; situation-dependent selection is the architecture | Agree, already shipped in the GM Guide | **Unchanged — still agree, still already shipped** |
| "Committed" was assumed a stance without source support | Already disclosed by me, not new | **Unchanged — still already disclosed; also now confirmed not the documented mechanic at all** |
| Tie-break rule inconsistency, resource economics, both-fail alternatives | Agree | **Unchanged — still open action items** |

Net: you were right about the one thing that mattered most, for reasons I couldn't verify at the time.
Everything else stands as previously assessed.

---

## 5. What Else the Brief Changes

**S-2 is the same kind of decision as S-1, and it's next.** The Brief ranks S-2 (hit-location default)
immediately behind S-1 with S-1 as its only dependency, and gives it the same "situation-dependent by
designer ruling" treatment (formal duel → locations on; chaotic brawl → locations off). Not solved here —
flagging it as the natural next thread.

**The Brief's own build order (§8) resolves an inconsistency flagged in the very first document of this
conversation.** That document noted the Roadmap's dependency graph (§4) sequences Effect/Harm work before
Location work, while the Roadmap's own Phase plan (§6) sequences Location (Phase 2) before Effects/Harm
(Phase 3) — a contradiction within the Roadmap itself. The Brief's §8 Implementation Sequence — step 2:
opposed quality measures, step 3: Outcome Effects + Quality→Injury mapping, step 4: two-track harm, step
5: location modules — agrees with the dependency graph, not the Phase plan. Location comes *after*
Effects and Harm in the source material the Roadmap was synthesized from. Worth correcting the Roadmap's
Phase ordering if it's revised.

---

## 6. Updated Action Plan

| # | Action | Status |
|---|---|---|
| 1 | Verify the Hybrid formula against the Brief | **Done — confirmed** |
| 2 | Relabel the stance mechanic S-1D — Experimental Stance Variant | **Done — code and results above use this label** |
| 3 | Winner/Loser/Total Cost breakdown | **Done — §3.3** |
| 4 | Test tie-break alternatives (repeat / lower-Roll-wins / situational) | **Still open** |
| 5 | Extend Skill bands to 200/250 for the corrected Hybrid | **Still open, low effort given §3's code** |
| 6 | Test both-fail alternatives | **Still open, low priority** |
| 7 | Reconcile the Brief's activity-type situational table with the GM Guide's Skill-and-stakes table into one document | **Still open — see note below** |
| 8 (new) | S-2 hit-location: same situation-dependent treatment as S-1 | **Not started — flagged in §5** |

---

## Open Note on the GM Guide

`Tiwas_Opposed_Contest_GM_Guide.md` used an invented Stakes × Skill-level heuristic because no documented
situational guidance was available at the time. It now is. The Brief's activity-type table (precision
tasks → Margin, force/commitment → Blackjack, mixed/unknown → Hybrid) should take priority over that
invented heuristic, with the Skill-99 threshold and stakes framing retained as a secondary refinement for
situations the Brief's three categories don't obviously cover. Not rebuilt in this document — say the
word and it's a direct follow-up, now unblocked.
