---
document:
  title: "Tiwas — L-004 Ruling Session Scribe Packet — Ready-to-Paste Register Rows (DEC-143 + Agenda A2–A7)"
  version: "1.0"
  status: "Advisory scribe material — Non-canonical. Contains NO decisions. Every bracketed blank (______, [ ], ⟨optional⟩) is Tiwa's to fill at session; nothing here is ruled, adopted, or recorded until Tiwa signs and the text is pasted into the register. Storage and drafting confer no authority (AGENTS.md)."
  created: "2026-09-16"
  author_llm: "buffy/codebuff"
  assessor_llm: []
  last_modified_by_llm: "buffy/codebuff"
  last_modified_date: "2026-09-16"
---

# L-004 Ruling Session — Scribe Packet (Ready-to-Paste Register Rows)

**Purpose and origin:** Prepared 2026-09-16 by Buffy/Codebuff (advisory) so the A7 "Scribe & close" slot is pure paste-and-fill. Source materials: the session agenda (`investigations/tiwas-l004-p0-p1-ruling-session-agenda-2026-09-16.md`), the DEC-143 batch-acceptance draft (`investigations/tiwas-dec143-l004-batch-acceptance-ruling-draft-2026-09-16.md`), and register rows DEC-137/DEC-142 (format precedent). All decision sentences below are quoted verbatim from the agenda; all figures were verbatim-verified against the nine source proposals on 2026-09-16.

---

## 0. Governance Notice

- This packet rules nothing. Rows take effect only if and as Tiwa signs them and the scribe pastes them.
- **Blanks:** `______` = fill in by hand · `[ ]` = Tiwa's checkbox · `⟨…⟩` = optional segment — delete entirely if the checkbox it belongs to is not ticked.
- **Pre-paste prerequisite (DEC-143 draft §5):** restore the two git-only source files before recording, so no register row cites an unresolvable path:
  ```bash
  git -c core.quotepath=off show 'HEAD:tiwas-ice-troll-location-template-proposal-2026-09-13.md'  > investigations/tiwas-ice-troll-location-template-proposal-2026-09-13.md
  git -c core.quotepath=off show 'HEAD:tiwas-blood-man-location-template-proposal-2026-09-13.md' > investigations/tiwas-blood-man-location-template-proposal-2026-09-13.md
  ```
- After pasting: verify pure-append on any row that received an annotation (word-diff must show zero deletions), then commit the register as its own commit per house precedent.

## 0.1 Numbering Plan (register ceiling: DEC-142)

| Item | Where it goes | Number |
|---|---|---|
| A1 batch acceptance (×9) | New row | **DEC-143** (R1 below) |
| A2 IT-Q3 anatomy baseline | New row — *or* annotation on DEC-112 if Tiwa prefers | **DEC-144** (R2; fallback R2′) |
| A3 TR-Q2 regeneration | New row (register-adjacent — must stand alone) | **DEC-145** (R3) |
| A4a DR-Q3 standing armor pattern | New row (it is a standing pattern, not a one-off) | **DEC-146** (R4) |
| A4b–e, A5a–b, A6 | Annotation appended to the DEC-143 row (content confirmations) | R5 block |
| Watch-items (A3, A5b) | Inside DEC-145 text + DEC-143 annotation | R3 / R5 |

*Optional promotions:* any R5 item can instead be lifted into its own DEC-147/148… row if Tiwa wants it standing — mark `⟨PROMOTE: DEC-______⟩` on that item and strike it from the annotation.

## 0.2 Attribution column (fill once, reuse in every pasted row)

```
Designer ruling, 2026-09-____ (Tiwa, in-session with ______________, ruling on `investigations/tiwas-l004-p0-p1-ruling-session-agenda-2026-09-16.md` items A_/A__; DEC-143 text drafted in `investigations/tiwas-dec143-l004-batch-acceptance-ruling-draft-2026-09-16.md`); confirmed by Tiwa to the scribe
```

---

## R1 — DEC-143: Batch Acceptance of the Nine L-004 Creature Templates (A1)

