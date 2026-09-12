---
document:
  title: "Tiwas — Human Location Address Template + 100-State Allocation (DEC-112 L-009 / L-010): Adopted Content"
  version: "1.0"
  status: "Designer-ruled content — accepted in-session by Tiwa on 2026-09-13. Content-authoring under DEC-077 / DEC-112 L-009–L-010. Not Canonical; recording does not confer canonical status — any future Canonical entry still requires the 8-step Promotion Rule (REQ-021 / governance/status-model.md)."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-13"
  last_modified_date: "2026-09-13"
---

# Tiwas — Human Location Address Template + 100-State Allocation

**Status: adopted designer content (Human v1).** This document records the merged
Human Location Address Template (**DEC-112 L-009**) and the Human 100-state numerical
allocation (**DEC-112 L-010**), accepted in full by **Tiwa** on **2026-09-13**. It is
content-authoring output, not a rules change. Register effect (recorded separately in
`_consolidation/decision-register.md`): new **DEC-137** plus in-cell amendment
annotations on **DEC-112** (L-009/L-010) and **DEC-136** (R1), preserving original cell
text.

---

## 0. Governance Notice

Per the standing role separation — **Tiwa rules; OpenCode records**. Tiwa selected a
**Merge of the two advisory candidates** and ruled each structural fork listed in §3.
The merged draft was produced by OpenCode (big-pickle) and **accepted by Tiwa as-is**.
Advisory source candidates (no DEC inferred by either):

- `investigations/tiwas-human-location-template-l009-l010-proposal-2026-09-12.md`
  (Claude Sonnet 5)
- `investigations/tiwas-location-100-state-allocation-information-capacity-investigation-2026-09-12.md`
  (opencode / big-pickle)
- Architecture proposal: `investigations/Tiwas TTRPG — Proposed Hierarchical Location
  Architecture Report.md` (GPT-5.6 Luna, 2026-09-08)

---

## 1. Binding constraints honored (unchanged)

| Constraint | Source | Effect |
|---|---|---|
| Four Tier-1 quartiles frozen | DEC-100 | Legs 1–25, Torso 26–50, Arms 51–75, Head 76–100 — 25 states each, not re-negotiated |
| Zero-Step sole index provider | DEC-014, Invariant 6 | All addresses derive from the existing tens/units exchange output |
| Single-source deterministic; no secondary roll | DEC-112 L-003/L-011, DEC-136 R1 | Full address path recoverable from one d100 value alone |
| Skill-Tier maps to Location Tier, no cap | DEC-112 L-005, DEC-136 R2 | Deeper Skill-Tier resolves deeper; effective depth also bounded by authored template |
| Location Tier = precision depth | DEC-112 L-006 | Each added Tier subdivides its parent |
| Parent covers all children | DEC-112 L-007 | Armor/Wounds bound at a coarse node cover every descendant |
| Laterality via Zero-Step parity only | DEC-041(3), DEC-112 L-008 | No explicit Left/Right numeric branches |
| Mismatch → parent fallback | DEC-112 L-014 | Missing fine node falls back to nearest defined ancestor (DEC-030 remains for Effect Tag/location mismatch) |
| Skill-Tier ≥ 2 gate | DEC-041(1) | Only promoted rolls from Skill-Tier ≥ 2 skills resolve locations in play |
| Leaf budget ≤ 100 | §9 proposal / LOC-I16 | Only the terminal-leaf count binds; depth is free |

---

## 2. Structural forks ruled (2026-09-13)

| # | Fork | Ruling |
|---|---|---|
| 1 | Resolution above the deepest leaf | **Decouple Tier from address depth.** Tiers 5+ exist mechanically (qualifiers, e.g. GM-Fiat precision / called-shot) but consume **no numeric leaf**; the address saturates at the deepest authored node. |
| 2 | Skull internal structure | **Single Skull node** (no Skull→Brain leaf). |
| 3 | Neck placement | **Neck is a Tier-2 sub-zone under Torso.** |
| 4 | Spine treatment | **Spine is a single Tier-2 leaf under Torso.** |
| 5 | Paired organs/limbs | **Single address leaf + parity**; side from the parity digit. |
| 6 | Parity digit | **Units digit** of the Zero-Step output (odd = Left, even = Right). |
| 7 | Per-zone reserves | **None.** All 100 states are assigned to named structures. |

---

## 3. Adopted allocation (Human v1)

### 3.1 Legs — states 1–25

| Tier | Node | Range | Width |
|---|---:|---:|---:|
| 2 | Thigh | 1–5 | 5 |
| 2 | Knee | 6–7 | 2 |
| 2 | Lower Leg | 8–12 | 5 |
| 2 | Ankle | 13 | 1 |
| 2 | Foot | 14–22 | 9 |
| 3 | — Hallux (big toe) | 14–15 | 2 |
| 3 | — 2nd Toe | 16 | 1 |
| 3 | — 3rd Toe | 17 | 1 |
| 3 | — 4th Toe | 18 | 1 |
| 3 | — 5th Toe | 19 | 1 |
| 3 | — Midfoot/Heel | 20–22 | 3 |
| 2 | Femoral/internal | 23–25 | 3 |

### 3.2 Torso — states 26–50

