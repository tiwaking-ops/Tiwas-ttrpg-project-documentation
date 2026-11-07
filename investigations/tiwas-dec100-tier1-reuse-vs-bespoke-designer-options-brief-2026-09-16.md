---
document:
  title: "DEC-100 Tier-1 Reuse vs Bespoke Tier-1 — Designer Options Brief (DEC-112 L-004, evidence: Blood Man / Dragon / Giant Spider)"
  version: "1.1"
  status: "Advisory options brief — Non-canonical. Not a ruling. No DEC inferred. Pending Tiwa's in-session ruling; if ruled, the ruling is recorded against the live register by the designer/OpenCode workflow before any register text changes."
provenance:
  author_llm: {name: "buffy/codebuff", version: "not established"}
  assessor_llm: []
  last_modified_by_llm: {name: "buffy/codebuff", version: "not established"}
  created_date: "2026-09-16"
  last_modified_date: "2026-09-16"
---

# DEC-100 Tier-1 Reuse vs Bespoke Tier-1 — Designer Options Brief

## 0. Governance Notice

This is an **advisory options brief**. It:

- formalizes one open question already carried by three stored proposals (Blood Man
  §6 Q1, Ice Troll §6 Q1, Giant Spider §2/§6) and implicitly by every L-004 template
  that reused DEC-100;
- presents an A/B/C option set with register consequences and a **recommended
  default** (LLM advice only — it confers no authority);
- does **not** rule, assign a DEC, amend the decision register, or change any
  Canonical text. **Tiwa** holds sole human ruling authority.

Source material (all advisory/non-canonical unless noted):
`investigations/tiwas-blood-man-location-template-proposal-2026-09-13.md`,
`investigations/tiwas-dragon-location-template-proposal-2026-09-13.md`,
`investigations/tiwas-giant-spider-location-template-proposal-2026-09-13.md`,
`investigations/tiwas-ice-troll-location-template-proposal-2026-09-13.md`;
`_consolidation/decision-register.md` (DEC-014, 041, 100, 112, 136, 137, 139);
companion brief `investigations/tiwas-l004-four-creature-template-open-questions-designer-options-brief-2026-09-16.md`.

## 1. The Question, Formalized

**Under DEC-112 L-004 (per-creature-type Location Templates), what is the rule for a
creature's Tier-1 coarse-zone allocation?** Specifically: do DEC-100's quartile
ranges (1–25 Legs / 26–50 Torso / 51–75 Arms / 76–100 Head) apply to non-Human
creatures by default, or does DEC-041(5)'s "individual templates per creature type
(not a shared scheme)" require Tier 1 itself to be authored per creature?

Three stored proposals pose or carry this exact fork:

- **Ice Troll §6 Q1 (2026-09-13):** "Does DEC-100's Tier-1 quartile split apply to
  every bipedal humanoid creature, or does DEC-041(5)'s 'not a shared scheme'
  require even Tier 1 to be bespoke per creature?" — the proposal assumes the
  former for humanoids and flags the point as open.
- **Blood Man §6 Q1 (2026-09-13):** is a bespoke Tier-1 split actually warranted,
  or should DEC-100 apply with the amorphousness expressed only in weaker Tier-2+
  content? §2 argues for bespoke because Arms/Legs quartiles would "silently assert
  an anatomical permanence the creature doesn't have."
- **Giant Spider §2/§6 (2026-09-13):** third bespoke case; proposes the boundary is
  limb persistence/structure, not size or "monstrousness."

No register entry currently settles it. The DEC-112 storage annotations record the
fork as open ("no ruling in this register settles it either way... consistent with
the Ice Troll proposal's Q1").

## 2. Evidence Base

### 2.1 Ruled text (unchanged under every option's *interpretation*; see §4 per-option consequences)

- **DEC-100 (C-08, 2026-09-04):** "Location-Tier-1 coarse zones use the quartile
  ranges: 1–25 Legs; 26–50 Torso; 51–75 Arms; 76–100 Head. Supplies the numeric
  ranges DEC-041 left directional/not locked." Preserves DEC-041. The ruling does
  not state its creature scope — the fork exists in that silence.
- **DEC-041(2) (2026-08-31):** Tier-1 → coarse zones "(Head/Torso/Arms/Legs) via
  anatomically-weighted numeric ranges" — a vertebrate-humanoid quartet, named
  before any non-human creature template existed.
- **DEC-041(5):** "Creature coverage: individual templates per creature type (not
  a shared scheme); content dependency on S-12 (open)."
- **DEC-112 L-004/L-006 (2026-09-08):** per-creature-type authored templates;
  "Tier 1 = coarse zones (Head/Torso/Arms/Legs)" as the precision-depth baseline.
