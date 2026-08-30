---
document:
  title: "Handoff Report and Instructions for OpenCode"
  version: "1.0"
  status: "Formal handoff record — read before touching the repository"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "not yet assessed"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
addressed_to: "OpenCode, or any future agent/session picking up this project"
---

# Handoff Report: Tiwas TTRPG Documentation Project

## 0. Read this first

This repository already has a governance system. **Read these four files before
making any change:**

1. `AGENTS.md` — binding operating rules for any agent working in this repo.
   In particular: no authority inference from recency/chronology/detail; no
   silent resolution of open design forks; no reclassification of documents
   without following the existing promotion process.
2. `governance/authority.md` — the documentation hierarchy (`canonical/` >
   everything else).
3. `governance/status-model.md` — status vocabulary and the 8-step Promotion
   Rule for anything moving toward canonical status.
4. `_consolidation/consolidation-plan.md` — the full account of the original
   consolidation pass, including its explicitly-flagged limitations.

This document supplements those — it does not override them.

## 1. What this project is

Tiwas is a tabletop RPG. Its documentation was originally consolidated (by
Claude Sonnet 5, 2026-08-29) from a single supplied file,
`TTTRPG-merge-v1.md`, into the current repository structure:
`canonical/`, `roadmap/`, `proposals/`, `investigations/`, `governance/`,
`_consolidation/`, `sources/`, `archive/` (currently empty), `audits/`
(currently empty).

That original consolidation was careful and largely self-consistent. It is
**not** the problem. The problem is what it was built from.

## 2. The core situation: the original source corpus was incomplete

`TTTRPG-merge-v1.md` was treated, at the time, as "the project's documentation
corpus." It was not the complete history. It contained only:

- Canonical Rules & Changelog **v1.3** (the current version)
- Implementation Roadmap v1.4.3
- Proposals/WIP v1.4.3
- S-2 Design Investigation **v5 synthesis only**
- S-2 Non-Attack Location Source Closure Record v1.2

Two files have since surfaced that are **not** in that merge file and were
**not** part of the original consolidation's source material:

- `Tiwas_TTRPG___Canonical_Rules___Changelog-v1-2.md`
- `Tiwas_TTRPG___Canonical_Rules___Changelog-v1-1-chatgpt.md`

Both were read and diffed against the in-repo v1.3 this session. Findings:

- **v1.1 → v1.2**: the only substantive change is the locking of S-2 Zero-Step
  (new §14 inserted; Reserved Systems renumbered with one wording carve-out;
  one new changelog entry). Everything else is byte-identical.
- **v1.2 → v1.3**: matches v1.3's own internal changelog exactly, no
  surprises.
- **The corpus's self-reported history is accurate**, as far as it goes — this
  is a positive signal, not a red flag. The problem is coverage, not honesty.

**The unresolved implication:** if two Canonical Rules versions were missing
from what was thought to be "the whole corpus," it is highly likely there is a
larger set of historical project material — earlier drafts, the S-2
Investigation rounds v1–v4, possibly an original pre-v1.1 "Core Rules v1,"
chat exports, or other artifacts — that also never made it into
`TTTRPG-merge-v1.md` and therefore never made it into this repository at all.

**Also unresolved:** whether Claude authored the original project files in
some prior session is a claim made by the human operator that could not be
verified by the Claude session that produced this handoff (no cross-session
memory was available). Treat this as an unverified claim, not a fact, unless
you find independent evidence.

## 3. Specific known gaps (starting list, not exhaustive)

| Missing item | Evidence it exists | Status |
|---|---|---|
| Canonical Rules v1.1 | Uploaded this session, verbatim | **Now have it** — needs filing into `archive/` |
| Canonical Rules v1.2 | Uploaded this session, verbatim | **Now have it** — needs filing into `archive/` |
| Canonical Rules "original v1" (pre-v1.1) | Referenced in v1.3 §17 ("original Tiwas v1 documentation... superseded by Core Rules v2") | Still missing — may or may not be distinct from the v1.1 upload; see open question below |
| S-2 Design Investigation v1–v4 | Referenced explicitly in the v5 synthesis ("consolidates findings from v1–v4") | Still missing |
| Roadmap v1.4.2 (old Phase 2/§9, old S-2 row of §4 only) | Referenced in Roadmap v1.4.3's own supersession note | Still missing |
| Proposals/WIP v1.4.1, v1.4.2 (old §2) | Referenced in Proposals v1.4.3 §22/§23 revision records | Still missing |
| S-2 Non-Attack "Starter Brief v1.1" | Referenced in the Closure Record's own supersession note | Still missing |

**Open question to resolve during your inventory pass:** does the uploaded
"v1.1" file correspond to the "original Tiwas v1 documentation" v1.3
references, or to the intermediate "Core Rules v2" state v1.3 also
references? Its internal changelog already contains both a "Core v1 → Core
v2" entry and an "S-1 v1 → v1.1" entry as resolved history, which suggests it
may already be post-v1 material. Do not guess — flag it in your own inventory
as an open provenance question, consistent with how this repo already treats
unresolved provenance (see `governance/provenance.md`).

