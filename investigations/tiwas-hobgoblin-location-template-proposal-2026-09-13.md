---
document:
  title: "Tiwas — Hobgoblin Location Address Template (DEC-112 L-004): Advisory Design Proposal"
  version: "0.1 (draft — not executed, not ruled)"
  status: "Advisory / Non-canonical. No DEC assigned. Pending Tiwa's review, edit, or rejection. NOT a DEC-077.A conversion candidate; NOT prior-referenced anywhere in the register — see §0 Provenance Flag (same posture as Orc/Kobold)."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "kilo-auto/free", version: "not established"}
    - {name: "buffy/codebuff", version: "not established"}
  last_modified_by_llm: {name: "buffy/codebuff", version: "not established"}
  created_date: "2026-09-13"
  last_modified_date: "2026-09-16"
---

# Tiwas — Hobgoblin Location Address Template

## Purpose and Origin

The file identifies Claude Sonnet 5 as its author (2026-09-13); this storage/assessment copy was prepared by kilo-auto/free on 2026-09-16. It remains advisory, non-canonical candidate material; storage and assessment confer no authority, assign no DEC, and amend no ruled text.

**Status: Advisory content-authoring proposal only.** Eighth worked instance of
**DEC-112 L-004**, and the first one chosen specifically for its **relationship to an
existing template** rather than for a new structural question. Hobgoblins are, in nearly
every fantasy-genre treatment, the same broad family as Goblins — bigger, more disciplined,
more martial, but recognizably kin. That relatedness raises a question none of the prior
seven templates needed to answer: **should a related creature's template be authored as an
independent design, or as a deliberate interpolation between its relatives' numbers?**
This document does the latter, explicitly, and flags the general question for the
framework as a whole in §6.

## 0. Provenance Flag — Read Before the Rest of This Document

Same posture as Orc and Kobold (weakest tier in this family): **no register mention
anywhere in this repository.** Not a DEC-077.A conversion candidate, and no DEC-084-style
precedent exists for Hobgoblin specifically. DEC-077's unqualified default applies in full.
Advisory candidate input only, zero presumption of acceptance.

---

## 1. Working Concept

