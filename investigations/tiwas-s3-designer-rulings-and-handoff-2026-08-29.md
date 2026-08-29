---
document:
  title: "Tiwas S-3 Outcome Effects — Designer Rulings & Investigation Handoff"
  version: "v1.0"
  status: "Designer ruling record (non-canonical) — resolves Q-S3-1 through Q-S3-4 from tiwas-s3-outcome-effects-investigation-v0.1-draft.md; opens one new follow-on investigation"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
  ruling_authority: "Human designer, via conversation with Claude Sonnet 5, 2026-08-29"
revision_note: >
  Revision pass (same date) narrows Q-S3-3's scope after independent review by
  opencode/big-pickle flagged that "Incapacitation" and "Function Impairment" are not
  part of the S-3 candidate Effect menu (Proposals §3.1) and are better read as S-7/S-4
  territory per Roadmap §9's own framing ("a future subsystem (S-3/S-5/S-7/S-10)").
  Also flags "Dizzy" as a session-introduced candidate, not a pre-existing menu item,
  and corrects a loose citation. No ruling content from Part 1 is reversed — this
  revision narrows scope and adds flags only. See inline notes marked
  "[Revision note]" at point of change.
---

# Tiwas S-3 — Designer Rulings & Handoff to OpenCode

## Purpose

This document records designer rulings made in conversation on 2026-08-29, resolving
the four open questions (Q-S3-1 through Q-S3-4) raised in
`investigations/tiwas-s3-outcome-effects-investigation-v0.1-draft.md`. It also opens
one new non-canonical investigation thread surfaced during that conversation.

**These are non-canonical designer rulings** — the same evidence class as DEC-017
through DEC-022 in `_consolidation/decision-register.md` (real human decisions about
candidate/non-canonical material). They do **not** modify Canonical Rules. Per the
8-step Promotion Rule (Proposals/WIP §21), they would need to complete that full
process — including formal documentation as a proposal, review, and a Canonical Rules
update — before becoming Canonical.

**Suggested filing:** these rulings should be written into `proposals/` (as a new S-3
section or subsection, mirroring how the S-2 candidate policy lives in Proposals §2.1A)
and cross-referenced from `_consolidation/decision-register.md`. **[Revision note]**
Because §B of that register is specifically corpus-derived (DEC-017–DEC-022, sourced
from D3/D4/D5), and these are in-session human rulings with a different provenance
chain, they should be recorded in a **distinct, clearly-labelled section** (e.g. a §D
for session-derived non-canonical rulings) rather than merged into §B — preserving the
existing corpus-vs-session distinction rather than blurring it. The original
investigation draft in `investigations/` should be updated to mark Q-S3-1–4 as Ruled,
consistent with how D3/D4's own revision records track resolved items.

---

## Part 1 — Rulings

### Q-S3-1 — RULED: Tiered Effect menu

