---
document:
  title: "Investigative Report — System Readiness for BToV-Madness Template-Creature vs. Random-PC Combat Testing"
  version: "1.0"
  status: "Advisory working document (not canonical). Investigative report only — makes no rulings, assigns no DEC numbers."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-04"
  last_modified_date: "2026-09-04"
---

# Investigative Report: System Readiness for Template-Creature vs. Random-PC Combat Testing

**Scope:** Determine whether the currently Ruled/Locked corpus is sufficient to run a live combat encounter between a randomly generated PC and a DEC-077.A template creature (Ice Troll or Blood Man), and enumerate every gap that would stop such a test cold.

**Method:** Cross-checked against `Tiwas-Alpha-Playtest-Corpus-2026-09-01.md` (Parts A–D) and `Tiwas-Task-Scoped-Snapshot-2026-09-02.md` (§4–§5) as the two most recent available snapshots. No mechanic is asserted, invented, or filled in below. Where the corpus is silent, the gap is flagged and left open per standing project discipline. This document proposes no rulings; all items require Tiwa's decision, and any resulting DEC assignment is OpenCode's responsibility against the live register.

---

## 1. Combat-Test Pipeline — What a Single Attack Round Requires

| Step | System | Status |
|---|---|---|
| 1 | Random PC generation (24-attribute matrix, DEC-003) | **Ruled / Locked** |
| 2 | Derived statistics (HP/MP/PE/Speed/Regen, DEC-004) | **Ruled / Locked** |
| 3 | Skill Cap / Starting Value (DEC-005) | **Ruled / Locked** |
| 4 | Creature stat-block generation (DEC-076 dual-mode; DEC-077/DEC-077.A conversion path) | **Ruled (architecture); creature instances provisional — see §4** |
| 5 | Core Test Transaction, 9-step (DEC-006) | **Ruled / Locked** |
| 6 | Cost / Overflow (DEC-007, DEC-007.A) | **Ruled / Locked** |
| 7 | S-1 Opposed Contest (attack roll) (DEC-013) | **Ruled / Locked** |
| 8 | Quality → Effect-tier gate (DEC-031, DEC-035.B) | **Ruled** |
| 9 | S-3 Effect selection & auto-apply (DEC-023, DEC-023.A, DEC-024, DEC-027) | **Ruled — content enumerated; magnitude gap, see §2.1** |
| 10 | S-2 Zero-Step Location Index (DEC-014, DEC-037, DEC-040) | **Ruled — granularity assignments directional, not locked (§3.1)** |
| 11 | S-4 Wound application (DEC-032–DEC-036, DEC-041, DEC-035.A/B) | **Ruled** |
| 12 | S-5 Armor check (DEC-058–DEC-062) | **Ruled** |
| 13 | S-6 Active Defense mitigation (DEC-044–DEC-050) | **Ruled** |
| 14 | S-7 Incapacitation / Death check (DEC-052–DEC-057) | **Ruled** |
| 15 | Recovery (DEC-008) | **Ruled / Locked** |
| 16 | Conditions vocabulary (Frightened, Stunned, etc.) (DEC-079) | **Ruled — vocabulary defined; some trigger mechanics absent, see §2.2** |
| 17 | Tags vocabulary (DEC-080) | **Ruled — alpha list defined; coverage gap, see §2.4** |
| 18 | Difficulty modifiers, if used (DEC-063–DEC-066) | **Ruled** |
| 19 | Post-combat healing (S-11) (DEC-071–DEC-074) | **Ruled** |

**Read of this table:** every *structural* system a combat round passes through is Ruled. The blocking gaps are not architectural — they are missing *content/values* inside otherwise-Ruled slots. §2 ranks these by how hard they block the test.

---

## 2. Blocking Gaps — Ranked by Severity

### 2.1 Inflict Injury magnitude formula — **CRITICAL, universal blocker**

No formula exists anywhere in the corpus for how much HP damage the base-tier **Inflict Injury** Effect (DEC-023.A) inflicts when selected as the Track B outcome of a won S-1 contest. This is distinct from Overflow (Track A), which is already fully defined (Cost − Remaining Resource → HP, DEC-007).

- Explicitly logged as open in DEC-085: *"Open: target-HP `Inflict Injury` magnitude."*
- This is **not creature-specific**. It blocks *every* combat exchange in the game, PC-vs-PC, PC-vs-creature, or otherwise, wherever the winner selects Inflict Injury as their Effect.
- Without it, Track B damage cannot be resolved at all; only Overflow damage (Track A) is currently computable.

**Table-readiness impact:** No combat round in this game — template-creature or otherwise — can currently resolve Track B damage. This is the single highest-priority gap for any combat test.

