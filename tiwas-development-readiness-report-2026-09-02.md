---
document:
  title: "Tiwas TTRPG — Development Readiness Report: Beyond the Vale of Madness Benchmark and Missing System Design Decisions"
  version: "1.0"
  status: "NON-CANONICAL — advisory compilation only. Does not rule, promote, demote, lock, unlock, or close any open item. Agreement among reporting LLMs is diagnostic convergence, not design authority."
provenance:
  author_llm:
    name: "Muse Spark 1.1"
    version: "v1.1 (self-reported identity; not independently verified by platform metadata)"
  assessor_llm:
    name: "Inkling"
    version: "Arena.ai Agent Mode (no independently exposed model version identifier accessible to this session)"
  last_modified_by_llm:
    name: "Inkling"
    version: "Arena.ai Agent Mode"
  created_date: "2026-09-02"
  last_modified_date: "2026-09-02"
  identity_established: "self-reported (Muse Spark 1.1); session assistant (Inkling)"
---

# Standing-Prohibition Overrule — Required Log Entry

This file is a **dated, one-off, scoped exception** (2026-09-02) for internal development planning. It is **NOT** a reinstatement of any standing merge artifact, is **NOT** to be periodically regenerated, and future agents must **NOT** assume the prohibition against unscoped single-file compilation is generally lifted. The developer (Tiwa) explicitly authorized this one compilation for the purpose of identifying missing systems and deciding how to design them, based on the 25-report meta-analysis compiled 2026-09-02.

---

# Part A — Executive Summary and Governance Boundary

## A.1 What this file is and is not

- **What it is:** A single-file, advisory development-planning compilation assembled from the 25-LLM meta-analysis (`tiwas-adapt-vale-of-madness-reports-1-llm-attribution-2026-09-02.md`) and the Tiwas Alpha-Playtest Corpus (`Tiwas-Alpha-Playtest-Corpus-2026-09-01.md`, 2026-09-01). It identifies which Tiwas subsystems are ready, which are missing, which require adaptation mapping, which are blocked by design-stage dependencies, and what design decisions the developer must make to unblock full playtesting of *Beyond the Vale of Madness — GURPS*.
- **What it is NOT:** A ruling. It does not resolve, merge, or clean up any open fork. It does not promote or demote anything. It does not invent mechanics. It does not treat agreement among 25 reports as authority. It does not alter the Canonical/Locked, Non-canonical, Draft, or Open status of any DEC.

## A.2 Authority vocabulary (per `governance/status-model.md` and Alpha Corpus)

| Label used in this file | Meaning |
|---|---|
| **Canonical / Locked** | Authoritative, current, must not be contradicted (D1 self-declared). |
| **Non-canonical designer ruling** | Real designer decision about candidate/non-canonical material. Not Canonical. |
| **Draft pending Tiwa reconfirmation** | Source handoff file is a draft; DEC entry in live register is the operative register content. |
| **Open** | No settled decision exists. Not table-ready. |
| **Confirmed-closed** | Resolved via named DEC/ruling; listed so it is neither re-opened nor omitted. |
| **Playtestable Now** | Subsystem can be exercised in an alpha session without inventing new mechanics. |
| **Adaptation Mapping Required** | The Tiwas mechanism exists but must be mapped to the adventure's specific content. Not a system gap. |
| **Design-Stage Dependency** | Architecture or direction is ruled but concrete executable content/rules are missing. |
| **Missing Subsystem** | No adequate Tiwas mechanism currently exists (Reserved per DEC-015 or absent entirely). |
| **Adventure Content Only** | Setting, pathing, item identity, NPC name, treasure list — not a Tiwas mechanical gap. |

## A.3 Source boundary

Only the following sources were consulted:

| Source | Function |
|---|---|
| `tiwas-adapt-vale-of-madness-reports-1-llm-attribution-2026-09-02.md` | Primary 25-report meta-analysis corpus; attribution manifest; SHA-256 repair records; system-by-system comparison; disagreement register D1–D10; isolated findings |
| `Tiwas-Alpha-Playtest-Corpus-2026-09-01.md` | Tiwas baseline; authority/status boundaries; DEC-001 through DEC-077; Part A/B/C/D; standing-prohibition note |
| `Beyond-the-Vale-of-Madness-GURPS.md` (referenced but **not directly accessible**) | Adventure benchmark; contents inferred exclusively via the 25 reports' extractions |

**Note on missing source access:** The original `Beyond-the-Vale-of-Madness-GURPS.pdf` was not directly accessible during this session. Every adventure reference, paragraph number, mechanical requirement, and damage expression cited below is derived from the 25 reports' parsed extractions, not from direct source inspection. Any discrepancy between the reports' extractions and the original adventure text is preserved as a source-boundary limitation, not corrected.

---

# Part B — Collated System Readiness Assessment

This section mirrors the Alpha Corpus formal structure (DEC references, status tags, readiness classification, evidence, notes). Each subsystem block records: the DEC reference(s); the Tiwas baseline status; the 25 reports' convergence or divergence; the readiness classification; the blocking significance for this specific adventure; what design decision the developer must make; and any flag for reopening or further investigation.

---

## B.1 DEC-001 — d100 Resolution / Core Transaction (DEC-001–DEC-012)

**DEC reference:** DEC-001 (d100); DEC-002 (floor rounding); DEC-003 (24-attribute matrix); DEC-004 (derived statistics); DEC-005 (skills); DEC-006 (Core Test Transaction); DEC-007 / DEC-007.A (resource cost, overflow, overflow-immutability clause); DEC-008 (recovery); DEC-009 (failure XP); DEC-010 (skill roll pool); DEC-011 (general XP); DEC-012 (advanced skills).

**Tiwas baseline:** Canonical / Locked (Part A, Alpha Corpus).

**25-report convergence:** **Universal agreement** — all 25 reports treat the Core Transaction as Playtestable Now. No disagreement recorded. No design-stage dependency. No missing mechanism.

**Evidence (direct quotes, truncated per meta-analysis discipline):**

- ChatGPT 5.6-1: *"The Core is not the problem... A large proportion of the adventure's apparently disparate GURPS tests reduce cleanly to ordinary Tiwas Core Tests."*
- Claude 5 Sonnet: *"The Core Test Transaction (DEC-006), S-1 Opposed Contest, and the S-2/S-4 Location-Index + Wound chain already cover the structural demands of ordinary skill tests."*
- Kimi K3: *"Core Skill Resolution — Status: ✅ Playtestable Now. Blocking: None."*

**Readiness classification:** 🟢 **Playtestable Now** — Canonical / Locked, fully executable.

**Blocking significance for *Beyond the Vale of Madness*:** **None.** The adventure's exploration checks (Climbing, Search, Tracking, Lockpicking, Forced Entry, Survival, Merchant, First Aid, Will, DX-equivalent, Perception-equivalent, Tactics) can all be expressed as ordinary Core Tests once skill mappings are authored.

**Development decision needed:** **None at the mechanism level.** The adaptation content work (authoring Tiwas skills for named adventure tasks) is content authoring, not system design. The developer must decide whether to author a canonical skill list or treat adventure skills as Advanced Skills created during play — both are permitted by DEC-005/DEC-012.

**Flag / note:** DEC-007.A (overflow-immutability clause, 2026-09-01) explicitly states: *"No Tag, Trait, Effect, Condition, or subsystem may reduce, redirect, absorb, or otherwise modify Overflow's magnitude or application to HP."* This prevents any future Armor or Defense subsystem from reducing Overflow damage — a structural boundary that must be preserved in any future design (B.5, B.6).

**Guess flagged (see G.1):** None at the mechanism level.

---

## B.2 DEC-003 / DEC-004 — 24-Attribute Matrix and Derived Statistics

**DEC reference:** DEC-003; DEC-004.

**Tiwas baseline:** Canonical / Locked.

**25-report convergence:** **Universal agreement** — Playtestable Now. All reports note that mapping GURPS's 4 attributes (ST, DX, IQ, HT) to Tiwas's 24 attributes is adaptation content, not a system gap.

**Readiness classification:** 🟢 **Playtestable Now** — architecture complete; mapping is content.

**Development decision needed:** Author a mapping table showing how adventure tasks that reference GURPS ST/DX/IQ/HT map to appropriate Tiwas Body/Mind attribute groups. This is content, not mechanism design.

---

## B.3 DEC-013 — S-1 Universal Opposed Contest (DEC-013 + DEC-031 Quality tie-breaker addendum)

**DEC reference:** DEC-013 (Canonical / Locked, §A.13); DEC-031 (Non-canonical, Ruled — Quality gates eligible Effects per Option B, 2026-08-30).

**Tiwas baseline:** Canonical / Locked (DEC-013); Non-canonical Ruled (DEC-031).

**25-report convergence:** **Universal agreement** — Playtestable Now. The adventure's explicit Quick Contest (#44: Stealth vs Perception 12) is identified by all 25 reports as a direct test case for S-1.

**Evidence:**

- ChatGPT 5.6-1: *"The adventure contains a genuine opposed contest: Stealth vs Perception. That maps directly into S-1 without requiring a new contest engine."*
- ChatGPT 5.6-2: *"This is an important validation point: Beyond the Vale of Madness provides a real adventure use case for S-1 rather than a hypothetical laboratory case."*
- Claude 5 Sonnet: *"S-1 Universal Opposed Contest — Ready. Directly applicable to the adventure's Stealth vs. Perception Quick Contest."*

**Readiness classification:** 🟢 **Playtestable Now** — subsystem level.

**Blocking significance:** **Low for the stealth branch (#44).** The opposed contest itself works; the blocker is that the Ice Troll's Perception-equivalent Skill value is not authored (B.14, S-12 content gap).

**Development decision needed:** Select a Quality mode for the stealth contest (Margin for precision/stealth is the default recommendation per DEC-013). Author the Ice Troll's Skill value. These are content/adaptation decisions.

**Flag / note:** DEC-031's Option B (Quality gates eligible Effects) is a **Non-canonical designer ruling** (2026-08-30, 5/8 LLM survey support). It does not change the Canonical S-1 mechanism; it adds the Quality→Effect-tier gate. The developer may treat this as playtestable or may override it per situation; no authority is conferred by the survey result.

---

## B.4 DEC-014 — S-2 Zero-Step Location Index Provider (Tier-1)

**DEC reference:** DEC-014 (§A.14, Canonical / Locked — Tier-1 provider only); DEC-037 (Non-canonical, Ruled — non-attack provenance); DEC-039 (Non-canonical, Ruled — final roll governs for Extended Tests); DEC-041 (Non-canonical, Ruled — Skill-Tier-gated anatomical mapping, universal scope, corrected 2026-08-31); DEC-042 (Non-canonical, Ruled — Tier-2+ subdivision, Option B, secondary roll, no resource cost).

**Tiwas baseline:** DEC-014 Canonical / Locked (provider); DEC-037/039/041/042 Non-canonical Ruled (content/procedure).

**25-report convergence:** **Universal agreement** that Zero-Step (tens/units digit exchange) is Playtestable Now. Divergence on whether the full anatomical mapping is Playtestable or Design-Stage Dependency (see D8).

**Readiness classification:** 🟡 **Adaptation Mapping Required / Design-Stage Dependency** — the provider works; the anatomical mapping (DEC-041) and Tier-2 subdivision (DEC-042) are ruled but not fully content-complete.

**Blocking significance:** **Medium for combat.** The adventure's combat scenes (#17, #38) reference hit locations implicitly (armor coverage, Blood Seep's "average torso DR" and "least-protected area"). Without authored armor tags (B.5) and creature anatomy (B.14), the location system cannot be fully exercised.

**Development decision needed:**
- Confirm DEC-041's universal Skill-Tier-2+ gate (corrected 2026-08-31): only Skills at Tier 2 or above can trigger a Location Index for any location-referencing Effect (Wound, Trip, Disarm/Break Hold, Equipment Damage, Armor Bypass). Base/untrained skills (Tier 1) never trigger location for any of these Effects.
- Confirm DEC-042's Option B (secondary roll, no resource cost, not a Core Test) for Tier-2+ subdivision.
- Author the individual creature anatomy templates (DEC-041 point 5) — separate per creature type; content dependency on S-12.
- Note: DEC-014 §14.2 ("no player choice") and DEC-042's revoked Option A (player-choice subdivision) must be preserved — no player choice mechanism exists for location targeting.

**Flag / note:** DEC-041 (2026-08-31 correction) supersedes an earlier "Wound-only" drafting restriction. The Skill-Tier-2+ gate applies universally to all location-referencing Effects. This narrows DEC-028 (S-3 Tag+Location gating) by adding the Skill-Tier qualifier.

---

## B.5 DEC-023–DEC-030 — S-3 Effect Menu and Gating

