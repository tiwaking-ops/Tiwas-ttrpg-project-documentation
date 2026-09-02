---
document:
  title: "Tiwas & Beyond the Vale of Madness — Development-Planning Report (25-LLM Meta-Analysis)")
  version: "1.0"
  status: "NON-CANONICAL - advisory development-planning compilation. Condenses 25 LLM adaptation reports and the Alpha Playtest Corpus; makes no rulings and confers no authority."
provenance:
  author_llm:
    - name: "Arena.ai Agent Mode"
      version: "unknown / not established (self-reported)"
    - name: "opencode"
      version: "big-pickle"
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-02"
  last_modified_date: "2026-09-02"
---

# Tiwas & *Beyond the Vale of Madness* — Development-Planning Report

## Standing-prohibition overrule — required log entry (per Alpha Corpus §1)

This document was compiled to a single workspace file as an internal development-planning
aid for the human designer (Tiwa). It is a dated, one-off advisory compilation, **not** a
standing merge artifact and **not** a reinstatement of the "do not create another single
merged file" prohibition. It should **not** be periodically regenerated. Scope set as an
advisory document per Tiwa's instruction; this is a compilation choice, not a design ruling.

The documents synthesised here (the 25-LLM meta-analysis and the Alpha Playtest Corpus) were
themselves produced under their own standing-prohibition overrules / scoped-exception
records; this report inherits their NON-CANONICAL status and confers none of it onward.

---

## Status, purpose and audience

**Status**: NON-CANONICAL — advisory only. This report condenses the 25 independent LLM
adaptation reports, as registered in the compiled meta-analysis and the Alpha Playtest Corpus,
into a single development-planning report. It makes **no rulings**, promotes nothing, demotes
nothing, closes nothing, and reopens nothing. The Canonical / Locked vs Non-canonical designer
ruling vs Draft-pending-reconfirmation vs Open / Missing / Reserved distinctions are preserved
**exactly** as they appear in the Alpha Corpus and decision register.

**Purpose**: To support Tiwa's actual development decisions about which missing systems to
build and in what priority order, ahead of the first proper playtest of *Beyond the Vale of
Madness (GURPS)* as a Tiwas benchmark. It is not for public or community consumption, and it is
not a substitute for Tiwa's decision authority.

**Agreement-as-evidence note (required)**: Where reports converge, that convergence is
diagnostic evidence of analytical agreement among reporting LLMs, **never** a Tiwas design
ruling. Authority over any design decision remains with Tiwa through the repository's
formal governance path (`_consolidation/decision-register.md`; Promotion Rule REQ-021 per
`governance/status-model.md`). This report neither settles nor floats any D1–D10 position.

**Authorship / assessor disclosure**: `author_llm` lists the producing session identities used
in the sources this report draws on (the compiled meta-analysis's self-reported producing
identity and the current compiler, opencode/big-pickle). The Arena.ai producing identity is
`unknown / not established` (self-reported; the platform exposes no non-forgeable model-version
metadata). `assessor_llm` is empty — no independent assessment pass has been performed on this
report, and none is claimed.

---

## Compilation basis and method

- Condensed from the system-by-system comparison and the priority-tier compilation of the 25
  source reports (see Part F for source pointers), cross-checked against the Alpha Playtest
  Corpus's status vocabulary and DEC numbering (`Tiwas-Alpha-Playtest-Corpus-2026-09-01.md`)
  and the live decision register (`_consolidation/decision-register.md`).
- Classification wording each report used is preserved where quoted; where reports use
  different readiness labels, those labels are retained verbatim rather than forced into one
  taxonomy, and each is mapped to the five shared readiness categories only where the report
  itself intended it.
- Corroboration figures are stated as "N of 25" by named report, per the source compilations.
- Source-grounding caveats are carried forward and must weight interpretation (Part F).

---

# Part A — Collated System Readiness Assessment

Each subsystem: DEC reference, Tiwas baseline status, reporting-LLM convergence/divergence,
representative quotes, readiness classification, blocking significance, development
recommendation. "Readiness" here is always *readiness to run the BTvM benchmark*, not a
statement that the subsystem is finished.

## SYS-Core — Core Test Transaction (DEC-001–DEC-016)

- **DEC refs**: DEC-001 (d100), DEC-002 (floor), DEC-003 (24-attribute), DEC-004 (derived),
  DEC-006 (Core Test Transaction), DEC-007/DEC-007.A (Cost/Overflow), DEC-009–DEC-012
  (Failure XP / Advanced Skills / recovery).
- **Tiwas baseline status**: Canonical / Locked (D1).
- **Convergence**: **Unanimous — Playtestable Now.** All 25 reports classify the Core Test as
  playtestable now.
- **Representative quotes**: chatgpt-5-2-1 "Core Test Transaction (DEC-006) for climbing,
  search, willpower, perception-like checks..."; chatgpt-5-6-2 "Playtestable Now — one of the
  strongest findings of the audit"; claude5-1 "the 9-step Core Test Transaction... Backbone of
  every resolution."
- **Readiness classification**: Playtestable Now.
- **Blocking significance**: None for the Core loop itself. Recurring caveat: **adaptation
  skill-mapping** (which Tiwas Skill stands in for each GURPS skill/attribute) is content work,
  not a Core gap; GURPS attributes must be routed through a Tiwas Skill.
- **Development recommendation**: No Core design action. Author the skill-mapping table for
  the adventure's specific task types before a session (content task).

## SYS-01 — S-1 Universal Opposed Contest (DEC-013)

- **Tiwas baseline status**: Canonical / Locked (DEC-013).
- **Convergence**: Strong consensus the S-1 primitive is Playtestable Now. Narrow split on
  **NPC stat values** (S-12 content) and **quality-mode selection**, not the S-1 mechanism.
- **Representative quotes**: chatgpt-5-6-1 "The adventure's Stealth-vs-Perception situation is
  a very strong direct test of S-1... one of the clearest successes"; grok-2 "Stealth vs
  Perception maps directly."
- **Readiness classification**: Playtestable Now (primitive); Adaptation Mapping Required for
  NPC Perception-equivalent values and DEC-013 quality-mode choice.
- **Blocking significance**: Branch-gate High (needs statted opponents via S-12).
- **Development recommendation**: No S-1 design action. Require an NPC Perception value when
  the troll's stat block is authored (ties to Part E, NPC Content).

## SYS-02 — S-2 Location / Hit-Location / Zero-Step Index (DEC-014, DEC-037, DEC-039)

- **Tiwas baseline status**: Canonical / Ruled non-canonical (Zero-Step provider DEC-014;
  non-attack provenance DEC-037/DEC-039).
- **Convergence**: Majority rate the Zero-Step Location Index Playtestable Now, several with an
  adaptation/integration caveat (anatomical mapping; connection to injury). **Disagreement**:
  mistral-1 rates it Missing Subsystem (no full GURPS hit-location table); copilot365-2_1 more
  conservative (Adaptation Mapping Required).
- **Representative quotes**: kimi-1 "Tier-1 (Head/Torso/Arms/Legs) is sufficient for this
  adventure"; claude5-1 "Ready, architecture only" (invoked only if combat/wound detail desired).
- **Readiness classification**: Playtestable Now for coarse Tier-1 zones; location-dependent
  consequences Design-Stage.