The S-3 Effect menu (Proposals §3.1's ten candidates) is structured as a **tiered
menu**, not a flat list:

- **Base tier (usable now, self-contained against Canonical):**
  - Inflict Injury — **HP-only form** (plain damage; does not touch S-4 wounds; see
    Q-S3-4 below)
  - Open Retreat / Compel Yield

- **Gated tiers** (each unlocks automatically when its named dependency locks; no
  hooks should be pre-built for these in the meantime — see Roadmap §9's own
  language on the S-2 non-attack deferral, "implementation should not pre-build
  hazard-location hooks in anticipation," and the general principle in Roadmap §24
  Rule 6 against silently resolving an open designer fork):
  - *Position tier* — Force Movement/Seize Position, Seize Tempo → unlocks with
    Time/Action (Proposals §12)
  - *Condition tier* — Impose Condition, Bleed/Ongoing Drain, and (session-proposed,
    not part of the original menu — see flag under Q-S3-4) Dizzy-type effects →
    unlocks with Conditions (Proposals §10)
  - *Equipment tier* — Damage Equipment → unlocks with Equipment (Proposals §13)
  - *Defense tier* — Guard Break → unlocks with S-6 (Proposals §6)
  - *Location tier* — Choose Location → unlocks with S-2 invocation-policy promotion

- **Disarm / Break Hold** — tier placement determined by Q-S3-3 (below): placed,
  along with Equipment Damage and Armor Bypass, in a combined Tag+Location-gated
  category, itself dependent on both the Tags subsystem and the anatomical mapping
  table. Function Impairment and Incapacitation are **not** placed by this ruling —
  see the Q-S3-3 deferral note.

### Q-S3-2 — RULED: Flat one-Effect-per-win

No Quality-based scaling and no "purchasing" of additional Effects off the size of a
single win. Every successful S-1 contest earns exactly one Effect from the currently
unlocked tiers. A second/additional Effect requires a **separate opposed roll** —
mechanism not yet designed; deferred to the new investigation (Part 2, Q-S3-2b).

### Q-S3-3 — RULED: Combined Location + Tag gating for the in-scope State-3 Effects

**[Revision note]** The original pass applied this ruling to all five State-3 concepts
listed in Roadmap §9 (Disarm, Equipment Damage, Function Impairment, Armor Bypass,
Incapacitation). On review, only **Disarm/Break Hold**, **Equipment Damage**, and
**Armor Bypass** actually appear in the S-3 candidate Effect menu (Proposals §3.1).
Roadmap §9 itself frames all five as concepts a *future subsystem* — "S-3/S-5/S-7/S-10"
— must explicitly claim; it does not assign them to S-3. **Function Impairment** and
**Incapacitation** are removed from this ruling's scope and flagged below as
deferred-out-of-S-3.

For **Disarm/Break Hold, Equipment Damage, and Armor Bypass**, triggering requires
**both**:

1. The relevant gear/ability carries a matching Tag (e.g., `[Disarming]`,
   `[Armor-Piercing]`); **and**
2. The Zero-Step Location Index (when the scene runs at Tier 1+) supports the Effect
   (e.g., lands on a hand/arm region for Disarm).

**Dependencies accepted by this ruling:**
- Tags subsystem (Proposals §11, Reserved) — needs at minimum a starter tag
  vocabulary covering these three Effects.
- Anatomical mapping table (Canonical §14.3, still unbuilt) — needed only if/when
  Tag+Location gating is used for *this* purpose; per Part 2 below, ordinary
  Injury/Condition effects at Tier 0 do not require it (see Q-S3-4 ruling).
- The S-2 attack-side invocation policy (Proposals §2.1A) still requires its own
  independent promotion path; unaffected by this ruling.

**New open question spun off from this ruling:** what happens on a *partial* match
(Tag present but location doesn't support it, or vice versa)? Not ruled — see Q-S3-3a
in Part 2.

**[Revision note] Deferred out of S-3 scope — Function Impairment and
Incapacitation.** These remain State-3 per Roadmap §9 but are not part of the S-3
candidate menu. They are left for whichever future subsystem claims them —
Incapacitation reads most naturally as S-7 (Proposals §7, Incapacitation/Death)
territory; Function Impairment reads most naturally as an S-4 Condition/Disability
concept. No S-3 ruling applies to either. If a future S-3 revision wants to claim
either as an Effect, that would need its own explicit ruling, not an extension of
Q-S3-3 by inference.

### Q-S3-4 — RULED: S-3/S-4 boundary confirmed as prototype-only; no interface work needed yet

Because Inflict Injury (the base-tier Effect) is HP-only and does not produce a
localized wound, there is currently **no S-3/S-4 interface to prototype**. The
Roadmap §10 boundary (S-3 may sketch that a data pipe exists toward a future Wound
Engine, but must not lock wound severity thresholds, activation triggers, disability
effects, or death checks) is confirmed as-is and remains dormant until a
wound-producing Effect is proposed.

**Direction captured for the future S-4 investigation (not an S-3 ruling, not
Canonical, recorded here for continuity):**

- A **location-based injury system** is the preferred future direction for S-4:
  localized, lasting (non-HP) injury should emerge from **repeated hits to the same
  body location**, using the Zero-Step Location Index as the natural rarity control —
  this supports Core Priority 2 (heroic resilience / low permanent character loss)
  by making significant injury a product of accumulated bad luck rather than a single
  tunable threshold.
- **No Location Index → no Injury Effect, ever, full stop.** Tier-0 scenes (which
  generate no Location Index, per Proposals §2.3) can never produce localized injury.
- Tier-0 scenes **can** still produce non-injury Effects (e.g., Bleed, and a
  session-proposed "Dizzy" — see flag below) via the Condition tier — these do not
  require a Location Index at all. This does not add new Effects to the Q-S3-1 menu
  beyond what's flagged; it clarifies that Condition-tier Effects are available at any
  Location Tier including 0, while Injury-with-lasting-consequence is Tier 1+ only.
- **[Revision note] "Dizzy" flagged as a new, session-introduced candidate.** It does
  not appear in the original ten-item S-3 menu (Proposals §3.1). It surfaced in this
  conversation as an example Condition-tier effect. It should be tracked as a
  candidate addition to the Condition tier, not mistaken for a pre-existing menu item,
  and would need its own confirmation if/when the Condition tier is designed in
  detail.
- **Per-location hit-history tracking is left to GM adjudication, not
  system-tracked state.** No persistent per-location hit counter is required. This
  trades system-guaranteed rarity for simplicity (Core Priority 3) — different GMs
  will call "same location" differently, which is an accepted tradeoff, not a defect
  to fix later.
- Healing behavior for such injuries ("maybe they heal, maybe not") remains fully
  open — explicitly not decided here.

This direction should be written up as the **opening brief for a future S-4
investigation** (mirroring how D4/D5 opened the S-2 investigations), not folded into
S-3's own scope.

---

## Part 2 — New investigation to open: "S-3 Effect Identity, Gating & Multi-Effect Opposition"

Status: **Open, non-canonical, no rulings.** Suggested location: `investigations/`,
same tier as D4/D5 and the S-3 draft itself.

- **Q-S3-2a — Effect identity / naming-collision risk.** Named Effects (Disarm,
  Bleed, etc.) create a naming-collision risk: since Advanced Skill names carry zero
  mechanical weight (Canonical §12.3), nothing currently stops a player from naming a
  skill after an Effect and arguing entitlement to it. Needs a ruling on whether
  Effects require a formal tag/category system on Advanced Skills, or stay purely
  declared-intent with no skill-name-based gating at all.
- **Q-S3-2b — Second-Effect opposed-roll mechanism.** What governs the roll for an
  additional Effect beyond the free one (per the Q-S3-2 ruling above)? Same Skill as
  the original contest, a different Skill, a flat check? Does the target get any
  defensive roll, given S-6 Defense is still Open?
- **Q-S3-3a — Partial Tag/Location match behavior.** If an attempted Effect has a
  matching Tag but the Location Index doesn't support it (or vice versa), does the
  Effect simply fail and fall back to plain damage (consistent with the flat
  one-Effect-per-win ruling), or is there a partial/reduced outcome?
- **Q-S3-5 — Auto-apply vs. contested application.** Does winning S-1 with a declared
  Effect apply it automatically, or does the Effect itself require passing some
  further check against the target? Currently undecided; only "auto-apply" is
  buildable today since S-6 Defense isn't locked.
- **Disarm/Break Hold's specific tier assignment** (carried over from Q-S3-1),
  informed by how Q-S3-3's combined gating and Q-S3-3a resolve.

---

## Part 3 — Explicitly not decided, not implied, by this document

Per Roadmap §24 Rule 6 (never silently resolve an open designer fork) and Proposals
§21 (Promotion Rule), the following remain untouched by this ruling set:

- No Canonical Rule is changed. Zero-Step, S-1, and all other locked mechanics are
  unaffected.
- The S-2 attack-side invocation policy (Proposals §2.1A) and the S-2 non-attack
  deferral (Proposals §2.5A) are unaffected and not reopened.
- The anatomical mapping table (Canonical §14.3) remains unbuilt; this document does
  not build it, only scopes when it would be needed.
- The Tags subsystem (Proposals §11) remains Reserved; no tag vocabulary is defined
  here.
- S-4 wound severity, activation thresholds, and consequences remain entirely
  undecided — the "direction" captured under Q-S3-4 is a steer for a future
  investigation, not a rule.
- Nothing in this document completes the 8-step Promotion Rule for any item; all
  rulings here remain non-canonical pending that process.