- **DEC-137 (2026-09-13):** the adopted Human v1 allocation preserves the four
  quartile ranges for Human — DEC-100 is not in dispute *for Humans*.

### 2.2 Template exhibits (ten L-004 instances to date)

| Instance | Tier-1 source | Body plan | Deciding anatomy |
|---|---|---|---|
| Human (DEC-137) | DEC-100 (authoritative) | Biped | The ruling's home case |
| Ice Troll | Reused (by assumption) | Biped, large | Persistent 2+2 limbs |
| Goblin / Orc | Reused | Biped | Persistent 2+2 limbs |
| Kobold | Reused + Tail sub-node | Biped | Persistent 2+2 limbs; minor feature fit inside a branch |
| Hobgoblin | Reused (interpolated) | Biped | Persistent 2+2 limbs |
| Troll | Reused (derived from Ice Troll) | Biped, large | Persistent 2+2 limbs |
| **Blood Man** | **Bespoke** (3 zones: 60/30/10) | Amorphous | **No persistent limb identity** — pseudopods reform between exchanges |
| **Dragon** | **Bespoke** | Quadruped + wings + tail | **Wrong limb count/kind** for the quartet; introduced "structural branch × parity" (2 branches × 2 sides) |
| **Giant Spider** | **Bespoke** (3 zones: 45/20/35) | Arachnid | **One limb type, wrong multiplicity** (8 legs = 4 structural branches × parity); proves the branch×parity mechanism scales to any even limb count |

### 2.3 What the three bespoke cases jointly establish