- **Blocking significance**: Low for the current adventure text paths (BTvM does not require
  detailed hit location to function).
- **Development recommendation**: No action required for the benchmark unless wound
  localization is desired; the Skill-Tier 2+ gate (DEC-041) largely side-steps the adventure.

## SYS-03 — S-3 Effects / Outcome Payloads (DEC-023–DEC-031)

- **Tiwas baseline status**: Base tier (Inflict Injury HP-only, Retreat/Compel Yield) Ruled
  non-canonical; **gated tiers (Position/Condition/Equipment/Defense/Location) have structure
  (DEC-023) but contents are NOT enumerated**. This is the single most-reported gap.
- **Convergence**: **24 of 25** name S-3 gated-tier content enumeration as a blocker.
  Near-unanimous that *the menu structure is Ruled and only the contents are missing*. Range:
  "CRITICAL BLOCKER" (gemini-2) down to "moderate gap" (copilot365-1_1).
- **Representative quotes**: chatgpt-5-2-1 "S-3 has a 'Condition tier' concept but contents not
  enumerated"; copilot365-2_1 "S-3 effect-content catalogue remains incomplete"; claude5-1
  "Ready" at architecture level.
- **Readiness classification**: Base tier Playtestable Now; gated tiers Design-Stage
  Dependency. mistral-1 calls the whole thing Missing Subsystem.
- **Blocking significance**: High (principal combat/content blocker). The concrete asks recur:
  fear, darkness, grapple/hold, ongoing "Blood Seep" corrosive damage, and the base-tier
  "Inflict Injury" **damage magnitude** (undefined — see Part E, Damage Magnitude).
- **Development recommendation**: Priority-1 content task: enumerate the gated-tier Effect
  contents the adventure actually exercises (Conditions, Position, Equipment, Defense,
  Location), building on the Ruled menu structure. This is the largest unblock action.

## SYS-04 — S-4 Wounds / Injury (DEC-032–DEC-042; OPEN-007)

- **Tiwas baseline status**: Damage/injury architecture (Injury=HP, Wound=localized state)
  Ruled non-canonical. **OPEN-007 wound-consequence magnitudes are Ruled in principle
  (penalties −1/−5/−30/−80/−100, healing-cost scaling) but not compiled as table-ready.**
- **Convergence**: Architecture broadly Ruled; OPEN-007 consequence magnitudes are the open
  item — classified Design-Stage by most, a real blocker by several (chatgpt set, copilot365-2,
  metaai set, grok set), but Playtestable Now by deepseek-1 and recallAI-1, and "Ready at
  architecture level (zone numbers open)" by claude5-1. Genuine readiness disagreement (D8).
- **Representative quotes**: chatgpt-5-6-2 "OPEN-007 wound consequences remain not table-ready";
  metaai-2 "Publish OPEN-007 magnitudes as table-ready"; deepseek-1 "Playtestable Now (with
  magnitude scaling remaining)."
- **Readiness classification**: Playtestable Now (injury/HP loop) / Design-Stage Dependency
  (consequence magnitudes); dissenting voices as above.
- **Blocking significance**: Medium–High (blocks injury→first-aid loops when wound penalties and
  healing-cost scaling are used).
- **Development recommendation**: Compile OPEN-007's Ruled magnitudes into a table-ready form
  and close the damage-magnitude question (ties Part E, Damage Magnitude). This is a dominate
  content/compilation task under an existing ruling, not new mechanics.

## SYS-05 — S-5 Armor / Shields / DR / Tags (DEC-058–DEC-062)

- **Tiwas baseline status**: Ruled non-canonical (Tag/Trait-based; no numeric soak).
- **Convergence**: Clear split. A playtestable-now block (copilot set, copilot365 set, recallAI-1,
  claude5-1) versus a design-stage/content block (chatgpt set, metaai set, mimo set, kimi-1,
  perplexity set, mistral-1 as Missing). Shared substantive point: **GURPS numeric DR does not
  map**; Tiwas armor is Tag-based with a **starter Tag vocabulary still to be authored** (Ice
  Troll's cold-conditional DR 2, Blood Man's DR 1).
- **Representative quotes**: kimi-1 "The system exists but adventure-specific Tags must be
  authored to replace GURPS DR values"; metaai-1 "The adventure's DR 2 only in freezing cannot
  be expressed without Tag definitions."
- **Readiness classification**: Playtestable Now (Tags architecture) / Design-Stage Dependency
  (Tag vocabulary content). See D9.
- **Blocking significance**: High for the two combats (armor reduces what attacks do).
- **Development recommendation**: Author a starter armor-Tag vocabulary for the adventure's
  equipment/monsters (Mail, Leather, Homogenous, cold-conditional, etc.) as a content task.

## SYS-06 — S-6 Active Defense / mitigation (DEC-044–DEC-050)

- **Tiwas baseline status**: Ruled non-canonical (Active Defense architecture: DEC-044–DEC-050;
  DEC-075 fatigue closure). **Which skill/attribute the defender rolls, and what mitigation
  does per Effect, is the open question.**
- **Convergence**: A large Playtestable-Now block (recallAI-1, copilot set, copilot365 set,
  deepseek-1, gemini set, grok set, metaai set, glm, chatgpt-5-6-1, claude5-1) versus a
  Design-Stage block citing the unspecified defender-skill / per-effect-mitigation (chatgpt-5-2-1,
  chatgpt-5-5-high-1, chatgpt-5-6-2, kimi-1, mimo set, perplexity set, mistral-1). Registered as
  D5/D8.
- **Representative quotes**: kimi-1 "which skill or attribute the defender rolls is not
  specified"; recallAI-1 "Active Defense... covers 90% of the tactical needs."
- **Readiness classification**: Playtestable Now (architecture Ruled) / Design-Stage Dependency
  (defender-skill + mitigation mapping).
- **Blocking significance**: High if combat runs "as written" with mitigation; the defender-skill
  gap is a genuine open choice for Tiwa.
- **Development recommendation**: Rule which skill/attribute the defender rolls for Active
  Defense and how mitigation affects an already-applied Effect (a design fork for Tiwa, not
  content authoring alone).

## SYS-07 — S-7 Incapacitation / Death (DEC-052–DEC-057)

- **Tiwas baseline status**: Ruled non-canonical (DEC-052–DEC-057).
- **Convergence**: Strong majority Playtestable Now. **Disagreement**: perplexity pair classifies
  death/unconsciousness as Missing/Design-Stage (no thresholds); mistral treats the death
  threshold as unspecified; claude5-1 adds a source-draft caveat (handoff still draft pending
  Tiwa reconfirmation).
- **Representative quotes**: chatgpt-5-5-high-1 "S-7 is one of the more usable non-canonical
  subsystems"; copilot365-1_1 "S-7 fully covers this."
