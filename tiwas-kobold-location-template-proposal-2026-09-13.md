---
document:
  title: "Tiwas — Kobold Location Address Template (DEC-112 L-004): Advisory Design Proposal"
  version: "0.1 (draft — not executed, not ruled)"
  status: "Advisory / Non-canonical. No DEC assigned. Pending Tiwa's review, edit, or rejection. NOT a DEC-077.A conversion candidate; NOT prior-referenced anywhere in the register — see §0 Provenance Flag (same posture as Orc)."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  created_date: "2026-09-13"
  last_modified_date: "2026-09-13"
---

# Tiwas — Kobold Location Address Template

**Status: Advisory content-authoring proposal only.** Seventh worked instance of
**DEC-112 L-004**. Kobold is chosen for what it adds to the method, not for testing DEC-100
reuse again in the abstract: it is unambiguously a stable-limbed biped (reuse holds, no
debate — see §2), but it has a genuine anatomical feature none of the humanoid templates so
far have had — **a tail** — while Dragon (the only prior template with a tail) is not
humanoid at all. This tests a **third pattern**, between "clean reuse, no new features"
(Ice Troll, Goblin, Orc) and "full bespoke rebuild" (Blood Man, Dragon): **reuse DEC-100's
shape, but add a genuinely new feature by carving space from an existing branch rather
than inventing a new Tier-1 zone.**

## 0. Provenance Flag — Read Before the Rest of This Document

Same posture as the Orc proposal (§0 there): **no register mention anywhere in this
repository.** Not a DEC-077.A conversion candidate (not Ice Troll or Blood Man), and unlike
Goblin/Dragon there is no DEC-084-style precedent either — nothing has ever specifically
addressed a Kobold in this project. DEC-077's unqualified default (creature content is
Tiwa's own authored content via playtesting) applies in full, with no softening precedent
to lean on. Advisory candidate input only, zero presumption of acceptance.

---

## 1. Working Concept

A small, reptilian, scaled humanoid — thin build, a short tail, clawed hands and feet, a
snouted reptilian face with small teeth and slit-pupil eyes, and (per the common trope)
notable physical fragility despite the draconic-adjacent scales. Biologically a stable
biped in every sense that matters for §2.

## 2. DEC-100 Reuse — Clean, No Hedge

Same conclusion as Goblin and Orc: persistent, individually identifiable limbs → DEC-100's
Tier-1 quartile ranges reused unchanged (Legs 1–25, Torso 26–50, Arms 51–75, Head 76–100).
`creature:size_small` (DEC-080), matching Goblin's size class. The interesting design work
in this template is entirely below Tier 1 (§3) and specifically in **how a tail gets added
to a template that was never designed with one** (§3.2, §4).

---

## 3. Kobold Location Address Tree

### 3.1 Legs (1–25)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Thigh | 1–10 | 10 | Smallest Thigh node of any template so far — slight build |
| 2 | Shin / Calf | 11–17 | 7 | |
| 3 | Foot (parent) | 18–25 | 8 | **Three digits, not five** — a tridactyl, lizard-like foot |
| 4 | — Sole / Heel (generic) | 18–19 | 2 | |
| 4 | — Inner Claw | 20–21 | 2 | |
| 4 | — Middle Claw | 22–23 | 2 | |
| 4 | — Outer Claw | 24–25 | 2 | |

### 3.2 Torso (26–50) — the Tail lives here

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Chest / Upper Torso (parent) | 26–37 | 12 | |
| 3 | — Ribs / Chest wall (scaled) | 26–32 | 7 | |
| 3 | — Lung | 33–34 | 2 | |
| 3 | — Heart | 35 | 1 | |
| 3 | — Neck | 36–37 | 2 | |
| 2 | Abdomen / Lower Torso (parent) | 38–50 | 13 | |
| 3 | — Abdominal Wall | 38–42 | 5 | |
| 3 | — Stomach | 43 | 1 | |
| 3 | — Liver | 44 | 1 | |
| 3 | — Intestines | 45 | 1 | |
| 3 | — Pelvis / Groin | 46 | 1 | |
| 3 | — Spine | 47 | 1 | |
| 3 | — **Tail** | 48–50 | 3 | **New sub-node, not present in any prior humanoid template** — see §4 for why it's here rather than a Tier-1 zone |

