---
document:
  title: "Tiwas — Giant Spider Location Address Template (DEC-112 L-004): Advisory Design Proposal"
  version: "0.1 (draft — not executed, not ruled)"
  status: "Advisory / Non-canonical. No DEC assigned. Pending Tiwa's review, edit, or rejection. NOT a DEC-077.A conversion candidate; NOT prior-referenced anywhere in the register — see §0 Provenance Flag (same posture as Orc/Kobold/Hobgoblin)."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "kilo-auto/free", version: "not established"}
    - {name: "buffy/codebuff", version: "not established"}
  last_modified_by_llm: {name: "buffy/codebuff", version: "not established"}
  created_date: "2026-09-13"
  last_modified_date: "2026-09-16"
---

# Tiwas — Giant Spider Location Address Template

## Purpose and Origin

The file identifies Claude Sonnet 5 as its author (2026-09-13); this storage/assessment copy was prepared by kilo-auto/free on 2026-09-16. It remains advisory, non-canonical candidate material; storage and assessment confer no authority, assign no DEC, and amend no ruled text.

**Status: Advisory content-authoring proposal only.** Ninth worked instance of
**DEC-112 L-004**, and the third body plan requiring a fully bespoke Tier-1 split (after
Blood Man and Dragon) — chosen specifically because an arachnid is non-humanoid for a
**third, structurally distinct reason**: not amorphous (Blood Man), not a quadruped-with-
wings-and-tail (Dragon), but a two-segment body (cephalothorax + abdomen) with **eight**
legs. That leg count is the real test this document runs: Dragon validated the
"structural branch × laterality parity" pattern at four legs (2 branches × 2 sides); this
document checks whether it scales cleanly to eight (4 branches × 2 sides), which happens
to be exactly how real arachnid legs are anatomically numbered (Legs I–IV, front to back).

## 0. Provenance Flag — Read Before the Rest of This Document

Same posture as Orc, Kobold, and Hobgoblin: **no register mention anywhere in this
repository**, no DEC-077.A authorization, no DEC-084-style precedent. DEC-077's
unqualified default applies in full. Advisory candidate input only, zero presumption of
acceptance.

---

## 1. Working Concept

A monstrous arachnid: a bulbous, iconic abdomen (the bulk of the visible body, containing
book lungs, heart, and silk-producing organs), a smaller cephalothorax (fused head/thorax,
carrying eyes, venom-delivering fangs, and sensory pedipalps), and eight thin, long legs
arranged in four bilateral pairs. `creature:size_large` (DEC-080) is proposed as a
baseline, in the same register as Ice Troll rather than the small/medium humanoids.

## 2. DEC-100 Reuse — No, for a New Reason

Neither of the two prior "no" cases applies for the same reason here. Blood Man had no
persistent limbs at all; Dragon had persistent limbs but the wrong *count and kind* for a
bipedal split. A Giant Spider has extremely persistent, well-defined limbs — **eight of
them, all the same kind** — which is exactly the situation DEC-100's four-zone
(Legs/Torso/Arms/Head) split has no answer for. This confirms the Blood Man proposal's
Appendix B rule (limb persistence, not size or "monstrousness," decides reuse) generalizes
correctly to a *third* kind of failure mode: **not two limb types in the wrong
arrangement, but one limb type with the wrong multiplicity.**

Bespoke Tier-1 split:

| Tier-1 Zone | Range | Width | What it represents |
|---|---:|---:|---|
| Abdomen | 1–45 | 45 | The large posterior body mass — vital organs, silk glands |
| Cephalothorax | 46–65 | 20 | Fused head/thorax — eyes, fangs, sensory appendages, leg attachment point |
| Legs | 66–100 | 35 | Four leg-pairs (Legs I–IV), each with Left/Right via parity |

---

## 3. Giant Spider Location Address Tree

