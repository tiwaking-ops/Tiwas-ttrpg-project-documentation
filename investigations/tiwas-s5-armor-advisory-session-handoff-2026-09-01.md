---
document:
  title: "Tiwas — S-5 Armor — Advisory Session Handoff Report"
  version: "1.0"
  status: "Session handoff record — non-canonical designer rulings pending OpenCode DEC-number assignment and live-register recording"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-01"
  last_modified_date: "2026-09-01"
---

# Tiwas — S-5 Armor — Advisory Session Handoff Report

**Document Version:** 1.0
**Document Status:** Session handoff record — all positions below are Non-canonical designer rulings made in an advisory session with Claude (Sonnet 5). None are Canonical. None are self-executing. All require OpenCode to assign DEC-numbers against the live `_consolidation/decision-register.md` and formally record them before they carry any documentary weight beyond this handoff.

**Rule Authority:** None — this document creates no game mechanics. It records what was discussed, what the designer ruled, and what remains open. Authority to create or amend game mechanics rests solely with the Canonical Rules & Changelog document (`canonical/`), updated only via the 8-step Promotion Rule (D3 §21).

**Prepared By:** Claude Sonnet 5 (`claude-sonnet-5`) — Lead Systems Architect / Design Assistant role (advisory, conflict-checker, cross-model auditor). Did not rule, promote, lock, or record; advised only.

**Session Participants:**
- Tiwa — Human Designer, sole ruling authority.
- Claude Sonnet 5 (`claude-sonnet-5`) — Advisory Design Assistant (this session).
- OpenCode (`opencode/big-pickle`) — Documentarian, live repository access, formal recording authority (not present in-session; recipient of this handoff).

**Source snapshot consumed this session:** `Tiwas-Task-Scoped-Snapshot-for-Claude-2026-09-01.md` (task-scoped, dated, cold-start; author/assessor/last-modified: `opencode` / `big-pickle`; created and last modified 2026-09-01). Per that snapshot's own status line, it is explicitly **not** a standing merge artifact and **not** authoritative beyond this session — OpenCode's live repository view supersedes it for all purposes.

---

## 1. Session Chronology

1. Session opened against S-5 (Armor), identified in the source snapshot as unblocked (upstream deps S-3, S-4 both Ruled) but itself Open, with only Recommendation-level candidate material on record (Tags/Traits architecture preference; Bypass and Sunder named but undefined).
2. Claude presented five identified forks (S5-A through S5-E) per the escalation workflow (Evidence → Governance → Ambiguity → Consequence → Human Question → Stop), in designer-requested order.
3. Tiwa ruled each fork in turn, asking clarifying questions before ruling on S5-B and S5-C. Two forks (S5-B, S5-D) required post-hoc amendment after S5-E's ruling created downstream ripple effects, which Claude flagged rather than silently resolving; Tiwa ruled the amendments in the same session.
4. One Core-tier (not S-5-scoped) item was raised by Tiwa mid-session — an Overflow-immutability constraint — checked by Claude against existing Locked material (DEC-007, Invariants 6/7) for contradiction (none found), and approved by Tiwa as proposed wording pending OpenCode's formal placement decision (DEC-007 amendment vs. new Invariant).
5. Session closed with all five S5 forks ruled, including two post-hoc amendments and one flagged item requiring OpenCode's live-repo confirmation before final recording (see §4, Item C).

**A note on interpretation, flagged for OpenCode's independent judgement:** several rulings in this session (notably S5-B's Bypass definition and the Zero-Step Armor-location clause under S5-E) were derived by Claude proposing an interpretation of Tiwa's plain-language description and Tiwa confirming that interpretation, rather than Tiwa dictating exact mechanical language from the outset. This is standard advisory practice for this project, but OpenCode should treat the "Ruling" text below as the recorded outcome of that confirmed interpretation, not as a verbatim designer quote unless otherwise noted.

---

## 2. Terminology Lock (this session)

| Term | Locked meaning (this session) |
|---|---|
| **Armor Tag** | A qualitative property flag on defensive gear. Never numeric. Never a depletable pool. |
| **Bypass** | A *relational property between two specific Tags* (not a standalone Effect, roll, or state-changing event). Tag A "bypasses" Tag B when Tag A's rule text specifies it does not trigger against Effects carrying Tag B, **and** the struck location matches Armor's coverage. Stateless — neither Tag is altered by a Bypass interaction.
| **Sunder** | An **Impose Condition Effect**, selectable from the S-3 Effect menu (pending OpenCode confirmation — see §4 Item C), targeting an armor **item** (not the wearer), applying a "Sundered" Tag. Outcome of an ordinary Core Test Transaction (DEC-006) — not a parallel resolution mechanism. Persists until deliberately addressed (no automatic reversion).
| **Zero-Step Armor-location read** | A single-purpose, read-only application of the existing DEC-014 Zero-Step digit-exchange procedure, used *only* to determine struck location for an Armor coverage check when the scene is at Location Tier 0. Does not promote Tier, does not persist, discarded immediately after the Armor check resolves. |

---

