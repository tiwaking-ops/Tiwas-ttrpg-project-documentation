# Candidate Entry — Third-Party Adjudication of Mutual-Failure Opposed Contests

**Status:** Provisional candidate — non-canonical, not implemented as active logic
**For:** Decision Register (Open Residual Decision Register)
**Proposed parent decision:** S-8 — Difficulty, Task Adjudication and Stakes (Open)
**Originated:** Human design discussion (Tiwa), 2026-08-30
**Source conversation:** https://claude.ai/chat/75ab8577-195d-41ca-a961-cff5badee8b5
**Drafted by:** Claude Sonnet 5, at Tiwa's request

---

## 1. Status Declaration

This entry documents a **candidate mechanic only**. It is not Locked, not yet a Candidate-accepted proposal per the project's 8-step Promotion Rule, and must not be implemented as active logic ahead of a formal designer ruling. It is filed here so the idea is captured and traceable rather than lost to chat history.

## 2. Problem Identified

The Locked portion of S-1 (Opposed Contest) resolves ties via Quality **only when at least one side succeeds**. When both participants in an opposed contest fail, no rule currently determines a winner of the *contest itself* — each participant independently resolves via Core Failing Forward (Failure XP, exertion cost, possible overflow), but the competition they were engaged in is left without an outcome.

This gap was surfaced via a worked example (two blacksmiths, equal Skill 40, rolls of 41 and 42 — both fail under roll-under-or-equal). Confirmed by direct search of the merged canonical/rules document: mutual failure appears only as a **regression-test label** ("...one succeeds, and both fail...", Phase 0 test suite), with no accompanying resolution rule. This is a genuine open gap, not a conflict with an existing Locked rule.

## 3. Proposed Candidate Mechanic

### 3.1 New derived term: Failure Margin

| Term | Formula | Meaning |
|------|---------|---------|
| **Failure Margin** | Roll − Skill | Symmetric counterpart to (success-side) Margin. Lower value = failed by less; closer to the Skill threshold. |

This does not modify the historical die roll and does not alter Core Failing Forward resolution for either participant — it is purely an interpretive value computed after the fact, in the same spirit as S-3's non-negotiable "Effects must never modify the historical die roll" constraint.

### 3.2 Proposed procedure

1. A third party (adjudicator — GM, an NPC, or another player character such as "the heroes' party") makes their own d100 roll against an appropriate Skill (candidates: Appraise, Investigate, or the same craft skill being judged — Blacksmith, in the worked example). Which skill applies is left to table/GM judgment in this draft; not itself resolved here.
2. **If the adjudicator succeeds:** they can reliably distinguish the two failed attempts. The contest winner is declared as whichever original participant had the **lower Failure Margin**.
   - Open sub-question: should the adjudicator's own Quality (Margin/Blackjack/Hybrid, per whichever mode is active) further modulate the outcome — e.g., gating how much detail or confidence accompanies the judgment? This would mirror the S-3 Quality-role question one layer up and is explicitly **not resolved by this draft**.
3. **If the adjudicator fails:** they cannot reliably distinguish the two failed works. Candidate fallback outcomes (not adjudicated against each other in this draft):
   - GM fiat
   - Flat coin-flip / random determination
   - Declared "no winner" / draw stands

## 4. Consistency Notes

- **Reuses existing primitives only.** Failure Margin is a direct structural mirror of the already-Locked Margin term; the procedure reuses the existing d100 roll-under-or-equal resolution rather than introducing a new resolution method. This satisfies the Explicit Prohibition against inventing new resolution methods.
- **Introduces a new procedure layer, not a new roll type.** The adjudication step is a second, dependent skill check layered onto an already-resolved (mutually-failed) contest. This is new *process*, which is why it requires its own ruling rather than being treated as inheriting S-1's Locked status.
- **Does not modify the historical die roll** of either original participant, consistent with the S-3 non-negotiable constraint applied here by analogy.

## 5. Open Sub-Questions (not resolved by this draft)

| # | Question |
|---|---|
| 1 | Which skill(s) are valid for the adjudication roll — fixed to one, or GM/table choice? |
| 2 | Does the adjudicator's own Quality modulate the outcome (confidence/detail), or is success purely binary (can-distinguish / cannot-distinguish)? |
| 3 | On adjudicator failure, which fallback (GM fiat / coin-flip / declared draw) is the default — or is this left fully to table discretion? |
| 4 | Edge case: if the adjudicator's own roll is a **failed Double**, do they unlock an Advanced Skill per §4's Core rule mid-adjudication? Is this desirable, or should adjudication rolls be exempted from the Advanced Skill trigger? |
| 5 | Does this mechanic generalize beyond crafting competitions to any mutual-failure opposed contest, or is it scoped narrowly to non-combat/task-based contests? |

## 6. Relationship to Other Open Items

- **Parent:** S-8 (Difficulty, Task Adjudication and Stakes) — Open. This candidate is a plausible sub-component of S-8's eventual scope (it governs adjudication procedure, per U-20 GM Procedure).
- **Structurally adjacent to:** S-3's open Quality-role question (see decision-register entry `tiwas-s3-documentarian-handoff-report-dec028-2026-08-30.md`) — both concern whether/how a Quality-like value should modulate an outcome beyond a binary win/lose determination. Any future ruling on one may inform the other, but neither should be assumed to resolve the other silently.

## 7. Explicit Non-Actions

This entry does not rule on any of the open sub-questions in §5. It does not promote this mechanic to Candidate or Locked status. No implementation should proceed from this document without a separate, explicit designer ruling.