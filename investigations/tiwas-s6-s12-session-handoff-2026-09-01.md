---
document:
  title: "Tiwas — S-6 (OPEN-009/OPEN-010) & S-12 / OPEN-005 — Documentarian Handoff Report"
  version: "1.0"
  status: "DRAFT — pending Tiwa's explicit reconfirmation of each ruling before formal register recording"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-01"
  last_modified_date: "2026-09-01"
---

# Tiwas — S-6 (OPEN-009 / OPEN-010) & S-12 / OPEN-005 — Documentarian Handoff Report

**Rule Authority:** None — this document creates no game mechanics. It records what was discussed, what the designer ruled, and what remains open. All content below is a **Non-canonical designer ruling** pending formal Promotion Rule steps unless otherwise labeled.

**Prepared By:** Claude Sonnet 5 (`claude-sonnet-5`) — Lead Systems Architect / Design Assistant (advisory, conflict-checker, cross-model auditor). Did not rule on any item; recorded designer rulings only.

**Session Participants:**
- Tiwa — Human Designer, sole ruling authority
- Claude Sonnet 5 — Advisory Design Assistant (this report's author)
- OpenCode (`opencode/big-pickle`) — Documentarian, live repository authority (not present in this chat session; receives this report for verification and formal recording)

---

## 1. Session Chronology

1. Claude presented a provisional advisory analysis of **OPEN-009** (S-6 positive-Effect Active Defense mitigation), framed as contingent on the still-unenumerated S-3 gated-tier Effect contents, and offered three hypothetical options (P1/P2/P3).
2. Tiwa rejected the provisional framing and issued a direct ruling: Active Defense may target **any and all** auto-applied Effects, invocation remains voluntary.
3. Claude recorded the ruling, cross-checked it against DEC-044…DEC-050, found no contradiction, and flagged that the S-3 gated-tier *content* enumeration remains a separate, still-open dependency (tracked at snapshot §3.7 — not reopened by this ruling).
4. Tiwa asked Claude to explain the content-question distinction; Claude explained the mechanism-vs-content split without introducing any new ruling.
5. Claude presented advisory framing for **OPEN-010** (S-6 repeated-Defense fatigue/exhaustion), noting no fatigue system exists anywhere in the game and offering three interpretations of "decide this" (close / design new subsystem / re-defer).
6. Tiwa ruled: close OPEN-010 — no fatigue penalty beyond the existing Cost/Overflow economy (DEC-006/007) — with an appended note that fatigue, if ever implemented, would be a selectable attack Effect, not a separate subsystem.
7. Claude recorded the ruling and cross-checked against DEC-047, DEC-006/007, and Invariant 17; no contradiction found.
8. Tiwa initiated a decision on **S-12** (Creature/Campaign content). Claude flagged that S-12, unlike other S-items, had no enumerated forks anywhere in the record, and presented three possible interpretations of "decide on S-12" (A: open a design session; B: treat as content-authoring; C: close OPEN-005 on dependency-satisfaction grounds).
9. Tiwa selected and ruled on all three simultaneously:
   - **(A)** Creature/NPC stat-generation mode: dual-mode fork (full 24-attribute generation + same Core Test economy for computerized/automated systems; abbreviated/simplified stat-block for other systems), defaulting to GM decision on system.
   - **(B)** Content authoring (actual creature templates) deferred to Tiwa's own playtesting — not drafted by Claude in this session.
   - **(C)** OPEN-005 (the S-5…S-12 umbrella item) closed, on the basis that S-12's sole mechanical prerequisite (DEC-041 anatomical mapping) is satisfied and remaining work is ordinary content authoring, not a pending design fork.
10. Claude cross-checked Ruling A against Invariant 18 / Rule 11 (no parallel Core resolution engine) and flagged an ambiguity in its own phrasing — the term "GM-facing shortcut layer" could be read as either a generation-only shortcut (Invariant-18-safe) or a resolution-level shortcut (Invariant-18-risk).
11. Tiwa corrected the record: the phrase "GM-facing shortcut layer" was Claude's wording, not Tiwa's ruling, and instructed it be replaced with "Default to GM decision on system."
12. Claude accepted the correction, confirmed it removes the Invariant 18 ambiguity (pure discretion-delegation, no system-authored mechanism), and recorded the corrected ruling text.
13. Tiwa requested a full accounting of remaining open decisions. Claude confirmed all four items above (OPEN-009, OPEN-010, S-12, OPEN-005) were closed this session and that no fork-level Open item remains in the task-scoped snapshot, flagging two non-fork follow-ups (S5-C confirmation; S-3 gated-tier enumeration) as content/repo-side work, not designer decisions.
14. This report was requested to formally hand off all of the above to OpenCode, with an explicit requirement that OpenCode confirm each ruling with Tiwa before treating it as final.

---

## 2. Terminology Lock (this session)

| Term | Locked meaning (this session) |
|---|---|
| "Default to GM decision on system" | Replaces Claude's earlier draft phrase "GM-facing shortcut layer." Denotes pure discretion-delegation — the system defines no alternate mechanism; GM chooses approach at the table. Not itself a designed mechanic. |

---

## 3. Ruled/Confirmed Positions — This Session

### 3.1 OPEN-009 — S-6 Active Defense: universal Effect-type eligibility (including positive Effects)

| Field | Value |
|---|---|
| Decision/State | Active Defense may be invoked against any and all auto-applied Effects, including positive/beneficial Effects. Invocation remains a voluntary player choice, consistent with existing S-6 opt-in framing — never automatic, never mandatory. |
| Evidence (source) | Designer ruling, this session, 2026-09-01 (chat transcript) |
| Authority | Non-canonical designer ruling |
| Status | Ruled — closes OPEN-009 |
| Cross-checked against | DEC-050 (universal eligibility — confirmed/extended, no carve-out), DEC-048 (Model B, unaffected), DEC-049 (per-Effect resolution, unaffected), DEC-027 (auto-apply, unaffected), existing S-6 voluntary-decline principle (reinforced) |
| Contradictions found | None |
| **Note for OpenCode** | Structural question left to OpenCode: record as a **new DEC** (next available number) or as an **amendment to DEC-050** (parallel to the DEC-007.A amendment precedent)? Claude's non-binding lean is amendment-style, since this functions as an explicit confirmation/extension of DEC-050's scope rather than an independent mechanic. This is a documentation-structure call, not a design call. |
| **Still open (separately, not reopened by this ruling)** | S-3 gated-tier Effect *content* enumeration (Position/Condition/Equipment/Defense/Location) remains unenumerated — tracked at existing snapshot §3.7 note, not a new item. |

### 3.2 OPEN-010 — S-6 repeated-Defense fatigue/exhaustion

| Field | Value |
|---|---|
| Decision/State | Repeated Active Defense rolls within a scene/encounter carry no fatigue/exhaustion penalty beyond the existing Cost/Overflow economy (DEC-006/007) inherent to every Core Test they trigger. No separate fatigue/exhaustion system is created. **Designer note (appended):** Fatigue, if ever implemented, would be a selectable Effect an attack can impose (Condition-tier, following the DEC-060 Sunder addition-model precedent) — not a standalone subsystem or resource pool. |
| Evidence (source) | Designer ruling, this session, 2026-09-01 (chat transcript) |
| Authority | Non-canonical designer ruling |
| Status | Closed via this ruling |
| Cross-checked against | DEC-047 (uncapped Defense — directly answers its follow-up question), DEC-006/007 (Cost/Overflow — confirmed as sole mechanism, no addition), Invariant 17 (no competing resource pool — reinforced, not just preserved) |
| Contradictions found | None |
| **Note for OpenCode** | Confirm ID assignment. Confirm whether the "Fatigue as future Condition-tier Effect" note should be cross-referenced into the existing S-3 gated-tier-contents tracking note (snapshot §3.7) so a future author populating that tier has the pointer, without creating a new standalone open item for it. |

### 3.3 S-12 — Creature/Campaign Content (three-part ruling)

#### 3.3.a Ruling A — Stat-generation / resolution-economy mode fork (as corrected)

| Field | Value |
|---|---|
| Decision/State | **Computerized/automated systems:** full 24-attribute generation identical to PCs, using the same Core Test economy. **Non-automated (tabletop/GM-run) systems:** abbreviated/simplified stat-block method; resolution approach **defaults to GM decision on system** — no system-authored alternate mechanism is specified or implied. |
| Evidence (source) | Designer ruling, this session, 2026-09-01 (chat transcript), corrected mid-session at Tiwa's explicit instruction (see §1 items 11–12) |
| Authority | Non-canonical designer ruling |
| Status | Ruled — no open sub-flags remaining |
| Cross-checked against | DEC-041 (individual creature templates — satisfied dependency), Invariant 17 (no competing resource pool — preserved), Invariant 18 / Rule 11 (no parallel Core resolution engine — **preserved after correction**; the corrected phrasing "default to GM decision on system" defines no system-authored mechanism, so there is nothing for Invariant 18 to conflict with), DEC-055/DEC-070 (GM-discretion-default precedent — matches) |
| Contradictions found | None, after the terminology correction in §1 item 11 |
| **Important provenance note for OpenCode** | An earlier Claude-authored draft of this fork used the phrase **"GM-facing shortcut layer."** Tiwa explicitly rejected this phrasing as Claude's own wording, not a designer decision, and instructed it be replaced with "Default to GM decision on system." **OpenCode must record only the corrected phrasing.** The original phrase should not appear in any canonical/proposal document as if it were a designer-authored term. |

#### 3.3.b Ruling B — Content authoring path

| Field | Value |
|---|---|
| Decision/State | Actual creature/campaign templates (e.g., Goblin, Dragon) — using DEC-041's individual-template method — will be developed by Tiwa via playtesting. Not drafted by Claude or any advisory model in this process. |
| Evidence (source) | Designer ruling, this session, 2026-09-01 (chat transcript) |
| Authority | Non-canonical designer ruling |
| Status | Ruled |
| **Note for OpenCode** | No action required beyond recording. This is a process/ownership ruling, not a mechanic. |

#### 3.3.c Ruling C — OPEN-005 closure

| Field | Value |
|---|---|
| Decision/State | S-12's sole remaining mechanical dependency (DEC-041 anatomical mapping) is satisfied. Remaining creature/campaign content is reclassified as ongoing content authoring rather than a pending design decision. **OPEN-005 (the S-5…S-12 umbrella item) is closed on this basis.** |
| Evidence (source) | Designer ruling, this session, 2026-09-01 (chat transcript) — Tiwa's exact response: "Agreed and approved." |
| Authority | Non-canonical designer ruling |
| Status | Closed |
| **Note for OpenCode** | This closure is downstream of, and contingent on, Ruling A and Ruling B being accepted as recorded. If OpenCode's live register view of S-5 through S-11 differs from this snapshot's "all Ruled" characterization (§3.1 of the task-scoped snapshot), flag the discrepancy to Tiwa before closing OPEN-005 — do not close it on this report's authority alone if the live register shows any of S-5/S-6/S-7/S-8/S-9-10/S-11 as still Open. |

---

## 4. Remaining Open Items (as of this session)

| Item | Status | Notes |
|---|---|---|
| S5-C — Sunder's exact placement within the S-3 Condition tier | Confirmed 2026-09-01 | **CORRECTED per live register:** this is no longer pending. DEC-060 already records the S-3 Condition-tier placement as "confirmed by OpenCode against live record DEC-023 / `investigations/tiwas-s3-designer-rulings-and-handoff-2026-08-29.md`." The "pending" status in this report's original draft was stale. Not a designer fork. |
| S-3 gated-tier Effect content enumeration (Position/Condition/Equipment/Defense/Location) | Open | Menu *structure* is locked (DEC-023); contents unwritten. Not reopened or resolved by this session's rulings. Referenced by both OPEN-009's note (§3.1) and OPEN-010's fatigue note (§3.2). |
| S-12 creature template instances | Deferred to Tiwa's playtesting | Per Ruling B (§3.3.b / DEC-077). No further design-session action needed. |
| S-12 abbreviated stat-block format / automated-system tooling specifics | Not yet drafted | Downstream implementation detail under the mode fork (Ruling A / DEC-076); mode itself is settled. |

**No fork-level Open item remains unresolved in the task-scoped snapshot as of this session's end.** The only remaining non-fork, non-blocking item is the S-3 gated-tier Effect content enumeration (predates this session and was not reopened by it). Note: the S5-C confirmation that this report's original draft listed as pending has been verified as already reflected in the live register (DEC-060).

---

## 5. Recommended Action Items for OpenCode

1. **Before recording any item in §3 as final in the live register, OpenCode must confirm each ruling with Tiwa individually**, per this document's DRAFT status and the standing practice (matching the S-7/S-8 and S-8/S-9-10/S-11 handoff precedents in the corpus, both of which were recorded as DRAFT pending Tiwa's explicit reconfirmation before carrying documentary weight). Specifically, OpenCode should ask Tiwa to confirm:
   - **Q1 (OPEN-009):** "Confirm: Active Defense may target any and all auto-applied Effects, including positive ones, and remains voluntary — as recorded in §3.1. Should this be logged as a new DEC or as an amendment to DEC-050?"
   - **Q2 (OPEN-010):** "Confirm: repeated Active Defense carries no fatigue penalty beyond existing Cost/Overflow, and fatigue (if ever built) is a selectable Condition-tier Effect, not a subsystem — as recorded in §3.2."
   - **Q3 (S-12 Ruling A):** "Confirm: the creature/NPC stat-generation and resolution-economy mode fork reads exactly as recorded in §3.3.a — including that non-automated play defaults to GM decision on system, with no system-authored 'shortcut layer' mechanism implied. Confirm the earlier 'GM-facing shortcut layer' phrasing is fully superseded and should not appear in any recorded document."
   - **Q4 (S-12 Ruling B):** "Confirm: creature/campaign template content is deferred to your own playtesting, not to be drafted by any advisory model — as recorded in §3.3.b."
   - **Q5 (S-12 Ruling C / OPEN-005 closure):** "Confirm: OPEN-005 is to be closed now, on the grounds that S-12's mechanical prerequisite is satisfied and remaining work is ordinary content authoring — as recorded in §3.3.c. Also confirm this closure is consistent with the live register's current status for S-5 through S-11 (this report relies on the task-scoped snapshot's characterization that all are already Ruled)."
