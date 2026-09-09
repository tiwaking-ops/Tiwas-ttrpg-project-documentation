---
document:
  title: "Tags / Effects / Conditions Unification — Decision Draft"
  version: "v0.1 (draft)"
  status: "Advisory working document — NOT canonical, NOT a ruling, NOT a proposal accepted into Proposals/WIP. For Tiwa's own review only."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-06"
  last_modified_date: "2026-09-06"
governance_note: >
  This document is Claude acting in its advisory-only capacity (no ruling authority,
  no repository access). It responds to a design-review prompt asking for a concrete,
  adoptable Decision Draft, not merely options-analysis. Nothing here is a ruling —
  it is written to be ruled on, edited, or rejected by Tiwa, then (if adopted)
  recorded by OpenCode against the live register through the normal 8-step
  Promotion Rule. All DEC citations reference the existing non-canonical decision
  register; none of them are altered by this document.
---

# Tags / Effects / Conditions Unification — Decision Draft

## 1. Executive Verdict

**Partial merge, not full merge.** Effects and Conditions are *already* the same
mechanical shape in practice — DEC-079's Condition format (`Tier-Y Condition Value Z`,
`Z = −Y`, optional `Location X`) is structurally identical to DEC-035.A's Wound record
format. Formalizing "Effect and Condition share one backbone" is close to a free
lunch: it removes duplicated rule text without erasing any distinction that is
currently doing work.

Folding **Tags** into that same backbone is where the hypothesis gets expensive. Tags
are deliberately stateless, non-numeric, vocabulary-only metadata (DEC-080 Q4,
Proposals §11) — of the 34 alpha Tags in DEC-080, only one (`state:sundered`) has ever
needed a Tier/Magnitude/removal rule. Forcing Tier/Magnitude fields onto
`slot:main_hand` or `damage:slashing` doesn't reduce complexity, it manufactures inert
fields that every future Tag author has to explicitly ignore. The "Tags counter Tags"
idea, taken literally as Tag-to-Tag arithmetic, also risks turning Tags into a second
active resolution layer — something DEC-058/080/088 and Invariant 17 were written
specifically to prevent.

Recommendation below: merge Effect+Condition into one schema now; keep Tags on a
compatible but mostly-inert version of that schema, so a *future* graded Tag doesn't
need a bespoke ruling — but do not treat "Tag" and "Condition" as the same fiction-level
concept, and do not build a generic Tag-vs-Tag counter primitive.

## 2. What "One Mechanical Backbone" Actually Means

A single record shape, differentiated by a required `Type` field, not three parallel
rule systems:

| Field | Required for | Meaning |
|---|---|---|
| `Type` | All | `Tag` \| `Effect` \| `Condition` — fiction-level identity only |
| `ID` | All | Vocabulary key, e.g. `state:sundered`, `wounded`, `inflict_injury` |
| `Location (X)` | Optional, all types | Numeric Location Index or absent |
| `Tier (Y)` | Required: Effect, Condition. Optional: Tag | Severity/production tier |
| `Magnitude (Z)` | Required whenever Tier present | `Z = −Y` (DEC-035.A cl.3 / DEC-079 C2) |
| `Persistence` | All (default, not stored per-instance unless overridden) | `Persistent` (Tag default) \| `Temporary` (Effect/Condition default) |
| `Removal` | Required only if Persistence = Persistent | Named trigger, or `GM Fiat` |
| `Source` | All | Skill/Effect/GM authorship provenance |

`Type` is the fiction-level label the user wants preserved. It changes nothing about
how a record is *consumed* — an Effect is still the one-per-win payload of a
successful S-1 contest (DEC-023–030, DEC-107); a Condition is still the standing state
that payload produces (DEC-079); a Tag is still classification/permission metadata
read by a consuming subsystem (DEC-080 Q4). What's unified is the *container*, not the
*role*.

## 3. Impact Analysis of the Five Ideas

### 3.1 "Tags are like Effects, but Tags are Permanent; Effects are caused by a Skill Roll."

Doesn't hold up as a clean split. DEC-079 C8 already makes Sundered a *Condition*
(Effect-produced) that is *also* permanent-until-repaired — Conditions already span
both durability profiles. DEC-088's Conditional-Trait Binding shows an Effect/Trait
can be "permanent while `env:X` holds" without touching Tag machinery at all. So the
Permanent/Temporary axis is real, but it's a **default**, not a **type boundary** — it
already cuts across Conditions, not just across the Tag/Effect line. Useful as
authoring guidance (Tags default persistent, Effects/Conditions default temporary);
not useful as the thing that distinguishes the three types.

### 3.2 "Tags, like Effects, have Tier Y Magnitude Z. Tags may also have Location X."