| Tier | Node | Range | Width |
|---|---:|---:|---:|
| 2 | Chest | 26–35 | 10 |
| 3 | — Chest wall / Sternum / Ribs | 26–29 | 4 |
| 3 | — Heart | 30–31 | 2 |
| 3 | — Lungs (paired) | 32–35 | 4 |
| 2 | Neck | 36–37 | 2 |
| 2 | Abdomen | 38–47 | 10 |
| 3 | — Abdominal wall / Guts | 38–40 | 3 |
| 3 | — Stomach | 41 | 1 |
| 3 | — Liver | 42–43 | 2 |
| 3 | — Intestines | 44–45 | 2 |
| 3 | — Kidneys (paired) | 46–47 | 2 |
| 2 | Pelvis | 48 | 1 |
| 2 | Groin | 49 | 1 |
| 2 | Spine | 50 | 1 |

### 3.3 Arms — states 51–75

| Tier | Node | Range | Width |
|---|---:|---:|---:|
| 2 | Shoulder | 51–52 | 2 |
| 2 | Upper Arm | 53–58 | 6 |
| 2 | Elbow | 59–60 | 2 |
| 2 | Forearm | 61–65 | 5 |
| 2 | Wrist | 66–67 | 2 |
| 2 | Hand | 68–75 | 8 |
| 3 | — Thumb | 68–69 | 2 |
| 3 | — Index Finger | 70 | 1 |
| 3 | — Middle Finger | 71 | 1 |
| 3 | — Ring Finger | 72 | 1 |
| 3 | — Little Finger | 73 | 1 |
| 3 | — Palm/Back | 74–75 | 2 |

### 3.4 Head — states 76–100

| Tier | Node | Range | Width |
|---|---:|---:|---:|
| 2 | Skull | 76–91 | 16 |
| 2 | Face | 92–100 | 9 |
| 3 | — Eyes (paired) | 92–93 | 2 |
| 3 | — Ears (paired) | 94–95 | 2 |
| 3 | — Nose | 96–97 | 2 |
| 3 | — Jaw/Teeth | 98–100 | 3 |

### 3.5 Whole-figure check

- 25 + 25 + 25 + 25 = **100 states** = `|Ω|` ✓
- All four Tier-1 quartiles contiguous and frozen by DEC-100 ✓
- Max numeric Tier = **4** (digit/organ layer); Tiers 5+ are qualifiers, not leaves (§2 #1) ✓

---

## 4. Content conventions

1. **Parity laterality (units digit of the Zero-Step output):** odd = Left, even =
   Right. Applied only to nodes with a genuine lateral counterpart.
2. **Midline discard:** parity is computed but discarded for Heart, Spine, Skull,
   Sternum/chest wall, Neck, Stomach, Liver, Intestines, Nose, Jaw/Teeth, Pelvis, Groin,
   Midfoot/Heel, Abdominal wall.
3. **Even-count paired leaves give both sides:** e.g. Lungs 32–35 → odd 33/35 Left,
   even 32/34 Right; Kidneys 46–47 → 46 Right, 47 Left; Shoulder/Elbow/Wrist/Thumb/
   Hallux/Eyes/Ears/Palm similar.
4. **Single-state paired leaves fix the side by that state's parity:** Ankle 13 →
   always Left Ankle; 2nd Toe 16 → Right; 3rd Toe 17 → Left; 4th Toe 18 → Right; 5th
   Toe 19 → Left; Index 70 → Right; Middle 71 → Left; Ring 72 → Right; Little 73 →
   Left. The sibling side is **not randomly reachable**; it is reachable only through
   the Tier-5+ qualifier layer (Fork #1) or GM Fiat.
5. **Address record:** keep the raw Zero-Step index alongside the named address in a
   Wound record, e.g. `Location Index 42 → Torso.Liver` (DEC-035.A `Location X`; DEC-112
   L-013). Example: `Location 38 (Torso.Chest.Heart) Tier-4 Wound -4 (bpe)`.

---

## 5. Effect interaction (unchanged mechanics; only resolution location)

- **Tier-1 Effects** (Wound / Inflict Injury, Trip, Disarm/Break Hold, Equipment
  Damage — DEC-113 R2): resolve at **Tier 1 coarse** via the DEC-100 quartile, no
  sub-zone descent regardless of Skill-Tier.
- **Armor Bypass (Tier-2, DEC-113 R2)**: with this template + allocation adopted,
  it now resolves for a **Human** target via the deterministic Location Index →
  Location Template → address path (DEC-112 L-003/L-011; DEC-136 R1 dependency
  satisfied). No secondary roll.
- Armor coverage and Wound matching follow DEC-112 L-007 (parent covers children) /
  L-012 / L-013; mismatch fallback per L-014.

---

## 6. Non-decisions (not altered by this record)

- DEC-100 quartiles are **not** reopened — within-zone weighting only.
- No Canonical text created; the hierarchical architecture remains a non-canonical
  designer ruling pending any future 8-step promotion.
- Other creature templates (Ice Troll, Blood Man, Goblin, Dragon, future content)
  remain content-authoring — the method in this document generalises but is not applied
  elsewhere here.
- Zone-level weighting, DEC-014, DEC-062, DEC-030, DEC-107, and Invariants 17/18 are
  untouched.

**End of record.** Content accepted by Tiwa 2026-09-13; recorded by OpenCode (big-pickle).