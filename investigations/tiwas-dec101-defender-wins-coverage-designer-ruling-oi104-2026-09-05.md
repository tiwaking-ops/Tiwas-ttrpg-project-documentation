---
document:
  title: "DEC-101 Defender-Wins Coverage Design Ruling (OI-104) — Closed: coverage satisfied"
  version: "1.0"
  status: "Advisory recording of a designer ruling. Non-canonical. Assigns DEC-109 in the decision register."
provenance:
  author_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
  ruling_origin: "Human designer (Tiwa), in-session ruling, 2026-09-05, resolving open item OI-104 (DEC-101 defender-wins coverage) from the v4 Cross-Report Synthesis 2026-09-05"
  recorded_in: "_consolidation/decision-register.md DEC-109"
---

# DEC-101 Defender-Wins Coverage Design Ruling (OI-104) — Closed: coverage satisfied

## 1. Purpose

This document records Tiwa's designer ruling resolving **OI-104** — the DEC-101
(defender-wins) **coverage** item. OI-104 arose from the v4 Cross-Report Synthesis
(2026-09-05) §6.4/§9.5: Claude's 99-round run recorded zero natural defender-wins and
flagged DEC-101 as a genuine coverage gap for a future matched-skill or forced-scenario
test; the synthesis scheduled a forced case (Low priority, coverage — not a rule gap).

## 2. Open item resolved

| ID | Issue | Source |
|---|---|---|
| OI-104 | DEC-101 coverage — need a matched or forced case to exercise defender-wins | v4 Cross-Report Synthesis (2026-09-05) §6.4, §9.5; Claude §8 coverage note |

## 3. Evidence established before the ruling

- **DEC-101 itself is already decided** and convergent (2 : 1, ruled 2026-09-04): on a
  defender win in an opposed attack contest the attack fails and the defender gains NO
  counter-Effect. OI-104 is an **empirical coverage** item, not a rule gap.
- **Grok 4.5's v4 run exercised DEC-101 frequently and in-spec:** "Every defender-win
  produced 'attack fails, no counter-Effect'. No reciprocal Injury or Condition applied"
  (`tiwas-ice-troll-combat-playtest-v4-comprehensive-report.md` line 99, 157); summary
  table "Defender-wins (no Effect) **Yes, Frequent**" (line 204). 16-round run, complete.
- **Claude Sonnet 5's v4 run** narrated **0** DEC-101 occurrences (`tiwas-ice-troll-v4-
  final-report.md` §4) **but its own embedded combined log contains double-success
  defender-win cases labelled "wins the opposed contest (DEC-101/C-09)"** (e.g.
  `tiwas-ice-troll-v4-combined-report.md` R6, R15, R20, ...) — an internal inconsistency
  in that artifact, noted for audit.
- **GPT-5.6 Luna** never reached the branch (aborted Round 1).

**Status before ruling:** OI-104 remained open in the synthesis §10 table only because the
synthesis followed Claude's summary; the branch had in fact been exercised in-spec by Grok.

## 4. The ruling — verbatim (Tiwa, 2026-09-05)

> **RULING — Option 1: Close OI-104 as resolved (coverage satisfied).**
>
> **Reason:** "Next playtest will invalidate these run results anyway."

## 5. Structured restatement (for execution)

- **OI-104 is CLOSED as resolved.** DEC-101's defender-win branch has been exercised
  in-spec by Grok's v4 run (frequent, complete, no invention); DEC-101's 2 : 1 convergence
  is unchanged. No rule change, no new mechanic, no forced-scenario test required as a
  prerequisite.
- **Empirical status:** the v4 run results (including the undisambiguated coverage
  question, the diverging round counts, and all scaffold-generated artefacts) are
  **superseded for analysis purposes** by the next playtest by Tiwa's ruling — the coming
  playtest will be run under the now-complete ruling set (DEC-103 through DEC-109) and any
  contradiction between v4 run reports and the new ruling set is resolved in favour of the
  new rulings.
- **Audit note (no action):** Claude's combined artifact internally contradicts itself on
  DEC-101 (narrative "0 occurrences" vs. log rows labelled DEC-101/C-09). This is a
  recording disagreement inside a superseded run, noted but not pursued.

## 6. Register entry

Recorded in `_consolidation/decision-register.md` (Section B, Non-canonical designer ruling):

| ID | Subject | Status |
|---|---|---|
| DEC-109 | DEC-101 defender-wins coverage (OI-104): closed as resolved — branch exercised in-spec by Grok; run results superseded by next playtest | Ruled (non-canonical) |

## 7. Status

**Status:** Advisory recording — not canonical
**Authority:** Non-canonical designer ruling (real decision; promotion requires the
8-step Promotion Rule)
**Assigns:** DEC-109 (next sequential ID after DEC-108)
**Resolves:** OI-104 (DEC-101 coverage) — closed as resolved; coverage satisfied
**Preserves:** DEC-101 (unchanged), DEC-013, DEC-024, DEC-023.A, DEC-105 (exchange
algorithm), and all of DEC-103–DEC-108
**Leaves open:** GM Fiat universality; the DEC-108 carried-open corners (AoE
"most-targets" composition with post-incapacitation targeting exclusion; PC extension of
the exclusion)
**Canonical rule change:** None