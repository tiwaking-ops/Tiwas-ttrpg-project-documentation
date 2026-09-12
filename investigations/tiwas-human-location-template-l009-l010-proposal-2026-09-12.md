---
document:
  title: "Tiwas — Human Location Address Template (DEC-112 L-009 / L-010): Advisory Design Proposal"
  version: "0.1 (draft — not executed, not ruled)"
  status: "Advisory / Non-canonical. No DEC assigned. Pending Tiwa's review, edit, or rejection. Content-authoring only (DEC-077.A framework), not a rules change."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  created_date: "2026-09-12"
  last_modified_date: "2026-09-12"
---

# Tiwas — Human Location Address Template

**Status: Advisory content-authoring proposal only.** This document proposes content for
**DEC-112 items L-009 (Human template)** and **L-010 (100-state numerical allocation)**,
both explicitly deferred to content-authoring by DEC-112. **Nothing in this document is
canonical, ruled, or DEC-numbered.** No mechanic in DEC-001–018 (Locked Canonical Core) or
any Ruled non-canonical decision (DEC-041, DEC-100, DEC-107, DEC-112, DEC-113) is altered.
Where this proposal requires a genuine designer choice beyond pure content-authoring —
because the underlying architecture is silent or under-specified — that choice is flagged
explicitly in §7 as an **open question for Tiwa**, not decided here.

---

## 1. Scope and Constraints

