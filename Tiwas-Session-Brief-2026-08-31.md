# Tiwas-TTRPG — Curated Session Brief (2026-08-31)

**Type:** Dated, task-scoped SNAPSHOT for a cold-reading advisory model. Not part of the project corpus.
**Compiled by:** OpenCode (documentarian), with live repository access, 2026-08-31.
**For:** ChatGPT (advisory design assistant). No memory of prior sessions. No repository access while this file is
loaded.
**Usage:** Tiwa uploads this file; ChatGPT reads it cold and gives **advisory opinions only** on the Open decisions
below. Tiwa verifies anything it acts on against the real repository, separately, with OpenCode.
**Purpose:** Enough context that ChatGPT can state, for every currently-Open decision in the live decision register,
(a) what is ruled/locked upstream, (b) what forks remain open, and (c) what governance rules constrain any future
ruling — plus the repository's actual formal-reporting/provenance standard so any document ChatGPT produces in the
session conforms to it on the first attempt.

> **STATUS — THIS FILE SUPERSEDES NOTHING.**
> This is a dated, task-scoped working snapshot, **not** the authoritative corpus, and it does not claim to be
> complete or current beyond this session. The repository itself (`canonical/`, `proposals/`, `roadmap/`,
> `investigations/`, `governance/`, `_consolidation/`) is the only authoritative source. Every claim below carries a
> repo path so it can be verified. Design material in this file is **non-canonical** unless explicitly labelled
> Canonical/Locked.

**Explicit one-session overrule on record.**
The standing handoff prohibition `sources/incoming/opencode-handoff-report.md` §6 — *"Do not create a new single
'mega-merge' file. Keep documents separable and individually inventoried"* — is **explicitly overruled by the human
designer (Tiwa) for this single task (2026-08-31)** so a cold-reading model can receive one self-contained,
curated brief. This is a **one-session exception**: it does not repeal the standing prohibition generally, does not
reinstate any prior consolidated merge file (e.g. `TTTRPG-merge-v2.md`) as a standing artifact, and generating this
file establishes no precedent that another merged file may be created. This file is disposable working material; it
may be deleted after use and is not a repository artifact.

**Pointers, not inline evidence.**
Items hash-indexed as evidence (per-decision handoff reports, raw survey transcripts, full investigation threads)
are **pointer-referenced** (path + one-line status) and **not reproduced inline**, per the standing
evidence-preservation rule. Do not treat a pointer as a copy of the referenced content.

---

## 1. Authority model and how to read status

### 1.1 Authority hierarchy (verbatim summary of `governance/authority.md`)

| Layer | Role | Authority |
|---|---|---|
| `canonical/` (D1) | Canonical Rules & Changelog | Sole source of **locked** game mechanics. Cannot be overridden by lower layers. |
| `roadmap/` (D2) | Implementation Roadmap & Project Governance | Implementation guidance only. "Rule Authority: None." Does not create mechanics. |
| `proposals/` (D3) | Proposals, WIP & Design Direction | Non-canonical design repository. Contains real designer rulings governing candidate, non-canonical material. |
| `investigations/` (D4, D5) | Design investigations feeding Proposals/WIP | Evidentiary/analytical work product. **Never self-executing**; requires designer/human ruling to affect even the non-canonical layer. |

Only material with clear evidence of Canonical status per D1 sits in `canonical/`. No promotion beyond what the
corpus itself documents has been performed by the consolidation.

### 1.2 Status vocabulary (from `governance/status-model.md` §"Status vocabulary")

- **Canonical / Locked** — authoritative, current, must not be contradicted by downstream design/implementation.
- **Reserved** — a known required subsystem with no settled implementation yet.
- **Historical / Superseded** — retained for understanding, no longer current.

Additional Proposals/WIP vocabulary (D3 §0): **Proposed** (candidate under active consideration), **WIP** (being
developed/reviewed), **Experimental** (tested/invented for exploration but excluded from the ruleset), **Design
Direction** (architectural/philosophical preference, not necessarily a mechanic), **Reserved**, **Superseded**.
None of Proposed / WIP / Experimental / Design Direction / Reserved / "observation" is a locked rule.

### 1.3 Evidence classes (from `governance/status-model.md`, D2 §23.2 / D3)

- **Mechanical fact** — directly follows from existing locked rules.
- **Empirical finding** — supported by simulation, playtesting, or other explicit evidence.
- **Designer ruling** — a deliberate choice not mathematically forced by the system.
- **Recommendation** — a proposed preference not yet accepted.
- **Architectural constraint** — governs how systems interact, not what a mechanic numerically does.

