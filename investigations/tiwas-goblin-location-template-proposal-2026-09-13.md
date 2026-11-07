---
document:
  title: "Tiwas — Goblin Location Address Template (DEC-112 L-004): Advisory Design Proposal"
  version: "0.1 (draft — not executed, not ruled)"
  status: "Advisory / Non-canonical. No DEC assigned. Pending Tiwa's review, edit, or rejection. NOT a DEC-077.A conversion candidate — see §0 Provenance Flag."
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
material (DEC-084-precedented posture, per its §0); storage and assessment confer no
authority, assign no DEC, and amend no ruled text.

# Tiwas — Goblin Location Address Template

**Status: Advisory content-authoring proposal only.** Fourth worked instance of
**DEC-112 L-004**, chosen because Goblins (and Orcs, not covered here) are among the most
common fantasy-genre monsters and are a useful **confirming case**: unlike Blood Man
(§2 of that proposal), a Goblin's body plan is unambiguously stable-limbed humanoid, so
this document tests whether that stability alone is sufficient grounds for DEC-100 reuse —
without any of Blood Man's complications.

## 0. Provenance Flag — Read Before the Rest of This Document

**Goblin content sits in a different authorization posture than Ice Troll and Blood Man.**
Those two are the specific creatures DEC-077.A authorizes for advisory-model drafting (the
GURPS-to-Tiwas conversion workflow). Goblin is **not** part of that authorization. The
governing precedent is **DEC-084**: an earlier advisory-drafted Goblin (and Dragon) from a
different model was explicitly ruled to have **no GURPS stat block in the source
material**, and Tiwa ruled that content should be **kept as Tiwa-authored new content,
outside the DEC-077.A workflow** — not rejected outright, but also not pre-approved by
virtue of being drafted. DEC-077's original bar (creature/campaign content is authored by
Tiwa via playtesting, "not to be drafted by Claude or any advisory model") remains the
default; DEC-084 is the one place that bar was visibly tested for exactly this creature
type, and the resolution was reclassification, not rejection.

This document follows that same posture: it is offered strictly as **advisory candidate
input**, on the same footing as the earlier Perplexity Goblin draft DEC-084 discusses —
not authorized content-authoring, not a conversion, and carrying **no presumption of
acceptance**. If Tiwa wants this content to exist, it needs its own explicit acceptance,
the way the Human, Ice Troll, and Blood Man proposals still do — but starting from a
weaker default than those two, not the same one.

---

## 1. Working Concept

A small, physically weak, numerous humanoid — thin limbs, a proportionally large head
dominated by oversized ears/nose/eyes, a modest pot-belly despite otherwise gaunt build,
and ordinary five-digit hands and feet (a goblin is biologically much closer to Human than
either Ice Troll or Blood Man is). No innate armor or regeneration is proposed; a Goblin
relies on worn equipment (ordinary `state:worn` Tags, DEC-080/081) like a Human would, not
an innate Trait like Ice Troll's freezing-gated hide.

## 2. Does DEC-100 Reuse Hold Here? — Yes, Cleanly

Per the Blood Man proposal's Appendix B conclusion, DEC-100 reuse is safe precisely when a
creature has **persistent, individually identifiable limbs** — a specific left arm stays
meaningfully "the left arm" across an encounter. A Goblin satisfies that trivially; it is
biologically a small Human in every structural respect that matters for this question. This
document reuses **DEC-100's Tier-1 quartile ranges unchanged** (Legs 1–25, Torso 26–50,
Arms 51–75, Head 76–100) without the qualification the Ice Troll proposal needed (§6 Q1 of
that document, still open) and without the rejection Blood Man required. Goblin is the
clean confirming case those two proposals bracket.