### 2.2 Fright / fear-reaction subsystem — **Open, likely required for these specific creatures**

No Tiwas equivalent of a GURPS Fright Check exists. "Frightened" is a defined Condition (DEC-079, part of the 14-Condition alpha vocabulary) — but the *trigger mechanic* (what test is rolled, against what, under what circumstance a creature imposes it outside of a won S-1 Effect) is not defined. The BToV-Madness source material is explicitly Cosmic-Horror-flavored; Ice Troll and Blood Man are plausible fear-inducing statline sources in GURPS terms.

**Table-readiness impact:** Combat itself does not strictly require this (Frightened can still be imposed as a normal S-3 Condition-tier Effect on a win). It matters if either creature's GURPS block includes a passive/aura fear trait outside the normal attack-and-win pathway — that specific trigger has no Tiwas mechanism yet.

### 2.3 Regeneration / Regrowth / Injury Tolerance vocabulary — **Partially open**

DEC-088 supplies the *binding grammar* (Conditional-Trait Binding: `Active only while [env:X] is present`) and the `env:freezing` Tag, which lets a creature's Regeneration/Regrowth/DR be gated on an environmental state. It does **not** define what Regeneration/Regrowth/Injury Tolerance *mechanically do* once active — no rate of Wound-tier reduction or HP restoration per interval, no interaction rule with the DEC-035.A Wound-tier/healing-gate framework, no defined relationship to S-11 Extended-Test healing.

**Table-readiness impact:** The Ice Troll's signature trait (troll regeneration) has a trigger condition (DEC-088) but no resolved mechanical payload. A combat test involving the Ice Troll's regeneration cannot currently be resolved past "the trait is active."

### 2.4 Night Vision / darkness-negation Tag — **Open**

DEC-080's 34-tag alpha vocabulary includes `env:darkness` (a scene-state Tag) but no counter-Tag (e.g., a creature-side "ignores darkness penalties" equivalent to GURPS Night Vision/Dark Vision). Neither the Environment (6) nor Creature (6) namespace sub-lists in DEC-080 contain one.

**Table-readiness impact:** Relevant only if the darkness-heavy BToV-Madness scenario is used and either creature has a GURPS Dark Vision/Night Vision trait — currently no Tag exists to encode it, and no penalty-negation mechanic exists to bind it to.

### 2.5 Untrained-fallback (skill/attribute default) rule — **Open, general blocker for random PCs specifically**

No rule defines what happens when a randomly generated PC attempts an action for which they have no relevant Skill at all (Skill does not exist / was never rolled up from a Tier-1 attribute into a usable Skill entry). Flagged generally as a missing subsystem, not scoped to combat, but a randomly generated PC — by definition not curated by a GM to have "sensible" starting skills — is exactly the case most likely to hit this gap in a combat test (e.g., no unarmed-combat-lineage Skill at all).

**Table-readiness impact:** Any random PC lacking an applicable combat Skill cannot currently take that action under a defined rule; GM-fiat substitution would be undocumented improvisation, not a Ruled mechanic.

---

## 3. Non-Blocking but Unresolved — Present During Testing, Won't Stop It

### 3.1 S-2 anatomical mapping granularity (DEC-041)
Tier-1 coarse-zone ranges and Tier-2 subdivision-to-granularity assignments are **directional, not locked** — usable for a test, but numeric zone weightings may shift after playtest feedback. Not a blocker; a known instability.

### 3.2 Track A / Track B mutual exclusivity
Per prior project learning: it is **not confirmed** whether Track A (Overflow) and Track B (Effect-selected Injury/Wound) are mutually exclusive on a single hit, or can compound as DEC-034 implies ("both can apply from one hit, sequentially"). DEC-034 is Ruled that both *can* apply — but the compounding relationship is worth an explicit sanity check before treating it as settled for testing purposes, since it directly affects total damage output per successful attack against a creature.

### 3.3 S-3 Position-tier Effect magnitudes
DEC-023.A enumerates Position-tier Effect *names* (Forced Movement, Knock Prone, Seize/Deny Ground, Pin/Hold Position, Open/Close Lane) but per the §5.5 dependency note, Position-tier Effect *magnitudes* remain open. Not required for a baseline damage-focused combat test; matters if positioning-heavy tactics are exercised.

### 3.4 Hazards formalization (Proposals §14)
Only `env:hazard_physical` / `env:hazard_systemic` Tags exist (DEC-080); full hazard formalization is not complete. Relevant if the Ice Troll's cold-environment context is treated as an active battlefield hazard rather than a passive Trait-gate condition.

---

## 4. Creature-Specific Readiness — Ice Troll & Blood Man