An empirical finding does not itself establish a designer ruling. An architectural constraint does not establish a
numerical mechanic. Evidence must be recorded with its scope and limitations.

### 1.4 Promotion Rule — the only path from non-canonical to canonical (D3 §21 / status-model.md §"Promotion Rule")

1. The design question is explicitly identified.
2. Competing alternatives have been considered where appropriate.
3. Relevant simulation/analysis has been completed.
4. The human designer has accepted the ruling.
5. The mechanic is documented as a formal rule.
6. The Canonical Rules & Changelog document is updated.
7. The former proposal is marked Superseded or Locked in its source document.
8. Implementation documentation is updated.

No item currently in `proposals/` or `investigations/` has completed this process. **A designer ruling is a
non-canonical designer ruling (e.g. DEC-023–DEC-043) — it governs candidate material only and is NOT canonical.**

### 1.5 LLM Governance Rules (D2 §24 / status-model.md — binding on any LLM working here)

1. Treat Canonical Rules as authoritative.
2. Treat Proposals/WIP as non-canonical.
3. Treat Roadmap recommendations as implementation guidance.
4. Never promote a proposal because it appears repeatedly in documentation.
5. Never infer a numerical threshold from an example unless explicitly locked.
6. Never silently resolve an open designer fork.
7. Identify contradictions between current and historical documents.
8. Prefer the current locked ruling over superseded source wording.
9. Preserve the distinction between empirical evidence and designer judgement.
10. State clearly when an answer depends on a proposal rather than a Canonical rule.
11. Never create a parallel Core resolution engine merely to implement a subsystem.
12. Never create a new primary resource or progression currency without explicit designer approval.
13. Treat an interface prototype as non-canonical unless a formal ruling says otherwise.
14. When a subsystem is locked, update the Canonical document and its changelog.
15. When a proposal is superseded, retain its historical significance but mark it Superseded.
16. If new evidence materially challenges a locked rule, recommend reopening it rather than silently changing it.

---

## 2. Locked / ruled foundation the Open decisions depend on

The following are the Canonical (locked) and Non-canonical (ruled) decisions that the currently-Open decisions
depend on. "Authority" is as the register records it, not an external assertion.

### 2.1 Canonical / Locked (from `_consolidation/decision-register.md` §A)

