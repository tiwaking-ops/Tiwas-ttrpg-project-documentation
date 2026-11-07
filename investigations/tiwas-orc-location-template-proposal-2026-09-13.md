---
document:
  title: "Tiwas — Orc Location Address Template (DEC-112 L-004): Advisory Design Proposal"
  version: "0.1 (draft — not executed, not ruled)"
  status: "Advisory / Non-canonical. No DEC assigned. Pending Tiwa's review, edit, or rejection. NOT a DEC-077.A conversion candidate; NOT prior-referenced anywhere in the register — see §0 Provenance Flag."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "buffy/codebuff", version: "not established"}
  last_modified_by_llm: {name: "buffy/codebuff", version: "not established"}
  created_date: "2026-09-13"
  last_modified_date: "2026-09-16"
---

## Purpose and Origin

The file identifies Claude Sonnet 5 as its author (2026-09-13). It was assessed and
stored in `investigations/` by Buffy/Codebuff on 2026-09-16 (advisory storage record
appended to the DEC-112 register entry). It remains advisory, non-canonical candidate
material (no register precedent, per its §0); storage and assessment confer no
authority, assign no DEC, and amend no ruled text.

# Tiwas — Orc Location Address Template

**Status: Advisory content-authoring proposal only.** Fifth worked instance of
**DEC-112 L-004**, and the deliberate counterweight to the Goblin proposal: same "common
fantasy monster" territory, but built as the **brute-strength contrast case** — bigger,
tougher, warrior-built, rather than small/weak/numerous. Anatomically it is the same class
of problem as Goblin (a stable-limbed humanoid), so this document leans less on re-arguing
method and more on showing how the *same* method produces a visibly different template
when the creature concept changes.

## 0. Provenance Flag — Read Before the Rest of This Document

**Orc has a weaker standing than even the Goblin proposal.** Goblin at least has a
governing precedent (DEC-084) establishing that advisory-drafted Goblin content, once
produced, gets reclassified as candidate new-content rather than rejected outright. **Orc
has no register mention anywhere in this repository** — no DEC references it, no prior
advisory draft exists to set precedent one way or the other. DEC-077's original,
unqualified bar applies in full: creature content is Tiwa's own authored content via
playtesting, and this document sits entirely outside that process. It is offered on
exactly the same terms as the Goblin proposal (§0 there) — advisory candidate input,
zero presumption of acceptance — but without even the weak precedent Goblin had.

---

## 1. Working Concept

A tall, heavily-muscled, warrior-built humanoid: broad chest, thick limbs built for
wielding heavy weapons, a robust/thick-boned skull with a pronounced brow ridge, lower
tusks, and deep-set eyes. Biologically close enough to Human/Goblin to be a stable-limbed
humanoid in every sense that matters for §2 below — the contrast with Goblin is entirely
in *proportion and emphasis*, not in structural kind.

## 2. DEC-100 Reuse

Same conclusion as Goblin, for the same reason (persistent, individually identifiable
limbs — see the Blood Man proposal's Appendix B and the Goblin proposal's §2): **DEC-100's
Tier-1 quartile ranges are reused unchanged** (Legs 1–25, Torso 26–50, Arms 51–75, Head
76–100), with no hedge. `creature:size_medium` (DEC-080) is proposed over `size_large` —
Orc is bigger and tougher than Human, but not in the oversized register Ice Troll occupies;
that distinction affects derived statistics elsewhere, not this template's Tier-1 shape.

---

## 3. Orc Location Address Tree