Paste as a new row after DEC-142. Ruled text is the draft's §1 one-line decision plus the outcome blanks:

```
| DEC-143 | L-004 creature location templates — batch acceptance of all nine stored candidates as working playtest content (closes the acceptance-posture question for the ten-instance L-004 family; opens DEC-112 L-004 content set beyond Human) | **RULED — ⟨tick one and delete the rest: [ ] Accept all nine as-authored (draft as-is) · [ ] Accept all nine, conditions binding (each row's conditions are the operative play posture) · [ ] Accept subset — struck rows: ______ (strike those creatures from the source list below and initial) · [ ] Accept as edited — which: ______ (initialed) · [ ] Rejected — which: ______⟩** "Accept all nine stored L-004 creature location-template proposals, as-authored, as working playtest content under DEC-077/DEC-077.A and DEC-112 (L-004) — each subject to the conditions listed in its row, none of which block initial playtesting." ⟨If subset/as-edited/reject chosen, scribe adjusts the quoted scope and the source list to match; the quotation is the draft's §1 one-liner verbatim for the default accept-all case.⟩ Advisory candidates (all authored by Claude Sonnet 5, stored verbatim with provenance frontmatter; ten trees sum to 100; 2026-09-16 verification records in the DEC-112 entry): `investigations/tiwas-ice-troll-location-template-proposal-2026-09-13.md` · `investigations/tiwas-blood-man-location-template-proposal-2026-09-13.md` (both restored from git HEAD 2026-09-16; DEC-077.A authorization) · `investigations/tiwas-goblin-location-template-proposal-2026-09-13.md` · `investigations/tiwas-orc-location-template-proposal-2026-09-13.md` · `investigations/tiwas-dragon-location-template-proposal-2026-09-13.md` · `investigations/tiwas-kobold-location-template-proposal-2026-09-13.md` · `investigations/tiwas-hobgoblin-location-template-proposal-2026-09-13.md` · `investigations/tiwas-giant-spider-location-template-proposal-2026-09-13.md` · `investigations/tiwas-troll-location-template-proposal-2026-09-13.md`. **Conditions (combat-mechanical, kept open by this acceptance):** Ice Troll — Armor Tag placement IT-Q2 (outcome recorded per A4b), regeneration per DEC-145, anatomy baseline per DEC-144; Blood Man — pseudopod laterality as-authored (A6), no Armor Tag/Regeneration confirmed (A4e); Orc — plays at `size_medium` (A5a); Dragon — provisional `size_large` with DEC-080 vocabulary extension queued (A5b); Kobold — no innate Armor Tag despite scales, Torso-only Tag standing fallback (A4d); Giant Spider — six armor registrations as-authored (A4c); Troll — unconditional Regeneration read per DEC-145 (A3), no Armor Tag (stands as-authored). **Preserves:** DEC-112 (L-004 architecture), DEC-077/077.A (content bar + BToV authorization), DEC-137 (Human precedent), DEC-088 (Condition Clause untouched), DEC-110 (healing magnitude is per-creature authoring). **Does NOT rule:** Tier-1 source questions (DEC-100 fork — options brief pending), related-creature policy, Human-reference corrections (addendum exists, not adopted). | ⟨attribution block, §0.2⟩ | Non-canonical designer ruling; working content | Ruled ⟨(conditions binding) / (as-authored) / (subset: ______)⟩; authoritative as content, explicitly non-canonical; promotion only via REQ-021 |
```

**R5 note:** if A1 passes, the A4b–e/A5/A6 confirmation annotation (R5 below) is appended to THIS row.

---

## R2 — DEC-144: IT-Q3 Ice Troll Anatomy Baseline (A2)

Ruled text is the agenda's decision sentence, verbatim:

