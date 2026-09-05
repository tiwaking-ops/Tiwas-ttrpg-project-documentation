---
document:
  title: "Claude Playtest Prompt — Review, Revision Instructions, and Playtest Conduct Guide"
  version: "1.0"
  status: "Advisory working document (not canonical). Report to the prompt author with revision instructions and universal conduct guidance. Makes no rulings, assigns no DEC numbers."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
---

# Claude Playtest Prompt — Review, Revision Instructions, and Playtest Conduct Guide

**Purpose:** This is the formal review of `claude-playtest-prompt-version1.md` (Claude Sonnet 5's Ice Troll Combat Playtest prompt), produced from a read-only cross-reference against the live decision register and the Tiwas corpus. It contains (1) revision instructions for the prompt author, (2) universal playtest-conduct guidance that is LLM-agnostic, (3) the required provenance note, (4) a candidate DEC list extracted from the scaffold values the combat will generate, and (5) an explanation of the Frightened Condition as the module's one uncovered subsystem.

**Authority note:** This document is advisory. It proposes no rulings, assigns no DEC numbers, and changes nothing's authority. All authoring/ruling of the playtest and any resulting DEC entries remain Tiwa's (or OpenCode recording against the live register, respectively).

---

## 1. Executive summary

The playtest prompt is fundamentally sound. It correctly:
- Targets the Wound pathway first, per DEC-085 item (6).
- Keeps the two-track separation (attacker Cost/Overflow vs. target Effect) per DEC-006/DEC-007/DEC-085 item (5).
- Uses DEC-052 (HP = 0 → forced incapacitation) as the combat conclusion.
- Correctly scopes scaffold-value authorization to the genuinely open gaps.

One substantive issue requires attention before execution: **the DEC-012 exception for Adventurer-1's two pre-built Tier-2 skills is novel for a PC and is NOT register-backed.** DEC-087 explicitly scopes pre-authored Tier-2 skills to creature/NPC templates and preserves DEC-012's failed-Double origin for player characters. Per Tiwa's ruling (2026-09-04), this exception is **kept as a prompt-level scaffold** — authorized for this test only, logged as such, and **explicitly noted in the final report as non-register-backed for PCs.** It must not be represented as having register authority.

---

## 2. Revision instructions for the prompt author (Claude)

Apply the following to `claude-playtest-prompt-version1.md`:

### 2.1 Fix the DEC-012 / DEC-087 justification
**Current (incorrect):** "This is scaffolding for this playtest only, parallel to how DEC-087 authorized pre-built Tier-2 skills for creature templates specifically."

**Problem:** DEC-087 (`_consolidation/decision-register.md`) scopes its pre-authored Tier-2 authorization to **creature/NPC templates** and explicitly preserves DEC-012's failed-Double origin for **player characters**. Invoking DEC-087 as precedent for a *PC* skill is self-contradictory: it implies the ruling covers PCs when it does not.

**Required change:** Replace the justification with wording that makes the non-register-backed nature explicit:
> "This is scaffolding for this playtest only and is **not backed by any PC-scoped register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates and explicitly preserves DEC-012's failed-Double origin for player-character skill advancement. The DEC-012 exception for Adventurer-1 is a **prompt-level scaffold** under Tiwa's authorization for this test only, is **not register-backed**, and must not be represented as creating new precedent or granting register authority."

### 2.2 Add the execution condition for Attack1/Defence1 construction
Where the prompt currently notes the tie-break on "two highest Body attributes" (all attributes = 50, so tie), lock in which two to use to remove an arbitrary construction detail from the executing LLM. **Per Tiwa, revert to the standard `floor(Cap/2)` Starting Value for Attack1/Defence1 (= 25)** — the exception covers *existence at Tier-2*, not a different starting-value rule. This is already correct in the current prompt; preserve it and do not drift toward the DEC-086 creature full-Cap convention for this PC.

### 2.3 Make the report's final-report structure carry the provenance note (§4)
Insert the provenance-note requirement directly into the "Final report" output specification so it is non-negotiable regardless of which LLM executes.

### 2.4 Keep the Ice Troll stat block as an attached reference
The prompt correctly states the executing LLM "will need that file's content supplied alongside this prompt." This is essential — the v0.2 stat block lives in `investigations/tiwas-gurps-creature-conversion-scratch-ice-troll-blood-man-v0.2-2026-09-03.md` and its numeric values must be supplied verbatim, **not re-derived.** Re-derivation is prohibited (it is already the DEC-085 default baseline; re-deriving invites drift).

### 2.5 Fright Check stop condition — keep explicit
The prompt's example stop condition ("does the Ice Troll's fear aura trigger here" when no Fright subsystem exists) is correct and should be kept verbatim. It is the model example of a "genuine subjective/narrative judgment call no numeric scaffold can resolve" and directly maps to the Frightened gap (§5).

---

## 3. Universal playtest conduct guide (LLM-agnostic)

This guide is written to be executed by **any** LLM as Combat Referee / Simulation Engine. It is independent of the prompt's current author and is intended to produce reproducible, cross-model-comparable results.

### 3.1 Role contract
- Act as **Combat Referee / Simulation Engine**, not a creative GM, not a designer.
- Resolve every roll mechanically and literally against the provided Ruled/Locked corpus.
- **Never** invent a rule to smooth over a gap.
- **Never** make a narrative judgment call silently.
- Where the corpus is silent and no scaffold value is pre-authorized, **stop and flag the human monitor** (Tiwa).

### 3.2 The three things the test produces data on
1. Which Ruled systems function correctly end-to-end in actual play.
2. How long a single combat takes to resolve (real time and round count).
3. Exactly where a human GM's judgment becomes necessary.

### 3.3 Derivation discipline
- Use the **supplied** stat blocks verbatim. Do not re-derive the Ice Troll or the PC.
- All 24 attributes for Adventurer-1 are fixed at **50**; do not randomise.
- Attack1 and Defence1: Cap = floor((A1+A2)/2) = 50; Starting Value = floor(Cap/2) = 25; NPC/creature full-Cap convention (DEC-086) does **not** apply to this PC.

### 3.4 Mandatory scaffold logging
Every scaffold value you invent must be:
- **Clearly flagged** as non-canonical in the live round-by-round log at the moment of invention.
- **Collated** in a single dedicated section of the final report ("Scaffold Values Used") for designer review.
- **Never** assigned a DEC number.
- **Never** claimed to be Ruled/Locked.

### 3.5 Mandatory GM-stop logging
Every genuine GM-required stop must be recorded verbatim in both the live log and the final report ("GM-Required Moments"), each with the reason.

### 3.6 Output format (both outputs required)
1. **Live combat log** — round-by-round, every roll: raw d100, Skill tested, Cost, Overflow if any, Success/Fail, Quality if relevant, Effect selected, Location Index if rolled, Wound/Condition applied, Recovery amount. One-line flag on every scaffold invention and every GM stop.
2. **Final report** — Markdown, opening with the YAML provenance block (§4). Structure: Purpose/Scope · Character & Opponent summary · Round-by-round summary table · Systems Confirmed Working · Systems That Failed/Gapped (with scaffold values collated) · Total real-time and round-count duration · GM-Required Moments (verbatim, with reasons) · Conclusion. No mechanics ruled, promoted, or invented as canon anywhere in the report.

### 3.7 Success criteria
- Combat runs to an actual conclusion (HP = 0 → DEC-052 incapacitation, or explicit abort) without silently skipping or softening any rule.
- Every scaffold value and every GM stop is distinguishable at a glance in both outputs — nothing canonical-looking sneaks in.
- The report is self-contained and precisely sourced so OpenCode can use it cold to identify concrete follow-up DEC candidates.

### 3.8 Constraints
- Never assign a DEC number.
- Never claim Ruled/Locked status for a scaffold value.
- No simplification of the 24-attribute matrix, Core Test 9-step transaction, S-1 Opposed Contest, S-2 Zero-Step, S-3 Effect resolution, S-4 Wound, S-5 Armor, or S-6 Active Defense.
- Do not invent new attributes, skills, Tags, or Conditions beyond what's Ruled or explicitly scaffolded.
- Tables for all stat blocks and roll sequences; no narrative flavor beyond the one-line color needed to log an Effect.

---

## 4. Provenance note (required in the final report's YAML provenance block)

The executing LLM's final report MUST open with this provenance block, with the executing LLM's own name/version substituted:

```yaml
provenance:
  author_llm: {name: "<executing LLM name>", version: "<executing LLM version>"}
  assessor_llm: []
  last_modified_by_llm: {name: "<executing LLM name>", version: "<executing LLM version>"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
```

### 4.1 Special note on the DEC-012 exception (must be stated in the report body)
The final report MUST include, prominently (e.g., under Character description and reiterated in the Conclusion):
> **Provenance of the DEC-012 exception:** the two pre-built Tier-2 skills on Adventurer-1 (Attack1, Defence1) were granted under a **prompt-level scaffold** (Tiwa's authorization, 2026-09-04) for this playtest only. They are **NOT backed by a PC-scoped register ruling.** DEC-087 authorizes pre-authored Tier-2 skills only for creature/NPC templates and preserves DEC-012's failed-Double origin for player-character skill advancement generally. Therefore: this exception is **non-register-backed**, creates **no new precedent**, grants the PC **no canonical authority** from these skills, and must **not** be cited in any future DEC or proposal as evidence that PCs can receive pre-authored Tier-2 skills outside DEC-012.

---

## 5. Candidate DEC list (extracted from scaffold values the combat will generate)

These are the open gaps the playtest is designed to surface. They are **candidates for future design rulings** — none is resolved here, and none may be resolved by the executing LLM or by this document. Each maps to a specific carried-open item in DEC-085 or a known gap.

| # | Candidate gap | Source of the open question | Expected scaffold value produced by combat |
|---|---|---|---|
| C-01 | **Inflict Injury magnitude** — how many target HP `Inflict Injury` (Base-tier) removes | DEC-085 carried-open; DEC-023 defines the Effect but no DEC gives a numeric HP magnitude. Blocks base-tier combat generally (most combat, since Wound requires Tier-2). | A numeric target-HP reduction the referee invents and logs. |
| C-02 | **Active Defense (S-6) mitigation amount** — how much a successful Active Defense reduces a declared Effect | DEC-044–050 rule the S-6 framework (Model B, defender's own Core Test) but no DEC specifies the numeric mitigation. | A numeric mitigation value the referee invents and logs. |
| C-03 | **S-3 Effect magnitudes generally** — numeric values for Condition/Effect tiers beyond those already scaled by Quality | DEC-023.A enumerates gated-tier content; DEC-031 scales magnitude by Effect Quality to a Tier; but concrete per-Effect numbers are not fully specified. | Numeric values for various Condition/Effect applications. |
| C-04 | **Fright Check / Frightened trigger mechanic** — when and how a Frightened Condition is imposed outside a won S-1 Effect | DEC-079 defines `Frightened` as a Condition (source-dependent, −Y to all Skills while source perceivable) but **no DEC defines the trigger** (what test is rolled, against what, under what circumstance a creature imposes it passively). The module invokes Fright Checks (§38, §58) with no Tiwas equivalent. | A GM-required stop (no numeric scaffold can resolve a nonexistent trigger). See §6. |
| C-05 | **Regeneration / Regrowth / healing-magnitude vocabulary** | DEC-088 extended `env:freezing` and the Condition Clause for the Ice Troll's gated DR/Regen presence, but the **healing-magnitude vocabulary itself** (how much HP per unit time a Regeneration trait restores) remains open, per DEC-085's carried-open note. | A numeric heal-per-tick value the referee invents and logs when a Regen tick would apply. |

**Note:** C-04 is qualitatively different — it is a **subsystem absence**, not a magnitude gap, so no numeric scaffold exists for it. It is expected to produce a GM-required stop rather than a logged scaffold.

---

## 6. The Frightened Condition and why it is the module's uncovered subsystem

### 6.1 What Frightened is (DEC-079, alpha vocabulary)
From `_consolidation/decision-register.md` (DEC-079, the 14-Condition alpha vocabulary), the `Frightened` Condition is fully defined **as a Condition**:

> *Frightened:* global; **−Y to all Skills while source remains perceivable**; same-tier values add, higher replaces; ends when source no longer perceivable, by removal Effect, or time; **source-dependent.**

What this means mechanically, exactly as the register specifies:
- **Valence:** negative Condition (imposes a penalty).
- **Scope:** global (affects all Skills, not a single limb/Location).
- **Magnitude:** `Value Z = −Y`, identical to Wound magnitude per DEC-079 (C2) — i.e., `Tier-Y Frightened Value −Y`, scaling with the generating Effect's Quality (hard ceiling, DEC-035.B) and gated to Skill-Tier ≥ 2 production (DEC-041).
- **Application form:** Skill-side penalty only (−Y to all Skills), overlaying Effective Skill. It does **not** modify the natural d100 roll (Invariant 6), does **not** auto-fail, and is **not** an action-denial Condition like Stunned.
- **Stacking:** same-tier values add; higher replaces.
- **Duration/termination:** ends when the source is no longer perceivable, by a removal Effect, or by time. **Source-dependent** — the Condition persists only while its fear source remains perceivable.
- **Distinct identity:** it is a Condition-tier Effect in DEC-023.A's enumeration, distinct from Stunned/Incapacitated (no action denial) and from all HP-loss Effects (no damage; DoT prohibition of DEC-023.A preserved).

### 6.2 What is missing — the trigger mechanic
What the register defines is the **Condition itself**, not the **circumstance that imposes it**. Three specific things are undefined in the corpus:
1. **What qualifies as a fear source** (a creature's passive "aura," proximity, a specific event).
2. **What test, if any, is rolled** to resist or impose it (in GURPS this is a Will-based Fright Check; Tiwas has no such subsystem).
3. **Who/what declares it** — in the won-S-1-Effect pathway, a creature could impose `Frightened` as a declared Condition-tier Effect on a win (that path is mechanical). What is absent is any **passive/aura trigger** outside that normal attack-and-win pathway.

### 6.3 Why this matters
The BToV-Madness source material is explicit Cosmic-Horror flavored and invokes GURPS Fright Checks at **§38** (Blood Man appearance, with a −2 in the -58 variant) and **§58** (corpse discovery). The Ice Troll (Appearance: Hideous) and Blood Man (Appearance: Monstrous) are exactly the kind of creature that, in GURPS terms, carries fear-inducing presence. Per the readiness reports, this is the one subsystem the module cannot approximate with a binary Core Test without a ruling on the trigger — the `Frightened` **Condition** is ready, but the **trigger** is not.

### 6.4 How the playtest handles it (correct behavior)
- **Inside a won S-1 Effect:** the creature may declare `Frightened` as a Condition-tier Effect exactly as it would any other gated-tier Effect. This path is mechanical and playtestable (Skill-Tier ≥ 2 gate satisfied for signature attacks; magnitude by Quality). **No scaffold needed** beyond the standard S-3 magnitude scaffolding (C-03).
- **Outside a won Effect (passive/aura):** there is **no defined trigger**, so this is a **GM-required stop**, exactly as the prompt's example describes. The referee must stop and flag Tiwa rather than invent a fear-trigger mechanic. Any future ruling to formalize this trigger is a candidate DEC (C-04).

### 6.5 Options for Tiwa to consider (not recommendations — genuinely open)
1. **Scope the trigger into the won-Effect pathway only** — treat `Frightened` strictly as a declared Condition-tier Effect on a win, with no passive/aura application. This requires no new mechanic; it simply declines to model GURPS's passive Fright triggers.
2. **Define a passive/aura trigger as a Core Test** (e.g., a Willpower/Composure/Resolve Skill test with S-8 difficulty, per DEC-063–066) — a binary/graded resistance roll on encounter, imposing `Frightened` on failure. This mirrors the readiness reports' favored "binary Core Test + Condition" position but requires a formal ruling.
3. **Model as a source-scoped Condition Clause-style trigger** — extend DEC-088's Condition Clause grammar so a creature Trait can impose `Frightened` while some scene/state Tag (`creature:type_undead`, or a new fear tag) is present. This is architecturally consistent with the read-only, stateless DEC-088 pattern.
4. **Defer** — leave the module's horror beats as GM-flavor, and revisit only if the full adventure is to be playtested.

### 6.6 What the executing LLM must NEVER do
- Must **not** invent a fear-trigger mechanic to keep the story moving.
- Must **not** claim `Frightened` can be imposed outside a won Effect without a ruling.
- Must **not** assign a DEC number or promote anything related to Fright.

---

## 7. What was and was not changed

**Changed by this document:** none in the repository. This is a new advisory investigation artifact in `investigations/`. It proposes prompt revisions, universal conduct guidance, a provenance note, a candidate DEC list, and a Frightened explanation; all are advisory. No register entry, no ruling, no promotion.

**Not changed:** `claude-playtest-prompt-version1.md` (the prompt) remains Claude Sonnet 5's authored working document — stored at repository root, unmodified. The decision register, governance documents, and all other repository material are untouched. No DEC numbers were assigned, and nothing's authority was altered.

**Recommended follow-up:** Tiwa reviews the prompt revision instructions and the candidate DEC list; on authorization, the prompt file may be updated (or superseded by a v2) with the §2 changes; the DEC candidates C-01…C-05 may be progressed through the normal designer-ruling path.

---

## 8. Methodology dispositions from the playtest collation (Tiwa, 2026-09-04)

The different LLM collation reports surfaced two *methodology* items (not game-mechanic candidates). Tiwa classified both as **playtest methodology / audit items — NOT DECs**, so they are tracked here rather than in the decision register.

### 8.1 G-11 — Attack/Defence attribute-pair disclosure (playtest reproducibility / prompt disclosure requirement)

**Tiwa amendment (2026-09-04):** the skill names should be **`AttackX` / `DefenceX`** where **X = the skill tier** of the skill (e.g., `Attack1` / `Defence1` for a Tier-1 skill; `Attack2` / `Defence2` for Tier-2). This makes the tier self-describing in the skill name. This naming applies to the playtest prompt and to any derived documentation (character blocks, reports), and is a reproducibility/disclosure requirement so the executing LLM does not silently choose which attribute pair or tier is in use.

### 8.2 G-12 — Scaffold-formula conflict (playtest methodology audit)

The cross-lineage divergence in scaffold formulas (Lineage A used Margin-based Injury/Defense; Lineage B used flat values) is a **methodology/audit issue**. It is tracked in the playtest methodology audit and **not** encoded as a game rule. It underscores that cross-lineage magnitude figures are not directly comparable and must never be averaged or statistically combined across lineages.

### 8.3 Relationship to the recorded rulings

All other candidates from the collated list (C-01, C-02, C-04/C-10, C-06, C-07, C-08, C-09, SC-04) received Tiwa designer rulings and are recorded as **non-canonical designer rulings** DEC-094…DEC-101 in `_consolidation/decision-register.md` Section B. None promotes anything to Canonical; the 8-step Promotion Rule has not been run.