This proposal authors the **Human** Location Address Template under **DEC-112 L-004**
(per-creature-type templates) and closes **L-009**/**L-010** for Human only. It does not
touch other creature templates (Ice Troll, Blood Man, Goblin, Dragon, or future content),
though §8 notes how the same method generalizes.

**Binding constraints inherited from the live register (none reopened, none altered):**

| Constraint | Source | Effect on this proposal |
|---|---|---|
| Tier-1 coarse-zone ranges are locked | DEC-100 | Legs 1–25, Torso 26–50, Arms 51–75, Head 76–100 — **not renegotiable here** |
| Zero-Step is the sole index provider; natural roll untouched | DEC-014, Invariant 6 | All addresses derive from the existing digit-exchange output only |
| Single-source deterministic resolution — **no secondary roll** | DEC-112 L-003, L-011 | The full address path must be recoverable from one d100 value alone |
| Skill-Tier maps directly to Location Tier, no formal cap | DEC-112 L-005 | Deeper Skill-Tier resolves deeper into this template's tree |
| Location Tier = precision depth; Tier 1 = coarse zones | DEC-112 L-006 | Each added Tier subdivides its parent, never redefines it |
| Parent covers all children (armor, wounds) | DEC-112 L-007 | Coverage declared at a coarse node automatically covers every descendant |
| Laterality via Zero-Step digit parity only; no explicit L/R nodes | DEC-041(3), DEC-112 L-008 | This template never encodes "Left"/"Right" as separate numeric branches |
| Mismatch → parent fallback | DEC-112 L-014 | A failed match at a fine node falls back to its coarser parent, not to DEC-030 in the armor-coverage case specifically (DEC-030 remains the fallback for Effect Tag/Location mismatches) |
| Skill-Tier ≥ 2 gate on all location-referencing Effects | DEC-041(1) | Nothing below Tier 2 in this template is ever reachable in play regardless of address depth |

This proposal does **not** revisit DEC-112's supersession of the earlier flat Level 2–5
menu (the old ladder is historical) — it re-expresses the same anatomical content the old
ladder targeted, but as a single deterministic address tree consistent with L-001–L-014.

---

## 2. Research Basis

### 2.1 Real-world anatomical trauma classification

The **Abbreviated Injury Scale (AIS)**, the standard anatomic injury-severity system used
in trauma medicine since 1971, divides the body into **nine chapters**: Head, Face, Neck,
Thorax, Spine, Abdomen/Pelvis, Upper Extremity, Lower Extremity, and External. Its
companion scoring tool, the **Injury Severity Score (ISS)**, collapses these into **six**
practical regions for scoring purposes: Head/Neck, Face, Chest, Abdomen/Pelvic contents,
Extremities/Pelvic girdle, and External.

Two design-relevant takeaways for a Human template:

1. **Neck and Spine are treated as anatomically and clinically distinct from both Head and
   Torso** in real trauma classification, even though no dedicated top-level Tiwas zone
   exists for either (DEC-100 has only four zones). This motivates treating Neck and Spine
   as *sub-zones* rather than omitting them.
2. Internal organ groupings used in trauma coding (thoracic: heart, lungs; abdominal:
   liver, stomach, intestines, kidneys) map naturally onto a "Tier-4 organ layer" within
   Chest and Abdomen.

### 2.2 TTRPG hit-location precedent

| System | Roll mechanism | Location count | Notable design choices |
|---|---|---:|---|
| **GURPS** (4th ed.) | 3d6 (range 3–18) | ~10 base locations, plus penalty-gated sublocations (Vitals, Eye, Ear, Nose, Jaw, Spine, veins/arteries, joints) | Extremities and organs are reached by *voluntary called shot* with an escalating skill penalty rather than a flatter random roll; "miss by 1" on a narrow sublocation redirects to Torso (a **fallback-to-parent** pattern) |
| **RuneQuest / BRP family** (incl. Mythras, OpenQuest) | d20, 7 base locations (Head, Chest, Abdomen, R/L Arm, R/L Leg) | 7 (base); community sub-tables add a further d4 for ~28 fine locations | Each location carries its **own fraction of total HP**, independent of the global pool — a design Tiwas explicitly does not use (Wounds are Skill-Tier-scaled state records, not local HP pools) |
| **Rolemaster (Arms Law)** | d100 attack-result cross-indexed to a location/severity crit table | Location + independent A–E severity letter | Location and *severity* are resolved as separate axes; severity (not location depth) drives narrative consequence — analogous to Tiwas's own separation of Location Tier (DEC-112) from Effect/Wound Tier (DEC-107) |
| **Warhammer 40,000 percentile systems** (Dark Heresy/Rogue Trader lineage) | d100, single roll | 6 (Head, R Arm, L Arm, Body, R Leg, L Leg) | **Percentile ranges are anatomically weighted, not equal-width** — Body received roughly 40% of the range, Legs ~15% each, Arms ~10% each, Head ~10% — directly analogous to what DEC-100 already does for Tiwas's four quartiles |
| **D20 hit-location variants (MERP/Rolemaster-adjacent homebrews)** | d20 crit tables | Variable | "Combat as a fail state": the crit *table entry itself* narrates the anatomical consequence rather than requiring a persistent numeric location record |

**Design conclusions carried into §3–§6:**

- Follow the **percentile-weighted, single-roll** pattern (closest existing precedent to
  DEC-112's single-source model), not GURPS's multi-die/called-shot pattern or BRP's
  location-local-HP pattern (both would require mechanics Tiwas does not have).
- Use **GURPS's fallback-to-parent behavior** as the direct real-world precedent for
  DEC-112 L-014, since it is the closest existing analogue of "narrow miss reverts to the
  coarser containing zone."
- Add **Neck** as a sub-zone (per AIS) and preserve a distinct **Spine** sub-zone, while
  keeping DEC-100's four top-level zones untouched.
- Model internal organs as a genuine Tier-4 layer under Chest/Abdomen (per AIS organ
  groupings and Rolemaster's precedent of granular internal consequences), rather than
  omitting them as GURPS effectively does for anything but Vitals.

---

## 3. The Resolution-Ceiling Problem (flagged before presenting numbers)

DEC-112 L-005 states Skill-Tier maps to Location Tier **with no formal cap**. But the
address space is **finite**: exactly 100 Zero-Step outputs exist, split into four
25-value quartiles by DEC-100. The old (superseded) flat-menu design solved this by
issuing a **separate secondary roll** at each deeper Tier (DEC-042) — but DEC-112 L-011
explicitly **removes** the secondary roll. Under the new single-source model, every
addressable leaf must be a genuine partition of the *original* 25-value quartile, with
no additional dice.

Concretely: Legs alone would need at least 5 leaves just for individual toes, before
Thigh and Shin/Calf even get their own ranges — and if the design pushed to true
phalanx-level detail (per the old ladder's Tier-5 "joint/phalanx segments"), Legs alone
would need on the order of 14+ leaves competing for 25 numbers, leaving almost no room
for anatomically-weighted realism (some leaves would be forced to 0–1% width).

This is a real architectural tension between L-005's "no cap" language and the finite
100-state resolution of a single d100 index. **§7, Question 1** proposes resolving it via
a **Terminal-Leaf Saturation** rule (recommended) rather than silently omitting content.
The numeric tables in §4–§6 stop at the digit/organ layer (the old ladder's "Tier 4") and
treat anything the old ladder called "Tier 5" (phalanx/joint segments) as **narrative-only
color with no independent address**, per that recommendation — flagged, not decided, here.

---

## 4. Address Notation

Each resolved location is recorded as an **ordered path** from the locked Tier-1 zone down
to the deepest node the acting Skill-Tier reaches, plus a laterality flag where the node is
not a midline structure:

```
Location Address = Zone.SubZone[.Region[.Node]] [ (Left|Right) ]
```

Examples: `Torso.Chest.Heart`, `Arm.Hand.Ring (Right)`, `Leg` (Tier 1 only — no deeper
resolution warranted), `Head.Face.Eyes (Left)`, `Torso.Spine`.

The **raw Zero-Step index is retained alongside the address** for auditability (e.g. in a
Wound record per DEC-112 L-013): `Location Index 38 → Torso.Chest.Heart`. This satisfies
DEC-035.A's `Location X` field (X = the raw index) while giving Effects, armor checks, and
narration a stable path to test containment against (L-007).

---

## 5. Human Location Address Tree

All ranges below are **within** the DEC-100 quartile they belong to; quartile boundaries
themselves are unchanged. Range widths follow the anatomically-weighted principle already
established by DEC-041(2) and DEC-100 (larger/central/common targets get wider ranges;
small, awkward, or already-vital targets get narrower ranges) — directly modeled on the
Dark Heresy/Rogue Trader percentile precedent in §2.2.

### 5.1 Legs (1–25) — Tier-1 locked

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Thigh | 1–13 | 13 | Largest single mass in the zone |
| 2 | Shin / Calf | 14–20 | 7 | |
| 3 | Foot (parent of the five toe nodes below) | 21–25 | 5 | Small/awkward target — narrow |
| 4 | — Hallux (big toe) | 21 | 1 | |
| 4 | — Second Toe | 22 | 1 | |
| 4 | — Third Toe | 23 | 1 | |
| 4 | — Fourth Toe | 24 | 1 | |
| 4 | — Fifth Toe (little toe) | 25 | 1 | |

### 5.2 Torso (26–50) — Tier-1 locked

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Chest (Upper Torso, parent) | 26–38 | 13 | |
| 3 | — Ribs / Chest wall | 26–34 | 9 | Generic hit; common/wide |
| 3 | — Lung | 35–37 | 3 | |
| 3 | — Heart | 38 | 1 | Vital; narrow (matches GURPS Vitals treatment) |
| 3 | Neck | 39–40 | 2 | New sub-zone per AIS (§2.1); small target |
| 2 | Abdomen (Lower Torso, parent) | 41–47 | 7 | |
| 3 | — Abdominal wall / Guts | 41–43 | 3 | Generic hit; common/wide |
| 3 | — Stomach | 44 | 1 | |
| 3 | — Liver | 45 | 1 | |
| 3 | — Intestines | 46 | 1 | |
| 3 | — Kidney | 47 | 1 | Paired organ — single leaf; side by parity (§5.5) |
| 2 | Pelvis / Groin | 48–49 | 2 | |
| 2 | Spine | 50 | 1 | New sub-zone per AIS (§2.1); posterior, hard to target directly |

### 5.3 Arms (51–75) — Tier-1 locked

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Upper Arm | 51–63 | 13 | Largest single mass in the zone |
| 2 | Forearm | 64–70 | 7 | |
| 3 | Hand (parent of the five digit nodes below) | 71–75 | 5 | Small/awkward target — narrow |
| 4 | — Thumb | 71 | 1 | |
| 4 | — Index Finger | 72 | 1 | |
| 4 | — Middle Finger | 73 | 1 | |
| 4 | — Ring Finger | 74 | 1 | |
| 4 | — Little Finger | 75 | 1 | |

### 5.4 Head (76–100) — Tier-1 locked

| Tier | Node | Range | Width | Note |
|---|---|---:|---:|---|
| 2 | Skull | 76–88 | 13 | Largest single mass; brain-case treated as the vital target at this node (no deeper organ split — see §7 Question 2) |
| 2 | Face (parent) | 89–100 | 12 | |
| 3 | — Eyes | 89–90 | 2 | Paired; narrow/vital, per GURPS Eye precedent |
| 3 | — Ears | 91–92 | 2 | Paired; narrow |
| 3 | — Nose | 93–95 | 3 | |
| 3 | — Jaw / Teeth | 96–100 | 5 | Larger structure; wider than the other Face sub-nodes |

### 5.5 Laterality (cross-cutting; not part of the tree above)

Per DEC-041(3)/L-008, laterality is read from the **parity of the original Zero-Step
index**, independent of which node it resolves to: **odd = Left, even = Right.** It is
applied only to nodes with a genuine left/right counterpart (limbs, digits, eyes, ears,
kidneys, lungs). Midline structures (Heart, Spine, Nose, Jaw/Teeth, Pelvis/Groin, generic
Skull, Ribs/Chest-wall, Abdominal wall, Neck) **discard** the parity flag — it is computed
but has no anatomical referent, mirroring how GURPS's Vitals/Neck/Groin have no left/right
variant despite being reachable by any roll.

*Worked example:* Zero-Step index **47** → `Torso.Abdomen.Kidney`; 47 is odd → **Left
Kidney**. Index **72** → `Arm.Hand.Index Finger`; 72 is even → **Right Index Finger**.
Index **50** → `Torso.Spine`; parity (even) is computed but discarded (midline).

---

## 6. Worked Examples (mechanics unchanged, only location resolution shown)

### 6.1 Tier-1 resolution (Skill-Tier 2, e.g. Trip per DEC-113)

Attacker's Trip skill is Skill-Tier 2 → per DEC-113 R2, Trip resolves at **Tier 1 coarse**
regardless of what a deeper Skill-Tier could reach. Zero-Step index 9 → Legs quartile only;
no further descent is consumed even though this template supports it. Address: `Leg` (no
sub-node recorded).

### 6.2 Deeper Wound resolution (Skill-Tier 4 causing skill)

A Skill-Tier-4 Attack skill wins an S-1 contest and the winner selects **Impose Condition:
Wounded**. Per DEC-107, Wound Tier defaults to the causing skill's Skill-Tier (4). Per
DEC-112 L-005/L-006, Location Tier tracks that same depth. Zero-Step index 38 →
`Torso.Chest.Heart`. The Wound record (DEC-035.A / L-013) reads:

```
Location 38 (Torso.Chest.Heart) Tier-4 Wound -4 (bpe)
```

### 6.3 Parent-fallback armor coverage (L-007 / L-014)

Defender's Body armor is registered with `defense:armor` bound at the **Torso** node
(Tier 1) — not at any specific organ. Incoming Effect resolves to `Torso.Abdomen.Liver`
(Tier 3). Per L-007, the Torso-level armor registration **covers every descendant**,
including Liver, without needing a separate armor entry per organ. If the armor had
instead been registered narrowly at `Torso.Chest` only, a hit resolving to
`Torso.Abdomen.Liver` would **not** be covered by it (different branch, not an ancestor) —
this is a genuine gap, not a fallback case; DEC-112 L-014's parent-fallback applies to a
node whose *own* entry is missing, falling back to its nearest defined ancestor, not to
unrelated siblings.

### 6.4 Terminal-leaf saturation (recommended — see §7 Question 1)

A hypothetical Skill-Tier 6 skill would, under L-005's literal "no cap" wording, seek a
Tier-6 address. Since no Tier-5+ numeric layer exists in this template (§3), the address
resolution **saturates at the deepest existing node** for that branch — e.g., a Tier-6
skill striking index 72 still resolves to `Arm.Hand.Index Finger` (this template's deepest
node on that branch), with no mechanical difference from a Tier-4 skill hitting the same
index. Any further "precision" a GM wants to narrate (e.g., a specific knuckle) is flavor
text only, carrying no separate address, Tier, or numeric weight.

---

## 7. Open Questions for Tiwa's Ruling

*(Per standing governance rules, none of these are decided in this document. Recorded so
Tiwa can rule, edit, or reject each independently — no DEC is inferred from silence.)*

1. **Resolution ceiling above the digit/organ layer.** §3 identifies a genuine tension
   between DEC-112 L-005's uncapped Skill-Tier→Tier mapping and the finite 100-state
   address space. Three options:
   - **(A) Terminal-Leaf Saturation (used in §5–§6 above; recommended).** The address tree
     stops at the digit/organ layer (old ladder's "Tier 4"); higher Skill-Tiers resolve to
     the same deepest node with no new address. Simple, deterministic, preserves
     anatomically-weighted ranges undiluted.
   - **(B) Full phalanx/joint numeric partition.** Extend the tree one more layer (the old
     ladder's "Tier 5") using genuine 1-in-100 leaves per phalanx/joint. Honors L-005's
     letter more literally, but forces every leaf in already-cramped zones (Foot, Hand) to
     near-zero width, eliminating anatomically-weighted realism at exactly the point it
     matters most (small/awkward targets should already be narrow, not forced narrower by
     construction).
   - **(C) Decouple "Tier" from "address depth" above Tier 4.** Tiers 5+ still exist
     mechanically (e.g., for GM Fiat or a future called-shot bonus) but consume no new
     numeric leaf — they act as *qualifiers* layered onto the same terminal address.
     Functionally similar to (A) but frames the excess Tier as meaningful rather than inert.
2. **Skull internal structure.** §5.4 leaves Skull as a single terminal node (no separate
   "Brain" sub-target), on the reasoning that Skull already functions as the head's vital
   zone in most crunch-forward precedent (§2.2, GURPS). An alternative is a Skull→Brain
   split mirroring Chest→Heart, for symmetry. Flagged, not decided.
3. **Neck placement.** §5.2 places Neck under Torso (Upper Torso branch) rather than under
   Head, since DEC-100 assigns no independent range to either treatment and both are
   defensible (AIS itself files Neck under "Head/Neck" for ISS purposes, but "Neck" is its
   own AIS chapter). Flagged, not decided.
4. **Spine as a Tier-2 sibling vs. a cross-cutting node.** §5.2 treats Spine as a single
   Tier-2 leaf under Torso rather than a structure spanning both Chest and Abdomen (as it
   does anatomically). Splitting Spine into Thoracic/Lumbar sub-nodes was considered and
   rejected for budget reasons (§3) but could be revisited if Question 1 is resolved as
   Option (B).
5. **Paired-organ/limb single-leaf convention.** §5 gives paired structures (kidneys,
   lungs, eyes, ears) **one** address leaf apiece, with side determined by parity (§5.5),
   rather than two separate leaves (Left Kidney / Right Kidney as distinct numeric ranges).
   This roughly halves the leaf budget consumed by paired structures. Flagged as a
   design-efficiency choice, not a forced consequence of any locked rule.

---

## 8. Generalization Note (non-binding)

Nothing above is specific to the numeric values chosen — the **method** (locked Tier-1
quartile → anatomically-weighted Tier-2/3/4 subdivision → terminal-leaf saturation →
parity-based laterality) is intended to generalize to future non-Human templates under
DEC-112 L-004, once each creature's own anatomy (digit count, organ set, presence/absence
of a given AIS-analogous region) is authored per DEC-077.A. This document does not attempt
that generalization; it closes Human only.

---

## Sources Consulted (paraphrased throughout; no verbatim rules text reproduced)

- Association for the Advancement of Automotive Medicine — Abbreviated Injury Scale (AIS)
  region structure and Injury Severity Score (ISS) body-region collapsing.
- Steve Jackson Games — GURPS 4th Edition hit-location table structure (roll range,
  sublocation penalties, "miss by 1 → Torso" fallback behavior) — described structurally,
  not quoted.
- Chaosium/The Design Mechanism — RuneQuest/BRP/Mythras d20 hit-location table and
  per-location hit-point convention — described structurally, not quoted.
- Iron Crown Enterprises — Rolemaster *Arms Law* critical/location-and-severity split —
  described structurally, not quoted.
- Community percentile hit-location table in the Dark Heresy/Rogue Trader (Warhammer
  40,000 percentile RPG) lineage — described structurally, not quoted.

---

**End of proposal.** No DEC assigned. No canonical or non-canonical ruling recorded by
this document. Awaiting Tiwa's direction on §7 before any handoff to OpenCode.