```
| DEC-144 | IT-Q3 — Ice Troll L-004 template adopted as the creature's anatomy baseline going forward (resolves the reconciliation question raised by the inventory; establishes template-vs-playtest-record relationship) | **RULED —** "The L-004 Ice Troll template is the creature's anatomy baseline for all future playtests; the v3–v6 playtest records stand as pre-template runs with no contradiction (they resolved Tier-1 coarse zones under DEC-102 and used no size tag or address tree); the stat block is re-based on the template before the next Ice Troll playtest." ⟨tick one: [ ] Approve as written · [ ] Approved as amended: ______⟩ **Evidence:** zero-mechanical-contradiction diff — the BToV-era conversion stat block (`investigations/tiwas-gurps-creature-conversion-scratch-ice-troll-blood-man-v0.2-2026-09-03.md`) contains no location tree, no size tag, and no digit/ear anatomical commitments; full record in `investigations/tiwas-ice-troll-itq3-anatomy-diff-evidence-record-2026-09-16.md`. Carry-forwards unchanged: IT-Q2 (DEC-145/R5), TR-Q2 watch-item (DEC-145). **Preserves:** the v3–v6 playtest records as historical runs (no rewriting); DEC-112 L-004. | ⟨attribution block, §0.2⟩ | Non-canonical designer ruling | Ruled |
```

**R2′ fallback** (only if Tiwa prefers annotation over a new row): paste instead into the DEC-112 row, house bracket format —

```
[IT-Q3 baseline ruling 2026-09-____ (Tiwa; agenda item A2; advisory-only context):** Ice Troll L-004 template = anatomy baseline going forward; v3–v6 records stand as pre-template runs, no contradiction (evidence record `investigations/tiwas-ice-troll-itq3-anatomy-diff-evidence-record-2026-09-16.md`); stat block re-based before next Ice Troll playtest. Outcome: ⟨approve/amend: ______⟩]
```

---

## R3 — DEC-145: TR-Q2 Regeneration Asymmetry (A3) — register-adjacent

Two mutually exclusive ruled texts — keep exactly one, delete the other:

```
| DEC-145 | TR-Q2 — Troll/Ice-Troll regeneration asymmetry read as net specialization (play posture; DEC-088 Condition Clause untouched) | **RULED —** "Reading A adopted as play posture: the Ice Troll's DEC-088 freezing-gated Regeneration and the Troll's unconditional Regeneration are read as net specialization of one trait — DEC-088's Condition Clause stands untouched; a playtest watch-item records any asymmetry evidence for a future DEC-088 revisit." **Watch-item registered:** Troll regeneration asymmetry — any playtest evidence of the unconditional Regeneration leaking effective healing outside freezing scenes routes back here before any DEC-088 amendment. **Preserves:** DEC-088 (ruled text byte-identical), DEC-110 (healing magnitude remains separate per-creature content-authoring). Options considered: direct DEC-088 amendment (not adopted — no playtest evidence yet). | ⟨attribution block, §0.2⟩ | Non-canonical designer ruling (register-adjacent: touches a ruled entry's interpretation, not its text) | Ruled; DEC-088 unamended; watch-item open |
```

```
| DEC-145 | TR-Q2 — DEC-088 amendment directed (regeneration specialization written into the ruled entry) | **RULED —** "Direct a DEC-088 amendment now: ______ ⟨Tiwa dictates the amendment text or points to the four-creature brief's Option B formulation⟩." Amendment executed as DEC-145.A ⟨or inline, per register amendment precedent⟩. **Evidence:** four-creature brief TR-Q2 row (Reading A "net specialization" vs Option B amendment); DEC-110 separation unchanged. | ⟨attribution block, §0.2⟩ | Non-canonical designer ruling + ruled-entry amendment | Ruled; DEC-088 amended via ______ |
```

---

## R4 — DEC-146: A4a — Standing Innate-Armor Registration Pattern (DR-Q3)

