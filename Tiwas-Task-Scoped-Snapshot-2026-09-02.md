# Tiwas-TTRPG — Task-Scoped Consolidated Snapshot for Advisory Session (2026-09-03)

---
document:
  title: "Task-Scoped Consolidated Snapshot — Advisory Design Session"
  version: "1.0"
  status: "Dated task-scoped working snapshot (NOT the authoritative corpus; NOT a standing merge artifact)"
  scope: "Single decision-making session. Consumed cold by an advisory design assistant with no repo access. Curated per task; superseded by the live repository at all times."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-02"
  last_modified_date: "2026-09-03"
---

## Standing-prohibition overrule (one-line log entry)

Tiwa has **explicitly and consciously** overridden the standing "do not create another single merged file" prohibition (`sources/incoming/opencode-handoff-report.md` §6), **for this one working session only.** This snapshot is a **dated, task-scoped exception** — NOT a reinstatement of `TTTRPG-merge-v2.md` as a standing artifact. Future agents must NOT assume the prohibition is lifted generally.

---

# 1. Purpose and Usage

You are reading this **cold** at the start of a decision-making work session, with no prior memory and no repository access. Tiwa is moving away from giving advisory LLMs broad/standing corpus access (GitHub Project integration, periodically-regenerated full merge file) because both produced stale, bloated, or unverifiable context, and because standing access let contamination from other LLMs' unrelated-game assumptions go unchallenged.

**How this works:** Tiwa will relay to you, separately, the specific open design decisions to advise on. You will give advisory opinions. Tiwa will verify them with OpenCode (live repo access) before anything is recorded.

This snapshot gives you:
1. Every **currently Open** decision in the register, each with its full upstream **Ruled/Locked dependency chain**.
2. The **governance framework** you need to interpret status vocabulary, authority, and provenance correctly.
3. The **current formal-reporting/provenance standard** for any document you produce this session — sourced **verbatim**, not reconstructed.

**This file is NOT the authoritative corpus.** It is a curated, dated snapshot. Anything downstream must treat the live repository as ground truth. Flag any discrepancy you cannot resolve from this file rather than guessing.

### Constraints binding your advice

- You may **inspect, compare, explain, identify contradictions, present evidence and possible interpretations, and recommend**.
- You may **not** resolve any Open decision, promote anything to Canonical, or reclassify any document — authority changes only through the project's formal 8-step Promotion Rule (§2.6) and a human ruling.
- Evidence is recorded with scope and limitations (evidence-class discipline, §2.4). An empirical finding is not a designer ruling; a design direction is not a rule; a proposal is not canonical merely because it is detailed.
- Hash-indexed / raw evidence files are **pointer-referenced, not reproduced inline** (§5). Do not treat them as rules; do not treat a pointer as a copy of the content.

---

# 2. Governance Framework

## 2.1 Authority hierarchy (verbatim from `governance/authority.md`)

```
CANONICAL RULES  (canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md = "D1")
      ↓
PROPOSALS / WIP  (proposals/tiwas-proposals-wip-and-design-direction-v1.4.3.md = "D3")
      ↓
IMPLEMENTATION ROADMAP  (roadmap/tiwas-implementation-roadmap-and-project-governance-v1.4.3.md = "D2")
```

- **D1** is the sole source of locked game mechanics. Per its own §0.1, D3 and D2 "cannot override" this document.
- **D3** is "Non-Canonical Design Repository... Design exploration only." Contains real designer rulings (see register §B, §D) but those rule *candidate, non-canonical* material, not the Canonical ruleset, until the 8-step Promotion Rule is completed.
- **D2** explicitly disclaims rule authority ("Rule Authority: None — this document does not create game mechanics"). Governs sequencing, dependencies, simulation gates, regression requirements, LLM/process rules.
- **`investigations/`** (D4/D5 evidence and analysis) is **never self-executing** — require designer/human ruling before anything they contain affects even the non-canonical Proposals/WIP layer, and never claim any effect on Canonical Rules.

No document in the corpus attempts to claim authority over another in a way that contradicts this hierarchy (checked: `_consolidation/conflict-register.md`).

## 2.2 Status vocabulary (verbatim from `governance/status-model.md`)

**D1's own header statuses:**
- **Canonical / Locked** — authoritative, current, must not be contradicted by downstream design/implementation.
- **Reserved** — a known required subsystem with no settled implementation yet.
- **Historical / Superseded** — retained for understanding, no longer current.

**D3 §0 expanded vocabulary (none of these is a locked rule):**

| Status | Meaning |
|---|---|
| Proposed | A candidate rule under active consideration |
| WIP | Currently being developed or reviewed |
| Experimental | Tested/invented for exploration but explicitly excluded from the ruleset |
| Design Direction | An architectural/philosophical preference, not necessarily a mechanic |
| Reserved | Known required subsystem with no settled implementation |
| Superseded | Historical material retained for understanding but no longer current |

**None of Proposed / WIP / Experimental / Design Direction / Reserved / an "observation" is a locked rule (D3 §0 explicit instruction).**

## 2.3 Status lifecycle (D2 §23.1)

```
Idea → Proposal → WIP → Independent Review → Simulation/Analysis → Designer Ruling → Accepted → Locked/Canonical
```

An item may return to WIP if evidence exposes a substantive problem.

## 2.4 Evidence classes (verbatim from `governance/status-model.md`)

- **Mechanical fact** — directly follows from existing locked rules.
- **Empirical finding** — supported by simulation, playtesting, or other explicit evidence (e.g., the E9 usability playtest, the Named-Outcome 21/21 trial).
- **Designer ruling** — a deliberate choice not mathematically forced by the system.
- **Recommendation** — a proposed preference not yet accepted.
- **Architectural constraint** — governs how systems interact, not what a mechanic numerically does.

An empirical finding does not itself establish a designer ruling. An architectural constraint does not establish a numerical mechanic. This project's source material is unusually careful about labeling which evidence class a given statement belongs to (see e.g. D1 §14.5 vs §14.6; D3 §2.6 vs §2.8) — that discipline should be preserved in all future additions.

## 2.5 Promotion Rule — the only path from non-canonical to canonical (D3 §21 / REQ-021)

1. The design question is explicitly identified.
2. Competing alternatives have been considered where appropriate.
3. Relevant simulation/analysis has been completed.
4. The human designer has accepted the ruling.
5. The mechanic is documented as a formal rule.
6. The Canonical Rules & Changelog document is updated.
7. The former proposal is marked Superseded or Locked in its source document.
8. Implementation documentation is updated.

**No item currently in `proposals/` or `investigations/` has completed this process.** A detailed proposal is not a rule merely because it is detailed (D3 §21).

## 2.6 LLM Governance Rules (D2 §24 — binding on any LLM working in this repository)

1. Treat Canonical Rules as authoritative.
2. Treat Proposals/WIP as non-canonical.
3. Treat Roadmap recommendations as implementation guidance.
4. Never promote a proposal because it appears repeatedly in documentation.
5. Never infer a numerical threshold from an example unless explicitly locked.
6. Never silently resolve an open designer fork.
7. Identify contradictions between current and historical documents.
8. Prefer the current locked ruling over superseded source wording.
9. Preserve the distinction between empirical evidence and designer judgement.
10. State clearly when an answer depends on a proposal rather than a Canonical rule.
11. Never create a parallel Core resolution engine merely to implement a subsystem.
12. Never create a new primary resource or progression currency without explicit designer approval.
13. Treat an interface prototype as non-canonical unless a formal ruling says otherwise.
14. When a subsystem is locked, update the Canonical document and its changelog.
15. When a proposal is superseded, retain its historical significance but mark it Superseded.
16. If new evidence materially challenges a locked rule, recommend reopening it rather than silently changing it.

