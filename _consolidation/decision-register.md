---
document:
  title: "Decision Register"
  version: "1.0"
  status: "Consolidation working record (not canonical)"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
---

# Phase 2 — Decision Register

Every row below is a decision **as recorded in the source corpus**. This register does not itself make anything canonical — it classifies what kind of decision each item is, and where its authority currently sits, per the corpus's own self-declared status labels and cross-references. "Authority" in the rightmost column reflects what the corpus itself claims, not an external ruling by this consolidation.

## A. Canonical decisions (locked game mechanics — Document Status: Canonical Source of Truth)

| ID | Subject | Decision | Evidence (source) | Authority | Status |
|---|---|---|---|---|---|
| DEC-001 | d100 core mechanic | Roll-under resolution on 1–100; `00` = 100; 100 always fails and always qualifies as a failed Double | D1 §2.1–§2.4 | Canonical / Locked | Current |
| DEC-002 | Rounding | All fractional calculations floor, no exceptions | D1 §2.5 | Canonical / Locked | Current |
| DEC-003 | Attribute matrix | 24 independently generated attributes (12 Body / 12 Mind), each 1d100 | D1 §3 | Canonical / Locked | Current |
| DEC-004 | Derived statistics | HP, MP, Physical Energy, Speed, Energy Regen, MP Regen, Movement Speed formulas; live-recalculation rule | D1 §4 | Canonical / Locked | Current |
| DEC-005 | Skill Tier/Cap/Starting Value | Cap = floored average of Tier attributes; Starting Value = floor(Cap/2) | D1 §5 | Canonical / Locked | Current |
| DEC-006 | Core Test Transaction | Fixed 9-step transaction (roll → outcome → cost → overflow → failure XP → doubles → recovery); no subsystem may replace it | D1 §6, reinforced by D1 §16 invariants 17–18 and D2 §2 | Canonical / Locked | Current |
| DEC-007 | Resource cost & Overflow | Cost = natural roll; insufficient resource → Overflow → direct HP damage; no second resource pool | D1 §7 | Canonical / Locked | Current |
| DEC-008 | Recovery | floor(Regen/2), clamped, always final step, unconditional | D1 §8 | Canonical / Locked | Current |
| DEC-009 | Failure XP | max(0, Roll − Skill) | D1 §9 | Canonical / Locked | Current |
| DEC-010 | Skill Roll Pool | Temporary, single-test-scoped; cascading increases while affordable; capped at Skill Cap; remainder → General XP | D1 §10 | Canonical / Locked | Current |
| DEC-011 | General XP | May exceed Cap; cost of +1 = current value; no partial advancement | D1 §11 | Canonical / Locked | Current |
| DEC-012 | Advanced Skills | Created only by a qualifying failed Double; Tier+1; full-formula Cap recompute; lineage-based resource domain | D1 §12 | Canonical / Locked | Current |
| DEC-013 | S-1 Opposed Contest | Universal opposed-contest primitive; outcome matrix; Margin/Blackjack/Hybrid Quality measures; Failure/Failure repeat; exact-tie repeat | D1 §13, confirmed complete/locked at D2 §8 | Canonical / Locked | Current |
| DEC-014 | S-2 Tier-1 Location Index provider (Zero-Step) | Deterministic tens/units-digit exchange on the natural attacking roll; no player choice; read-only post-process; does not alter Core Test consequences | D1 §14.1–§14.2 | **Canonical / Locked — but explicitly limited in scope** (D1 §14 header: "limited S-2 decision") | Current |
| DEC-015 | Reserved Systems list | Everything not explicitly locked (hit-location beyond Tier-1, wounds, Effects, armor, defense, incapacitation, death, healing, Rest, equipment, etc.) remains outside the locked Core | D1 §15 | Canonical (a locked *scope* statement, not a locked mechanic for those subsystems) | Current |
| DEC-016 | Core Architectural Invariants | 18 invariants binding on all future subsystem work | D1 §16 | Canonical / Locked | Current |

