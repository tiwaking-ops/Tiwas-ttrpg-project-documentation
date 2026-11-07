---
document:
  title: "Tiwas — Troll Location Address Template (DEC-112 L-004): Advisory Design Proposal"
  version: "0.1 (draft — not executed, not ruled)"
  status: "Advisory / Non-canonical. No DEC assigned. Pending Tiwa's review, edit, or rejection. NOT a DEC-077.A conversion candidate (only 'Ice Troll' specifically is named there) — see §0 Provenance Flag."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  created_date: "2026-09-13"
  last_modified_date: "2026-09-13"
---

# Tiwas — Troll Location Address Template

**Status: Advisory content-authoring proposal only.** Tenth worked instance of
**DEC-112 L-004**, and the first one built by **direct derivation from an already-drafted
template** rather than independent authoring (like seven of the prior nine) or sibling
interpolation (like Hobgoblin). This document is the base "Troll" species the earlier Ice
Troll proposal already describes itself as a variant *of* — so deriving it means
subtracting the ice-specific parts from Ice Troll's already-built tree, not inventing a
new concept from scratch.

## 0. Provenance Flag — Read Before the Rest of This Document

DEC-077.A authorizes **"Ice Troll"** by name for GURPS conversion, not a generic "Troll."
This document is therefore **not** covered by that authorization, despite its close
relationship to a document that is. It carries the same weak posture as Orc, Kobold,
Hobgoblin, and Giant Spider: no register mention, no precedent, DEC-077's unqualified
default in full force. Advisory candidate input only.

---

## 1. Method: Derivation, Not Interpolation — Why This Differs From Hobgoblin

The Hobgoblin proposal's §3 built new numbers as a weighted *average* between two
independently-conceived relatives (Goblin, Orc), and §6 Q1 of that document left open
whether that was even the right general approach — a real concern, since interpolating
between two things each individually justified by their own concept risks producing
numbers justified only *relative to their neighbors*.

This document does something narrower and better-grounded: **Ice Troll's own working
concept (§1 of that proposal) already states it is a variant of a base Troll**, and that
document's own §2 ("What Does Not Carry Over") already separated *troll-generic* anatomy
(four digits, no distinct ears, wide/tough hide nodes, prominent jaw/tusks) from
*ice-specific* content (the freezing-gated Armor Tag, the Ice Gland organ). Building base
Troll is therefore **subtraction from a documented parent-child relationship**, not
averaging between peers — there is no second reference point being blended in, and no new
proportion judgment calls of the kind Hobgoblin's §3 required. The whole tree below is
**identical to Ice Troll's** except at the two points §2 already flagged as ice-specific.

This is offered as a partial, non-binding answer to Hobgoblin's §6 Q1: **"related
creature" is not one relationship** — direct-variant derivation (this document) and
sibling interpolation (Hobgoblin) may reasonably warrant different policies even if Tiwa
ultimately wants a single rule for both.

## 2. What Changes From Ice Troll (Two Changes Only)

| Element | Ice Troll | Troll (this proposal) | Why |
|---|---|---|---|
| `Torso.Chest` node at index 38 | Ice Gland (frost-themed organ) | **Regenerative Core** | Same slot, rethemed — an anchor point for this creature's actual defining trait (§4), not an ice-elemental flourish |
| Innate Armor Tag | `defense:armor`, freezing-gated (DEC-088), registered at Torso+Arms+Legs | **None** | The armor was explicitly tied to Ice Troll's env:freezing Conditional-Trait Binding — a base Troll has no elemental basis for it; represented instead through toughness/regeneration, matching the Goblin/Orc/Kobold "ordinary creature, no innate armor" convention |
| Everything else (all ranges, all digit counts, laterality convention, DEC-100 reuse assumption) | — | **Unchanged** | None of it was ice-specific to begin with — Ice Troll's own §2 never listed proportions, digit count, or the missing-Ears choice as ice-related |

`creature:size_large` (DEC-080) carries over unchanged — same species, same size class.

---

## 3. Troll Location Address Tree (identical to Ice Troll except the two changes above)

### 3.1 Legs (1–25)

| Tier | Node | Range | Width |
|---|---|---:|---:|
| 2 | Thigh | 1–15 | 15 |
| 2 | Shin / Calf | 16–21 | 6 |
| 3 | Foot (parent) | 22–25 | 4 |
| 4 | — Great Claw | 22 | 1 |
| 4 | — Second Claw | 23 | 1 |
| 4 | — Third Claw | 24 | 1 |
| 4 | — Outer Claw | 25 | 1 |