### 3.1 Legs (1–25)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Thigh | 1–14 | 14 | Thick, muscular — matches Human's proportion class, slightly heavier |
| 2 | Shin / Calf | 15–20 | 6 | |
| 3 | Foot (parent) | 21–25 | 5 | Ordinary five-toe structure — no generic catch-all node this time (a deliberate stylistic difference from Goblin's tree, not a rule) |
| 4 | — Hallux | 21 | 1 | |
| 4 | — Second Toe | 22 | 1 | |
| 4 | — Third Toe | 23 | 1 | |
| 4 | — Fourth Toe | 24 | 1 | |
| 4 | — Fifth Toe | 25 | 1 | |

### 3.2 Torso (26–50)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Chest / Upper Torso (parent) | 26–41 | 16 | **Widest Chest node of any template so far** — broad, barrel-chested warrior build |
| 3 | — Ribs / Chest wall | 26–35 | 10 | Large generic target |
| 3 | — Lung | 36–38 | 3 | |
| 3 | — Heart | 39 | 1 | |
| 3 | — Neck | 40–41 | 2 | Thick "bull-neck," but kept at Human's width — thickness ≠ larger target in this model |
| 2 | Abdomen / Lower Torso (parent) | 42–50 | 9 | **Narrower than Goblin's** — a muscled midsection, not a pot-belly; the direct opposite emphasis from the Goblin template |
| 3 | — Abdominal Wall | 42–45 | 4 | Tighter/muscled — less "soft target" width than Goblin's equivalent (9) |
| 3 | — Stomach | 46 | 1 | |
| 3 | — Liver | 47 | 1 | |
| 3 | — Intestines | 48 | 1 | |
| 3 | — Pelvis / Groin | 49 | 1 | |
| 3 | — Spine | 50 | 1 | |

### 3.3 Arms (51–75)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Upper Arm | 51–64 | 14 | Thick, weapon-wielding — largest single Arm node among the humanoid-reuse templates |
| 2 | Forearm | 65–70 | 6 | |
| 3 | Hand (parent) | 71–75 | 5 | Ordinary five digits |
| 4 | — Thumb | 71 | 1 | |
| 4 | — Index Finger | 72 | 1 | |
| 4 | — Middle Finger | 73 | 1 | |
| 4 | — Ring Finger | 74 | 1 | |
| 4 | — Little Finger | 75 | 1 | |

### 3.4 Head (76–100)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Skull | 76–89 | 14 | Thick-boned, pronounced brow ridge — widest Skull node of any template |
| 2 | Face (parent) | 90–100 | 11 | No distinct Ears node (folded into Skull, as with Human) — ears are not this creature's defining feature the way they are Goblin's |
| 3 | — Eyes | 90–91 | 2 | Deep-set, narrow |
| 3 | — Nose | 92–93 | 2 | |
| 3 | — Jaw / Tusks | 94–100 | 7 | Lower tusks and a heavy jaw — the dominant facial feature, wider even than Ice Troll's equivalent (6) |

**Totals check:** Legs 14+6+5=25; Torso 16+9=25 (Chest 10+3+1+2=16; Abdomen 4+1+1+1+1+1=9);
Arms 14+6+5=25; Head 14+11=25 (Face 2+2+7=11). Sum = 100. ✓

### 3.5 Laterality

Standard convention, identical to Human/Goblin (persistent limbs, no Blood Man-style
relabeling needed). Applies to: all Leg and Arm nodes, Lung, Eyes. Discarded (midline) for:
Heart, Neck, Abdominal Wall, Stomach, Liver, Intestines, Pelvis/Groin, Spine, Skull, Nose,
Jaw/Tusks.

*Worked example:* index **39** → `Torso.Chest.Heart`; midline, parity discarded. Index
**64** → `Arm.Upper Arm`; 64 is even → **Right Upper Arm**.

---

## 4. Armor, Toughness, and Regeneration — Content Flags Only

- **No innate Armor Tag proposed**, matching Goblin's stance and diverging from Ice
  Troll's. Across the templates drafted so far, an innate Armor Tag has only been proposed
  for a creature with an explicit supernatural/elemental basis for it (Ice Troll's
  freezing-gated hide, DEC-088); a mundane, if unusually tough, humanoid like Orc is
  proposed to express toughness through ordinary derived statistics (HP, attributes) and
  worn equipment, not a body-bound Trait. Flagged as an emerging pattern across this
  template family, not a rule.
- **No Regeneration/Regrowth content proposed** — an ordinary mortal creature.
- **Signature-attack anchor point (flavor note, not a proposal):** a Tier-2 signature melee
  attack (per DEC-086/087) would naturally anchor to `Arm.Upper Arm`/`Arm.Forearm` given
  the trope's association with heavy two-handed weapons, contrasting with Goblin's
  Hand-anchored knife-work suggestion. No such skill is authored by this document.

---

## 5. Open Questions for Tiwa's Ruling

1. **Acceptance posture (§0)** — the primary question, as with Goblin, and starting from
   an even weaker default given the total absence of prior register engagement.
2. **`size_medium` vs. `size_large` (DEC-080).** §2 proposes medium (bigger/tougher than
   Human but not in Ice Troll's oversized register); a "large" orc variant (ogre-adjacent)
   is a common enough subtype in the genre that Tiwa may want it treated separately rather
   than folded into one template.
3. **Chest/Abdomen proportion (16/9) is the most extreme upper/lower split of any
   humanoid-reuse template so far** — more lopsided than Human's or Ice Troll's 15/10, and
   the direct inverse of Goblin's 11/14. This is a deliberate "opposite of Goblin" design
   choice for the comparison to be legible, not independently justified beyond the trope.
4. **No distinct Ears node** was a judgment call to keep Jaw/Tusks as the single dominant
   facial feature; an alternate design could give Orc modest-but-present Ears (like Human
   implicitly has, just unlabeled) at Jaw/Tusks' expense.

---

## Appendix A — Consolidated Quick-Reference Table (all 100 values)

| Index | Address | L/R? |
|---:|---|:---:|
| 1–14 | Leg.Thigh | L/R |
| 15–20 | Leg.Shin/Calf | L/R |
| 21 | Leg.Foot.Hallux | L/R |
| 22 | Leg.Foot.Second Toe | L/R |
| 23 | Leg.Foot.Third Toe | L/R |
| 24 | Leg.Foot.Fourth Toe | L/R |
| 25 | Leg.Foot.Fifth Toe | L/R |
| 26–35 | Torso.Chest.Ribs/Chest-wall | mid |
| 36–38 | Torso.Chest.Lung | L/R |
| 39 | Torso.Chest.Heart | mid |
| 40–41 | Torso.Neck | mid |
| 42–45 | Torso.Abdomen.Abdominal Wall | mid |
| 46 | Torso.Abdomen.Stomach | mid |
| 47 | Torso.Abdomen.Liver | mid |
| 48 | Torso.Abdomen.Intestines | mid |
| 49 | Torso.Pelvis/Groin | mid |
| 50 | Torso.Spine | mid |
| 51–64 | Arm.Upper Arm | L/R |
| 65–70 | Arm.Forearm | L/R |
| 71 | Arm.Hand.Thumb | L/R |
| 72 | Arm.Hand.Index Finger | L/R |
| 73 | Arm.Hand.Middle Finger | L/R |
| 74 | Arm.Hand.Ring Finger | L/R |
| 75 | Arm.Hand.Little Finger | L/R |
| 76–89 | Head.Skull | mid |
| 90–91 | Head.Face.Eyes | L/R |
| 92–93 | Head.Face.Nose | mid |
| 94–100 | Head.Face.Jaw/Tusks | mid |

---

## Appendix B — Five-Template Comparison (Human / Ice Troll / Blood Man / Goblin / Orc)

| Feature | Human | Ice Troll | Blood Man | Goblin | Orc |
|---|---|---|---|---|---|
| Tier-1 source | DEC-100 | DEC-100 (reused) | Bespoke | DEC-100 (reused) | **DEC-100 (reused)** |
| Digits per hand/foot | 5 | 4 (clawed) | n/a | 5 | **5** |
| Chest : Abdomen ratio | 15 : 10 | 15 : 10 | n/a | 11 : 14 (reversed) | **16 : 9 (most lopsided)** |
| Widest Skull/Face node | Skull 13 | Skull 15 | n/a | Face 16 | **Skull 14 / Jaw-Tusks 7** |
| Distinct Ears node | No | No | n/a | **Yes (4 — largest feature-node)** | No |
| Innate Armor Tag | None | Torso+Arms+Legs, freezing-gated | None proposed | None | **None** |
| Size tag | — | `size_large` | — | `size_small` | **`size_medium`** |
| Authorization posture | Own standing | DEC-077.A conversion | DEC-077.A conversion | Advisory only, weak precedent (DEC-084) | **Advisory only, no precedent at all** |

**What the Goblin/Orc pair confirms:** the same DEC-100-reuse method produces genuinely
different templates for genuinely different concepts without needing new architecture —
Goblin and Orc are structurally identical in *kind* (both cleanly reuse DEC-100, both use
ordinary five-digit humanoid extremities, neither needs Blood Man's bespoke treatment) and
differ entirely in *proportion*. That is the intended division of labor: DEC-112's
mechanism stays fixed; DEC-041(5)'s "individual templates" clause is where all the
creature-specific character actually lives.

---

**End of proposal.** No DEC assigned. No canonical or non-canonical ruling recorded by this
document. Per §0, this candidate has **no standing precedent at all** and requires Tiwa's
explicit acceptance before any further use — more so than any other template in this
family so far.