---

# 3. Formal Reporting / Provenance Standard

**Any document produced by an LLM during this session MUST conform to this standard on first attempt.**

## 3.1 Mandatory metadata block (verbatim from `governance/provenance.md`)

Every document created by an LLM in this repository must open with a metadata block identifying `author_llm`, `assessor_llm`, and `last_modified_by_llm` (each with `name` and `version`), plus `created_date` and `last_modified_date`. Use `unknown` or `not established` rather than inventing a value. `assessor_llm` may be a **list** when more than one assessment pass has been performed; each entry represents one assessment, earliest first.

**YAML schema:**

```yaml
---
document:
  title: "Document Title"
  version: "1.0"
  status: "Status string (use the project's own status vocabulary)"
provenance:
  author_llm: {name: "Model Name", version: "model-id"}
  assessor_llm:
    - {name: "Model Name", version: "model-id"}
  last_modified_by_llm: {name: "Model Name", version: "model-id"}
  created_date: "YYYY-MM-DD"
  last_modified_date: "YYYY-MM-DD"
---
```

## 3.2 Role distinction (verbatim from `governance/provenance.md`)

- **author_llm** — the original creator. Never overwritten by later editors, even if they substantially rewrite the document.
- **assessor_llm** — reviews for factual/documentary consistency, canonical-status accuracy, provenance, or structure. An assessment is not a human decision and does not confer authority. Where an additional independent assessment is later performed, the independent assessor is **appended** to this field as another entry — the original assessor record is preserved, not overwritten.
- **last_modified_by_llm** — the most recent substantive editor. Updated on material changes; formatting-only changes may be handled per future project policy.

## 3.3 Provenance template for documents produced this session

For an advisory model producing a document during this session, the metadata block would typically look like:

```yaml
---
document:
  title: "Advisory Session [Topic] Report"
  version: "1.0"
  status: "Advisory working document (not canonical)"
provenance:
  author_llm: {name: "[Your Model Name]", version: "[your-model-id]"}
  assessor_llm: []
  last_modified_by_llm: {name: "[Your Model Name]", version: "[your-model-id]"}
  created_date: "2026-09-02"
  last_modified_date: "2026-09-02"
---
```

Set `assessor_llm` to `[]` if no independent second-model assessment has been performed. If one is performed later, append it as a list entry (do not overwrite the author).

## 3.4 Decision register column structure (verbatim from `_consolidation/decision-register.md`)

The live register uses this exact column structure:

| Column | Content |
|---|---|
| **ID** | DEC-NNN (designer rulings) or OPEN-NNN (explicitly unresolved) |
| **Subject** | Short description of the decision/question |
| **Decision / State** | The ruling text, or "Unresolved" with what the corpus says |
| **Evidence (source)** | Source document reference(s) — path + section, or in-session chat date |
| **Authority** | Evidence class + source: "Non-canonical designer ruling", "Canonical / Locked", "Architectural constraint (assessment)", etc. |
| **Status** | "Current", "Ruled", "Closed via DEC-XXX", "Inert / dormant", etc. |

**Column mapping to evidence classes:**
- "Canonical / Locked" = Mechanical fact from D1
- "Non-canonical designer ruling" = Designer ruling on candidate material
- "Architectural constraint (assessment)" = Architectural constraint assessment (not a numeric mechanic)

---

# 4. Decision Register — Full Current State

All items from `_consolidation/decision-register.md` as of 2026-09-03. **Every OPEN item (OPEN-001 through OPEN-010) is now closed.** What remains are open design *threads* (content-enumeration, implementation-layer details) that survive the fork-level rulings — see §5.

## 4.A. Canonical decisions (DEC-001 through DEC-016)

These are locked game mechanics from D1. Status: **Current**. No advisory session may override these.

| ID | Subject | Decision | Evidence | Authority | Status |
|---|---|---|---|---|---|
| DEC-001 | d100 core mechanic | Roll-under resolution on 1–100; `00` = 100; 100 always fails and always qualifies as a failed Double | D1 §2.1–§2.4 | Canonical / Locked | Current |
| DEC-002 | Rounding | All fractional calculations floor, no exceptions | D1 §2.5 | Canonical / Locked | Current |
| DEC-003 | Attribute matrix | 24 independently generated attributes (12 Body / 12 Mind), each 1d100 | D1 §3 | Canonical / Locked | Current |
| DEC-004 | Derived statistics | HP, MP, Physical Energy, Speed, Energy Regen, MP Regen, Movement Speed formulas; live-recalculation rule | D1 §4 | Canonical / Locked | Current |
| DEC-005 | Skill Tier/Cap/Starting Value | Cap = floored average of Tier attributes; Starting Value = floor(Cap/2) | D1 §5 | Canonical / Locked | Current |
| DEC-006 | Core Test Transaction | Fixed 9-step transaction (roll → outcome → cost → overflow → failure XP → doubles → recovery); no subsystem may replace it | D1 §6, reinforced by D1 §16 invariants 17–18 and D2 §2 | Canonical / Locked | Current |
| DEC-007 | Resource cost & Overflow | Cost = natural roll; insufficient resource → Overflow → direct HP damage; no second resource pool | D1 §7 | Canonical / Locked | Current |
| DEC-007.A | Overflow-immutability clause | **AMENDMENT (designer-approved wording, 2026-09-01):** Overflow is a pure function of the natural roll and the resource pool at time of test. No Tag, Trait, Effect, Condition, or subsystem may reduce, redirect, absorb, or otherwise modify Overflow's magnitude or application to HP. Placement: amendment to DEC-007 per designer ruling. **Corollary:** Armor Tags never modify Overflow (Item B corollary). | Designer ruling 2026-09-01; `tiwas-s5-armor-advisory-session-handoff-2026-09-01.md` §4 Item A | Canonical / Locked (amendment makes explicit existing implication) | Current |
| DEC-008 | Recovery | floor(Regen/2), clamped, always final step, unconditional | D1 §8 | Canonical / Locked | Current |
| DEC-009 | Failure XP | max(0, Roll − Skill) | D1 §9 | Canonical / Locked | Current |
| DEC-010 | Skill Roll Pool | Temporary, single-test-scoped; cascading increases while affordable; capped at Skill Cap; remainder → General XP | D1 §10 | Canonical / Locked | Current |
| DEC-011 | General XP | May exceed Cap; cost of +1 = current value; no partial advancement | D1 §11 | Canonical / Locked | Current |
| DEC-012 | Advanced Skills | Created only by a qualifying failed Double; Tier+1; full-formula Cap recompute; lineage-based resource domain | D1 §12 | Canonical / Locked | Current |
| DEC-013 | S-1 Opposed Contest | Universal opposed-contest primitive; outcome matrix; Margin/Blackjack/Hybrid Quality measures; Failure/Failure repeat; exact-tie repeat | D1 §13, confirmed complete/locked at D2 §8 | Canonical / Locked | Current |
| DEC-014 | S-2 Tier-1 Location Index provider (Zero-Step) | Deterministic tens/units-digit exchange on the natural attacking roll; no player choice; read-only post-process; does not alter Core Test consequences | D1 §14.1–§14.2 | Canonical / Locked — explicitly limited in scope (only the Tier-1 provider; not tier policy, anatomical mapping, or downstream interaction) | Current |
| DEC-015 | Reserved Systems list | Everything not explicitly locked remains outside the locked Core | D1 §15 | Canonical (a locked scope statement, not a locked mechanic for those subsystems) | Current |
| DEC-016 | Core Architectural Invariants | 18 invariants binding on all future subsystem work | D1 §16 | Canonical / Locked | Current |

