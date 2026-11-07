---
document:
  title: "Project Status Report — Repository State as of 2026-10-26"
  version: "1.0"
  status: "Assessment record — read-only analytical review of repository state. Advisory, non-canonical. No DEC inferred; REQ-021 not invoked; no document's authority status changed."
provenance:
  author_llm: {name: "freebuff-buffy-01 (Buffy, Codebuff)", version: "buffy-codebuff 1.0"}
  assessor_llm: {name: "not established", version: "not established"}
  last_modified_by_llm: {name: "freebuff-buffy-01 (Buffy, Codebuff)", version: "buffy-codebuff 1.0"}
  created_date: "2026-10-26"
  last_modified_date: "2026-10-26"
  scope: >
    Read-only inspection of the repository as it exists on 2026-10-26 (branch
    main, 53 commits): governance model, registers, canonical document,
    consolidation records, git working-tree state, and structural integrity
    checks (referenced paths, register continuity, encoding, local links,
    gitignore coverage). No repository file was modified other than this
    report. This record is review/analysis only: it confers no authority,
    promotes nothing, reclassifies nothing, and resolves nothing.
---

**Author:** freebuff-buffy-01 (Buffy, Codebuff) · **Version:** 1.0 (report
`audits/PROJECT-STATUS-REPORT-2026-10-26.md`) · **Date:** 2026-10-26

---

## 1. Scope and Method

