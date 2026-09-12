---
document:
  title: "Session Report — Reaction Trigger Taxonomy & Tag Vocabulary Content-Authoring (DEC-132/132.A Content Closure)"
  version: "1.0"
  status: "Advisory / Non-canonical. No DEC assigned by this report. Recording authority rests with OpenCode per its designated documentarian role; ruling authority rests exclusively with Tiwa."
provenance:
  author_llm:
    name: "Claude Sonnet 5"
    version: "claude-sonnet-5"
  assessor_llm: []
  last_modified_by_llm:
    name: "Claude Sonnet 5"
    version: "claude-sonnet-5"
  created_date: "2026-09-13"
  last_modified_date: "2026-09-13"
---

# Session Report — Reaction Trigger Taxonomy & Tag Vocabulary Content-Authoring

**Author (LLM name / version):** Claude Sonnet 5 / `claude-sonnet-5`
**Session date:** 2026-09-13
**Scope:** DEC-132.A(R1) content-authoring closure — reaction trigger taxonomy and
`reaction:` Tag vocabulary.
**Authority statement:** This report is advisory only. It records what occurred in this
session and what was produced. It does not itself rule, promote, or lock anything. No DEC
is assigned or inferred by this document. Per standing governance, Claude operates in a
strictly advisory capacity in this project; Tiwa holds exclusive ruling authority; OpenCode
is the designated documentarian and records formally after Tiwa's approval.

---

## 1. Purpose of This Report

To give OpenCode a complete, self-contained account of this session's work so it can be
formally recorded, cross-referenced, and — if and when Tiwa directs — folded into the live
decision register. This report does not replace the two work-product documents it
describes (§4); it summarizes them and the session's decision trail.

---

## 2. Background / Triggering Context

DEC-132 (2026-09-07) established the Reactions-beyond-Active-Defense framework and left
four items carried open. DEC-132.A (2026-09-10) closed all four, including (R1) the
trigger-taxonomy question — ruling that reaction triggers use a **category-level
taxonomy** (not a flat trigger list) and that exact trigger menus and the reaction-granting
Tag vocabulary remain **content-authoring (DEC-077.A)**, not a framework-level ruling.

This session's work is that content-authoring task: producing the concrete taxonomy and
Tag vocabulary DEC-132.A(R1) deferred.

---

## 3. Session Narrative (chronological)

### 3.1 Initial advisory discussion

The session opened with a request for advice on solving the reaction trigger
menus/Tag-vocabulary content gap. Claude:

- Restated the binding constraints already fixed by DEC-132/DEC-132.A (Tag-gating,
  full-S-1-exchange resolution, no new action economy, category-level taxonomy, AD/Reaction
  independence, uncapped frequency, DEC-025's Skill/Tag prohibition, DEC-080's open
  namespace model, DEC-116's vocabulary-only Tag default).
- Surveyed comparative TTRPG precedent (Pathfinder 2e named-trigger reactions, D&D 5e's
  single hard-coded Opportunity Attack trigger as a negative example, Shadowrun interrupt
  actions, GURPS All-Out-Defense/retreat triggers) to inform category coverage, consistent
  with this project's standing comparative-research practice.
- Proposed a draft four-category taxonomy (movement-trigger, ally-targeted-trigger,
  HP/state-threshold-trigger, and a fourth candidate — declared-action-trigger, modeled on
  Shadowrun-style interrupts) plus a draft starter Tag vocabulary, and raised four explicit
  open questions for Tiwa, including whether to adopt the fourth category, which namespace
  to use, what Tag grain to use, and whether to rename DEC-132's own `combat:vigilant`
  example.

**Nothing in §3.1 was recorded as a ruling.** It was a menu of options and a request for
direction, per standing advisory practice.

### 3.2 Tiwa's decisions

Tiwa answered all four open questions directly, each with a stated reason:

| # | Decision | Reason (Tiwa, verbatim) |
|---|---|---|
| 1 | Reject the declared-action-trigger category | "Adds complexity to decision making." |
| 2 | Use a new `reaction:` namespace (not an extension of `combat:`) | "Can use them in non-combat situations." |
| 3 | One Tag per category (coarse grain) | "This may expand in the future." |
| 4 | Approve renaming `combat:vigilant` → `reaction:vigilant` | (approved without further comment) |

These four decisions were treated by Claude as authoritative direction for the
content-authoring pass that followed. They are recorded here as **Tiwa's stated
decisions within this session** — per standing practice, formal DEC-numbering and
canonical/non-canonical status assignment is OpenCode's/the register's prerogative, not
self-assigned by this report.

### 3.3 Full options brief drafted and stored

Claude produced a complete options brief incorporating all four decisions:
`tiwas-reaction-trigger-tag-vocabulary-options-brief-2026-09-13.md` (see §4.1). Key
content:

- **Three-category taxonomy** (movement-trigger, ally-targeted-trigger,
  HP/state-threshold-trigger), each given both a combat-framed and a non-combat-framed
  worked example, consistent with Decision #2's stated non-combat-usability rationale.
- **Three-entry `reaction:` Tag vocabulary** (`reaction:vigilant`, `reaction:guardian`,
  `reaction:opportunist`), one per category per Decision #3, all vocabulary-only per
  DEC-116 (no Tier/Magnitude fields).
- **A flagged scope tension**, surfaced by Claude, not resolved by Claude: DEC-132(2)(c)'s
  own text specifies a Reaction resolves as a "full S-1 **combat** exchange," which is in
  tension with Decision #2's non-combat rationale. The brief proceeds on the working
  assumption that S-1 (DEC-013) is the universal opposed-contest primitive and therefore
  usable outside combat, but explicitly does not treat that assumption as settled — it is
  listed as Open Item 1 requiring Tiwa's explicit confirmation.
- **A worked example** (a guard with two of the three Tags) demonstrating category firing,
  AD/Reaction independence (DEC-132.A R2), and uncapped frequency (DEC-132.A R3) together.
- **A cross-check table** against DEC-025, DEC-115/116/117, DEC-132.A(R1/R2/R3), DEC-082,
  Invariant 17, and DEC-077.A — no conflicts found.
- **Three open items** left explicitly unresolved for Tiwa (the scope-tension
  confirmation; per-creature/per-class trigger wording beyond the worked examples; whether
  the three Tag names are final or placeholders).

No DEC was assigned by Claude to any part of this brief. It is explicitly labeled
content-authoring advisory material pending Tiwa's review, parallel in status to the prior
DEC-112 L-009/L-010 Human Location Template proposal pattern (advisory draft → Tiwa
accepts/edits/rejects → OpenCode records).

---

## 4. Deliverables Produced This Session

### 4.1 Options brief

| Field | Value |
|---|---|
| Filename | `tiwas-reaction-trigger-tag-vocabulary-options-brief-2026-09-13.md` |
| Author | Claude Sonnet 5 (`claude-sonnet-5`) |
| Status | Advisory / non-canonical / no DEC assigned |
| Location | `/mnt/user-data/outputs/` (session output; not yet in the live repository) |
| Summary | Full options brief: three-category trigger taxonomy, three-entry `reaction:` Tag vocabulary, worked example, invariant/DEC cross-checks, three open items |

### 4.2 This report

| Field | Value |
|---|---|
| Filename | `tiwas-reaction-trigger-tag-vocabulary-session-report-2026-09-13.md` (this document) |
| Author | Claude Sonnet 5 (`claude-sonnet-5`) |
| Status | Advisory / non-canonical / no DEC assigned |
| Location | `/mnt/user-data/outputs/` (session output; not yet in the live repository) |

---

## 5. What This Session Did NOT Do

Per standing governance discipline (advisory/ruling separation is absolute), this report
explicitly notes the following were **not** done and require separate, explicit action:

- **No DEC number was assigned** to Tiwa's four decisions (§3.2) or to the taxonomy/Tag
  content (§3.3). If Tiwa wants these recorded as a formal DEC (e.g., as a DEC-132.B
  amendment closing DEC-132.A(R1)'s content-authoring deferral), that is a distinct,
  explicit instruction to OpenCode, not inferred by this report.
- **No canonical status change occurred.** Nothing here touches the Canonical Rules &
  Changelog; the entire subject matter (Reactions, DEC-132/132.A) remains non-canonical.
- **The scope-tension flag (§3.3) was not resolved.** Whether Reactions fire on any S-1
  exchange or combat exchanges only remains an open question, not a default.
- **No per-creature/per-class trigger content was authored.** Only the taxonomy layer and
  the three Tag names exist; concrete trigger wording for any specific creature, class, or
  item remains a separate DEC-077.A authoring pass.

---

## 6. Required OpenCode Actions (if Tiwa directs recording)

1. Confirm whether Tiwa wants the four §3.2 decisions and/or the §3.3 taxonomy/Tag content
   entered into the live decision register, and under what DEC number/designation.
2. If recorded, cross-reference against DEC-132 and DEC-132.A in the register (as an
   amendment or a new content-closure entry, per the existing DEC-135.A / DEC-081.A /
   DEC-082.A amendment-row precedent).
3. Confirm the scope-tension flag (§3.3, Open Item 1) is carried forward as an explicit
   open item, not silently resolved by recording.
4. File both deliverables (§4.1, this report) under the appropriate `investigations/` or
   `proposals/` path per the existing repository structure, per Tiwa's placement
   preference.

---

## 7. Reconfirmation Checklist for Tiwa

- [ ] Confirm the four decisions in §3.2 as recorded (no changes)
- [ ] Confirm or reject the three-category taxonomy in §3.3 / the brief
- [ ] Confirm or reject the three `reaction:` Tag names
- [ ] Resolve Open Item 1 (combat-only vs. universal S-1 scope for Reactions)
- [ ] Direct OpenCode on DEC numbering / recording, or hold as advisory-only for now

---

## 8. Authority Statement (restated)

This report and the options brief it describes are advisory work product only. Claude does
not rule, assign DEC numbers, or record canonical or non-canonical decisions. All content
above is presented for Tiwa's review and, where applicable, OpenCode's formal recording
following Tiwa's explicit direction.
