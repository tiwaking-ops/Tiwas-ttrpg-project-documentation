---
document:
  title: "Tiwas — Beyond the Vale of Madness (GURPS) → Tiwas TTRPG — Formal Adaptation Report"
  version: "1.0"
  status: "NON-CANONICAL — advisory formal report. Read-only analysis per AGENTS.md; no rulings, no promotion, no status changes. Storage and drafting confer no authority."
provenance:
  author_llm: {name: "Buffy (Codebuff)", version: "unknown / not established"}
  assessor_llm: []
  last_modified_by_llm: {name: "Buffy (Codebuff)", version: "unknown / not established"}
  created_date: "2026-09-17"
  last_modified_date: "2026-09-17"
  identity_established_by: "self-reported"
---

# Tiwas — Beyond the Vale of Madness (GURPS) → Tiwas TTRPG: Formal Adaptation Report

## Provenance note

This report was produced by **Buffy (Codebuff)** on **2026-09-17**. The producing-model
identity stated here is **self-reported** — a claim by the producing model, not an
independently verified signature. The platform does not expose a non-forgeable model
version field to this session; the version is therefore recorded as *unknown / not
established* rather than guessed. This report is NON-CANONICAL and advisory only.
Repetition, chronology, majority view, or report ordering confers no authority on any
Tiwas subsystem.

## 1. Governing rules and method

Formal documentation rules in force for this report:

1. **AGENTS.md** — operating-control rules: status before substance; no authority from
   chronology, repetition, or apparent quality; analysis never resolves authority;
   evidence → ambiguity → consequence → human question; no scope expansion.
2. **governance/authority.md** — the authority hierarchy (canonical/ > roadmap/ >
   proposals/ > investigations/); investigations never self-execute.
3. **governance/status-model.md** — status vocabulary, evidence classes, and the 8-step
   Promotion Rule (the only path from non-canonical to canonical). No item in
   `proposals/` or `investigations/` has completed it.
4. **governance/provenance.md** — mandatory provenance block (above), author/assessor
   distinction, do-not-fabricate rule.
5. **prompts/llm-adaptation-report-author-identity-prompt.md** — the house format
   precedent for BToV-adjacent formal reports (front-matter, provenance note, source
   register, explicit guesses section, governance boundary).

**Standing limitation (flagged, not resolved):** the full text of
`prompts/project-documentation-consolidation-prompt.md` is not present in the
repository (the stored file is a capture summary). Per AGENTS.md §"Unresolved governing
specification", its status remains unresolved; this report does not reconstruct it and
does not rely on it. If any ruling below is needed at promotion time, escalate to the
human.

**Method:** This is an **adaptation-needs analysis, not a conversion**. It reads the
adventure PDF verbatim, maps each adventure requirement onto the current status of the
Tiwas rules, and classifies each dependency by evidence class (per status-model.md):
*mechanical fact* (directly follows from locked rules), *empirical finding* (supported
by stored playtest records), *designer ruling* (exists in the register but non-canonical),
*recommendation*, or *architectural constraint*. Where a dependency falls on a Reserved
system or a Missing system, that is recorded — not resolved.

## 2. Basis and method detail — source boundary and attribution

**Source boundary (attached/consulted sources only):**

| Source | Function in this report |
|---|---|
| `Beyond-the-Vale-of-Madness-GURPS.pdf` (J.C. Connors, v1.2) | The adaptation target: adventure structure, encounters, creatures, treasures, keyword tracking, pregens, advancement awards (primary evidence for every adventure-side figure quoted) |
| `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` | The sole locked ruleset (canonical/systems/README.md §"exactly one locked ruleset"); source of Canonical/Locked and Reserved classifications |
| `_consolidation/decision-register.md` | Designer rulings DEC-041, -076, -077, -077.A, -078, -079, -085, -088, -094, -098, -100, -102, -105, -110, -112, -135, -136, -137, -139, -142/143-draft context |
| `investigations/tiwas-gurps-creature-conversion-scratch-ice-troll-blood-man-v0.2-2026-09-03.md` | The standing working conversion of the adventure's two stat blocks (HP 705 / 650; Tier-2 signature attacks; DEC-077.A workflow) |
| `investigations/tiwas-gurps-creature-conversion-pipeline-gpt-5.6-luna-2026-09-03.md` | The conversion method (24-attribute, overflow model) adopted as working baseline by DEC-085 |
| `investigations/tiwas-ice-troll-itq3-anatomy-diff-evidence-record-2026-09-16.md` | Evidence that the v3–v6 playtest stat block and the L-004 Ice Troll template do not contradict |
| `investigations/tiwas-adapt-vale-of-madness-reports-1-llm-attribution-2026-09-02.md` | The 25-report multi-LLM evaluation corpus (cross-referenced, not reproduced) |
| `governance/*.md`, `prompts/*.md`, `AGENTS.md` | Formal documentation rules in force |