This report records the **current state of the Tiwas TTRPG project
documentation repository** — what the project is, what is complete, what
remains — and the results of a structural verification pass run on 2026-10-26.
It is a read-only analytical activity per `AGENTS.md` ("Analysis versus
action") and requires no special authority.

**Sources consulted (primary, in order of authority):**
`governance/authority.md`, `governance/status-model.md`,
`governance/provenance.md`; `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md`
(internal version v1.4); `_consolidation/` registers (decision, requirement,
conflict, relationship, consolidation-plan); `PROJECT_CONTEXT.md`, `README.md`,
`AGENTS.md`; `audits/` records; `roadmap/` and `proposals/` file inventory; git
history and working-tree state.

**Checks executed (2026-10-26, read-only):** referenced-path checklist (16
targets), local markdown link scan (space-aware, deduped; external URLs
excluded), register ID continuity/duplicate analysis, strict UTF-8 decode of
every `.md` (tool directories excluded), provenance front-matter presence,
`git status`/`git fsck --connectivity-only`/`git rev-list --count`, and
`git check-ignore` coverage tests.

**Explicit non-actions:** no file was edited or moved; no status, authority, or
provenance field was changed on any existing document; no DEC number was
created or inferred; the 8-step Promotion Rule (REQ-021) was **not** invoked;
the external-API script `scripts/lark/test_lark.py` was inspected but **not
run** (it authenticates to a live Lark/Feishu Bitable and writes a record —
an external side effect outside this report's scope).

---

## 2. Executive summary

**The project's documentation foundation is complete and sound; the game
design is complete at the Canonical (locked) level only for the Core engine,
S-1, and the S-2 attack-side invocation policy — everything else exists as
ruled-but-non-canonical design work awaiting the promotion process, and a
large body of content authoring awaits the designer.**

- **Documentation consolidation: COMPLETE.** All three human approval points
  are closed (canonical placement confirmed 2026-08-29; evidentiary gap C5
  accepted as a permanent limitation 2026-08-29; mandatory independent
  second-model assessment completed 2026-08-29 and **approved 2026-08-31**,
  lifting the provisional-for-reliance status). The governance trio, four
  registers, and the audit trail exist and are internally consistent.
- **Canonical/locked design:** the complete Core resolution engine, S-1
  Universal Opposed Contest, and S-2 attack-side invocation policy (DEC-017,
  promoted via the full 8-step rule; canonical document now internal v1.4).
- **Routed-but-not-canonical design:** the decision register carries
  **DEC-001 … DEC-156 with no gaps** across canonical decisions (§A, 18
  rows), non-canonical designer rulings (§B), the formerly-unresolved OPEN
  items (§C, **all ten now closed or superseded**), and the S-3 session
  rulings (§D). S-3 through S-12 subsystem design is largely ruled at the
  non-canonical layer; none of it is locked except DEC-017.
- **Structural verification: PASS** with findings — every referenced path
  exists; registers are gapless and duplicate-free; encoding is clean; git
  connectivity passes. Findings are listed in §6 (unignored copyrighted
  PDFs, 111 untracked entries, 5 broken link targets, two stale index
  documents).
- **Only one governance-level escalation remains open:** the unresolved
  status of the governing specification (`prompts/project-documentation-consolidation-prompt.md`),
  which `AGENTS.md` forbids resolving or classifying — carried forward
  unchanged (§7).

---

## 3. What the project is

Per its own Canonical Rules (§1, quoted in `PROJECT_CONTEXT.md`): Tiwas is a
**high-consequence percentile universal RPG** in which every meaningful
attempt uses one common resolution engine (d100 roll-under, the 100-Fumble
rule, Doubles, a 24-attribute matrix), every test costs resources, failure
generates mechanical growth, and meaningful success changes the tactical or
narrative state. Locked design priorities, in order: granular physical
simulation where warranted; heroic resilience / low permanent character loss;
minimum resolution steps without sacrificing Priority 1.

This repository is the **consolidated project documentation** produced from a
five-document source corpus (D1–D5, supplied 2026-08-29) and governed by its
own authority model. Only `canonical/rules/` is canonical game-mechanics
source; `roadmap/` is implementation/process guidance with explicit "Rule
Authority: None"; `proposals/` is non-canonical design exploration (including
real but non-canonical designer rulings); `investigations/` is evidentiary and
analytical work product; `governance/`, `_consolidation/`, and `audits/` govern
and record the documentation itself (`governance/authority.md`).

---

## 4. Authority and governance state (as established by the repository)

| Element | State | Evidence |
|---|---|---|
| Authority hierarchy | Established, self-consistent across D1–D5 | `governance/authority.md` |
| Status vocabulary + lifecycle + 8-step Promotion Rule | Established (REQ-021 governs every promotion) | `governance/status-model.md`; `_consolidation/requirement-register.md` |
| Provenance model (`author_llm` / `assessor_llm` / `last_modified_by_llm` + dates) | Established and in use across the corpus | `governance/provenance.md` |
| Canonical document | `tiwas-canonical-rules-and-changelog-v1.3.md` — internal **v1.4**, bumped 2026-09-05 at Promotion Step 6 for DEC-017; author provenance "not established" (source document, correctly preserved) | canonical file front matter, lines 17–29 |
| Canonical decisions | DEC-001 … DEC-017 (+ DEC-007.A) = 18 rows in register §A | `_consolidation/decision-register.md` §A |
| Non-canonical designer rulings | Register §B, DEC-018 … DEC-156 territory (annotated with advisory storage records) | register §B |
| Formerly-unresolved items | **All ten (OPEN-001 … OPEN-010) closed or superseded** via DEC-035/037/038/040/041/042/050/075/076/077, with DEC-135 superseding OPEN-010 | register §C |
| Requirements | REQ-001 … REQ-025, gapless, no duplicate rows; no contradictory pair found | requirement register |
| Conflicts | C1–C3 resolved in the corpus itself and recorded (not re-litigated); C5 closed 2026-08-29 as an accepted permanent limitation | `conflict-register.md`; consolidation-plan |
| Consolidation approval gates | All three human approval points CLOSED | consolidation-plan "Human approval points" |
| Independent second-model assessment | Completed 2026-08-29 (`audits/INDEPENDENT-ASSESSMENT-2026-08-29.md`, nemotron-3-super-120b, fresh session), **approved by the human 2026-08-31**; assessors appended per §4.4 | provenance.md; consolidation-plan |

Nothing in this table was changed by this report; it is a transcription of
existing records.

---

## 5. Completion status

### 5.1 Documentation layer — COMPLETE

The consolidation is finished and gated: corpus split and reorganized
verbatim, governance authored, registers built, approval points closed,
independent assessment approved. `archive/` is intentionally empty (C5 closed
as a permanent limitation — recovery only via a future designer ruling).
The repository — not conversational context — is the designated persistent
project memory (consolidation-plan, "Recommended future maintenance process"
§5). The corpus has since accumulated 53 commits of stewardship (decision
recording, playtest storage, advisory intakes) through `9e4bf7f`.

### 5.2 Locked (Canonical) game design — a deliberate minority

- The **complete Core resolution engine**: d100 handling, 100-Fumble,
  Doubles, 24-attribute matrix, derived statistics, Skills (Tier/Cap/Starting
  Value), the 9-step Core Test Transaction, resource cost/Overflow, Recovery,
  Failure XP, Skill Roll Pool, General XP, Advanced Skills — plus the 18 Core
  architectural invariants (REQ-001 … REQ-018 / DEC-016 / Canonical §16).
- **S-1 Universal Opposed Contest** — fully locked (Margin/Blackjack/Hybrid).
- **S-2 attack-side invocation policy** — locked as Canonical §14.7 via
  DEC-017's completed 8-step promotion (2026-09-05; source material marked,
  changelog updated — the file's own promotion record at lines 29+).

### 5.3 Routed but NOT canonical — the bulk of current work

Per `governance/status-model.md`, promotion requires the full 8-step rule;
detail does not confer authority. As recorded in the register, designer
rulings now exist (non-canonical) for: **S-3** Effect menu and content
enumeration (DEC-023/023.A/024.A/025–031), **S-4** Wounds (DEC-032–037,
amended DEC-035.A/107/115), **S-5** Armor (DEC-058–062), **S-6** Defense
(DEC-044–050, DEC-075, DEC-135), **S-7** Incapacitation/Death (DEC-052–057),
**S-8** Difficulty (DEC-063–066; Stakes Gate rejected DEC-051), **S-9/S-10**
Extended Tests (DEC-067–070), **S-11** Rest/Healing (DEC-071–074), **S-12**
Creature/Campaign (DEC-076–077), **Encumbrance** (DEC-078 + R1/R2/R3),
**Conditions** alpha vocabulary (DEC-079/079.A), **Tags** ontology
(DEC-080/114), **Equipment** (DEC-081/118/129), **unified Effect/Condition
schema** (DEC-115/116/117/121/127), **location anatomy** (DEC-100/136/137/
139/144), and **Magic subsystem design questions** (DEC-146, Q-M1–Q-M10,
implementation still Reserved). The **S-2 non-attack deferral** remains a
binding non-canonical ruling. Ten L-004 creature-template content candidates
are stored as advisory authoring work (DEC-077/077.A track).

**Promotion is the mechanism that converts any of this into locked rules**
(REQ-021); the roadmap's promotion-backlog stream (GDD orchestration plan
v0.3) is where that work is sequenced. Nothing else has been promoted.