Small size (`creature:size_small`, DEC-080) changes **derived statistics elsewhere**
(HP, Energy, etc. — outside this document's scope), not the Tier-1 proportions: DEC-100's
split represents *relative* body-region proportion for a generic humanoid, and a smaller
creature scales uniformly rather than reshaping the split.

---

## 3. Goblin Location Address Tree

### 3.1 Legs (1–25)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Thigh | 1–11 | 11 | Thinner than Human's 13 — gaunt build |
| 2 | Shin / Calf | 12–19 | 8 | Proportionally longer than Human's — gangly-limbed trope |
| 3 | Foot (parent) | 20–25 | 6 | |
| 4 | — Sole / Heel (generic) | 20 | 1 | New relative to Human's tree — a generic catch-all before the toe split |
| 4 | — Hallux | 21 | 1 | |
| 4 | — Second Toe | 22 | 1 | |
| 4 | — Third Toe | 23 | 1 | |
| 4 | — Fourth Toe | 24 | 1 | |
| 4 | — Fifth Toe | 25 | 1 | |

### 3.2 Torso (26–50)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Chest / Upper Torso (parent) | 26–36 | 11 | Narrower than Human's — the trope's thin ribcage |
| 3 | — Ribs / Chest wall | 26–32 | 7 | |
| 3 | — Lung | 33–34 | 2 | |
| 3 | — Heart | 35 | 1 | |
| 3 | — Neck | 36 | 1 | Very narrow — a thin, scrawny neck |
| 2 | Abdomen / Lower Torso (parent) | 37–50 | 14 | **Wider** than Chest — the pot-belly trope, reversed from Human's chest-dominant proportion |
| 3 | — Abdominal Wall / Gut | 37–45 | 9 | Exposed pot-belly; wide/common target |
| 3 | — Stomach | 46 | 1 | |
| 3 | — Liver | 47 | 1 | |
| 3 | — Intestines | 48 | 1 | |
| 3 | — Pelvis / Groin | 49 | 1 | |
| 3 | — Spine | 50 | 1 | |

*(No separate Kidney node — folded into the generic Abdominal Wall; not every creature's
organ list needs to match Human's, per DEC-041(5).)*

### 3.3 Arms (51–75)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Upper Arm | 51–60 | 10 | Thin, wiry |
| 2 | Forearm | 61–68 | 8 | |
| 3 | Hand (parent) | 69–75 | 7 | Ordinary five digits — biologically close to Human |
| 4 | — Thumb | 69 | 1 | |
| 4 | — Index Finger | 70 | 1 | |
| 4 | — Middle Finger | 71 | 1 | |
| 4 | — Ring Finger | 72 | 1 | |
| 4 | — Little Finger | 73 | 1 | |
| 4 | — Palm / Back (generic) | 74–75 | 2 | Mirrors the Foot's Sole/Heel catch-all |

### 3.4 Head (76–100)

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Skull | 76–84 | 9 | Proportionally *smaller* than Human's 13 — "mostly face" trope |
| 2 | Face (parent) | 85–100 | 16 | Much wider than Human's 12 — the defining goblin feature set |
| 3 | — Eyes | 85–87 | 3 | Large, light-sensitive — wider than Human's 2 (nocturnal/underground trope) |
| 3 | — Ears | 88–91 | 4 | Large, pointed — the signature goblin feature; no Human or Ice Troll equivalent gets this much weight |
| 3 | — Nose | 92–95 | 4 | Large, hooked/bulbous |
| 3 | — Jaw / Teeth | 96–100 | 5 | Sharp teeth, mild underbite |

**Totals check:** Legs 11+8+6=25; Torso 11+14=25 (Chest 7+2+1+1=11; Abdomen 9+1+1+1+1+1=14);
Arms 10+8+7=25; Head 9+16=25 (Face 3+4+4+5=16). Sum = 100. ✓

### 3.5 Laterality

Standard convention (parity of the raw Zero-Step index; odd = Left, even = Right),
identical in kind to Human's — Goblin's limbs are just as persistent/individually
identifiable as Human's, so no Blood Man-style relabeling is needed. Applies to: all Leg
and Arm nodes (including Sole/Heel and Palm/Back), Lung, Eyes, Ears. Discarded (midline)
for: Heart, Neck, Abdominal Wall, Stomach, Liver, Intestines, Pelvis/Groin, Spine, Skull,
Nose, Jaw/Teeth.

*Worked example:* index **91** → `Head.Face.Ears`; 91 is odd → **Left Ear**.

---

## 4. Armor, Signature Attack, and Regeneration — Content Flags Only

- **No innate Armor Tag proposed.** A Goblin's protection, if any, comes from ordinary
  worn equipment (`state:worn`, `defense:armor` where applicable) under the standard
  equipment/Tag rules — the same model Human uses, contrasting with Ice Troll's innate
  freezing-gated hide.
- **No Regeneration/Regrowth content proposed.** An ordinary mortal creature; nothing here
  suggests otherwise.
- **Signature-attack anchor point (flavor note, not a proposal):** if a Tier-2 signature
  attack is authored for Goblin per DEC-086/087 (e.g., a knife/shiv-based "Sneak Attack"),
  `Arm.Hand` is the natural anatomical anchor for it, mirroring how Ice Troll's claws
  anchor to its Hand node. No such skill is authored by this document.

---

## 5. Open Questions for Tiwa's Ruling

1. **Acceptance posture (§0).** Unlike Ice Troll/Blood Man, this content has no standing
   authorization at all — the first and primary open question is simply whether Tiwa wants
   this content to exist in the repository as candidate material, independent of anything
   about its anatomical specifics.
2. **Pot-belly proportion reversal (§3.2).** Giving Abdomen (14) more width than Chest (11)
   inverts every other template's chest-dominant convention (Human 15/10, Ice Troll 15/10).
   Defensible for the trope, but a genuine departure worth confirming rather than assuming.
3. **Ear width (4/100, §3.4) is the largest single "small feature" node of any template so
   far** — wider than Human's Eyes+Ears combined (4) and Ice Troll's Eyes+Nose combined
   (4). This directly encodes "ears are iconically important to this creature" into the
   numbers; a narrower, more conventionally-proportioned Ears node is equally defensible if
   that trope emphasis isn't wanted mechanically (as opposed to just narratively).
4. **No Kidney node (§3.2 note)** — an organ-list simplification relative to Human, offered
   without strong justification beyond budget; could be restored by narrowing another
   Abdomen leaf if Tiwa wants full organ-list parity with Human.

---

## Appendix A — Consolidated Quick-Reference Table (all 100 values)

| Index | Address | L/R? |
|---:|---|:---:|
| 1–11 | Leg.Thigh | L/R |
| 12–19 | Leg.Shin/Calf | L/R |
| 20 | Leg.Foot.Sole/Heel | L/R |
| 21 | Leg.Foot.Hallux | L/R |
| 22 | Leg.Foot.Second Toe | L/R |
| 23 | Leg.Foot.Third Toe | L/R |
| 24 | Leg.Foot.Fourth Toe | L/R |
| 25 | Leg.Foot.Fifth Toe | L/R |
| 26–32 | Torso.Chest.Ribs/Chest-wall | mid |
| 33–34 | Torso.Chest.Lung | L/R |
| 35 | Torso.Chest.Heart | mid |
| 36 | Torso.Neck | mid |
| 37–45 | Torso.Abdomen.Abdominal Wall | mid |
| 46 | Torso.Abdomen.Stomach | mid |
| 47 | Torso.Abdomen.Liver | mid |
| 48 | Torso.Abdomen.Intestines | mid |
| 49 | Torso.Pelvis/Groin | mid |
| 50 | Torso.Spine | mid |
| 51–60 | Arm.Upper Arm | L/R |
| 61–68 | Arm.Forearm | L/R |
| 69 | Arm.Hand.Thumb | L/R |
| 70 | Arm.Hand.Index Finger | L/R |
| 71 | Arm.Hand.Middle Finger | L/R |
| 72 | Arm.Hand.Ring Finger | L/R |
| 73 | Arm.Hand.Little Finger | L/R |
| 74–75 | Arm.Hand.Palm/Back | L/R |
| 76–84 | Head.Skull | mid |
| 85–87 | Head.Face.Eyes | L/R |
| 88–91 | Head.Face.Ears | L/R |
| 92–95 | Head.Face.Nose | mid |
| 96–100 | Head.Face.Jaw/Teeth | mid |

---

## Appendix B — Four-Template Comparison (Human / Ice Troll / Blood Man / Goblin)

| Feature | Human | Ice Troll | Blood Man | Goblin |
|---|---|---|---|---|
| Tier-1 source | DEC-100 | DEC-100 (reused) | Bespoke (not reused) | **DEC-100 (reused, no caveat)** |
| Digits per hand/foot | 5 | 4 (clawed) | n/a (Pseudopod) | **5** |
| Distinct Ears node | No (folded into Skull) | No (folded into Skull) | n/a | **Yes — widest Face sub-node of any template (4)** |
| Chest vs. Abdomen proportion | Chest-dominant (15/10) | Chest-dominant (15/10) | n/a | **Abdomen-dominant (11/14) — reversed** |
| Innate Armor Tag | None | Torso+Arms+Legs, freezing-gated | None proposed | **None** |
| Regeneration content | None | Freezing-gated (DEC-088) | Suggested, not authored | **None** |
| Authorization posture | Original proposal (own standing) | DEC-077.A conversion | DEC-077.A conversion | **Neither — advisory candidate only (§0)** |

**What this confirms:** the DEC-100-reuse question (raised by Ice Troll, broken by Blood
Man) resolves cleanly in the affirmative once a creature is simply "a differently-shaped
Human" rather than structurally alien — Goblin needed no hedge at all, unlike Ice Troll's
still-open Question 1. The genuinely load-bearing test is limb persistence, not size,
species, or monstrousness in general.

---

**End of proposal.** No DEC assigned. No canonical or non-canonical ruling recorded by this
document. Per §0, this candidate has a **weaker standing default than the Ice Troll and
Blood Man proposals** and requires Tiwa's explicit acceptance before any further use.