```
| DEC-146 | DR-Q3 — Dragon's Tier-2 exception-carving adopted as the standing pattern for innate armor on creature templates (resolves the armor-framing question for the whole L-004 family) | **RULED —** "Dragon's Tier-2 exception-carving registration is adopted as the standing pattern for innate armor on creature templates (whole-coverage default, exceptions carved at sub-zone granularity)." Immediate applications confirmed in-session: Giant Spider's six registrations, Eyes/Spinnerets carved (A4c); Ice Troll Tag at Torso+Arms+Legs, skull not covered (A4b). Non-applications confirmed: Kobold no Tag despite scales, Torso-only Tag standing fallback (A4d); Blood Man no Tag/Regeneration, future mitigation routes through DEC-110-style per-creature authoring (A4e); Troll no Tag stands as-authored. **Evidence:** Dragon proposal §4 (exception-carving mechanics, consistent with L-007/L-012); Giant Spider proposal §4; corpus practice (de facto pattern across stored templates). | ⟨attribution block, §0.2⟩ | Non-canonical designer ruling (standing content-authoring pattern) | Ruled |
```

*If Tiwa rules A4a down:* strike R4; the five armor items then record individually in R5 with per-item blanks.

---

## R5 — Annotation appended to the DEC-143 row (A4b–e, A5a–b, A6 confirmations)

Paste at the end of the DEC-143 row's ruled cell (before the closing pipe), house bracket format. **Delete any item Tiwa did not confirm; delete the whole block if R4 was ruled and Tiwa wants no per-item record.**

```
[Session confirmations 2026-09-____ (Tiwa, in-session; agenda items A4–A6; advisory-only, non-canonical):** A4b IT-Q2 — Ice Troll DEC-088 Armor Tag registers at Torso+Arms+Legs, skull not covered ⟨confirmed / amended: ______⟩. A4c GS-Q3 — Giant Spider plays as-authored with six armor registrations, Eyes/Spinnerets carved ⟨confirmed / two-registration fallback: ______⟩. A4d KB-Q2 — Kobold no innate Armor Tag despite scales; Torso-only Tag standing fallback ⟨confirmed / Tag granted: ______⟩. A4e BM-Q4 — Blood Man's absence of Armor Tag and Regeneration confirmed as authored; future mitigation/healing routes through DEC-110-style per-creature authoring ⟨confirmed / ______⟩. A5a OR-Q2 — Orc plays at `size_medium` as-authored ⟨confirmed / size_large: ______⟩. A5b DR-Q2 — Dragon plays provisionally at `size_large`; DEC-080 category extension (`size_huge`/`size_gargantuan`) queued as separate content item — **watch-item registered** ⟨confirmed / extension ruled now: ______⟩. A6 BM-Q2 — Blood Man's Pseudopod zone carries no left/right identity (as authored): pseudopods reform between exchanges, so Wound records accumulate on the zone, not on sides ⟨confirmed as-authored / relabel persistent A/B: ______⟩.]
```

---

## R6 — Recording checklist for A7 (scribe, 10 min)

1. ☐ Restore the two git-only proposals (§0 commands) — **before** any paste.
2. ☐ Fill §0.2 attribution block once; reuse verbatim in every pasted row.
3. ☐ Paste R1 (DEC-143) — outcome checkbox resolved, unused options deleted.
4. ☐ Paste R2 or R2′ (A2 outcome), R3 (one variant only), R4 (if A4a passed).
5. ☐ Append R5 to the DEC-143 row (items pruned to what was confirmed).
6. ☐ Verify: word-diff the register — **zero deletions** on DEC-112 and any annotated row; new rows end with the standard six columns; no ruled text elsewhere touched.
7. ☐ Commit the register alone (`register: record DEC-143…` per house message precedent); advisory documents can follow in a second commit.
8. ☐ Confirm both watch-items are written down (DEC-145 text + R5 A5b) and queue P2 (T1 options brief, REL, HREF addenda) + flagged P3 for a later session.

**Explicit non-recordings:** T1 reuse/bespoke (brief pending), related-creature policy, Human-reference correction addenda, and all P3 polish — none of these may be pasted today; their open status survives the session untouched.

*Status: advisory scribe material only. Every row above is a draft for Tiwa's session; nothing is ruled, and the register is untouched by this packet until the scribe pastes post-signature.*
