---
document:
  title: "Tiwas — Magic & Special Abilities Subsystem: Designer Ruling Record (Q-M1–Q-M10)"
  version: "1.0"
  status: "Advisory session record — Non-canonical. Recorded in the live decision register as DEC-146 (2026-09-18, ruled by Tiwa and recorded by OpenCode). Magic/special-ability implementation remains Reserved (Canonical §15 / DEC-015)."
provenance:
  author_llm: []
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-18"
  last_modified_date: "2026-09-18"
---

# Tiwas — Magic & Special Abilities Subsystem: Designer Ruling Record (Q-M1–Q-M10)

## 0. Purpose and Authority Boundary

This document is an **advisory session record**, not a ruling and not a canonical or
non-canonical rules document in its own right. It records decisions made by Tiwa (human
designer / ruling authority) during an in-session advisory conversation with OpenCode
(big-pickle), for the purpose of formal recording by OpenCode into the live decision
register (`_consolidation/decision-register.md`).

**No DEC number is assigned by this document.** Per standing project governance, only
OpenCode assigns DEC numbers and records rulings into the register after Tiwa's approval.
This record supplies the ruling content, rationale, and cross-references needed for that
recording step (recorded as **DEC-146**).

**Ruling basis:** `tiwas-magic-subsystem-project-proposal-2026-09-12.md` (Claude Sonnet 5;
advisory, non-canonical, no DEC; version 0.1) — §5 option catalog, §7 compliance matrix,
§8 recommended direction, §9 open design questions Q-M1–Q-M10 — as verified against the
live register (through DEC-145, 2026-09-18) via the Q-M1–Q-M10 options summary prepared
by OpenCode / big-pickle.

## 1. Item Addressed

**Magic / Special Abilities subsystem**, carried as **Reserved** (Canonical §15;
DEC-015 — Design Direction only): the standing direction is that magic and special
abilities emerge through the existing Advanced-Skill architecture (Canonical §12) rather
than a bespoke spell list, and that a setting may grant permission for a Skill lineage to
represent magic, martial techniques, psychic ability, technology, etc. The
`magic:`/`ability:` Tag namespace is reserved with zero entries (DEC-114 R3).

| Prior reference | Status before this ruling |
|---|---|
| Canonical §15 / DEC-015 | Magic/Special Abilities Reserved; Design Direction only |
| DEC-114 R3 | `magic:`/`ability:` namespace reserved, zero entries; any future list requires authorization together with the Magic subsystem |
| Proposals/WIP v1.4.3 §15 | Current non-canonical design direction: magic via Advanced Skills; no mandatory fixed spell list |
| Proposal (2026-09-12, v0.1) | Advisory; Q-M1–Q-M10 "recorded for Tiwa's ruling"; no DEC |
| Proposal storage annotation on DEC-114 | Advisory storage 2026-09-12 (assessed & stored by OpenCode / big-pickle; no DEC inferred) |

## 2. Rulings

**RULED by Tiwa, 2026-09-18 (in-session, this advisory conversation): ten sub-rulings
(R1–R10), one per open question.** Magic/special-ability implementation remains Reserved
(Canonical §15 / DEC-015); these rulings are Non-canonical; no promotion under the 8-step
Promotion Rule (REQ-021) has been sought or performed. Rulings R3/R9 are **contingent**
rulings that only become operative if Option 5 (Corruption) is ever adopted.

