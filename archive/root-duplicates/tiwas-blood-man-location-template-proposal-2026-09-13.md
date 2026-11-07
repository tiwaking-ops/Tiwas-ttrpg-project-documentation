---
document:
  title: "Tiwas — Blood Man Location Address Template (DEC-112 L-004): Advisory Design Proposal"
  version: "0.1 (draft — not executed, not ruled)"
  status: "Advisory / Non-canonical. No DEC assigned. Pending Tiwa's review, edit, or rejection. Content-authoring only, under the DEC-077.A conversion workflow (Blood Man is the second of the two creatures authorized for that workflow)."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  created_date: "2026-09-13"
  last_modified_date: "2026-09-13"
---

# Tiwas — Blood Man Location Address Template

**Status: Advisory content-authoring proposal only.** This is a third worked instance of
**DEC-112 L-004**, and the first one deliberately chosen to **stress-test** the assumption
carried unexamined through the Human and Ice Troll proposals: that DEC-100's Tier-1
quartile split (Legs/Torso/Arms/Head, 25 states each) is a safe default for any bipedal
creature. Blood Man was selected specifically because its body plan is **provisionally
humanoid but not structurally fixed** — a useful edge case. As with the Ice Troll
proposal, **nothing here is canonical, ruled, or DEC-numbered**, and per DEC-077.A, Tiwa
retains final authorship over each conversion element.

**Same scope caveat as the Ice Troll proposal applies:** this document has no access to
the source GURPS stat block, imports no GURPS numbers (DEC-085 cl.3), and everything below
is new anatomical content consistent with the "Blood Man" name and the one confirmed
behavior already on record (DEC-083: a single-application, non-DoT "Blood Seep" Effect
triggered on a successful Grapple win). If a working stat block already fixes body-plan
details differently, that stat block should win.

---

## 1. Working Concept

Blood Man is treated here as an animate, roughly man-shaped mass of coagulated blood/ichor
held into a semi-stable silhouette by whatever force animates it — **not** a creature with
a skeleton, discrete organs, or fixed-position limbs. It maintains a humanoid *outline*
(a main mass plus limb-like protrusions and a denser upper "head" clot) well enough that
naming it "Blood Man" makes sense, but its "limbs" are **reformable pseudopods**, not
persistent anatomical structures — it can partially reabsorb and re-extrude them between
exchanges.

This single design choice is what forces the divergence from Human/Ice Troll in §2 below.

---

## 2. Does DEC-100 Reuse Survive Contact With This Creature? — No.

The Ice Troll proposal reused DEC-100's four-way quartile split because Ice Troll's limbs,
whatever their internal content, are **persistent, individually identifiable structures**
(a specific left arm stays the left arm across an entire encounter). Blood Man's
protrusions are **not** persistent in that sense — there is no stable "left arm" for a
Location Index to keep pointing at, because the creature can reabsorb and reform its
pseudopods between exchanges. Treating two of its four DEC-100 quartiles as "Arms" and
"Legs" would silently assert an anatomical permanence the creature doesn't have.

**Recommendation (flagged, not a ruling — see §6 Question 1): author a bespoke Tier-1
split for Blood Man**, per DEC-041(5)'s explicit "individual templates... not a shared
scheme" allowance, rather than reusing DEC-100. Proposed three-way split, still spanning
the same 1–100 Zero-Step output range and still governed by the same deterministic,
single-source mechanism (DEC-112 L-003) — only the **top-level categories** change:

| Tier-1 Zone | Range | Width | What it represents |
|---|---:|---:|---|
| Core Mass | 1–60 | 60 | The undifferentiated bulk of the creature — most of its total volume |
| Pseudopod | 61–90 | 30 | Any currently-extended limb-like protrusion (no left/right identity — see §4) |
| Head-Clot | 91–100 | 10 | The denser, semi-permanent upper mass that directs the creature's behavior |