### 3.3 Arms (51–75)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Upper Arm | 51–60 | 10 | Thin |
| 2 | Forearm | 61–67 | 7 | |
| 3 | Hand (parent) | 68–75 | 8 | **Four digits, not five** — matches neither Human/Goblin/Orc (5) nor exactly Ice Troll's convention (4, but themed as troll-claws, not lizard-claws) |
| 4 | — Thumb-Claw | 68–69 | 2 | |
| 4 | — Index-Claw | 70–71 | 2 | |
| 4 | — Middle-Claw | 72–73 | 2 | |
| 4 | — Outer-Claw | 74–75 | 2 | |

*(Note the deliberate asymmetry: four fingers, three toes. Every prior template kept
matching hand/foot digit counts — this is the first one that doesn't, reflecting a common
depiction of reptilian feet as more reduced than hands. Flagged as a genuine departure, not
an oversight.)*

### 3.4 Head (76–100)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Skull (small horns) | 76–85 | 10 | |
| 2 | Face (parent) | 86–100 | 15 | No distinct Ears node (folded into Skull, as with Human/Ice Troll/Orc — the Goblin emphasis on ears was that creature's trope specifically, not a default) |
| 3 | — Eyes (slit-pupil) | 86–87 | 2 | |
| 3 | — Snout / Nose | 88–92 | 5 | Reptilian snout — wider than any prior template's Nose node, the defining facial feature here |
| 3 | — Jaw / Teeth | 93–100 | 8 | Widest Jaw/Teeth node of any template — many small sharp teeth, the kobold's primary natural weapon |

**Totals check:** Legs 10+7+8=25; Torso 12+13=25 (Chest 7+2+1+2=12; Abdomen
5+1+1+1+1+1+3=13); Arms 10+7+8=25; Head 10+15=25 (Face 2+5+8=15). Sum = 100. ✓

### 3.5 Laterality

Standard convention (persistent limbs, no relabeling needed). Applies to: all Leg and Arm
nodes, Lung, Eyes. Discarded (midline) for: Heart, Neck, Abdominal Wall, Stomach, Liver,
Intestines, Pelvis/Groin, Spine, **Tail** (a single midline appendage, not paired — parity
computed but discarded, same treatment as Human's Spine), Skull, Snout/Nose, Jaw/Teeth.

*Worked example:* index **49** → `Torso.Abdomen.Tail`; midline, parity discarded — there is
only one tail, not a left/right pair.

---

## 4. Why the Tail Is a Sub-Node, Not a Tier-1 Zone

Dragon's Tail got a full Tier-1 zone (15/100 — a major weapon-grade appendage). Kobold's
tail is proposed here as a **minor balancing feature** — thin, not primarily offensive —
and is given a modest 3-number sub-node under Torso's Lower Torso branch instead. This is
a genuinely different design pattern from anything the prior six templates demonstrated:

- **Ice Troll, Goblin, Orc:** reuse DEC-100's shape, adjust only the *proportions* and
  *content* of existing branches. No new named anatomical feature.
- **Blood Man, Dragon:** the creature's shape doesn't match DEC-100 at all → full bespoke
  Tier-1 rebuild.
- **Kobold (this document):** reuse DEC-100's shape *and* successfully add a genuinely new
  named feature, by finding room for it inside an existing branch rather than needing a
  new top-level zone.

The deciding factor, consistent with how Dragon's Tail was scaled relative to its whole
body: **proportional narrative/mechanical significance.** A appendage important enough to
be a primary weapon or major target (Dragon's tail, 15% of the whole creature) earns
top-level treatment; one that is present and addressable but minor (Kobold's tail, 3% of
the whole creature, nested three levels deep) does not need to displace an existing
Tier-1 zone or shrink the others to make room.

---

## 5. Armor and Regeneration — Content Flags Only

- **No innate Armor Tag proposed**, despite the scaled skin. This is a genuine judgment
  call, not an obvious default — see §6 Question 2. The recommendation here prioritizes the
  common "fragile despite draconic heritage" trope over scale-implies-armor logic, matching
  Goblin/Orc's no-innate-armor stance rather than Ice Troll's or Dragon's armored
  precedent.
- **No Regeneration/Regrowth content proposed** — ordinary mortal creature.
- **Signature-attack anchor point (flavor note, not a proposal):** `Head.Face.Jaw/Teeth`
  (widest node in the template) or `Arm.Hand` are the natural anchors for a bite- or
  claw-based Tier-2 signature attack per DEC-086/087. No such skill is authored here.

---

## 6. Open Questions for Tiwa's Ruling

1. **Acceptance posture (§0)** — no standing precedent at all, as with Orc.
2. **No innate armor despite scaled skin (§5).** The strongest counter-argument: several
   genre conventions (and Dragon's own template in this family) treat scales as
   inherently at least somewhat protective. A minimal, narrow-coverage Armor Tag (e.g.
   Torso only, excluding limbs and face) is a defensible middle ground between "no armor"
   (this draft) and Dragon's near-total coverage, if Tiwa wants scale-logic to have *some*
   mechanical weight without contradicting the fragility trope entirely.
3. **Tail width (3/100) and placement (§4)** — a judgment call with no strong precedent
   to anchor it beyond "smaller than Dragon's tail, proportionally." If Kobold tails are
   meant to matter mechanically (balance, a minor whip attack, a grapple-related Trait),
   3/100 may be too small to reliably address; if purely cosmetic, even that may be more
   granularity than needed.
4. **Asymmetric digit count (4 fingers / 3 toes, §3.3 note)** is new to this template
   family and not validated against any existing convention — flagged as invented content,
   not derived from anything already on record.

---

## Appendix A — Consolidated Quick-Reference Table (all 100 values)

| Index | Address | L/R? |
|---:|---|:---:|
| 1–10 | Leg.Thigh | L/R |
| 11–17 | Leg.Shin/Calf | L/R |
| 18–19 | Leg.Foot.Sole/Heel | L/R |
| 20–21 | Leg.Foot.Inner Claw | L/R |
| 22–23 | Leg.Foot.Middle Claw | L/R |
| 24–25 | Leg.Foot.Outer Claw | L/R |
| 26–32 | Torso.Chest.Ribs/Chest-wall | mid |
| 33–34 | Torso.Chest.Lung | L/R |
| 35 | Torso.Chest.Heart | mid |
| 36–37 | Torso.Neck | mid |
| 38–42 | Torso.Abdomen.Abdominal Wall | mid |
| 43 | Torso.Abdomen.Stomach | mid |
| 44 | Torso.Abdomen.Liver | mid |
| 45 | Torso.Abdomen.Intestines | mid |
| 46 | Torso.Pelvis/Groin | mid |
| 47 | Torso.Spine | mid |
| 48–50 | Torso.Abdomen.Tail | mid |
| 51–60 | Arm.Upper Arm | L/R |
| 61–67 | Arm.Forearm | L/R |
| 68–69 | Arm.Hand.Thumb-Claw | L/R |
| 70–71 | Arm.Hand.Index-Claw | L/R |
| 72–73 | Arm.Hand.Middle-Claw | L/R |
| 74–75 | Arm.Hand.Outer-Claw | L/R |
| 76–85 | Head.Skull | mid |
| 86–87 | Head.Face.Eyes | L/R |
| 88–92 | Head.Face.Snout/Nose | mid |
| 93–100 | Head.Face.Jaw/Teeth | mid |

---

## Appendix B — Seven-Template Comparison

| Feature | Human | Ice Troll | Blood Man | Goblin | Orc | Dragon | Kobold |
|---|---|---|---|---|---|---|---|
| Tier-1 source | DEC-100 | Reused | Bespoke | Reused | Reused | Bespoke | **Reused** |
| Digits (hand/foot) | 5/5 | 4/4 | n/a | 5/5 | 5/5 | n/a (claws, no digit tier) | **4/3 — first mismatch** |
| Distinct Ears node | No | No | n/a | Yes | No | n/a | No |
| Novel named feature added within a reused Tier-1 shape | — | No (proportions only) | n/a | No | No | n/a (bespoke, not reuse) | **Yes — Tail, as a sub-node (§4)** |
| Innate Armor Tag | None | Whole zones, conditional | None | None | None | Sub-zone, permanent | **None (flagged, §6 Q2)** |
| Authorization posture | Own standing | DEC-077.A | DEC-077.A | Weak (DEC-084) | None | Weak (DEC-084) | **None** |

**What Kobold confirms:** the reuse/bespoke split established across the first six
templates was never actually about "can this creature have any unique anatomy" — Ice
Troll, Goblin, and Orc all did, entirely through proportion and content changes within
DEC-100's existing shape. Kobold shows the shape itself can also **gain a genuinely new
named feature** without being forced into Blood Man/Dragon's full-rebuild category,
provided the feature is minor enough to nest inside an existing branch rather than
demanding its own Tier-1 zone. The three-way pattern is now: **reuse-as-is**,
**reuse-with-added-minor-feature**, and **bespoke-rebuild** — decided by whether a new
feature needs a top-level zone or fits inside an existing one.

---

**End of proposal.** No DEC assigned. No canonical or non-canonical ruling recorded by this
document. Per §0, this candidate has no standing precedent at all and requires Tiwa's
explicit acceptance before any further use.