### 5.4 Explicitly still open (design layer)

- Everything Canonical-side beyond §5.2: the broader S-2 architecture
  (Tier-selection policy as a *scene* matter is closed via DEC-040, but
  anatomical-mapping content and Tier-2+ procedure content continue under
  DEC-041/042), Conditions-adjacent content authoring, plus Time/Action,
  Equipment content, Hazards, Magic/Special Abilities implementation
  (Reserved — canonical §15 / DEC-015 design direction only), and Setting
  Modules (`PROJECT_CONTEXT.md` "not yet built" list).
- Inline open questions tracked per DEC row (examples, not exhaustive):
  the DEC-100-quartile-vs-bespoke Tier-1 fork for creature templates (Giant
  Spider and kin) and the per-creature §6 questions awaiting Tiwa
  (2026-09-20 advisory report; C1 Tier-2+ copy-permission gap unruled);
  DEC-122 Items 2–4 pending; DEC-078's band re-anchoring question left open
  for the designer; DEC-081 §1 amendment Q1 open; the starter `magic:`/
  `ability:` vocabulary authorization deferred (Q-M7); S-8 difficulty grades
  and Skill-side modification (DEC-051 note).
- Process requirements in force on all future work: REQ-019 (Phase 0
  regression suite), REQ-020 (roadmap may not decide numbers), REQ-021
  (promotion), REQ-022 (no silent resolution of designer forks), REQ-023
  (documentation maintenance rule), REQ-024/025 (evidentiary-scope labels).

