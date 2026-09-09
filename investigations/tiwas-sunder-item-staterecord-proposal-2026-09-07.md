---
document:
  title: "Sunder Redesign — Item StateRecord with Tier-Gated Magnitude Damage (Proposal)"
  version: "v1.0"
  status: "Advisory proposal record — Non-Canonical. Not a ruling. Presents Tiwa's design for Tiwa/OpenCode ruling session."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "not established", version: "not established"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-07"
  last_modified_date: "2026-09-07"
session_role: "Claude is presenting Tiwa's own design (dictated verbatim in-session) in formal documentation form, with precedent cross-referencing and conflict-flagging per standing advisory duties. Claude did not originate this mechanic and is not recommending it over alternatives. All numbered items in §4 require Tiwa's ruling, to be worked out directly with OpenCode."
supersedes: "This proposal supersedes Options A/B/C from `tiwas-equipment-tier-sunder-advisory-handoff-2026-09-07.md` §3.3–3.5 as the live candidate for OI-EQ-06. It resolves the Option-A/Option-B contradiction OpenCode flagged when attempting to record OI-EQ-06/OI-EQ-02 by replacing both prior candidates with a single new mechanic (referred to here as Option D)."
---

# Sunder Redesign — Item StateRecord with Tier-Gated Magnitude Damage (Proposal)

## 0. Origin and Status

This document formalizes a design supplied directly by Tiwa in-session, in response to OpenCode's contradiction-stop on the prior Sunder options draft (Options A/B/C, see the superseded handoff referenced above). It is presented here as **Option D** — a new, single mechanic replacing the earlier three-option menu, not a fourth option alongside them.

Nothing in this document is Canonical or ruled. It is written for Tiwa and OpenCode to work through together; Claude's role here is transcription into formal documentation, precedent cross-referencing, and conflict-flagging only.

---

## 1. The Mechanic, As Specified

### 1.1 Item StateRecord

Every Item that can be Sundered carries its own persistent record, using the DEC-115 unified schema shape:

```
Type: Item
Location X: [item slot / held limb, per DEC-081]
Tier Y: [Item Tier — authoring/source TBD, see §4 OI-SU-01]
Magnitude Z: [Item HP — current durability value]
```

**Magnitude Z is explicitly "Item HP"** — a numeric value that starts at some maximum (authoring/source TBD, §4 OI-SU-02) and can be reduced by successful Sunder/Equipment Damage hits.

### 1.2 Sunder / Equipment Damage as the damaging Effect

When a Sunder or Equipment Damage Effect successfully applies to an item (i.e., after the existing DEC-028/DEC-114 Tag+Location gate has already been satisfied — see §3.1 for how this new mechanic relates to that existing gate):

- The Effect carries its own **Sunder Tier** and **Sunder Magnitude**.
- **Gate:** damage is applied to the item's Magnitude (Item HP) **only if Sunder Tier ≥ Item Tier.**
- **If the gate passes:** the item's Magnitude Z is reduced by an amount equal to the Sunder Effect's Magnitude.
- **If the gate fails** (Sunder Tier < Item Tier): the item's Magnitude is **not** reduced.

### 1.3 Persistence regardless of gate outcome

The Sunder Tag/Effect record **persists on the item regardless of whether the Tier gate passed.** A failed-gate hit still leaves a record on the item; it simply does not reduce Magnitude. (What exactly persists — a marker Tag, a logged prior-attempt record, or something else — is not fully specified; see §4 OI-SU-03.)

### 1.4 Unusable threshold

If the item's Magnitude Z is reduced to **0 or below**, the item becomes **Unusable.** Whether the item is narratively "destroyed" versus merely "broken/inert" is explicitly immaterial to this design — both collapse to the same mechanical state (Unusable), per Tiwa's original design goal.

---

## 2. Worked Example (Illustrative Only — Not Authored Content)

To make the mechanic concrete (numbers are illustrative placeholders, not ruled values):