**Scope note on DEC-014:** D1 §14.3 is explicit that this locks *only* the Tier-1 Location Index provider — not whether/when a scene uses Tier 0/1/2, not anatomical mapping, not wound/armor/defense interaction, not whether any later rule may consume a Location Index.

## 4.B. Non-canonical designer rulings (DEC-018 through DEC-093; DEC-017 promoted to Canonical)

All are genuine human/designer rulings on candidate/non-canonical material. None have completed the 8-step Promotion Rule, except DEC-017 which was promoted to Canonical §14.7 on 2026-09-05 (see §4.A reference). Status as of 2026-09-03:

### S-2 Hit Location Architecture (DEC-017 through DEC-022)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-017 | S-2 attack-side invocation/warrant policy | Four-state model + Named-Outcome Test accepted as "current non-canonical working direction" (attack-side only) | **Promoted to Canonical §14.7 (2026-09-05)** |
| DEC-018 | Explicit-only objectives | GM does not infer unstated distinct objective from location/fictional context alone | Current, folded into DEC-017's policy |
| DEC-019 | Structural Weak Points reclassified State 1 → State 2 | Anchored but not yet resolvable; zero State-1/Active cache entries currently exist | Current |
| DEC-020 | S-2 non-attack Location Index source — categorical deferral | Non-attack physical resolutions generate no Tier-1 Location Index under current design | **Reopened** — S-4 met reopening condition; now able to produce Wounds via Effect, pending new Location Index generation rule |
| DEC-021 | S-2 non-attack deferral — rejected alternative | "GM-authored hazard warrant" (Direction 1) rejected, not deleted | Current |
| DEC-022 | H0 provenance rule and riders | Retained as inert candidate record for non-attack question if/when reopened — explicitly not validated as operative rule | Inert / dormant |

### S-3 Outcome Effects (DEC-023 through DEC-031)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-023 | S-3 Effect menu structure | Tiered Effect menu: base tier + five gated tiers (Position → Time/Action; Condition → Conditions; Equipment → Equipment; Defense → S-6; Location → S-2 invocation promotion) | Ruled; Disarm/Break Hold placement finalised via DEC-028 |
| DEC-023.A | S-3 Gated-Tier Effect Content Enumeration (**AMENDMENT to DEC-023**) | **Package 1 Option A: Full alpha enumeration.** Content policy: no damage-over-time; Prone/Grappled/Restrained distinct; action-economy Effects → Skill-side or Movement penalty (Quality-scaled); beneficial Effects in scope. Locked alpha content by tier: *Base* — Inflict Injury, Open Retreat/Compel Yield. *Position* — Forced Movement, Knock Prone, Seize/Deny Ground, Pin/Hold Position, Open/Close Lane. *Condition* — Encumbered (DEC-078), Grappled, Restrained, Prone, Blinded, Deafened, Frightened, Slowed, Stunned/Incapacitated, Fatigued (DEC-075), Sunder-Condition (DEC-060), Poisoned/Sickened. *Equipment* — Disarm, Break/Sunder Item, Armor Bypass, Disable Device/Weapon, Steal/Take Item. *Defense* — Lower Defense, Deny Defense, Force Defense, Expose. *Location* — Impose Wound, Critical Location, Cripple Limb. **Prohibitions:** no DoT; no Advantage/Disadvantage language; no natural d100 modification (Invariant 6); no new pools (Invariant 17); one Effect per win (DEC-024) | Ruled; Condition-tier contents gated on Conditions subsystem (§10) |
| DEC-024 | S-3 Effect purchasing / multiplicity | Flat one-Effect-per-win. No Quality-based scaling. A second Effect requires a separate opposed roll — mechanism deferred | Ruled; mechanism deferred to new thread |
| DEC-025 | S-3 Effect naming/identity gating | Pure declared intent (no Skill-side gating). Formal tag/category system on Advanced Skills rejected | Ruled |
| DEC-026 | Second-Effect opposed-roll mechanism | Different Advanced Skill; defensive roll deferred to S-6 | Ruled |
| DEC-027 | Effect application — auto vs contested | Auto-apply. Winning S-1 with declared Effect applies it directly. Contested application rejected as S-3 default | Ruled |
| DEC-028 | State-3 Effect triggering — location+tag gating | Combined Location + Tag gating for Disarm/Break Hold, Equipment Damage, Armor Bypass. **Narrowed by DEC-041:** Skill-Tier ≥ 2 gate added | Ruled (narrowed by DEC-041) |
| DEC-029 | S-3/S-4 boundary | Confirmed prototype-only; base-tier Injury is HP-only, no wound produced | Ruled; S-4 direction non-binding |
| DEC-030 | Partial Tag/Location match | Fail-and-fall-back to Base Inflict Injury (HP-only) | Ruled |
| DEC-031 | S-3 Quality's Role in Single-Effect Outcome Resolution | Quality gates eligible Effects (Option B). Higher Quality unlocks more severe Effects; floor rule; no scaling | Ruled |

### S-4 Wound Activation/Severity (DEC-032 through DEC-039)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-032 | S-4 Terminology: Injury vs. Wound | Injury = HP Damage; Wound = Localized, Lasting Numerical State | Ruled |
| DEC-033 | S-4 Wound Trigger & Location Scope | Wounds exclusively triggered as selectable Effect from S-1 contest (Impose Condition: Wounded). Both Inflict Injury and Impose Condition: Wounded require Location Index. Overflow exempt. **Narrowed by DEC-041:** Skill-Tier ≥ 2 gate | Ruled (narrowed by DEC-041) |
| DEC-034 | S-4 Track A/B Interaction | Both Track A (Overflow→HP) and Track B (Wound Effects) can apply from one hit, sequentially | Ruled |
| DEC-035 | S-4 Wound Severity Definition | Severity comes from the S-3 gated Effect, not accumulated count. Wounds tracked individually with own numerical magnitude | Ruled (amended by DEC-035.A / DEC-035.B) |
| DEC-035.A | S-4 Wound format, magnitude, tier, stacking & healing (**AMENDMENT to DEC-035**) | Wound recorded as `Location X Tier-Y Wound Z (Attribute or Skill)`. Tier = equal-or-less-than causing skill's Skill-Tier OR GM Fiat (universal override). Magnitude Z = Tier (−Y). Same-tier/same-location wounds stack (values add) but never raise tier. Healing requires skill tier ≥ wound tier. GM Fiat overrides all downstream tier-gated requirements. **Clause 2 (Skill-Tier ceiling) refined/superseded by DEC-035.B** — Quality is the operative ceiling; Skill-Tier retains only production-gate function | Ruled; clause 2 refined by DEC-035.B |
| DEC-035.B | Quality × Skill-Tier Ceiling Precedence (**AMENDMENT to DEC-035.A; closes OPEN-007 residual**) | Quality is the hard ceiling on wound tier (wound tier ≤ Quality-gated Effect tier, DEC-031). Skill-Tier functions only as production gate (Skill-Tier ≥ 2 required, DEC-041). GM Fiat remains universal. **Consequence:** OPEN-007 magnitude architecture closed; accumulation-to-permanent-loss threshold remains GM discretion (DEC-055/DEC-070) | Ruled |
| DEC-036 | S-4 DEC-020 Reopening | DEC-020 (non-attack deferral) reopened. Non-attack physical resolutions can produce Wounds via Effect | Ruled |
| DEC-037 | S-2 / S-4 Non-Attack Location Index Generation | (1) Primary Provenance Rule: character's failed governing Core Test roll supplies digits for Zero-Step. (2) Hazard "Win": failure qualifies for S-3 Effect applied to location indicated by failed roll. (3) Systemic Exempt: global threats apply direct HP/Conditions. (4) Passive Fallback: numeric stub routed through Zero-Step | Ruled |
| DEC-038 | OPEN-001A — H0 Rider B causal attribution | Single causal-attribution principle: whichever Core Test is causally responsible supplies the Location Index | Ruled |
| DEC-039 | OPEN-001B — Extended Test governing roll for Location Index | Final roll in the sequence governs | Ruled |