## 4. Your task: DO NOT bulk-merge. Inventory first.

The human has a large amount of additional historical project material and
GitHub access, plus a local project folder. **The instruction from this
session is: do not merge old files into the existing repository structure,
and do not create another single merged file like `TTTRPG-merge-v1.md`.**
That pattern is exactly what caused this gap — a merge file was treated as
authoritative and complete when it wasn't.

Instead, follow the same disciplined process the original consolidation
itself used (see `_consolidation/document-inventory.md`,
`_consolidation/relationship-map.md`, `_consolidation/conflict-register.md`,
`_consolidation/decision-register.md` as your templates):

### Step 1 — Staging, not merging

Place all newly-supplied historical files, verbatim and unmodified, into a
clearly separate staging location — do **not** write into `canonical/`,
`roadmap/`, `proposals/`, `investigations/`, or `archive/` yet. Suggested
location: `sources/incoming/` (a new subfolder), so the distinction between
"already-processed source material" (`sources/`, flat) and "newly surfaced,
not-yet-triaged material" (`sources/incoming/`) is visible at a glance.

### Step 2 — Inventory

For every newly-staged file, produce (or extend) an inventory entry in the
same style as `_consolidation/document-inventory.md`: title, version, self-
declared status, what it supersedes/is superseded by, author/LLM provenance
(record `not established` rather than guessing), subject matter, and whether
it contains decisions or requirements.

### Step 3 — Relationship and conflict mapping

Extend `_consolidation/relationship-map.md` and
`_consolidation/conflict-register.md` to show how each newly-found document
relates to what's already in the repo. Specifically check:

- Does anything in the newly-found material **contradict** what's currently
  in `canonical/rules/...v1.3.md`? (It shouldn't, if v1.3 is genuinely the
  current state — but verify, don't assume.)
- Do the S-2 Investigation v1–v4 rounds (if found) change or complicate any
  conclusion the v5 synthesis currently states as settled (e.g., the
  Structural Weak Points State-1→State-2 reclassification, the Armor Bypass
  wording correction)? The v5 synthesis references "corrections applied
  after independent external review" — earlier rounds may contain the
  original claims being corrected, which is useful evidentiary context, not
  a contradiction to flag as urgent.

### Step 4 — Archive properly, only after inventory

Once a document is fully understood (superseded status confirmed, no
unexplained conflicts with canonical material), move it into `archive/` with
an external provenance wrapper header — follow the exact pattern already used
in `investigations/tiwas-s2-non-attack-location-source-closure-record-v1.2.md`
or `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` (metadata
block, `consolidation_note` explaining the placement, substantive content
left verbatim below).

**Do not touch the substantive content of any historical document while
archiving it.** Wrapper headers only.

### Step 5 — Update the registers, not the canonical content

Update `_consolidation/conflict-register.md` (close out item C5 to whatever
extent is now possible), `_consolidation/document-inventory.md`, and
`_consolidation/consolidation-plan.md`'s "known limitations" section to
reflect the fuller picture. **Do not modify `canonical/rules/...v1.3.md`**
unless you find genuine evidence that v1.3 itself is not actually the current
canonical state (which would be a major finding requiring explicit human
confirmation before any action — see `AGENTS.md` §"Repository modification
control").

## 5. Independent review role

Separately from the archival work above: you are also being brought in
specifically to serve as the **independent second-model review** that
`governance/provenance.md` flagged as recommended but not yet performed (the
original consolidation was single-model, single-session, self-assessed). When
you do this review, focus particularly on:

- Whether the original `_consolidation/decision-register.md` Sections A/B
  correctly separate Canonical (§A) from non-canonical-but-real (§B) decisions
- Whether any placement decision in `canonical/`, `roadmap/`, `proposals/`,
  `investigations/` was made on weaker evidence than the corresponding
  document claims
- Whether this handoff report and the accompanying session decision log
  (`session-decision-log-2026-08-29-part2.md`, same directory) are themselves
  accurate against the conversation they summarize, if that conversation
  history is available to you

## 6. What NOT to do

Per `AGENTS.md`, explicitly reiterated here because it's the most likely
failure mode given the volume of new material you're about to process:

- Do not infer canonical status from a document's length, detail,
  confidence, or recency.
- Do not resolve any of the currently-open design forks (OPEN-001 through
  OPEN-005 in `_consolidation/decision-register.md` §C, or any of S-3–S-12)
  as a side effect of organizing historical material. If old material seems
  to answer one of these questions, **surface it as evidence for a human
  decision** — do not treat it as the decision.
- Do not create a new single "mega-merge" file. Keep documents separable and
  individually inventoried, exactly as the existing `sources/` folder already
  does.
- Do not overwrite or delete anything in `canonical/`, `roadmap/`,
  `proposals/`, or `investigations/` without a specific, separately-flagged
  human confirmation, matching the process already used for the original
  `canonical/` placement decision.