### 3.2 Torso (26–50)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---:|---|
| 2 | Chest / Upper Torso (parent) | 26–40 | 15 | |
| 3 | — Hide / Chest wall | 26–34 | 9 | |
| 3 | — Lung | 35–36 | 2 | |
| 3 | — Heart | 37 | 1 | |
| 3 | — **Regenerative Core** | 38 | 1 | **Changed from Ice Gland** — anchor for unconditional Regeneration (§4) |
| 3 | — Neck | 39–40 | 2 | |
| 2 | Abdomen / Lower Torso (parent) | 41–47 | 7 | |
| 3 | — Abdominal Hide | 41–43 | 3 | |
| 3 | — Stomach | 44 | 1 | |
| 3 | — Liver | 45 | 1 | |
| 3 | — Intestines | 46 | 1 | |
| 3 | — Kidney | 47 | 1 | Paired |
| 2 | Pelvis / Groin | 48–49 | 2 | |
| 2 | Spine | 50 | 1 | |

### 3.3 Arms (51–75)

| Tier | Node | Range | Width |
|---|---|---:|---:|
| 2 | Upper Arm | 51–64 | 14 |
| 2 | Forearm | 65–71 | 7 |
| 3 | Hand (parent) | 72–75 | 4 |
| 4 | — Thumb-Claw | 72 | 1 |
| 4 | — Index-Claw | 73 | 1 |
| 4 | — Middle-Claw | 74 | 1 |
| 4 | — Outer-Claw | 75 | 1 |

### 3.4 Head (76–100)

| Tier | Node | Range | Width |
|---|---|---:|---:|
| 2 | Skull | 76–90 | 15 |
| 2 | Face (parent) | 91–100 | 10 |
| 3 | — Eyes | 91–92 | 2 |
| 3 | — Nose | 93–94 | 2 |
| 3 | — Jaw / Tusks | 95–100 | 6 |