### 3.1 Abdomen (1–45)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Carapace (dorsal, generic) | 1–30 | 30 | Tough chitin shell; armored (§4) |
| 2 | Book Lung | 31–35 | 5 | Paired respiratory organ |
| 2 | Heart | 36–38 | 3 | |
| 2 | Spinnerets | 39–42 | 4 | Silk-producing organs at the rear; treated as one composite node (§3.4) |
| 2 | Underside / Soft Membrane | 43–45 | 3 | Ventral cuticle — thinner than the dorsal carapace; **not** armored (§4), the closest analogue to Dragon's underbelly weak point |

### 3.2 Cephalothorax (46–65)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Carapace (dorsal, generic) | 46–56 | 11 | Houses the fused ganglia (brain-equivalent); armored (§4) |
| 2 | Eyes | 57–59 | 3 | Composite cluster — see §3.4 for why this isn't parity-paired the way most "Eyes" nodes in this family are |
| 2 | Fangs / Chelicerae | 60–63 | 4 | Venom-delivery structure — the primary weapon; **not** armored (§4), a called-shot-relevant soft/precise target |
| 2 | Pedipalps | 64–65 | 2 | Sensory/feeding appendages; unarmored |

### 3.3 Legs (66–100) — four pairs

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Leg I (frontmost pair) | 66–75 | 10 | |
| 3 | — Upper Leg (coxa–femur) | 66–71 | 6 | Armored (§4) |
| 3 | — Lower Leg (patella–tarsus) | 72–75 | 4 | Thinner joint cuticle; unarmored (§4) |
| 2 | Leg II | 76–84 | 9 | |
| 3 | — Upper Leg | 76–80 | 5 | Armored |
| 3 | — Lower Leg | 81–84 | 4 | Unarmored |
| 2 | Leg III | 85–92 | 8 | |
| 3 | — Upper Leg | 85–88 | 4 | Armored |
| 3 | — Lower Leg | 89–92 | 4 | Unarmored |
| 2 | Leg IV (rearmost pair) | 93–100 | 8 | |
| 3 | — Upper Leg | 93–96 | 4 | Armored |
| 3 | — Lower Leg | 97–100 | 4 | Unarmored |

*(Every leg pair saturates at Tier 3 — the per-leg budget leaves no room for the further
segment-level detail real arachnid legs have (coxa/trochanter/femur/patella/tibia/
metatarsus/tarsus, seven segments); Terminal-Leaf Saturation applies here exactly as it
did for every zone in every prior bespoke template that ran out of numeric budget before
running out of real anatomy.)*

**Totals check:** Abdomen 30+5+3+4+3=45; Cephalothorax 11+3+4+2=20; Legs
(10+9+8+8)=35, i.e. Leg I 6+4=10, Leg II 5+4=9, Leg III 4+4=8, Leg IV 4+4=8. Grand total =
45+20+35=100. ✓

### 3.4 Laterality — validating the pattern at eight legs

Dragon established "structural branch × parity" for four legs (Foreleg/Hindleg × L/R).
Giant Spider extends the identical mechanism one step further: **four structural branches
(Leg I–IV) × parity (Left/Right) = eight distinct addressable legs**, which is not a design
convenience — it is exactly how real arachnid leg pairs are anatomically numbered. The
mechanism did not need to change at all to reach a different, larger, but still exactly
correct limb count. As with Dragon, **one armor registration per branch node covers both
its Left and Right instances automatically** (§4) — laterality never needs its own separate
registration, because it is computed from the raw index, not encoded as an extra tree
branch.

Two nodes in this template get a **new** laterality treatment not seen in any prior
template: **Eyes** and **Spinnerets** are each genuinely multiple in real arachnid anatomy
(most giant-spider depictions carry six or eight eyes in clusters; several species have two
or three spinneret pairs) but don't reduce cleanly to a single Left/Right pair the way a
vertebrate's two eyes do. Both are modeled here as **composite/midline nodes** — parity is
computed on the raw index as always, but discarded, the same treatment as any other midline
structure. This is offered as the correct default for "genuinely multiple but not
bilaterally-paired-in-a-simple-sense" features; see §6 Question 2 for the alternative.