| Item | Status |
|---|---|
| DEC-077.A conversion authorization | **Ruled** — advisory-model GURPS→Tiwas conversion permitted for BToV-Madness scope only |
| Valid conversion targets | Only Ice Troll and Blood Man have full GURPS stat blocks in the source PDF (scope-locked; Goblin/Dragon reclassified new-content under DEC-084, out of conversion scope) |
| Working baseline method | **Ruled (DEC-085)** — GPT-5.6 Luna baseline adopted: derived stats via DEC-004/005, no GURPS dice/Dodge/Parry/DR numbers, Tier-2 signature attacks, attack roll = attacker resource cost not target damage |
| Blood Man "Blood Seep" DoT conflict | **Resolved (DEC-083)** — single-application Effect on grapple win, no ongoing DoT |
| Starting Skill Fork A/B tension | **Resolved (DEC-086)** — signature attack skills start at full Cap ("veteran"); non-signature skills use standard `floor(Cap/2)` |
| Pre-authored Tier-2 skill / DEC-012 origin tension | **Resolved (DEC-087)** — creature templates may pre-author ready-made Tier-2 skills; DEC-012's failed-Double origin rule applies only to PC advancement |
| Conditional/environmental Armor & Trait Tags | **Resolved (DEC-088)** — Conditional-Trait Binding grammar + new `env:freezing` Tag; enables Ice Troll's Regeneration/Regrowth/DR to be environment-gated |
| Overall stat-block status | **Provisional** — each conversion item is individually "Ruled" only insofar as it resolves a *governance flag*; the v0.2 stat-block document itself remains provisional/unaffirmed per DEC-077.A until Tiwa formally confirms the full document (or specific entries in it) against the live register |

**Net effect:** 4 of the original 8 flagged conversion issues (Blood Seep, Fork A/B Starting Skill, DEC-012 origin tension, conditional Armor Tags) are now closed by DEC-083/086/087/088. The remaining 4 (Inflict Injury magnitude, Fright subsystem, Regeneration/Regrowth mechanical payload, Night Vision Tag) map directly onto §2.1–§2.4 above and are **not creature-conversion-specific** — they are corpus-wide gaps the creature work exposed.

---

## 5. Summary Table — What Must Close Before a Combat Test Is Fully Table-Ready

| Priority | Gap | Blocks |
|---|---|---|
| 1 | Inflict Injury magnitude formula | All Track B damage, any combat, any creature |
| 2 | Untrained-fallback default rule | Random PCs lacking a relevant combat Skill |
| 3 | Regeneration/Regrowth mechanical payload | Ice Troll's signature trait once triggered |
| 4 | Fright/fear-reaction subsystem | Any passive/aura fear trait outside a won S-1 Effect |
| 5 | Night Vision / darkness-negation Tag | Only if darkness-heavy scenario + relevant creature trait is used |
| — | Formal Tiwa affirmation of the v0.2 stat-block document | Treating Ice Troll/Blood Man numbers as more than provisional |

Items 3.1–3.4 (anatomical granularity, Track A/B compounding, Position-tier magnitudes, Hazards) do not block a test but should be logged as known-unstable during any session using them.

---

## 6. Options for Sequencing (presented for Tiwa's decision — not a recommendation)

- **Option A — Minimal unblock:** Rule only on Inflict Injury magnitude (§2.1) and run a stripped-down test (no Regeneration trigger, no fear content, well-lit scenario) using PCs with GM-assigned combat Skills to sidestep the untrained-fallback gap.
- **Option B — Full creature fidelity:** Rule on all of §2.1–§2.4 plus formally affirm the v0.2 stat-block document before testing, so the Ice Troll's signature Regeneration and any fear content can actually be exercised.
- **Option C — Split test:** Run Blood Man first (no Regeneration dependency, Blood Seep already resolved) while §2.3/§2.4 remain open, and hold Ice Troll for a second pass once Regeneration's mechanical payload is ruled.

No option above is a ruling; each is presented with its trade-off for Tiwa to select or reject.

---

## 7. Sources

- `Tiwas-Alpha-Playtest-Corpus-2026-09-01.md` — Parts A (D1 Locked Core), B (Ruled non-canonical subsystems S-1–S-11), C (not-table-ready items), D (playtest template)
- `Tiwas-Task-Scoped-Snapshot-2026-09-02.md` — §4 (full decision register DEC-001–DEC-088), §5 (open design threads, incl. §5.4 S-12 creature content)
- Prior-session working knowledge: BToV-Madness v0.2 creature conversion document and its 8 originally flagged governance items

**Governance note:** This report identifies gaps and presents options only. No DEC numbers are assigned herein — DEC assignment against the live register is OpenCode's responsibility following Tiwa's ruling on any of the items above.