| Step | Value |
|---|---|
| Item's own record | Tier 2, Magnitude (Item HP) 5 |
| Attacker lands Equipment Damage, Sunder Tier 1 | Gate check: 1 ≥ 2? **No.** Magnitude unchanged (still 5). Record persists on item per §1.3. |
| Attacker lands Equipment Damage again, Sunder Tier 3 | Gate check: 3 ≥ 2? **Yes.** Magnitude reduced by Sunder Magnitude (e.g., 3) → Item HP = 5 − 3 = 2. |
| Third hit, Sunder Tier 2, Sunder Magnitude 3 | Gate check: 2 ≥ 2? **Yes.** Item HP = 2 − 3 = −1 → **Unusable.** |

---

## 3. Relationship to Existing Rulings

### 3.1 Does this replace or sit alongside the DEC-028/DEC-114 Tag+Location gate?

The existing gate (DEC-028, narrowed by DEC-041; Tag-match table per DEC-114 R2) determines **whether an Equipment-tier Effect triggers at all** — it is evaluated once, post-win, and a failure falls back to Base Inflict Injury per DEC-030.

This new mechanic (§1.2) appears to operate **downstream** of that gate: once Equipment Damage/Sunder has already triggered (Tag+Location gate passed), the *new* Sunder-Tier-vs-Item-Tier check then determines whether that already-triggered hit actually reduces Magnitude. This document assumes that reading but does not rule it — see §4 OI-SU-04, since an alternative reading (the new Tier gate *replacing* the Tag+Location gate entirely) is also structurally possible and has very different consequences for DEC-030's fallback behavior.

### 3.2 Precedent: this is structurally close to DEC-103

DEC-103 (S-4/S-6 Active Defense Effect mitigation) already established a **Tier-comparison-then-Magnitude-reduction** pattern in the corpus, applied to Effects landing on characters:

> "Step 1 Skill-Tier comparison shred... Step 2 margin de-escalation: Mag −= Defender's Margin... Tier floor 0 → Effect negated."

Tiwa's Item design is structurally the same shape — a Tier comparison gates whether a Magnitude reduction applies — applied to Items instead of character-side Effects. This is a useful precedent to cite when reconciling the new mechanic with the rest of the corpus: it is not a wholly novel pattern, just the first time it is applied to Item durability rather than Effect negation.

### 3.3 Direct conflict: DEC-058

DEC-058 (S5-A, Armor architecture) rules **"No numeric durability/soak pool"** for Armor, and describes Armor as "structurally identical in kind to item Tags **generally**" — a phrasing that extends the no-numeric-pool reasoning to equipment as a category, not only Armor.

