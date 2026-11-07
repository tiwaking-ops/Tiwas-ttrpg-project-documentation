---
document:
  title: "Seven Consuming Mechanics — Adversarial Verification / Chat Results Report (DEC-133.A R3)"
  version: "1.0"
  status: "Non-canonical advisory record — OpenCode chat-results report; no authority-changing action authorized"
  authority: "Verification record only"
  scope: "Complete results of the 2026-09-19 OpenCode chat performing independent adversarial verification (red-team) of the non-canonical fusion-synthesis draft `tiwas-g5-seven-consuming-mechanics-fusion-synthesis-2026-09-19.md` against the Core Invariants and the live decision register"
provenance:
  author_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  assessor_llm:
    - {name: "Nemotron 3 Ultra", version: "nemotron-3-ultra-550b-a55b (nvidia provider via opencode run, 2026-09-19)"}
  last_modified_by_llm: {name: "opencode", version: "muse-spark-1.3-contributor-free"}
  created_date: "2026-09-19"
  last_modified_date: "2026-09-19"
  note: "This report records the results of the verification chat only. It is non-canonical advisory material, records no DEC, and does not promote, demote, supersede, or alter the authority of any document."
  storage_note: "Moved from repo root to investigations/ on 2026-09-19 by opencode / muse-spark-1.3-contributor-free per the analyze-assess-record-store workflow. Body unaltered; frontmatter updated to record the independent Nemotron 3 Ultra assessment (stored alongside as investigations/tiwas-g5-seven-consuming-mechanics-independent-assessment-2026-09-19.md). Second red-team of the same draft after the upstage solar-pro4:free verification (verifier-only report + summary, stored alongside). Advisory-only, non-canonical, no DEC inferred; storage & assessment confer no authority."
reviewed_document:
  title: "Fusion Synthesis — Seven Consuming Mechanics Candidates (DEC-133.A R3)"
  file: "tiwas-g5-seven-consuming-mechanics-fusion-synthesis-2026-09-19.md"
  author: "grok-fusion (multi-llm-synthesis-2026-09-19)"
  created_date: "2026-09-19"
  status: "Non-canonical advisory"
  decision_reference: "DEC-133.A R3"
---

# Seven Consuming Mechanics — Adversarial Verification / Chat Results Report

**Author:** opencode/big-pickle (version: opencode/big-pickle)
**Assessment date:** 2026-09-19
**Report status:** Non-canonical advisory record. **Nothing herein is Canonical; no DEC is inferred; no authority is changed by this record.**

## 1. Purpose

This report documents the complete substantive results of the OpenCode chat that
performed an **independent adversarial verification** (red-team) of the draft
`tiwas-g5-seven-consuming-mechanics-fusion-synthesis-2026-09-19.md` against:

