---
document:
  title: "Tiwas — S-8 / S-9-S-10 / S-11 Advisory Session — Documentarian Handoff Report"
  version: "1.0"
  status: "DRAFT — pending Tiwa's explicit reconfirmation of each fork before it carries any documentary weight beyond this handoff"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-01"
  last_modified_date: "2026-09-01"
---

# Tiwas — S-8 / S-9-S-10 / S-11 Advisory Session — Documentarian Handoff Report

**Document Version:** 1.0
**Document Status:** DRAFT — pending Tiwa's explicit reconfirmation of each fork before it carries any documentary weight beyond this handoff.
**Rule Authority:** None — this document creates no game mechanics. It records what was discussed, what the designer provisionally decided in-session, and what remains open. Nothing below is Canonical or Locked until OpenCode confirms each item directly with Tiwa and completes the 8-step Promotion Rule (D3 §21).
**Prepared By:** Claude Sonnet 5 (`claude-sonnet-5`) — Lead Systems Architect / Design Assistant (advisory, conflict-checker, cross-model auditor role). Did not rule, promote, lock, or record any decision.

## Session Participants

| Participant | Role | Ruling Authority |
|---|---|---|
| Tiwa | Human designer | Sole ruling authority |
| Claude Sonnet 5 (`claude-sonnet-5`) | Advisory design assistant | None — advisory only |
| OpenCode (`opencode/big-pickle`) | Documentarian, live repository access | Authoritative recorder; must independently confirm every item below with Tiwa before recording |

---

## 1. Session Chronology

Session worked the OPEN-005 umbrella (S-5…S-12 subsystem sequencing) from the task-scoped snapshot dated 2026-09-01 (`Tiwas-Task-Scoped-Snapshot-for-Claude-2026-09-01.md`, v2.0). Items addressed in order:

