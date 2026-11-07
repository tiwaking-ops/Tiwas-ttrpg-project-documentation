---
document:
  title: "Project Context"
  version: "1.0"
  status: "Reconstructed from source corpus; not itself a rules document"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
    - {name: "nemotron-3-super-120b-a12b:free", version: "unknown"}
  last_modified_by_llm: {name: "tencent", version: "hy4-preview-free"}
  created_date: "2026-08-29"
  last_modified_date: "2026-11-08"
---

# Project Context

## What Tiwas is

Per its own Canonical Rules (`canonical/rules/...` §1):

> Tiwas is a high-consequence percentile universal RPG in which every meaningful attempt uses the common resolution engine; every test costs resources; failure generates mechanical growth; meaningful success changes the tactical or narrative state.

Locked design priorities, in order:

1. Granular physical simulation where the situation warrants it.
2. Heroic resilience / low permanent character loss rate.
3. Minimum resolution steps per exchange without sacrificing Priority 1.

## What is currently built (Canonical / Locked)

- The complete Core resolution engine: d100 roll-under, the 100-Fumble rule, Doubles, the 24-attribute matrix, derived statistics, Skills (Tier/Cap/Starting Value), the 9-step Core Test Transaction, resource cost/Overflow, Recovery, Failure XP, the Skill Roll Pool, General XP, and Advanced Skills.
- **S-1 — Universal Opposed Contest**: fully locked, including Margin/Blackjack/Hybrid Committed Quality measures.
- **S-2**: the Tier-1 Zero-Step Location Index provider (a deterministic digit-exchange transform of the attacking roll) and the attack-side invocation/warrant policy (§14.7, DEC-017, promoted 2026-09-05) are locked. Nothing else about hit locations is locked — see below.

## What is explicitly not yet built (Reserved / Open)

Nothing beyond §"What is currently built" above is **Canonical**. In addition to the Core engine, S-1 and the two locked S-2 items, the following are **ruled by the designer but still non-canonical** — they carry real designer rulings recorded in `_consolidation/decision-register.md` (DEC-001…DEC-156) and none has completed the 8-step Promotion Rule (REQ-021) except DEC-017: S-3 Effects, S-4 Wounds, S-5 Armor, S-6 Defense, S-7 Incapacitation/Death, S-8 Difficulty, S-9/S-10 Extended Tests, S-11 Rest/Healing, S-12 Creature/Campaign, Encumbrance, Conditions, Tags, Time/Action (partly), Equipment, location anatomy, and the G-series movement mechanics.

Still **Reserved / not ruled** at any layer: the full Magic / Special Abilities subsystem (Canonical §15 / DEC-015), the full Time/Action subsystem definition, Setting Modules, and the specific content-authoring corpus under DEC-077 / DEC-077.A. See the decision register's inline "carried open" items for the live list.

## What is in active non-canonical development

Two real designer rulings govern *candidate, non-canonical* S-2 material. One has since been promoted to Canonical:

1. **S-2 attack-side invocation policy** — **CANONICAL as of 2026-09-05 (Canonical §14.7, DEC-017, 8-step Promotion Rule):** a Tier-1 Location Index is generated for an attack only when the W1/W2/W3 gates (explicit distinct outcome, established location-dependence, current resolvability) are satisfied. See `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` §14.7 (v1.4) and `investigations/tiwas-dec017-s2-invocation-promotion-package-2026-09-05.md`.
2. **S-2 non-attack deferral** (binding, non-canonical): non-attack physical resolutions (falls, hazards, structural collapses) generate no Location Index at all, under any framing, until S-4, S-7, or S-8 reaches a design stage that reopens the question. The mechanism for non-attack cases where a Wound Effect applies is governed by DEC-037. See `proposals/...` §2.5A and `investigations/tiwas-s2-non-attack-location-source-closure-record-v1.2.md`.

**[Maintenance note, 2026-11-08 — snapshot refreshed, nothing promoted.]** The two items above are no longer the whole picture: since 2026-08-31 the decision register has grown to **DEC-001 … DEC-156** (latest row DEC-156, 2026-09-21) and now records non-canonical designer rulings across S-3 to S-12, Encumbrance, Conditions, Tags, Equipment, location anatomy and the G-series movement mechanics. Detail does not confer authority (see `governance/status-model.md`); **DEC-017 remains the only item ever promoted to Canonical.** For the authoritative live list consult `_consolidation/decision-register.md` rather than this orientation snapshot.

## How the project's own documents govern themselves

The project already, internally, distinguishes:

- **Canonical** (locked game mechanics) — `canonical/rules/`
- **Implementation/process guidance with no rule authority** — `roadmap/`
- **Non-canonical design exploration, including real but non-canonical designer rulings** — `proposals/`
- **Evidentiary/analytical investigations feeding those proposals** — `investigations/`

This structure is not something invented by this consolidation — it is a direct transcription of what the source documents already, consistently, say about themselves. See `governance/authority.md`.

## What this consolidation did and did not settle

This consolidation reorganized and indexed the supplied material; it did **not** advance any non-canonical item to Canonical status, did **not** resolve any of the corpus's own explicitly-open questions (Tier selection policy, anatomical mapping, S-3 through S-12 content, H0 Rider B's unadjudicated sub-options), and did **not** reconstruct any prior document version that was referenced but not supplied. See `_consolidation/consolidation-plan.md` for the full account.

**[Maintenance note, 2026-11-08.]** Several of those formerly-open questions have since been closed by *later designer rulings* (OPEN-001…OPEN-010 in `_consolidation/decision-register.md` §C are all closed or superseded), not by this consolidation. The consolidation's own non-action statement above is unchanged and remains correct.