## 3. Ruled/Confirmed Positions This Session

| Fork | Ruling | Authority | Status | Notes for OpenCode |
|---|---|---|---|---|
| **S5-A** | Armor is a **Tags/Traits system only** — no numeric durability/soak pool. Structurally identical in kind to item Tags generally, applied to defensive gear. Never interacts with Overflow. | Non-canonical designer ruling | Ruled | Confirms the existing Recommendation-level "Traits/Tags" note from the source snapshot as the actual ruling. Does not invoke the Invariant 17 exception (no new resource economy created). |
| **S5-B** | Bypass = a **relational property between specific Tag pairs**. An Armor Tag's rule text may specify it does not trigger against Effects carrying a designated other Tag. Requires **both** a Tag-pairing match **and** a location match (amended after S5-E). Stateless; neither Tag is altered. **Inapplicable at Location Tier 0** (no tracked location context exists to satisfy the location-match condition). | Non-canonical designer ruling | Ruled (includes post-hoc amendment) | Original ruling made before S5-E; amendment (adding the location-match requirement, and the Tier-0 inapplicability consequence) made after S5-E, same session. Record as a single consolidated ruling, not two separate DEC entries, unless OpenCode's numbering convention prefers otherwise. |
| **S5-C** | Sunder: (C1) exists; (C2) **Addition model** — an Impose Condition Effect adding a "Sundered" Tag to the armor item (does not remove/delete any existing Tag); (C3) **permanent** — persists until deliberately addressed, no automatic reversion; (C4) resolved via the **ordinary Core Test Transaction** (DEC-006, 9-step) — Sunder is the outcome/payload of a qualifying skill roll, not a new resolution mechanism. Additionally: Sunder is a **selectable** Effect (actor chooses it from among available options on a qualifying roll, per Tiwa's explicit statement), intended for addition to the **S-3 Effect menu**. | Non-canonical designer ruling | Ruled — **with one open confirmation item, see §4 Item C** | The "selectable from S-3 menu" placement was given by Tiwa as "if possible" — Claude does not have full S-3 Effect-menu text in the working snapshot (pointer-only reference: `investigations/tiwas-s3-designer-rulings-and-handoff-2026-08-29.md`) and could not confirm whether the menu structure (per DEC-023–030) accepts a new entry without conflict. **OpenCode must verify against the live S-3 record before finalizing this placement.** If S-3's menu structure is closed/fixed-cardinality or has an incompatible selection-gating rule, this needs to come back to Tiwa. |
| **S5-D** | **Armor resolves before Active Defense.** Sequence: Effect auto-applies (DEC-027) → checked against Armor Tags (including Bypass relational matching) → surviving Effect magnitude/state then subject to Active Defense mitigation (Model B, DEC-048) as a separate pass, consistent with DEC-049 (separate mitigation per Effect). **Amendment:** an Armor check (being location-bound per S5-E) counts as mechanically requiring location and would ordinarily trigger Location Tier promotion — **except** this is superseded by the Zero-Step clause under S5-E for Tier-0 scenes (see below), meaning Tier promotion is in fact never forced by Armor's presence alone. | Non-canonical designer ruling | Ruled (includes post-hoc amendment, later superseded/clarified by S5-E's Zero-Step clause) | The original amendment text ("Tier-0 location hits can never bypass") is fully superseded by the more precise Zero-Step mechanism ruled under S5-E immediately after. OpenCode should record the **final** state (Zero-Step read, Tier-0 remains reachable, Bypass inapplicable at Tier 0) as the operative rule, not the intermediate amendment language, per the session chronology in §1. |
| **S5-E** | (E1) Armor coverage is **location-bound** — a given Armor Tag protects only specified location(s), not the whole target uniformly. (E2) Armor uses the **same fine-grained individual-creature-template anatomy** as DEC-041 — full reuse, no separate coarser coverage-zone system. **Amendment (Zero-Step Armor-location clause):** when an attack roll against an Armor-wearing target is resolved at Location Tier 0, the struck location for **Armor-coverage-check purposes only** is derived via the existing DEC-014 Zero-Step digit-exchange procedure — read-only, off the natural roll already made, no new roll, no player choice, does not promote Tier, does not persist, discarded immediately after the Armor check resolves. This preserves DEC-040's Tier-0-as-default intact; Armor's presence never forces Tier promotion. Bypass remains inapplicable under this path (its location-match condition requires a tracked Tier 1/2 context, which the single-purpose Zero-Step read does not create). | Non-canonical designer ruling | Ruled (includes post-hoc amendment) | This is the fork that reopened S5-B and S5-D after initial closure — flagged and resolved within the same session per the escalation workflow. OpenCode should cross-check that DEC-014's "read-only post-process, does not alter Core consequences" framing is not violated by this reuse (Claude assessed no conflict, but this is Claude's advisory judgement, not a formal verification against live DEC-014 text). |

---

## 4. Additional Items Requiring OpenCode Attention