### S-2 Tier Policy & Anatomical Mapping (DEC-040 through DEC-042)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-040 | OPEN-002 — Scene/campaign Location Tier default | Tier 0 is universal default; promotion is per-roll only; no scene-level "stays elevated" state. **Deferred:** which specific actions call for Tier 1 vs. Tier 2 promotion | Ruled (per-action promotion list deferred) |
| DEC-041 | OPEN-003 — Anatomical mapping: Skill-Tier-gated granularity | Six-part rule: (1) Gate: Location Index only when roll promoted + Skill-Tier 2+ (Advanced). Base/untrained = Skill-Tier 1, never triggers location. (2) Tier 1 → coarse zones via anatomically-weighted ranges. (3) Left/right via digit-parity. (4) Tier 2 → granularity scales with Skill-Tier (**directional, not locked**). (5) Individual creature templates. (6) Universal scope. **Deferred:** exact tier-to-granularity assignments, numeric ranges | Ruled (granularity assignments deferred) |
| DEC-042 | OPEN-004 — Tier-2 subdivision procedure and cost | Option B: secondary roll, no resource cost. Not a second Core Test. Location-mismatch → fail-and-fall-back per DEC-030 | Ruled |

### S-8 Third-Party Adjudication (DEC-043)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-043 | S-8 — Third-Party Adjudication of Mutual-Failure Opposed Contests (Q1–Q5) | All five sub-questions closed: same-skill default, full Core Test, binary outcome, inverted comparison, Double-eligible, generalized to all mutual-failure | Ruled |

### S-6 Defense (DEC-044 through DEC-050, DEC-075)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-044 | OPEN-005 S-6 Fork 3 — Defense architecture | Active Defense: defender makes genuine Core Test | Ruled |
| DEC-045 | OPEN-005 S-6 Fork 4 — Who makes the Defense roll | The defender rolls | Ruled |
| DEC-046 | OPEN-005 S-6 Fork 5 — Voluntary decline of Defense | Yes, defender may choose not to defend | Ruled |
| DEC-047 | OPEN-005 S-6 Fork 7 — Defense roll ceiling | Uncapped. Deferred: fatigue/exhaustion from repeated rolls | Ruled |
| DEC-048 | OPEN-005 S-6 Fork 2 — Defense timing vs. auto-apply | Model B: Effect auto-applies exactly as DEC-027; Defense acts as post-hoc mitigation, not a gate | Ruled |
| DEC-049 | OPEN-005 S-6 Fork 6 — DEC-026 deferred defensive position | Separate mitigation per Effect; each auto-applied Effect gets independent Defense roll | Ruled |
| DEC-050 | OPEN-005 S-6 Fork 1 — Defensible-Effect scope | Universal eligibility: any auto-applied Effect eligible. **Amendment (2026-09-01):** includes positive/beneficial Effects; invocation voluntary | Ruled (amended, resolves OPEN-009) |
| DEC-075 | OPEN-010 — S-6 repeated-Defense fatigue/exhaustion | No fatigue/exhaustion penalty beyond existing Cost/Overflow. Future fatigue, if implemented, = Condition-tier Effect (DEC-060 precedent), not a subsystem | Ruled (closes OPEN-010) |

### S-8 Stakes Gate (DEC-051)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-051 | S-8 Stakes Gate rejection | Rejected. No pre-Core-Test "skip the roll" filter for stakes-based reasons | Ruled |

### S-7 Incapacitation/Death (DEC-052 through DEC-057)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-052 | S-7 Fork 1 — HP = 0 forced incapacitation | HP = 0 triggers forced incapacitation. No roll, no save | Ruled |
| DEC-053 | S-7 Fork 2 — Wound/Incapacitation independence | Incapacitation is HP-driven only. Wound severity does not feed into incapacitation | Ruled |
| DEC-054 | S-7 Fork 3 — Permanent character loss (death) | Two-branch: (a) incapacitated + all revival skill tests failed (unlimited attempts), OR (b) voluntary choice while incapacitated | Ruled |
| DEC-055 | S-7 Fork 4 — Stabilization procedure | GM discretion, no formal procedure. Skill tests fixed by DEC-054; mechanics of attempts are GM discretion | Ruled |
| DEC-056 | S-7 Fork 5 — S-11 boundary | No interaction with S-11 (Rest/Healing) | Ruled |
| DEC-057 | S-7 Fork 6 — S-2 non-attack reopening trigger closure | Original flag superseded by DEC-053 (HP-only incapacitation); reopening pathway no longer exists | Ruled (session-level assessment) |

### S-5 Armor (DEC-058 through DEC-062)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-058 | S5-A — Armor architecture: Tags/Traits only | No numeric durability/soak pool. Tags/Traits system only. Never interacts with Overflow | Ruled |
| DEC-059 | S5-B — Bypass definition | Relational property between specific Tag pairs + location match required. Inapplicable at Location Tier 0 | Ruled |
| DEC-060 | S5-C — Sunder Effect | Addition model: adds "Sundered" Tag. Permanent. Resolved via ordinary Core Test. Selectable Effect at Condition tier | Ruled |
| DEC-061 | S5-D — Armor resolution sequence vs. Active Defense | Armor resolves before Active Defense. Tier-0 location hits never forced to promote by Armor alone | Ruled |
| DEC-062 | S5-E — Armor coverage location-bound + Zero-Step clause | Armor coverage location-bound; uses same fine-grained creature-template anatomy as DEC-041. Zero-Step clause: at Tier 0, struck location for Armor check derived via Zero-Step digit-exchange (read-only, no new roll, no promotion) | Ruled |

### S-8 Difficulty/Adjudication (DEC-063 through DEC-066)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-063 | S8-A — Difficulty grade structure | Named tiers with fixed additive Skill-side modifiers. Modifiers act on Skill side only — never on natural roll | Ruled |
| DEC-064 | S8-B — Difficulty-modified Skill usage scope | Effective Skill used for all three: success/fail check, Failure XP calculation, and Skill Roll Pool cascade entry | Ruled |
| DEC-065 | S8-C — Skill Roll Pool cascade cap | Effective Skill clamped at permanent Cap for cascade stopping condition. Preserves Invariant 10 exactly | Ruled |
| DEC-066 | S8-D — Difficulty grade symmetry | Symmetric grades (bonuses and penalties) | Ruled |

### S-9/S-10 Extended Tests (DEC-067 through DEC-070)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-067 | S9-A — Extended Test progress method | Margin-accumulation: each successful interval's Margin adds to running total; failures contribute nothing; monotonically increasing | Ruled |
| DEC-068 | S9-B — Extended Test failure behavior | Neutral: failed interval costs resources and generates Failure XP but does not reduce progress | Ruled |
| DEC-069 | S9-C — Invariant-17 coherence assessment | No Invariant-17 violation (no income/expenditure dynamic) | Ruled (architectural constraint assessment) |
| DEC-070 | S-9/S-10 Extended Test completion target | GM discretion, no formula | Ruled |