Direct textual conflict with DEC-080 Q4 ("Tags carry identity/vocabulary only;
mechanical effects live in consuming subsystems") if a Tag's own Magnitude does
mechanical work. Of DEC-080's 34 alpha Tags, essentially none have a natural
Tier/Magnitude — `handling:heavy`, `defense:shield`, `creature:size_large` are boolean
classifications, not graded quantities. Adding the field to *all* Tags is schema noise.
It only pays for itself on the minority that are genuinely graded state — currently
exactly one (Sundered, DEC-060/079 C8) plus one flagged-open future case (graded
`env:` temperature tags, "carried open" per DEC-088).

**Verdict:** make the field *available*, not *populated by default*. This is fixed in
the recommended schema (§6) by making Tier/Magnitude optional for Tags.

### 3.3 "Tags can counter other Tags (creature-side ignores-darkness vs env:darkness)."

Under-specified as a mechanic. Two readings:

- **Boolean presence-counter** ("if Tag A is present, Trait X's binding to Tag B is
  suppressed"): fully compatible with statelessness — nothing is mutated, it's an
  extra clause evaluated by the *consuming* Trait/Effect. This is not new: DEC-088's
  Condition Clause grammar (`Active only while [env:X] is present`) already supports
  exactly this shape once extended to allow a compound expression. A Night-Vision
  counter to `env:darkness` is: the darkness Skill-penalty binding reads `Active only
  while [env:darkness present] AND [creature lacks tag:night_vision]`. No Tag ever
  touches another Tag.
- **Magnitude-arithmetic counter** (subtracting one Tag's Magnitude from another's):
  requires Tags to carry Magnitude (3.2) *and* a defined evaluation order/precedence —
  this is new resolution machinery outside the Core Test Transaction, and risks
  reading as a second resolution engine (Invariant 18) if it becomes general-purpose
  rather than a single hard-coded case.

**Verdict:** adopt the boolean/Condition-Clause reading only. Reject a generic
Tag-vs-Tag arithmetic primitive as its own subsystem.

### 3.4 "Tags and Conditions are NOT distinct."

The largest real collision. DEC-079 gives Conditions an exact numeric format, a fixed
magnitude rule, and *per-Condition* stacking/removal rules (same-tier-adds vs
highest-tier-only, 14 authored entries). DEC-080 gives Tags an open, non-numeric,
namespace-based vocabulary with *no* stacking rule at all — because most Tags are
simple booleans. Proposals §11 states "Tags are not Conditions" as design direction
(non-canonical, but a stated architectural line).

The one existing precedent for blurring this line is DEC-079 C8 itself: Sundered is
explicitly "Condition + Tag model" — a Tag (`state:sundered`) used as the *identity
handle* other subsystems check for, paired with a Condition-shaped *mechanical body*
(reduced effectiveness, cumulative at same tier, permanent until repaired). That's not
"Tags and Conditions are the same thing" — it's "one state can wear both hats." That
is exactly the Type/Subtype pattern in §2, generalized from a one-off special case
into an explicit, reusable pattern.

A literal full merger (delete the boundary) would force every one of the 34 alpha Tags
to acquire authored Tier/Magnitude/stacking/removal rules even where none are needed
(`slot:main_hand` gains a stacking rule?) — this is a large authoring-burden increase,
directly opposed to the stated goal.

**Verdict:** reject literal identity. Adopt Type/Subtype (§2/§6): a record can declare
itself `Type: Tag` and *also* carry a Condition-shaped mechanical body, generalizing
the Sundered precedent, without collapsing the boundary for the ~33 Tags that don't
need one.

### 3.5 "Tags can be Removed."

Not a conflict — a genuine gap. Only one worked case exists (Sundered: "permanent
until repaired," DEC-060/079). No general Tag-removal grammar exists anywhere in the
corpus. This is cheap to fix and doesn't require any schema merger at all — it can be
added to the existing Tag system standalone.

**Verdict:** adopt as-is. Every Tag authored with `Persistence: Persistent` must
declare a `Removal` trigger (named action/Effect, or `GM Fiat` as the unspecified
default), generalizing Sundered instead of leaving future permanent Tags without a
removal path.

## 4. The Complexity Math

- **Effect + Condition merge:** net **reduction**. The two already have identical
  numeric shape (Tier-Y/Value Z=−Y/optional Location X — compare DEC-035.A and
  DEC-079 side by side). Writing one schema section instead of two removes duplicate
  rule text and removes the risk of the two formats silently drifting apart (as
  DEC-035 → DEC-035.A → DEC-107 already shows happened once with Wound-severity
  wording). This part of the proposal should be adopted regardless of what happens to
  Tags.
- **Tag merge (full, as literally stated):** net **increase** for roughly 33 of 34
  current alpha Tags — each gains unused fields and an implicit "N/A" burden, and the
  proposal invites rules-lawyering questions ("can `slot:main_hand` be Removed? Does
  it have a Tier?") that don't currently exist because Tags are simple.
- **Tag merge (schema-compatible, fields optional, as recommended in §6):** roughly
  **complexity-neutral to slightly positive**. Existing Tags are untouched in practice
  (fields stay empty/inert, per DEC-080 Q4). The win is narrow but real: the *next*
  graded Tag (a future `env:cold_severity`, say) gets a ready-made mechanism instead of
  a bespoke DEC the way Sundered (DEC-060) and env:freezing (DEC-088) each needed one.

**Honest bottom line:** this proposal, as five ideas taken together, does not reduce
total rulebook weight. It relocates and partially reduces it — real savings on the
Effect/Condition side, roughly a wash on the Tag side, with the size of the wash
depending entirely on how disciplined the "optional field" boundary is held.

## 5. Conflicts and Honest Tensions

**(a) Tag-counters-Tag vs. stateless/read-only guardrail.** Resolved above (§3.3):
boolean presence-composition in the *consuming* Trait's Condition Clause is safe and
sufficient; Magnitude-vs-Magnitude Tag arithmetic is not currently safe without new
resolution machinery and should not be built as a general primitive.

**(b) "Tags and Conditions are NOT distinct" vs. the current distinct-format design.**
Resolved above (§3.4): Type/Subtype, not identity. DEC-079's per-Condition
stacking/removal rules and DEC-080's vocabulary-only Tag default both survive
unmodified; only records that are *deliberately authored* with both a Tag identity and
a Condition body (the Sundered pattern) cross the line, and they already do so today.

**(c) Permanence/removal phrasing.** The user's own clarification ("default state, not
absolute") is the right resolution and needs no new enum — `Persistence` is a
per-Type default (Tag → Persistent, Effect/Condition → Temporary), overridable at
authoring time by giving the specific instance its own `Removal` trigger. This is
consistent with the DEC-035.A cl.6 "GM Fiat is universal" override precedent and adds
exactly one new field (`Removal`) rather than a permanence sub-system.

**(d) Does this reopen DEC-025?** No. DEC-025 rejected a formal tag/category
*vocabulary attached to Skills* specifically because it let Skill choice gate Effect
entitlement (exploitable, and rejected on that exact rationale). This proposal is
about *state records* — Tags/Effects/Conditions attached to characters, items,
locations, or scenes — not Skill-side classification. Nothing here gives a Skill a Tag
or lets a Tag determine which Effects a Skill can produce. Flagging this explicitly
because it is the adjacent-sounding decision most likely to get silently re-litigated
by accident if this proposal is read carelessly.

## 6. Concrete Recommended Design

1. **Merge Effect and Condition into one schema now** (§2 table), with `Type` as the
   only distinguishing field. This is the low-risk, clearly-positive half of the
   proposal.
2. **Extend the same schema to Tags, but leave Tier/Magnitude/Location optional and
   inert by default.** An un-graded Tag (the current 33 of 34) behaves exactly as
   today — pure vocabulary, read by consuming subsystems, no numeric role. This
   satisfies idea 3.2 without violating DEC-080 Q4.
3. **A Tag may be authored with Tier/Magnitude only when a specific ruling grants it
   one** (Sundered today; any future graded Tag tomorrow) — this generalizes DEC-079
   C8's pattern instead of repeating a bespoke ruling per case.
4. **Reject a Tag-to-Tag counter primitive.** Countering is expressed as a compound
   boolean clause (AND/OR/NOT over Tag presence) on the *consuming* Trait/Effect,
   extending DEC-088's single-Tag Condition Clause grammar. No Tag reads or modifies
   another Tag.
5. **Adopt general Tag removal.** Any Tag authored as `Persistence: Persistent` must
   declare a `Removal` trigger (named action/Effect, or `GM Fiat` if unspecified),
   generalizing DEC-060/079's Sundered precedent to all future permanent Tags.
6. **DEC-007.A / Invariant 17 remain absolute and unmodified.** No field on any record
   Type — including a Tag's new optional Magnitude — may read, redirect, or modify
   Overflow, HP, MP, or Physical Energy directly. Any resource consequence still
   routes exclusively through DEC-027 (Effect auto-apply) and DEC-007 (Overflow).
7. **DEC-025 is untouched.** No Skill acquires a Tag or category; Skill-side gating
   remains rejected.

**What this departs from:** Proposals §11's flat sentence "Tags are not Conditions" is
superseded as *literal wording* — they now share a container — but its functional
intent (Tags default to lightweight, non-numeric, vocabulary-first) is fully preserved
by making the numeric fields optional and inert by default. This should be recorded
explicitly as a wording supersession if adopted, not silently dropped.

## 7. Open Questions to Rule On

- Does this become a rules-text merge (Proposals §10/§11 and the S-3 Effect sections
  are rewritten into one shared section) or stay an internal schema note with the
  three existing document sections left as-is?
- Should `Persistence` be a real stored field, or purely descriptive/non-binding prose
  guidance? (Recommendation above treats it as a default, not a hard field — worth an
  explicit ruling either way.)
- Who authors the compound boolean (AND/OR/NOT) extension to DEC-088's Condition
  Clause grammar — is that itself a new DEC, since DEC-088 only specified single-Tag
  clauses?
- If a Tag is authored with Tier/Magnitude, does it inherit DEC-079's existing
  stacking rules wholesale, or does each graded Tag need its own stacking rule the way
  each of DEC-079's 14 Conditions currently does?
- Should the Effect+Condition merge (§6 items 1, low risk) be promoted independently
  and ahead of the Tag schema extension (§6 items 2–5, higher risk), rather than as one
  package through the 8-step Promotion Rule?