**DEC reference:** DEC-023 (Effect menu structure — base tier: Inflict Injury HP-only + Open Retreat/Compel Yield; gated tiers: Position → Time/Action; Condition → Conditions; Equipment → Equipment; Defense → S-6; Location → S-2 promotion); DEC-024 (flat one-Effect-per-win); DEC-025 (Effect identity = pure declared intent, no Skill-side gating, formal tag system rejected); DEC-026 (second-Effect mechanism = different Advanced Skill, defender roll deferred until S-6 locks); DEC-027 (Effect application = auto-apply, gate checks evaluated once post-win); DEC-028 (State-3 triggering = combined Tag + Location gating for Disarm/Break Hold, Equipment Damage, Armor Bypass; narrowed by DEC-041); DEC-029 (S-3/S-4 boundary — prototype-only, no interface work yet); DEC-030 (partial Tag/Location match → fail-and-fall-back to Base Inflict Injury, full stop).

**Tiwas baseline:** All DEC-023 through DEC-030 are **Non-canonical designer rulings — Ruled** (recorded in `_consolidation/decision-register.md`, sources `investigations/tiwas-s3-designer-rulings-and-handoff-2026-08-29.md`).

**Critical caveat (verbatim from source):** The S-3 menu **structure** is Ruled. The **contents within the gated tiers** (the specific Effects populating Position, Condition, Equipment, Defense, and Location tiers) are **NOT fully enumerated** and remain an open tracking item (Part C.3 of Alpha Corpus). They are referenced, not resolved, by DEC-050 (B.6) and DEC-075 (Part C.2).

**25-report convergence:** **Universal agreement on architecture; significant divergence on blocking significance** (see D2 in C.2 below). Most reports classify the unenumerated gated-tier contents as a Critical blocker for the Blood Man encounter (grapple, ongoing corrosive damage, darkness conditions, fear). Some reports (Copilot family, DeepSeek-V3, RecallAI, Gemini family) treat base-tier Inflict Injury + Retreat/Compel Yield as sufficient for alpha play, making the gap a Design-Stage Dependency rather than a Missing Subsystem.

**Evidence:**

- ChatGPT 5.5-high: *"S-3's base-tier Inflict Injury and Retreat/Compel Yield are sufficient to model most of the adventure's combat outcomes... Needs development for some advanced combat effects."*
- Kimi K3: *"S-3 Base-Tier Damage Quantification — ⚠️ Design-Stage Dependency. Blocking: Critical. The base-tier Inflict Injury says 'HP-only' but does not specify how much HP damage is dealt."*
- Claude 5 Sonnet: *"S-3 Effect menu... Ready. Governs what a combat win accomplishes."*
- ChatGPT 5.6-2: *"The Tiwas system deliberately separates the mechanical skill architecture from adventure-specific skill/content authoring... Is that necessarily a missing subsystem? No."*

**Readiness classification:** 🟡 **Design-Stage Dependency** — architecture ruled; concrete effect payloads (damage magnitude, conditions, position, equipment interaction) missing.