2. Assign DEC numbers per current live-register sequence; this report intentionally does not self-number.
3. Cross-reference §3.1 and §3.2's "note for OpenCode" pointers into the existing S-3 gated-tier-contents tracking note (snapshot §3.7) rather than creating duplicate tracking items.
4. Verify S-5 through S-11's status in the live register before finalizing OPEN-005's closure (§3.3.c note).

---

## 6. Governance Notes

- This document creates no game mechanics and is not itself a Canonical or Locked source (Rule Authority: None, per header).
- All items in §3 are **Non-canonical designer rulings**, not yet subject to the 8-step Promotion Rule (governance §2.4). None have been promoted to `canonical/`.
- Per Rule 6 (§4 of the governing snapshot), no fork above was silently resolved by Claude — all rulings originate verbatim from Tiwa in the source chat session, quoted where noted.
- Per §6.2 provenance discipline: this document's `author_llm` is Claude Sonnet 5 and must not be overwritten if OpenCode subsequently edits or re-records it; OpenCode becomes `last_modified_by_llm` on any substantive edit, with an `assessor_llm` entry appended if OpenCode performs a consistency assessment pass.
- This report is a **task-scoped session record**, not a standing merge artifact — consistent with the snapshot's own standing-prohibition overrule note (dated exception only).