### S-11 Rest/Healing (DEC-071 through DEC-074)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-071 | S11-A — Rest/Healing resolution method | Explicit Skill Test required (full 9-step Core Test) | Ruled |
| DEC-072 | S11-B — Wound magnitude healing penalty | Penalty on healer's effective Skill (same pattern as DEC-064 difficulty-on-Skill-side) | Ruled |
| DEC-073 | S11-C — S-11 as literal Extended Test instance | S-11 healing IS an Extended Test instance: one Rest period = one interval; Margin-accumulation (DEC-067); failures neutral (DEC-068); GM discretion target (DEC-070) | Ruled |
| DEC-074 | S-11 healing completion target | GM discretion, generally — no HP-deficit lock | Ruled |

### S-12 Creature/Campaign (DEC-076 through DEC-077)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-076 | S-12 Ruling A — Creature/NPC stat-generation & resolution-economy mode fork | Dual-mode: computerized = full 24-attribute + Core Test; tabletop = abbreviated stat-block, GM discretion default. Earlier "GM-facing shortcut layer" draft explicitly rejected by designer | Ruled |
| DEC-077 | S-12 Ruling B — Creature/Campaign content authoring path | Content deferred to Tiwa's own playtesting. Not to be drafted by advisory models. **AMENDED by DEC-077.A:** advisory models may convert GURPS creatures to Tiwas working stat blocks for the BToV-Madness playtest (provisional, Tiwa rules each) | Ruled (amended by DEC-077.A) |
| DEC-077.A | BToV-Madness GURPS-to-Tiwas creature stat-block conversion (**AMENDMENT to DEC-077**) | Advisory models may convert GURPS source creatures to Tiwas working stat blocks for the BToV-Madness playtest; Tiwa rules on each; provisional unless affirmed. Rationale: Tiwa does not know GURPS, cannot author the conversion. Scope: BToV-Madness only, abbreviated stat-block (DEC-076) + individual-template (DEC-041) methods. Tiwa retains final ownership. Bar otherwise stands | Ruled (conversion workflow; provisional) |

### P3 — Encumbrance (DEC-078)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-078 | P3 — Encumbrance Model | **Option A: Load Thresholds/Penalties.** Sub-rulings: (A1) Capacity source: Body attribute — bpe/bee (Endurance-coded); (A2) Penalty application: Skill-side modifier only (DEC-063 / Invariant 6 compliant); (A3) Movement Speed interaction: untouched — locked `floor((bsp+bss)/15)` formula unchanged (DEC-004); (A4) Condition creation: yes — exceeding threshold imposes Condition Encumbered; (A5) Resource model: static thresholds + Skill-side penalty only; no secondary pool (Invariant-17-safe). **Hard dependency:** Conditions subsystem (Proposals §10, Reserved) — resolved by DEC-079. **Carried open:** exact capacity formula, threshold values, modifier magnitudes | Ruled (contents/values open) |

### §5.5 Reserved Systems — Conditions, Tags, Equipment, Time/Action (DEC-079 through DEC-082)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-079 | Conditions subsystem — format, magnitude, and alpha vocabulary | **Format:** `Tier-Y Condition Value Z` (global) or `Location X Tier-Y Condition Value Z` (localized), parallel to DEC-035.A Wound format. **Magnitude:** Value Z = −Y (identical to Wound). **Tier production:** Quality (hard ceiling) + Skill-Tier ≥ 2 (production gate). **Alpha vocabulary — 14 Conditions:** Encumbered (DEC-078), Grappled, Restrained, Prone, Blinded, Deafened, Frightened, Slowed, Stunned, Incapacitated, Fatigued (DEC-075), Sundered (DEC-060), Poisoned, Sickened. Each with mechanical effects, stacking rules, duration/removal. **Stacking:** most stack as "same-tier values add; higher replaces"; Stunned, Incapacitated, Prone, Grappled use "highest tier only." **Slowed + Encumbered:** do not stack — apply worse penalty. **Body-affecting scope:** all Skills using a Body Attribute. **Sundered:** Condition + Tag model (`state:sundered`), expanding DEC-060. **Resolves:** "hard dependency on Conditions subsystem" flagged in DEC-023.A, DEC-078 | Ruled (contents/values open) |
| DEC-080 | Tags ontology model and alpha vocabulary | **Ontology:** open extensible namespace-based model. **Alpha list — 34 Tags:** Equipment (22): slot:main_hand, slot:off_hand, slot:two_hand, slot:body, slot:head, slot:shield, damage:bludgeoning, damage:slashing, damage:piercing, offense:melee, offense:ranged, offense:thrown, handling:light, handling:heavy, handling:reach, handling:finesse, defense:armor, defense:shield, state:held, state:worn, state:sheathed, state:stowed. Environment (6): env:hazard_physical, env:hazard_systemic, env:terrain_difficult, env:terrain_hazardous, env:darkness, env:weather_obscuring. Creature (6): creature:type_humanoid, creature:type_beast, creature:type_undead, creature:size_small, creature:size_medium, creature:size_large. **Resolves:** "Tags subsystem starter vocabulary" dependency referenced in DEC-028 | Ruled (vocabulary extensible) |
| DEC-081 | Equipment state model | Equipment state fully expressed through Conditions + Tags. No independent state-tracker. Held items automatically receive the Location of the holding limb (consistent with DEC-062/DEC-041 anatomical mapping). | Ruled |
| DEC-082 | Time/Action economy model | Skill-side / Movement-penalty model only. No discrete action budget or action points. Consistent with Invariant 17 (no new resource pools) and DEC-063/DEC-072 penalty-expression precedent. | Ruled |

### S-12 BToV-Madness Creature Conversion & Playtest (DEC-083 through DEC-088)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-083 | Blood Man Blood Seep vs no-DoT policy | **Single-application Effect on a grapple win; NO ongoing DoT.** GURPS per-second corrosive DoT not ported (violates DEC-023.A no-DoT). Represented as one-shot Impose-Condition/Inflict-Injury on a Grapple-Contest win (per DEC-024 one-Effect-per-win) or narrative/GM-Fiat. Resolves the conflict flagged by Claude (§4.5) and Perplexity. Applies to Blood Man working stat block | Ruled |
| DEC-084 | Perplexity Goblin/Dragon scope | **Kept as Tiwa-authored NEW-Content creatures, NOT GURPS conversions.** No GURPS stat block exists for them in the source PDF; Perplexity invented standard templates. They are outside DEC-077.A conversion scope but may be developed as original Tiwas creatures. Ice Troll/Blood Man remain the only genuine conversions under DEC-077.A | Ruled (new-content classification) |
| DEC-085 | Playtest creature working baseline & method | **Adopt rule-faithful GPT-5.6 Luna baseline.** Derived stats via DEC-004/005; no GURPS dice/Dodge/Parry/DR numbers; Tier-2 signature attacks for Wound-capable creatures (not a universal rule); attack roll = attacker resource cost NOT target damage (DEC-007); test via Wound pathway first. **Open:** target-HP `Inflict Injury` magnitude, Regeneration/Regrowth/Fright vocabularies. *(Conditional freezing DR now resolved by DEC-088.)* | Ruled (method; Injury magnitude open) |
| DEC-086 | Creature signature-skill Starting Value | **Full-Cap "veteran" for creature signature (signature-attack) skills, NOT `floor(Cap/2)`.** Even for full 24-attribute Fork A creatures, signature attack skills start at Cap by content-authoring design (Wound-capable creatures must have functioning Tier-2 attack skills). General (non-signature) skills still use standard `floor(Cap/2)` or Fork B GM value. Applies to all future creature templates. Resolves Claude v0.2 §4.6 Fork A/B tension | Ruled (signature skills full-Cap veteran) |
| DEC-087 | Pre-authored Tier-2 creature skills | **Creature/NPC templates MAY pre-author ready-made Tier-2 (Advanced) skills at creation.** DEC-012's failed-Double origin rule applies to PC skill advancement, NOT creature/NPC template authoring. Preserves DEC-041 Tier-2 Wound gate and DEC-085 item (4) non-universal Tier-2. Resolves Claude v0.2 §4.7 | Ruled (pre-authored Tier-2 permitted) |
| DEC-088 | Environment-conditional Trait/Tag binding + `env:freezing` Tag | **Conditional-Trait Binding grammar (Condition Clause `Active only while [env:X] is present`) + new `env:freezing` scene-state Tag (7th entry in DEC-080 Environment namespace).** Read-only, stateless, GM-declared presence/absence; bound Trait/Effect treated as absent when Tag not present. Extends DEC-059's pattern; Invariant 17/6/7/DEC-007.A compliant. Resolves DEC-085's conditional freezing DR item. Applies to Ice Troll (Regeneration/Regrowth/DR all gated on `env:freezing`). **Open:** graded temperature (binary only now), scene-state tracking mechanism | Ruled (binding + Tag; graded temp & scene-tracking open) |