- **Readiness classification**: Playtestable Now (majority); dissents above.
- **Blocking significance**: Medium (map the adventure's "incapacitated vs dead" end condition).
- **Development recommendation**: No design action; map the adventure's end-state to Tiwas
  Incapacitated/Dead states as adaptation. Note the claude5-1 draft-reconfirmation caveat.

## SYS-08 — S-8 Difficulty / Modifiers (DEC-063–DEC-066)

- **Tiwas baseline status**: Ruled non-canonical (additive effective-Skill modifiers, graded
  tiers). **The named difficulty-tier numeric modifier table and a GURPS→Tiwas conversion policy
  are not fully supplied in the excerpt.** mimo-2-5-2 flags the Promotion-Rule (REQ-021) caveat
  that S-8 is Ruled but not formally promoted.
- **Convergence**: Broad consensus the S-8 *mechanism* is Playtestable Now; the recurring open
  item is the numeric tier table + conversion policy (chatgpt-5-5-high-1, perplexity set,
  chatgpt-5-2-1 as Design-Stage/Adaptation).
- **Representative quotes**: chatgpt-5-6-2 "The remaining work is mapping GURPS modifiers into
  Tiwas difficulty grades, not designing a new resolution mechanic"; gemini-2 "finalize named-tier
  table (Easy +10, Hard −20)."
- **Readiness classification**: Playtestable Now (mechanism) / Adaptation Mapping Required (tier
  table + conversion policy).
- **Blocking significance**: Medium (needed to express the adventure's ±3/−5/DX−5 modifiers).
- **Development recommendation**: Author the named difficulty-tier table and a GURPS-modifier
  conversion policy (content/table task, not a new mechanic). Record the REQ-021 promotion caveat.

## SYS-09 — S-9/S-10 Extended Tests (DEC-067–DEC-070)

- **Tiwas baseline status**: Ruled non-canonical (DEC-067–DEC-070).
- **Convergence**: General consensus Playtestable Now; the adventure does not deeply require
  extended tests. Minor divergences: grok-2's cold-temperature template question (no
  continuous-attrition template), perplexity-2's single-vs-extended mapping policy, chatgpt-5-2-1's
  "Adventure Content Only."
- **Readiness classification**: Playtestable Now.
- **Blocking significance**: Low.
- **Development recommendation**: None required for the benchmark.

## SYS-10 — S-11 Rest / Healing / First Aid (DEC-071–DEC-074)

- **Tiwas baseline status**: Ruled non-canonical. Healing is a literal S-9/S-10 Extended Test
  instance requiring an explicit Skill Test (DEC-071–DEC-074).
- **Convergence**: Broadly Playtestable Now; the recurring open item is **mapping the GURPS
  immediate "First Aid restores 1d−3 HP" onto Tiwas' Margin/Extended-Test healing model**
  (flagged as Adaptation by chatgpt-5-6-2, kimi-1, metaai set, chatgpt set).
- **Readiness classification**: Playtestable Now (system) / Adaptation Mapping Required
  (1d−3 → Margin/Extended-Test mapping).
- **Blocking significance**: Low–Medium.
- **Development recommendation**: Author the First-Aid-to-S-11 mapping as adaptation content.

## SYS-11 — S-12 Creatures / NPC stat blocks / template method (DEC-076–DEC-077)

- **Tiwas baseline status**: Ruled non-canonical. DEC-076 (dual-mode stat-generation fork:
  automated full-24-attribute vs GM-run abbreviated; GM discretion on system).
  **DEC-077 (content authoring deferred to Tiwa's own playtesting — not to be drafted by any
  advisory model).** **No creature templates exist** (Ice Troll, Blood Man absent).
- **Convergence**: **The single most-cited blocker — 23–24 of 25.** The decisive taxonomy
  disagreement (D2) is whether this is a **content-authoring task under the already-Ruled
  architecture** (claude5-1, kimi-1, copilot-1_1, grok-1, copilot-2_1, deepseek-1) or a
  **Missing Subsystem / system gap** (mistral-1, mimo set, metaai set, recallAI-1, grok-2, glm).
- **Representative quotes**: recallAI-1 "THE critical blocker... S-12 is empty. No pre-made Ice
  Troll exists"; claude5-1 "a troll stat template must be authored (content, not a system gap)";
  copilot365-1_1 "S-12 remains content-authoring territory."
- **Readiness classification**: Missing Subsystem (content) / content-authoring task; the split
  is D2.
- **Blocking significance**: **Highest — blocks the two central combats.**
- **Development recommendation**: Per **DEC-077**, creature templates are Tiwa's own authoring
  task and are **not** to be drafted by Claude or any advisory model in this process. The report
  therefore notes the requirement and the ownership boundary; it does not draft the stat blocks.

## SYS-12 — Equipment / Weapons / Combat Payload / Damage / Damage Types (DEC-015 Reserved)

- **Tiwas baseline status**: **Reserved (DEC-015).** No settled equipment system.
- **Convergence**: Broad agreement this is a major remaining gap — Missing/Design-Stage (only
  recallAI-1 rates it playtestable-with-GM-Tags; copilot-1_1 does not treat it as a separate
  blocker). Two recurring sub-items: **damage magnitude/no non-Overflow damage** and
  **damage-type differentiation** (crushing/cutting/corrosive).
- **Readiness classification**: Missing Subsystem / Design-Stage Dependency.
- **Blocking significance**: High (the adventure repeatedly uses equipment to gate actions).
- **Development recommendation**: Decide the minimal-viable equipment/encumbrance rule and, with
  S-3/S-5, author the starter weapon/gear Tags. Flag the damage-magnitude design decision (Part E).

## SYS-13 — Environmental Hazards / Cold / Darkness / Survival / Time-pressure

- **Tiwas baseline status**: Systemic threats (Extreme Temperature etc.) exempt from Location
  Index per DEC-037 §3; no continuous-cold / darkness content layer.
- **Convergence**: **One of the clearest disagreements (D7).** A playtestable-now/minor block
  (copilot set, copilot365-1_1, gemini set, recallAI-1, glm, perplexity-1 via DEC-037) versus a
  P0-blocker/missing block (grok set, chatgpt-5-5-high-1, mistral-1, mimo set, metaai set on rates,
  kimi-1, claude5-1 on flat dice). Continuous-cold P0 claim is the strongest in the set.
- **Readiness classification**: Mixed — Playtestable Now vs Missing/P0 depending on report.
- **Blocking significance**: High (continuous-cold block) if the opening risk economy is to be
  reproduced; otherwise Medium.
- **Development recommendation**: Decide whether continuous cold is required for alpha or can be
  treated as GM-discretion attrition. If required, author the hazard cadence/content layer.

## SYS-14 — Fear / Fright / Morale / Mental-stress Conditions

- **Tiwas baseline status**: No fear subsystem anywhere. Folds into the S-3 Condition-tier
  enumeration (contents unwritten).
- **Convergence**: **Hard split (D3).** Majority treat fear as Missing/Design-Stage (consequence
  model absent: what a failed Fright Check does). Minority treat basic Fright Checks as
  playtestable via Will/Resolve Core Tests (mistral-1, grok-1 binary, grok-2 substitution,
  perplexity basic).
- **Readiness classification**: Missing Subsystem (consequence model) / Playtestable via mental
  tests (basic).
- **Blocking significance**: Medium (load-bearing for tone per claude5-1).
- **Development recommendation**: Decide whether a fear consequence is needed before first
  playtest or only for full fidelity; if needed, define the Frightened Condition Effect content
  within the S-3 Condition tier (design/content decision, Part E).

## SYS-15 — Magic / Spells / Special Abilities

- **Tiwas baseline status**: Magic is Reserved (DEC-015 list). No magic implementation.
- **Convergence**: **D4 split — magic as Required/Missing vs Not-required/excludable.** The
  concrete shape most converge on: **exclude the Enfys/mage pregen from alpha, or rule a
  minimal non-canonical fire-only stub** (metaai-1/metaai-2). copilot365-1_1 firmly "NOT
  REQUIRED"; glm calls it Critical/Priority-1; copilot365-2_1 Required-for-parity.
- **Readiness classification**: Missing Subsystem (but excludable for alpha).
- **Blocking significance**: High only if the mage pregen is used; Low/absent if the non-magical
  pregen is used.
- **Development recommendation**: Make the scope decision (exclude Enfys OR fire-only stub)
  before alpha; defer full magic design. Do not invent a magic system (Part E flags the decision).

## SYS-16 — Economy / Loot / Treasure / Currency / Advancement Reward

- **Tiwas baseline status**: No settled economy; advancement via General XP (DEC-011) exists.
- **Convergence**: **D6 — deepseek-1 is the outlier** (Critical/Priority-2, conclusion #60
  needs treasure valuation). Nearly every other report treats it as Adventure Content Only /
  non-blocking or a low-priority mapping item.
- **Readiness classification**: Adventure Content / non-blocking (majority); Missing (deepseek-1).
- **Blocking significance**: Low (majority) / High (deepseek-1).
- **Development recommendation**: Treat treasure/valuation as adventure-content mapping; do not
  design an economy for the benchmark unless decision #60's resolution requires it.

## SYS-17 — Skills / Skill-list / Skill-mapping / Untrained-fallback (skill defaults)

- **Tiwas baseline status**: Skill mapping is content (no canonical skill catalog in the excerpt);
  **no skill-default / untrained-attribute-substitution rule exists anywhere.**
- **Convergence**: Mapping is near-universally content adaptation. **D10 — the untrained-fallback
  rule is elevated disproportionately**: claude5-1 calls it **"the single largest blocking
  factor for full mechanical fidelity"** with no existing investigation touching it; kimi-1 calls
  it an immediate pre-session Critical ruling, with the sharp observation that a Skill-0 test on
  d100 (range 1–100) "can never succeed" because success requires roll ≤ 0. Others treat it as a
  mapping/design-stage item of lower urgency (chatgpt-5-5-high-1, perplexity set, metaai set,
  mistral-1).
- **Readiness classification**: Missing Subsystem (claude5-1, kimi-1) / Adaptation or handled via
  defaults-Difficulty (others).
- **Blocking significance**: High per the elevated minority (Skill-0 on d100 is unrollable); low
  for the majority. **Recommendation-flag**: disproportionately important relative to low
  corroboration count.
- **Development recommendation**: Rule a skill-default / untrained-fallback before the first
  session (a genuine design fork for Tiwa, not content authoring). See Part E.

## SYS-18 — Time / Action Economy / Tactical Movement / Combat Procedure Integration

- **Tiwas baseline status**: No dedicated combat-procedure / time-action-economy DEC; assembled
  from the S-1..S-7 chain (each Ruled non-canonical). No turn-order / movement / per-second
  ongoing-effect model.
- **Convergence**: **The largest divergence in the whole set (D1).** Playtestable-now-leaning
  (recallAI-1, claude5-1, copilot-1_1, copilot365-1_1, gemini-1, deepseek-1) versus
  design-stage/integration-dependent (the ~16-report majority). Time/action economy is the crux:
  "per-second" Blood Seep and movement cannot be represented without it; others deem tactical grid
  **optional** (abstract combat acceptable; copilot365-1_1 "Ignore entirely").
- **Readiness classification**: Playtestable Now (chain integrated) vs Missing/Design-Stage
  (procedure + time/action), per D1.
- **Blocking significance**: High (full-fidelity combat); Low-to-optional for abstract/ToTM
  combat.
- **Development recommendation**: Decide the alpha combat procedure scope — full consequence-chain
  integration vs. theater-of-mind abstraction. If the Blood Man "per-second" mechanic is to run,
  a time/action economy (or an explicit ToTM substitute) is required (Part E).

## SYS-19 — Grapple / Ongoing (corrosive) Damage / "Blood Seep"

- **Tiwas baseline status**: No grapple subsystem; folds into S-3 gated-tier Effect enumeration
  (structure Ruled, contents unwritten).
- **Convergence**: Few reports treat it as distinct (chatgpt set, metaai-2, kimi-1, mimo set,
  grok set); those that do expose it as a concrete combat blocker central to the Blood Man
  set-piece (Attack → Wound → Grapple → ongoing Blood Seep → death).
- **Readiness classification**: Missing / Design-Stage (as S-3 content).
- **Blocking significance**: High only on the Blood Man branch.
- **Development recommendation**: Include Grapple/Hold + ongoing-damage in the S-3
  Condition/Position-tier enumeration (content task under the Ruled menu structure).

---

# Part B — Development Priority Framework

Priorities derived from the 25 reports' convergence on blockers. This is a recommended
**sequencing** aid for Tiwa's decision-making; it is not a ruling. Corroboration is "N of 25"
by named report, per the source compilations.

## Priority 1 — S-3 gated Effect-menu contents (Position/Condition/Equipment/Defense/Location)

- **Corroboration**: 24 of 25.
- **Why**: The menu structure is Ruled (DEC-023) but contents are unwritten; nearly every
  combat/content blocker (grapple, fear, ongoing damage, conditions) routes through this.
- **Unblocks**: full-fidelity combat and conditions.
- **Recommendation**: populate the gated-tier Effect contents the adventure actually exercises.

## Priority 2 — S-12 creature/NPC stat blocks (Ice Troll, Blood Man)

- **Corroboration**: 23–24 of 25 (single most-cited blocker).
- **Why**: the two central combats cannot run without stat blocks.
- **Unblocks**: both featured combats, Stealth-vs-Perception (needs NPC value), combat testing.
- **Recommendation**: per DEC-077, this is **Tiwa's own authoring task** (not advisory-model
  drafting). Author the two blocks under the Ruled DEC-076 method.