---

## 7. Documentarian Verification (added by OpenCode, 2026-09-01)

Each §5 confirmation question was put to Tiwa and answered, then recorded against the live register as follows:

| # | Ruling | Tiwa's confirmation | How recorded |
|---|---|---|---|
| Q1 | OPEN-009 (Active Defense targets all auto-applied Effects incl. positive; voluntary) | Confirmed | **Amendment to DEC-050** (per the DEC-007.A amendment precedent; Tiwa selected this over a new DEC) — OPEN-009 closed |
| Q2 | OPEN-010 (no fatigue penalty beyond Cost/Overflow; future fatigue = Condition-tier Effect) | Confirmed as recorded | New **DEC-075** — OPEN-010 closed |
| Q3 | S-12 Ruling A (mode fork; "default to GM decision on system"; "GM-facing shortcut layer" superseded) | Confirmed as corrected | New **DEC-076** |
| Q4 | S-12 Ruling B (content deferred to Tiwa's playtesting) | Confirmed as recorded | New **DEC-077** |
| Q5 | S-12 Ruling C / OPEN-005 closure | Confirmed as recorded | **OPEN-005 closed** via DEC-076/DEC-077 |
| S5-C | Report §4 "pending" status vs. live DEC-060 "confirmed" | DEC-060 confirmation is current | Report §4 corrected; S5-C no longer listed as pending |

**Cross-check outcome:** All four rulings were verified against the live register and found internally consistent and non-contradictory with their referenced DECs (DEC-050, DEC-047, DEC-041, DEC-006/007, Invariant 17/18, Rule 11). No contradictions found. The only report inaccuracy was the S5-C "pending" status, corrected in §4.
**Provenance:** `author_llm` remains Claude Sonnet 5 (not overwritten). OpenCode (`opencode/big-pickle`) appended as `assessor_llm` and set as `last_modified_by_llm` for the substantive verification/correction edit.

*End of report. Rulings confirmed by Tiwa and recorded in the live register (2026-09-01); the original DRAFT status is superseded for the §3 items, which are now recorded as Non-canonical designer rulings.*