| ID | Subject | Decision (abridged) |
|---|---|---|
| DEC-001 | d100 core | Roll-under on 1–100; `00`=100; 100 always fails & is a failed Double |
| DEC-005 | Skill Tier/Cap/Start | Cap = floored avg of Tier attributes; Starting Value = floor(Cap/2) |
| DEC-006 | Core Test Transaction | Fixed 9-step transaction; **no subsystem may replace it** |
| DEC-007 | Cost & Overflow | Cost = natural roll; insufficient → Overflow → direct HP; no second resource pool |
| DEC-012 | Advanced Skills | Created only by qualifying failed Double; Tier+1; full Cap recompute; lineage domain |
| DEC-013 | S-1 Opposed Contest | Universal primitive; outcome matrix; Margin/Blackjack/Hybrid Quality; Failure/Failure repeat; exact-tie repeat |
| DEC-014 | S-2 Tier-1 Location Index (Zero-Step) | Deterministic tens/units exchange on natural roll; **no player choice**; read-only; does not alter Core Test consequences. **Limited scope** (see 2.3) |
| DEC-015 | Reserved Systems list | Everything not explicitly locked (hit-location beyond Tier-1, wounds, Effects, armor, defense, incapacitation, death, healing, etc.) is outside locked Core |
| DEC-016 | Core Architectural Invariants | 18 invariants binding on all future subsystem work (incl. #17, #18: no competing resource economy; modules must build on the Core Test Transaction) |

### 2.2 Non-canonical designer rulings relevant to the Open decisions (from register §B, §D)

| ID | Subject | Decision (abridged) | Status |
|---|---|---|---|
| DEC-017 | S-2 attack-side invocation/warrant policy | Candidate four-state model + Named-Outcome Test, "accepted... for further development/testing" (attack-side only) | **Promoted to Canonical §14.7 (2026-09-05)** |
| DEC-018 | Explicit-only objectives | Only stated objectives are Warrant-eligible; GM does not infer unstated objectives | Current, folded into DEC-017 |
| DEC-019 | Structural Weak Points | Reclassified State 1 → State 2 (anchored, not yet resolvable); no Location Index→component mapping yet | Current |
| DEC-020 | S-2 non-attack deferral | Non-attack resolutions generate **no** Tier-1 Location Index currently (deferral, not impossibility) | **Reopened** by DEC-036 |
| DEC-022 | H0 provenance rule + riders | Retained as an **inert** candidate record for the non-attack question; explicitly **not** an operative rule | Inert / dormant |
| DEC-023–DEC-031 | S-3 Outcome Effects (menu structure, one-Effect-per-win, declared-intent naming, second-Effect Advanced-Skill roll, auto-apply, location+tag gating, boundary, fail-and-fall-back, Quality-gated Effects) | Ruled; governs candidate S-3 material | Ruled (non-canonical) |
| DEC-032 | S-4 Injury vs. Wound | Injury = HP; Wound = localized lasting numerical state | Ruled |
| DEC-033 | S-4 Wound Trigger & Location Scope | Wound = selectable Effect (Wounded Condition) from successful S-1; **Inflict Injury and Wounded both require a Location Index**; Overflow exempt. **NARROWED by DEC-041** (Skill-Tier ≥ 2 gate) | Ruled (narrowed by DEC-041) |
| DEC-034 | S-4 Track A/B | Both Overflow→HP and Wound Effects from one hit, sequentially | Ruled |
| DEC-035 | S-4 Wound Severity | Severity comes from the S-3 gated Effect (a Serious wound is a distinct Effect), not accumulated count | Ruled (corrected) |
| DEC-036 | S-4 DEC-020 Reopening | Reopens DEC-020; non-attack resolutions CAN produce Wounds via Effect if a Location Index can be generated | Ruled |
| DEC-037 | S-2/S-4 Non-Attack Location Index Generation | (1) Failed governing Core Test supplies digits for Zero-Step; (2) hazard "win"; (3) systemic exempt (drowning, suffocation, extreme temp, poison); (4) passive numeric-stub fallback deferring anatomical naming until OPEN-003. Non-blocking residual flags: H0 Rider B (→ DEC-038/039), S-8 dependency | Ruled |
| DEC-038 | OPEN-001A — Rider B causal attribution | **Single causal-attribution principle**: governing Core Test = whichever is causally responsible for the physical consequence, regardless of who rolled it | Ruled |
| DEC-039 | OPEN-001B — Extended Test governing roll | **Final roll** of an Extended Test is governing for Location Index; no earlier roll stored/referenced; closes DEC-037 residual flag | Ruled |
| DEC-040 | OPEN-002 — Scene/campaign Tier | **Tier 0 is the universal default; promotion is per-roll only**; scene reverts to Tier 0 after; no scene-level elevated state | Ruled |
| DEC-041 | OPEN-003 — Anatomical mapping | Skill-Tier-gated granularity, **universal gate** (see §3.1 Open-3 for full six-part rule); narrows DEC-033 & DEC-028 | Ruled |
| DEC-042 | OPEN-004 — Tier-2+ subdivision | **Option B: secondary roll, no resource cost**, not a second Core Test; DEC-030 fail-and-fall-back for mismatch | Ruled |
| DEC-043 | S-8 Third-Party Adjudication | All five sub-questions (same-skill default/GM-discretion fallback; full ordinary Core Test; binary outcome; inverted comparison on adjudicator failure; failed Double unlocks Advanced Skill; generalized to all mutual-failure contests) | Ruled |

### 2.3 The DEC-014 scope limitation (verbatim `_consolidation/decision-register.md` §A note)

> D1 §14.3 is explicit that this locks *only* the Tier-1 Location Index provider — not whether/when a scene uses
> Tier 0/1/2, not anatomical mapping, not wound/armor/defense interaction, not whether any later rule may consume a
> Location Index. Treating DEC-014 as settling any of those adjacent questions would be an unsupported inference.

---

## 3. Currently-Open decisions (from `_consolidation/decision-register.md` §C, live post-DEC-043)

**Resolved within/outside this set are struck in the register; the truly-Open items are OPEN-005 and OPEN-007.**
OPEN-001/002/003/004 are **closed** (DEC-038/040/041/042); OPEN-006 is resolved via DEC-035; OPEN-008 is closed via
DEC-037. They are shown below with their closure only where they remain load-bearing for an Open item's upstream
chain — not as open.

### Open-1 — OPEN-005: S-5 through S-12 subsystem content

| | |
|---|---|
| **Register row** | Decision-register §C OPEN-005 |
| **What the corpus says** | All S-5…S-12 subsystems are "Open"/"Reserved"/"Proposed" — **no locked mechanic for any of them**. S-4 is now ruled (DEC-032–DEC-037). |
| **Upstream ruled/locked** | DEC-001–DEC-016 (Core, incl. DEC-013 S-1, DEC-014 Zero-Step/Tier-1, DEC-016 invariants). Non-attack provenance chain resolved: DEC-020 (reopened) → DEC-036 → DEC-037, and DEC-038/039 (causal attribution + Extended-Test governing roll). S-3 Effects ruled (DEC-023–031). S-4 wound chain ruled (DEC-032–037). |
| **Forks remaining** | Which subsystem to design next; per-subsystem candidate space for **Armor (S-5), Defense (S-6), Incapacitation/death (S-7), Difficulty/task adjudication & Stakes Gate (S-8), Extended Test progress (S-9), Extended Test failure loss (S-10), Rest/Healing (S-11), NPC compression (S-12)**. Roadmap §6.1/§6.2 gives a functional-order dependency layering: S-5/S-6 → S-7/S-8 → S-9/S-10 → S-11/S-12; S-5/S-11 unblocked by S-4; S-6 has DEC-026 & DEC-027 waiting on it; S-12 needs preceding systems. |
| **Governance constraints** | Nothing here may be resolved by an advisory model; only the human designer rules, and promotion requires the 8-step Promotion Rule (§1.4). Any subsystem that produces a Location Index must honor DEC-014's scope limit and Invariant 11/18. S-8's Stakes Gate is flagged as the **most likely natural trigger** for reopening the S-2 non-attack deferral (Roadmap §11.2/§13). |

### Open-2 — OPEN-007: S-4 Wound Consequences

| | |
|---|---|
| **Register row** | Decision-register §C OPEN-007 |
| **What the corpus says** | **RULED already — included only for completeness.** Wounds carry individual mechanical attribute penalties; different wounds may have different magnitudes (−1/−5/−30/−80/−100); more/severe wounds → more negatives; accumulating too many → "game overed"; weaker characters reach that point faster; healing cost scales with the magnitude of the negative; Greater Wound Effects cause serious negatives. |
| **Upstream ruled/locked** | DEC-032 (Injury vs. Wound), DEC-033 (Wound trigger & Location scope, narrowed by DEC-041), DEC-034 (Track A/B), DEC-035 (severity from Effect). |
| **Forks remaining** | None currently open — this item is recorded as Ruled. Retained here only because it is still listed in §C; do not treat as open. |
| **Governance constraints** | Recorded as a designer ruling; promotion still requires the 8-step Promotion Rule. |

### Closed-for-context (struck in register §C — load-bearing upstream, not open)

| ID | Closed via | One-line | Remains relevant to |
|---|---|---|---|
| OPEN-001 | DEC-038 (causal attribution) + DEC-039 (Extended-Test governing roll) | H0 Rider B's two sub-options adjudicated into a single causal-attribution rule; Extended-Test final-roll-govems sub-question closed | S-2 non-attack provenance, S-9/S-10 Extended Tests |
| OPEN-002 | DEC-040 | Tier 0 default, per-roll promotion | Location subsystem (Tier granularity) |
| OPEN-003 | DEC-041 | Skill-Tier-gated granularity, universal | Anatomical mapping, Wound & DEC-028 Effects |
| OPEN-004 | DEC-042 | Option B secondary roll, no cost | Tier-2+ subdivision |
| OPEN-006 | DEC-035 (corrected) | Severity from S-3 Effect, not count-threshold | Wound severity |
| OPEN-008 | DEC-037 | Non-attack Location Index generation ruled | Non-attack provenance |

---

## 4. The repository's actual formal-reporting / provenance standard

This section is sourced **verbatim** from `governance/provenance.md` and the real example report named below —
**not** paraphrased or reconstructed. Any document ChatGPT produces during the session (draft ruling reports, handoff
records, etc.) must conform to this standard on the first attempt.

### 4.1 Mandatory metadata block (verbatim from `governance/provenance.md` §"Mandatory metadata block")

> Every document created by an LLM in this repository must open with a metadata block identifying `author_llm`,
> `assessor_llm`, and `last_modified_by_llm` (each with `name` and `version`), plus `created_date` and
> `last_modified_date`. Use `unknown` or `not established` rather than inventing a value — see below. `assessor_llm`
> may be a **list** when more than one assessment pass has been performed (e.g., an original authoring-session
> assessment followed by an independent second-model assessment appended later); each entry represents one
> assessment, earliest first.

**Role distinction (verbatim from provenance.md §"Role distinction"):**

- **author_llm** — the original creator. Never overwritten by later editors, even if they substantially rewrite the
  document.
- **assessor_llm** — reviews for factual/documentary consistency, canonical-status accuracy, provenance, or
  structure. An assessment is not a human decision and does not confer authority. Where an additional independent
  assessment is later performed, the independent assessor is **appended** to this field as another entry — the
  original assessor record is preserved, not overwritten.
- **last_modified_by_llm** — the most recent substantive editor. Updated on material changes; formatting-only
  changes may be handled per future project policy, not yet defined.

**The actual YAML schema** (as used in the register and governance docs):

```yaml
---
document:
  title: "..."
  version: "..."
  status: "..."        # governance status vocabulary (§1.2)
provenance:
  author_llm: {name: "...", version: "..."}
  assessor_llm:        # list if more than one assessment pass
    - {name: "...", version: "..."}
  last_modified_by_llm: {name: "...", version: "..."}
  created_date: "YYYY-MM-DD"
  last_modified_date: "YYYY-MM-DD"
---
```

**Hard rules:**
- Never name a model without its `version`. If unknown, use `unknown` / `not established` — do not invent.
- `author_llm` is never overwritten by a later editor.
- Do not list yourself as both author AND assessor of the same content unless that is genuinely true — and if it
  is, say so honestly (a single model authoring and "assessing" its own output is weaker review than an independent
  pass).
- Do not fabricate provenance; record unknown provenance as unknown/not established.

### 4.2 State your LLM identity, exact version, and role

The header must state which model you are, your exact version string, and which role you occupy
(author / assessor / last-modifier) for that document. Example from a real report:

> `**Prepared By:** ChatGPT Sonnet 5 (ChatGPT-sonnet-5), in the Lead Systems Architect / Design Assistant role for
> this project, working from the static project snapshot — no live repository access this session.`

Also include Document Version, Document Status, Rule Authority (none / handoff), Session Participants (each
model + version + role), and Purpose — the standard header fields used in the exemplar below.

### 4.3 Decision-register column alignment

Each ruling an LLM drafts should map cleanly onto the register's row structure:
`ID | Subject | Decision/State | Evidence (source) | Authority | Status`.
Per item: give a subject, the decision/state text, the source/evidence pointer, the authority
(e.g. `Non-canonical designer ruling`), and a status (`Ruled` / `Draft` / `Open`). **Do not fabricate DEC
numbers** — leave numbering to OpenCode against the live register's actual next-available sequence.

### 4.4 Formatting exemplar (real report — `investigations/tiwas-s4-documentarian-handoff-report-2026-08-30.md`)

The canonical reference for the report shape is that file's header (title, Document Version/Status, Rule Authority,
Prepared By with model+version+role, Session Participants, Purpose). **Do not reproduce its internal per-item
content**; reproduce only its formal structure and metadata discipline. Documents produced in-session also require
the §4.1 YAML metadata block (the exemplar predates the current consolidated schema and may not carry it — the
**YAML block from §4.1 is the current binding standard**; the exemplar is the reference for header/field conventions
and register-column alignment).