1. **S-8 remainder** (difficulty grades + Skill-side modification) — forks S8-A, S8-B, S8-C, S8-D raised, ruled, then S8-C revised mid-session after Tiwa identified a misunderstanding of "Skill Roll Pool advancement" (Invariant 10 scope). Correction walked through with a worked numeric example (including a sign-convention error by Claude, corrected on Tiwa's challenge) before Tiwa revoked the original S8-C ruling and replaced it.
2. **S-9/S-10 Extended Tests** (progress-method/failure-behavior) — forks S9-A, S9-B raised and ruled. S9-C (fork-combination coherence check) initially could not be evaluated because Tiwa's actual A2+B1 combination fell outside the illustrative combination table Claude had prepared; Claude performed a fresh coherence/Invariant-17 check on the actual combination and confirmed it clean. A follow-on gap (completion-target-setting mechanism) was identified and ruled as GM discretion, with express confirmation that GM-discretion rulings do not require a numeric default (precedent: DEC-055).
3. **S-11 Rest/Healing** (cost-scaling with wound magnitude) — forks S11-A, S11-B ruled. S11-C (multi-attempt progress-tracking model) went through three passes: an initial "reuse S-9/S-10 vs. build new" framing that Tiwa didn't understand, a plain-language re-explanation, and finally Tiwa's own proposal — ruling S-11 healing as a literal instance of the S-9/S-10 Extended Test subsystem rather than an analogous-but-separate mechanic. Completion target for the healing case confirmed as general GM discretion (no HP-deficit lock).
4. **OPEN-009** (S-6 positive-Effect Active Defense mitigation) — raised, but confirmed blocked per the snapshot's own stated dependency (undefined S-3 Effect menu). Claude declined to generate real forks against an undefined menu; at Tiwa's request, Claude produced a clearly-labeled *provisional* ruling exercise against a hypothetical placeholder Effect menu (fork recommendation A2+B1 offered, not confirmed) — **Tiwa then deferred the entire item to be voted on in a separate future session/chat.** No ruling was made on OPEN-009 in this session.

---

## 2. Terminology / Scope Notes Established This Session

- **"Skill Roll Pool advancement" (DEC-010/Invariant 10)** refers specifically to the automatic, single-test cascade loop (`while Pool >= Current Skill and Current Skill < Cap`) that converts a test's Failure XP into permanent Skill increases within that same test. It is distinct from General XP (DEC-011), which has no Cap ceiling. This distinction was the source of the S8-C revision below and should be treated as a clarifying restatement, not a new rule.
- Difficulty/wound-magnitude modifiers, per this session's rulings, act on the **Skill** side of a comparison only — never on the natural die roll (Invariant 6/Invariant 1 preserved throughout).

---

## 3. Ruled / Provisionally-Decided Positions (Non-Canonical — Require Tiwa Reconfirmation)

**Instruction to OpenCode:** For every row below, ask Tiwa to explicitly reconfirm the fork and ruling shown before recording it against the live decision register. Do not record any row as final on the strength of this document alone.

### 3.1 S-8 — Difficulty Grades & Skill-Side Modification

| Fork | Question to Ask Tiwa | Provisional Ruling This Session | Evidence Class | Notes for OpenCode |
|---|---|---|---|---|
| S8-A | "Confirm: difficulty grade structure = named tiers (e.g., Trivial/Easy/Standard/Hard/Extreme) with fixed additive modifiers to effective Skill?" | **A1** | Designer ruling | No further caveats raised this session. |
| S8-B | "Confirm: the difficulty-modified (effective) Skill is used for the success/fail check, for Failure XP calculation, AND as the comparison value entering the Skill Roll Pool cascade?" | **B1** | Designer ruling | Stated rationale: supports advancement past Skill 100; "tough times make tough men" — high-risk/high-reward design intent. **Interacts directly with S8-C below — do not record B1 without also confirming the C2 constraint on the cascade's stopping point, or Invariant 10 is put at risk.** |
| S8-C | "Confirm: effective (difficulty-modified) Skill is CLAMPED at the character's permanent Cap for purposes of the Skill Roll Pool cascade stopping condition — i.e., the cascade cannot push a character's permanent Skill above their normal Cap, regardless of difficulty bonus. Any Pool XP beyond what the cascade can spend before hitting Cap spills into General XP (DEC-011) as normal." | **C2** (supersedes an initial C1 selection, formally revoked by Tiwa mid-session after clarifying discussion) | Designer ruling | **Flag: an earlier, different C1 selection was made and explicitly revoked in this same session before C2 was substituted. OpenCode should confirm ONLY C2 with Tiwa — do not present C1 as a live option, but it may be useful to mention the revocation occurred so Tiwa isn't confused if it appears in transcript logs.** Effect of C2: preserves Invariant 10 exactly as currently worded; no Invariant-level amendment required for S-8. |
| S8-D | "Confirm: difficulty grades apply symmetrically — both bonuses (easier tests) and penalties (harder tests) — rather than penalty-only?" | **D1** | Designer ruling | No further caveats raised this session. |

**Net assessment (Claude's audit note, not a ruling):** With B1 + C2 together, S-8 requires **no amendment to any Core Invariant.** This is an improvement over the session's initial trajectory (B1 + the original C1 selection would have required an Invariant 10 amendment analogous to DEC-007.A). OpenCode should verify this reading is what Tiwa intends before recording.

### 3.2 S-9/S-10 — Extended Tests: Progress-Method & Failure-Behavior

| Fork | Question to Ask Tiwa | Provisional Ruling This Session | Evidence Class | Notes for OpenCode |
|---|---|---|---|---|
| S9-A | "Confirm: interval progress toward completing an Extended Test accumulates via Margin-accumulation — each successful interval's Margin (Skill − Roll) adds to a running total; failures contribute nothing?" | **A2** | Designer ruling | Stated rationale: increased realism; allows faster completion than a flat success-count threshold. |
| S9-B | "Confirm: a failed interval is neutral with respect to progress — it costs resources and generates ordinary Failure XP per DEC-006/007/009, but does not reduce or reset the accumulated progress total?" | **B1** | Designer ruling | No further caveats raised this session. |
| S9-C | "Confirm: the A2+B1 combination (a monotonically-increasing, never-decreasing Margin total) does not require an explicit Invariant-17 non-violation note, since it has no income/expenditure ('spending') dynamic and cannot be mistaken for a competing resource pool?" | **Confirmed coherent; no Invariant-17 note required** | Architectural constraint (assessment), not itself a numeric mechanic | Claude flags: this assessment specifically covers A2+B1. If Tiwa or a future session revisits S9-B toward any setback-on-failure option, this coherence assessment would need to be redone — it does not generalize to other B-fork choices. |
| Completion target (S-9/S-10) | "Confirm: the numeric target a Margin-accumulation total must reach to complete an Extended Test is set entirely at GM discretion, per-instance, with no formula and no fixed default?" | **GM discretion, no formula** | Designer ruling | Precedent cited in-session: DEC-055 (S-7 stabilization procedure) uses the same "GM discretion, no formal procedure" pattern for a different subsystem. OpenCode should confirm Tiwa intends the same category of ruling here, not merely an analogy. |

### 3.3 S-11 — Rest/Healing: Cost-Scaling with Wound Magnitude

| Fork | Question to Ask Tiwa | Provisional Ruling This Session | Evidence Class | Notes for OpenCode |
|---|---|---|---|---|
| S11-A | "Confirm: healing during a Rest period requires an explicit Skill Test (a full, ordinary 9-step Core Test per DEC-006) — not a passive/automatic HP restoration?" | **A1** | Designer ruling | No further caveats raised this session. |
| S11-B | "Confirm: wound magnitude penalizes the healer's EFFECTIVE Skill for the healing test — the same mechanism pattern as S8-B's difficulty-on-Skill-side approach — rather than altering the natural roll, the resource Cost, or the HP amount restored directly?" | **B1** | Designer ruling | Mirrors S8-B's mechanism for cross-subsystem consistency. |
| S11-C | "Confirm: S-11 Rest/Healing is to be treated as a LITERAL INSTANCE of the S-9/S-10 Extended Test subsystem — not merely an analogous or independently-built mechanic — meaning: one Rest period = one Extended Test interval; each interval is an ordinary Core Test with S11-B's wound-magnitude Skill penalty applied; progress accumulates via S9-A's Margin-accumulation (A2); failures are neutral per S9-B (B1); and the completion target follows the same general GM-discretion rule as S-9/S-10 (see below), with no S-11-specific override?" | **Confirmed — S-11 healing IS an Extended Test instance** | Designer ruling (Tiwa's own proposal, adopted after two prior framings were rejected as unclear) | This was Tiwa's proposed resolution, not Claude's original recommendation (Claude had proposed a narrower "reuse the architecture by analogy" framing first, which Tiwa found unclear; Tiwa's own "make healing literally an Extended Test" proposal was adopted instead). **OpenCode should confirm Tiwa still wants the literal-instance framing versus the earlier by-analogy framing, since the distinction matters for how S-11 is documented (a redirect/pointer to S-9/S-10 vs. a separate but parallel rule set).** |
| Completion target (S-11 healing case) | "Confirm: for healing specifically, the completion target remains GENERAL GM discretion — same as the base S-9/S-10 rule — and is NOT locked to 'HP deficit' as a required or default target, even though HP deficit is an obvious candidate a GM might reach for?" | **GM discretion, generally — no HP-deficit lock** | Designer ruling | Claude had raised HP-deficit-as-locked-default as an alternative option; Tiwa explicitly declined it in favor of unmodified general GM discretion. |

---

## 4. Item Explicitly Deferred This Session — No Ruling Made

### OPEN-009 — S-6 Positive-Effect Active Defense Mitigation

**Status: DEFERRED BY TIWA to a future session/chat. No ruling was made. Do not record any decision against this item.**

Session notes for context only:

- Per the snapshot (§3.4), this item is explicitly blocked: *"Cannot be scoped until the S-3 Effect menu is defined (currently undefined)."* Claude initially declined to generate real forks against an undefined menu, consistent with governance Rule 6 (never silently resolve an open fork) and Rule 9 (preserve the distinction between empirical evidence and designer judgement).
- At Tiwa's explicit request, Claude produced a clearly-labeled **provisional, hypothetical exercise** — constructing a placeholder Effect menu from fragments actually present in the snapshot (Wounded, Sundered, Dizzy, Condition tier, confirmed existence of positive Effects per OPEN-009's own text) and offering illustrative forks (OP9-A: does Active Defense apply to positive Effects at all; OP9-B: who may invoke it) with a non-binding recommendation (A2+B1 — adversarial-use-case-only, invoked only by a target of an opponent's self-directed buff).
- **Tiwa did not adopt or rule on any of these provisional forks.** Tiwa deferred the entire item before any ruling was finalized, to be revisited and voted on in a separate future chat.
- **OpenCode should take no action on OPEN-009** beyond noting that this session's exploratory discussion exists (for continuity/context if useful to a future session) — it must not be recorded as a ruling, provisional or otherwise, and the placeholder Effect menu used in the exercise must not be mistaken for progress toward defining the actual S-3 Effect menu.

---

## 5. Audit Findings / Corrections Made In-Session

1. **S8-C revocation and replacement.** Tiwa's initial S8-C selection (C1) was based on a different understanding of what "Skill Roll Pool advancement" (Invariant 10) refers to than the mechanism actually defined in DEC-010/§4 of the system instructions. Claude explained the mechanism concretely with a worked numeric example; a sign-convention error in that first example (treating an "Extreme" difficulty modifier as a bonus rather than a penal, inconsistent with the intended risk framing) was caught by Tiwa's own challenge and corrected by Claude before the explanation was finalized. Tiwa then explicitly revoked C1 and selected C2. This sequence should be visible to Tiwa in the final confirmation pass so nothing is recorded on the strength of the earlier, revoked selection.
2. **S9-C combination gap.** Claude's original fork-combination table for S9-C did not include Tiwa's actual selected combination (A2+B1). Claude performed the coherence/Invariant-17 check live, after the fact, rather than having pre-validated it. This is noted so OpenCode/Tiwa are aware the S9-C confirmation was reactive, not from a pre-built option set.
3. **S11-C required two re-framings.** Claude's first two framings of the S11-C question (an abstract "reuse vs. build new progress model" framing, then a plain-language explanation) did not land with Tiwa. The eventual resolution was Tiwa's own proposal (healing as a literal Extended Test instance), not a selection from Claude's offered options. This is flagged per the general documentarian practice of not attributing a designer's own proposal to Claude's advisory recommendation set.

---

## 6. Remaining Open Items (Unaffected or Newly Surfaced by This Session)

- **OPEN-009** — deferred, unruled (see §4).
- **S5-C** (Sunder Effect menu placement, from a prior session) — still pending OpenCode's live-repository confirmation; unaffected by this session but noted as still outstanding per the snapshot (§3.2).
- **S-12** (Creature/Campaign content) — untouched this session, remains Open per the snapshot.
- **S-8 remainder beyond the four forks ruled here** — no further S-8 sub-forks were raised or identified as outstanding this session; OpenCode should confirm against the live register whether any additional S-8 sub-questions exist beyond S8-A/B/C/D.
- **Provenance note carried over from the snapshot:** the model-string self-identification format `{name: "Claude Sonnet 5", version: "claude-sonnet-5"}` was used per the snapshot's own §6.3 instruction; OpenCode should confirm this is still the correct canonical form for its provenance records.

---

## 7. Recommended Action Items for OpenCode

1. Walk Tiwa through §3.1–§3.3 row by row, using the exact "Question to Ask Tiwa" phrasing (or equivalent), and obtain explicit reconfirmation before assigning DEC numbers or writing to the live register.
2. Do **not** number or record OPEN-009 in any form this session; leave its status as `Open, deferred` in the register, optionally with a pointer to this handoff's §4 for context.
3. When recording S8-C, ensure only C2 is written to the register; the revoked C1 selection should not appear as if it were ever an operative ruling (a one-line historical note referencing the revocation is acceptable per standard practice, consistent with how superseded material is otherwise retained).
4. When recording S11-C, confirm with Tiwa whether the "literal Extended Test instance" framing should be documented as a redirect/cross-reference to the S-9/S-10 rule text (avoiding duplication) or as a self-contained S-11 section that restates the inherited mechanics — this is a documentation-structure choice, not a ruling, but affects how future LLMs/readers find the rule.
5. Cross-check the assembled S8-B + S8-C combination, and the S11-B + S11-C combination, against Invariant 10 and Invariant 17 respectively one more time using OpenCode's live-repository view, since this document's Invariant-compliance assessments were performed by Claude against the task-scoped snapshot only, not the full live corpus.

---

## 8. Governance Notes

- **Non-canonical reminder:** Nothing in this document is Canonical or Locked. All rows in §3 are, at most, non-canonical designer rulings pending OpenCode's confirmation pass with Tiwa and completion of the 8-step Promotion Rule (D3 §21) for any that are intended to eventually reach `canonical/`.
- **No self-authorization:** Claude did not rule, promote, lock, or record any decision during this session, per its defined advisory role. Every ruling recorded above as "provisional" originates from Tiwa's own selections in-chat; Claude's contributions were limited to fork construction, Invariant/consistency checking, evidence-class labeling, and flagging ambiguities per Rule 6.
- **OPEN-009 handling is a governance-compliant deferral, not an oversight** — Tiwa explicitly chose not to rule this session after being shown a clearly-labeled provisional exercise; this is the correct outcome under Rule 6 (never silently resolve an open fork) when the designer determines more consideration is needed.

*End of handoff report.*