### S-14 5.5 Systemic Hazard Resolution Cadence (DEC-089 through DEC-093)

| ID | Subject | Decision | Status |
|---|---|---|---|
| DEC-089 | Systemic hazard cadence (H1-A) | Systemic hazard = ongoing progress toward surviving, not isolated damage events; uses existing Core Test machinery; NO new resource economy (Invariant 17; DEC-037/076) | Ruled |
| DEC-090 | Scope to S-3 Effect interface (H2-A) | Scoped to the S-3 systemic-hazard Effect interface; S-3 does NOT own the full hazard engine (Core Test / S-8 / DEC-037 / Cost / Overflow / XP / recovery remain distinct) | Ruled |
| DEC-091 | Terrain hazard coverage + `env:terrain_*` descriptive-only (H3-A) | Terrain hazards resolve via existing failed Core Test → DEC-037/Zero-Step → S-3 pipeline; `env:terrain_difficult`/`env:terrain_hazardous` are DESCRIPTIVE-ONLY (no independent mechanical trigger); difficulty from GM-graded DEC-063. Distinct from DEC-088's `env:freezing` activation Tag | Ruled |
| DEC-092 | Hazard difficulty as Skill-side penalty (H4-A) | Difficulty grade = fixed additive Skill-side modifier to Effective Skill (DEC-063); never modifies natural roll/Cost/Overflow/XP/recovery | Ruled |
| DEC-093 | Graded intensity as lookup key only (H5-B) | Intensity = lookup key into predefined hazard parameters only; no independent dice/resource/Effect/Overflow/transaction | Ruled |

## 4.C. Previously Open items — now all closed

| ID | Closed via | Date |
|---|---|---|
| OPEN-001 (H0 Rider B sub-options) | DEC-038 | 2026-08-31 |
| OPEN-002 (Scene/campaign Tier selection) | DEC-040 | 2026-08-31 |
| OPEN-003 (Anatomical mapping) | DEC-041 | 2026-08-31 |
| OPEN-004 (Tier-2 procedure/cost) | DEC-042 | 2026-08-31 |
| OPEN-005 (S-5–S-12 umbrella) | DEC-076/DEC-077 | 2026-09-01 |
| OPEN-006 (Wound Severity thresholds) | DEC-035 (corrected) | 2026-08-30 |
| OPEN-007 (Wound consequences) | Ruled (structure via DEC-035.A; Quality × Skill-Tier ceiling resolved by DEC-035.B) | 2026-08-30 (structured 2026-09-02; ceiling resolved 2026-09-02) |
| OPEN-008 (Non-attack LI generation) | DEC-037 | 2026-08-30 |
| OPEN-009 (S-6 positive-Effect defense) | DEC-050 amendment | 2026-09-01 |
| OPEN-010 (S-6 repeated-Defense fatigue) | DEC-075 | 2026-09-01 |

**No fork-level Open item remains in the register.**

---

# 5. Currently Open Design Threads (post-ruling, implementation-layer)

Nothing in the decision register is marked "Open." What remains are **open design threads** — content-enumeration, implementation-detail, and deferred-scoping work that the fork-level rulings explicitly left for future sessions. These are the items an advisory session might be asked about.

## 5.1 S-3 gated-tier Effect content enumeration (highest priority)

**What's Ruled:** The S-3 Effect menu *structure* is locked (DEC-023), and the *specific Effects within each gated tier* are now **enumerated** (DEC-023.A, 2026-09-02): full alpha content by tier, content policy rulings (no DoT, no Advantage/Disadvantage language, no natural d100 modification, no new pools, beneficial Effects in scope), and explicit prohibitions. DEC-024 (one-Effect-per-win) remains in force.

**What's still open:** The Condition-tier Effects are **gated on the Conditions subsystem** (Proposals §10, currently Reserved) — "Encumbered," "Grappled," "Restrained," etc. cannot be table-ready mechanics until that vocabulary exists. Equipment-tier Effects similarly require a Tags subsystem vocabulary (§11, Reserved). The S-2 anatomical mapping ranges (DEC-041 deferred) are needed for Location-tier Effects.

**Why it matters:** Blocking combat fidelity. Referenced as Critical for the Blood Man encounter (grapple/hold, darkness/vision, fear, tactical position, defense-mitigation interaction).

**Relevant DEC rulings (upstream context):**
- DEC-023 + DEC-023.A (menu structure + content enumeration) → DEC-028 (Tag+Location gating for three Effects) → DEC-041 (Skill-Tier gate universal)
- DEC-024 (one-Effect-per-win; second Effect mechanism deferred)
- DEC-026 (second-Effect uses different Advanced Skill; defensive roll deferred to S-6 — now locked DEC-044–050)
- DEC-027 (auto-apply) → DEC-048 (Defense is post-hoc mitigation) → DEC-050 (universal defensible scope)
- DEC-031 (Quality gates eligible Effects) → DEC-035.B (Quality is hard ceiling on wound tier)
- DEC-060 (Sunder addition-model precedent for Condition-tier Effect)
- DEC-075 (future fatigue = Condition-tier Effect, not a subsystem)
- DEC-078 (Encumbered = Condition-tier Effect, routes through Conditions subsystem)

**Dependency:** S-6 Defense is fully Ruled (DEC-044–050) but its *interaction with specific Defense-tier Effects* is not defined until Defense-tier Effects are enumerated (now done; locked in DEC-023.A). S-3 §11 (Tags subsystem starter vocabulary) is now resolved (DEC-080). All Condition-tier Effects now have a concrete vocabulary (DEC-079). The Conditions subsystem dependency flagged in §5.1 is **fully resolved**.

**Tracking note:** Explicitly flagged in DEC-050 amendment note ("the still-unenumerated S-3 gated-tier Effect content remains a separate tracking item") and the S-6/S-12 handoff §4 table.

## 5.2 Wound consequence magnitudes (OPEN-007 — now structured via DEC-035.A, Quality ceiling resolved via DEC-035.B, 2026-09-02)

**Note (2026-09-02):** This section is updated to reflect the DEC-035.A amendment and DEC-035.B quality-ceiling ruling. The wound **format, tier framework, magnitude and healing gate** are now Ruled (see §4.B table), and the Quality × Skill-Tier ceiling precedence is now resolved (DEC-035.B).

