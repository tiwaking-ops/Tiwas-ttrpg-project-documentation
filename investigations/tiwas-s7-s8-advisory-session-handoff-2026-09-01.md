---
document:
  title: "Advisory Session Handoff — S-7 Incapacitation/Death Forks & S-8 Stakes Gate Rejection"
  version: "1.0 — DRAFT, pending Tiwa reconfirmation"
  status: "Draft"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-01"
  last_modified_date: "2026-09-01"
---

# Advisory Session Handoff — 2026-09-01

**Document Version:** 1.0 — DRAFT (all items below require Tiwa's explicit reconfirmation before OpenCode records
anything against the live register — see §4)
**Document Status:** Draft
**Rule Authority:** None (this document is advisory work product only; it does not itself rule, promote, or lock
anything — per Promotion Rule §1.4 and LLM Governance Rule 6, no fork is silently resolved)
**Prepared By:** Claude Sonnet 5 (`claude-sonnet-5`), in the Lead Systems Architect / Design Assistant (advisory,
conflict-checker, cross-model auditor) role for this project, working from the static project snapshot
(`Tiwas-Advisory-Session-Brief-2026-08-31.md` + `opencode-s5s7s8-repoinfo-for-claude1.md`) — **no live repository
access this session.**
**Session Participants:**
- Tiwa — human designer, sole ruling authority
- Claude Sonnet 5 (`claude-sonnet-5`) — advisory design assistant, author of this document
- OpenCode (`opencode`/`big-pickle`) — documentarian, live repository access, addressee of this handoff

**Purpose:** Formally capture the rulings made in this session (S-8 Stakes Gate rejection; S-7 Incapacitation/Death
forks 1–6) for OpenCode to verify against the live repository, assign DEC numbers, and commit to the register — and
to flag every item that requires Tiwa's **explicit reconfirmation** before that happens.

---

## 1. Ruling — Proposals/WIP §8: Stakes Gate

| Field | Value |
|---|---|
| **Subject** | S-8 Stakes Gate proposal (Proposals/WIP §8) |
| **Decision** | **Rejected.** No pre-Core-Test "skip the roll" filter will exist for stakes-based reasons. |
| **Designer's stated rationale** | Rolls are intended to be meaningful and to carry risk/reward. A Stakes Gate reduces roll frequency, which comes at the cost of player opportunities for risk and reward that the system is designed to preserve. |
| **Evidence source** | This session (2026-09-01), advisory brief §Open-1 / repo-info file, S-8 section |
| **Evidence class** | Designer ruling (not mechanically forced; not an empirical finding) |
| **Authority** | Non-canonical designer ruling, pending DEC assignment |
| **Status** | Ruled (this session) — **Draft** until Tiwa reconfirms (§4) and OpenCode commits |

**Downstream effects flagged (not decided by this document):**
- Proposals/WIP §8's Stakes Gate entry should be marked Rejected/Superseded.
- Roadmap Phase 6 scope ("difficulty grades, Skill-side modification, Stakes Gate") should have Stakes Gate struck.
  Remaining S-8 scope narrows to difficulty grades + Skill-side modification only.
- Both source documents (brief §Open-1; repo-info file) flagged the Stakes Gate specifically as the most likely
  trigger for reopening the S-2 non-attack Location Index deferral (DEC-020→036→037 chain). With Stakes Gate
  rejected, that specific reopening pathway no longer exists. This is **not** a claim that the DEC-037 chain is
  reinforced or re-verified — only that this one flagged trigger is removed.

---

## 2. Rulings — Proposals/WIP §7: Incapacitation and Death (S-7)

Six forks were surfaced from the directional material in Proposals/WIP §7 (per `opencode-s5s7s8-repoinfo-for-claude1.md`).
All six now have designer rulings. Evidence source for all: this session, 2026-09-01.

| Fork | Subject | Decision | Evidence Class |
|---|---|---|---|
| **1** | HP = 0 state | Forced incapacitation. No roll, no save/check. | Designer ruling |
| **2** | Wound (S-4) / Incapacitation relationship | Independent. Wound severity (DEC-035) does not feed into incapacitation. Incapacitation is HP-driven only. | Designer ruling |
| **3** | Permanent character loss (death) | Occurs when: (a) character is incapacitated **and** all attempts to revive via skill tests have failed, **or** (b) player voluntarily chooses permanent loss while incapacitated. | Designer ruling |
| **4** | Stabilization procedure | **GM discretion, no formal procedure.** | Designer ruling |
| **5** | Interaction with S-11 (Rest/Healing) | Incapacitation is HP-driven; does not affect healing/recovery mechanics. | Designer ruling |
| **6** | S-2 non-attack reopening-trigger flag | See §2.1 below — closed for this session, not formally retired in register. | Designer ruling (closure), pending verification |