## Priority 3 — Equipment / weapons / item Tags + encumbrance

- **Corroboration**: 20–22 of 25.
- **Why**: the adventure repeatedly uses equipment to gate actions; weapon Tags (Reach, Heavy)
  are the concrete ask.
- **Unblocks**: weapon/gear use and the treasure/economy mapping.
- **Recommendation**: decide a minimal-viable equipment/encumbrance rule and author starter Tags,
  in coordination with S-5 armor and S-3 Equipment tier.

## Priority 4 — Combat procedure / consequence-chain integration (incl. time/action economy)

- **Corroboration**: 10–12 of 25 (see D1 — genuine split on whether this is needed).
- **Why**: full-fidelity combat and the "per-second" Blood Seep mechanic need a time/action model.
- **Unblocks**: faithful combat; not required for abstract/ToTM alpha.
- **Recommendation**: decide full-chain vs theater-of-mind scope (Part E), then integrate.

## Priority 5 — Wound consequences (OPEN-007) table-ready + damage magnitude

- **Corroboration**: 16–18 of 25.
- **Why**: OPEN-007 magnitudes are Ruled in principle but not table-ready; damage magnitude for
  non-Overflow damage is undefined.
- **Unblocks**: injury→first-aid loops and weapon/hazard damage assignment.
- **Recommendation**: compile OPEN-007 magnitudes table-ready; rule the base "Inflict Injury"
  magnitude (Part E, Damage Magnitude).