This is a genuinely different **shape**, not just different labels on DEC-100's numbers —
Core Mass alone is 60% of the address space (versus Torso's 25% for Human/Ice Troll),
because most of Blood Man's body is one continuous, undifferentiated thing. Arms and Legs
are **merged into one "Pseudopod" category** because the distinction between "an arm" and
"a leg" is not meaningful for a creature that reshapes the same mass to do either job.

**What does *not* change:** Zero-Step itself (DEC-014), the single-source deterministic
mechanism (L-003), the parent-covers-child rule (L-007), and the Skill-Tier ≥ 2 gate
(DEC-041(1)) all apply exactly as they do for Human and Ice Troll. Only the **content** of
the template — how many top-level zones exist and what they represent — is bespoke. This
is the actual boundary of "shared scheme" the earlier open question was probing: the
**mechanism** is shared; a specific **numeric template** (like DEC-100's) is not
automatically portable to every creature.

---

## 3. Blood Man Location Address Tree

### 3.1 Core Mass (1–60)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Outer Slurry | 1–52 | 52 | The bulk of the creature; a hit here passes through semi-liquid mass with no fixed internal structure to damage precisely |
| 2 | Core Clot | 53–60 | 8 | A denser inner mass — the closest thing this creature has to a vital organ; functions as this template's "Heart"-equivalent |

*(No Tier-3+ content authored for Core Mass — the Outer Slurry genuinely has no further
anatomical distinctions to make, and the Core Clot is already the terminal vital target.
This branch saturates at Tier 2.)*

### 3.2 Pseudopod (61–90)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Limb-Mass | 61–82 | 22 | The generic length of whatever protrusion is currently extended |
| 2 | Grasping Tip (parent) | 83–90 | 8 | The business end used for grappling (per DEC-083's Blood Seep trigger) |
| 3 | — Grasping Pad | 83–87 | 5 | Generic contact surface |
| 3 | — Barbed Extrusion | 88–90 | 3 | The specific offensive structure; narrower, more dangerous/vital-adjacent |

*(This branch saturates at Tier 3 — one layer deeper than Core Mass or Head-Clot, because
the Grasping Tip is the creature's primary offensive structure and warrants the extra
distinction.)*

### 3.3 Head-Clot (91–100)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Generic Head Mass | 91–97 | 7 | |
| 2 | Directive Node | 98–100 | 3 | The creature's actual sensory/behavioral locus — this template's most vital single target |

*(Saturates at Tier 2.)*

**Totals check:** Core Mass 52+8=60; Pseudopod 22+5+3=30; Head-Clot 7+3=10. Sum = 100. ✓

---

## 4. Laterality — Does It Even Apply Here?

DEC-041(3)/L-008 compute laterality mechanically from the parity of the raw Zero-Step
index regardless of creature type — that computation is unconditional and is **not**
being changed here. What *is* an open design question is whether that parity bit should
be given any **narrative meaning** for this creature.

For Human and Ice Troll, "Left" and "Right" name persistent, individually trackable
structures — a Wound on the Left Hand stays meaningfully distinct from one on the Right
Hand for the rest of the encounter. For Blood Man's Pseudopods, there is no such
persistence: the "left" pseudopod struck this exchange may already be reabsorbed and a new
one extruded elsewhere by the next exchange.

**Recommendation (flagged, see §6 Question 2):** compute parity as normal (no mechanical
change — Wound records still need *some* deterministic tag), but do not present it to the
GM/player as "Left"/"Right." Instead, label the two parity states **"Pseudopod A"** and
**"Pseudopod B"** — arbitrary, non-anatomical identifiers that only matter for
same-Tier-and-location Wound *stacking* purposes (DEC-035.A cl.4: same-tier + same-location
+ same-target wounds stack). This preserves the mechanical function of parity (distinguishing
two possible Wound-record buckets so they don't over-stack) without asserting a persistent
anatomy the creature doesn't have.

Core Mass and Head-Clot nodes are all midline/singular — parity is computed but discarded
for them, identically to Human and Ice Troll's midline nodes.

*Worked example:* index **89** → `Pseudopod.Grasping Tip.Barbed Extrusion`; 89 is odd →
labeled **Barbed Extrusion (Pseudopod A)**, not "Left Barbed Extrusion."

---

## 5. Armor and Regeneration — No Template Change Needed

Blood Man has no hide/carapace analog proposed here (unlike Ice Troll's DEC-088 Armor
Tag) — a liquid creature has nothing for an Armor Tag to bind to in the conventional
sense, and no Armor Tag is proposed by this document. If Tiwa wants Blood Man to have some
form of damage mitigation, it would more plausibly be authored as a Regeneration/Regrowth
Trait (DEC-110, content-authored per creature) rather than an Armor Tag — reabsorbing and
redistributing mass rather than blocking it. This is a content suggestion, not a proposal
requiring a decision here.

As with Ice Troll, **no template change is needed** to support future Regeneration content:
Wound records carry their full address regardless of this template's contents (DEC-112
L-013), so whatever healing/reabsorption mechanic Tiwa eventually authors for Blood Man
applies uniformly to any node in §3 without further design work.

DEC-083's Blood Seep (a single-application Effect triggered on a Grapple win) is not
currently location-gated at all — it does not consume this template. If a future ruling
ever makes Blood Seep location-referencing, the natural anchor point would be the
`Pseudopod.Grasping Tip` branch, since that is already identified as the creature's
grappling structure (§3.2). Noted for forward reference only; not proposed as a change.

---

## 6. Open Questions for Tiwa's Ruling

1. **Is a bespoke Tier-1 split actually warranted here, or does "humanoid enough to be
   named Man" mean DEC-100 should still apply, with Blood Man's amorphousness expressed
   only in weaker Tier-2+ content (e.g., an Arms quartile whose Tier-2 nodes are just
   "generic mass" rather than Upper Arm/Forearm)?** §2 argues for the bespoke split
   because Arms/Legs would misrepresent a body plan with no persistent limb identity, but
   the alternative (keep DEC-100, weaken only the content beneath it) is a real
   alternative that trades architectural honesty for cross-creature table consistency
   (every creature's Zero-Step index would land in one of the same four named quartiles,
   which might matter for GM-facing UX even if it's a fiction for this creature).
2. **Should Pseudopod laterality be relabeled ("Pseudopod A/B") or simply suppressed
   entirely (no laterality distinction recorded at all for this zone, treating all
   Pseudopod Wounds as one undifferentiated bucket)?** §4 recommends relabeling
   (preserves the DEC-035.A stacking distinction Wound records rely on); full suppression
   is simpler but means two simultaneous Pseudopod Wounds from different exchanges always
   stack together regardless of which parity they rolled, which changes accumulation
   behavior from every other creature template.
3. **Core Clot's width (8/100 — over three times the size of Human's Heart or Ice
   Troll's Heart+Ice Gland combined) is a deliberate compensation** for this creature
   having only one vital-organ-equivalent instead of five. Reasonable, but a genuine
   design choice rather than a forced one — a narrower Core Clot (matching Human/Ice
   Troll's ~1–2% vital-organ convention) is equally defensible and would make this
   creature's single vital point proportionally harder to hit rather than easier.
4. **No Armor Tag or Regeneration content is proposed (§5)** — this is a gap flag, not a
   design recommendation. Some in-genre "blood creature" versions regenerate rapidly or
   are resistant to piercing/slashing damage in favor of vulnerability to fire/cold; none
   of that is decided here.

---

## Appendix A — Consolidated Quick-Reference Table (all 100 values)

| Index | Address | Parity label |
|---:|---|:---:|
| 1–52 | Core Mass.Outer Slurry | — (midline) |
| 53–60 | Core Mass.Core Clot | — (midline) |
| 61–82 | Pseudopod.Limb-Mass | A/B |
| 83–87 | Pseudopod.Grasping Tip.Grasping Pad | A/B |
| 88–90 | Pseudopod.Grasping Tip.Barbed Extrusion | A/B |
| 91–97 | Head-Clot.Generic Head Mass | — (midline) |
| 98–100 | Head-Clot.Directive Node | — (midline) |

---

## Appendix B — Three-Template Comparison (Human / Ice Troll / Blood Man)

| Feature | Human | Ice Troll | Blood Man |
|---|---|---|---|
| Tier-1 source | DEC-100 (authoritative) | DEC-100 (reused by assumption) | **Bespoke** (DEC-100 not reused — §2) |
| Number of Tier-1 zones | 4 | 4 | **3** |
| Widest Tier-1 zone | Torso — 25 | Torso — 25 | **Core Mass — 60** |
| Discrete left/right limb identity | Persistent | Persistent | **Not persistent** — relabeled A/B (§4) |
| Deepest address Tier reached | 4 (digits/organs) | 4 (claws/organs) | **3** (Grasping Tip only; most branches saturate at 2) |
| Innate Armor Tag | None | Torso+Arms+Legs, freezing-gated | **None proposed** |
| Vital-target convention | Narrow (Heart, 1/100) | Narrow (Heart+Ice Gland, 2/100) | **Wide** (Core Clot, 8/100 — flagged, §6 Q3) |

**Conclusion this comparison supports (recommendation, not a ruling):** the part of
DEC-112's architecture that is genuinely universal is the **mechanism** — Zero-Step,
single-source determinism, parent/child coverage, and the Skill-Tier≥2 gate. The part
that is **not** universal, and must be re-examined per creature rather than assumed, is
the **specific quartile template** DEC-100 supplies for Human-like anatomy. Ice Troll was
close enough to reuse it safely; Blood Man was not. Future creature templates should ask
the §2 question explicitly rather than defaulting to DEC-100 by habit.

---

**End of proposal.** No DEC assigned. No canonical or non-canonical ruling recorded by this
document. Per DEC-077.A, this conversion candidate remains provisional until Tiwa reviews,
edits, or rejects it — and should be checked against any existing Blood Man working stat
block for consistency before use.
