---
document:
  title: "C-05 Regeneration/Regrowth Healing-Magnitude Vocabulary Design Ruling — Content-authoring per creature (no rule gap)"
  version: "1.0"
  status: "Advisory recording of a designer ruling. Non-canonical. Assigns DEC-110 in the decision register."
provenance:
  author_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
  ruling_origin: "Human designer (Tiwa), in-session ruling, 2026-09-05, resolving candidate DEC item C-05 (Regeneration/Regrowth healing-magnitude vocabulary) from the playtest candidate-DEC list and carried-open tracking"
  recorded_in: "_consolidation/decision-register.md DEC-110"
---

# C-05 Regeneration/Regrowth Healing-Magnitude Vocabulary Design Ruling — Content-authoring per creature (no rule gap)

## 1. Purpose

This document records Tiwa's designer ruling resolving **C-05** — the
Regeneration/Regrowth **healing-magnitude vocabulary** item. C-05 was carried as an
open item from the BToV-Madness Ice Troll combat-pipeline work: DEC-088 established
the *trigger grammar* for an environment-conditional Trait (`Active only while
[env:freezing] is present`) but supplied **no mechanical payload** — no HP per
cadence, no Wound-tier/Regrowth effect, no S-11 relationship.

## 2. Open item resolved

| ID | Candidate gap | Expected scaffold (v2 prompt appendix) |
|---|---|---|
| C-05 | Regeneration/Regrowth healing-magnitude vocabulary | "Numeric heal-per-tick value, invented and logged when a Regen tick applies" |

## 3. Evidence established before the ruling

- **DEC-085 (register, 2026-09-03)** carried open "Regeneration/Regrowth/Fright
  vocabularies"; register note: *"Regeneration/Regrowth vocabulary partially addressed
  by DEC-088's Condition Clause + `env:freezing` Tag, though the healing-magnitude
  vocabulary itself remains open."*
- **DEC-088 (2026-09-03)** supplies Conditional-Trait Binding grammar only;
  read-only/stateless; determines trait *presence*, never magnitude.
- **Readiness investigation §2.3 (2026-09-04):** "Partially open" — DEC-088 gives "no
  rate of Wound-tier reduction or HP restoration per interval, no interaction rule with
  the DEC-035.A Wound-tier/healing-gate framework, no defined relationship to S-11
  Extended-Test healing."
- **Comparative Systems Readiness Report §12:** Regeneration/Regrowth deliberately
  inactive in all three executions; **Untested**; not a passed subsystem.
- **GURPS source (source-system values, not imported per DEC-085 cl.3):** Ice Troll —
  Regeneration (Fast, **1 HP/minute**, freezing only); **Regrowth (freezing only)**;
  DR 2 (freezing only). Scale mismatch: GURPS pool 15 → 1 HP/min ≈ 6.7%/min vs. Tiwas
  Troll pool **705** → ≈ **0.14%/min**.
- **Environmental-trait advisory handoff (2026-09-03):** *"Magnitude/timing value
  (1 HP/min) is a content-authoring value under DEC-077.A, not part of the binding rule
  itself."*
- **Tiwas magnitude patterns that already exist:** Energy Regen = bep + bes (DEC-004),
  recovered as a step each combat exchange (`ER / 2`, clamped) — a formula-derived
  magnitude with no dice; C-01 Inflict Injury magnitude resolved via convergent scaffold
  (DEC-096, Winner's Margin); C-10 Frightened magnitude folded into the existing
  Condition architecture (DEC-094 — no independent magnitude system).

## 4. The ruling — verbatim (Tiwa, 2026-09-05)

> **RULING — Option A: Content-authoring per creature (no rule gap).**
>
> **Reason:** "Simplest fix for playtest only."

## 5. Structured restatement (for execution)

- **C-05 is CLOSED as a content-classification, not established as a rule.** No new
  amount/cadence mechanic is created. The healing-magnitude *vocabulary* (heal value
  + cadence + any Regrowth/Wound-tier effect) is **authored content per creature** under
  the DEC-077.A in-playtest content-authoring path (provisional, Tiwa rules on each).
- **DEC-088 unchanged:** the Condition Clause still determines *whether* a
  Regen/Regrowth tick applies in the current scene; it does not and will not supply a
  magnitude.
- **GURPS source value is a reference, not an import:** the Ice Troll's 1 HP/min
  (freezing) is source-system flavour available to inform Tiwa's authored playtest value
  if chosen; nothing is mechanically adopted by this ruling, consistent with DEC-085 cl.3.
- **Interactions preserved:** S-11 Extended-Test healing (DEC-071–074) and the
  DEC-035.A Wound-tier/healing-gate framework are untouched. Whether a creature's
  authored Regen value interacts with either is a content decision, not a new rule.
- **No canonical-facing change:** DEC-004 derived statistics unchanged; no new derived
  stat; Invariant 17 satisfied (no new resource/progression economy).

## 6. Register entry

Recorded in `_consolidation/decision-register.md` (Section B, Non-canonical designer ruling):

| ID | Subject | Status |
|---|---|---|
| DEC-110 | C-05 — Regeneration/Regrowth healing-magnitude vocabulary: content-authoring per creature (no rule gap) | Ruled (non-canonical) |

## 7. Status

**Status:** Advisory recording — not canonical
**Authority:** Non-canonical designer ruling (real decision; promotion requires the
8-step Promotion Rule)
**Assigns:** DEC-110 (next sequential ID after DEC-109)
**Resolves:** C-05 (Regeneration/Regrowth healing-magnitude vocabulary) — closed as
content-classification; no rule gap
**Preserves:** DEC-088 (Condition-Clause gating — presence only), DEC-085 cl.3 (no
GURPS numeric import), DEC-077.A (content-authoring path), S-11 (DEC-071–074),
DEC-035.A (Wound-tier/healing-gate), DEC-004 (derived statistics), Invariant 17
**Canonical rule change:** None