* the **Core Architectural Invariants** (6, 17, 18) from the Canonical Rules
  (`canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md`, §16 — "Pay Cost
  equal to the natural roll"; the invariant list the spec card locks); and
* the **live decision register** (`_consolidation/decision-register.md`, through
  DEC-145).

The verification acted strictly in the **Adversarial Verifier** role defined in
`roadmap/tiwas-gdd-multi-llm-orchestration-plan-v0.1-2026-09-18.md` (§2, §3 P2):
a model not in the drafter pool red-teams candidate drafts; pass/fail evidence is
reported; the draft is **not** rewritten; open designer forks are surfaced, never
resolved.

## 2. Verification scope and method

The task instruction required the verifier to report **only**:

1. Invariant violations;
2. silent assumptions;
3. contradictions with existing DECs;
4. unresolved designer forks;
5. claims missing an evidence class;

and to produce, for each of the seven consuming mechanics, an invariant status, a
contradiction listing, a designer-question list, and evidence-class flags — without
rewriting the draft.

### 2.1 Documents examined

| Document | Role in verification |
|---|---|
| `tiwas-g5-seven-consuming-mechanics-fusion-synthesis-2026-09-19.md` | Draft under review (339 lines; seven-machinery candidate rules text, §0–§10) |
| `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` | Canonical invariant source (§16; Cost = natural roll) |
| `_consolidation/decision-register.md` | Live decision register, rows DEC-001 … DEC-145, incl. DEC-024/026/030, DEC-077.A, DEC-079(+A), DEC-095, DEC-123, DEC-126, DEC-133(+A), DEC-138 |
| `governance/status-model.md` | Evidence-class vocabulary (mechanical fact / empirical finding / designer ruling / recommendation), status lifecycle, Promotion Rule, LLM Governance Rules |
| `governance/provenance.md` | Provenance block conventions (author_llm / assessor_llm / last_modified_by_llm / dates) |
| `tiwas-dec082-time-action-subsystem-advisory-brief-2026-09-09.md` | Advisory record of Tiwa's option selections for the same seven mechanics (non-ruling) |
| `roadmap/tiwas-gdd-multi-llm-orchestration-plan-v0.1-2026-09-18.md` | Pipeline definition for the verifier role |

### 2.2 Procedural finding — filename mismatch (resolved)

The task instruction referenced a draft named `tiwas-g7-five-consuming-mechanics-fusion-synthesis-2026-09-19.md`. **No such file exists.** The draft actually present is `tiwas-g5-seven-consuming-mechanics-fusion-synthesis-2026-09-19.md`, whose internal title ("Fusion Synthesis — Seven Consuming Mechanics (DEC-133.A R3)") matches the seven-mechanics scope of DEC-133.A R3 exactly. The name in the instruction was interpreted as a typo for this file. This is recorded so future sessions are not confused by the naming discrepancy. It was **not** treated as evidence of anything about the draft's authority.

## 3. Verification results

### 3.1 Spec-card invariant check

**Invariant 6 — Cost = natural roll** (canonical; natural d100 never modified): all
seven candidates maintain full-Cost S-1 contests (DEC-006/DEC-013) with no natural-roll
modification. **Result: PASS, 7/7**, with one flagged item — the Zone of Control Z-A
"2 hexes of Movement Distance allowance per 1 hex traversed" distance multiplier,
which the draft argues is "position accounting, not a second Cost channel." This is a
**soft pass** and is recorded as contradiction **C1** below.

**Invariant 17 — no competing resource pools** (canonical): no candidate creates a
stored movement fund, per-scene counter, or second progression channel; movement
remains ephemeral per-turn allowance under DEC-095 and DEC-133. **Result: PASS, 7/7.**

**Invariant 18 — build on the Core Test; no separate "movement engine"**: all seven
mechanics are expressed as S-1 opposed contests or as Effect payloads under DEC-023.A
Position tier; no parallel resolution engine is introduced. **Result: PASS.**

### 3.2 Contradiction list

| ID | Contradiction / tension | Severity |
|---|---|---|
| **C1** | **Zone of Control Z-A distance multiplier vs DEC-138 (G1 closure).** Dec-138 (2026-09-13) adopted the uniform `Tier-Y Condition Value Z` (`Z = -Y`) overlay as the universal default for movement-penalty magnitude, with content-authored exceptions (DEC-077.A) reserved for degenerate results only (e.g. DEC-125 floor-of-1). The Z-A "2 hexes per 1 hex" multiplier is neither the Tier-Y overlay nor such a narrow exception. This is not a hard lock violation (ZoC as such is carried-open per DEC-133.A R3), but it is an unresolved designer fork on whether a distance multiplier is Invariant 6/17-safe without its own ruling. | Soft |
| **C2** | **Pin/Hold Condition-stack citation imprecision.** The draft's P-0 row cites DEC-122/123/124/126/131 as the Condition stack for Pin/Hold. DEC-126 is a terminology clarification ("Helpless" is not a mechanical term), not a Condition-defining DEC; DEC-122 is the self-referential-Y total-lock mechanism, not a Condition list. The actual Condition vocabulary lives in DEC-079's alpha list (Encumbered, Grappled, Restrained, …). Citations are not false, but they are imprecise. | Minor |
| **C3** | **§10 invariant audit table rows lack individual evidence-class tags.** The §10 Invariant 6/17 audit rows state results ("Satisfied") without per-row `[EC: …]` labels; the table footer carries the umbrella evidence class. Cosmetic, no substantive error. | Minor |
| **C4** | **Draft default recommendations vs DEC-082 advisory-brief selections (informational).** The 2026-09-09 DEC-082 advisory brief (explicitly non-ruling, non-canonical) records Tiwa's earlier option selections for these mechanics (e.g. Disengage = Option B reaction-gated; Chase = Option B chained S-1; Pin/Hold = Option A reuse Restrained; Seize/Deny = Option A Tag-based). The draft presents some "Default recommendation" notes (e.g. K-A binary band steps) without referencing these recorded selections. Since the brief is explicitly non-ruling, this is an omission for designer awareness, not a violation. | Informational |

### 3.3 Designer question list (unresolved forks — NOT resolved by this chat)

The draft correctly preserves the following open forks. This report likewise does not
resolve them.

1. **Disengage shape** — contested S-1 gate (D-A) vs free exit + reaction window (D-B) vs hybrid; Skill lineages for Disengage contests; whether a failed D-A exit consumes movement allowance only or also the substantive action (DEC-095 interaction).
2. **Zone of Control shape** — cost-overlay (Z-A), pure reaction-enabler (Z-B), or gated pass-through contest (Z-C); whether ZoC and Seize/Deny Ground are exclusive or stackable; default hex/band coverage.
3. **Chase shape** — binary band steps (K-A) vs margin-accumulation track (K-B).
4. **Generic movement contest** — Skill lineages and payload selection rules for the shared primitive (Fork G).
5. **Forced Movement magnitude** — Tier-scaled hexes (F-A), fixed 1 hex (F-B), or MS-referenced (F-C); consistent with DEC-107 (Effect Tier = causing Skill-Tier).
6. **Pin/Hold vector** — full existing Condition (reuse Restrained per P-A/previous selection) vs lightweight leave-contest mark (P-B).
7. **Seize/Deny shape** — denial-field (G-A), seize + displace (G-B), unified (G-C).
8. **Fork C (contested-movement consumption)** — mover's allowance, distance already travelled, or nothing beyond natural-roll Cost. Explicitly carried-open by DEC-133.A R2; preserved.
9. **Fork T (extra Skill-Tier gate on Position-tier Effects)** — whether Position-tier requires a DEC-041-style gate beyond the DEC-023.A unlock.
10. **ZoC ↔ Seize/Deny relationship** — exclusive, layered, or soft/hard versions.
11. **Default Skill families for movement contests** (Disengage, Chase, generic M-0).
12. **Duration defaults for pins and ground claims** (interaction with G3/DEC-145 per-domain durations not re-litigated here).
13. **ZoC Z-A distance multiplier invariant status** (derives from C1) — does the multiplier require its own designer ruling, or is the accounting-vs-currency framing sufficient?
14. **Pin/Hold Condition-stack reference precision** (derives from C2) — should P-0 cite DEC-079's alpha vocabulary rather than / alongside DEC-122/123/124/126/131?

### 3.4 Evidence-class flags

| ID | Claim | Evidence class | Status |
|---|---|---|---|
| E1 | Invariant 6 / 17 rows in draft §0.1 | `[EC: mechanical fact for Invariants; designer ruling for listed DECs]` | Covered (table footer) |
| E2 | Draft §1(b)–§7(b) per-mechanic evidence bullet lists | Explicit `[EC: …]` per bullet (e.g. DEC-095 free movement; DEC-133 hex equivalence; DEC-013/006/007 S-1 full Cost; DEC-107 Effect Tier) | Covered |
| E3 | Cross-cutting consumption fork (§8) | Designer ruling that the fork exists (DEC-133.A R2); recommendation to leave open | Covered |
| E4 | §10 audit table rows | Rows ("Satisfied") lack individual `[EC:]` tags; umbrella tag only | Minor flag (C3) |
| E5 | Draft provenance (author_llm grok-fusion; assessor_llm "not established") | Recorded honestly as not-established; assessment pending | Covered |
| E6 | "Nothing herein is Canonical" declarations | Status self-declaration, validated against governance (non-canonical, no DEC inferred); consistent with status-model design | Covered |

## 4. Decisions and conclusions

* **No DEC was inferred, ruled, promoted, demoted, or superseded** in this chat. All
  seven consuming mechanics remain carried-open as Position-tier Effects under
  DEC-023.A / DEC-133.A R3, exactly as the register establishes.
* **The draft is fit for purpose as non-canonical advisory material.** It survives
  Invariant 6, 17, and 18; it preserves rather than collapses the open designer forks;
  it carries evidence-class discipline throughout its body.
* **Three items warrant designer attention before any subsequent sprint**: C1 (ZoC
  Z-A multiplier vs DEC-138 magnitude model), C2 (Pin/Hold Condition-stack citation
  precision), and C3 (§10 audit-table evidence-class tags). C4 is informational.
* **Storage recommendation**: consistent with `governance/status-model.md` (LLM
  Governance Rule 2) and the draft's own header instruction, the draft and this report
  remain non-canonical; placement in `investigations/` or `proposals/` is appropriate.
  Neither storage nor assessment confers authority.
* **Independent-assessment recommendation**: to match the project's healthy review
  discipline (second-model assessment precedent, `audits/README.md`; provenance.md
  self-assessment caveat), a separate-model independent review of this verification is
  recommended before the designer gate (G1) consumes its findings.

## 5. Unresolved issues / next steps

1. Designer (Tiwa) ruling requests: C1 (ZoC distance-multiplier invariant status),
   C2 (Pin/Hold Condition-stack reference), C3 (audit-table EC tags) — formal
   designer ruling, then optional DEC recording via the 8-step Promotion Rule.
2. The 14 designer questions in §3.3 — agenda material for the designer; none are
   answerable by any LLM under current governance.
3. Pending verifier_model selection per orchestration plan §9 item 2 — a strong model
   outside the drafter pool; recorded open.
4. No repository governance item was reopened or resolved as part of this chat.

## 6. Appendix — operational notes from the chat

For future sessions working in this repository under PowerShell 5.1:

* The `&&` chaining operator is **not** supported (ParserError: InvalidEndOfLine).
  Use `;` or `if ($?) { … }` instead.
* `Find-String` is not a valid cmdlet. Use `Select-String` or `findstr`.
* Large files (`decision-register.md`, the draft, JSON candidates) truncate at ~2000
  lines / each read; re-read with `offset` or use targeted `grep` of DEC rows.
* File reads returning partial content should be re-issued with an offset before
  drawing conclusions; the draft's frontmatter was confirmed at first read but its
  body required a second read.

---

**End of report.** This record is non-canonical advisory material. It confers no
authority and changes no document status.