A disciplined, militaristic goblinoid — larger and more physically conditioned than a
Goblin, recognizably kin (the same family's ear/nose/jaw features are present) but toned
down from Goblin's caricatured extremes, with a soldier's build rather than a scavenger's
gaunt frame. Medium size, not Small.

## 2. DEC-100 Reuse — Clean, No Hedge

Same conclusion as Goblin/Orc/Kobold: persistent, individually identifiable limbs → DEC-100
reused unchanged. `creature:size_medium` (DEC-080), matching Orc rather than Goblin's
`size_small`. Standard five digits per hand and foot (matching Goblin's convention, not
Kobold's or Ice Troll's clawed reductions) — same species family as Goblin, so the
established design pattern of "family trait consistency" (per the Kobold proposal's own
logic about feature inheritance) argues for keeping digit count identical to Goblin's
rather than inventing a new count the way each unrelated creature has.

## 3. Design Method: Explicit Interpolation, Not Independent Authoring

Rather than author this template from a blank concept the way Goblin, Orc, and Kobold each
were, this document builds Hobgoblin's numbers as a **deliberate midpoint** between Goblin
(small, gaunt, feature-exaggerated) and Orc (medium, muscular, feature-restrained), guided
by where the Hobgoblin concept actually sits between those two reference points on each
axis:

| Axis | Goblin | Orc | Hobgoblin (this proposal) | Placement rationale |
|---|---:|---:|---:|---|
| Thigh width | 11 | 14 | **13** | Trained soldier — closer to Orc than Goblin |
| Chest : Abdomen ratio | 11 : 14 (pot-belly) | 16 : 9 (barrel chest) | **14 : 11** | Disciplined build, no pot-belly, but not Orc's extreme — pulled most of the way back toward Human's baseline 15:10 |
| Upper Arm width | 10 | 14 | **13** | Same logic as Thigh |
| Ears node width | 4 (signature feature) | 0 (folded into Skull) | **3** | Family trait present, visibly toned down — neither absent nor exaggerated |
| Nose width | 4 | 2 (folded into Skull's absence of emphasis — Orc has no distinct Nose beyond the standard 2) | **3** | Same "present but restrained" logic as Ears |
| Jaw/Teeth width | 5 | 7 (tusks) | **5** | Kept at Goblin's/Human's baseline — Hobgoblin is not proposed to have tusks, a deliberate point of divergence from Orc despite the size/build similarity |

This is offered as a **methodology demonstration**, not a claim that interpolation is the
"correct" way to build a related creature — see §6 Question 1 for the honest alternative
(independent authoring, as every other template used) and the tradeoffs between them.

---

## 4. Hobgoblin Location Address Tree

### 4.1 Legs (1–25)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Thigh | 1–13 | 13 | |
| 2 | Shin / Calf | 14–19 | 6 | |
| 3 | Foot (parent) | 20–25 | 6 | Standard five toes |
| 4 | — Hallux | 20–21 | 2 | Widest toe, matching real proportion (as Human's implicit design, made explicit here) |
| 4 | — Second Toe | 22 | 1 | |
| 4 | — Third Toe | 23 | 1 | |
| 4 | — Fourth Toe | 24 | 1 | |
| 4 | — Fifth Toe | 25 | 1 | |

### 4.2 Torso (26–50)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Chest / Upper Torso (parent) | 26–39 | 14 | |
| 3 | — Ribs / Chest wall | 26–34 | 9 | |
| 3 | — Lung | 35–36 | 2 | |
| 3 | — Heart | 37 | 1 | |
| 3 | — Neck | 38–39 | 2 | |
| 2 | Abdomen / Lower Torso (parent) | 40–50 | 11 | No pot-belly emphasis — smallest Lower-Torso proportion of the goblinoid/orcish cluster |
| 3 | — Abdominal Wall | 40–44 | 5 | |
| 3 | — Stomach | 45 | 1 | |
| 3 | — Liver | 46 | 1 | |
| 3 | — Intestines | 47 | 1 | |
| 3 | — Pelvis / Groin | 48 | 1 | |
| 3 | — Spine | 49 | 1 | |
| 3 | — Kidney | 50 | 1 | Restored relative to Goblin (which dropped it for budget) — no budget pressure here |

### 4.3 Arms (51–75)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Upper Arm | 51–63 | 13 | |
| 2 | Forearm | 64–70 | 7 | |
| 3 | Hand (parent) | 71–75 | 5 | |
| 4 | — Thumb | 71 | 1 | |
| 4 | — Index Finger | 72 | 1 | |
| 4 | — Middle Finger | 73 | 1 | |
| 4 | — Ring Finger | 74 | 1 | |
| 4 | — Little Finger | 75 | 1 | |

### 4.4 Head (76–100)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Skull | 76–87 | 12 | |
| 2 | Face (parent) | 88–100 | 13 | |
| 3 | — Eyes | 88–89 | 2 | |
| 3 | — Ears | 90–92 | 3 | Family trait, restrained (§3) |
| 3 | — Nose | 93–95 | 3 | Family trait, restrained (§3) |
| 3 | — Jaw / Teeth | 96–100 | 5 | No tusks — a deliberate divergence from Orc (§3) |

**Totals check:** Legs 13+6+6=25; Torso 14+11=25 (Chest 9+2+1+2=14; Abdomen
5+1+1+1+1+1+1=11); Arms 13+7+5=25; Head 12+13=25 (Face 2+3+3+5=13). Sum = 100. ✓

### 4.5 Laterality

Standard convention. Applies to: all Leg and Arm nodes, Lung, Eyes, Ears, **Kidney**
(paired, per the Human precedent — corrected here from a midline assumption, since Kidney
is a genuinely paired organ). Discarded (midline) for: Heart, Neck, Abdominal Wall,
Stomach, Liver, Intestines, Pelvis/Groin, Spine, Skull, Nose, Jaw/Teeth.

*Worked example:* index **50** → `Torso.Abdomen.Kidney`; 50 is even → **Right Kidney**.

---

## 5. Armor and Regeneration — Content Flags Only

- **No innate Armor Tag proposed**, matching the rest of the "ordinary mortal humanoid"
  cluster (Goblin, Orc, Kobold), despite Hobgoblins' genre-standard reputation for
  disciplined use of well-maintained gear. That reputation is proposed to be represented
  entirely through **equipment** (ordinary `state:worn`/`defense:armor` Tags) rather than a
  body-bound Trait — consistent with how "wears good armor" and "has armored hide" have
  been kept mechanically distinct across every template so far.
- **No Regeneration/Regrowth content proposed.**
- **Signature-attack anchor point (flavor note):** `Arm.Upper Arm`/`Arm.Forearm`
  (disciplined weapon use, closer to Orc's anchor than Goblin's Hand-anchored knife-work)
  is the natural anchor for a Tier-2 signature attack per DEC-086/087. No such skill is
  authored here.

---

## 6. Open Questions for Tiwa's Ruling

1. **Should related-creature templates use explicit interpolation (§3), or should every
   template continue to be authored independently the way Goblin, Orc, Ice Troll, Blood
   Man, Dragon, and Kobold all were?** This is the primary question this document raises,
   and it is bigger than Hobgoblin specifically:
   - **For interpolation:** faster to author, keeps genuinely related creatures
     numerically coherent (a player who's fought both a Goblin and a Hobgoblin should be
     able to sense the kinship in more than just flavor text), and makes future family
     members (e.g. a Bugbear, if the goblinoid family gets a third entry) easier to place
     consistently.
   - **Against interpolation:** every template so far has been justified from its own
     concept, not from arithmetic averaging of others — interpolation risks producing
     numbers that are defensible *relative to their neighbors* but not independently
     motivated, and could compound: an eventual Bugbear interpolated from Hobgoblin, which
     was itself interpolated from Goblin/Orc, is two steps removed from any independently-
     reasoned design.
   - This document does not resolve this; it demonstrates the interpolation approach once
     so the tradeoff is visible, and defers the general policy question to Tiwa.
2. **Acceptance posture (§0)** — no standing precedent, as with Orc/Kobold.
3. **No tusks (§3, Jaw/Teeth row)** is a specific point of divergence from Orc despite
   otherwise sitting close to Orc on most axes — flagged because some genre depictions do
   give Hobgoblins tusks or prominent canines; this proposal deliberately keeps that
   feature Orc-exclusive within the family so the two remain visually/mechanically
   distinguishable at the Jaw node specifically, not because tusks would be wrong for a
   Hobgoblin in principle.
4. **Kidney correction (§4.5)** — noted for the record that this document treats Kidney as
   a paired (L/R) organ, matching the Human proposal's original treatment; if that was
   itself meant to be revisited (it was never flagged as an open question in the Human
   document), this is a quiet consistency fix, not a new design choice.

---

## Appendix A — Consolidated Quick-Reference Table (all 100 values)

| Index | Address | L/R? |
|---:|---|:---:|
| 1–13 | Leg.Thigh | L/R |
| 14–19 | Leg.Shin/Calf | L/R |
| 20–21 | Leg.Foot.Hallux | L/R |
| 22 | Leg.Foot.Second Toe | L/R |
| 23 | Leg.Foot.Third Toe | L/R |
| 24 | Leg.Foot.Fourth Toe | L/R |
| 25 | Leg.Foot.Fifth Toe | L/R |
| 26–34 | Torso.Chest.Ribs/Chest-wall | mid |
| 35–36 | Torso.Chest.Lung | L/R |
| 37 | Torso.Chest.Heart | mid |
| 38–39 | Torso.Neck | mid |
| 40–44 | Torso.Abdomen.Abdominal Wall | mid |
| 45 | Torso.Abdomen.Stomach | mid |
| 46 | Torso.Abdomen.Liver | mid |
| 47 | Torso.Abdomen.Intestines | mid |
| 48 | Torso.Pelvis/Groin | mid |
| 49 | Torso.Spine | mid |
| 50 | Torso.Abdomen.Kidney | L/R |
| 51–63 | Arm.Upper Arm | L/R |
| 64–70 | Arm.Forearm | L/R |
| 71 | Arm.Hand.Thumb | L/R |
| 72 | Arm.Hand.Index Finger | L/R |
| 73 | Arm.Hand.Middle Finger | L/R |
| 74 | Arm.Hand.Ring Finger | L/R |
| 75 | Arm.Hand.Little Finger | L/R |
| 76–87 | Head.Skull | mid |
| 88–89 | Head.Face.Eyes | L/R |
| 90–92 | Head.Face.Ears | L/R |
| 93–95 | Head.Face.Nose | mid |
| 96–100 | Head.Face.Jaw/Teeth | mid |

---

## Appendix B — Eight-Template Comparison

| Feature | Human | Ice Troll | Blood Man | Goblin | Orc | Dragon | Kobold | Hobgoblin |
|---|---|---|---|---|---|---|---|---|
| Tier-1 source | DEC-100 | Reused | Bespoke | Reused | Reused | Bespoke | Reused | **Reused** |
| Digits (hand/foot) | 5/5 | 4/4 | n/a | 5/5 | 5/5 | n/a | 4/3 | **5/5** |
| Chest : Abdomen | 15:10 | 15:10 | n/a | 11:14 | 16:9 | n/a | 12:13 | **14:11** |
| Distinct Ears node | No | No | n/a | Yes (4) | No | n/a | No | **Yes (3)** |
| Design method | Independent (own research) | Independent | Independent | Independent | Independent | Independent | Independent | **Interpolated (§3)** |
| Size tag | — | `large` | — | `small` | `medium` | `large`(+) | `small` | **`medium`** |
| Authorization posture | Own standing | DEC-077.A | DEC-077.A | Weak (DEC-084) | None | Weak (DEC-084) | None | **None** |

**What Hobgoblin confirms — and what it doesn't:** it shows a related-creature template
*can* be built coherently by interpolating between existing relatives' numbers rather than
starting from a blank concept, and that the resulting template still passes every
consistency check (100-state sum, laterality, DEC-100 reuse) the independently-authored
ones do. It does **not** by itself establish that interpolation is the *better* method —
that remains §6 Question 1, genuinely open.

---

**End of proposal.** No DEC assigned. No canonical or non-canonical ruling recorded by this
document. Per §0, this candidate has no standing precedent at all and requires Tiwa's
explicit acceptance before any further use.