Applies (parity meaningful): Book Lung, and all eight Leg segments (Upper/Lower ×
Leg I–IV). Discarded (midline/composite): Carapace (both instances), Heart, Underside/Soft
Membrane, Eyes, Fangs/Chelicerae, Pedipalps, Spinnerets.

*Worked example:* index **89** → `Legs.Leg III.Lower Leg`; 89 is odd → **Left Leg III,
Lower Leg**. Index **58** → `Cephalothorax.Eyes`; midline/composite, parity discarded.

---

## 4. Armor Placement — Six Registrations, Not Two

Following the same **L-007 parent-coverage exception-carving** pattern the Dragon proposal
used, but exercised at a higher branch count: full coverage requires **six separate
registrations**, not the two or three simpler prior templates needed, because the Legs
zone alone has four independent branches that each need their own Upper-Leg registration
(registering at the Legs Tier-1 parent would incorrectly extend armor into the
deliberately-soft Lower-Leg joints via L-007's normal parent-covers-child behavior):

| Registered at | Covers | Excludes |
|---|---|---|
| `Abdomen.Carapace` | (terminal node) | `Abdomen.Book Lung`, `Heart`, `Spinnerets`, `Underside/Soft Membrane` — none of these are children of Carapace, so none inherit its coverage |
| `Cephalothorax.Carapace` | (terminal node) | `Eyes`, `Fangs/Chelicerae`, `Pedipalps` |
| `Legs.Leg I.Upper Leg` | (terminal node) | `Legs.Leg I.Lower Leg` |
| `Legs.Leg II.Upper Leg` | (terminal node) | `Legs.Leg II.Lower Leg` |
| `Legs.Leg III.Upper Leg` | (terminal node) | `Legs.Leg III.Lower Leg` |
| `Legs.Leg IV.Upper Leg` | (terminal node) | `Legs.Leg IV.Lower Leg` |

The joints (all four Lower Leg nodes) and the fangs/eyes/pedipalps/underside are the
proposed weak points — "sever a leg at the joint" and "strike past the fangs" are both
common genre tropes for fighting giant spiders, and both get direct mechanical support
here rather than being purely narrative.

---

## 5. Venom, Webbing, and Regeneration — Content Flags Only

- **`Cephalothorax.Fangs/Chelicerae` is the natural anchor point** for a venom-related
  Effect (analogous to how Dragon's Nostrils anchors a breath weapon and Ice Troll's Hand
  anchors its claws). No such Effect is authored or proposed here.
- **`Abdomen.Spinnerets` is a plausible anchor point** for any future web/webbing-related
  Effect. Not proposed here either.
- **No Regeneration/Regrowth content proposed** — real arachnids have limited leg
  regrowth across molts, but nothing about a static combat encounter with a "giant spider"
  obviously calls for it; flagged as a content decision if a specific subtype wants it.

---

## 6. Open Questions for Tiwa's Ruling

1. **Acceptance posture (§0)** — no standing precedent, as with Orc/Kobold/Hobgoblin.
2. **Composite/midline treatment of Eyes and Spinnerets (§3.4).** This document proposes
   treating "genuinely multiple but not simply bilateral" features as midline/composite
   rather than inventing a third laterality category beyond "paired" and "midline." An
   alternative — giving Eyes its own internal Tier-3 split (e.g. "Anterior Eye Row" /
   "Posterior Eye Row," still midline) — is more anatomically granular but was not adopted
   here for budget and simplicity reasons; flagged as a genuine design choice rather than a
   forced one.
3. **Six-registration armor coverage (§4)** is more bookkeeping-heavy than any prior
   template's armor proposal. Whether that complexity is worth the mechanical payoff
   (four independently-severable weak-point joints) versus a simpler "Legs entirely
   unarmored, Abdomen/Cephalothorax armored" two-registration model is a genuine tradeoff,
   not a settled one.
4. **Leg-pair proportion (10/9/8/8, front-to-back descending)** reflects a design guess
   that front legs (used for reaching, first contact, and sometimes prey-grappling) are
   marginally more mechanically significant than rear legs (primarily propulsive). Real
   arachnid leg-pair functional differences are more nuanced than this; an equal 35/4≈8.75
   split (not evenly divisible, so not literally available, but a closer-to-equal
   9/9/9/8 split) is an equally defensible simplification.

---

## Appendix A — Consolidated Quick-Reference Table (all 100 values)

| Index | Address | L/R? | Armored? |
|---:|---|:---:|:---:|
| 1–30 | Abdomen.Carapace | mid | Yes |
| 31–35 | Abdomen.Book Lung | L/R | No |
| 36–38 | Abdomen.Heart | mid | No |
| 39–42 | Abdomen.Spinnerets | mid | No |
| 43–45 | Abdomen.Underside/Soft Membrane | mid | **No** |
| 46–56 | Cephalothorax.Carapace | mid | Yes |
| 57–59 | Cephalothorax.Eyes | mid | No |
| 60–63 | Cephalothorax.Fangs/Chelicerae | mid | **No** |
| 64–65 | Cephalothorax.Pedipalps | mid | No |
| 66–71 | Legs.Leg I.Upper Leg | L/R | Yes |
| 72–75 | Legs.Leg I.Lower Leg | L/R | No |
| 76–80 | Legs.Leg II.Upper Leg | L/R | Yes |
| 81–84 | Legs.Leg II.Lower Leg | L/R | No |
| 85–88 | Legs.Leg III.Upper Leg | L/R | Yes |
| 89–92 | Legs.Leg III.Lower Leg | L/R | No |
| 93–96 | Legs.Leg IV.Upper Leg | L/R | Yes |
| 97–100 | Legs.Leg IV.Lower Leg | L/R | No |

---

## Appendix B — Nine-Template Comparison

| Feature | Human | Ice Troll | Blood Man | Goblin | Orc | Dragon | Kobold | Hobgoblin | Giant Spider |
|---|---|---|---|---|---|---|---|---|---|
| Tier-1 source | DEC-100 | Reused | Bespoke | Reused | Reused | Bespoke | Reused | Reused | **Bespoke** |
| Reason reuse fails (if bespoke) | — | — | No persistent limbs | — | — | Wrong limb type/count for a biped | — | — | **Right limb type, wrong multiplicity (8, not 2 or 4)** |
| Limbs of one type in one zone | No | No | n/a | No | No | Yes (4: 2×2) | No | No | **Yes (8: 4×2)** |
| Armor registrations needed for full "mostly armored, deliberate exceptions" coverage | n/a | 3 (whole zones) | n/a | n/a | n/a | 6 | n/a | n/a | **6** |
| Novel laterality treatment | — | — | Relabeled (no persistent side) | — | — | Whole paired Tier-1 zone (Wings) | — | — | **Composite/midline for inherently-multiple features (Eyes, Spinnerets)** |
| Authorization posture | Own standing | DEC-077.A | DEC-077.A | Weak (DEC-084) | None | Weak (DEC-084) | None | None | **None** |

**What Giant Spider confirms:** the "structural branch × parity" solution Dragon
introduced for multi-limb creatures is not specific to four legs — it scales cleanly to
any even limb count by adding more structural branches, and in this case the math happens
to land exactly on real arachnid leg-numbering convention (Legs I–IV) without needing to
be forced. Three bespoke templates in (Blood Man, Dragon, Giant Spider), the reuse/bespoke
boundary from the Blood Man proposal still holds with no exceptions: it has never once
been about size, danger, or "monster-ness" — only about whether the creature is a
stable-limbed **biped**.

---

**End of proposal.** No DEC assigned. No canonical or non-canonical ruling recorded by this
document. Per §0, this candidate has no standing precedent at all and requires Tiwa's
explicit acceptance before any further use.
