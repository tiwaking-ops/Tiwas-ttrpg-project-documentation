---
document:
  title: "Tiwas — DEC-143 (Draft) — Batch Acceptance Ruling for the Nine DEC-112 L-004 Creature Location-Template Candidates"
  version: "1.0-draft"
  status: "Advisory draft — Non-canonical. A ruling TEXT prepared for Tiwa's review and signature; it is NOT a ruling until Tiwa signs it. No DEC is created by this document's storage or by any agent action. If signed as-is, it is proposed for recording as DEC-143 (next free register number, ceiling verified DEC-142)."
provenance:
  author_llm: {name: "buffy/codebuff", version: "not established"}
  assessor_llm: []
  last_modified_by_llm: {name: "buffy/codebuff", version: "not established"}
  created_date: "2026-09-16"
  last_modified_date: "2026-09-16"
---

# DEC-143 (Draft) — Batch Acceptance of the Nine L-004 Creature Location-Template Candidates

## 0. Governance Notice

**This document is a draft ruling text, not a ruling.** It has no effect, creates no
DEC, and changes no document's status until **Tiwa reviews, edits, and signs it** in a
ruling session. Storage confers no authority (AGENTS.md; standing convention).

**Drafted from established precedent only.** The acceptance mechanics below are the
house pattern from DEC-137 ("Tiwa accepted … as-is"; "working content pending any
future promotion via the 8-step Promotion Rule (REQ-021)") and DEC-077.A ("Tiwa rules
on each …; stays provisional until affirmed"). Nothing here invents a new acceptance
mechanism.

**Why a batch ruling is offered at all:** the L-004 open-questions inventory
(`investigations/tiwas-l004-open-questions-inventory-blocking-rank-2026-09-16.md`)
ranks acceptance posture (ACC, ×9) as the single highest-leverage P0 item — one
decision converts nine stored advisory candidates into usable playtest content.
Tiwa may instead rule per-creature or per-group using the same per-row text; the
batch is offered for efficiency, not required.

**Companion records (all advisory, none authoritative):**
- `investigations/tiwas-l004-open-questions-inventory-blocking-rank-2026-09-16.md` — question inventory and blocking rank
- `investigations/tiwas-l004-four-creature-template-open-questions-designer-options-brief-2026-09-16.md` — 12-row decision table (Giant Spider, Hobgoblin, Kobold, Troll)
- `investigations/tiwas-dec100-tier1-reuse-vs-bespoke-designer-options-brief-2026-09-16.md` — Tier-1 rule A/B/C (open; not ruled here)
- `investigations/tiwas-l004-ten-template-consolidated-comparison-reference-2026-09-16.md` — unified ten-template feature table

## 1. The Decision (one line)

**Accept all nine stored L-004 creature location-template proposals, as-authored, as
working playtest content under DEC-077/DEC-077.A and DEC-112 (L-004) — each subject
to the conditions listed in its row, none of which block initial playtesting.**

*Optional narrower scope:* strike any row(s) to accept a subset; rows are
independent. If Tiwa edits any template before signing, that creature is "accepted
as edited" and its row should be initialed.

## 2. The Nine Candidates (per-creature ruling rows)

All nine were authored by **Claude Sonnet 5** (advisory), stored verbatim with
provenance frontmatter in `investigations/`. All ten trees sum to exactly 100; all
stored copies verified faithful to their sources (2026-09-16 verification records in
the DEC-112 register entry). Each row states the creature's **as-authored defaults**
— what plays if Tiwa signs without edits — and any **conditions** (items that are
combat-mechanical; acceptance keeps the question open without blocking play).

### Row 1 — Ice Troll
- **Source:** `investigations/tiwas-ice-troll-location-template-proposal-2026-09-13.md` (git-recoverable; restore before recording — see §5)
- **Authorization precedent:** DEC-077.A conversion-workflow creature (explicit).
- **As-authored:** DEC-100 quartile Tier-1 **reused** (Legs / Torso / Arms / Head, 25 each) — flagged in the proposal itself as an assumption, Q1 open; `size_large`; Human-divergent content: 4 digits per hand/foot, no separate Ears node (vestigial ear tissue inside Skull 15), prominent Jaw/Tusks (6); **no** standalone Armor Tag in the template (the `defense:armor` freezing-gated Tag is DEC-088's and remains a stat-block trait, placement per open IT-Q2); Regeneration per DEC-088/DEC-110 content-authoring.
- **Condition (combat-mechanical, open):** IT-Q2 Armor Tag placement (Torso+Arms+Legs vs full-body incl. skull plate); IT-Q3 reconciliation against the existing Ice Troll stat block (v3–v6 playtest series) before further playtests of that creature — **diff completed 2026-09-16: zero mechanical contradiction** (those runs exercised no size tag, digit count, or below-Tier-1 address; see `investigations/tiwas-ice-troll-itq3-anatomy-diff-evidence-record-2026-09-16.md`), so IT-Q3 is now a forward-looking baseline adoption (agenda A2), not a retroactive repair.

### Row 2 — Blood Man
- **Source:** `investigations/tiwas-blood-man-location-template-proposal-2026-09-13.md` (git-recoverable; restore before recording — see §5)
- **Authorization precedent:** DEC-077.A conversion-workflow creature (explicit).
- **As-authored:** bespoke three-zone Tier-1 (Core Mass 60 / Pseudopod 30 / Head-Clot 10); **no size tag authored**; no Armor Tag (deliberate — a liquid body gives conventional Armor nothing to bind to); no Regeneration (deliberate flag; DEC-110 route if wanted).
- **Conditions (combat-mechanical, open):** BM-Q2 Pseudopod laterality — as-authored the zone carries no left/right identity ("any currently-extended limb-like protrusion"); relabel A/B vs suppress changes Wound-stacking behavior; BM-Q3 the Core vital node's width 8 vs the narrower ~1–2 vital convention elsewhere (accept as-authored by default).

### Row 3 — Goblin
- **Source:** `investigations/tiwas-goblin-location-template-proposal-2026-09-13.md`
- **Authorization precedent:** DEC-084 names Goblin among creature examples (weak; Goblin also had one adventure-playtest appearance — the road encounter in the Your-First-Adventure playtest record — under the DEC-076-lineage stat-generation flow).
- **As-authored:** DEC-100 reused Tier-1; `size_small`; no innate Armor Tag; no Regeneration.
- **Open (cosmetic, non-blocking):** GO-Q2 pot-belly reversal (Abdomen 14 > Chest 11); GO-Q3 Ears width 4; GO-Q4 no Kidney node.

### Row 4 — Orc
- **Source:** `investigations/tiwas-orc-location-template-proposal-2026-09-13.md`
- **As-authored:** DEC-100 reused Tier-1; `size_medium`; no innate Armor Tag; no Regeneration; no distinct Ears node.
- **Conditions (combat-mechanical, open):** OR-Q2 size class (`size_medium` vs `size_large`, ogre-adjacent subtype) — plays as `size_medium` unless edited.
- **Open (cosmetic, non-blocking):** OR-Q3 16:9 chest/abdomen split (deliberate brute contrast).

### Row 5 — Dragon
- **Source:** `investigations/tiwas-dragon-location-template-proposal-2026-09-13.md`
- **Authorization precedent:** DEC-084 names Dragon (weak precedent).
- **As-authored:** bespoke six-zone Tier-1 (Torso 40 / Neck 10 / Head 15 / Tail 15 / Wings 12 / Legs-Claws 8) with structural-branch × parity laterality; Tier-2 sub-zone-granular permanent Armor registration (exception-carved underbelly); `size_large` **provisional**.
- **Conditions (combat-mechanical, open):** DR-Q2 size tag — no fitting DEC-080 category exists; **plays provisionally at `size_large`** unless/until the `size_huge`/`size_gargantuan` extension is ruled; DR-Q1 underbelly width (wide 10 vs narrow 2–3); DR-Q3 armor exception-carving confirmed as the general pattern (or not) for future templates.
- **Open (cosmetic, non-blocking):** DR-Q4 unarmored Jaws/Fangs simplification.

### Row 6 — Kobold
- **Source:** `investigations/tiwas-kobold-location-template-proposal-2026-09-13.md`
- **As-authored:** DEC-100 reused Tier-1; `size_small`; **no** innate Armor Tag despite scales (deliberate call — KB-Q2's fallback, a Torso-only Tag, remains available); Tail width-3 sub-node; deliberate 4-finger/3-toe asymmetry.
- **Conditions (combat-mechanical, open):** KB-Q2 armor posture (plays with no Tag as-authored).
- **Open (cosmetic, non-blocking):** KB-Q3 Tail width/placement; KB-Q4 digit asymmetry.

### Row 7 — Hobgoblin
- **Source:** `investigations/tiwas-hobgoblin-location-template-proposal-2026-09-13.md`
- **As-authored:** DEC-100 reused Tier-1 (explicit Goblin↔Orc interpolation as methodology demonstration); `size_medium`; no innate Armor Tag; Kidney as paired L/R; no tusks.
- **Open (cosmetic / framework, non-blocking):** HG-Q1 interpolation policy (the REL framework question — open independently); HG-Q3 tusks; HG-Q4 paired Kidney affirmation.

### Row 8 — Giant Spider
- **Source:** `investigations/tiwas-giant-spider-location-template-proposal-2026-09-13.md`
- **As-authored:** bespoke three-branch Tier-1 (Abdomen 45 / Cephalothorax 20 / Legs 35, 4 pairs × structural-branch × parity); `size_large`; six armor registrations with Eyes/Spinnerets carved out (GS-Q3's simpler two-registration model remains available).
- **Conditions (combat-mechanical, open):** GS-Q3 armor registration model (plays six-registration as-authored); GS-Q2 composite-midline treatment for Eyes/Spinnerets as a standing convention.
- **Open (cosmetic, non-blocking):** GS-Q4 leg-pair proportions.

### Row 9 — Troll
- **Source:** `investigations/tiwas-troll-location-template-proposal-2026-09-13.md`
- **As-authored:** derived from Ice Troll by subtracting the two frost/DEC-088-tied items (freezing-gated Armor Tag; Ice Gland); DEC-100-style values otherwise matching Ice Troll's tree; `size_large`; **unconditional** Regeneration (the asymmetry question below).
- **Conditions (combat-mechanical, open — register-adjacent):** TR-Q2 regeneration asymmetry — as-authored means the plain Troll regenerates in all scenes while the Ice Troll does not outside freezing. **Recommended playing posture (per the options brief, unruled):** Read A ("net specialization" — Ice Troll's Template as the more specialized cousin; DEC-088's Condition Clause stays untouched) with a playtest watch-item; revisit DEC-088 only on playtest evidence. If Tiwa prefers, strike this row's acceptance until TR-Q2 is ruled — it is the only row with a ruled-entry adjacency.
- **Open (cosmetic, non-blocking):** TR-Q4 no innate Armor Tag.

### Framework questions deliberately NOT ruled by this acceptance

This draft accepts **templates as-authored**; it does **not** settle:
- **T1** — DEC-100 reuse vs bespoke Tier-1 boundary (A/B/C brief open; acceptance of mixed-source templates presupposes no rule about which is *correct* for future authoring).
- **REL** — related-creature authoring policy (derivation vs interpolation; affects future templates, not these nine).
- **HREF** — six proposals still cite pre-adoption Human reference numbers (Thigh 13→5, Skull 13→16, chest:abdomen 15:10→10:10, missing Ears row). **Non-blocking:** each template's internal tree is self-consistent and sums to 100; the stale figures affect comparative prose only. Correction addendum recorded: `investigations/tiwas-l004-human-reference-correction-addendum-2026-09-16.md`.

## 3. What Acceptance Effects (play-ready summary)

If signed as-is, then per the DEC-137 pattern:

1. **Each of the nine templates becomes working playtest content** — usable in
   playtest stat blocks and playtests, authoritative *as content* for its creature
   (edit as needed), **non-canonical** (not a Canonical rule).
2. **No promotion** — none of this enters canonical rules without the 8-step
   Promotion Rule (REQ-021). Status stays exactly DEC-137's: working content.
3. **Armor Bypass, Wounds, and laterality resolve immediately** for every accepted
   creature under the already-ruled DEC-112/136/137/139 stack, because every tree
   sums to 100 and carries DEC-041(3) parity conventions. Only the listed
   per-creature conditions (Tag placement/coverage, size class, Pseudopod
   laterality, Troll regeneration posture) remain as content-level knobs.
4. **No canonical rule changes** — nothing here amends or reopens any ruled DEC.
   TR-Q2's DEC-088 adjacency is handled by the play posture in Row 9 (Reading A
   leaves DEC-088's text untouched; reopening is explicitly *not* adopted).

## 4. Explicit Non-Effects

- No DEC number is created by this document or its storage; **DEC-143 is proposed
  only if Tiwa signs** (number verified free — current register ceiling DEC-142).
- No proposal text is edited by this acceptance (acceptance is a status change in
  the register + Tiwa's ownership, not a document mutation). Correction addenda for
  HREF, if wanted, are separate future artifacts.
- No question's open status changes except as each row's conditions state: the
  combat-mechanical items stay open as *play-affecting* knobs; acceptance neither
  auto-resolves nor suppresses them.
- Advisory-model authorship remains governed by DEC-077/077.A: this acceptance, if
  signed, is **Tiwa's own ruling** on advisory-drafted content — the decision, not
  the drafting, is what carries weight (DEC-137 precedent).

## 5. Recording Notes for the Scribe (post-signature mechanics)

- Record as **DEC-143** (next free number) with status *Non-canonical designer
  ruling; working content* — mirroring DEC-137's row shape and status text.
- **Before recording:** restore the two DEC-077.A source files from git history into
  `investigations/` (`tiwas-ice-troll-location-template-proposal-2026-09-13.md`,
  `tiwas-blood-man-location-template-proposal-2026-09-13.md` — deleted from the
  working tree, exist only in git HEAD). They are the Row 1 and Row 2 source records;
  the register should not cite unresolvable paths.
- Paste the **entire §1 one-line ruling** into the register row's RULED text, with
  the nine source paths and per-creature conditions listed, and note the batch scope
  (or the struck rows, if any).

## 6. Sign-off Block (for Tiwa)

> Decision needed: accept all nine L-004 creature templates as-authored, as working
> playtest content (with the per-row conditions noted), per the DEC-137 precedent.
>
> - [ ] **Accept all nine as-authored** (this draft as-is).
> - [ ] **Accept with listed conditions binding** (as-authored + each row's
>       conditions treated as the operative posture, e.g., Dragon at provisional
>       `size_large`, Troll under Reading A).
> - [ ] **Accept subset** — strike rows: ______________
> - [ ] **Edit before acceptance** — which: ______________ (then "accepted as edited")
> - [ ] **Reject** — which: ______________
>
> Signature: ____________________  Date: ____________
>
> Confirms: I have reviewed the nine templates (or their consolidated comparison
> reference), the conditions listed per row, and the DEC-077/077.A authorship
> context. This is my ruling as designer; advisory drafting context (DEC-077/077.A,
> DEC-137 precedent) understood.

---

*Prepared by buffy/codebuff (advisory), 2026-09-16. Companion to the open-questions
inventory, the four-creature options brief, the Tier-1 A/B/C brief, and the
ten-template consolidated comparison reference. Advisory only; confers no authority;
nothing is ruled, accepted, or recorded until Tiwa signs.*

*Verbatim-verification pass completed 2026-09-16: every quotation, figure, size tag,
Tier-1 split, and precedent wording re-checked against its source (register row,
stored proposal, or git-recovered original); corrections applied (HREF count 7→6,
IT-Q3 evidence pointer, Goblin appearance wording).*