**Blocking significance for adventure:** **Critical for Blood Man (#38)** — the encounter requires: grapple/hold condition; darkness condition; fear/terror condition; ongoing corrosive damage per time-step; tactical positioning effects; defense mitigation interaction. None of these are fully enumerated in the current gated-tier contents.

**Development decisions needed (no mechanics invented — design questions only):**

1. **Damage magnitude procedure:** How does a successful base-tier "Inflict Injury" translate to a numeric HP reduction? Is it derived from Skill quality? From the weapon's tag? From the attacker's attribute? From a fixed table? The adventure provides GURPS dice expressions (`1d-3`, `2d-2`, `1d-2`, `sw-2 cr`, etc.); Tiwas does not import these. The developer must decide whether to: (a) define a minimal damage-magnitude mapping for alpha play; (b) treat combat damage as GM-adjudicated narrative outcome for the alpha benchmark; or (c) design a formal damage-magnitude mechanism independent of Overflow.
2. **Condition tier contents:** What concrete Conditions exist? At minimum for this adventure: Darkness (attack penalty, vision); Grappled/Held (restricts actions); Wounded (mechanical consequence — but note OPEN-007 consequences are not table-ready); Frightened/Fear (will/resolution effect); Exhausted/Cold (resource/HP effect); Corrosive/Ongoing damage (per-interval effect over time). Each requires: trigger condition; effect payload; duration; removal/recovery method.
3. **Position tier contents:** What tactical position effects exist? At minimum: movement/repositioning; adjacency/reach; retreat/withdrawal; tactical starting position (the adventure provides hex maps for both combat scenes). These must be expressed as selectable Effects, not as separate tactical rules.
4. **Time/action economy interaction:** The Blood Man's "Blood Seep 1d-2 corrosive per second" and the Ice Troll's "Regeneration 1 HP/min only in freezing temperatures" require a time/action framework that is not yet defined (B.15, S-9/S-10/Time). This is a cross-cutting dependency.

**Flag / note (guess — see G.2):** The classification of this gap as "Critical blocker" vs "Design-Stage Dependency" depends on the developer's threshold — whether a GM can adjudicate combat narratively for alpha, or whether full mechanical expression is required before any combat playtest. This is an interpretive choice, not a Tiwas ruling.

---

## B.6 DEC-032–DEC-042 — S-4 Wound / Injury (DEC-032–DEC-036, DEC-041, DEC-042; DEC-037 at B.2; DEC-035 correction at B.4)

**DEC reference:** DEC-032 (Injury = HP damage; Wound = localized lasting numerical state); DEC-033 (Wound trigger: selectable Effect from successful S-1; "Wounded" Condition via S-3 Effect #2; narrowed by DEC-041's Skill-Tier ≥ 2 gate; Overflow never causes Wounds); DEC-034 (Track A/B sequential interaction from one hit); DEC-035 (corrected — severity from the S-3 gated Effect, not accumulated count; magnitudes may differ per wound: −1, −5, −30, −80, −100); DEC-036 (DEC-020 reopened — non-attack physical resolutions can produce Wounds via Effect + Location Index); DEC-041 (Skill-Tier-gated anatomical mapping, universal scope, corrected 2026-08-31); DEC-042 (Tier-2+ subdivision: Option B, secondary roll, no resource cost, not a Core Test, mismatch → DEC-030 fall-back).

**Critical open item (not table-ready):** **OPEN-007 — Wound consequences** are explicitly listed in Part C.4 of the Alpha Corpus as **Ruled (architecture) but NOT table-ready (contents)**. The individual mechanical penalties per magnitude, healing-cost scaling, and the "more wounds → faster game-over" relationship are documented but not executable.

**Tiwas baseline:** Non-canonical designer ruling — Ruled (DEC-032–DEC-036, DEC-041, DEC-042); Draft pending Tiwa reconfirmation (source handoff `tiwas-s7-s8-advisory-session-handoff-2026-09-01.md`); DEC entries are the operative register content per `_consolidation/decision-register.md`.

**25-report convergence:** **Universal agreement** on architecture; divergence on practical readiness (see D1 in C.2). Most reports (ChatGPT 5.2, 5.5-high, 5.6 series, Kimi K3, Claude 5 Sonnet) note that combat in the adventure requires damage magnitude (B.5) which feeds into S-4; without damage magnitude, the wound system cannot be fully exercised.

**Evidence:**

- Claude 5 Sonnet: *"DEC-035 (S-4, Ruled) — severity from the S-3 gated Effect, not accumulated count... Prior 'severity = accumulated numerical count' recording was an LLM misreading and is superseded."*
- Kimi K3: *"Wound consequence magnitudes, Condition-tier contents, environmental hazard rates — architecture locked but contents not table-ready."*
- ChatGPT 5.6-1: *"Wounds are tracked individually, each with its own numerical magnitude... OPEN-007 wound consequences remain not table-ready."*

**Readiness classification:** 🟡 **Design-Stage Dependency** — architecture ruled; magnitude mapping and consequence contents (OPEN-007) not table-ready.

**Blocking significance:** **Medium/High for the adventure.** The Blood Man encounter requires a "wounded" state (the victim must be wounded before being grappled for Blood Seep). Without the wound mechanism fully executable, the combat loop cannot be mechanically validated. However, the developer can use a provisional GM-adjudicated "wounded" label for alpha diagnostic purposes.

**Development decisions needed:**

1. **Confirm DEC-035 correction:** Wound severity derives from the S-3 gated Effect that creates it (e.g., "Serious Frost/Fire/Shock Wound" as a distinct Effect), not from an accumulated count of wounds. Each wound is tracked individually with its own magnitude.
2. **Confirm DEC-041 universal gate:** The Skill-Tier-2+ gate applies to all location-referencing Effects, not just wounds. This affects the adventure's untrained/default attempts (DEC-005): if a character attempts a skill at Tier 1 (base/untrained), no location-referencing Effect (including Wound) can trigger — full stop. The developer must decide whether to author Adventure-Specific Advanced Skills for tasks that require location-referencing outcomes (e.g., combat using untrained weapon skills).
3. **Confirm DEC-042 Option B:** Subdivision by secondary roll, no resource cost, not a Core Test. The secondary roll's mismatch resolves via DEC-030 (fall-back to Base Inflict Injury). This avoids inventing a new resolution mechanism.
4. **Design decision for OPEN-007:** The individual wound consequences (penalties per magnitude, scaling, recovery) remain unenumerated. The developer must decide whether to: (a) enumerate them now as a prerequisite for combat playtesting; (b) treat them as GM-adjudicated for alpha; or (c) defer OPEN-007 until after combat integration is settled.

**Flag / note (guess — see G.3):** The practical blocking significance depends on whether the developer requires full wound mechanics for the alpha benchmark or can proceed with provisional labels. This is an interpretive choice.

---

## B.7 DEC-058–DEC-062 — S-5 Armor (Tags/Traits Only)

**DEC reference:** DEC-058 (Tags/Traits architecture; no numeric soak; never modifies Overflow — confirms DEC-007.A corollary); DEC-059 (Bypass = relational property between specific Tag pairs; location-match required; inapplicable at Tier 0); DEC-060 (Sunder = Condition-tier Effect; addition model — adds "Sundered" Tag; permanent; resolved via ordinary Core Test; selectable; confirmed by OpenCode against DEC-023); DEC-061 (Armor resolves before Active Defense; sequence: auto-apply → Armor check → Active Defense mitigation; DEC-050 supersession: Tier-0 hits never forced to promote); DEC-062 (Armor coverage = location-bound; same individual-template anatomy as DEC-041; Zero-Step clause for Tier-0 Armor check — read-only, no promotion, discarded after check; Bypass inapplicable at Tier 0).

**Tiwas baseline:** Non-canonical designer ruling — Ruled (`investigations/tiwas-s5-armor-advisory-session-handoff-2026-09-01.md`); S5-C caveat preserved verbatim but superseded by DEC-060's confirmed menu placement.

**Critical corollary (DEC-058 + DEC-007.A):** Armor Tags **never** modify Overflow under any circumstance. This is not a new DEC; it is a direct structural consequence of the two existing rulings.

**25-report convergence:** **Universal agreement** on architecture; divergence on blocking significance (see D3 in C.2). Most reports note the absence of Armor Tag vocabulary (no starter vocabulary for armor items) as the practical blocker, not the architecture itself.

**Evidence:**

- ChatGPT 5.6-2: *"S-5 explicitly uses Tags/Traits only; no numeric soak pool... Readiness: Design-Stage Dependency / Not directly compatible [with GURPS DR import]."*
- Muse Spark 1.1-2: *"Architecture locked (DEC-058-062) but starter Tag vocabulary (e.g., DR 2 cold-only, Bypass relational pairs) not enumerated."*
- Claude 5 Sonnet: *"DEC-058 (S5-A, Ruled) — Armor is Tags/Traits only. Confirmed as actual ruling. No numeric durability/soak pool."*

**Readiness classification:** 🟡 **Design-Stage Dependency** — architecture ruled; content (Tag vocabulary, item tags, coverage templates) missing.

**Blocking significance:** **High for combat fidelity.** The adventure's Ice Troll (DR 2, cold-regeneration) and Blood Man (DR 1, homogeneous injury tolerance) require armor/natural defense representation. Without authored tags, the adventure's combat cannot be mechanically validated. However, the developer can proceed with a minimal alpha layer: define provisional Armor Tags for the two monsters and for PC soft armor, accepting that these are non-canonical content, not canonical rules.

**Development decisions needed:**

1. **Confirm DEC-058 corollary:** Armor never interacts with Overflow. Any future design proposal that attempts to use armor to reduce Overflow must be rejected at the governance level.
2. **Author starter Armor Tag vocabulary:** At minimum, define tags for: Soft Armor (basic), Hard Armor (advanced), Cold-Adapted Hide (Ice Troll — includes regeneration interaction), Homogeneous Injury Tolerance (Blood Man — affects wound/grapple interaction), Shield Tags (medium shield from #13; defense mapping to S-6). These are content, not mechanism.
3. **Confirm DEC-062 Zero-Step clause:** At Tier 0, struck location for Armor check uses the single-purpose Zero-Step read (tens/units exchange) from the natural roll — no new roll, no promotion, discarded immediately. This preserves DEC-040's universal Tier-0 default.
4. **Confirm DEC-060 confirmation:** Sunder's menu placement is confirmed by OpenCode against DEC-023 (`investigations/tiwas-s3-designer-rulings-and-handoff-2026-08-29.md`). The S5-C caveat preserved above is historical only; the operative placement is DEC-060.

---

## B.8 DEC-044–DEC-050 — S-6 Active Defense

**DEC reference:** DEC-044 (Active Defense architecture — defender rolls genuine Core Test; full PE/MP cost; full consequences); DEC-045 (defender rolls — defensive agency); DEC-046 (voluntary decline permitted — defender may accept incoming Effect as applied); DEC-047 (uncapped — no per-action limit; follow-up deferred: repeated Defense fatigue — non-blocking, closed by DEC-075 in Part C.2); DEC-048 (Model B — post-hoc mitigation; DEC-027 literal preservation; Effect auto-applies in every case; Defense only affects aftermath); DEC-049 (separate mitigation per Effect — each auto-applied Effect receives its own independent Active Defense roll; consistent with DEC-026's separate-opposed-roll mechanism); DEC-050 (Fork 1 — Universal eligibility, amended 2026-09-01, resolves OPEN-009; any auto-applied Effect, positive or negative, may be targeted; invocation remains voluntary, never automatic/mandatory).

**Tiwas baseline:** Non-canonical designer ruling — Ruled (DEC-044–DEC-050, recorded `investigations/tiwas-s6-defense-opening-brief-2026-08-31.md`); DEC-050 amendment (2026-09-01) resolves OPEN-009; DEC-075 (Part C.2) closes the fatigue follow-up.

**Critical note from source handoff (`investigations/tiwas-s6-s12-session-handoff-2026-09-01.md` §3.1):** The DEC-050 amendment extends scope to include positive/beneficial Effects. The invocation remains voluntary. This amendment supersedes any earlier interpretation that might have excluded positive Effects from defense eligibility.

**25-report convergence:** **Universal agreement** on architecture; divergence on practical combat readiness (see D4 in C.2). Most reports treat S-6 as Playtestable Now at the subsystem level but note that practical combat integration requires S-3 (B.5), S-4 (B.6), and S-12 (B.14) to be executable together.

**Evidence:**

- ChatGPT 5.6-1: *"S-6 is now ruled as: Active Defense; defender rolls; voluntary; uncapped; post-hoc mitigation; separate mitigation per Effect... Readiness: 🟢 Playtestable Now at subsystem level. Adaptation content still required."*
- Kimi K3: *"S-6 Active Defense — ⚠️ Design-Stage Dependency. Blocking: Medium. S-6 architecture is complete, but which skill or attribute the defender rolls is not specified."*
- Claude 5 Sonnet: *"DEC-044–DEC-050 (S-6, Non-canonical, Ruled)... Readiness: Playtestable Now for the mechanical resolution loop."*

**Readiness classification:** 🟢 **Playtestable Now (subsystem)** / 🟡 **Design-Stage Dependency (integrated combat)** — the architecture works; the integration with attack/effect/damage requires B.5, B.6, B.14.

**Development decisions needed:**

1. **Confirm DEC-048 Model B:** Active Defense never prevents application; it only mitigates the aftermath. This aligns with DEC-027's auto-apply principle. No mechanism is needed that allows a defender to "block" an attack before it applies.
2. **Confirm DEC-049 separate mitigation:** Each Effect from a single exchange gets its own Defense roll. This allows the defender to mitigate some effects while accepting others — a meaningful tactical choice.
3. **Confirm DEC-050 universal eligibility + voluntary invocation:** The defender may choose which Effects to mitigate. Positive Effects (e.g., healing, buffs) may also be targeted by defense (e.g., resisting a healing spell) — this is architecturally permitted, not an error.
4. **Confirm DEC-047 uncapped + DEC-075 closure:** There is no fatigue/exhaustion penalty for repeated defenses beyond the existing Cost/Overflow economy. No new subsystem is required. The follow-up is closed.
5. **Author defensive Skills:** Which Skill governs Active Defense for each adventure situation? The architecture allows any Skill; the developer must decide (e.g., Reflexes for dodging, Composure for resisting mental effects, Toughness for absorbing physical effects). This is content, not mechanism.

---

## B.9 DEC-052–DEC-057 — S-7 Incapacitation / Death

**DEC reference:** DEC-052 (HP = 0 → forced incapacitation, no roll — replaces earlier directional note; supersedes any "HP = 0 = death" assumption); DEC-053 (Wound/Incapacitation independence — Wounds do not feed incapacitation; supersedes prior Proposals/WIP §7 "serious localized injury may matter"); DEC-054 (Permanent loss: either all revival skill-tests failed with unlimited attempts and no cap, OR player voluntary choice while incapacitated); DEC-055 (Stabilization procedure — GM discretion on skill/attempts/pacing; discretion governs mechanics of attempts, NOT whether skill tests are used — that is fixed by DEC-054); DEC-056 (No interaction with S-11 healing/recovery); DEC-057 (S-2 non-attack reopening trigger closed — supersession of prior §7 line; session-level assessment, not formal DEC-037 re-verification).

**Critical source status note:** Source handoff `tiwas-s7-s8-advisory-session-handoff-2026-09-01.md` is **DRAFT pending Tiwa reconfirmation** per Alpha Corpus §B.7. The DEC entries (DEC-052–DEC-057) recorded in `_consolidation/decision-register.md` are the **operative register content** per the live register's last modification (2026-09-01) and Tiwa's confirmation to OpenCode. The draft status of the handoff file does not alter the operative DEC content; it is preserved for provenance only.

**Tiwas baseline:** Non-canonical designer ruling — Ruled (DEC entries operative; source handoff draft preserved).

**25-report convergence:** **Universal agreement** — Playtestable Now. All 25 reports treat HP = 0 forced incapacitation as usable. Most note that the adventure's narrative death/end conditions (#15, #17, #38, #52) align well with Tiwas's two-branch permanent-loss model.

**Evidence:**

- ChatGPT 5.5-high: *"HP = 0 forced incapacitation, no roll... Readiness: Playtestable Now."*
- Claude 5 Sonnet: *"S-7 Incapacitation/Death (DEC-052–057) — Ruled (register-operative, source handoff still draft per §B.7 caveat)."*

**Readiness classification:** 🟢 **Playtestable Now** — mechanism level; adaptation content (which skill for revival attempts) is GM discretion per DEC-055.

**Development decisions needed:**

1. **Confirm DEC-054 branch selection:** The developer must decide whether to treat adventure "instant death" endings as: (a) narrative outcomes (adventure content) that override Tiwas mechanics for the module; or (b) mechanical outcomes requiring failed revival attempts. The architecture supports both; the adventure's text often declares death directly (e.g., "If you died or fell unconscious, ends"). This is an adventure-design choice, not a Tiwas mechanism gap.
2. **Confirm DEC-055 discretion boundaries:** GM discretion covers which Skill is used for revival attempts, how many attempts are permitted, and the pacing. It does NOT cover whether skill tests are required — DEC-054 fixes that they are.

---

## B.10 DEC-063–DEC-066, DEC-043, DEC-051 — S-8 Difficulty and Third-Party Adjudication

**DEC reference:** DEC-063 (named tiers with fixed additive Skill-side modifiers — symmetric grades); DEC-064 (effective Skill drives success/fail check, Failure XP, Skill Roll Pool cascade entry — must be read with DEC-065); DEC-065 (Skill Roll Pool cascade cap = permanent Cap; earlier C1 revoked; preserves Invariant 10 exactly; no Invariant-level amendment required); DEC-066 (difficulty grades symmetric — bonuses and penalties, not penalty-only); DEC-043 (Third-party adjudication — full ordinary Core Test; default adjudication skill = same skill as contestants; binary outcome; inverted comparison — lower Failure Margin wins on adjudicator success, higher on failure; failed Double unlocks Advanced Skill; generalized to all mutual-failure contests); DEC-051 (Stakes Gate — **REJECTED** — supersedes Proposals/WIP §8; no pre-Core-Test skip filter; Roadmap Phase 6 scope narrowed; S-2/DEC-037 non-attack deferral reopening trigger removed).

**Critical cross-reference (DEC-064 + DEC-065):** These must be read together to preserve Invariant 10 exactly. DEC-064 establishes that the difficulty-modified (effective) Skill drives the Skill Roll Pool cascade entry. DEC-065 confirms that the cascade stops at the permanent Cap, with any remaining pool spilling to General XP. This combination produces a monotonically-increasing, never-decreasing progress mechanism (DEC-069, S-9 assessment) without creating a competing resource economy (DEC-069, no Invariant-17 violation).

**Tiwas baseline:** Non-canonical designer ruling — Ruled (`investigations/tiwas-s8-s9s10-s11-advisory-session-handoff-2026-09-01.md` §3.1).

**Critical open item (not mechanism — content):** The **actual numeric values** for the named difficulty tiers (Trivial, Easy, Standard, Hard, Extreme) are not supplied in the Alpha Corpus or in any DEC. This is a content gap, not a mechanism gap.

**25-report convergence:** **Universal agreement** on architecture; divergence on practical readiness (see D7 in C.2). Most reports note that the adventure's modifier-heavy checks (`+2` Lockpicking, `+3` Tracking, `-2` Fright, `-3` Climbing, `-5` Search default, `-8` untrained climbing, encumbrance penalties, darkness `-3` to attack) require the numeric modifier table to be authored before full playtest.

**Evidence:**

- ChatGPT 5.6-1: *"The function is available. What remains is the actual Tiwas difficulty-grade numerical table/interface needed to translate the adventure's explicit GURPS modifiers."*
- Claude 5 Sonnet: *"DEC-063/DEC-064/DEC-066 (S-8, Non-canonical, Ruled)... Readiness: Adaptation Mapping Required."*
- ChatGPT 5.5-high: *"Supplied corpus does not provide the actual fixed modifier table. Cannot consistently map GURPS numeric modifiers."*

**Readiness classification:** 🟡 **Adaptation Mapping Required** — architecture ruled; numeric modifier table is content that must be authored.

**Blocking significance:** **Medium** for full adventure playtest; **Low** for partial diagnostic play. The core tests can proceed without difficulty grades (using raw Skill); the adventure's modified checks cannot be fully validated without the table.

**Development decisions needed:**

1. **Confirm DEC-051 rejection:** No Stakes Gate mechanism exists. Every meaningful roll must be resolved by the Core Test. This aligns with the adventure's frequent checks (many rolls are required regardless of stakes).
2. **Confirm DEC-043 adjudication mechanism:** For any mutual-failure opposed contests not covered by the repeat mechanism (DEC-013 §13.5 — exact tie repeats), the third-party adjudicator uses the same Skill as the contestants, performs a full Core Test, and applies the binary/inverted-comparison outcome. This is a mechanism; it requires no new design work.
3. **Author the difficulty modifier table:** Define fixed additive modifiers for the named tiers. Must act on Skill side only (DEC-064/DEC-002). Must preserve symmetry (DEC-066). Must interact correctly with DEC-065's Cap-clamped cascade. Example design decision (not an invented rule — a proposal only): `Trivial = +10`, `Easy = +5`, `Standard = 0`, `Hard = -5`, `Extreme = -10`. Any numeric values are acceptable as long as they satisfy DEC-063/DEC-066.
4. **Confirm DEC-064/DEC-065 interaction:** The cascade stops at Cap; remainder spills to General XP. This must be preserved exactly — any proposal that allows Skill advancement past Cap via difficulty-modified cascade violates Invariant 10 and must be rejected.

---

## B.11 DEC-067–DEC-070 — S-9/S-10 Extended Tests

**DEC reference:** DEC-067 (Margin-accumulation — monotonically increasing progress total from successful intervals); DEC-068 (Neutral failure — failed intervals cost resources + generate Failure XP but do not reduce/reset progress); DEC-069 (Invariant-17 coherence assessment — no violation; no competing resource created; assessment covers A2+B1 only; does not generalize to other B-fork choices); DEC-070 (Completion target — GM discretion, per-instance, no formula, same pattern as DEC-055).

**DEC-039 reference (at B.2):** For Extended Tests that produce physical consequences, the final roll in the sequence governs the Location Index (DEC-039, Non-canonical, Ruled, 2026-08-31).

**Tiwas baseline:** Non-canonical designer ruling — Ruled (`investigations/tiwas-s8-s9s10-s11-advisory-session-handoff-2026-09-01.md` §3.2).

**25-report convergence:** **Universal agreement** — Playtestable Now. Most reports note that the adventure does not deeply require Extended Tests but could use them for digging (#10, #21) or healing sequences if the designer chooses.

**Readiness classification:** 🟢 **Playtestable Now (subsystem)** / 🟡 **Adaptation Mapping Required (adventure use)** — the mechanism exists; applying it to adventure sequences is a design/adaptation choice.

**Development decisions needed:**

1. Confirm DEC-069 assessment: No additional mechanism is needed to prevent Invariant-17 violation. The monotonic Margin-accumulation mechanism is structurally sound.
2. Confirm DEC-070 discretion pattern: The developer must set the target per Extended Test instance. There is no default formula; the developer may establish conventions for common scenarios (e.g., "digging through ice requires Margin 20").
3. Confirm DEC-039 application: For multi-interval physical efforts (e.g., prolonged digging that produces fall/hypothermia consequences), only the final interval's roll feeds Zero-Step for location/damage purposes.

---

## B.12 DEC-071–DEC-074 — S-11 Rest / Healing

**DEC reference:** DEC-071 (Rest/Healing = explicit Skill Test — full 9-step Core Test; not automatic/passive); DEC-072 (Wound magnitude penalizes healer's effective Skill — same mechanism pattern as DEC-064; Skill-side only); DEC-073 (S-11 IS an Extended Test instance — one Rest period = one interval; DEC-072 penalty applied; DEC-067/DEC-068 progress; DEC-070 target); DEC-074 (Healing target = GM discretion, no HP-deficit lock — same base DEC-070 pattern; no S-11-specific override).

**Critical cross-reference:** DEC-071/DEC-073 + DEC-067/DEC-068 + DEC-074 form a coherent subsystem: healing is an Extended Test where each interval is a full Core Test with a Skill-side penalty based on wound magnitude, progress accumulates monotonically, failures are neutral, and the target is GM-set.

**Critical source status note:** Same as B.9 — source handoff draft; DEC entries operative.

**25-report convergence:** **Universal agreement** — Playtestable Now at subsystem level. Most reports note that the adventure's immediate First Aid expectations (`#21 restores 1d-3 HP on success; 1 HP on failure`) do not map directly onto the Extended Test framework; this requires an adaptation decision.

**Evidence:**

- ChatGPT 5.6-1: *"The adventure's healing requirement is now directly testable against S-11. The GURPS 'restore 1d-3 HP / minimum 1' procedure itself should not be imported."*
- Claude 5 Sonnet: *"S-11 Rest/Healing — Ready. Applicable if the party rests mid-adventure."*

**Readiness classification:** 🟢 **Playtestable Now (subsystem)** / 🟡 **Adaptation Mapping Required (adventure-specific healing task)**.

**Development decisions needed:**

1. Confirm DEC-073 framing: Healing during rest is an Extended Test, not a single-roll HP restoration. The developer must decide whether to: (a) convert the adventure's immediate First Aid checks to full S-11 Extended Tests; (b) treat them as single Core Tests with a simplified outcome (e.g., "success = restore 1 HP; failure = restore 0"); or (c) define a minimal alpha-layer healing procedure that does not conflict with DEC-073.
2. Confirm DEC-074 discretion: The healing target is GM-set and is NOT locked to the HP deficit. The developer may choose HP deficit as a convention, but it is not mandatory.
3. Confirm DEC-072 interaction with DEC-064/DEC-065: The wound-magnitude penalty applies to the healer's effective Skill for the healing test; the cascade stops at Cap; remainder spills to General XP. This must be preserved.

---

## B.13 DEC-076 / DEC-077 — S-12 Creature / Campaign Content

**DEC reference:** DEC-076 (dual-mode fork — automated systems use full 24-attribute generation with same Core Test economy; tabletop/GM-run systems use abbreviated/simplified stat-block method with resolution defaulting to GM decision on system — supersedes earlier "GM-facing shortcut layer" draft); DEC-077 (content authoring path — actual creature templates via DEC-041 individual-template method; developed by Tiwa via playtesting; not drafted by advisory model).

**Critical caveat (verbatim, preserved for record):** The S5-C Sunder menu-placement caveat (`investigations/tiwas-s5-armor-advisory-session-handoff-2026-09-01.md` §4 Item C) states that OpenCode's live-repository confirmation was required. Per the live register (`_consolidation/decision-register.md`), DEC-060 records the placement as confirmed by OpenCode against DEC-023. The caveat is preserved above for provenance; the operative placement is DEC-060.

**Tiwas baseline:** Non-canonical designer ruling — Ruled (DEC-076/DEC-077); actual creature templates **Open / not table-ready** (Part C.1, Alpha Corpus).

**25-report convergence:** **Universal agreement** that S-12 content is missing. Divergence on whether this is a Missing Subsystem, Design-Stage Dependency, or pure Content-Authoring Dependency (see D5 in C.2). Most reports treat it as the single most common blocker for full adventure playtesting.

**Evidence:**

- ChatGPT 5.5-high: *"No creature stat blocks/templates... Critical blocker."*
- Copilot 1: *"Creature templates are a content-authoring track, not a settled mechanic... This is design work, but it does not require new mechanics."*
- Claude 5 Sonnet: *"S-12 creature templates — Adaptation Mapping Required (content), architecture Design-Stage. DEC-076/DEC-077 Ruled architecture; no actual templates authored."*
- Kimi K3: *"Monster Stat Blocks — 📋 Adventure Content Only. Blocking: None. Conversion is content work."* (Note: minority position; most reports treat S-12 as blocking.)

**Readiness classification:** 🔴 **Missing Content** — architecture Ruled (DEC-076/DEC-077); actual templates not authored.

**Blocking significance:** **Critical** for the Ice Troll (#17) and Blood Man (#38) encounters. The adventure requires at least two statted hostile monsters with tactical behavior, plus an injured hunter NPC (#37) that may be modeled mechanically or treated as narrative.

**Development decisions needed:**

1. **Confirm DEC-076 dual-mode selection:** The developer must decide whether to author full 24-attribute creature blocks (automated mode) or simplified tabletop stat blocks (abbreviated mode) for the adventure. The architecture permits both; there is no mechanism gap.
2. **Author the two monster templates:** Ice Troll (cold regeneration; DR/natural armor; claw/maw attacks; stealth/camouflage; tracking; morale/retreat at 0 HP; All-Out Attack option). Blood Man (night vision; homogeneous injury tolerance; claws; grapple → Blood Seep → ongoing corrosive damage; fright checks; darkness interaction; Injury Tolerance; Combat Reflexes; tactical starting positions). These are content, not mechanism.
3. **Confirm DEC-077 content path:** Templates must use DEC-041's individual-template anatomy (not a shared scheme). The developer must author anatomy for each creature type.
4. **Design decision for alpha benchmark:** The developer may proceed with provisional, GM-authored stat blocks that approximate the adventure's requirements without being canonical templates. This allows partial combat playtesting without completing S-12 content authoring. This approach is consistent with DEC-076's tabletop/GM-run mode.

---

## B.14 DEC-015 — Reserved Systems (Scope Statement)

**DEC reference:** DEC-015 (Reserved systems list: hit-location rules except Tier-1 Zero-Step; wound activation/severity; Outcome Effects; armor; active/passive defense; incapacitation; death; healing; Rest; equipment; encumbrance; conditions; environmental hazards; difficulty grades; task/stakes adjudication; Extended Tests; NPC construction; magic/special-ability implementation; GM procedure; campaign procedures; setting-specific content).

**Critical updates since DEC-015:** Several previously Reserved systems have been incorporated through formal governance (S-1 DEC-013 Canonical; S-2 DEC-014 Canonical; S-3 DEC-023–DEC-030 Ruled; S-4 DEC-032–DEC-042 Ruled; S-5 DEC-058–DEC-062 Ruled; S-6 DEC-044–DEC-050 Ruled; S-7 DEC-052–DEC-057 Ruled; S-8 DEC-063–DEC-066 Ruled; S-9/S-10 DEC-067–DEC-070 Ruled; S-11 DEC-071–DEC-074 Ruled; S-12 DEC-076/DEC-077 Ruled architecture, open content). DEC-015's Reserved classification remains valid for any system not separately incorporated.

**Remaining Reserved / Missing for this adventure (per DEC-015 and source reports):**

| System | Current status | Why it remains reserved/missing |
|---|---|---|
| Equipment / Weapons / Tools | Reserved / Missing Subsystem (DEC-015) | No item stat model, no weight/encumbrance, no weapon tags, no ranged combat, no light-source rules |
| Magic / Special Abilities | Reserved / Missing Subsystem (DEC-015) | No spell framework, no powerstone, no enchantment mechanism; architecture direction = Advanced Skills rather than competing core engine |
| Environmental Hazards (cold/hypothermia) | Reserved / Partial (DEC-037 acknowledges category; no resolution mechanics) | Systemic threat exemption exists (DEC-037); no fixed attritional mechanism; no temperature mechanics |
| Fatigue / Exhaustion (separate from PE) | Reserved / No separate subsystem | Physical Energy (DEC-004) serves as the resource; no GURPS-style FP economy; DEC-075 closes fatigue follow-up |
| Tactical Combat / Action Economy / Time | Reserved / Missing Subsystem | No turn structure, no movement/action sequencing, no initiative model; S-9/S-10 Extended Tests provide interval progress but not combat time |
| Economy / Currency / Treasure Valuation | Reserved / Adventure Content Only | No currency model; treasure tracking is narrative; advancement uses General XP (DEC-011) |
| Social Interaction / Reaction Modifiers | Reserved / Non-blocking for this adventure | Not invoked in adventure branches; Core Test + S-1 sufficient for minimal social checks |

---

# Part C — Named Disagreement Register (D1–D10 from Meta-Analysis)

This section preserves the 10 material disagreements identified in the meta-analysis (`tiwas-btvm-system-comparison-compiled1.md`, Part 4 — Named Disagreement Register). Each disagreement is preserved without silent reconciliation. The developer is not asked to resolve them here; they are preserved as advisory flags for future governance review.

---

## C.1 D1 — S-4 Wound / Injury: Sufficient for Playtesting?

**Question:** Does current S-4 provide sufficient mechanical consequence definition for Vale combat wounds, or does it require additional design before playtesting?

**Position A (higher blocker):** ChatGPT 5.2 R1, ChatGPT 5.5-high R1, Gemini 3.6 Flash R1/R2, Claude 5 Sonnet R1 — S-4's OPEN-007 consequences (individual penalties, magnitudes, healing scaling) are not table-ready; combat cannot be fully validated without them.

**Position B (lower blocker / architecture sufficient):** ChatGPT 5.6 R1/R2, Copilot R1/R2, Copilot 365 R1/R2, DeepSeek-V3 R1, Mimo 2.5 R1/R2, Perplexity R1/R2, glm-4.5-air R1 — The architecture (DEC-032–DEC-036, DEC-041, DEC-042) is sufficient for alpha diagnostic play; OPEN-007 is a separate design item that can be deferred.

**Nature:** Classification threshold — principle-level ruling vs quantified magnitude table.

**Consequence for developer:** Affects whether combat playtesting must wait for OPEN-007 enumeration, or whether provisional wound labels are sufficient for alpha.

**Resolution status:** **Unresolved — preserved as advisory disagreement.** Not decided by this report. The developer retains authority to choose the threshold.

---

## C.2 D2 — S-3 Gated-Tier Effect Contents: Block Playtest?

**Question:** Does missing enumeration of S-3 gated-tier Effect contents block Vale playtest, or can it be handled as narrative / GM adjudication for alpha?

**Position A (Critical / Major blocker):** ChatGPT 5.2 R1, ChatGPT 5.6 R1/R2, DeepSeek-V3 R1, Mimo 2.5 R1/R2, Perplexity R1/R2, Mistral R1, glm-4.5-air R1 — The unenumerated contents (fear, darkness, grapple, corrosive, position) are required for the Blood Man encounter and for combat fidelity.

**Position B (Playtestable Now / Design-Stage):** ChatGPT 5.5-high R1, Gemini 3.6 Flash R1/R2, Claude 5 Sonnet R1, Grok 4.6 R1, Kimi K3 R1, Muse Spark 1.1 R1/R2 — The base-tier Inflict Injury + Retreat/Compel Yield is sufficient for alpha; the gated contents can be added incrementally.

**Nature:** Threshold for "playtestable" — whether full-fidelity combat requires complete S-3 content or whether GM adjudication + base-tier is sufficient for a one-off alpha diagnostic.

**Consequence:** Defines first playtest scope — full-fidelity vs partial transactional Core Test playtest possible now.

**Resolution status:** **Unresolved — preserved.** The developer may proceed with either scope.

---

## C.3 D3 — S-5 Armor: Tag System Sufficient?

**Question:** Is S-5 Armor Tag system sufficient to model GURPS Armor (DR) for Vale combat, or does it require extension?

**Position A (Tag-based sufficient / Playtestable with content):** ChatGPT 5.6 R2, Gemini 3.6 Flash R2, Grok 4.6 R1, Kimi K3 R1 — The architecture is directionally appropriate; the gap is Tag vocabulary content, which is a content-authoring task.

**Position B (Not directly compatible / requires design):** ChatGPT 5.2 R1, DeepSeek-V3 R1, Muse Spark 1.1 R1/R2, RecallAI R1 — The GURPS DR model cannot be imported; the Tag-based approach requires a new design framework for representing protection values.

**Nature:** Whether the architecture's structural difference from GURPS DR is a functional improvement (requiring only content) or a fundamental gap (requiring mechanism design).

**Consequence:** Determines if Vale combat can proceed with provisional Tag vocabulary or requires a new armor mechanism.

**Resolution status:** **Unresolved — preserved.** The developer may treat this as a content gap (author provisional tags) or as a mechanism gap (design a numeric interaction model). Note: DEC-058 explicitly prohibits any mechanism that modifies Overflow; any design proposal must respect this.

---

## C.4 D4 — S-6 Defense: Playtestable or Design-Stage?

**Question:** Does S-6 Active Defense architecture support practical combat for this adventure, or does it require further design before combat playtesting?

**Position A (Design-Stage / needs skill mapping):** Kimi K3, ChatGPT 5.5-high R1, ChatGPT 5.6 R1/R2, Grok 4.6 R1/R2, Muse Spark 1.1 R1/R2, Mimo 2.5 R1/R2, Perplexity R1/R2 — Which Skill powers defense is unspecified; practical combat requires integration with S-3, S-4, S-5, S-12.

**Position B (Playtestable Now at subsystem level):** Copilot R1/R2, Copilot 365 R1/R2, RecallAI, DeepSeek-V3, Laguna S 2.1, Gemini 3.6 Flash R1/R2, Claude 5 Sonnet — The architecture is complete; defense works as a post-hoc mitigation mechanism.

**Nature:** Readiness classification divergence — architecture-complete vs practically-integrated.

**Consequence:** Affects whether defense can be tested independently of combat integration.

**Resolution status:** **Unresolved — preserved.** The developer may proceed with independent S-6 testing (using provisional defensive Skills) before integrating full combat.

---

## C.5 D5 — S-12 Creature Content: Hard Blocker or Content Work?

**Question:** Is missing S-12 a hard blocker or can NPC/creature stats be improvised via the 24-attribute matrix for Vale's limited bestiary?

**Position A (Critical / Missing Subsystem):** ChatGPT 5.2, ChatGPT 5.5-high, ChatGPT 5.6, Copilot 365, DeepSeek-V3, Grok 4.6-1/2, Muse Spark 1.1-1/2, Mimo 2.5-1/2, Perplexity 1/2, Mistral — The adventure requires specific monsters with specific abilities; improvised stat blocks are insufficient for mechanical validation.

**Position B (Content-Only / Adaptation Mapping):** Copilot 1, RecallAI, Kimi K3, Claude 5 Sonnet — DEC-076's dual-mode fork permits abbreviated tabletop stat blocks; the architecture is complete and the content work can proceed independently.

**Position C (Partial / Three-way split):** Laguna S 2.1, Mistral, Copilot families (intermediate positions — minimal stat blocks sufficient for alpha).

**Nature:** Whether S-12 is treated as a mechanism gap (requires new system) or a content gap (requires templates under existing DEC-076/DEC-077).

**Consequence:** Affects sequencing — whether S-12 content authoring must precede any combat playtest, or whether minimal provisional blocks allow concurrent testing.

**Resolution status:** **Unresolved — preserved.** The developer may choose either sequencing approach; DEC-076's tabletop mode explicitly supports provisional blocks.

---

## C.6 D6 — Magic: In-Scope or Avoidable?

**Question:** Are Vale's supernatural elements (Enfys Loom spellcaster, enchanted dagger, troll regeneration, blood man traits) required for the benchmark, or can they be excluded?

**Position A (Missing / Required if using pregen):** ChatGPT 5.6 R2, Mimo 2.5 R2, Perplexity 1/2, glm-4.5-air R1, DeepSeek-V3 R1 — The adventure includes a spellcaster pregen and magical items; if the full benchmark uses the pregen, magic is required.

**Position B (Avoidable / Optional):** ChatGPT 5.5-high R1, Claude 5 Sonnet R1, Gemini 3.6 Flash R1/R2, ChatGPT 5.2 R1, Muse Spark 1.1 R1/R2 — The adventure can be run with the non-magical pregen (King Coppertong) and without magical items; magic is optional.

**Position C (Effect framework sufficient):** Grok 4.6 R1, Kimi K3 R1, RecallAI R1, Laguna S 2.1 R1, Mistral R1 — Some magical effects could be expressed via the existing S-3 Effect framework without a dedicated magic subsystem.

**Nature:** Whether magic must be designed before the benchmark, or whether the benchmark can proceed without it.

**Consequence:** Affects Priority 8 placement; allows the developer to exclude magic from the initial playtest scope.

**Resolution status:** **Unresolved — preserved.** The developer may exclude magic from the initial benchmark scope (recommended) without closing the broader question.

---

## C.7 D7 — S-8 Difficulty: Ready for Environmental/Condition Challenges?

**Question:** Is S-8 Difficulty architecture sufficient to model the adventure's environmental challenges (darkness penalties, fright modifiers, cold exposure), or is it incomplete?

**Position A (Playtestable / Ready):** ChatGPT 5.5-high R1, Claude 5 Sonnet R1, Gemini 3.6 Flash R1, Grok 4.6 R1, Muse Spark 1.1 R1/R2 — The architecture (DEC-063–DEC-066) supports named tiers and symmetric modifiers; the missing piece is the numeric table, not the mechanism.

**Position B (Incomplete / Interface missing):** ChatGPT 5.2 R1, ChatGPT 5.6 R1/R2, Copilot R1/R2, Copilot 365 R1/R2, Perplexity R2 — Without the actual modifier values and without Condition-tier effects for darkness/fear, the adventure's environmental challenges cannot be fully modeled.

**Nature:** Readiness classification divergence for practical adventure use.

**Consequence:** Affects whether environmental and horror elements can be playtested with provisional modifier values.

**Resolution status:** **Unresolved — preserved.** The developer may proceed with provisional modifier values for alpha play (e.g., `Hard = -5`, `Extreme = -10`) without committing to canonical values.

---

## C.8 D8 — S-2 Location Index: Settled for Called Shots?

**Question:** Is the Location Index generation mechanism settled for the adventure's combat maneuvers (called shots, grapple locations, armor coverage checks)?

**Position A (Settled):** Claude 5 Sonnet R1, ChatGPT 5.5-high R1, Gemini 3.6 Flash R1 — DEC-014 (Canonical), DEC-041 (Ruled, 2026-08-31 correction — universal Skill-Tier-2+ gate), DEC-062 (Ruled — Zero-Step clause for Tier-0 armor) are sufficient.

**Position B (Open / Not fully executable):** ChatGPT 5.2 R1, DeepSeek-V3 R1, Mimo 2.5 R1, Perplexity R1 — The anatomical mapping numbers (DEC-041 point 4: "directional, not locked") and Tier-2 subdivision (DEC-042 Option B) require further confirmation before reliable combat location play.

**Nature:** Whether the confirmed-closed list (§C.4 of Alpha Corpus) includes sufficient content for combat, or whether additional design work remains.

**Consequence:** Affects whether called shots, grapple locations, and armor coverage checks can proceed reliably in combat playtesting.

**Resolution status:** **Unresolved — preserved.** Note: DEC-014 §14.2 explicitly states that no player-choice mechanism exists for targeting. Any proposal that introduces called-shot player choice must be treated as an optional-rule appendix, not as a correction to the Canonical provider.

---

## C.9 D9 — Fear / Terror: Condition Effect or S-8 Adjudication?

**Question:** Should GURPS Fright Checks (#38, #58) be modeled as S-3 Condition-tier Effects or as Core Test + S-8 adjudication?

**Position A (Condition-tier / Design-Stage):** ChatGPT 5.2 R1, ChatGPT 5.6 R1/R2, Claude 5 Sonnet R1, Gemini 3.6 Flash R2 — The adventure's graded Fright results require a Condition mechanism; the binary Will test (DEC-001) is insufficient.

**Position B (S-8 + Core Test / Playtestable):** ChatGPT 5.5-high R1, Grok 4.6 R1/R2, Muse Spark 1.1 R1/R2, Kimi K3 R1, RecallAI R1 — A binary success/failure on a Will/Resolve-equivalent Skill, with difficulty modifiers (DEC-063–DEC-066), can approximate Fright Checks for alpha play; graded results can be deferred.

**Nature:** Mechanism choice — dedicated Condition subsystem vs existing architecture with difficulty adjustments.

**Consequence:** Determines whether a new Condition-tier enumeration (for fear/terror) is required before the adventure can express its horror elements.

**Resolution status:** **Unresolved — preserved.** The developer may choose either approach for alpha; a dedicated fear Condition remains an open design item.

---

## C.10 D10 — Combat Maneuvers: Effect Translation or Dedicated Rules?

**Question:** Should GURPS combat maneuvers (All-Out Attack, tactical positioning, retreat, called shots) be translated through the S-3 Effect framework (Movement + Attack combinations) or require dedicated rules?

**Position A (Effect translation / Sufficient):** ChatGPT 5.6 R2, Gemini 3.6 Flash R2, Grok 4.6 R1, Claude 5 Sonnet R1 — The adventure's maneuvers (tactical positioning, All-Out Attack with no defense, retreat at 0 HP) can be expressed through existing S-3 base/gated Effects and DEC-046 (defense decline) without new rules.

**Position B (Dedicated rules / More granular):** Copilot R1/R2, Copilot 365 R1/R2, Perplexity R2, DeepSeek-V3 R1 — Some maneuvers (e.g., multi-attack sequences, precise tactical movement) may require dedicated procedural rules beyond the current Effect framework.

**Nature:** Translation granularity — whether the existing universal subsystem architecture is sufficient for tactical combat, or whether combat-specific rules are needed.

**Consequence:** Affects complexity and learning curve; affects whether combat can be tested with existing rules.

**Resolution status:** **Unresolved — preserved.** The developer may proceed with Effect-based combat for alpha; dedicated combat rules can be added incrementally.

---

# Part D — Development Priority Framework

This framework is derived directly from the 25 reports' convergence on what blocks full adventure playtest, ordered by the dependency chain exposed by *Beyond the Vale of Madness* itself. The framework is advisory; the developer retains full sequencing authority.

---

## D.1 Dependency Chain (derived from adventure path analysis)

The meta-analysis (`tiwas-btvm-system-comparison-compiled1.md`, §7.2–7.4) identifies the densest subsystem stress points by following the adventure's critical paths:

```
Core Transaction (DEC-001–012) — READY
    │
    ├── Ordinary Tests (DEC-006) — READY
    ├── S-1 Opposed (DEC-013) — READY
    ├── Difficulty (DEC-063–066) — READY (table missing)
    │
    └── COMBAT INTEGRATION (Critical Path)
             │
        ┌─────┼─────────┐
        ▼     ▼         ▼
     Effects  Defense  Damage / Wounds
     (B.5)    (B.8)    (B.6 / B.5)
        │       │          │
        └───────┼──────────┘
                ▼
           Grapple / Conditions
           (B.5 — gated contents open)
                │
                ▼
           Time / Action Economy
           (B.11 — Extended Tests / Time)
                │
         ┌──────┼──────────┐
         ▼      ▼          ▼
    Equipment  Magic     NPC/Creature
    (Reserved) (Reserved) (B.13 — content open)
         │       │          │
         └───────┼──────────┘
                 ▼
         Full Adventure Playtest
         (Blocked until above complete)
```

This dependency chain is not a proposal to change Tiwas architecture; it is the structure exposed by this benchmark.

---

## D.2 Prioritized Recommendations (Priority 1 – Priority 9)

Each priority includes: what it addresses; which DEC references apply; the 25-report consensus; the design decision required; whether mechanism design or content authoring; and the dependency relationship.

---

### Priority 1 — Combat Payload and Damage Magnitude (DEC-023 / DEC-024 / DEC-027 / DEC-028 / DEC-030 / DEC-032 / DEC-033 / DEC-034 / DEC-035)

**What it addresses:** The complete way to answer: "When an attack succeeds, what happens?" Includes: how much HP damage; how weapons/creature attacks are expressed; how armor reduces/redirects/blocks; how defense mitigates; how multiple effects per turn work; how wounds trigger; how ongoing damage operates over time.

**DEC references:** B.5 (DEC-023–DEC-030), B.6 (DEC-032–DEC-042), B.8 (DEC-044–DEC-050), B.4 (DEC-041 — Skill-Tier-2+ gate for location-referencing effects).

**25-report consensus:** **Universal agreement** that combat is the dominant blocker. Divergence on whether base-tier Inflict Injury is sufficient for alpha (D2 — preserved).

**Design decisions needed (no mechanisms invented):**
- How does a successful base-tier Inflict Injury translate to numeric HP damage? (Options: Skill-quality derived; weapon-tag derived; attacker-attribute derived; GM-adjudicated; minimal alpha mapping; formal mechanism design.)
- What concrete gated-tier Effects must exist at minimum for this adventure? (At minimum: Grappled/Held condition; Darkness/Visibility condition; Frightened/Fear condition; Wounded condition with magnitude; Corrosive/Ongoing damage per interval; Tactical Position/Movement effects.)
- How does the Blood Man's compound loop (Attack → Wound → Grapple → Ongoing Corrosive → Possible Death) resolve mechanically? The architecture permits sequential Effects (DEC-026: separate opposed rolls; DEC-034: sequential Track A/B; DEC-048/DEC-049: separate defense mitigation per effect). The developer must confirm that this compound loop is expressible without inventing new mechanisms.
- Confirm DEC-028's combined Tag + Location gating applies to all three effects (Disarm/Break Hold, Equipment Damage, Armor Bypass) with the Skill-Tier-2+ gate (DEC-041 correction). Confirm that partial match resolves via DEC-030 fall-back.

**Type:** Mechanism design for damage magnitude; content authoring for gated-tier Effects; integration design for compound combat loops.

**Dependency:** Unblocks Priority 3, 4, 5, 6, 7 (combat integration depends on damage magnitude + effects + defense + wounds + conditions).

---

### Priority 2 — Creature / NPC Content Authoring (DEC-076 / DEC-077 / DEC-041)

**What it addresses:** The Ice Troll (#17) and Blood Man (#38) stat blocks; the injured hunter NPC (#37); optional implied tundra wolves/grave ghouls.

**DEC references:** B.13 (DEC-076 — dual-mode fork; DEC-077 — content authoring path; DEC-041 — individual-template anatomy).

**25-report consensus:** **Universal agreement** on missing content. Divergence on blocking significance (D5 — preserved); DEC-076's tabletop/GM-run mode permits provisional abbreviated blocks.

**Design decisions needed:**
- Confirm DEC-076 mode selection: Use full 24-attribute automated mode or abbreviated tabletop mode for the two monsters? The architecture permits both.
- Author the two monster templates using DEC-041's individual-template anatomy (not a shared scheme). Each creature requires its own anatomical mapping.
- Confirm DEC-077 content path: Templates are developed through playtesting; advisory models do not draft them. The developer must author them.
- Confirm the adventure's creature traits (Regeneration, Regrowth, Night Vision, Fearlessness, Regeneration in cold only, Homogeneous Injury Tolerance, Combat Reflexes) are expressed as Tags/Traits or as special abilities — the mechanism for these traits is not fully defined (see Priority 4 — Magic/Traits).

**Type:** Content authoring (not mechanism design) — under DEC-076/DEC-077.

**Dependency:** Unblocks combat playtesting (Priority 1 requires statted opponents for validation). Can proceed concurrently with Priority 1.

---

### Priority 3 — Equipment, Weapons, Armor Tags, and Encumbrance (DEC-015 Reserved / DEC-058–DEC-062)

**What it addresses:** Weapons, armor, shields, tools, item weights, carrying capacity, encumbrance penalties, weapon prerequisites (ST 12 for mace), item permissions (dagger for lockpicking; rope/pitons for climbing; torch for darkness).

**DEC references:** B.5 (DEC-058–DEC-062); B.10 (DEC-015 — Reserved); DEC-007.A (overflow-immutability — armor never modifies overflow).

**25-report consensus:** **Universal agreement** — Reserved/Missing Subsystem. Divergence on blocking significance (D6 — preserved): Critical vs Medium vs Low.

**Design decisions needed:**
- Confirm DEC-058 architecture: Tags/Traits only; no numeric soak; no interaction with Overflow (DEC-007.A corollary preserved exactly).
- Author starter Armor Tag vocabulary (soft armor, hard armor, cold hide, homogeneous tolerance, shield tags, armor bypass pairs).
- Author weapon/equipment Tags: Antique Mace (ST requirement equivalent? — no mechanism exists; must be expressed as a Tag condition); Glass Dagger (Shatterproof enchantment — trait/magic tag); Crossbow (ranged — mechanism missing); Shield (defense interaction with S-6 — mechanism exists, content missing); Rope/Grapple (climbing tool); Pitons; Torch/Tinderbox (light source — mechanism missing for darkness interaction).
- Confirm encumbrance/load mechanism: DEC-015 reserves this; the adventure uses climbing penalties (`-1` per encumbrance level) and carrying capacity (`ST 14` for tapestry). The developer must decide whether to: (a) implement a minimal encumbrance model (load thresholds, penalties); (b) treat it as adventure-specific fiat; or (c) defer to a future equipment subsystem design.
- Confirm weapon prerequisites: The adventure uses GURPS ST requirements (`ST 12` for mace). Tiwas has no equivalent mechanism. The developer must decide whether to express this as: (a) a Skill-cap or Skill-starting-value condition; (b) an equipment Tag (cannot equip without sufficient attribute); or (c) a narrative gate.

**Type:** Mechanism design (encumbrance, prerequisites, item stats) + content authoring (Tag vocabulary).

**Dependency:** Unblocks exploration branch (#15 climbing with encumbrance; #51 tapestry carry limit; #35 rope/grapple use) and combat branch (#2 mace stats; #59 crossbow; #13 shield defense). Can proceed concurrently with Priority 1 and 2.

---

### Priority 4 — Environmental Hazards and Fatigue Mapping (DEC-037 / DEC-015 / DEC-052 / DEC-007.A)

**What it addresses:** Extreme cold/hypothermia (#19, #21); snow/ice digging (#10); cliff falls (#15, #52); slippery stairs (#25, #50); darkness/light source (#7, #38, #55); wind gust (#52); exhaustion/FP loss (#10, #19, #21); collapse/death at resource exhaustion.

**DEC references:** B.2 (DEC-037 — non-attack provenance; systemic exemption for extreme temperature; hazard win = failed test; direct HP/Conditions); B.9 (DEC-052–DEC-057 — incap/death; no separate fatigue mechanism); DEC-015 (Reserved — environmental hazards); DEC-007.A (overflow-immutability — any fatigue mechanism must not conflict).

**25-report consensus:** **Universal agreement** on missing mechanism. Divergence on blocking significance (D8 — preserved): Critical/High vs Playtestable Now via Core Test + DEC-037.

**Design decisions needed:**
- Confirm DEC-037 point (1) application: Failed governing Core Tests against environmental hazards supply the Zero-Step Location Index for physical consequences. This connects hazards to S-4 (wounds) and S-2 (location).
- Confirm DEC-037 point (3): Systemic threats (Extreme Temperature, Poison, Suffocation) apply direct HP/Conditions without a Location Index. Cold/hypothermia falls under this exemption.
- Confirm DEC-037 point (4) passive fallback: If a physical impact occurs with no roll (e.g., falling from a cliff without a test), a stub Location Index is output and deferred to DEC-041 anatomy naming. This affects fall damage (#15, #52, #55).
- Confirm DEC-052/DEC-053 interaction with fatigue: There is no separate fatigue mechanism. The developer must decide whether cold exposure reduces Physical Energy (DEC-004), produces direct HP damage (DEC-034 Track A), creates a Condition (DEC-023 gated tier — not enumerated), or operates as a GM-adjudicated hazard with a provisional procedure.
- Confirm the adventure's `FP = 0 → collapse/death` mechanism: Since Tiwas has no FP resource, the developer must map this to either: (a) Physical Energy depletion + Overflow → HP → incapacitation (DEC-052); (b) a Condition effect (`Exhausted` — gated tier, not enumerated); or (c) GM discretion per DEC-055 pattern.

**Type:** Mechanism design (environmental hazard resolution, temperature effects, exhaustion mapping) + content (hazard definitions, triggers, consequences).

**Dependency:** Affects exploration branches (#19 cold trek; #21 rescue/healing after cold damage; #52 wind/fall; #7 darkness; #55 pit jump). Can proceed independently but affects the adventure's survival theme significantly.

---

### Priority 5 — Difficulty Modifier Numeric Table (DEC-063–DEC-066)

**What it addresses:** The actual numeric values for named difficulty tiers; conversion policy from GURPS modifiers (`+2`, `+3`, `-2`, `-3`, `-5`, `-8`, etc.); default/untrained attempt policy.

**DEC references:** B.10 (DEC-063, DEC-064, DEC-065, DEC-066); B.3 (DEC-013 — S-1 quality selection); B.1 (DEC-006 — untrained Skill = 0, cost of first increase = 0, fails any positive Skill roll).

**25-report consensus:** **Universal agreement** — architecture ruled; table missing. Divergence on practical readiness (D7 — preserved): Playtestable vs Incomplete.

**Design decisions needed:**
- Confirm DEC-066 symmetry: Difficulty applies bonuses and penalties symmetrically.
- Confirm DEC-064/DEC-065 interaction: Difficulty-modified Skill drives success/fail, Failure XP, and Skill Roll Pool cascade entry; cascade stops at permanent Cap; remainder spills to General XP.
- Confirm DEC-063 tier naming: The developer may use any named tiers (e.g., Trivial/Easy/Standard/Hard/Extreme or GURPS-equivalent terms) as long as they have fixed additive modifiers.
- Confirm DEC-051 rejection: No Stakes Gate; every meaningful roll is resolved by the Core Test.
- Confirm DEC-043 adjudication mechanism (for mutual-failure contests not resolved by DEC-013's repeat rule): Full ordinary Core Test; default skill = contestants' skill; binary/inverted-comparison outcome; failed Double unlocks Advanced Skill.
- Author the modifier table (example design proposal — not invented mechanism, just a numerical assignment): Trivial `+10`; Easy `+5`; Standard `0`; Hard `-5`; Extreme `-10`. Any values are acceptable.
- Confirm untrained/default policy: DEC-005 allows Skills to start at 0. A Skill-0 test succeeds only on rolls `≤ 0`, which is impossible (DEC-001: d100 produces 1–100). A failed Skill-0 test thus always fails but grants Failure XP and may trigger Skill Roll Pool advancement (DEC-009/DEC-010: Skill at 0 has zero cost to increase to 1; any nonzero Failure XP raises it to at least 1). The developer must confirm whether the adventure's untrained defaults (`DX-5`, `IQ-4`, etc.) are expressed as: (a) Skill-0 attempts with difficulty penalties; (b) authored Tier-1 Advanced Skills for untrained attempts; or (c) GM discretion.

**Type:** Content authoring (modifier values, tier names, conversion policy, default policy).

**Dependency:** Unblocks full exploration path validation (many modified checks); supports combat difficulty adjustments; supports environmental challenge modeling.

---

### Priority 6 — Healing and First Aid Mapping (DEC-071–DEC-074 / DEC-067–DEC-070)

**What it addresses:** The adventure's First Aid/Physician checks (`#21`, `#37`) that restore HP; the immediate vs. extended nature of healing; the relationship to wounds and recovery.

**DEC references:** B.12 (DEC-071, DEC-072, DEC-073, DEC-074) + B.11 (DEC-067–DEC-070).

**25-report consensus:** **Universal agreement** — architecture ready; adventure-specific mapping needed.

**Design decisions needed:**
- Confirm DEC-073: Healing IS an Extended Test instance. The developer must decide whether to apply this to all First Aid checks or only to extended/rest scenarios.
- Confirm DEC-074: Completion target is GM discretion; no HP-deficit lock. The developer may choose to set targets based on wound magnitude or HP deficit as a convention.
- Confirm DEC-072 interaction: Wound magnitude penalizes the healer's effective Skill. If the adventure uses OPEN-007 wound consequences (not table-ready), the penalty mechanism is defined but the magnitude values are not.
- Confirm DEC-056 independence: Healing mechanics are independent from incapacitation/death mechanics. A character at HP 0 (incapacitated) can still receive healing attempts per DEC-054/DEC-071.
- Confirm DEC-011 interaction: Any remaining Skill Roll Pool from failed healing attempts spills to General XP; this is automatic per DEC-010/DEC-011.

**Type:** Mechanism confirmation (DEC-073/DEC-074 pattern already ruled) + content/convention (target values, application scope).

**Dependency:** Unblocks post-combat recovery paths (#21, #37); supports full adventure loop validation.

---

### Priority 7 — Conditions: Darkness, Fear, Grappled, Wounded, Hypothermia, Corrosive/Ongoing (DEC-023 Gated Tier — Contents Not Enumerated / DEC-035 / DEC-041 / DEC-050)

**What it addresses:** The concrete effects needed for the Blood Man encounter (grapple, darkness, fear, wound state, corrosive seep, tactical position, defense interaction) and for exploration conditions (hypothermia, darkness state flag, ambush state).

**DEC references:** B.5 (DEC-023 — gated tier structure; contents open; DEC-024 — one effect per win; DEC-025 — pure declared intent; DEC-026 — separate roll for second effect; DEC-027 — auto-apply; DEC-028 — combined Tag + Location gating, narrowed by DEC-041; DEC-030 — partial match fall-back); B.4 (DEC-035 — wound severity from gated effect); B.7 (DEC-052 — incapacitation independent from wounds); B.8 (DEC-050 — universal eligibility, amended 2026-09-01; positive effects defensible); B.10 (DEC-051 — Stakes Gate rejected — conditions are not exempt from rolls); Part C.3 (S-3 gated-tier contents explicitly NOT table-ready).

**Critical note:** The S-3 Condition tier exists structurally (DEC-023) but the specific Condition contents are not enumerated (Alpha Corpus Part C.3; DEC-050 amendment note; DEC-060 Sunder placement reference). This is not a mechanism gap — it is a content-enumeration gap. The mechanism for applying conditions exists: they are selectable Effects (DEC-025: pure declared intent; DEC-027: auto-apply; DEC-028/DEC-030: gating applies where relevant). The developer must enumerate the conditions.

**Design decisions needed (content enumeration — no mechanism invention):**
- Confirm the minimum condition set for alpha play (design proposal, not mechanism): Darkness; Grappled/Held; Wounded; Frightened; Exhausted/Cold-Exposed; Corrosive/Ongoing Damage (per-interval); Ambushed; Rescued (state flag). Each requires: trigger; payload; duration; removal/recovery.
- Confirm DEC-028's combined Tag + Location gating applies to any condition that references location or equipment (e.g., a "Sundered Armor" condition requires an Armor Tag + location match; a "Disarmed" condition requires weapon Tag + hand location).
- Confirm DEC-041's universal Skill-Tier-2+ gate applies to all location-referencing conditions (not just wounds).
- Confirm DEC-050 amendment: Positive conditions (e.g., a healing effect, a buff, a tactical advantage) may also be targeted by Active Defense — the defender may choose to mitigate them. This is permitted architecturally; it does not require a separate mechanism.
- Confirm DEC-024/DEC-026 interaction: If a player wants both a condition and an injury from one win, a second opposed roll with a different Advanced Skill is required. The defender receives a separate defense roll for each effect (DEC-049). This compound mechanism is architecturally supported.
- Confirm the adventure's darkness/vision interaction: The adventure applies `-3` to attacks in darkness unless Night Vision. This can be expressed as: (a) a Difficulty modifier (DEC-063); (b) a Condition effect (`Darkness` — penalties to attack skills); (c) a Trait/Tag (`Night Vision` — cancels the condition). The developer must decide which representation to use for alpha.

**Type:** Content enumeration (Condition definitions, triggers, payloads, durations) + mechanism confirmation (existing rules cover all interactions).

**Dependency:** Critical for full adventure playtest (Blood Man encounter requires all of these); can be addressed incrementally (prioritize Darkness, Grappled, Wounded, Corrosive for combat; Frightened and Cold for horror/survival).

---

### Priority 8 — Magic / Special Abilities / Traits (DEC-015 Reserved / DEC-005 / DEC-012 / DEC-028)

**What it addresses:** The Enfys Loom spellcaster pregen (#18–19); magical items (Shatterproof glass dagger #24; possible enchantments); creature special abilities (Regeneration, Night Vision, Regrowth, Homogeneous Injury Tolerance, Combat Reflexes, Fearlessness); character traits/advantages (Luck, Fit, Charisma, Magery, Bad Temper, etc.).

**DEC references:** B.14 (DEC-015 — Reserved; DEC-076/DEC-077 for creature traits); B.5 (DEC-025 — formal Skill-side tag system rejected for Effects; DEC-012 — Advanced Skills as mechanism for special abilities); B.10 (DEC-063–DEC-066 — difficulty for magical challenges).

**25-report consensus:** **Universal agreement** — Missing Subsystem. Divergence: Essential vs Optional (D6 — preserved). Most reports recommend excluding magic from initial benchmark scope (use King Coppertong pregen rather than Enfys Loom) without closing the broader design question.

**Design decisions needed:**
- Confirm DEC-015 reservation: Magic/special abilities remain Reserved. No mechanism is provided in the Alpha Corpus.
- Confirm architectural direction (per meta-analysis consensus): Magic is intended to emerge through Advanced Skills (DEC-012) rather than as a competing core engine. The developer must decide: (a) design a minimal magic framework now (as part of Priority 8); or (b) exclude magic from the initial benchmark; or (c) treat magical effects as provisional GM-adjudicated narrative outcomes for alpha.
- Confirm DEC-025 rejection of Skill-side formal tags: The decision to reject a formal Skill-side tag/category system (DEC-025) affects how magical skills would be categorized. The developer must confirm whether this rejection applies to all special abilities (including magic) or whether a separate framework is needed for abilities that do not fit the Skill structure.
- Confirm trait/advantage mechanism: The adventure's pregenerated characters include 30+ traits. There is no mechanism for representing these. The developer must decide: (a) design a Trait/Tag system; (b) express traits as Tags on skills/equipment; or (c) exclude traits from initial playtest.
- Confirm DEC-028 interaction: Some creature abilities (e.g., Night Vision — cancels darkness penalty; Regeneration — per-time-step HP restoration; Homogeneous Injury Tolerance — modifies wound/grapple interaction) interact with existing subsystems. The developer must confirm whether these are expressed as: (a) special Effects; (b) Tags on creature stat blocks; (c) Conditions; or (d) a new special-ability framework.

**Type:** Mechanism design (special ability framework, trait mechanism, magic framework) — significant; or exclusion from initial scope — recommended.

**Dependency:** Optional for initial benchmark. Affects use of Enfys pregen; affects creature fidelity; affects item enchantment mechanics.

---

### Priority 9 — Economy, Currency, Loot Conversion, Advancement Mapping (DEC-011 / DEC-015 / DEC-063)

**What it addresses:** The adventure's treasure table; monetary rewards (`$500` for rescue; character-point awards `+2` for success, `+1` for defeating monsters, `+1` for loot > $500); selling loot at end; economy continuity.

**DEC references:** B.18 (DEC-011 — General XP receives adventure/quest awards; cost of increase = current value; above-Cap advancement permitted); DEC-015 (Reserved — economy); DEC-063–DEC-066 (difficulty for merchant/appraisal tasks).

**25-report consensus:** **Universal agreement** — not a blocker for short-form diagnostic play; needed for campaign continuity. Divergence on blocking significance: Low for alpha; High for full adventure resolution (treasure valuation, reward conversion).

**Design decisions needed:**
- Confirm DEC-011 conversion: The adventure's "gain 2 characters [points]" is interpreted by most reports as "gain 2 character points" (likely GURPS terminology). The developer must confirm the conversion to General XP: e.g., `1 GURPS character point = X General XP`. This is a content/convention decision.
- Confirm economic mechanism: DEC-015 reserves economy. The developer must decide whether to: (a) implement a minimal currency/economy framework; (b) treat treasure values as abstract ratings for alpha; or (c) exclude economy from initial benchmark (recommended for Priority 1–8 focus).
- Confirm DEC-063 interaction: The Merchant skill check (`#23`) requires a difficulty grade and an outcome mapping (success = correct appraisal; failure = incorrect value). This is an adaptation content decision, not a mechanism gap.

**Type:** Content/convention (conversion rates, abstract ratings) — mechanism design only if full economy is desired.

**Dependency:** Non-blocking for combat/survival benchmark; required only for full adventure resolution including reward and advancement tracking.

---

# Part E — Playtest Readiness Verdict

---

## E.1 Overall Adventure Readiness

**Classification:** **Not Ready for Full Mechanically-Complete Playtest.**

**Evidence:** The adventure's complete mechanical envelope requires multiple systems that Tiwas does not yet provide in executable form. The 25 reports converge on this finding with only divergence on severity classification (D1–D10 — preserved, not reconciled).

**Specific blockers (highest impact, per 25-report consensus):**

| Blocker | DEC reference | Why it blocks | Priority |
|---|---|---|---|
| Combat integration (attack/damage/effect/magnitude loop) | B.5 (DEC-023–DEC-030) / B.6 (DEC-032–DEC-042) | Ice Troll (#17) and Blood Man (#38) cannot be resolved mechanically without damage magnitude, wound mechanics, and compound effect sequencing | 1 |
| Creature stat blocks | B.13 (DEC-076/DEC-077) / B.4 (DEC-041) | Monsters have no authored templates; individual anatomy not completed | 2 |
| Equipment / weapons / armor tags / encumbrance | B.14 (DEC-015 Reserved / DEC-058–DEC-062) | Adventure depends on mechanically meaningful equipment in nearly every path; armor interaction requires content vocabulary | 3 |
| Environmental hazards / cold / fatigue mapping | B.14 (DEC-037 / DEC-015 / DEC-052) | Survival theme requires cold/hypothermia/exhaustion mechanics; no resolution framework exists | 4 |
| Difficulty modifier numeric table | B.10 (DEC-063–DEC-066) | Adventure is modifier-heavy (`+2`, `+3`, `-3`, `-5`, `-8`, darkness `-3`); no executable values exist | 5 |
| Healing / First Aid mapping to S-11 Extended Test | B.12 (DEC-071–DEC-074) | Adventure expects immediate HP restoration; S-11 uses Extended Test with Margin accumulation | 6 |
| Condition tier contents (fear, darkness, grapple, ongoing damage) | B.5 (DEC-023 / Part C.3) / B.9 (DEC-052) / B.10 (DEC-051) | Blood Man encounter requires compound conditions; contents not enumerated | 7 |
| Magic / special abilities / traits (optional) | B.14 (DEC-015 / DEC-025 / DEC-012) | Enfys pregen and monster traits unsupported; can be excluded from initial scope | 8 |
| Economy / treasure / advancement conversion | B.9 (DEC-011 / DEC-015) | Not required for survival/combat benchmark; needed for full adventure resolution | 9 |

---

## E.2 Partial Diagnostic Readiness

**Classification:** **Partially Playtestable as Alpha Diagnostic.**

**Systems playable now (without invention):**

- Core Test Transaction (DEC-001–DEC-012) — all ordinary exploration checks.
- S-1 Opposed Contest (DEC-013) — stealth vs perception (#44) works with provisional NPC Skill values.
- S-7 Incapacitation/Death (DEC-052–DEC-057) — HP = 0 forced incapacitation; permanent loss by failed revival or voluntary choice.
- Difficulty architecture (DEC-063–DEC-066) — can proceed without numeric table (raw Skill checks) for partial testing.
- Extended Tests (DEC-067–DEC-070) — available if designer chooses to apply them to digging/healing.
- S-8 Difficulty (DEC-043, DEC-051) — adjudication mechanism available; Stakes Gate rejected.

**Diagnostic route that minimizes blockers (derived from meta-analysis §7.2):**

A low-combat, partial-diagnostic route that avoids the major combat/blocker clusters:

`#1 → #19 (cold/survival — tests Core + resource attrition) → #3 (courtyard exploration — search, lockpicking, forced entry) → #43 (search/perception — tests S-1 without combat dependency) → #14 (servant entrance — equipment interaction, trap/damage via DEC-037 non-attack provenance) → #33 (banquet hall — merchant appraisal, carrying capacity narrative) → #55 (pit jump — environmental hazard, DEC-037 direct damage) → #46 (corrosive injury — DEC-037 direct HP/Condition, no combat) → #53 (treasure/ending — adventure content only) → #60 (rewards — DEC-011 General XP, conversion decision needed)`

Even this route includes: cold exposure (DEC-037 — mechanism missing); jump/fall damage (DEC-037 — mechanism missing); corrosive injury (DEC-037 — mechanism missing); equipment/encumbrance interaction (DEC-058–DEC-062 — content missing). Therefore, a fully supported partial route is not yet achievable without either: (a) provisional GM adjudication for hazards; or (b) design decisions for environmental hazard mechanisms.

**Recommended alpha diagnostic approach:**
- Use the Core Test for all exploration and non-combat checks (DEC-006).
- Treat combat as GM-adjudicated narrative outcome (not mechanical) for initial diagnostic sessions.
- Use provisional difficulty modifiers (e.g., Hard = -5, Extreme = -10) without committing to canonical values.
- Author minimal creature stat blocks (DEC-076 tabletop mode) for the Ice Troll and Blood Man as content only, without requiring full S-12 framework completion.
- Author provisional Armor Tags and weapon Tags for alpha combat, accepting their non-canonical status.
- Log play observations against Part D (Playtest Report Template) of the Alpha Corpus.

---

## E.3 Canonical vs Non-Canonical Readiness (Summary)

| Layer | Readiness |
|---|---|
| Canonical Core (DEC-001–DEC-012) | 🟢 Strong — ready for task resolution |
| Non-canonical subsystems (DEC-013–DEC-077) | 🟡 Partial — architecture ruled; content/integration incomplete |
| Open / Reserved systems (DEC-015 exclusions) | 🔴 Missing — mechanism or content absent |

**Critical reminder:** "Playtestable Now" refers to the mechanism's availability under the Alpha Corpus's Non-canonical ruling framework. It does **not** mean Canonical. Any design decision arising from alpha play must be confirmed through Tiwa's established governance path (8-step Promotion Rule, REQ-021) before it becomes Canonical.

---

# Part F — Source Register and Evidence Discipline

---

## F.1 Source files actually consulted

| File path (workspace) | Source function | Access status |
|---|---|---|
| `/home/user/uploads/tiwas-btvm-system-comparison-compiled1.md` | Primary 25-report meta-analysis corpus; attribution manifest (with SHA-256 repair records for Copilot 1/2 and Copilot 365 1/2); Part 1 (System-by-System); Part 2 (D1–D10); Part 3 (Isolated Findings); Part 4 (Guesses); Part 5 (Governance) | Direct access — full text read |
| `/home/user/uploads/Tiwas-Alpha-Playtest-Corpus-2026-09-01.md` | Tiwas baseline; DEC-001 through DEC-077; Part A/B/C/D; status vocabulary; standing-prohibition overrule; confirmed-closed list (§C.4 / §3.9) | Direct access — full text read |
| `/home/user/uploads/` (directory listing) | Confirmed presence of both source files; no additional files present | Confirmed |
| `Beyond-the-Vale-of-Madness-GURPS.pdf` (referenced) | Adventure benchmark; not directly accessible; contents inferred exclusively via 25 reports' parsed extractions | **Inferred only — not directly inspected** |

---

## F.2 Attribution manifest reference (from meta-analysis source)

The meta-analysis source (`tiwas-adapt-vale-of-madness-reports-1-llm-attribution-2026-09-02.md`) records the following 25 reporting LLMs, with repaired attribution for Copilot and Copilot 365 (original duplicates repaired to `_1` files per SHA-256 repair record):

| LLM | Report number(s) | File reference (per attribution index) |
|---|---|---|
| ChatGPT 5.2 | 1 | `btvmadness-adapt-report-chatgpt-5-2-1.md` |
| ChatGPT 5.5-high | 1 | `btvmadness-adapt-report-chatgpt-5-5-high-1.md` |
| ChatGPT 5.6 | 1, 2 | `btvmadness-adapt-report-chatgpt-5-6-1.md`, `btvmadness-adapt-report-chatgpt-5-6-2.md` |
| Copilot | 1, 2 | `btvmadness-adapt-report-copilot-1_1.md`, `btvmadness-adapt-report-copilot-2_1.md` (repaired) |
| Copilot 365 | 1, 2 | `btvmadness-adapt-report-copilot365-1_1.md`, `btvmadness-adapt-report-copilot365-2_1.md` (repaired) |
| Claude 5 Sonnet | 1 | `Tiwas-Adventure-Readiness-Audit-Vale-of-Madness-2026-09-01.md` |
| DeepSeek-V3 | 1 | `btvmadness-adapt-report-deepseek-1.md` |
| Gemini 3.6 Flash | 1, 2 | `btvmadness-adapt-report-gemini-1.md`, `btvmadness-adapt-report-gemini-2.md` |
| glm-4.5-air | 1 | `Tiwas-Adventure-Readiness-Audit.md` |
| Grok 4.6 | 1, 2 | `btvmadness-adapt-report-grok-1.md`, `btvmadness-adapt-report-grok-2.md` |
| Kimi K3 | 1 | `btvmadness-adapt-report-kimi-1.md` |
| Laguna S 2.1 | 1 | Reference in meta-analysis index (not fully extracted in this session) |
| Mimo 2.5 | 1, 2 | `btvmadness-adapt-report-mimo-2-5-1.md`, `btvmadness-adapt-report-mimo-2-5-2.md` |
| Mistral | 1 | Reference in meta-analysis index |
| Muse Spark 1.1 | 1, 2 | `btvmadness-adapt-report-metaai-1.md`, `btvmadness-adapt-report-metaai-2.md` (producing LLM of meta-analysis; identity established by self-reported identity in meta-analysis provenance) |
| Perplexity | 1, 2 | `btvmadness-adapt-report-perplexity-1.md`, `btvmadness-adapt-report-perplexity-2.md` |
| RecallAI | 1 | `btvmadness-adapt-report-recallAI-1.md` |

**Note on missing provenance for some reports:** The meta-analysis source references reports by file names and LLM names but does not provide full content for all 25 reports within the compiled file (some are summarized rather than fully quoted). Where a report's content is summarized rather than quoted, the classification is derived from the meta-analysis's summary, not from direct inspection of the original report file. This is preserved as a source-boundary limitation (see G.4).

---

## F.3 Evidence discipline (per meta-analysis method)

Every significant claim about a subsystem's readiness, blocker significance, or design dependency is supported by at least one of:

- Direct DEC reference (DEC-XXX, Alpha Corpus or meta-analysis).
- Direct quote from a reporting LLM (truncated, with source file reference).
- Reference to the meta-analysis's system-by-system comparison table.
- Reference to the named disagreement register (D1–D10) where divergence exists.

No claim is made without source grounding. No mechanism is invented. No open item is silently closed. No agreement is converted into authority.

---

# Part G — Explicit Guesses, Assumptions, and Interpretive Flags

This section fulfills the prompt's requirement (success criterion 3; constraint: flag all guesses; Part G requirement). Every interpretation, inference, classification choice, or assumption made during compilation is listed here with its basis and confidence level.

---

## G.1 Section mapping (Part A–G) — Inferred from Alpha Corpus structure, not explicitly instructed

- **Assumption:** The formal documentation structure should mirror the Alpha Corpus (DEC-XXX sections, Part A/B/C/D, advisory markers, source pointers) and extend it with additional sections (Part E — Design Decisions, Part F — Source Register, Part G — Guesses) derived from the meta-analysis's own structure.
- **Basis:** The user's selected format (`format_guide` answer: `alpha_corpus_format`). The Alpha Corpus has Parts A–D; the meta-analysis adds comparison, disagreement, and isolated findings. Combining these structures is an interpretive choice.
- **Confidence:** High — the user's selection of "Alpha Corpus format" supports this mapping; the extension sections (E, F, G) are derived from the user's scope selection (`dev_priorities`) and the meta-analysis's own structure.
- **Flagged in report:** Yes (Part G header; this entry).

---

## G.2 Readiness classification thresholds — Interpretive choice from meta-analysis method (§2.5)

- **Assumption:** A disagreement is recorded only when two or more reports take materially different positions on a substantive question (readiness classification, blocking significance, architectural conclusion). Different wording expressing the same conclusion is not manufactured into disagreement.
- **Basis:** Meta-analysis method (§2.5: "A disagreement is recorded only when two or more reports take materially different positions on a substantive question").
- **Application:** D1–D10 are preserved exactly as recorded in the meta-analysis; no additional disagreements were manufactured; no complementary observations were split into false disagreements.
- **Flagged in report:** Yes (Part C — all D1–D10 include the nature of disagreement and resolution status).

---

## G.3 Blocker significance classification — Interpretive choice

- **Assumption:** The classification of a gap as "Critical blocker" vs "Medium blocker" vs "Low blocker" reflects the meta-analysis's own classification (derived from report consensus) rather than an independent assessment.
- **Basis:** The meta-analysis's Playtestability Matrix (§5.2) and Development Priorities (§9) provide explicit rankings; the 25 reports' convergence/divergence is preserved.
- **Specific interpretive choices flagged:**
  - Priority 1 (Combat) is ranked as the dominant blocker based on universal agreement across 25 reports; this is a compilation choice, not a Tiwas ruling.
  - Priority 8 (Magic) is ranked lower because the meta-analysis notes it is optional for the benchmark (use King Coppertong pregen); this reflects the source reports' consensus, not a design decision.
  - The dependency chain diagram (§D.1) is derived from the meta-analysis's path analysis (§7.1–7.4); it is not a Tiwas architecture proposal.
- **Flagged in report:** Yes (Part D — each priority notes "derived from 25-report consensus"; dependency chain header includes "not a proposal to change architecture").

---

## G.4 Missing source access — Confirmed limitation

- **Assumption:** `Beyond-the-Vale-of-Madness-GURPS.pdf` was not directly accessible; all adventure references are derived from the 25 reports' parsed extractions.
- **Evidence:** The file was listed as an attachment in the user's message (saved to `/home/user/uploads/`); the directory listing (`bash` command executed during analysis) confirmed the file's presence but the `read_file` tool did not return its content (only the `.md` files were directly readable). The meta-analysis source explicitly states it relies on the reports' extractions from the PDF.
- **Consequence:** Any discrepancy between the reports' extractions and the original adventure text is preserved as a source-boundary limitation, not corrected by this compilation.
- **Flagged in report:** Yes (§A.3 — Source Boundary; §F.1 — Source Register; §F.2 — Note on missing provenance for some reports).

---

## G.5 Mechanism invention prohibition — Confirmed compliance

- **Assumption:** No new Tiwas mechanics were invented in this report. Every mechanism referenced is either: (a) Canonical/Locked (DEC-001–DEC-016); (b) Non-canonical Ruled (DEC-023–DEC-077); or (c) Reserved/Open (DEC-015 exclusions, Part C open items).
- **Verification:** Each subsystem block (B.1–B.14) references DEC numbers; each design decision in Part E is framed as a question or proposal (not an invented mechanism); no mechanism text is provided; the Priority framework (Part D) is advisory sequencing.
- **Specific checks performed:**
  - No damage magnitude procedure invented (Priority 1 — design decision only).
  - No equipment stat model invented (Priority 3 — design decision + provisional content proposal only).
  - No condition definitions invented (Priority 7 — content enumeration proposed, not mechanism).
  - No magic framework invented (Priority 8 — excluded from initial scope per recommendation).
  - No fatigue mechanism invented (Priority 4 — mapped to existing DEC-004 Physical Energy + DEC-052/DEC-037; no new resource created).
- **Flagged in report:** Yes (§A.1 — "What it is NOT" includes "It does not invent mechanics"; Part E — every priority explicitly frames design decisions as questions/proposals, not mechanisms).

---

## G.6 Author/assessor identity — Confirmed from source attribution

- **Assumption:** The assessor/author field includes both the meta-analysis producing LLM (Muse Spark 1.1, v1.1, self-reported) and the current session assistant (Inkling, Arena.ai Agent Mode).
- **Evidence:** The meta-analysis source (`tiwas-adapt-vale-of-madness-reports-1-llm-attribution-2026-09-02.md`) records Muse Spark 1.1 as the producing LLM (self-reported identity). The user's answer (`author_identity` selection: `both_listed`) confirms both should be listed.
- **Limitations:** No independently verified platform-metadata mechanism was available to confirm either identity; the meta-analysis notes this explicitly (`SC-09`, `SC-10`, `SC-11`, `SC-12` in meta-analysis §9). The `identity_established` field is set to `self-reported` for Muse Spark 1.1 and `session-assistant` for Inkling.
- **Flagged in report:** Yes (Document metadata block; §F.2 — Attribution note; G.6 — this entry).

---

## G.7 No authority from agreement — Confirmed compliance

- **Assumption:** Agreement among 25 reports is presented as diagnostic convergence, not as a design ruling; conflicts (D1–D10) are preserved without reconciliation; no mechanism status is promoted/demoted/closed/reopened.
- **Verification:**
  - Each subsystem block notes the status tag (Canonical/Locked, Non-canonical Ruled, Open, Confirmed-closed) without alteration.
  - The disagreement register (Part C) preserves all 10 disagreements with unresolved status explicitly marked.
  - No mechanism status is changed (e.g., S-3 gated-tier contents remain "not fully enumerated"; OPEN-007 remains "not table-ready"; DEC-076/DEC-077 architecture remains Ruled but content remains Open).
  - The closing advisory note (§A.1; closing section) explicitly states that agreement does not confer authority.
- **Flagged in report:** Yes (throughout; explicitly in §A.1, closing advisory note, and D1–D10 resolution status columns).

---

## G.8 Non-canonical advisory status — Confirmed compliance

- **Assumption:** The entire document is marked as NON-CANONICAL advisory; no promotion/demotion occurs; no open item is silently closed; no Canonical rule is altered.
- **Verification:**
  - Document metadata (`status` field): `NON-CANONICAL — advisory compilation only`.
  - Standing-prohibition overrule (§1): Required log entry preserved.
  - Every DEC reference preserves its original status tag.
  - No mechanism text modifies any DEC.
  - No design proposal in Part E claims to be a ruling.
  - The final closing advisory note (after Part F) repeats the advisory status.
- **Flagged in report:** Yes (document header; §A.1; standing-prohibition overrule; closing advisory note).

---

# Closing Advisory Note

This report is a **dated, one-off, non-canonical advisory compilation** produced for internal development planning by the developer (Tiwa) on 2026-09-02. It does not alter the status of any Tiwas material. It does not invent mechanisms. It does not treat LLM agreement as authority. It does not close open items (S-3 gated-tier contents, OPEN-007 wound consequences, DEC-076/DEC-077 content, DEC-015 reserved systems). Any design decision arising from this report — particularly the mechanism design questions in Priority 1 (damage magnitude), Priority 3 (equipment/encumbrance), Priority 4 (environmental hazards/fatigue), Priority 7 (condition contents), and Priority 8 (magic/traits) — remains subject to Tiwa's governance authority and must pass through the established 8-step Promotion Rule (REQ-021 / Proposals/WIP §21) before acquiring Canonical status.

The meta-analysis's most valuable finding — preserved here without alteration — is that the adventure has moved Tiwas development from the question "Which RPG subsystems haven't we designed yet?" toward the more precise and actionable question: **"Which real play situations still force a Tiwas GM to invent a rule?"** The answer, derived from 25 independent assessments, is that combat integration, time/action sequencing, equipment/mechanics interaction, grappling/conditions, environmental hazards, and NPC content are the remaining practical blockers — not the Core resolution architecture, which the reports validate as mature and ready.

No mechanism has been promoted. No mechanism has been invented. No open item has been silently resolved. This file may be used as a reference for design sequencing, alpha playtest planning, and future governance review, but it confers no authority on any of its contents.

*End of advisory compilation — 2026-09-02.*
