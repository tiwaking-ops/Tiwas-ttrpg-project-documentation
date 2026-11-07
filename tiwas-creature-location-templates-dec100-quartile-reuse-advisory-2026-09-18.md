---
document:
  title: "Tiwas — Creature Location Templates: DEC-100 Quartile-Reuse vs. Bespoke Tier-1 (L-004 Family) — Advisory Options Analysis"
  version: "1.0"
  status: "Advisory / Non-canonical. No DEC assigned. No rule invented, amended, promoted, or superseded. Options analysis only — the underlying fork remains open pending Tiwa's ruling."
  purpose: >
    Consolidates and formalizes the open DEC-112 L-004 design fork surfaced across the ten
    stored Creature Location Template proposals: whether a new creature template's Tier-1
    zone split should default to reusing DEC-100's Human quartiles or should always be
    authored bespoke per DEC-041(5). Synthesizes the evidence already on record, presents
    a three-option analysis, and records a recommendation for Tiwa's consideration.
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-18"
  last_modified_date: "2026-09-18"
  session_type: "Chat advisory session (claude.ai), single-model authorship — carries no independent-review authority"
  sources_consulted:
    - "canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md (internally v1.4)"
    - "_consolidation/decision-register.md (DEC-041, DEC-100, DEC-112, DEC-137, DEC-136, DEC-141, DEC-142)"
    - "Stored L-004 creature-template proposals: Human (adopted, DEC-137), Goblin, Orc, Ice Troll,
       Hobgoblin, Kobold, Troll, Dragon, Blood Man, Giant Spider"
---

# Tiwas — Creature Location Templates: DEC-100 Quartile-Reuse vs. Bespoke Tier-1 (L-004 Family)

**Document class:** Advisory options analysis. Not a ruling. No DEC number is assigned or
proposed. Nothing in this document promotes, demotes, amends, or supersedes any Ruled or
Canonical material. Authority to close the fork described below rests solely with Tiwa.

---

## 1. Purpose and Scope

This report documents, in full, the results of a chat session (2026-09-18) in which the
biggest currently-open cluster of Creature Location Template (DEC-112 L-004) questions was
identified and analyzed: whether the Tier-1 hundred-state split for a new creature template
should **default to reusing DEC-100's Human quartile boundaries**, or whether **every
template must be bespoke-authored** per the literal wording of DEC-041(5).

This question recurs, unresolved, across every one of the ten creature-template proposals
stored to date. It has never been formally ruled. This report exists to consolidate the
scattered evidence into a single citable analysis so that Tiwa can close it once, rather
than it being independently re-raised (and inconsistently answered) in future template
proposals.

---

## 2. Governing Rules and the Precise Gap

| Governing rule | What it establishes | What it leaves open |
|---|---|---|
| DEC-112 L-004 | Location Templates are per-creature-type authored; each creature type has its own template | Silent on whether a new template's Tier-1 boundaries may be *copied* from an existing template or must be *invented* |
| DEC-041(5) | Creature coverage = individual templates per creature type, "not a shared scheme" | Textually reads as bespoke-by-default, but does not explicitly forbid numeric overlap between two templates |
| DEC-100 | Human Tier-1 quartiles: 1–25 Legs, 26–50 Torso, 51–75 Arms, 76–100 Head | Ruled for the Human template only; does not state whether it is the *default starting point* for other creature types |
| DEC-137 | Human v1 100-state allocation (weighted subdivision within the DEC-100 quartiles) | Confirms DEC-100 for Human; does not extend or restrict its applicability elsewhere |

**The fork, stated precisely:** when a new L-004 template is authored, is the Tier-1
hundred-state split (a) DEC-100's numbers by default, deviated from only when the
creature's anatomy structurally cannot support a Legs/Torso/Arms/Head partition, or
(b) always bespoke on principle, with any numeric resemblance to DEC-100 being incidental?

No DEC currently answers this.

---

## 3. Evidence — Disposition of All Ten Stored L-004 Proposals

| Creature | Choice made | Rationale / open-question status |
|---|---|---|
| Human (DEC-137, **adopted**) | Source of the DEC-100 quartiles | N/A — this proposal *is* the quartile ruling |
| Goblin | Reused DEC-100 quartiles unchanged | Clean fit — bipedal humanoid body plan |
| Orc | Reused DEC-100 quartiles unchanged | Clean fit — bipedal humanoid body plan; only `size_medium` vs `size_large` left open |
| Ice Troll | Reused DEC-100 quartiles | §6 Q1 explicitly flagged open — reuse was an **assumption**, not a resolved choice |
| Hobgoblin | Interpolated between Human and Goblin/Orc proportions | §6 Q1 open — cites the Goblin/Orc proportion split as unresolved precedent |
| Kobold | Minor-feature reuse of the quartile structure | Same open Q1, at content level |
| Troll | Derived from Ice Troll (frost/`env:freezing`-tied elements subtracted) | Inherits Ice Troll's unresolved Q1 |
| Dragon | **Bespoke six-zone split**: Torso 40 / Neck 10 / Head 15 / Tail 15 / Wings 12 / Legs-Claws 8 | Explicit departure — no torso-limb-head quartile model fits a winged, tailed quadruped |
| Blood Man | **Bespoke three-zone split**: Core Mass 1–60 / Pseudopod 61–90 / Head-Clot 91–100 | Explicit departure — reformable pseudopods have no persistent "limb," so DEC-100 cannot structurally apply |
| Giant Spider | Bespoke split proposed (non-humanoid, eight-leg body plan) | Explicit departure, flagged as an open fork against non-canonical DEC-100/L-006 |

