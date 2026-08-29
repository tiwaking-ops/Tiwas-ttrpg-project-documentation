---
document:
  title: "Project Context"
  version: "1.0"
  status: "Reconstructed from source corpus; not itself a rules document"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
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
- **S-2, Tier-1 only**: the Zero-Step Location Index provider (a deterministic digit-exchange transform of the attacking roll) is locked. Nothing else about hit locations is locked — see below.

## What is explicitly not yet built (Reserved / Open)

Everything else: the broader S-2 architecture (when a Location Index is warranted at all, which Tier a scene uses, anatomical mapping), Outcome Effects (S-3), Wounds (S-4), Armor (S-5), Defense (S-6), Incapacitation/Death (S-7), Difficulty/Stakes (S-8), Extended Tests (S-9/S-10), Rest/Healing (S-11), NPC Compression (S-12), Conditions, Tags, Time/Action, Equipment, Hazards, Magic/Special Abilities, and Setting Modules.

## What is in active non-canonical development

Two real designer rulings currently govern *candidate, non-canonical* S-2 material and are worth knowing about even though they are not Canonical:

1. **S-2 attack-side invocation policy** (accepted candidate, not locked): a four-state classification and a "Named-Outcome Test" determine when a Location Index is warranted for an attack. See `proposals/...` §2.1A and `investigations/tiwas-s2-hit-location-investigation-v5-synthesis.md`.
2. **S-2 non-attack deferral** (binding, non-canonical): non-attack physical resolutions (falls, hazards, structural collapses) generate no Location Index at all, under any framing, until S-4, S-7, or S-8 reaches a design stage that reopens the question. See `proposals/...` §2.5A and `investigations/tiwas-s2-non-attack-location-source-closure-record-v1.2.md`.

## How the project's own documents govern themselves

The project already, internally, distinguishes:

- **Canonical** (locked game mechanics) — `canonical/rules/`
- **Implementation/process guidance with no rule authority** — `roadmap/`
- **Non-canonical design exploration, including real but non-canonical designer rulings** — `proposals/`
- **Evidentiary/analytical investigations feeding those proposals** — `investigations/`

This structure is not something invented by this consolidation — it is a direct transcription of what the source documents already, consistently, say about themselves. See `governance/authority.md`.

## What this consolidation did and did not settle

This consolidation reorganized and indexed the supplied material; it did **not** advance any non-canonical item to Canonical status, did **not** resolve any of the corpus's own explicitly-open questions (Tier selection policy, anatomical mapping, S-3 through S-12 content, H0 Rider B's unadjudicated sub-options), and did **not** reconstruct any prior document version that was referenced but not supplied. See `_consolidation/consolidation-plan.md` for the full account.
