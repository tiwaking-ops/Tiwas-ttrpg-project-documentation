---
document:
  title: "Tiwas — Ice Troll Location Address Template (DEC-112 L-004): Advisory Design Proposal"
  version: "0.1 (draft — not executed, not ruled)"
  status: "Advisory / Non-canonical. No DEC assigned. Pending Tiwa's review, edit, or rejection. Content-authoring only, under the DEC-077.A conversion workflow (Ice Troll is one of the two creatures authorized for that workflow)."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  created_date: "2026-09-13"
  last_modified_date: "2026-09-13"
---

# Tiwas — Ice Troll Location Address Template

**Status: Advisory content-authoring proposal only.** This is a second worked instance of
**DEC-112 L-004** (per-creature-type Location Templates), applied to the **Ice Troll** —
one of the two creatures DEC-077.A authorizes for GURPS-to-Tiwas conversion work
(alongside Blood Man). It generalizes the method from the Human proposal
(`tiwas-human-location-template-l009-l010-proposal-2026-09-12.md`), not its numbers.
**Nothing here is canonical, ruled, or DEC-numbered**, and per DEC-077.A, **Tiwa retains
final authorship and rules on each conversion element individually** — this document
proposes candidates only.

**Important scope note:** this document does **not** have access to the source GURPS stat
block in `Beyond-the-Vale-of-Madness-GURPS.pdf`. Per DEC-085 cl.3, GURPS numeric values
(DR, damage dice, etc.) are never imported verbatim regardless. Location addressing is
Tiwas-native architecture with no GURPS analogue to convert *from* — everything below is
**new anatomical content**, authored to be consistent with a generic "ice troll" fantasy
archetype and with the Ice Troll behavior already on record in this repository (DEC-088's
freezing-gated Armor/Regeneration/Regrowth Traits; DEC-085/087's Tier-2 signature-attack
convention). If an existing Ice Troll working stat block already fixes details this
document guesses at (exact size, digit count, etc.), that stat block is authoritative and
this proposal should be reconciled against it, not the reverse.

---

## 1. What Carries Over Unchanged From the Human Template

| Element | Status for Ice Troll |
|---|---|
| Zero-Step as sole index provider (DEC-014); natural roll untouched (Invariant 6) | Unchanged |
| Single-source deterministic resolution, no secondary roll (DEC-112 L-003/L-011) | Unchanged |
| Skill-Tier → Location Tier mapping, no formal cap (DEC-112 L-005) | Unchanged |
| Parent covers children (DEC-112 L-007); mismatch → parent fallback (L-014) | Unchanged |
| Laterality via Zero-Step digit parity only (DEC-041(3), L-008) | Unchanged |
| Skill-Tier ≥ 2 gate on all location-referencing Effects (DEC-041(1)) | Unchanged |
| Terminal-Leaf Saturation as the resolution-ceiling answer (§3 of the Human proposal) | Carried forward as the same recommendation — see §5 below; not re-argued here |
| Address notation (`Zone.SubZone.Region.Node (Left/Right)`, raw index retained) | Unchanged format |

## 2. What Does *Not* Carry Over — Creature-Specific Design

DEC-041(5) is explicit that creature coverage uses **individual templates per creature
type, not a shared scheme**. The Human template's Tier-2+ content (5 digits, distinct
Ears, five internal organs, etc.) is Human-specific anatomy — it is not assumed here.
Design differences applied for Ice Troll, each flagged as a content choice rather than a
forced consequence of any rule:

- **Four digits per hand/foot, not five** (thick, clawed, fused outer digits) — a common
  troll/ogre-archetype convention, distinguishes this template structurally from Human's.
- **No distinct external-Ear node** — folded into a generic Skull reading (small,
  skin-covered, or vestigial ears are common in troll depictions and not worth a separate
  narrow leaf here).
- **A troll-specific internal organ ("Ice Gland")** near the heart — new content tied
  directly to the creature's frost theme and to the DEC-088 Conditional-Trait Binding
  grammar (a plausible future anchor point if a frost-specific Wound Effect or vulnerability
  is ever authored, though none is proposed by this document).
- **Wider, tougher "Hide" nodes throughout** in place of Human's "skin/wall" generic nodes
  — reflects size (`creature:size_large`, DEC-080) and the armored-hide theme already
  implied by DEC-088's freezing-gated Armor Tag.
- **A location-bound placement recommendation for that Armor Tag** (§4) — DEC-088
  establishes *that* the Ice Troll has a freezing-gated Armor Tag; it does not say *where*
  on the body it is bound. This document proposes an answer.