**Attribution discipline:** figures quoted from the adventure PDF are quoted from the
PDF text extraction made for this report (lines cited by §number). Figures quoted from
Tiwas rules are quoted from the locked v1.3 document or the register. Where a stored
advisory document is the only source of a figure (e.g., HP 705), it is labeled as such —
advisory figures remain advisory here.

**Prior-work relationship:** twenty-five independent LLM adaptation reports already
exist (2026-09-02 corpus). This report **cross-references that corpus but does not
reproduce or reconcile it** — producing yet another opinion joined to that set would be
duplicative; instead this report works directly from the PDF and the current rules,
and uses the corpus only to confirm that the same friction points recurred across
independent assessments.

## 3. The adventure, summarized (what is being adapted)

Structure: a 60-paragraph choose-your-path solo adventure (J.C. Connors, v1.2). One
pre-generated character or a 150-point GURPS fantasy character. Play proceeds
paragraph-to-paragraph with keyword tracking (DARKNESS, AMBUSHED, RESCUER) written on
the character sheet. Two mandatory-to-the-climax combat encounters — an **Ice Troll**
(p.4 stat block) in the caves, and a **Blood Man** (p.8 stat block) in the castle —
plus two optional fights (#17 ambush, #38 confrontation). Non-combat resolution uses
GURPS 3d6 skill rolls (Climbing, Stealth, Lockpicking, First Aid, Search, Merchant,
Tracking, Survival, Tactics, Forced Entry, DX/Will/ST/Perception rolls), FP attrition
from cold/exertion, falling/cutting damage, a Fright Check at #38 (and #58 at −2),
treasure acquisition (12-entry table), an NPC rescue subplot (Jrak Kul, RESCUER), and
an end-of-adventure award schedule: 2 characters (+1 for defeating monsters, +1 for
over $500 in loot). Battle maps for both combats are included (pp. 13–14).

## 4. Part 1 — System-by-system adaptation mapping

For each adventure requirement: what the adventure needs, what the current Tiwas rules
provide, and the evidence class of that provision. Classifications cite their source;
none are upgraded by this report.

### 4.1 Solo-play structure and character generation — **READY (mechanical fact)**

The adventure's single-protagonist structure requires no special Tiwas support beyond
a working character. Tiwas generates starting characters by 24-attribute generation
(four 1–100 attribute blocks; the 1–100 range is locked, Canonical §11.2). The
adventure's 150-point equivalence is **not portable** — point-buy is a GURPS concept
with no Tiwas analog — so the two pregenerated GURPS characters (King Coppertongue,
Enfys Loom) must be rebuilt as Tiwas characters via the locked generation method rather
than translated. This is a mechanical fact about what conversion requires, not a ruling
that it must be done a particular way.

### 4.2 Opposed and unopposed task resolution (all skill rolls) — **READY (mechanical fact)**

Every roll in the adventure — Climbing (−3 gargoyle wall; penalized −1/encumbrance
level), Stealth vs. Perception 12 Quick Contest (#44), Lockpicking +2 (#18), First Aid
(#21/#37), Search/Vision (#30, #43), Merchant (#23), Tracking +3 (#27), Survival
(Mountains) (#19), Tactics (#38), Forced Entry (#40), DX/Will/ST/Perception checks, and
the repeated climbing/DX falls — maps onto the locked Core Test. The DEC-100 quartile
mapping (1–25 Legs … 76–100 Head) and DEC-041's tiers are in place. The Core Test is
the locked resolution engine; per DEC-076's dual-mode fork, the solo (non-automated)
mode permits the abbreviated stat-block method for the creatures.

### 4.3 Creature conversion: Ice Troll and Blood Man — **READY (empirical finding + standing ruling)**

This is the adventure requirement the repository has already metabolized. The two stat
blocks (Ice Troll p.4: ST 15, HP 15, DR 2 freezing-only, Regeneration/Regrowth
freezing-only, Icy Claws/Sharktoothed Maw 1d+2 cut; Blood Man p.8: ST 13, HP 15, DR 1,
Claws 1d cut, Blood Seep 1d-2 corrosive/second, Night Vision 6) were converted to
Tiwas working stat blocks under the DEC-077.A conversion workflow (2026-09-02), using
DEC-076 Ruling A's method and DEC-041's individual-template method: HP 705 (Troll) and
650 (Blood Man), 24-attribute generation,Tier-2 signature attacks (required for any creature that must be able to inflict Wounds — DEC-041 requires Skill-Tier ≥ 2 for Location Index generation), overflow model (per the scratch's own citations: DEC-023/DEC-027/DEC-032). DEC-085
adopted the Luna/GPT-5.6 rule-faithful pipeline as the working baseline; four playtest
series (v3–v6) have exercised these conversions empirically. **Evidence class:
empirical finding** — the conversions have been executed and played, not merely
proposed. Outstanding: DEC-077.A keeps each conversion **provisional until Tiwa affirms
it**; the L-004 template for the Ice Troll (full anatomy) awaits the batch-acceptance
ruling (DEC-143 draft, agenda A1/A2).

### 4.4 Damage, injury, and armor — **PARTIAL (mechanical facts + Reserved gap)**

Weapon/attack damage (1d+2 cut, 1d-2 corrosive, falling 2d-2 cr, etc.) maps onto the
Core Test's Inflict Injury outcome and the Wound system. The L-004 family's armor
registrations (Dragon's exception-carving pattern; Giant Spider's six registrations;
DEC-088's Armor Tag on Ice Troll) exist as **ruled non-canonical** content. The gap:
canonical §15 lists **armor, active/passive defense, incapacitation, death, healing,
conditions, wound activation/severity, Outcome Effects, environmental hazards,
equipment, encumbrance** as **Reserved** — outside the locked Core. The adventure's
Blood Seep (per-second corrosive vs. averaged DR) and its fall damage ("only soft
armor protecting") therefore have no canonical armor/deflection math to land on yet.
They land on ruled non-canonical material instead. This is the report's central
structural finding, expanded in §6.

### 4.5 Fatigue and environmental attrition — **PARTIAL (ruled non-canonical; canonical seed exists)**

The adventure's FP economy (−1 FP digging through snow; −2 FP breaking out; collapse at
0) has no direct Tiwas analog. Canonical §15 reserves **environmental hazards** and
**conditions**; the canonical attribute table names **Stamina (bes)** as a Body/
Endurance/Endurance trait but no canonical mechanic consumes it. DEC-135 ruled
repeated-Defense fatigue as a Condition-tier Effect (register), which is the closest
ruled scaffold. Recommendation-class mapping: cold exposure and exertion map to
Condition-tier effects (e.g., Exhausted/Cold conditions under DEC-079's format), with
magnitude tracked per DEC-079's `Tier-Y Condition Value Z` record format. This is
presented as a mapping option, not a ruling.

### 4.6 Fear checks — **READY as ruled non-canonical (designer ruling exists)**

The adventure's two Fright Checks (#38 Fright Check p. B360; #58 at −2) map to the
ruled **Frightened Condition**: DEC-094 (C-04/G-04) ruled the passive/aura Frightened
trigger as a scene-state/Condition-Clause trigger with C-10 magnitude folding; DEC-079
provides the Condition record format. Evidence class: designer ruling (non-canonical).
A solo Fright Check is a self-triggered scene-state check rather than an aura trigger —
the mapping is natural but is itself an unruled extension of DEC-094's trigger
taxonomy; flagged, not resolved.

### 4.7 Treasure, wealth, and reward — **MISSING (no canonical or ruled system)**

The 12-entry treasure table, Winterhaven merchant sale, the $500 threshold, and the
RESCUER reward ($500 silver talents + Martyrs of War induction) have **no Tiwas
currency, wealth, or equipment-pricing system** to map onto — canonical §15 reserves
equipment; the register contains no currency ruling. The 25-report corpus flagged the
same gap repeatedly. Options exist in design-space (abstract wealth Condition, item
Tier ratings, equipment-tier Effect integration per DEC-081.A R1) but none is ruled.
The adventure is playable without pricing (treat treasure as narrative items with a
loot-count for the award schedule), but the award schedule's $-thresholds are then
GM-fiatted. Recorded as Missing; not resolved.

### 4.8 Advancement awards — **READY (mechanical fact)**

The end-of-adventure award (2 characters + up to 2 bonus) maps to the locked General
XP advancement rules (Canonical §11: General XP raises Attributes/Skills at current-
value cost, no partial advancement; GM/quest/adventure awards are explicitly a listed
XP source). The adventure's per-adventure bonus structure is a straightforward GM-award
discretionary call under that rule. Above-Cap advancement (§11.1) and the 100-Fumble
ceiling (§11.2) are already locked and require no adaptation.

### 4.9 Magic (Enfys Loom's spell list) — **OUT OF SCOPE for canonical adaptation (Reserved)**

The advanced pregen (Enfys Loom, Magery 3, ~20 GURPS spells: Fireball, Flame Jet,
Dark Vision, etc.) cannot be canonically converted: canonical §15 reserves
**magic/special-ability implementation** outright, and DEC-041(2)/(5)'s
individual-template method governs content authoring (a "mage" template would be a
full L-004-style authoring act, not a conversion). The two preregistered precedent
paths: (a) DEC-077.A conversion workflow does **not** cover spell conversion (scope:
GURPS *creatures*), so Enfys's spells would need either a new authoring authorization
or a magic-system ruling first; (b) the warrior pregen (King Coppertongue) is
convertible today under the existing workflow. Flagged for the human: choosing to
adapt the mage pregen first requires deciding the magic question, which is Reserved
and not resolvable by this report.

### 4.10 Battle maps and tactical combat — **PARTIAL (mapped; positioning rules Reserved)**

Both climactic battles offer tactical-map play (Troll Caves, castle ambush map). The
ruled melee-exchange algorithm (DEC-105: one S-1 opposed contest; both always roll)
and the ruled movement system (DEC-133 abstract bands; DEC-138 uniform Tier-based
penalties) support **abstract** tactical play without a map. Hex-by-hex positioning,
facing, and reach (the adventure's Reach C, ambush start-position rules, "on the blood
stained snow hex") have no canonical or ruled Tiwas implementation — Reserved
(§15: GM procedure). Practical adaptation: run both fights under DEC-105/DEC-133
abstract exchange rules; the adventure's start-position and ambush keywords map to
scene-state conditions (DEC-094's scene-state trigger pattern).

## 5. Part 2 — Named adaptation dependencies (adventure → Tiwas)

| ID | Adventure requirement | Tiwas provision | Status | Evidence class |
|---|---|---|---|---|
| N1 | Solo CYOA structure | None needed beyond character + Core Test | Ready | Mechanical fact |
| N2 | Skill/task rolls (§4.2 list) | Core Test (locked); DEC-100/DEC-041 tiers | Ready | Mechanical fact |
| N3 | Ice Troll + Blood Man stat blocks | DEC-077.A conversions (HP 705/650); L-004 family pending DEC-143 | Ready (provisional) | Empirical finding + standing ruling |
| N4 | Damage/injury incl. Blood Seep, falls | Core Inflict Injury; Wounds; **armor Reserved** | Partial | Mechanical fact + Reserved gap |
| N5 | FP attrition (cold/digging) | Stamina exists; DEC-135/DEC-079 scaffolds; no canonical hazard rule | Partial | Ruled scaffold, no canonical mechanic |
| N6 | Fright Checks ×2 | DEC-094 Frightened Condition + DEC-079 format | Ready (non-canon) | Designer ruling |
| N7 | Treasure table + $ thresholds | No currency/wealth system (Missing) | Missing | — |
| N8 | 2–4 character award schedule | General XP; GM awards listed as XP source | Ready | Mechanical fact |
| N9 | Enfys Loom spell list | Magic Reserved; DEC-077.A scope excludes spells | Out of scope | Reserved |
| N10 | Battle-map positioning, Reach, ambush hexes | DEC-105/133/138 abstract combat; positioning Reserved | Partial | Mechanical fact + Reserved gap |
| N11 | Keyword tracking (DARKNESS/AMBUSHED/RESCUER) | DEC-094 scene-state trigger pattern (natural fit) | Ready (non-canon) | Designer ruling |
| N12 | NPC rescue subplot (Jrak Kul) | DEC-076 abbreviated stat-block mode for NPCs | Ready | Designer ruling |

## 6. Part 3 — Central structural finding (isolated, but framing)

Every one of the adventure's **combat-critical** dependencies (N3, N4, N5, N10) resolves
today only through **ruled non-canonical** material — DEC-076/077.A/078/079/085/088/
094/105/110/135 conversions, conditions, and armor registrations. The locked Core
(carried by this report's N1, N2, N8) supplies resolution economy, characters,
advancement, and tiers, but canonical §15 reserves armor, defense, injury severity,
hazards, and conditions. An adaptation "succeeds" empirically (four playtest series
ran on the ruled stack) while remaining, by the repository's own status model,
**entirely dependent on non-canonical scaffolding**. Per status-model.md, no amount of
successful playtesting promotes any of it — only the 8-step Promotion Rule does. The
consequence is stated, not decided: the BToV playtest is simultaneously the best-evidenced
and the least-locked subsystem family in the repository.

## 7. Guesses I had to make

1. **"Adapt" scope** — read as "produce a formal adaptation-needs analysis with a
   system-by-system mapping," not "produce a converted adventure document." Basis: the
   25-report corpus precedent (which defined adaptation reports as assessments) and
   DEC-077.A (which reserves actual conversion to a specific authorized workflow with
   per-conversion Tiwa rulings). Confidence: high. A full converted adventure is a
   different deliverable and would itself be advisory authoring under DEC-077's bar.
2. **"Formal project documentation report rules"** — read as AGENTS.md + the governance
   triad + the BToV-report format precedent, because the named consolidation prompt's
   full text is absent and its status is unresolved per AGENTS.md. Confidence: high.
3. **Treasure-value threshold ($500)** — retained as narrative text, not converted to a
   Tiwas quantity, because no currency system exists to convert into. Confidence: high.
4. **FP → Condition mapping (§4.5)** — presented as recommendation-class, not the only
   possible mapping. Basis: DEC-079 format + DEC-135 precedent; alternatives exist.
   Confidence: medium.
5. **Solo Fright Check as self-triggered scene-state check** — natural reading of
   DEC-094's taxonomy; not an existing ruled case. Confidence: medium.6. **King Coppertongue's name** — verified as rendering "King Coppertongue" consistently in two independent text extractions of p.13; retained as a flag because the pregen blocks sit in a stylized multi-column layout and the rendered page was not independently inspected.
7. **Report placement** — `investigations/` per governance/authority.md §4
   (evidentiary/analytical work product; never self-executing). Confidence: high.

## 8. Governance and authority boundary

This report does **not**: promote, demote, supersede, or alter the status of any
document; convert repeated LLM agreement or successful playtesting into a designer
ruling; resolve any Reserved system; authorize any conversion or authoring act; treat
the adventure PDF as authority over Tiwas mechanics; infer authority from chronology,
majority, ordering, or apparent quality; or fabricate missing mechanics, figures, or
provenance. All classifications carry exactly the status their sources carry. Nothing
here affects the Canonical rules; the 25-report corpus is cross-referenced, not
reproduced; and the standing conversion workflow (DEC-077.A) remains the only
authorized path by which any creature conversion becomes working playtest material —
pending, as always, Tiwa's per-conversion ruling.

## 9. Human questions this report surfaces (not answers)

Per AGENTS.md's escalation workflow, the following are the decision points this analysis
reaches and stops at — each requires Tiwa's direction and none is resolved here:

1. **Armor/defense/hazard canonization priority** — the combat-critical Reserved set
   (§4.4, N4/N5) is the single largest readiness gap; ruling whether promotion of the
   existing ruled stack precedes the next BToV playtest series is a sequencing decision
   above this report's authority.
2. **Enfys Loom / magic** — adapting the mage pregen requires either a magic-system
   ruling or an explicit expansion of DEC-077.A's conversion scope to spells (§4.9, N9).
3. **Currency/wealth** — whether the BToV treasure/award economy waits on a currency
   ruling or plays narrative-only (§4.7, N7).
4. **DEC-077.A affirmation backlog** — the four playtest series' conversions remain
   provisional until individually affirmed; whether affirmation happens per-creature at
   the next ruling session (cf. the DEC-143 agenda) is the human's call (§4.3, N3).

---

*End of NON-CANONICAL advisory adaptation report.*