1. **The stable-limbed-biped rule.** First argued in Blood Man's Appendix B
   conclusion (the universal part is the *mechanism*; the Human-specific quartile
   template "must be re-examined per creature rather than assumed"), and given its
   crispest wording in Giant Spider's own close — which credits Blood Man's rule
   ("limb persistence, not size or 'monstrousness,' decides reuse") and then states:
   the reuse/bespoke boundary "has never once been about size, danger, or
   'monster-ness' — only about whether the creature is a stable-limbed **biped**"
   (Giant Spider, 2026-09-13; the quoted sentence is Giant Spider's formulation,
   not Blood Man's own).
2. **Giant Spider's confirmation** (2026-09-13): the rule generalizes to a third
   failure mode — "not two limb types in the wrong arrangement, but one limb type
   with the wrong multiplicity." The reuse/bespoke boundary tracks **limb
   persistence and structure**, and the Dragon mechanism (structural branch ×
   parity) handles any even limb count without modification.
3. **Zero contradictions:** across ten instances, no creature's bespoke split has
   been shown unnecessary, and no reusing creature has been shown to need one.
   The corpus already behaves as if a stable rule exists; it is simply unrecorded.
4. **Blood Man §6 Q1's honest counterweight:** even for the clearest bespoke case,
   keeping DEC-100 and weakening only Tier-2+ content is a *real* alternative,
   trading "architectural honesty" for cross-creature table consistency (every
   creature's Zero-Step index would land in one of the same four named quartiles —
   possibly a GM-facing UX benefit even where it is anatomically a fiction).

## 3. Decision Summary Table

| ID | Question | Options | Recommended default | Stakes |
|---|---|---|---|---|
| T1 | Tier-1 allocation rule for non-Human creatures under L-004 | **A** DEC-100 universal default for stable bipeds; **B** bespoke-always (DEC-100 Human-only); **C** codified body-plan test | **C** — codify the boundary the ten instances already follow | Medium (authoring convention; likely permanent; frequently re-triggered by every future creature) |

## 4. Options

### Option A — DEC-100 as universal default (humanoid-permissive reading)

DEC-100's quartiles are the default Tier-1 split for any creature whose body plan
maps onto the quartet (persistent distinct arm/leg limb types, one head, one torso
mass) — i.e., every stable-limbed biped regardless of size. Bespoke Tier-1 is the
*exception*, carved whenever the body plan structurally diverges (Blood Man, Dragon,
Giant Spider remain valid precedents of the exception).

- **Register reading:** DEC-100 is read as architecture-level ("supplies the numeric
  ranges"); DEC-041(5) "not a shared scheme" is read as governing **Tier-2+ content**
  (each creature's below-Tier-1 anatomy is per-type), while the four Tier-1 zone
  boundaries stay shared where the shape fits. No ruled text amended.
- **Consequences:** matches what all six reusing instances already assume; maximal
  cross-creature consistency (one named quartet everywhere); no re-derivation work.
  Weakness: the exception is left informal — "maps onto the quartet" is judged
  case-by-case, which is exactly the ambiguity the fork complains about.

### Option B — Bespoke-always (strict per-type reading)

DEC-041(5) requires each creature type's Tier-1 to be authored individually;
DEC-100's quartiles are Human-scoped. Every creature template, including Goblin and
Orc, would author its own Tier-1 split (even if the numbers land near 25/25/25/25).

- **Register reading:** DEC-041(5) read literally at full depth; DEC-100's scope is
  narrowed to Human — this is a **scope amendment to a ruled entry** (DEC-100), not
  merely an interpretation, and would additionally need reconciliation with DEC-041(2)'s
  pre-template quartet naming.
- **Consequences:** maximizes "architectural honesty" (Blood Man §6 Q1's argument):
  no template asserts an anatomical structure the creature lacks. But it invalidates
  the common assumption of six existing instances (Ice Troll, Goblin, Orc, Kobold,
  Hobgoblin, Troll all reused by assumption or derivation), imposes re-derivation or
  per-instance ratification work, forfeits cross-creature table consistency, and
  contradicts the register's own 2026-09-16 storage annotations, which treat reuse
  as a defensible posture. Highest-cost option; evidence corpus points against it.

### Option C — Codified body-plan test (recommended default) *(Recommended)*

Codify explicitly the boundary the ten instances have already converged on:

> **T1 rule.** A creature template reuses DEC-100's Tier-1 quartile ranges **iff**
> the creature is a *stable-limbed biped*: it has (i) persistent, individually
> identifiable limbs of two kinds (arms and legs), (ii) a single head, and (iii) a
> torso mass. Otherwise Tier 1 is **bespoke**, authored from the creature's actual
> body plan, with the mechanics unchanged: structural branch × digit-parity for
> multi-limbed creatures (any even count; Dragon/Giant Spider method), midline/
> composite discard for genuinely-multiple or unpaired features, and relabel (A/B)
> where laterality is not persistent (Blood Man method).

- **Register reading:** DEC-100 text untouched (its quartiles stand, now with an
  explicit scope rule); DEC-041(5) is satisfied because the *test itself* is what
  "individual templates per creature type" produces at Tier 1 — the template is
  per-type; it just reaches the same four ranges when the body plan matches.
  Formally this is an interpretation + authoring-rule codification; if Tiwa prefers
  it recorded as an amendment/closure row (DEC-112-adjacent), that is a drafting
  choice for the ruling step.
- **Consequences:** converts the three proposals' shared open question into one
  deterministic test; zero re-derivation (every existing instance already complies);
  future creatures (Bugbear, any arachnid/quadruped/amorph) get an immediate answer;
  preserves Blood Man's architectural honesty where it actually bites. Weakness:
  edge cases will still need judgment (e.g., a wingless tailed biped, a many-armed
  biped — the test gives the *default*, not every answer; novel cases flag to Tiwa
  per DEC-077 as usual).

## 5. Recommended Default — Rationale

**C**, because:

1. it is the only option that changes nothing retroactively — A also changes
   nothing but leaves the boundary informal; B forces rework;
2. it is *already the corpus's de facto rule* (§2.3.1–2.3.2), so codification adds
   determinism without adding new design commitments;
3. it resolves all three carrying questions (Blood Man §6 Q1, Ice Troll §6 Q1,
   Giant Spider's bespoke posture) with a single ruling;
4. it requires no amendment to DEC-100's ruled text — the lowest-risk path through
   a ruled entry's silence.

If Tiwa prefers minimal machinery instead, **A** is the acceptable fallback (same
outcomes for every current instance; the boundary just stays case-by-case).

## 6. Interaction and Sequencing Note

- This ruling would close the Tier-1 fork referenced by the companion brief
  `investigations/tiwas-l004-four-creature-template-open-questions-designer-options-brief-2026-09-16.md`
  (its ACC row presumes candidates remain usable under whichever Tier-1 rule holds;
  no ordering dependency — the two can be ruled in either order or together).
- It is independent of TR-Q2 (DEC-088 regeneration asymmetry) and of all armor/
  laterality content questions.
- Regardless of option chosen, the three bespoke templates' *content* (zone names,
  widths, armor, laterality treatments) remains advisory candidate material pending
  each creature's acceptance — this ruling fixes only the *allocation rule*.

## 7. Explicit Non-Decisions

This brief does not:

- assign a DEC or alter the decision register;
- amend, reopen, or re-scope DEC-100, DEC-041, DEC-112, DEC-136, DEC-137, or
  DEC-139 (Option B *would* require a DEC-100 scope amendment if chosen — it is
  presented, not adopted);
- promote any template to canonical or rule any creature's acceptance posture;
- rule the Goblin/Dragon DEC-084 precedent's scope beyond what DEC-084 itself
  already says;
- author new creature content or stat blocks.

If Tiwa rules, the chosen option (and, for C, the exact codified test text) is
recorded against `_consolidation/decision-register.md` by the designer/OpenCode
workflow after explicit sign-off, per standing governance.