---

## 3. Ice Troll Location Address Tree

Assumption (flagged, see §6 Question 1): **DEC-100's Tier-1 quartile ranges are reused
unchanged** (Legs 1–25, Torso 26–50, Arms 51–75, Head 76–100) on the grounds that Ice Troll
is bipedal and humanoid-shaped (two legs, two arms, one head, one torso), so the *quartile*
split itself needs no reinvention even though DEC-041(5) authorizes a fully bespoke
Tier-1 if a creature's body plan required it (a quadruped or non-humanoid would).

### 3.1 Legs (1–25)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Thigh | 1–15 | 15 | Wider than Human's 13 — thicker, more powerful troll legs |
| 2 | Shin / Calf | 16–21 | 6 | |
| 3 | Foot (parent) | 22–25 | 4 | Four claws, not five |
| 4 | — Great Claw | 22 | 1 | |
| 4 | — Second Claw | 23 | 1 | |
| 4 | — Third Claw | 24 | 1 | |
| 4 | — Outer Claw (fused ring/little digit) | 25 | 1 | |

### 3.2 Torso (26–50)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Chest / Upper Torso (parent) | 26–40 | 15 | Barrel-chested |
| 3 | — Hide / Chest wall | 26–34 | 9 | Thick armored hide — generic, wide |
| 3 | — Lung | 35–36 | 2 | |
| 3 | — Heart | 37 | 1 | |
| 3 | — Ice Gland | 38 | 1 | New content: frost-themed internal organ, adjacent to Heart |
| 3 | — Neck | 39–40 | 2 | Short/thick — narrow target |
| 2 | Abdomen / Lower Torso (parent) | 41–47 | 7 | |
| 3 | — Abdominal Hide | 41–43 | 3 | |
| 3 | — Stomach | 44 | 1 | |
| 3 | — Liver | 45 | 1 | |
| 3 | — Intestines | 46 | 1 | |
| 3 | — Kidney | 47 | 1 | Paired; side by parity |
| 2 | Pelvis / Groin | 48–49 | 2 | |
| 2 | Spine | 50 | 1 | |

### 3.3 Arms (51–75)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Upper Arm | 51–64 | 14 | Long, thick — the classic troll long-reach silhouette |
| 2 | Forearm | 65–71 | 7 | |
| 3 | Hand (parent) | 72–75 | 4 | Four claws, matching the Foot convention |
| 4 | — Thumb-Claw | 72 | 1 | |
| 4 | — Index-Claw | 73 | 1 | |
| 4 | — Middle-Claw | 74 | 1 | |
| 4 | — Outer-Claw (fused ring/little digit) | 75 | 1 | |

### 3.4 Head (76–100)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Skull | 76–90 | 15 | Thick, heavy — includes vestigial ear tissue (no separate Ears node) |
| 2 | Face (parent) | 91–100 | 10 | |
| 3 | — Eyes | 91–92 | 2 | Small, deep-set — narrow, per the troll archetype |
| 3 | — Nose | 93–94 | 2 | |
| 3 | — Jaw / Tusks | 95–100 | 6 | Prominent underbite and tusks — wide, the dominant facial feature |

**Totals check:** Legs 15+6+4=25; Torso 15+7+2+1=25 (Chest 15, Abdomen 7, Pelvis 2, Spine
1); Arms 14+7+4=25; Head 15+10=25. Sum = 100. ✓

### 3.5 Laterality

Same convention as Human (§5.5 of the prior proposal): parity of the raw Zero-Step index,
odd = Left, even = Right, applied only where a genuine bilateral counterpart exists (limbs,
digits, Lung, Kidney, Eyes). Midline nodes (Heart, Ice Gland, Neck, Spine, Pelvis/Groin,
Skull, Hide/wall nodes, Stomach, Liver, Intestines, Nose, Jaw/Tusks) discard the parity
flag.

*Worked example:* index **73** → `Arm.Hand.Index-Claw`; 73 is odd → **Left Index-Claw**.
Index **38** → `Torso.Chest.Ice Gland`; midline, parity discarded.

---

## 4. Armor Tag Placement (DEC-088 / DEC-062 worked application)

DEC-088 establishes that the Ice Troll's icy-hide Trait is a **Conditional-Trait Binding**:
an Armor Tag (`defense:armor`) active only while `env:freezing` is present in the scene.
It does not specify *where* that Tag is bound. This proposal recommends registering it at
**three Tier-1 nodes** — `Torso`, `Arms`, `Legs` — but **not** `Head`:

| Zone | Armor Tag registered? | Rationale |
|---|:---:|---|
| Torso | Yes | Core mass, thickest hide |
| Arms | Yes | Same hide continues down the limbs |
| Legs | Yes | Same hide continues down the limbs |
| Head | **No** | Face is comparatively exposed/soft tissue; keeps Eyes/Jaw as genuine soft targets rather than trivializing called shots to the head |

Per **DEC-112 L-007**, each of the three registrations automatically covers *every*
descendant node under it — e.g., a Tier-4 hit resolving to `Arm.Hand.Middle-Claw` is
covered by the Arms-level registration without a separate per-digit Armor Tag entry. Per
DEC-088, all three registrations vanish simultaneously the instant `env:freezing` is no
longer present in the scene (the whole Trait, not just its magnitude, is treated as absent
— no partial-armor state).

This placement is a **content choice**, not a forced consequence of any rule — see §6
Question 2.

---

## 5. Resolution Ceiling (same issue, same recommendation)

The Human proposal (§3) already identified the tension between DEC-112 L-005's uncapped
Skill-Tier→Tier mapping and the finite 100-state address space. That analysis and its
recommended fix — **Terminal-Leaf Saturation**: the tree stops at the digit/organ layer,
and any Skill-Tier beyond what a given branch's deepest node supports resolves to that
same terminal node with no new address — apply identically here and are not re-derived.
Ice Troll's tree in §3 is already built to that ceiling (four-layer maximum depth, same as
Human's).

---

## 6. Open Questions for Tiwa's Ruling

1. **Does DEC-100's Tier-1 quartile split apply to every bipedal humanoid creature, or
   does DEC-041(5)'s "not a shared scheme" require even Tier 1 to be bespoke per
   creature?** This proposal assumes the former (§3 preamble) since Ice Troll's body plan
   is humanoid. A quadruped or radically non-humanoid creature would clearly need its own
   Tier-1 split; whether a *humanoid but oversized* creature like Ice Troll still qualifies
   for the shared Tier-1 baseline is the open point.
2. **Armor Tag placement (§4).** Torso+Arms+Legs / not Head is a specific proposal, not a
   determined fact. An alternative — full-body coverage including a hardened brow/skull
   plate — is equally defensible for a "troll" archetype and would change which called
   shots remain viable against this creature.
3. **Four-digit hands/feet and the missing Ears node (§2) are invented anatomy**, not
   drawn from any existing Ice Troll source material in this repository. If a working
   Ice Troll stat block already exists elsewhere with different assumptions (five digits,
   distinct ear anatomy, different size class), this template should be reconciled to it
   rather than treated as authoritative on its own.
4. **The "Ice Gland" organ (§3.2) is wholly new content** with no mechanical hook proposed
   here (no Effect currently reads it). It is offered only as a plausible future anchor
   point for frost-themed Wound content; Tiwa may reject it outright with no loss to the
   rest of the template, since removing it only requires re-widening its 1-number range
   into the adjacent Heart or Lung node.
5. **Regrowth interaction (DEC-088/DEC-110) requires no template change**, noted here only
   for completeness: because Wound records already carry their full address (DEC-112
   L-013) independent of this template's content, the existing Regrowth Condition Clause
   and Heal Effect System (DEC-121/127) apply to any Ice Troll Wound record — including
   severed-claw Wounds — with no new mechanism needed. This is an observation, not a
   proposal requiring a decision.

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
| 38 | Torso.Chest.Ice Gland | mid |
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

## Appendix B — Human vs. Ice Troll: Template Divergence Summary

| Feature | Human | Ice Troll | Why it differs |
|---|---|---|---|
| Digits per hand/foot | 5 | 4 | Fantasy-troll archetype; content choice |
| External Ears as a distinct node | Yes | No (folded into Skull) | Vestigial/skin-covered ears |
| Unique internal organ | — | Ice Gland | Frost theme; anchor for possible future content |
| Widest single Tier-2 node | Skull (13) / Thigh (13) — tied | Skull (15) | Larger overall size class |
| Armor Tag registration | None proposed (Human has no innate hide armor) | Torso + Arms + Legs, freezing-gated (DEC-088) | Species-specific Trait |
| Tier-1 quartile ranges | DEC-100 (authoritative for Human) | DEC-100 reused by assumption (§6 Q1) | Open — see Question 1 |

---

**End of proposal.** No DEC assigned. No canonical or non-canonical ruling recorded by this
document. Per DEC-077.A, this conversion candidate remains provisional until Tiwa reviews,
edits, or rejects it — and should be checked against any existing Ice Troll working stat
block for consistency before use.