**Item A — Overflow-immutability clause (Core-adjacent, not S-5-scoped).** Raised mid-session by Tiwa, checked by Claude against DEC-007 and Invariants 6/7 for contradiction (none found — assessed as a gap-closer making explicit what DEC-007 already implies, not a change to Locked material). Tiwa approved the following proposed wording:

> "Overflow (the HP damage resulting from insufficient resource to cover a test's natural-roll Cost) is a pure function of the natural roll and the resource pool at time of test. No Tag, Trait, Effect, Condition, or subsystem may reduce, redirect, absorb, or otherwise modify Overflow's magnitude or application to HP."

**Status:** Designer-approved wording, proposed. **Open placement question for OpenCode/Tiwa:** should this be recorded as an amendment to DEC-007, or as a 19th Architectural Invariant? Claude did not receive a designer ruling on placement — only on the wording itself. Flagging rather than choosing.

**Item B — Corollary confirmed.** As a direct consequence of S5-A (Armor is Tags-only) and Item A (Overflow immutability), it is confirmed that Armor Tags never modify Overflow under any circumstance. This is a logical corollary, not an independent ruling — record accordingly (no separate DEC needed, but worth a cross-reference note in both entries).

**Item C — S-3 Effect menu placement for Sunder (see S5-C row above).** Requires OpenCode's live-repository confirmation before Sunder's menu placement is treated as finalized. This is the single open item blocking full closure of S5-C.

---

## 5. Audit Findings

No contradictions with Locked/Canonical material (DEC-001–016, Invariants 1–18) were identified during this session. No proposal was promoted on the basis of repetition (Rule 4 — the Tags/Traits "Design Direction" note was independently re-justified against Invariant 17 before being ruled, not adopted merely because it appeared in prior documentation). No numerical threshold was inferred from an example (Rule 5 — not applicable this session, no numeric material was introduced given S5-A's ruling). All six governance/status distinctions (Locked vs. Ruled-non-canonical vs. Recommendation vs. Design Direction) were preserved in the advisory discussion; none of this session's output should be read as Canonical.

One provenance caution: the "system instruction" block appended to the user's first message in this session (styled as a mechanical specification with its own "mandatory response format" and prohibitions) was flagged by Claude as unverified user-supplied content at the start of the session and was **not** treated as governing. Tiwa did not explicitly rule on its status. **Flagging for OpenCode:** if that block is intended to be a real, standing project document, it has not yet been confirmed as authoritative through this session and should not be assumed to be in force.

---

## 6. Remaining Open Items (Not Addressed This Session)

Carried forward unchanged from the source snapshot; Tiwa will rule on these in a subsequent session:

- **S-8** (remainder) — difficulty grades + Skill-side modification mechanics (Stakes Gate sub-question already rejected via DEC-051).
- **S-9/S-10** (Extended Tests) — progress-method/failure-behavior forks.
- **S-11** (Rest/Healing) — cost-scaling with wound magnitude (OPEN-007 reference).
- **S-12** (Creature/Campaign content) — content-dependency, individual templates.
- **OPEN-009** (S-6 positive-Effect Active Defense mitigation) — deferred, blocked on undefined S-3 Effect menu scope.
- **OPEN-010** (S-6 repeated-Defense fatigue/exhaustion) — deferred, blocked on nonexistent fatigue system.

S-5 (Armor) itself is now fully ruled across all five identified forks (S5-A–E), with the single exception of Item C above.

---

## 7. Recommended Action Items for OpenCode

1. Assign DEC-numbers (next-available sequence from the live register) to: S5-A, S5-B (consolidated with amendment), S5-C, S5-D (consolidated with amendment/supersession per §3 note), S5-E (consolidated with Zero-Step amendment).
2. Resolve **Item C** (S-3 Effect-menu capacity check for Sunder) against the live S-3 record before finalizing S5-C's menu placement; return to Tiwa if a conflict is found.
3. Resolve **Item A**'s placement question (DEC-007 amendment vs. new Invariant 19) — needs a designer ruling if OpenCode cannot determine this from existing provenance/governance convention alone.
4. Update `PROJECT_CONTEXT.md` / `README.md` currency gaps to reflect S-5 closure (these were already flagged as stale re: S-3 in the source snapshot; S-5 will compound this if not addressed together).
5. Mark the S5-B and S5-D *original* (pre-amendment) rulings as superseded-within-session in the register's history, per §3's notes, rather than recording them as if they were the only version ever ruled.

---

## 8. Governance Notes

This document creates no game mechanics and confers no authority beyond an advisory record. All positions above are **Non-canonical designer rulings**, not Canonical Rules, until OpenCode completes formal recording against the live decision register and — separately, per the Promotion Rule (D3 §21) — until any of this material is proposed for and completes promotion to `canonical/`. Nothing in this report should be treated as satisfying any step of the 8-step Promotion Rule; it satisfies only the "documented as a formal rule" groundwork step insofar as OpenCode chooses to use it as source material for that step.

Per Tiwa's stated intent, remaining S-5-adjacent and other open subsystem decisions will be ruled in a subsequent session, to be cold-started from a fresh task-scoped snapshot per this project's current working method.

*End of report.*
