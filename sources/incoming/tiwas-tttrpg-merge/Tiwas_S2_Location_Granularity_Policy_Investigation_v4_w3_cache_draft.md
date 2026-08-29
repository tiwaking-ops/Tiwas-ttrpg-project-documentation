# Tiwas S-2 Design Investigation v4 — W3 Cache Draft (W2-Derived)

**Status: Design investigation output — NON-CANONICAL. Recommendation-class material only.**
**Purpose:** Execute option (1) from v3 §8 — build a first-pass W3 category list by systematically applying the W2 outcome-differentiation test, rather than by intuition (which is what produced v1's premature and S-3-contaminated list).
**Not settled by this document:** which of W2, W3, or the W2/W3 synthesis becomes the actual policy. This is preparatory material for whichever way that designer decision goes — a usable cache exists either way (as the core mechanism under pure W3, or as the fallback-reducing cache under the synthesis).

---

## 1. Scope Note

**[Architectural constraint, carried from Canonical Rules §14.1]** Zero-Step derives a Location Index from "the attacker's natural d100 roll" — the mechanism presumes a Core Test that represents an attack or impact against a target (a person, creature, or object). This cache is therefore scoped to **offensive/impact resolutions**, not to skill tests generally. A Mind-domain research test or a social Skill test has no "impact roll" for Zero-Step to act on and falls outside this cache by construction, not by a judgment call each time.

---

## 2. Construction Method

Each entry below is built by asking the W2 question directly: *for this category of resolution, does the permissible outcome set genuinely differ depending on which location the roll indicates?* Entries are written to describe **the nature of the declared objective**, not the name or number of any specific S-3/S-4 rule — per §6 of v3, referencing an unlocked rule by name would reintroduce C1's flaw. Where the honest answer depends on how an unlocked future subsystem eventually gets written, that is flagged explicitly as a **Medium** or **Low** confidence entry rather than asserted as settled.

**[Recommendation]** Each entry carries:
- **Category** — the reusable rule-text description.
- **W2 reasoning** — why the outcome branches (or doesn't).
- **Confidence** — High / Medium / Low, per §2 above.
- **Revisit trigger** — what future event should cause this entry to be re-checked.

---

## 3. Categories That Pass W2 (Candidate Cache Entries)

| Category | W2 reasoning | Confidence | Revisit trigger |
|---|---|---|---|
| **Declared disarm** — attacker states an objective requiring a specific item-bearing location be struck to force an item loose | Outcome set strictly branches: item-bearing-location hit → drop possible; elsewhere → not | **High** | S-3 locks the actual Disarm/Break Hold Effect — confirm the location condition matches this entry's assumption |
| **Equipment/gear targeting** — attacker targets a specific worn or carried item (strap, buckle, container, weapon itself) rather than the bearer | Outcome (item disabled/destroyed vs. not) is strictly location-bound to the item's position on the target | **High** | S-3 locks Equipment Damage Effect; S-5 locks Armor interaction — confirm alignment |
| **Called shot to impair a specific function** — attacker states an objective tied to a named bodily function (e.g., disabling a limb's use, impairing sight, impairing speech/verbal casting) | Outcome (function impaired vs. ordinary damage) depends on whether the indicated location maps to that function | **Medium** — depends on how Conditions (Proposals §10) and any Magic-component interaction (Proposals §15) eventually get written | S-4/S-10 lock Condition application rules; S-15 locks Magic component rules |
| **Attack intended to incapacitate/kill via a vital strike** | Outcome plausibly branches (vital-location hit vs. not) once any Wound/incapacitation severity rule exists, but no such rule is locked yet | **Low** — this is the incapacitation edge case flagged in v3 §5; included provisionally because it is a near-certain future consumer, not because current rules confirm it | S-4 locks Wound severity; S-7 locks incapacitation/death — this entry should convert to High or be rewritten once either locks |
| **Attack against a structure/object with location-dependent mechanical weak points** (e.g., a door's hinge vs. lock vs. panel, each producing a different breach outcome) | Outcome set differs by which named weak point was struck; ordinary "break down the door" does not need this | **High** | None specific — stable structural logic, unlikely to change with future subsystems |
| **Environmental hazard with location-differentiated consequence** (e.g., a fall where which limb strikes first plausibly changes injury type/severity) | Outcome branches if the hazard's resolution logic distinguishes by struck location; many hazards will not | **Medium** — depends on how the specific hazard is written; this entry describes a *pattern*, not a blanket rule for "all hazards" | S-4 locks Wound rules that hazards would feed into |
| **Formal duel with a location-dependent win condition** (e.g., "disable the weapon arm to win," not "first solid hit") | Outcome branches because the duel's own declared victory condition is location-specific; this is conditioned on the *win condition*, not on "duel" status generically | **High** — but only when paired with a genuinely location-specific win condition; see explicit rejection of bare "formal duel" as a category in §4 | None specific |

---

## 4. Categories That Fail W2 (Explicit Rejections)

Included deliberately, to keep the cache from drifting into "everything combat-adjacent," which was the failure mode both prior reviews warned against.

| Category | W2 reasoning | Confidence |
|---|---|---|
| **Ordinary attack, no stated objective beyond damage** | No outcome differs by location under any currently reasoned rule; this is the baseline null case | **High** |
| **Called shot with no stated mechanical objective** ("I aim for the arm" with nothing further) | Narration alone doesn't create branching; this is the case that separates W1 from W2 (v2 §3) and must stay excluded to avoid quietly reintroducing W1 through the cache | **High** |
| **"Formal duel" as a bare category**, independent of its win condition | Reintroduces Candidate-A scene-level logic through the back door (v3 §3, duel trap); only the specific win-condition subtype in §3 qualifies | **High** |
| **Cinematic or mass-combat framing, as a category** | This is a *context that suppresses* warrant (per v3 §3), not a trigger that creates it; including it as a "category" would invert its actual function | **High** |
| **Coup de grâce / strike against an already-helpless, already-determined-fate target** | The outcome (target's fate) is already fixed by the helplessness ruling itself; location adds no branching to what happens mechanically, only narrative color | **Medium** — could change if a future rule ties manner-of-death or a Condition specifically to location even for helpless targets, which is plausible but unconfirmed |
| **Environmental hazard with a uniform, non-location-dependent consequence** (e.g., flat poison-gas exposure, generic fire damage with no differentiated severity) | Outcome is identical regardless of location by the hazard's own design | **High** |
| **Sneak attack / surprise attack, as a category by itself** | "Surprise" changes the Core Test's circumstances (e.g., difficulty, per future S-8), not whether location differentiates the outcome; a sneak attack with no further stated objective is still the null case from row 1 | **High** |
| **Ranged vs. melee delivery method, as a category** | Weapon/delivery type does not itself create outcome branching; any warrant present comes from the stated objective (disarm, equipment-targeting, etc.), which is already covered by its own entry regardless of delivery method | **High** |

---

## 5. Maintenance Protocol

**[Recommendation]** If this cache is adopted (either as the core W3 mechanism or as the fallback-reducing layer under the W2/W3 synthesis from v3 §7), it should be maintained under these rules:

1. Every entry's **Confidence** and **Revisit trigger** fields are load-bearing, not decorative — when a listed trigger event occurs (a specific subsystem locking), the entry must be re-evaluated against the newly locked rule text before being treated as confirmed.
2. An entry may move from Medium/Low to High only by explicit re-check against locked rule text — never by default or by time elapsed.
3. New entries may be added at any time by applying the W2 test to a novel situation encountered in play; per v3 §7, this is exactly the fallback path the synthesis model describes, and each successful fallback application is a candidate for promotion into the cache.
4. Rejected categories (§4) should remain listed and visible, not silently dropped — their presence is what keeps future contributors from re-adding W1-style "any called shot" logic by accident.

---

## 6. Remaining Designer Decisions

**[Unresolved designer decision]** Whether this cache is adopted as-is, edited, or rejected in favor of relying on GM-applied W2 without a pre-built list.

**[Unresolved designer decision]** The Low-confidence incapacitation entry (§3, row 4) is the cache's weakest link and mirrors the exact edge case flagged in v3 — the designer should decide whether to include it provisionally (as drafted here), omit it until S-4/S-7 lock, or replace it with a narrower, more defensible interim wording.

**[Unresolved designer decision]** Whether the §7-of-v3 synthesis (W2 as principle, this cache as maintained shorthand) is the adopted architecture at all — this document assumes it might be, in order to produce a usable artifact, but does not itself rule on that fork.

---

## 7. Status Relative to the Open Fork (v3 §8)

This document completes option (1) from v3 §8. Option (2) — a table-practice stress test on GM-burden for the W2 fallback — has not been run and would require actual play data rather than further first-principles analysis. It remains the recommended companion validation step before this cache is treated as more than a well-reasoned draft.
