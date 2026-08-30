# Tiwas S-3 — Quality's Role in Effect Resolution: LLM Survey & Meta-Analysis Handoff

**Status:** Non-canonical design evidence — archival record, not a ruling
**Decision context:** S-3 Outcome Effects (Open) — sub-question: what role, if any, does Quality (already Locked at S-1, §13) play after a contest winner is determined and receives their one Effect
**Compiled by:** Claude Sonnet 5, at Tiwa's request
**Date:** 2026-08-30
**Filename sequence note:** "dec028" is an *inferred* next position in the documentarian-handoff filename sequence (…dec025, dec026, dec027 observed). No canonical DEC-0xx decision registry exists in the project's Residual Decision Register (which uses S-1…S-12); this number is a filename-sequence guess, not a registered decision ID.
**Related fixed rulings (not reopened by this document):** "One roll → one Effect" is fixed. Quality's job at S-1 (breaking ties between two successful rolls) is fixed and unaffected by anything below.

---

## 1. Purpose & Scope

This record consolidates:
1. An 8-model blind survey (self-contained prompt, no project access) asking each LLM to pick Option A, B, or C for the Quality-role question.
2. Three sequential rounds of Gemini meta-analysis performed *over* that survey.
3. Claude's independent audit of both the raw survey and each Gemini round.

It exists so a cold reader (human or LLM) can reconstruct the full evidence chain without re-reading four separate source files.

## 2. Question Surveyed (verbatim options given to each model)

| Option | Mechanic |
|---|---|
| **A — Inert** | Quality does nothing beyond its existing S-1 job. Winner picks any one Effect, flat. |
| **B — Gating** | Quality determines *which* Effects are eligible for selection (higher Quality → larger/more severe eligible subset). |
| **C — Scaling** | The one Effect always applies; Quality scales its *potency/magnitude*. |

Each model was scored against three stated design priorities, in order: (1) granular physical simulation, (2) heroic resilience / low permanent character loss, (3) minimum resolution steps per exchange.

## 3. Survey Method