**What's Ruled (DEC-035.A, 2026-09-02):**
- Wound record format: `Location X Tier-Y Wound Z (Attribute or Skill)`
- Tier = equal-or-less-than causing skill's Skill-Tier OR GM Fiat (universal override)
- Magnitude Z = Tier (−1 for Tier-1, −2 for Tier-2, etc.)
- Stacking: same-tier/same-location wounds add; never raise tier
- Healing: skill tier ≥ wound tier; GM Fiat can override
- Wounds may now target Skills directly (scope expansion over DEC-032's attribute-only framing)

**What's Ruled (DEC-035.B, 2026-09-02 — resolves the OPEN-007 residual):**
- Quality is the **hard ceiling** on wound tier (wound tier ≤ Quality-gated Effect tier, DEC-031)
- Skill-Tier functions only as a **production gate** (Skill-Tier ≥ 2 required for any Location Index, DEC-041); does NOT raise or lower maximum wound magnitude
- GM Fiat remains the universal override (DEC-035.A clause 6)
- DEC-035.A clause 2 (Skill-Tier ceiling role) refined/superseded for ceiling purposes
- OPEN-007 magnitude architecture is **closed**; accumulation-to-permanent-loss threshold remains GM discretion (DEC-055/DEC-070)

**What's still open:**
- The individual penalty magnitudes are now defined *by tier*; the "accumulation to game-over threshold" (how many/which stacked wound negatives trigger DEC-054 permanent loss) remains GM-discretion per DEC-055/DEC-070 precedent, with no default guidance.

**Relevant DEC rulings:**
- DEC-032 (Injury vs. Wound terminology)
- DEC-033 (Wound trigger & Location Scope, narrowed by DEC-041)
- DEC-035 + DEC-035.A + DEC-035.B (severity, format, tier, magnitude, stacking, healing, quality ceiling)
- DEC-037 (non-attack LI generation)
- DEC-053 (Incapacitation HP-only, independent of Wounds)
- DEC-071–074 (S-11 healing as Extended Test instance)

## 5.3 S-2 residual architecture (anatomical mapping details, tier promotion triggers, GM-facing wording)

**What's Ruled (forks closed):**
- DEC-014: Zero-Step locked (Tier-1 LI provider)
- DEC-020 (reopened by DEC-036): non-attack deferral reopened
- DEC-037: Non-attack LI generation mechanism defined
- DEC-038: Causal attribution principle
- DEC-039: Extended Test governing roll
- DEC-040: Tier 0 default, per-roll promotion
- DEC-041: Skill-Tier-gated anatomical granularity (universal)
- DEC-042: Tier-2 secondary roll, no cost

**What's explicitly deferred (not closed, not Ruled):**
- **DEC-040:** "Which specific actions call for Tier 1 vs. Tier 2 promotion is deferred to per-Effect/per-action design (not resolved here)." — This depends on the S-3 Effect content enumeration (§5.1).
- **DEC-041:** "Exact tier-to-granularity assignments are directional, not locked." Numeric ranges/zone-weightings not finalized.
- **DEC-042:** Tier-2 formal rule text and Invariant-18 scoping statement still needed.
- **Proposals §2.5 / Roadmap §9:** "Final GM-facing wording for the simplified invocation procedure — drafted, not yet separately validated."

**Dependency:** Anatomical mapping numeric ranges (DEC-041 deferred) are needed before creature templates (DEC-077, Tiwa's domain) can be built. Tier-1/Tier-2 promotion trigger list (DEC-040 deferred) depends on S-3 Effect enumeration (§5.1).

## 5.4 S-12 creature/campaign content (architecture Ruled, content conversion-workflow Open)

**What's Ruled:** DEC-076 (dual-mode stat-generation fork) and DEC-077 (content authoring owned by Tiwa's playtesting). **Amendment DEC-077.A (2026-09-02):** for the BToV-Madness playtest, advisory models may convert GURPS source creatures to Tiwas working stat blocks, each pending Tiwa's ruling and provisional unless affirmed — because Tiwa does not know the GURPS system. This is scoped to BToV-Madness conversion work only; the DEC-077 bar against advisory-model authoring of definitive templates otherwise stands.

**What's open:** Actual creature templates (Goblin, Dragon, Ice Troll, Blood Man, etc.) do not exist yet — the BToV-Madness GURPS creature conversions are in progress under DEC-077.A. S-12's abbreviated stat-block format and automated-system tooling specifics are also not yet drafted (downstream implementation detail under DEC-076).

**Constraint:** DEC-077 bars advisory models from drafting *definitive* creature templates outside the DEC-077.A conversion workflow for BToV-Madness. Advisory models may propose GURPS-to-Tiwas working conversions for the playtest; Tiwa rules on each. The conversions are provisional playtest material, not finished or authoritative content. **Scope clarified by DEC-084 (2026-09-03):** only the Ice Troll and Blood Man are genuine GURPS conversions under DEC-077.A; Perplexity's Goblin/Dragon are **new-content creatures** (Tiwa-authored), not conversions. **Working method clarified by DEC-085 (2026-09-03):** adopt the rule-faithful GPT-5.6 Luna baseline — derived stats via DEC-004/005, no GURPS dice/Dodge/Parry/DR numbers, Tier-2 signature attacks for Wound-capable creatures, attack roll = attacker resource cost (not target damage), test via the Wound pathway first. Blood Seep resolved as single-application on grapple win (DEC-083). **Creature-skill conventions ruled by DEC-086/087 (2026-09-03):** creature signature attack skills are pre-built at full Cap as veteran content (not `floor(Cap/2)`), and creature/NPC templates may pre-author Tier-2 Advanced skills at creation (DEC-012's failed-Double origin applies to PC advancement, not creature authoring). **Env-conditional Traits ruled by DEC-088 (2026-09-03):** new Conditional-Trait Binding grammar (`Active only while [env:X] is present`) + `env:freezing` Tag (7th env entry); resolves DEC-085's conditional freezing DR and enables the Ice Troll's temperature-gated Traits (Regeneration/Regrowth/DR all gated on `env:freezing`).

## 5.5 Reserved systems (DEC-015) — structural Rulings exist, most now have concrete foundations

The canonical locked Core (DEC-015 Reserved Systems) leaves the entire non-locked universe as Reserved / unbuilt. The DEC decisions provide structural rulings for many of these. As of 2026-09-03, six major subsystems now have concrete foundations (DEC-079–082 Conditions/Tags/Equipment/Time-Action; DEC-088 env-conditional binding; DEC-089–093 hazard resolution cadence); Magic and Setting remain unbuilt.

| System | Proposals section | Status |
|---|---|---|
| Conditions | §10 | **Ruled** — DEC-079: format, magnitude, alpha vocabulary (14 Conditions); DEC-078: Encumbered; DEC-075: Fatigued; DEC-060: Sundered |
| Tags | §11 | **Ruled** — DEC-080: namespace ontology, 34-tag alpha vocabulary |
| Time/Action economy | §12 | **Ruled** — DEC-082: Skill-side / Movement-penalty only, no discrete action budget |
| Equipment | §13 | **Ruled** — DEC-081: expressed through Conditions + Tags; held items auto-receive holding limb Location |
| Hazards (environmental) | §14 | Partially addressed — `env:hazard_physical` and `env:hazard_systemic` Tags defined (DEC-080); resolution cadence/difficulty/intensity scoped (DEC-089–093); formalization still open |
| Magic/Special Abilities | §17 | Design Direction only |
| Setting Interface | §19 | Not started |
| Setting Integration | §20 | Not started |