### 2.1 — Fork 6 detail (for the record)

The original flag arose from Proposals/WIP §7's pre-DEC-032 phrasing, "serious localized injury may matter where
locations are active." Tiwa clarified in-session that "injury" in that pre-formalization sentence refers to what
is now formally "Wound" (post-DEC-032 split: Injury = HP, Wound = localized lasting state). Under that
retranslation, the original line implied severe location-gated Wounds should factor into incapacitation — which
would have conflicted with Fork 2 as ruled.

**Tiwa explicitly confirmed Option A**: Fork 2 stands as ruled (HP-only), and the original §7 line is superseded by
the Fork 2 ruling, notwithstanding the terminology clarification. Fork 6 is treated as closed for this session on
that basis — the reopening risk is assessed as substantially reduced, since incapacitation under the ruled system
has a single trigger (HP = 0) with no Wound-severity or location dependency, and non-attack HP-loss cases are
already covered by DEC-037's four-case framework. This assessment is **advisory, not a claim that DEC-037 has been
re-verified** — that determination belongs to whoever next reviews DEC-037 against the finished S-7 ruleset.

### 2.2 — Flagged relationship requiring explicit statement (not a new fork, a documentation note)

Fork 3's wording commits to "skill tests" as the revival mechanism for a downed character. Fork 4 leaves the
*procedure* around that mechanism (which skill, how many attempts, pacing) to GM discretion. These two rulings are
coherent together but the relationship should be stated explicitly in the Canonical documentation rather than left
for a reader to infer — GM discretion applies to the mechanics of the skill-test-based revival attempts, not to
whether skill tests are used at all (that much is fixed by Fork 3).

---

## 3. Items explicitly NOT decided in this session

For clarity and to avoid scope creep in OpenCode's recording pass:

- No DEC numbers have been assigned by this document — per the brief §4.3, numbering is left to OpenCode against
  the live register's actual next-available sequence.
- S-5 (Armor) was discussed for context only — no forks were opened or ruled.
- S-8's remaining scope (difficulty grades, Skill-side modification mechanics) was **not** ruled — only the Stakes
  Gate sub-question was closed.
- OPEN-009 (S-6 positive-Effect Active Defense mitigation) and OPEN-010 (S-6 repeated-Defense fatigue/exhaustion)
  were not addressed this session.
- No formal Canonical Rules & Changelog language was drafted — Promotion Rule steps 5–8 remain OpenCode's/Tiwa's
  next actions after DEC assignment, not something this document performs.

---

## 4. Reconfirmation required from Tiwa

Per governance (no AI model self-authorizes decisions; Claude's role is advisory capture, not ruling authority),
**this document is a session transcript formalized into handoff shape — it is not itself authoritative.** Before
OpenCode commits anything against the live register, please explicitly reconfirm each item below (a simple
"confirmed" per line, or corrections, is sufficient):

1. **S-8 Stakes Gate rejection** (§1) — confirm the decision and rationale as recorded are accurate.
2. **S-7 Fork 1** — confirm: HP = 0 triggers forced incapacitation, no roll.
3. **S-7 Fork 2** — confirm: incapacitation is HP-driven only; Wounds remain fully independent (Option A, as
   reconfirmed after the injury/Wound terminology discussion).
4. **S-7 Fork 3** — confirm the two-branch permanent-loss condition (failed revival attempts, or voluntary player
   choice) is complete as worded — in particular, whether "all attempts... have failed" implies an unlimited number
   of revival attempts is permitted (no cap was stated), or whether a cap is intended and simply wasn't specified.
5. **S-7 Fork 4** — confirm "GM discretion, no formal procedure" is the final intended scope, including the
   relationship noted in §2.2 (discretion governs the skill-test mechanics, not whether skill tests are used).
6. **S-7 Fork 5** — confirm incapacitation has no interaction with S-11 healing/recovery mechanics.
7. **S-7 Fork 6** — confirm the closure assessment in §2.1 is acceptable to record as-is, understanding it is a
   session-level assessment and not a formal re-verification of DEC-037.

Once reconfirmed, OpenCode should proceed with DEC-number assignment, register updates, and (where applicable)
Promotion Rule steps 5–8 for any items Tiwa additionally designates for Canonical promotion.

---

*End of handoff document. Prepared by Claude Sonnet 5 (`claude-sonnet-5`), 2026-09-01, working from the static
snapshot — no live repository access this session. This document is disposable working material pending Tiwa's
reconfirmation and OpenCode's verification against the live register; it supersedes nothing on its own.*