## Priority 6 — Continuous cold / environmental hazard content layer

- **Corroboration**: 14–16 of 25 as a gap; ~9–10 treat as already playtestable (D7).
- **Why**: the opening risk economy (cold/hypothermia/exhaustion) cannot be reproduced without a
  continuous cold model (grok set P0).
- **Unblocks**: faithful opening-sequence play.
- **Recommendation**: decide whether continuous cold is required for alpha; if yes, author the
  hazard cadence/content (can defer with GM discretion otherwise).

## Priority 7 — Conditions: Fear / Fright / morale

- **Corroboration**: 19–21 of 25 as an item; categorization splits hard (D3).
- **Why**: tone/load-bearing per claude5-1; the Frightened consequence model is absent.
- **Unblocks**: full-fidelity fear mechanics (not required for binary Will-test play).
- **Recommendation**: decide whether a fear consequence is needed for the first playtest; if yes,
  define the Frightened Condition Effect (Part E).

## Priority 8 — Magic scope decision

- **Corroboration**: 19–21 of 25 name magic; split "missing" vs "excludable" (D4).
- **Why**: the supplied pyromancer pregen (Enfys) is unsupported.
- **Unblocks**: full-benchmark parity and use of the mage pregen.
- **Recommendation**: decide **exclude Enfys OR rule a minimal fire-only stub** for alpha; defer
  full magic design. Never invent a magic system here.

## Priority 9 — Economy / treasure valuation + advancement-reward mapping

- **Corroboration**: 7–8 of 25 as a gap; several treat as adventure content (D6). deepseek-1 is
  the outlier (Critical/Priority-2).
- **Why**: only conclusion #60 (treasure → reward) needs valuation.
- **Unblocks**: campaign continuity / decision #60 resolution; not required for the short form
  (majority).
- **Recommendation**: treat as adventure-content mapping unless decision #60 must be resolved.

## Dependency graph (simplified sequencing)

```
S-3 Effect menu contents (P1)
   ├─→ Wound consequences OPEN-007 + Damage magnitude (P5)   [S-3 base "Inflict Injury"]
   ├─→ Conditions incl. Fear (P7)                             [S-3 Condition tier]
   ├─→ Grapple / ongoing damage (P1-as-S-3)                   [S-3 Position/Condition tier]
   └─→ Combat procedure integration (P4)                      [Effects → consequence chain]
S-5 Armor Tags (P3-alongside)
   └─→ Equipment/weapons Tags + encumbrance (P3)
S-12 creature stat blocks (P2)                                  [needs S-3 effects to function]
   └─→ Combat testing / Stealth-vs-Perception (P4-adjacent)
S-8 difficulty-tier table (P3-alongside)                        [enables modifiers]
   └─→ Environmental hazard content (P6)                        [uses difficulty + conditions]
Magic scope decision (P8)                                       [parallel; exclude-or-stub]
Economy mapping (P9)                                            [parallel; adventure content]
```

Dependencies reflect the source reports' stated blockers; exact ordering is Tiwa's call.

## Shortest diagnostic route that avoids major blockers

Several reports describe a low-combat / non-combat path (kimi-1 "~15% minimum no-combat path";
perplexity set "exploration-and-resolution playtest"; glm "90% shortest path"). The common
recommended slice:

1. **Core Test (SYS-Core)** — Playtestable Now.
2. **Skill mapping** (SYS-17 content) — author the task→Skill table.
3. **S-8 difficulty-tier table** (SYS-08) — author numeric grades for modifiers.
4. **S-1 opposed contests** with a GM-furnished NPC value (SYS-01) — no S-12 world needed for a
   single opposed check.
5. **S-7/S-11** (SYS-07, SYS-10) for end-state and recovery.

This slice avoids the S-3-gated, equipment, and creature blockers (P1/P2/P3) and is playtestable
now for the exploration-and-resolution portion of the adventure, per the reports that describe it.

## Which priorities unblock full-fidelity play of *Beyond the Vale of Madness*

Near-unanimous reports: **full** fidelity requires P1 (S-3 effects) **and** P2 (S-12 creatures)
at minimum; P3 (equipment) and P4 (combat procedure/time-action) for the combat set-pieces; P5
(wound consequences) for injury/first-aid; P6 (cold) for the opening; P7 (fear) for tone; P8
(magic) for the mage pregen; P9 (economy) only for decision #60. A **partial** alpha (non-combat
routes) is available once P1+skill-mapping+S-8 exist; a **combat-inclusive** alpha additionally
needs P2 and (per D1) a decision on P4.

---

# Part C — Named Disagreement Register (D1–D10)

All ten positions remain **live and unresolved**. Nothing here selects between them; per
governance, only Tiwa can resolve them through the formal path. Side A/Side B and the practical
Consequence are recorded for each. Sides list the LLMs on each position per the source comparisons.

### D1 — Is the combat pipeline / full adventure playtestable now?

- **Side A** (Playtestable-now-leaning, chain integrated): recallAI-1, claude5-1, copilot-1_1,
  copilot365-1_1, gemini-1, deepseek-1.
- **Side B** (Design-stage / integration-dependent, majority): chatgpt-5-2-1, chatgpt-5-5-high-1,
  chatgpt-5-6-1, chatgpt-5-6-2, copilot-2_1, copilot365-2_1, gemini-2, grok-1, grok-2, kimi-1,
  metaai-1, metaai-2, mimo-2-5-1, mimo-2-5-2, mistral-1, perplexity-1, perplexity-2.
- **Consequence**: whether "author two monsters" (P2) is sufficient to unblock combat, or whether
  the combat consequence chain / time-action economy (P4) must be integrated and verified first.

### D2 — S-12 taxonomy: content-authoring task vs Missing Subsystem

- **Side A** (Content-authoring under Ruled architecture): claude5-1, kimi-1, copilot-1_1, grok-1,
  copilot-2_1, deepseek-1.
- **Side B** (Missing Subsystem / system gap): mistral-1, mimo-2-5-1, mimo-2-5-2, metaai-1,
  metaai-2, recallAI-1, grok-2, glm.
- **Consequence**: scopes the dev ticket — "author N stat blocks" vs "design a creature system +
  author N stat blocks."

### D3 — Fear/fright: Missing Subsystem vs playtestable via mental tests

- **Side A** (Missing / design-stage, majority): chatgpt-5-2-1, chatgpt-5-5-high-1, chatgpt-5-6-1,
  chatgpt-5-6-2, copilot-2_1, copilot365-2_1, facebai-laguna-s-2-1-1, gemini-1, gemini-2, metaai-1,
  metaai-2, mimo-2-5-1, mimo-2-5-2, perplexity-1, perplexity-2, recallAI-1, copilot365-1_1,
  claude5-1.
- **Side B** (Playtestable / substitution, minority): mistral-1 (Will test), grok-1 (binary),
  grok-2 (substitution), perplexity-1/-2 (basic Will), copilot365-1_1 (generic mental).