**Dependency note (2026-09-02, updated 2026-09-03):** The Conditions vocabulary (DEC-079) and Tags vocabulary (DEC-080) now resolve the blocking dependencies that prevented Condition-tier and Equipment-tier Effects from being table-ready. The Conditions subsystem dependency flagged in DEC-023.A, DEC-078, and §5.1 is fully resolved. The Tags subsystem dependency flagged in DEC-028 is resolved. Hazard resolution cadence/difficulty/intensity is now scoped (DEC-089–093), and env-conditional Trait binding is ruled (DEC-088). Remaining open work: remaining Hazards formalization content (`env:hazard_physical` vs `env:hazard_systemic` detail), Position-tier Effect magnitudes, Magic/Special Abilities, and Setting Interface/Integration.

---

# 6. Evidence Pointers (not reproduced inline)

Evidence files are referenced by path + one-line status. Do not treat pointers as content copies.

| Pointer | Status |
|---|---|
| `investigations/tiwas-s3-designer-rulings-and-handoff-2026-08-29.md` | S-3 session rulings and handoff (rev. 1); source of DEC-023 through DEC-030 |
| `investigations/tiwas-s3-effect-identity-and-multi-effect-opposition-investigation-v0.1-open.md` | S-3 Effect Identity investigation thread — **Closed**, no open forks remain |
| `investigations/tiwas-s3-outcome-effects-investigation-v0.1-draft.md` | S-3 Outcome Effects investigation — draft, conclusions captured in DEC-023–031 |
| `investigations/tiwas-s4-documentarian-handoff-report-2026-08-30.md` | S-4 cross-model session handoff; source of DEC-032–037, stress-test audit finding |
| `investigations/tiwas-s4-dec035-original-wording-and-correction-2026-08-30.md` | Verbatim designer quote for DEC-035 correction |
| `investigations/tiwas-s4-dec037-stress-test-rerun-2026-08-30.md` | DEC-037 stress-test re-run (14 scenarios); non-blocking flags: H0 Rider B, S-8 dependency |
| `investigations/tiwas-s5-armor-advisory-session-handoff-2026-09-01.md` | S-5 Armor advisory session; source of DEC-058–062, DEC-007.A |
| `investigations/tiwas-s6-defense-opening-brief-2026-08-31.md` | S-6 Defense opening brief; source of DEC-044–050 |
| `investigations/tiwas-s7-s8-advisory-session-handoff-2026-09-01.md` | S-7/S-8 advisory session; source of DEC-043, DEC-051–057 |
| `investigations/tiwas-s8-s9s10-s11-advisory-session-handoff-2026-09-01.md` | S-8/S-9/S-10/S-11 advisory session; source of DEC-063–074 |
| `investigations/tiwas-s6-s12-session-handoff-2026-09-01.md` | S-6/S-12 session; source of DEC-075–077 |
| `investigations/tiwas-grok-advisory-session-decision-report-s3-content-encumbrance-wound-precedence-2026-09-02.md` | Grok 4.5 advisory session report; source of DEC-023.A, DEC-035.B, DEC-078 |
| `investigations/tiwas-grok-advisory-session-reserved-systems-5-5-conditions-tags-equipment-timeaction-2026-09-02.md` | Grok 4.5 advisory session report; source of DEC-079, DEC-080, DEC-081, DEC-082 |
| `investigations/tiwas-gurps-creature-conversion-scratch-ice-troll-blood-man-2026-09-03.md` | Claude Sonnet 5 GURPS→Tiwas conversion scratch v0.1 (Ice Troll, Blood Man); correct appendix appended per DEC-085/F-04 — superseded by v0.2 |
| `investigations/tiwas-gurps-creature-conversion-scratch-ice-troll-blood-man-v0.2-2026-09-03.md` | Claude Sonnet 5 GURPS→Tiwas conversion scratch v0.2 (GPT-5.6 Luna assessed); §4.1 Injury-magnitude flag, §4.6/§4.7 governance flags (source of DEC-086/087); Blood Seep flag resolved by DEC-083 |
| `investigations/tiwas-btv-madness-ice-troll-combat-pipeline-gpt-5.6-luna-2026-09-03.md` | GPT-5.6 Luna Ice Troll combat-pipeline report; source of DEC-085 baseline & F-01→F-08 findings |
| `investigations/tiwas-perplexity-creature-conversion-framework-playtest-2026-09-03.md` | Perplexity creature-creation transcript (framework + Ice Troll/Blood Man/Goblin/Dragon); source for DEC-084 classification |
| `investigations/tiwas-env-conditional-trait-tag-advisory-handoff-2026-09-03.md` | Claude Sonnet 5 advisory draft — Environment-Conditional Trait/Tag Binding (Option A); source of DEC-088 (Condition Clause grammar + `env:freezing` Tag; 7th env entry) |
| `investigations/tiwas-reserved-systems-hazard-cadence-confirmation-gpt5.6-luna-2026-09-03.md` | GPT-5.6 Luna advisory confirmation report — 5.5 Systemic Hazard Resolution Cadence (H1-A–H5-B); source of DEC-089–093 |
| `investigations/tiwas-s8-third-party-adjudication-mutual-failure-candidate-v1.md` | S-8 Third-Party Adjudication candidate; source of DEC-043 |
| `investigations/tiwas-s2-hit-location-investigation-v5-synthesis.md` | S-2 Design Investigation v5 synthesis (Correction Pass); source of DEC-017–019. **DEC-017 promoted to Canonical §14.7 (2026-09-05); synthesis retained as historical evidence record.** |
| `investigations/tiwas-s2-non-attack-location-source-closure-record-v1.2.md` | S-2 Non-Attack closure record; 14-scenario stress-test set; source of DEC-020–022 |
| `investigations/tiwas-s3-documentarian-handoff-report-dec028-2026-08-30.md` | S-3 DEC-028 handoff; Quality's role investigation |
| `investigations/llm-quality-s3-reports-2026-08-30.md` | 8-model LLM blind survey on Quality's role (5/8 Option B) |
| `sources/incoming/tiwas-s3-documentarian-handoff-report-2026-08-29.md` | S-3 documentarian handoff (per-decision reports: dec025, dec026, dec027) |
| `sources/incoming/tiwas-s3-documentarian-handoff-report-dec025-2026-08-29.md` | DEC-025 handoff report |
| `sources/incoming/tiwas-s3-documentarian-handoff-report-dec026-2026-08-29.md` | DEC-026 handoff report |
| `sources/incoming/tiwas-s3-documentarian-handoff-report-dec027-2026-08-29.md` | DEC-027 handoff report |
| `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` | D1 — Canonical Rules & Changelog (sole source of locked mechanics) |
| `proposals/tiwas-proposals-wip-and-design-direction-v1.4.3.md` | D3 — Proposals, WIP & Design Direction (non-canonical design repository) |
| `roadmap/tiwas-implementation-roadmap-and-project-governance-v1.4.3.md` | D2 — Implementation Roadmap & Project Governance (rule authority: none) |

---

# 7. Conflict Register Summary

No unresolved substantive rules conflict exists in the corpus. The single evidence-gap item (C5, missing prior-version source text) is closed as an **accepted permanent limitation** by human ruling (2026-08-29); recovery is no longer required. See `_consolidation/conflict-register.md` for full detail.

---

# 8. Snapshot Label

This is a **dated, task-scoped snapshot** compiled by OpenCode (documentarian, live repo access) on 2026-09-02, for a single advisory design session. It is NOT the authoritative corpus, NOT a standing merge artifact, and NOT current beyond this session. The live repository (`_consolidation/decision-register.md` and all files it references) is ground truth at all times.

All design material in this file is **non-canonical** unless explicitly labelled Canonical/Locked. Nothing in this snapshot promotes, demotes, or reclassifies any document in the repository.