**This proposal is, unambiguously, a numeric durability pool on items** (Item HP, explicitly named as such in Tiwa's own description). It does not attempt to disguise this as a Tag-only mechanic the way the earlier Option A did. This is the same conflict flagged as **OI-EQ-05** in the prior handoff document and is **not resolved by this document.** Adopting this mechanic as written requires Tiwa to either:

- amend DEC-058 to permit numeric Item Magnitude generally, or
- rule that DEC-058's "generally" language was scoped to Armor's combat-relevant DR specifically and does not bind general Item durability.

This is the single highest-priority open item below (§4 OI-SU-05, superseding the prior OI-EQ-05 in light of this new design).

### 3.4 Interaction with DEC-079 C8 / DEC-116 R1 (existing Sundered vocabulary)

DEC-079 C8 already describes Sundered as "Cumulative at same Tier / Permanent until repaired," and DEC-116 R1 cites `state:sundered` as the register's example of a graded-Tag precedent. This proposal is broadly consistent with that existing lean toward a graded Sundered — more so than the earlier flat-flag Option A was — though it replaces "grade the Tag itself" with "grade the Item's own separate record," which is a different implementation of the same graded intent. Whether the `state:sundered` Tag still exists as a marker under this design (e.g., applied once Magnitude reaches 0, to flag Unusable state for other systems like DEC-062 Armor coverage checks) or is retired entirely in favor of the Item StateRecord is unresolved — see §4 OI-SU-06.

---

## 4. Open Questions Register

None of the following are ruled. These are to be worked through by Tiwa and OpenCode directly; Claude has not proposed answers.

| ID | Question |
|---|---|
| OI-SU-01 | Where does an Item's own Tier (Y) come from? Authored per-item at creation (DEC-077.A/DEC-085 content-authoring precedent), derived from some existing value (e.g., item cost/rarity), or GM-assigned per instance? |
| OI-SU-02 | Where does an Item's starting/maximum Magnitude (Item HP) come from? Flat per-Tier formula, per-item authored value, or something else? |
| OI-SU-03 | What exactly "persists on the item" per §1.3 when the Tier gate fails? A record of the failed attempt, a cosmetic marker Tag, or nothing beyond the fact that Magnitude is unchanged? |
| OI-SU-04 | Does the new Sunder-Tier-vs-Item-Tier gate operate *downstream* of the existing DEC-028/DEC-114 Tag+Location gate (§3.1's assumed reading), or does it *replace* that gate for the Equipment-tier Effects? This changes what DEC-030's fail-and-fall-back applies to. |
| OI-SU-05 (supersedes prior OI-EQ-05) | Does adopting Item Magnitude/Item HP require amending DEC-058, or ruling that DEC-058's "generally" language was always Armor-scoped and does not bind general Item durability? |
| OI-SU-06 | Does the `state:sundered` Tag (DEC-060/DEC-079 C8) still exist as a marker once an item's Magnitude hits 0 (e.g., for other subsystems like DEC-062 Armor coverage checks to key off of), or is it fully retired in favor of "Item Magnitude ≤ 0" as the sole Unusable signal? |
| OI-SU-07 | Where does the attacking Effect's own **Sunder Tier** come from? Precedent (DEC-107) sets Effect Tier = the attacking Skill's Skill-Tier — does that apply unmodified here, or does Sunder Tier need its own rule? |
| OI-SU-08 (carried) | Repair procedure (EQ-2): does repairing an item restore Magnitude directly (by how much, via what skill/cost), and can repair only occur once an item is already Unusable, or at any Magnitude value? |
| OI-SU-09 (carried) | Item-selection when multiple items occupy one struck coarse zone (prior OI-EQ-03) — unaffected by this redesign; still needs its own ruling. |
| OI-SU-10 (carried) | The DEC-059-Bypass vs. DEC-028/114-"Armor Bypass" naming collision (prior OI-EQ-04) — unaffected by this redesign; still needs its own ruling. |

---

## 5. Handoff Instructions for OpenCode

1. Do not record any DEC number from this document. This is a proposal write-up of Tiwa's own design, submitted for a live ruling session between Tiwa and OpenCode.
2. This document **supersedes** Options A/B/C in the prior handoff (`tiwas-equipment-tier-sunder-advisory-handoff-2026-09-07.md` §3.3–3.5) as the candidate answer to OI-EQ-06. Treat those three options as withdrawn from consideration, not as remaining alternatives.
3. OI-SU-05 (§3.3) is the load-bearing question: most of the other open items (OI-SU-01, OI-SU-02, OI-SU-06) are only worth finalizing in detail once it's settled whether this mechanic is adoptable under DEC-058 at all, or whether DEC-058 needs amendment first.
4. OI-SU-09 and OI-SU-10 are carried forward unchanged from the prior handoff document and are independent of this redesign — they do not need to wait on OI-SU-05.
5. The prior handoff's OI-EQ-01 (Break/Sunder Item vs. Equipment Damage naming) and OI-EQ-07 (content-authoring status of stage meanings) should be revisited once OI-SU-01/02/06 are answered, since this redesign changes what "the effectiveness of a hit" actually consists of.