**Totals check:** identical to Ice Troll's — Legs 15+6+4=25; Torso 15+7+2+1=25; Arms
14+7+4=25; Head 15+10=25. Sum = 100. ✓ (No recomputation was needed since no width
changed — only one node's *content*, not its range, differs from Ice Troll.)

### 3.5 Laterality

Unchanged from Ice Troll: parity of the raw index (odd=Left, even=Right), applied to all
Leg and Arm nodes, Lung, Kidney; discarded (midline) for Heart, Regenerative Core, Neck,
Abdominal Hide, Stomach, Liver, Intestines, Pelvis/Groin, Spine, Skull, Nose, Jaw/Tusks.

---

## 4. Regeneration — The Actual Defining Trait, and a Flagged Asymmetry

Regeneration is proposed here as **unconditional** — not gated behind any `env:` Condition
Clause the way Ice Troll's was gated behind `env:freezing` (DEC-088). This is the
single biggest content difference between the two templates, bigger in practice than
either of the two tree changes in §2, even though it requires no address-tree change at
all (per the established pattern: Wound/Effect healing content applies uniformly to any
node regardless of this template's contents, same observation made for every prior
template with regeneration content flagged).

**A genuine asymmetry worth flagging, not resolved here:** if Troll's regeneration is
unconditional and Ice Troll's is conditional-on-freezing, then in any non-freezing scene
Ice Troll is **strictly worse off** than a base Troll at the single trait most people
associate with the species — which reads backward for an "elemental variant," normally
expected to trade a narrower situational bonus for something extra, not lose the
species' signature trait outside its niche. Two readings are available and neither is
adopted here:

- **Reading A:** Ice Troll trades baseline (always-on) regeneration for a *combined*
  freezing-gated package (regeneration **and** armor together) that is more powerful
  than base Troll's kit specifically while frozen conditions hold, and weaker outside
  them. A net specialization, not a strict downgrade.
- **Reading B:** the original DEC-088 ruling, made before this base Troll template
  existed, simply didn't have an unconditional baseline to compare against, and may
  warrant revisiting once one does.

This document does not choose between them — flagged as §6 Question 2.

---

## 5. Open Questions for Tiwa's Ruling

1. **Acceptance posture (§0)** — no standing precedent, as with Orc/Kobold/Hobgoblin/
   Giant Spider, and notably not extended by Ice Troll's DEC-077.A authorization even
   though this document derives directly from it.
2. **The regeneration asymmetry (§4)** — whether Ice Troll's freezing-gated regeneration
   should now be revisited in light of a proposed unconditional baseline, or whether
   Reading A (net specialization, not a downgrade) is the intended relationship and needs
   no change.
3. **Derivation vs. interpolation as separate policies (§1)** — this document's central
   methodological claim is that "related creature" splits into at least two distinct
   cases warranting possibly different treatment. Whether Tiwa agrees that's a real
   distinction (rather than a distinction without a difference) bears directly on how
   Hobgoblin's still-open §6 Q1 should ultimately be resolved.
4. **No innate armor (§2 table)** — matches the Goblin/Orc/Kobold convention, but a
   counter-argument exists: trolls are proverbially thick-skinned even without an
   elemental basis for it, and a modest unconditional Armor Tag (distinct from Ice
   Troll's conditional one) is a defensible alternative not adopted here.

---

## Appendix A — Consolidated Quick-Reference Table (all 100 values)

| Index | Address | L/R? |
|---:|---|:---:|
| 1–15 | Leg.Thigh | L/R |
| 16–21 | Leg.Shin/Calf | L/R |
| 22 | Leg.Foot.Great Claw | L/R |
| 23 | Leg.Foot.Second Claw | L/R |
| 24 | Leg.Foot.Third Claw | L/R |
| 25 | Leg.Foot.Outer Claw | L/R |
| 26–34 | Torso.Chest.Hide | mid |
| 35–36 | Torso.Chest.Lung | L/R |
| 37 | Torso.Chest.Heart | mid |
| 38 | Torso.Chest.Regenerative Core | mid |
| 39–40 | Torso.Neck | mid |
| 41–43 | Torso.Abdomen.Abdominal Hide | mid |
| 44 | Torso.Abdomen.Stomach | mid |
| 45 | Torso.Abdomen.Liver | mid |
| 46 | Torso.Abdomen.Intestines | mid |
| 47 | Torso.Abdomen.Kidney | L/R |
| 48–49 | Torso.Pelvis/Groin | mid |
| 50 | Torso.Spine | mid |
| 51–64 | Arm.Upper Arm | L/R |
| 65–71 | Arm.Forearm | L/R |
| 72 | Arm.Hand.Thumb-Claw | L/R |
| 73 | Arm.Hand.Index-Claw | L/R |
| 74 | Arm.Hand.Middle-Claw | L/R |
| 75 | Arm.Hand.Outer-Claw | L/R |
| 76–90 | Head.Skull | mid |
| 91–92 | Head.Face.Eyes | L/R |
| 93–94 | Head.Face.Nose | mid |
| 95–100 | Head.Face.Jaw/Tusks | mid |

---

## Appendix B — Ten-Template Comparison (relatedness column added)

| Feature | Human | Ice Troll | Blood Man | Goblin | Orc | Dragon | Kobold | Hobgoblin | Giant Spider | Troll |
|---|---|---|---|---|---|---|---|---|---|---|
| Tier-1 source | DEC-100 | Reused | Bespoke | Reused | Reused | Bespoke | Reused | Reused | Bespoke | **Reused (inherited)** |
| Relationship to another template | None | None (Troll's variant, but Troll didn't exist yet) | None | None | None | None | None | Interpolated (Goblin×Orc) | None | **Derived (subtraction from Ice Troll)** |
| Innate Armor Tag | None | Whole zones, conditional | None | None | None | Sub-zone, permanent | None | None | Sub-zone, permanent | **None** |
| Regeneration | None | Conditional (freezing-gated) | Suggested, not authored | None | None | None | None | None | None | **Unconditional** |
| Authorization posture | Own standing | DEC-077.A | DEC-077.A | Weak (DEC-084) | None | Weak (DEC-084) | None | None | None | **None (narrower than its own parent's authorization)** |

**What this confirms:** related-template construction isn't one method needing one
policy answer. Hobgoblin interpolated between two peers that could each stand alone.
Troll instead recovers a parent concept a child template had already partially described.
The two produce structurally similar-looking outputs (both reuse most of another
template's numbers) but rest on very different amounts of justification — worth keeping
distinct when Tiwa rules on how future related creatures should be built.

---

**End of proposal.** No DEC assigned. No canonical or non-canonical ruling recorded by this
document. Per §0, this candidate requires Tiwa's explicit acceptance before any further
use, independent of Ice Troll's own (different, narrower) authorization.