### 4.5 Pointer-not-inline for evidence

Any hash-indexed or audit-trail evidence (per-decision handoff reports `dec025`/`dec026`/`dec027`, the S-2 closure
record, raw LLM survey transcripts) is referenced by **path + one-line status**, never reproduced inline. Example:

- `investigations/tiwas-s2-non-attack-location-source-closure-record-v1.2.md` — S-2 non-attack closure record; holds
  the 14-scenario stress-test set and reopening conditions (pointer, not reproduced).

---

## 5. Practical guidance for advisory opinions

- You may **inspect, compare, explain, identify contradictions, present evidence and possible interpretations, and
  recommend**. You may **not** resolve any Open decision, promote anything to Canonical, or reclassify any document
  — authority changes only through the 8-step Promotion Rule (§1.4) and a human ruling.
- The register (§3) is the source of truth for what is Open vs. Ruled; this brief is a dated subset of it.
- The two distinct "Tier" concepts must not be conflated: **Skill-Tier** (1+, attribute count; base = 1, Advanced =
  2+) vs. **Location-Tier** (0/1/2, scene granularity; default 0, per-roll promotion). This collision previously
  misled a draft; keep them separate.
- Anything you cannot verify against the live repository should be flagged as unverified rather than asserted or
  fabricated (including likely DEC numbering for any new proposal).

---

*End of brief. Compiled 2026-08-31 by OpenCode (documentarian, `opencode`/`big-pickle`) as a task-scoped,
disposable working snapshot. This file supersedes nothing.*