---

## 6. Verification results and findings (2026-10-26)

### 6.1 Checks that PASSED

| Check | Result |
|---|---|
| Referenced-path checklist (governance ×3, registers ×4, prompts spec, canonical rules, PROJECT_CONTEXT, archive/README, consolidation-plan, 4 directories) | **16/16 exist** |
| Decision register continuity | **DEC-001…DEC-156, no gaps; no duplicate base rows** (15 legitimate `.A`-style sub-rows; apparent dupes DEC-007/035/072/077/079 are sub-rows) |
| Requirement register | REQ-001…REQ-025 complete, no duplicates |
| Conflict register | Content present (C1–C5 heading scheme) with full provenance front matter |
| Encoding | **0** `.md` files fail strict UTF-8 decoding |
| Provenance front matter | Present on governance trio, canonical rules, decision/requirement registers (and the other consolidation files) |
| Git integrity | Branch `main`, **0 modified tracked files**, no stashes; `git fsck --connectivity-only` exit 0 (one benign dangling tree) |

### 6.2 Findings (recorded, not resolved — no change made)

| ID | Finding | Evidence | Consequence |
|---|---|---|---|
| F-1 | **Copyright-protection gap in `.gitignore`.** The ignore file blocks only `Beyond-the-Vale-of-Madness-GURPS.pdf` (line 5) with a comment forbidding committing third-party copyrighted material, but `DnD - Basic Rules Boxed Set Adventure.pdf`, `website - xiaomi1.pdf`, and the GURPS text conversions (`Beyond-the-Vale-of-Madness-GURPS.md`, its conversion report) are untracked and **not ignored** (`git check-ignore` negative) | `git status --porcelain`; `git check-ignore -v` | One `git add -A` would commit exactly what the repository forbids. **Human question:** extend `.gitignore` to cover these files? (Modification not performed — outside this report's authorised scope.) |
| F-2 | **111 untracked entries** (tracked side clean): playtest reports, `investigations/` harness scripts (incl. `run_playtest.py`), GURPS conversion documents, `desktop.ini`, `.freebuff/`, this report's siblings | `git status` | Large uncommitted surface; intake decision required (which files belong in the corpus?). **Human question:** what should an intake commit include? Per `AGENTS.md`, modification scope needs explicit authorisation — nothing staged or committed. |
| F-3 | **77 broken local-link references across 5 distinct targets:** `Prompt - tag condition effect unification1.md` (×52) and `Beyond-the-Vale-of-Madness-GURPS.pdf` (×21) linked from `investigations/` without `../` (both exist at repo root); a bare UUID `4e6fd18b-2dcb-4da5-8418-172c52657ace` (×2, in `merged-combat-reports-playtest1.md`); `quality_vs_skill.png` and `quality_vs_skill_corrected.png` (×1 each, `sources/incoming/tiwas-tttrpg-merge/`) | link scan (space-aware; external URLs excluded) | Navigation breaks for readers/tools that resolve links relative to the containing file. **Recommendation:** add `../` prefixes / remove the dead UUID references / note the missing images — a modification needing authorisation. |
| F-4 | **`audits/README.md` is stale.** It states audits are "Empty (`current/` and `historical/`)" and the independent second-model assessment is "**Pending**", but the assessment file exists in this directory and was approved by the human 2026-08-31 (recorded in `governance/provenance.md` and consolidation-plan) | audits/README vs provenance.md / consolidation-plan | A reader could wrongly conclude the repository is still provisional-for-reliance. Maintenance item under REQ-023. |
| F-5 | **`PROJECT_CONTEXT.md` snapshot is stale (last_modified 2026-08-31).** Its "active non-canonical development" section describes only the two S-2 rulings, and its "not yet built" list predates the S-3…S-12 ruling waves now recorded through DEC-156 (register last annotations 2026-09-20). Likewise `governance/status-model.md`'s sentence "No item currently in `proposals/` or `investigations/` … has completed this process" predates DEC-017's 2026-09-05 promotion | file dates; register contents | Orientation documents understate how much design work is ruled (while correctly stating what is *locked*). Maintenance item under REQ-023 — update the snapshots **without promoting anything**. |
| F-6 | **Unresolved governing specification (carried forward, NOT resolved here).** `AGENTS.md` fixes the status of `prompts/project-documentation-consolidation-prompt.md` as unresolved: do not resolve, classify, or reconstruct it; escalate if it becomes operationally relevant | `AGENTS.md` §"Unresolved governing specification" | Remains open by governance. This report deliberately makes no finding on it. |
| F-7 | Canonical filename says **v1.3** while the document's internal version is **v1.4** (intentional: bumped at Promotion Step 6, file note at line 29) | canonical front matter | Observation only — consistent with its own promotion record; noted so a future reader does not mistake it for drift. |
| F-8 | `scripts/lark/test_lark.py` is named "test" but is an external-service writer (Lark Bitable, requires `LARK_APP_ID`/`LARK_APP_SECRET`); not run | script source | If a test runner is ever pointed at the repository root it would collect this file. Noted; no change made. |

---

## 7. Unresolved issues and escalations (summary)

1. **Governing specification status** (F-6) — unresolved by design; escalate
   to the human only if it becomes operationally relevant. Not classified here.
2. **Repository hygiene decisions** (F-1, F-2, F-3) — each requires a human
   direction before any modification; presented as questions, not actions.
3. **Documentation-maintenance backlog** (F-4, F-5) — REQ-023 upkeep of the
   orientation documents against the live register.
4. **Design-layer open questions** (§5.4) — awaiting Tiwa; none may be
   resolved by an LLM (REQ-022).
5. **No consolidation-layer gate remains open** — all three human approval
   points and the independent-assessment gate are closed (§4).

---

## 8. Work still required (ordered)

1. **Designer rulings** on the inline open questions (§5.4) — creature-
   template §6 questions, DEC-122 Items 2–4, DEC-078 band re-anchoring,
   DEC-081 amendment Q1, S-8 difficulty grades, Q-M7 magic vocabulary.
2. **Promotion work** — route locked-eligible material through the 8-step
   Rule (REQ-021) via the roadmap's promotion-backlog stream; update the
   Canonical changelog at Step 6 as DEC-017 did.
3. **Magic/Special Abilities subsystem** — remains Reserved; implementation
   only with explicit designer authorisation (DEC-014 R3 vocabulary pending).
4. **Documentation maintenance (REQ-023)** — F-4, F-5 updates.
5. **Repository hygiene (human-authorised)** — F-1 gitignore extension,
   F-2 intake triage/commit, F-3 link repairs.
6. **Content authoring** — L-004 template family and further DEC-077/077.A
   work, per the register's authorisation postures (none of it canonical).

---

## 9. Decisions and conclusions

- **Decisions made by this report: none.** No DEC number was assigned, no
  status was promoted, demoted, or reclassified, no authority field was
  edited. Everything asserted here is either (a) transcribed from the
  repository's own records with the source named, or (b) a structural
  measurement executed on 2026-10-26.
- **Conclusion 1:** the documentation/governance layer is **complete and
  healthy** — the consolidation's gates are all closed, registers are
  gapless, encoding and provenance discipline hold, and git integrity passes.
- **Conclusion 2:** the design layer is **intentionally incomplete**: a small
  locked core (§5.2), a large ruled-but-non-canonical body (§5.3), and open
  designer questions (§5.4). That distribution is the governance model
  working as written, not a defect.
- **Conclusion 3:** the concrete remaining risks are repository hygiene
  (F-1/F-2/F-3) and orientation-document staleness (F-4/F-5) — all narrow,
  mechanical, and addressable once authorised.
- **Limitations of this report:** point-in-time (2026-10-26); content-level
  claims about individual rulings were taken from the registers and not
  re-litigated against every source document; the link scan covers local
  relative links only; per `governance/provenance.md`, an assessment does not
  confer authority — this record is review, not a human decision.

---

*Filed under `audits/` as an assessment record, advisory and non-canonical,
per `audits/README.md` and `governance/provenance.md`. Author:
freebuff-buffy-01 (Buffy, Codebuff), version buffy-codebuff 1.0, 2026-10-26.*