| Q-M | Ruling (Tiwa, verbatim option; reason verbatim) | Effect |
|---|---|---|
| **Q-M1** Base architecture | **A — Options 1+2+3 ADOPTED.** Reason (verbatim): "simplicity and compatibility with Tiwas TTRPG." | Magic is Advanced-Skill-native (Option 1); Technique×Form naming grammar (Option 2) is an authoring convention (catalogs are DEC-077.A content); ritual magic (Option 3) reuses S-9/S-10 (DEC-067–070). Option 5 not adopted. Options 4/6/7 rejected. |
| **Q-M2** Permission Tag vs fictional gate | **B — Vocabulary-only descriptive Tag(s): no mechanical gate.** Reason (verbatim): "Record keeping, flavour, increased immersion. Although no mechanical effect may change in later due to in-game social effects e.g. reputation of unorthodox magic vs orthodox or traditional magic users." | Permission is fictional/GM-adjudicated (DEC-130 available). Any `magic:`/`ability:` Tag is vocabulary-only per DEC-116; DEC-025 preserved. Social/reputation effects accrue narratively, never mechanically; future grading = separate ruling (DEC-116 Open). |
| **Q-M3** Corruption trigger (contingent) | **A — COUPLED trigger.** Reason (verbatim): "simplification on roll one rule." | If Option 5 is ever adopted: Corrupted fires on the same qualifying failed Double that creates the Advanced Skill (Canonical §12). Contingent — not operative now. |
| **Q-M4** Body/Mind lineage mixing | **A — Permitted by default.** Reasons (verbatim): "freedom to create skills is up to the player." / "GM Fiat for setting restricted content (option B)." | Canonical §12.3 applies unchanged; hybrid casters allowed. Setting restrictions are GM Fiat (DEC-130) / content (DEC-077.A), not a framework gate. |
| **Q-M5** Location-referencing magical Effects gate | **A — Same Skill-Tier ≥ 2 gate (confirm DEC-041).** Reason (verbatim): "Strict adherence to Tiwas TTRPG system. Also, GM Fiat can override this e.g. huge fireball hitting multiple locations when checking to see if fragile items were affected or damaged." | No magic-specific carve-out. The cited multi-location fragile-item check is an ordinary application of DEC-130 GM Fiat. |
| **Q-M6** New-spell acquisition | **A — Mechanical trigger sufficient.** Reason (verbatim): "GM fiat if want another way to gain skills." | Canonical §12 failed Double stays the sole mechanical trigger; narrative framing is GM color; alternatives are GM Fiat (DEC-130) / content (DEC-077.A). |
| **Q-M7** Starter `magic:`/`ability:` Tag vocabulary | **A — DEFERRED.** Reason (verbatim): "Tiwas TTRPG is in too primitive of a state to authorize an official vocabulary." | No entries authorized now; DEC-114 R3 reservation stands at zero entries; authorization step pending a future draft. Future vocabulary ships vocabulary-only per Q-M2. |
| **Q-M8** Ritual minimum Skill-Tier | **A — No minimum.** Reason (verbatim): "Ritual magic is just another way to use magic and, other than GM fiat, should be available to everyone." | Rituals available from any Skill-Tier; scope/completion per DEC-070 GM discretion; DEC-130 available; DEC-041's gate not extended to rituals. |
| **Q-M9** Corrupted removal route (contingent) | **B — Two routes (DEC-135.A pattern).** Reason (verbatim): "Two routes allows more flexibility. For example, the setting may not have a purification action or may have a very involved ingame system. Heal will be sufficient as a fallback or base system." | If Option 5 is ever adopted: Effect Heal System (DEC-121/DEC-127) as base/fallback + setting-specific restoration/"purification" action as content (DEC-077.A), which a setting may or may not provide. Contingent — not operative now. |
| **Q-M10** Tiwas-native "Paradox" (Option 6) | **B — Deferred as later separate proposal; neither adopted nor finally closed.** Reason (verbatim): "I want to reject this, however it may be possible to base this on existing attributes and statistics leading to a more robust and interesting system." | Option 6 not pursued now; possible future re-expression of witnessed-vs-unwitnessed / subtle-vs-overt casting built on existing attributes and statistics. |

## 3. Contingencies and Recorded Scope Notes

1. **Option 5 (Corruption) is NOT adopted.** R3 (Q-M3) and R9 (Q-M9) are contingent
   rulings recorded so the trigger-coupling fork and the removal-route pattern are
   pre-decided if Option 5 is ever adopted; they are not operative mechanics today.
2. **Q-M7 defers the DEC-114 R3 vocabulary authorization.** DEC-114 R3 remains "reserved,
   zero entries, authorization pending." Recording R7 here does not constitute the
   authorization step — the step is explicitly deferred.
3. **Q-M10 is a deferral, not a final rejection.** Option 6's "Paradox" re-expression is
   not pursued now but remains a candidate for a later, separate proposal grounded in
   existing attributes and statistics.
4. **Q-M2's social/reputation clause is flavor, not a ruling.** Tiwa's note that
   in-game social effects (reputation of unorthodox vs orthodox magic) "may change in
   later" is recorded as a forward-direction: it may accrue narratively at the table;
   it does not grade Tags today, and any future mechanical grading is a separate ruling
   (DEC-116 Open).

## 4. Preserved / Not Touched

- **Preserved in full:** Canonical §12/§12.3/§15/§16; DEC-015; DEC-021 (promotion rule);
  DEC-023.A; DEC-025; DEC-035.A; DEC-041; DEC-067–070; DEC-070; DEC-077.A; DEC-079;
  DEC-091; DEC-107; DEC-114 R3/R4; DEC-115/116/117; DEC-121; DEC-127; DEC-130;
  DEC-135.A; Proposals §15 Design Direction; Invariants 6/7/17/18.
- **Not touched:** Magic/special-ability Canonical status (remains Reserved); DEC-114 R3
  vocabulary authorization (pending); Option 5 adoption (not adopted; R3/R9 are
  contingencies); DEC-132.B R2's "system too primitive" deferral discipline (parallel
  precedent, unaffected).

## 5. Recording

- **DEC-146** — recorded in `_consolidation/decision-register.md` (Non-canonical designer
  ruling; Status: Ruled (non-canonical); Magic remains Reserved; DEC-114 R3 vocabulary
  authorization pending).
- **DEC-114** — advisory annotation updated with a cross-reference to DEC-146; R3
  authorization status restated as pending.
- **Proposal** — `tiwas-magic-subsystem-project-proposal-2026-09-12.md` version/status/
  document-control updated (version 0.2, 2026-09-18) and a recorded-rulings annex added.
- **Status disclaimer:** recording these rulings confers no Canonical authority. Any
  future promotion of Magic/Special Abilities material (including this proposal's
  content) still requires the full 8-step Promotion Rule (REQ-021 / Proposals/WIP §21).