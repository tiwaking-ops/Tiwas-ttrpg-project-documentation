---
document:
  title: "Session Decision Log — Continuation Session (Part 2)"
  version: "1.0"
  status: "Consolidation working record (not canonical)"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "not yet assessed — pending OpenCode review"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
session_context: >
  This is a continuation of the initial consolidation session (also 2026-08-29,
  same date, same model) that produced the repository structure described in
  _consolidation/consolidation-plan.md. This log covers decisions made in the
  follow-up conversation, after the initial consolidation was already complete
  and synced to GitHub.
---

# Session Decision Log — Continuation Session

## 1. Human approval points from the original consolidation — resolved

Per `_consolidation/consolidation-plan.md`, three items were flagged for human
approval. Status after this session:

| # | Item | Resolution |
|---|---|---|
| 1 | Canonical placement of `tiwas-canonical-rules-and-changelog-v1.3.md` | **APPROVED.** Human confirmed this document and its lineage have been the sole canonical document since the project was formalized during development. No change to repository structure needed — the existing placement in `canonical/rules/` stands. |
| 2 | Whether to pursue missing prior-version documents for `archive/` | **JOINT SEARCH INITIATED**, then **ESCALATED** — see §3 below. Not resolved; status changed from "flagged gap" to "active, ongoing, and now understood to be larger than originally scoped." |
| 3 | Whether a second model/session should independently assess the consolidation | **DEFERRED TO EXTERNAL REVIEW.** Human is bringing in OpenCode (separate model/session) to perform this. No independent review was performed by this session itself. |

## 2. Design decisions — explicitly parked, not resolved

The following substantive (non-documentation-process) design questions were
raised and explicitly deferred by the human, not resolved:

- OPEN-001 (H0 Rider B's unadjudicated sub-options)
- OPEN-002 (scene/campaign Location Tier selection policy)
- S-3 through S-12 (all remaining open subsystems)
- The S-2 non-attack Location Index deferral's reopening trigger

**No ruling was made on any of these.** They remain exactly as recorded in
`_consolidation/decision-register.md` §C and in `proposals/`/`investigations/`.
This is a deliberate non-decision per Roadmap §24 Rule 6 ("never silently
resolve an open designer fork") — recorded here so a future session does not
mistake "not discussed" for "resolved."

## 3. Critical discovery: the original source corpus was incomplete

### What happened

The human supplied two files for upload:
- `Tiwas_TTRPG___Canonical_Rules___Changelog-v1-2.md`
- `Tiwas_TTRPG___Canonical_Rules___Changelog-v1-1-chatgpt.md`

These were offered as material believed to already exist inside
`TTTRPG-merge-v1.md` (the original source corpus for the entire consolidation).

**On inspection, this was false.** `sources/SOURCE_CORPUS_ORIGINAL_TTTRPG-merge-v1.md`
contains exactly five embedded documents:
1. Canonical Rules & Changelog **v1.3 only** (no v1.1, no v1.2)
2. Implementation Roadmap v1.4.3
3. Proposals/WIP v1.4.3
4. S-2 Hit Location Investigation **v5 synthesis only** (no v1–v4)
5. S-2 Non-Attack Location Source Closure Record v1.2

Both uploaded files (Canonical Rules v1.1 and v1.2) are **genuinely new
evidence**, not previously-supplied material that had been mishandled. The
same is true, by clear implication, of S-2 Design Investigation rounds v1–v4,
which remain entirely unaccounted for.

### Why this matters

The entire original consolidation (`_consolidation/`, and the resulting
`canonical/`, `roadmap/`, `proposals/`, `investigations/` structure) was built
from `TTTRPG-merge-v1.md` as if it were the complete project history. It was
not. It was **one snapshot/export that happened to omit** at least:

- Canonical Rules v1.1 (and possibly an even earlier "v1")
- Canonical Rules v1.2
- S-2 Design Investigation v1, v2, v3, v4
- Possibly other material not yet identified

This was **not fabrication** — the original consolidation's own
`conflict-register.md` item C5 and `archive/README.md` explicitly and
correctly flagged all of this as "referenced but not supplied" from the very
first pass. The gap was known and disclosed; what changed is that it's now
confirmed larger than a few footnoted references, and primary source material
to fill some of it now exists.

### What was verified this session

Both uploaded files were read in full and diffed against the in-repo v1.3:

**v1.1 → v1.2 (uploaded files, diffed against each other):**
- Only substantive change: locking of S-2 Zero-Step (new §14 "S-2 — Tier-1
  Location Index Provider" inserted; old §14 Reserved Systems renumbered to
  §15 with one wording carve-out for the new exception; new "S-2 v1.1 → v1.2"
  changelog entry added).
- Everything else (Core dice, attribute matrix, derived stats, skills, Core
  Test Transaction, Overflow, Recovery, Failure XP, Skill Roll Pool, General
  XP, Advanced Skills, S-1 in full) is byte-identical between the two.

**v1.2 (uploaded) → v1.3 (in repo):**
- Matches v1.3's own §17 changelog exactly. §14.5 (E9 record) reworded with
  explicit evidence-class labeling; new §14.6 (comparative derivation-cost
  residual) added; new "S-2 documentation reconciliation v1.3" changelog entry.
- **No inconsistency found.** The corpus's self-reported history checks out
  end-to-end against actual prior-version text, for the first time since this
  project's documentation was consolidated.

**Provenance anomaly flagged, not resolved:**
- The v1.1 upload has no in-document "Document Version" field (unlike v1.2 and
  v1.3, both of which have one) and its own internal changelog already
  contains both "Core v1 → Core v2" and "S-1 v1 → v1.1" as resolved history.
  This suggests it may be functionally "Core Rules v2 + S-1 v1.1" rather than
  a pristine original "v1" — i.e., it may be the document v1.3's own changelog
  calls "Core Rules v2," not the "original Tiwas v1 documentation" that v1.3
  separately references as superseded by Core Rules v2.
- The filename suffix `-chatgpt` suggests different tooling/session provenance
  than the rest of the corpus (recorded elsewhere as "not established").
- **This is recorded as an open uncertainty, not a conclusion.** Per this
  project's own evidentiary standards (`AGENTS.md`), missing historical
  material must not be reconstructed as fact.

### A claim that was raised and could not be verified

The human stated, in effect, that this assistant (Claude) was "the creator of
the original project files for this project." This session's assistant
instance has no persistent memory across sessions and could neither confirm
nor deny this claim. It is recorded here as **stated by the human, unverified
by the assistant**, and should not be treated as an established fact by any
future session without independent evidence.

## 4. Decisions on how to proceed

- **No re-consolidation from scratch.** The existing `canonical/`, `roadmap/`,
  `proposals/`, `investigations/` structure remains valid for the material it
  already covers. The gap is in *historical completeness*, not in the
  correctness of what was already processed.
- **The human will use OpenCode** (a separate, free-tier tool with local
  project folder + GitHub access) to organize the larger set of historical
  project documents that exist outside `TTTRPG-merge-v1.md`.
- **This assistant did not perform that organization work** due to session
  token constraints. Two handoff documents were produced instead: this log,
  and a separate situation report/instruction document for OpenCode (see
  `opencode-handoff-report.md`, same directory).
- **The two uploaded files (v1.1, v1.2) were read and diffed but not yet
  written into `archive/`** — that action is deferred to the OpenCode handoff
  so it happens as part of one coherent pass rather than a partial one here.

## 5. Summary of repository state as of this session

| Area | Status |
|---|---|
| `canonical/rules/...v1.3.md` | Confirmed sole canonical document; placement approved by human |
| `roadmap/`, `proposals/`, `investigations/` | Unchanged, still valid for what they cover |
| `_consolidation/conflict-register.md` C5 | Still open; now known to be a larger gap than originally scoped |
| `archive/` | Still empty; two new candidate files identified (v1.1, v1.2 Canonical Rules) but not yet filed |
| Independent review (Section 23.2/§21 process, `governance/provenance.md`) | Not yet performed; assigned to OpenCode |
| S-3 designer rulings (DEC-023–030) and their two investigation threads | Untouched by this session |