- **Consequence**: whether a fear ruling is needed before first playtest or only for full
  fidelity.

### D4 — Magic: Required/Missing vs Not-required/excludable

- **Side A** (Required / Missing, must decide): chatgpt-5-6-2, copilot365-2_1, glm, kimi-1,
  mistral-1, metaai-1, metaai-2.
- **Side B** (Not required / excludable): copilot365-1_1, deepseek-1, chatgpt-5-2-1, perplexity-1,
  perplexity-2 (chatgpt-5-6-1, gemini set, grok set treat as deferrable).
- **Consequence**: whether a magic ruling is needed before first playtest or only for full
  benchmark parity.

### D5 — Overall verdict: playtestable now vs restricted/not-yet

- **Side A** (Yes today): recallAI-1 ("playtest this adventure in Tiwas today"; "System-Ready but
  Content-Empty"), copilot365-1_1 ("75–85% ready"; "can be run today"), copilot-1_1 ("mechanically
  playtestable now" with scaffolding).
- **Side B** (restricted / not-yet): variously — non-combat-only (perplexity set, kimi-1 ~15%,
  glm 90% shortest path, metaai set martial ~70%); No for the full adventure (chatgpt set, gemini
  set, grok set, mimo set, mistral-1, facebai-laguna-s-2-1-1, copilot365-2_1, deepseek-1,
  copilot-2_1, claude5-1).
- **Consequence**: whether an alpha session can be scheduled now (minority) or only after Tier-1 /
  P1–P2 items complete (majority).

### D6 — Economy/treasure: Critical blocker vs Adventure Content

- **Side A** (Critical / Priority-2, outlier): deepseek-1 only ("conclusion #60 cannot be resolved
  without an economy").
- **Side B** (Real-but-low/adaptation): copilot-1_1, copilot-2_1, chatgpt-5-6-1, grok-1, metaai-1,
  glm, copilot365-2_1.
- **Side C** (Adventure content / non-blocking): kimi-1, metaai-2, mistral-1, perplexity-1,
  perplexity-2, grok-2.
- **Consequence**: whether conclusion #60 cannot be resolved without an economy (deepseek) or is
  adventure-content (majority).

### D7 — Continuous cold / environmental attrition: P0 blocker vs already covered

- **Side A** (P0 blocker): grok-1, grok-2.
- **Side B** (Design-stage / missing): chatgpt-5-5-high-1, chatgpt-5-6-1, copilot365-2_1,
  facebai-laguna-s-2-1-1, metaai-1, metaai-2, mimo-2-5-1, mimo-2-5-2, mistral-1, perplexity-2,
  chatgpt-5-2-1.
- **Side C** (Already playtestable / minor): copilot-1_1, copilot-2_1, copilot365-1_1, gemini-1,
  gemini-2, recallAI-1, glm, perplexity-1.
- **Consequence**: whether the opening risk economy can be reproduced without a continuous cold
  model.

### D8 — Wound consequences (OPEN-007): ready vs design-stage vs missing

- **Side A** (Playtestable Now / architecture ready): deepseek-1, recallAI-1, claude5-1
  (architecture, zone numbers open).
- **Side B** (Design-stage / content missing, majority): chatgpt set, copilot set, copilot365 set,
  grok-1, grok-2, kimi-1, metaai set, mimo set, perplexity set, glm.
- **Consequence**: whether wound consequences block the injury/first-aid loop or are a
  content-completion task.

### D9 — S-5 Armor subsystem: playtestable architecture vs design-stage/content

- **Side A** (Playtestable Now / Ready, Tags architecture): copilot-1_1, copilot-2_1,
  copilot365-1_1, copilot365-2_1, recallAI-1, claude5-1.
- **Side B** (Design-stage / Adaptation / Missing, Tag vocabulary to author): chatgpt-5-2-1,
  chatgpt-5-5-high-1, chatgpt-5-6-1, chatgpt-5-6-2, deepseek-1, metaai-1, metaai-2, mimo set,
  kimi-1, perplexity set, grok-2, mistral-1, glm.
- **Consequence**: whether armor needs only Tag content or a stronger approach (numeric DR cannot
  be imported).

### D10 — Skill-default / untrained-fallback rule: single highest priority vs routine mapping

- **Side A** (Single highest priority / Missing Subsystem): claude5-1 (highest), kimi-1 (Critical
  immediate).
- **Side B** (Design-stage / mapping): chatgpt-5-5-high-1, perplexity-1, perplexity-2,
  chatgpt-5-2-1, mistral-1, metaai-1, metaai-2.
- **Side C** (Handled via defaults / Difficulty): copilot-1_1, copilot-2_1, grok-2, metaai-2.
- **Consequence**: whether a Skill-default ruling is required before the first session.

---

# Part D — Playtest Readiness Verdict

Verdict expressed in the 5 shared readiness categories used across the reports (Playtestable Now /
Adaptation Mapping Required / Design-Stage Dependency / Missing Subsystem / Adventure Content),
per subsystem in Part A.

## Full-adventure readiness: **Not Ready**

Near-unanimous (see D5): the full adventure cannot be run "as written" until at least P1
(S-3 effects) and P2 (S-12 creatures) complete, with P3–P8 depending on combat/attrition/fear/magic
scope. The majority holds combat-inclusive play is no; a minority holds a restricted/partial run is
schedulable today.

## Partial-diagnostic readiness: **Partially Playtestable**

A non-combat exploration-and-resolution route is playtestable now once the following are in place:

- **Playtestable Now** (no prior work): Core Test (DEC-001–016), S-1 opposed primitive (DEC-013),
  S-2 coarse zones (DEC-014/037/039), S-7 (DEC-052–057), base-tier S-3 (DEC-023 Inflict Injury
  HP-only) — all as full Core Tests.
- **Adaptation content required first**: skill-mapping table, S-8 difficulty-tier table, First-Aid
  mapping, Stealth-vs-Perception NPC value (single GM-furnished number, not full S-12).

## Systems that block combat (must be before combat runs as written)

- S-3 gated Effect contents incl. damage magnitude (P1/P5).
- S-12 creature stat blocks (P2) — the two monsters.
- Equipment/weapon Tags (P3).
- Combat consequence-chain / time-action integration **or** an explicit ToTM substitute (P4, D1).

## Systems that are optional (deferrable / adventure-content)

- S-2 detailed hit location (Low; Tier-1 coarse is enough).
- Economy/treasure valuation (D6 majority: adventure content).
- Magic (D4: exclude mage pregen or fire-only stub).
- Tactical grid (D1 minority + copilot365-1_1: abstract acceptable).

## Classification summary (5 readiness categories)

| Subsystem | Category |
|---|---|
| Core Test (SYS-Core) | Playtestable Now |
| S-1 Opposed Contest | Playtestable Now (primitive); adaptation for NPC values |
| S-2 Location / Zero-Step | Playtestable Now (coarse); consequences Design-Stage |
| S-3 Effects (base) | Playtestable Now |
| S-3 Effects (gated contents) | Design-Stage Dependency (24/25 blocker) |
| S-4 Wounds / OPEN-007 | Playtestable Now (injury loop); consequences Design-Stage (D8) |
| S-5 Armor | Playtestable Now (architecture); Tag content Design-Stage (D9) |
| S-6 Active Defense | Playtestable Now (architecture); defender-skill Design-Stage (D5/D8) |
| S-7 Incapacitation / Death | Playtestable Now |
| S-8 Difficulty | Playtestable Now (mechanism); tier-table Adaptation (REQ-021 caveat) |
| S-9/S-10 Extended Tests | Playtestable Now |
| S-11 Rest / Healing | Playtestable Now; First-Aid mapping Adaptation |
| S-12 Creatures / NPC | Missing Subsystem / content task (D2); **P2 owner = Tiwa (DEC-077)** |
| Equipment / payload / damage | Missing Subsystem / Design-Stage |
| Environmental hazards / cold | Playtestable Now vs Missing/P0 (D7) |
| Fear / fright / morale | Missing Subsystem (consequence model) / basic mental Playtestable (D3) |
| Magic | Missing Subsystem (excludable for alpha) (D4) |
| Economy / treasure | Adventure Content (majority) / Missing (deepseek outlier) (D6) |
| Skills / untrained-fallback | Missing Subsystem (elevated) / adaptation (D10) |
| Time / action economy | Playtestable Now (chain) vs Missing/Design-Stage (procedure) (D1) |
| Grapple / ongoing damage | Missing / Design-Stage (as S-3 content) |

---

# Part E — Missing System Design Decisions

For each critical missing subsystem, this notes **what Tiwa must decide** and explicitly does
**not** provide or invent mechanics. Each item records where a design decision is required and
whether it can be deferred or handled as GM discretion for alpha. All final authority is Tiwa's.

## E-1 — Damage magnitude (base-tier "Inflict Injury")

- **Status**: base-tier S-3 Effect structure Ruled (DEC-023), but the numeric magnitude of a
  base "Inflict Injury (HP-only)" for weapon/hazard damage is **undefined** (Kimi) and non-Overflow
  damage magnitude is unspecified (SYS-12/SYS-13).
- **Decision**: how much HP a base "Inflict Injury" Effect deals (e.g., fixed number, Margin-based,
  or per-Effect), and how GURPS dice damage converts into Tiwas terms.
- **Alpha**: can GM-discretion at the table for a short run **if** Tiwa is willing; but note
  DEC-007.A forecloses modeling flat fall-damage dice via Overflow. Recommend a ruling before combat.
- **Cannot be deferred without**: any weapon or hazard that deals non-Overflow damage.

## E-2 — Combat procedure / time-action economy

- **Status**: no dedicated procedure DEC; assembled from the S-1..S-7 chain.
- **Decision**: (a) is combat run as a full consequence-chain procedure, and (b) is a time/action
  economy needed to represent "per-second" ongoing effects (Blood Seep) and movement, or is a
  theater-of-mind abstraction sufficient (D1)?
- **Alpha**: ToTM abstraction can defer the time/action economy; the Blood Man branch cannot run
  "per-second" without it (or an explicit simplification).
- **Cannot be deferred without**: full-fidelity Blood Man combat.

## E-3 — Skill-default / untrained-fallback rule

- **Status**: Missing Subsystem; claude5-1 calls it the single largest blocker; kimi-1 notes a
  Skill-0 test on d100 can never succeed (roll ≤ 0 impossible).
- **Decision**: what an untrained character's effective Skill is for an attribute-roll substitute
  (e.g., floor(governing attribute/2), −20 per missing Tier, or another rule). Candidate values
  appear across reports but no Tiwas ruling exists.
- **Alpha**: **cannot be deferred** for full fidelity — 8 untrained calls exist (kimi-1). A GM
  fallback could mask it for a single session, but this is a true design fork, not content.

## E-4 — Fear / fright consequence model

- **Status**: no fear subsystem; folds into S-3 Condition-tier enumeration.
- **Decision**: whether a Frightened Condition Effect (with a defined consequence) is required
  for the first playtest, or whether a binary Will/Resolve Core Test is sufficient (D3).
- **Alpha**: binary Will-test can defer the consequence model; tone fidelity needs the Condition.
- **Cannot be deferred without**: full-fidelity fright-check tone (Fright Check −2).

## E-5 — Magic scope

- **Status**: Magic Reserved (DEC-015); no implementation. The mage pregen (Enfys) is unsupported.
- **Decision**: **exclude the Enfys pregen from alpha OR rule a minimal non-canonical fire-only
  stub** (per the metaai set's decision-doc framing). Full magic design is deferred.
- **Alpha**: excludable — use the non-magical pregen.
- **Cannot be deferred without**: the pyromancer pregen and full-benchmark parity.

## E-6 — NPC Content (S-12 creature stat blocks)

- **Status**: DEC-076 (method) Ruled; DEC-077 (ownership) Ruled — **content authoring is Tiwa's
  own task, not advisory-model drafting**.
- **Decision**: Tiwa authors Ice Troll and Blood Man stat blocks under DEC-076; the D2 split
  (content task vs system gap) determines whether a creature *system* also needs design.
- **Alpha**: the two combats cannot run without the blocks.
- **Cannot be deferred without**: the two featured combats (P2).

## E-7 — Equipment / encumbrance / weapon Tags

- **Status**: Reserved (DEC-015).
- **Decision**: the minimal-viable equipment/encumbrance rule and the starter weapon/gear Tag set
  (Reach, Heavy, etc.), coordinated with S-5 armor and the S-3 Equipment tier.
- **Alpha**: can be light (GM-authored Tags) for a short run, but the adventure repeatedly gates
  actions on equipment (priorities concrete ask).
- **Cannot be deferred without**: faithful gating of many early decisions.

## E-8 — Continuous cold / environmental hazard cadence

- **Status**: systemic-threat exemption exists (DEC-037 §3) but no continuous-cold/darkness content.
- **Decision**: whether continuous cold attrition is required for alpha or handled as GM-discretion
  fatigue (D7).
- **Alpha**: GM discretion can reproduce an approximation; faithful opening risk economy needs the
  cadence/content.
- **Cannot be deferred without**: faithful reproduction of the opening cold risk.

## E-9 — Grapple / ongoing corrosive damage (Blood Seep)

- **Status**: no grapple subsystem; part of S-3 gated-tier enumeration.
- **Decision**: whether Grapple/Hold + ongoing-damage are enumerated as S-3 Condition/Position-tier
  Effects for the Blood Man branch.
- **Alpha**: simplifiable (e.g., treat as a Condition) at Tiwa's discretion; full fidelity needs the
  Effects.
- **Cannot be deferred without**: the Blood Man set-piece as written.

## E-10 — Economy / treasure valuation

- **Status**: no settled economy; advancement via General XP (DEC-011) exists.
- **Decision**: whether decision #60 (treasure → reward) needs a valuation procedure (deepseek
  outlier) or can be handled as adventure-content mapping (majority, D6).
- **Alpha**: deferrable — treat as adventure content.
- **Cannot be deferred without**: resolution of #60 as a measured reward.

---

# Part F — Source and Evidence Register

## The 25 source reports (by LLM, report number, file reference)

Per the attribution manifest (`investigations/tiwas-adapt-vale-of-madness-reports-1-llm-attribution-2026-09-02.md`).
Filenames below correspond to the merged-file section names; the repaired Copilot/Copilot 365
reports are stored in `investigations/` with the `_1` suffix.

| # | Report (merged section name) | Source-report author | Repaired file (where applicable) |
|---|---|---|---|
| 1 | btvmadness-adapt-report-chatgpt-5-2-1.md | ChatGPT 5.2 | — |
| 2 | btvmadness-adapt-report-chatgpt-5-5-high-1.md | ChatGPT 5.5-high | — |
| 3 | btvmadness-adapt-report-chatgpt-5-6-1.md | ChatGPT 5.6 | — |
| 4 | btvmadness-adapt-report-chatgpt-5-6-2.md | ChatGPT 5.6 | — |
| 5 | btvmadness-adapt-report-copilot-1.md | Copilot | btvmadness-adapt-report-copilot-1_1.md |
| 6 | btvmadness-adapt-report-copilot-2.md | Copilot | btvmadness-adapt-report-copilot-2_1.md |
| 7 | btvmadness-adapt-report-copilot365-1.md | Copilot 365 | btvmadness-adapt-report-copilot365-1_1.md |
| 8 | btvmadness-adapt-report-copilot365-2.md | Copilot 365 | btvmadness-adapt-report-copilot365-2_1.md |
| 9 | btvmadness-adapt-report-deepseek-1.md | DeepSeek-V3 | — |
| 10 | btvmadness-adapt-report-facebai-laguna-s-2-1-1.md | Laguna S 2.1 | — |
| 11 | btvmadness-adapt-report-gemini-1.md | Gemini 3.6 Flash | — |
| 12 | btvmadness-adapt-report-gemini-2.md | Gemini 3.6 Flash | — |
| 13 | btvmadness-adapt-report-grok-1.md | Grok 4.6 | — |
| 14 | btvmadness-adapt-report-grok-2.md | Grok 4.6 | — |
| 15 | btvmadness-adapt-report-kimi-1.md | Kimi K3 | — |
| 16 | btvmadness-adapt-report-metaai-1.md | Muse Spark 1.1 | — |
| 17 | btvmadness-adapt-report-metaai-2.md | Muse Spark 1.1 | — |
| 18 | btvmadness-adapt-report-mimo-2-5-1.md | Mimo 2.5 | — |
| 19 | btvmadness-adapt-report-mimo-2-5-2.md | Mimo 2.5 | — |
| 20 | btvmadness-adapt-report-mistral-1.md | Mistral | — |
| 21 | btvmadness-adapt-report-perplexity-1.md | Perplexity | — |
| 22 | btvmadness-adapt-report-perplexity-2.md | Perplexity | — |
| 23 | btvmadness-adapt-report-recallAI-1.md | RecallAI | — |
| 24 | Tiwas-Adventure-Readiness-Audit-Vale-of-Madness-2026-09-01.md | Claude 5 Sonnet | — |
| 25 | Tiwas-Adventure-Readiness-Audit.md | glm-4.5-air | — |

## Repaired Copilot / Copilot 365 attribution

In the original merge, the Copilot pair and the Copilot 365 pair were textually identical
duplicate pairs. Tiwa supplied corrected versions; the four reports are now distinct and treated
as independent viewpoints in this report (no duplicate-pair discounting). The corrected files are
stored under the `_1` suffix in `investigations/`.

## Adventure-sourcing caveats (must be stated)

- **`Beyond-the-Vale-of-Madness-GURPS.pdf` was not directly accessible to the compilation
  process.** Its contents are inferred **via the 25 reports' extractions** from it, not from
  direct reading of the PDF. This is a compositional limitation; it does not establish authority.
- Report-level grounding differs: `glm` had no direct PDF access (requirements inferred from
  generic GURPS patterns); `copilot-2_1` worked from a truncated/garbled extract; `mimo-2-5-2`
  OCR-scanned with transcription errors and truncated in the Blood Man stat block; `chatgpt-5-2-1`
  parsed pages 1–12 plus 16–19 (pregens); all others had the full PDF or full provided text. Weigh
  these when relying on any single report's specific claims.

## Primary records consulted

- `investigations/tiwas-adapt-vale-of-madness-reports-1.md` (merged 25-report corpus)
- `investigations/tiwas-adapt-vale-of-madness-reports-1-llm-attribution-2026-09-02.md`
- `investigations/tiwas-adapt-vale-of-madness-reports-compilation-2026-09-02.md`
- `investigations/tiwas-adapt-vale-of-madness-reports-system-comparison-2026-09-02.md`
- `Tiwas-Alpha-Playtest-Corpus-2026-09-01.md`
- `_consolidation/decision-register.md`
- `governance/status-model.md`, `governance/provenance.md`

---

# Part G — Explicit Guesses / Assumptions

Every interpretation, classification, or inference not directly stated in a source is flagged
here, per source-reports' convention. None of these is a Tiwas ruling.

1. **D1–D10 classification threshold.** The threshold for "materially different" (when a split
   was registered as a named disagreement vs. routine emphasis variation) was applied per the
   meta-analysis method (§2.5). This is a compilation choice, not a Tiwas ruling.
2. **Readiness-category inference.** Where a report did not explicitly tag a subsystem with one
   of the five readiness categories, the category assigned here was inferred from the report's
   overall treatment of that subsystem, flagged per report. Where reports disagreed, the split is
   preserved (Part C) rather than averaged.
3. **"Agreement = evidence, not authority."** The interpretation that LLM consensus constitutes
   diagnostic convergence (not authority) is an interpretive choice carried throughout; it is
   consistent with governance but is itself a judgement.
4. **Development-priority vs. pure-analysis framing.** The prompt's "Development priorities +
   recommendations" selection was resolved as: this report presents priorities and recommendations
   but deliberately not full mechanics. A pure-analysis-only reading of the brief would have
   omitted Part B. This report chose the combined reading.
5. **Combined author identity.** `author_llm` "Both" combines the meta-analysis's self-reported
   producing LLM with the current compiler. No platform-metadata mechanism independently verified
   either identity.
6. **Damage-magnitude and defender-skill gaps.** Whether a report's silence on damage magnitude
   / S-6 defender-skill implies "no intent" vs "not reached" was inferred from that report's
   structure. Only the named reports (Kimi on magnitude; Kimi + the design-stage block on
   defender-skill) made explicit claims.
7. **DEC-to-subject mapping.** The mapping of each Tiwas system to its DEC range follows the Alpha
   Corpus and decision register; where a system has no DEC (fear, magic, equipment, grapple,
   damage magnitude), the absence is noted rather than invented.
8. **Priority 1–9 collation.** The Priority 1–9 labels are a condensation of the reports'
   blocker corroboration; exact tier membership and ordering are this report's recommendation,
   not a source-stated fact.
9. **PDF non-access.** Every claim about the adventure's mechanics is second-hand via the reports;
   the PDF was not directly read here. This statement is itself a required caveat, not a guess.

---

## Closing advisory note

This is **NON-CANONICAL advisory material**. Agreement among LLMs — including unanimity on
"Playtestable Now" for the Core Test — does **not** create authority. Every design decision
(equipment, damage magnitude, defender-skill, skill-default, fear, magic scope, creature
authoring, combat-procedure scope) remains subject to Tiwa's governance through the repository's
formal path. Nothing in this report promotes, demotes, closes, or reopens any item, and no open
item (D1–D10) is silently resolved.