Each of 8 models received an identical, fully self-contained prompt (no access to Tiwas project files, no access to each other's answers). Models were forbidden from proposing a 4th option or revising the fixed one-Effect rule.

## 4. Collated Findings

| Model | Recommendation | Core Justification | Notable Issues (see §5) |
|---|---|---|---|
| ChatGPT-5.4 Nano | **B** | Deterministic lookup on existing Quality value; zero added arithmetic; keeps severe outcomes rare. | Table formatting collapsed in source output — cosmetic only, reasoning unaffected. |
| Claude Sonnet 5 | **B** | Captures simulation depth for free; keeps severity logic inside S-3's menu layer, avoiding premature lock-in of unresolved S-4 wound math. | None identified. |
| DeepSeek-V4-Flash-0731 | **C** | Reuses the continuous Quality scalar directly; flags that B's eligibility floor could produce a "no-Effect dead end" on narrow wins. | None identified — this is the one substantive cross-cutting objection surfaced by the survey (see §7). |
| Gemini 1.5 Pro (13:45 NZST) | **B** | Single threshold check is cheaper at the table than post-roll scaling arithmetic. | None identified. |
| Gemini 1.5 Pro v1.5 (14:32 UTC) | **B** | Notes discrete/binary Effects (e.g., Conditions) don't scale cleanly under C — this specific point is valid. | **Fabricated citation**: invented "DEC-024" and a nonexistent "S-2 rule that only the contest winner's roll generates a Location Index," neither of which appears in the prompt given or in the actual project record. Also **mischaracterizes Option C** as reintroducing the already-rejected multi-Effect model — it does not; C scales the magnitude of the single Effect, it does not add Effects. |
| Meta AI (Muse Spark 1.1) | **C** | Continuous scaling avoids arbitrary "cliff effects" at threshold boundaries; curve can be capped per-Effect. | **Invented menu item**: cites "Amputation" as an Effect severity example; this was never part of the menu given in the prompt. |
| Mistral Medium 3.5 | **C** | Connects percentile precision directly to outcome magnitude. | Reasoning notably thinner/more generic than other reports; does not engage with the discrete-Effect problem Gemini v1.5 raised. |
| Qwen3.7 | **B** | Models tactical/anatomical exposure without added runtime math. | Minor list-formatting inconsistency only. |

### 4.1 Corrected Tally

The survey source document's own built-in "Summary of Consensus" table misattributed votes (it listed ChatGPT Nano and DeepSeek under Option A, which neither recommended). Verified tally against each report's actual Recommendation line:

| Option | Verified votes | Source doc's (incorrect) claim |
|---|---|---|
| A (Inert) | **0** | 2 |
| B (Gating) | **5** | 5 (right count, wrong members listed) |
| C (Scaling) | **3** | 3 (right count, right members) |

Discounting Gemini v1.5's report for the errors in §5 above (fabricated citation, mischaracterized mechanic — reasoning defect, not just a vote), the more defensible count is **4 unimpeachable votes for B, 3 for C, 0 for A**.

## 5. Errors & Fabrications Identified (traceable)

| Source | Defect type | Specific claim | Verification |
|---|---|---|---|
| Gemini 1.5 Pro v1.5 | Fabricated citation | "DEC-024's flat one-Effect-per-win" | No DEC-024 exists in the prompt given to it or in the project's actual decision record. |
| Gemini 1.5 Pro v1.5 | Fabricated citation | "existing S-2 rule that only the contest winner's roll generates a Location Index" | Not present in the prompt; not verified elsewhere in this record. |
| Gemini 1.5 Pro v1.5 | Conceptual error | Claims Option C "risks reintroducing" the rejected multi-Effect model | Incorrect — C scales magnitude of the single fixed Effect; it does not add a second Effect. |
| Meta AI (Muse Spark 1.1) | Scope padding | Cites "Amputation" as a menu example | Not part of the Effect menu given in the prompt. |
| Original survey doc | Tabulation error | Consensus table lists ChatGPT Nano and DeepSeek under Option A | Both models' own Recommendation sections state B and C respectively; zero models recommended A. |

## 6. Meta-Analysis Rounds (Gemini, 3 passes)

| Round | What it got right | What it got wrong / overstated |
|---|---|---|
| **Round 1** (gemini-S-3-collate-table1.md) | Confirmed the corrected 5–3 B/C tally. | Did not catch either fabrication in §5. Mischaracterized ChatGPT Nano as having "acknowledged Option A as purest for speed" — Nano's table cell listed A's pros (as every model's table did) but its actual recommendation was unambiguously B. Introduced an unsupported theory that a typo ("S-2" vs "S-3") in Tiwa's phrasing indicated a substantive scope mismatch in the survey — speculative, not evidenced. |
| **Round 2** (gemini-S-3-collate-table2.md) | Correctly absorbed Claude's audit; explicitly credits and reproduces the fabrication/padding findings from §5; introduces the "4 Unimpeachable" framing; correctly separates Gemini v1.5's one *valid* point (discrete-Effect scaling) from its fabricated citations. | Minor framing issue: lists the discrete-Effect point as something to "resolve" for Option B, when it is actually an argument in B's favor (B handles binary Effects natively; it is C that has the open problem here). |
| **Round 3** (gemini-S-3-collate-table3.md) | Identical content to Round 2 — no new information, no regression. | N/A (no new claims to audit). |

## 7. Compare & Contrast — Convergence and Unresolved Tension

**Convergent findings (all three independent passes — survey, Claude audit, Gemini audit — agree):**
- Option A is rejected by every model that reasoned soundly; 0 real recommendations for A.
- The B/C split is genuinely about *how* to spend the granularity, not *whether* to (both camps score above A on Priority 1).
- Discrete/binary Effects (e.g., Disarm-type outcomes) are a structural argument for B and an open problem for C — not disputed by any report.

**Unresolved tension carried forward, not settled by the survey:**
- DeepSeek's "no-Effect dead end" objection to B (a sufficiently narrow win could, if poorly tuned, be eligible for zero Effects) has **not been mechanically resolved** by any report. This is the one substantive open engineering question the survey surfaced.

## 8. Open Mechanical Requirement Before Option B Is Implementable

| Requirement | Status |
|---|---|
| Every winning Quality value (≥ 1) must guarantee at least one eligible baseline-tier Effect | **Unresolved.** No report — survey or meta-analysis — proposes a concrete floor mechanism. Required before B moves from provisional lean to implementable rule. |

## 9. Provisional Human Lean (explicitly non-binding)

Tiwa's current lean, as of this record, is **Option B**, contingent on the floor requirement in §8 being resolved. **This is not a ruling.** S-3 remains Open per the project status model; nothing in this document promotes B to Candidate or Locked status. Per the project's own Promotion Rule (8-step process, Proposals §21), survey evidence does not self-promote a proposal to canonical — an explicit designer ruling is still required.

## 10. Filed Artifacts

Stored alongside this report:
- `gemini-S-3-collate-table1.md` — Gemini meta-analysis, round 1
- `gemini-S-3-collate-table2.md` — Gemini meta-analysis, round 2
- `gemini-S-3-collate-table3.md` — Gemini meta-analysis, round 3 (duplicate of round 2)
- Original 8-model survey document (referenced throughout; not re-attached here — already held by Tiwa as `llm-quality-s3-reports-2026-08-30.md`)

## 11. Note to OpenCode

This document is filed for **archive only**. No follow-on task, validation pass, or artifact drafting is requested of OpenCode at this time. If S-3 is later ruled, this record should be linked as supporting evidence in that ruling's provenance trail, not treated as the ruling itself.