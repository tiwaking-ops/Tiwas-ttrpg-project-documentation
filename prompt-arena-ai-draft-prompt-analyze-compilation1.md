# Draft Prompt — Confirmed Before Answer

---

## Role
Arena Agent (Agent Mode) — acting as a formal Tiwas TTRPG documentation compiler, not a game designer. The vocabulary, judgment, and tone must match the Alpha Corpus formal style: DEC-XXX references, Canonical/Locked vs Non-canonical vs Open distinctions, advisory/non-canonical status markers, source-register discipline, no invented mechanics.

## Context
You are compiling a comprehensive development-planning report from the attached 25-LLM meta-analysis (`tiwas-adapt-vale-of-madness-reports-1-llm-attribution-2026-09-02.md`) and the Alpha Playtest Corpus (`Tiwas-Alpha-Playtest-Corpus-2026-09-01.md`). The meta-analysis compares 25 independent LLM reports assessing whether *Beyond the Vale of Madness — GURPS* can be played in Tiwas, identifying which subsystems are Playtestable Now, which need adaptation, which are Design-Stage Dependencies, and which are Missing Subsystems. The developer (Tiwa) needs this condensed and collated into a single advisory report that supports actual development decisions about which missing systems to build and in what priority order.

## Audience
The developer (Tiwa) — internal development planning only. Not for public/community consumption. Not for a design-ruling audience. The report must support the developer's decision-making, not substitute for it.