**Note on DEC-014's scope:** D1 §14.3 is explicit that this locks *only* the Tier-1 Location Index provider — not whether/when a scene uses Tier 0/1/2, not anatomical mapping, not wound/armor/defense interaction, not whether any later rule may consume a Location Index. Treating DEC-014 as settling any of those adjacent questions would be an unsupported inference; this register deliberately does not do so.

## B. Non-canonical designer rulings (real decisions, but recorded outside Canonical Rules — Document Status: Non-Canonical)

These are genuine "designer ruling" evidence-class items per the corpus's own evidence-class vocabulary (D2 §23.2 / D3 §0), not LLM recommendations. They are decisions **about candidate/non-canonical material**. Per D3 §21 (Promotion Rule) and the governing consolidation specification, none of these become Canonical without the full 8-step promotion process, which the corpus gives no evidence of having been run for any of them.

| ID | Subject | Decision | Evidence (source) | Authority | Status |
|---|---|---|---|---|---|
| DEC-017 | S-2 attack-side invocation/warrant policy | Candidate four-state model + Named-Outcome Test accepted as "current non-canonical working direction" for when a Location Index is warranted (attack-side only) | D3 §2.1A, §23 (v1.4.2 revision record); full model in D4 §2–§6 | Non-canonical designer ruling ("Accepted ... for further development/testing", D4 header) | Current (accepted candidate, not locked) |
| DEC-018 | Explicit-only objectives | GM does not infer an unstated distinct objective from location/fictional context alone; only stated objectives are Warrant-eligible | D3 §2.1A "Designer rulings adopted"; D4 §5 table and §8 item 1 ("RULED — Explicit-only") | Non-canonical designer ruling | Current, folded into DEC-017's policy |
| DEC-019 | Structural Weak Points reclassified State 1 → State 2 | Anchored but not yet resolvable (no settled Location Index→component mapping); zero State-1/Active cache entries currently exist | D3 §23 (2nd correction round); D4 correction #4, §4/§6, §8 item 7 ("RULED") | Non-canonical designer ruling | Current |
| DEC-020 | S-2 non-attack Location Index source — categorical deferral | Non-attack physical resolutions (falls, hazards, structural collapses) generate **no** Tier-1 Location Index under current design, regardless of GM framing, stated stakes, or whether a governing Core Test exists — a deferral, not a claim of impossibility | D3 §2.5A (authoritative non-canonical location, per D3's own header); D5 §1 (fullest record); D2 §9 (implementation-relevant summary) | Non-canonical designer ruling, explicitly "Binding" per D5's own section header | Current — closed as a deferral, reopenable |
| DEC-021 | S-2 non-attack deferral — rejected alternative | "GM-authored hazard warrant" (Direction 1) rejected for now, not deleted from the record | D3 §2.5A investigation-record table; D5 §3 | Non-canonical designer ruling (rejection, not adoption) | Current |
| DEC-022 | H0 provenance rule and riders | Retained as an *inert* candidate record for the non-attack question if/when reopened — explicitly **not** validated as an operative rule | D5 §1, §3 | Non-canonical; explicitly not an operative decision | Inert / dormant |

## C. Explicitly unresolved (no decision exists — recorded here so it is not mistaken for one)

| ID | Subject | What the corpus says | Evidence |
|---|---|---|---|
| OPEN-001 | H0 Rider B's two sub-options | Identified but "never adjudicated against each other" | D5 §3 |
| OPEN-002 | Scene/campaign Location Tier selection (0 vs 1 vs 2) | Explicitly stated as **not** narrowed or resolved by DEC-017/DEC-014 | D3 §2.5, §2.3; D4 "Architectural constraint" note at top of §2 |
| OPEN-003 | Anatomical mapping (Location Index → body/structural component) | Explicitly open, "untouched" by any investigation | D3 §2.5; D4 §4 note; D1 §14.3 |
| OPEN-004 | Tier-2 procedure/cost | Explicitly open | D1 §14.3; D3 §2.3, §2.5 |
| OPEN-005 | S-3–S-12 subsystem content (Outcome Effects, Wounds, Armor, Defense, Incapacitation/Death, Difficulty/Stakes, Extended Tests, Conditions, Tags, Time, Equipment, Rest/Healing, Magic, NPCs, Setting Interface) | All explicitly "Open" / "Reserved" / "Proposed" — no locked mechanic for any of them | D1 §15; D3 §3–§17, §20 register |

## D. S-3 Outcome Effects — session designer rulings (non-canonical)

Recorded 2026-08-29 in the S-3 design thread. These are **real human/designer rulings** given in-session about candidate, non-canonical S-3 material, documented in `tiwas-s3-designer-rulings-and-handoff-2026-08-29.md` (rev. 1; authored by Claude Sonnet 5, assessed/reviewed by opencode/big-pickle) and in the subsequent per-decision handoff reports (dec025, dec026, dec027). Consistent with Sections A–C and the governance note below, recording a ruling here does **not** make it Canonical: any promotion still requires the full 8-step Promotion Rule (REQ-021 / Proposals/WIP §21). **All eight S-3 session decisions (DEC-023…DEC-030) are now Ruled (non-canonical).** The `investigations/tiwas-s3-effect-identity-and-multi-effect-opposition-investigation-v0.1-open.md` thread is **Closed** — no open forks remain in it.

| ID | Subject | Decision / State | Evidence (source) | Authority | Status |
|---|---|---|---|---|---|
| DEC-023 | S-3 Effect menu structure (Q-S3-1) | **RULED — Tiered Effect menu**: base tier = Inflict Injury (HP-only) + Open Retreat/Compel Yield; five gated tiers (Position → Time/Action; Condition → Conditions; Equipment → Equipment; Defense → S-6; Location → S-2 invocation promotion). **Disarm/Break Hold** placed via Q-S3-3's combined Tag+Location gating | In-session human ruling, 2026-08-29; handoff rev.1 | Non-canonical designer ruling | Ruled; Disarm/Break Hold placement finalised via DEC-028 |
| DEC-024 | S-3 Effect purchasing / multiplicity (Q-S3-2) | **RULED — Flat one-Effect-per-win.** No Quality-based scaling, no purchasing of additional Effects off a single win. A second/additional Effect requires a **separate opposed roll** — mechanism not yet designed; deferred | In-session human ruling, 2026-08-29; handoff rev.1 | Non-canonical designer ruling | Ruled; mechanism deferred to new thread |
| DEC-025 | S-3 Effect naming/identity gating (Q-S3-2a) | **RULED — Pure declared intent (no Skill-side gating).** Effects are granted solely by the declared outcome of a successful S-1 contest (subject to the other gates already ruled: gear/ability Tag + Location Index where required, DEC-028). The Skill name carries no mechanical weight and does not entitle or gate any Effect; a formal tag/category system on Advanced Skills is **rejected** (designer rationale: formal tags are exploitable and would push players to limit Skill choices to degenerate mechanical Effects). Reinforces Canonical §12.3; no Skill-side tag data introduced; REQ-017 satisfied | In-session human ruling, 2026-08-29 (per dec025 handoff report) | Non-canonical designer ruling | Ruled |
| DEC-026 | Second-Effect opposed-roll mechanism (Q-S3-2b) | **RULED — Different Advanced Skill; defensive roll deferred.** The separate opposed roll for any Effect beyond the single free one (DEC-024) uses a **different Advanced Skill** domain-appropriate to the declared second Effect; the actor accepts the risk of the additional roll. The full 9-step Core Test Transaction applies (REQ-018). The target receives **no defensive roll until S-6 locks**; any provisional resistance used in the interim is non-canonical scaffolding to be discarded when S-6 locks. Same-Skill and flat-check options rejected. No residual Advantage/Margin/state carries from the first contest | In-session human ruling, 2026-08-29 (per dec026 handoff report) | Non-canonical designer ruling | Ruled |
| DEC-027 | Effect application — auto vs contested (Q-S3-5) | **RULED — Auto-apply.** Winning S-1 with a declared Effect applies it directly; no secondary application contest is required. Gate checks (Tag + Location Index where required, DEC-028; fail-and-fall-back per DEC-030) remain in force and are evaluated once, post-win. Contested application is **rejected as the S-3 default**; S-6 (Defense) may later introduce Tags/equipment that counter or prevent specific Effects after auto-apply (e.g., locked gauntlets prevent Disarm), and any contested-application mechanic is deferred to S-6 as an optional modifier, not an S-3 default | In-session human ruling, 2026-08-29 (per dec027 handoff report) | Non-canonical designer ruling | Ruled |
| DEC-028 | State-3 Effect triggering — location+tag gating (Q-S3-3) | **RULED — Combined Location + Tag gating** for the three in-scope S-3 Effects (**Disarm/Break Hold, Equipment Damage, Armor Bypass**): trigger requires both a matching gear/ability Tag **and** a supporting Zero-Step Location Index (Tier 1+). **Function Impairment and Incapacitation deferred OUT of S-3 scope** (Flagged: Incapacitation → S-7; Function Impairment → S-4/Condition). Dependencies: Tags subsystem starter vocabulary (§11); anatomical mapping table (canonical §14.3, unbuilt); S-2 invocation policy (§2.1A) unaffected | In-session human ruling, 2026-08-29; handoff rev.1 (narrowed on review) | Non-canonical designer ruling | Ruled; 2 concepts deferred out of S-3 |
| DEC-029 | S-3/S-4 boundary (Q-S3-4) | **RULED — confirmed prototype-only; no S-3/S-4 interface work needed yet** (base-tier Injury is HP-only, no wound produced). Roadmap §10 boundary holds, dormant until a wound-producing Effect is proposed. S-4 *direction* (location-based injury from repeated hits; no Location Index → no Injury, full stop; per-location hit-history by GM adjudication; healing open) recorded as a **steer for a future S-4 investigation, not an S-3 ruling, not Canonical** | In-session human ruling, 2026-08-29; handoff rev.1 | Non-canonical designer ruling (boundary) + recorded S-4 direction (non-ruling) | Ruled; S-4 direction non-binding |
| DEC-030 | Partial Tag/Location match (Q-S3-3a) | **RULED — Fail-and-fall-back (Option A).** On a partial Tag/Location match for any Tag+Location-gated Effect (Disarm/Break Hold, Equipment Damage, Armor Bypass), the declared Effect fails entirely; the successful S-1 contest instead applies the Base-tier Effect Inflict Injury (HP-only form). No residual Advantage, magnitude, duration, or secondary state is generated from the partial match. Designer clarification: any further Effect beyond the single free Effect from a win requires a **separate opposed roll using an appropriate Advanced Skill** — the actor accepts the risk of that additional roll (consistent with, and not expanding, DEC-024) | In-session human ruling, 2026-08-29 (confirmed in post-handoff follow-on); handoff report rev.1 | Non-canonical designer ruling | Ruled |

**Carried forward / open from the S-3 thread:**
- **All items in the Effect Identity & Multi-Effect Opposition thread are now Ruled/closed** — DEC-025 (Q-S3-2a), DEC-026 (Q-S3-2b), DEC-027 (Q-S3-5), and DEC-030 (Q-S3-3a). No open forks remain there.
- Disarm/Break Hold's *specific tier* is **determined**: it sits in the combined Tag+Location-gated category (DEC-028), and its partial-match failure behaviour falls back to Base Inflict Injury (HP-only) per DEC-030 — identical to Equipment Damage and Armor Bypass.

## Governance note on this register

Per the specification governing this consolidation, an entry such as "Evidence strongly supports Position A" is never converted here into "Position A is canonical." Section A above lists only what the corpus's own top-authority document (D1) self-declares locked. Section B lists real decisions that the corpus itself repeatedly and explicitly labels non-canonical — this register preserves that label rather than upgrading it. Section C exists specifically so that silence is not mistaken for agreement. **Section D records in-session human rulings on non-canonical candidate S-3 material; like Section B, it preserves the non-canonical label and does not promote anything to Canonical.**