**Pattern observed:** every bipedal-humanoid creature (Human, Goblin, Orc, Hobgoblin,
Kobold, Troll) reused DEC-100 without structural difficulty. Every non-humanoid or
non-persistent-anatomy creature (Dragon, Blood Man, Giant Spider) required a bespoke split,
and in each such case the stated reason was structural incompatibility of the body plan
with a four-zone Legs/Torso/Arms/Head model — not authorial preference.

**Secondary data-hygiene finding (applies independent of how the fork resolves):** several
of the above proposals (Ice Troll, Blood Man, Hobgoblin, Dragon, Goblin, Orc) were authored
against the **pre-adoption Human candidate**, not the adopted DEC-137 allocation. Any
Human-comparison figures in those documents (e.g., "Thigh 13," "Skull 13") are stale and
should be re-derived from DEC-137 before further use.

---

## 4. Option Set

| Option | Rule | Consequence |
|---|---|---|
| **A — DEC-100 as default, bespoke as escape valve** | New templates start from DEC-100's four zones unless the creature's body plan cannot support a Legs/Torso/Arms/Head partition (no persistent limbs, non-bilateral symmetry, extra limbs, no discrete head, etc.), in which case a bespoke split is authored and explicitly flagged | Fast authoring for the common case (most humanoids); gives an explicit, checkable trigger for deviation; matches every reuse case observed in §3 |
| **B — Every template is bespoke (literal DEC-041(5))** | No template may cite DEC-100 as its source; each author derives its own hundred-state split from first principles, even where the numeric result happens to be four 25-wide zones | Maximally faithful to "individual templates, not a shared scheme"; discards no actual content (identical numbers can still be reached); adds authoring overhead with no mechanical payoff for the humanoid majority |
| **C — Body-plan classification rule** | A small, explicit taxonomy (e.g., *bipedal-humanoid*, *quadrupedal*, *multi-limbed/segmented*, *amorphous/formless*) is defined, with DEC-100 pre-assigned to *bipedal-humanoid* and each other class either given its own future pre-ruled template or explicitly deferred to bespoke authoring | Formalizes the pattern that already emerged organically across the ten stored proposals; gives future template authors (and OpenCode) a rule to apply instead of re-litigating this Q1 on every new creature; scales cleanly as further body plans are added |

---

## 5. Recommendation

**Option C** is recommended, for three reasons drawn directly from the corpus:

1. **It matches existing behavior exactly.** No stored content would need to change: the
   six humanoid templates keep DEC-100; the three non-humanoid templates keep their
   bespoke splits.
2. **It resolves the recurring Q1 without repealing DEC-041(5).** Each creature type still
   receives its own authored template (the letter of DEC-041(5) is preserved); what Option
   C settles is only whether copying DEC-100's numbers is a legitimate authoring shortcut
   for a given body plan — not whether a template is required at all.
3. **It follows the project's own recent simplification precedent.** DEC-136 (secondary-roll
   removal), DEC-141 (Tier-combination formula), and DEC-142 (Skill-Tier gate) each closed a
   similarly recurring open fork with a single "pick the simple default, expand later"
   ruling rather than re-deciding per instance. This fork is structurally identical: a
   recurring per-creature question with a clear majority pattern already visible in the
   evidence.

**If Option C is adopted**, a minimal closing ruling would need to specify only:

- The starting taxonomy (bipedal-humanoid → DEC-100 default; all other classes →
  bespoke-by-default until/unless a further body-plan class is separately pre-ruled).
- That bespoke splits still route through DEC-112's L-003–L-014 mechanics unchanged
  (single-source deterministic resolution, parity laterality, parent/child fallback) —
  only the Tier-1 zone boundaries differ under a bespoke split.

This report makes no ruling on Tiwa's behalf; Option A, B, or C (or a fourth option not
enumerated here) remain equally available for Tiwa's decision.

---

## 6. Secondary Open Items Riding on This Fork

These were each flagged in the stored proposals and remain unresolved regardless of which
option above is chosen:

- Giant Spider's exact bespoke zone boundaries for an eight-leg body plan.
- Dragon's `size_huge` / `size_gargantuan` Tag extension — a separate DEC-080 T1 namespace
  addition, not resolvable inside this fork.
- The stale pre-DEC-137 Human-comparison figures noted in §3, independent of how this fork
  resolves.

---

## 7. Explicit Non-Findings

For clarity and to prevent this report from being mistaken for authority it does not carry:

- **No DEC is assigned or inferred by this document.**
- **No rule is invented, amended, promoted, or superseded.**
- **No template's Tier-1 boundaries are changed by this document** — Human (DEC-137),
  Goblin, Orc, Ice Troll, Hobgoblin, Kobold, Troll, Dragon, Blood Man, and Giant Spider all
  retain their previously stored content exactly as recorded in the register.
- **This document is single-model authorship** (Claude Sonnet 5, chat surface) with no
  independent second-assessor pass; per the project's provenance discipline, this is
  recorded as a weaker form of review than a corroborated assessment and confers no
  additional authority on its own conclusions.

---

## 8. Recommended Next Step

Should Tiwa wish to close this fork, the recommended path is a single in-session ruling
selecting Option A, B, or C (§4), following the same lightweight format used for DEC-136,
DEC-141, DEC-142, and DEC-143. No further research or additional advisory drafts are
needed to make that decision — the evidence in §3 is exhaustive of what is currently on
record.

---

**End of report.**

**Author:** Claude Sonnet 5 (`claude-sonnet-5`)
**Date:** 2026-09-18
**Classification:** Advisory options analysis — No DEC assigned, non-canonical.