## Format and Length
- **Strict Tiwas Alpha Corpus format** (DEC-XXX sections, Part A/B/C/D structure, source pointers, advisory/non-canonical status markers throughout).
- **Markdown output**, saved as a workspace file.
- **Length:** Comprehensive but condensed from ~25 reports (~140KB source) — target ~8,000–12,000 words of structured formal documentation.
- Must include:
  - Document metadata block (`title`, `version`, `status`: NON-CANONICAL advisory, `author_llm` with both producing and assessing LLM names + versions, `assessor_llm`, `created_date`: 2026-09-02, `last_modified_date`: 2026-09-02).
  - **Assessor / Author field** — must include LLM name and version if accessible.
  - Standing-prohibition overrule note (required per Alpha Corpus §1).
  - Part A — Collated System Readiness Assessment (each subsystem: DEC reference, Tiwas baseline status, reporting LLM convergence/divergence, representative quotes from source reports, readiness classification, blocking significance, development recommendation).
  - Part B — Development Priority Framework (prioritized recommendations: Priority 1 through Priority 9, derived from the 25 reports; include dependency graph; include the shortest diagnostic route that avoids major blockers; note which priorities unblock full playtest of *Beyond the Vale of Madness*).
  - Part C — Named Disagreement Register (D1–D10 from meta-analysis; preserve all 10 unresolved disagreements without silent reconciliation; include Side A/Side B/Consequence per D1–D10).
  - Part D — Playtest Readiness Verdict (full-adventure readiness: Not Ready; partial-diagnostic readiness: Partially Playtestable; which systems are Playtestable Now; which block combat; which are optional; exact classification per the 5 readiness categories from source reports).
  - Part E — Missing System Design Decisions (for each critical missing subsystem — Combat integration, Time/Action Economy, Equipment, Grappling, Conditions, Fear, Magic, NPC Content, Damage Magnitude — note what decision the developer must make; do NOT invent mechanics; flag where a design decision is needed; note if the subsystem can be deferred or handled as GM discretion for alpha).
  - Part F — Source and Evidence Register (table of all 25 reports by LLM, report number, file reference; note repaired Copilot/Copilot 365 attribution; note that `Beyond-the-Vale-of-Madness-GURPS.pdf` was not directly accessible and contents are inferred via reports).
  - Part G — Explicit Guesses / Assumptions (flag every guess made during compilation: classification thresholds, readiness interpretation, missing mechanism inference, whether the meta-analysis's agreement constitutes evidence rather than authority, etc.).
  - Closing advisory note: this is NON-CANONICAL advisory material; agreement among LLMs does not create authority; any design decision remains subject to Tiwa's governance.
- Must reference DEC-XXX numbers for every system/subsystem discussed.
- Must preserve the Canonical/Locked vs Non-canonical vs Open distinction exactly as it appears in the Alpha Corpus.
- Must not invent mechanics; must not fabricate provenance; must not silently reconcile conflicting evidence.

## Success Criteria (what separates great from mediocre)
1. **Formal format compliance:** Every section references DEC-XXX, uses the Alpha Corpus vocabulary, marks advisory/non-canonical status explicitly, and includes the required source pointers — not just generic markdown.
2. **No authority overreach:** Agreement among 25 reports is presented as diagnostic convergence, never as a design ruling; conflicts are preserved (D1–D10); no mechanism is invented; no open item is silently closed; no missing mechanism is fabricated.
3. **Actionable development prioritization:** The report clearly separates "what can be playtested now" from "what must be designed before full playtest"; the Priority 1–9 framework is derived directly from the 25 reports' convergence on blockers; the developer can read Part B and make an actual sequencing decision.

## Constraints (hard boundaries)
- **Do not invent Tiwas mechanics.** Identify gaps; recommend priorities; describe what a design decision must cover; do not write the mechanics themselves.
- **Do not treat the adventure as authority over Tiwas mechanics.** GURPS mechanics (ST, DX, FP, DR) are adventure requirements, not Tiwas rules.
- **Do not convert LLM agreement into authority.** Agreement is evidence of diagnostic convergence only.
- **Do not promote/demote/close/reopen any open item.** Preserve all open/missing/status distinctions exactly as they appear in the source reports and Alpha Corpus.
- **Do not omit the author/assessor identity.** Must include both LLM name and version if accessible.
- **Do not omit the standing-prohibition overrule note.** Required per Alpha Corpus §1.
- **No fabricated provenance.** `Beyond-the-Vale-of-Madness-GURPS.pdf` was not directly accessible; contents inferred via reports — must be stated explicitly.
- **Flag all guesses.** Every interpretation, classification, or inference that was not directly stated in a source must be flagged in Part G.

## Examples / References (what I've shared)
- `tiwas-btvm-system-comparison-compiled1.md` (the 25-report meta-analysis compilation; includes attribution manifest with SHA-256 repair records for Copilot/Copilot 365; includes Part 1 System-by-System Comparison, Part 2 Named Disagreement Register D1–D10, Part 3 Isolated Findings, Part 4 Guesses, Part 5 Governance Boundary)
- `Tiwas-Alpha-Playtest-Corpus-2026-09-01.md` (formal Alpha Corpus with DEC-001–DEC-077, status vocabulary: Canonical/Locked, Non-canonical designer ruling, Draft pending Tiwa reconfirmation, Open, Confirmed-closed; Part A/B/C/D structure; standing-prohibition overrule)
- Note: `Beyond-the-Vale-of-Madness-GURPS.pdf` was attached as reference but its full text was not directly accessible; the analysis relies on the 25 reports' extractions from it.

---

## Guesses / Assumptions I must flag in final report (pre-identified)
- Classification of D1–D10 disagreements (threshold for "materially different") was applied per meta-analysis method (§2.5); this is a compilation choice, not a Tiwas ruling.
- Readiness classification of systems not explicitly classified by a given report was inferred from the report's overall treatment — flagged per report.
- The meta-analysis's agreement on "Playtestable Now" is treated as diagnostic evidence, not as authority — this is an interpretive choice.
- Whether the developer wants actual design proposals vs pure analysis was resolved by the user's "Development priorities + recommendations" selection — the report includes recommendations but not full mechanics.
- The author identity selection "Both" combines the meta-analysis's self-reported producing LLM with the current session assistant; no platform-metadata mechanism independently verified either.
