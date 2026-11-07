---
document:
  title: "Tiwas — Comparative Analysis Report: Wurm Online Crafting System vs. Tiwas TTRPG Crafting System"
  version: "v1.0"
  status: "Advisory / Non-canonical analytical report. No DEC assigned or inferred. Presents suggestions, including systems explicitly identified as incompatible with Tiwas; nothing here is adopted by virtue of appearing in this report."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-17"
  last_modified_date: "2026-09-17"
relationship_to_prior_session_documents: >
  Builds on, but does not repeat, four prior documents from this session:
  tiwas-crafting-system-proposal-v0.1-2026-09-12.md,
  tiwas-tier1-primitive-item-catalog-v0.1-2026-09-12.md,
  tiwas-wurm-online-crafting-adaptation-session-report-2026-09-17.md (v1),
  tiwas-wurm-online-crafting-adaptation-session-report-v2-2026-09-17.md (v2).
  This report is a system-level comparative analysis; item catalogs and worked
  examples live in those four documents and are referenced, not reproduced, here.
---

**Author:** Claude Sonnet 5 — LLM name: `claude-sonnet-5`, LLM version: `claude-sonnet-5`
**Date:** 2026-09-17
**Classification:** Advisory / Non-canonical analytical report. No DEC assigned. Contains suggestions, some explicitly flagged as incompatible with Tiwas by design.

---

# Tiwas — Comparative Analysis Report: Wurm Online vs. Tiwas Crafting

## 0. Governance Statement

- Assigns **no DEC number**. Every recommendation below is a candidate for Tiwa's review, not an adopted rule.
- This report deliberately documents systems it recommends **against** porting, alongside systems it recommends **for** porting — per your instruction, negative findings are as much the point of this document as positive ones.
- Nothing here overrides any already-Ruled Tiwas decision (DEC-001 through DEC-140). Where a suggestion would require reopening a Ruled decision, that is stated explicitly.

---

## 1. Executive Summary

Wurm Online's crafting system is a 20-year-old, real-time MMO simulation built for continuous play, player-driven economy, and long-horizon skill grinding. Tiwas is a session-paced, GM-run, turn-resolved tabletop system built around a single unified d100 Core Test and an explicit design priority ordering (granular simulation, then heroic resilience, then minimum resolution steps). The two systems solve related problems — "how does making things well take work and get better with practice" — under almost opposite constraints.

**Net finding:** Wurm's *quality-capping-by-input* logic and its *tool-bootstrapping dependency chains* transplant cleanly and strengthen Tiwas's Priority-1 simulation goal. Wurm's *real-time action economy*, *stamina-gated pacing*, *sprawling sub-skill list*, and *grind-economy failure punishment* do not transplant, and porting them would actively work against Tiwas's own Priority 2 and Priority 3. Tiwas, in turn, already has a stronger failure-handling philosophy (failure always generates growth) than Wurm does, and that strength should be preserved rather than diluted by any Wurm import.

---

## 2. Methodology / Scope

This report synthesizes the Wurm Online research conducted across this session (crude-tool bootstrapping, carpentry, blacksmithing/weapon smithing, leatherworking, cloth tailoring, masonry/pottery, ropemaking — sourced from Wurmpedia, Wurm Wikia/Fandom, and community guides) against the current Tiwas Core (Canonical Rules v1.4) and this session's non-canonical crafting proposal. It does not introduce new Wurm research beyond what the prior four session documents already gathered; it re-analyzes that material specifically for compatibility.

---

## 3. Wurm Online Crafting System — Overview

| Mechanic | Strength (in Wurm's own context) | Weakness (in Wurm's own context) |
|---|---|---|
| Quality Level (QL), continuous ~1–99+ | Fine-grained economic differentiation; every crafted item has a real, tradeable quality gradient | Opaque to a new player without external tools — a bare number with no inherent narrative meaning |
| Material QL and Tool QL both cap output QL | Forces genuine sourcing/logistics play; rewards specialization and trade between players | Can hard-block progress if a player lacks access to good ore/tool sources — a real economic bottleneck |
| Improvement ("imping") toward an asymptotic, skill-based ceiling | Gives crafting a long-tail mastery curve with satisfying diminishing returns | Encourages repetitive, low-stakes click-grinding ("imp to skill+10") tuned for unlimited play time |
| Failure with partial cost (byproduct, or item damage + partial material loss) | Softer than total loss; adds textured realism | Still a real time/resource cost, calibrated for a grind economy, not a narrative session |
| Real-time action timers, gated by stamina/skill/tool QL | Creates a persistent, living-world pace appropriate to a 24-hour server | Fundamentally a wall-clock system — no analog in a scene-paced, turn-resolved game |
| 100+ named sub-skills (Blade Smithing, Heads Smithing, Weapon Smithing, Shield Smithing, Chain/Plate Armour Smithing, Locksmithing, Metallurgy, Jewelry Smithing, etc.) | Deep specialization, trade niches, strong roleplay/identity hooks | Steep entry curve, heavy content-maintenance burden, skill list grown organically over ~20 years without a unifying formula |
| kg-precision material tracking (e.g., a log must stay above 4 kg to retry; 0.05 kg of rivets consumed on failure) | Strong logistics/simulation feel; meaningful hauling, wagon, and ship-cargo gameplay | Granularity with no payoff at tabletop narrative pace — precision the players will never actually track by hand |
| Player-driven server economy | Emergent, social, genuinely MMO-defining | Does not exist in a GM-run tabletop game in the same form; porting it means reinventing it, not translating it |

---

## 4. Tiwas TTRPG Crafting-Relevant System — Overview

| Mechanic | Strength | Weakness / current gap |
|---|---|---|
| d100 roll-under Core Test (Cost = Roll, Overflow → HP, Failure XP, Recovery) — DEC-006 | One unified resolution engine for *everything*, including crafting (Invariant 18); fast to resolve at a table; every subsystem plugs into the same nine steps | Has no native duration/threshold concept of its own — crafting must borrow one (Extended Test) |
| Failure XP / Skill Roll Pool / Advanced Skill creation — DEC-009/010/012 | Failure is never purely wasted — it always generates mechanical growth (Locked Priority 2); no dead rolls | Crafting-specific failure (DEC-128 Q2) currently overrides this spirit at the *item* level — the natural-roll Failure XP still lands, but the item itself is a hard binary loss with no partial credit |
| Item Tier/Magnitude record — DEC-128 Q1, DEC-129 | Clean, reusable record shape, already integrated with Repair/Upgrade | Tier is a coarse discrete band, not a continuous dial — less price/quality granularity than Wurm's QL, by design |
| Extended Test — DEC-067/068/070 | Already-Ruled multi-attempt progress model; directly reusable for crafting durations without inventing a new system (already exploited by DEC-128 Q2's "Creation is an Extended Test") | Completion-threshold scaling by Tier is still unformalized (open item carried since the base crafting proposal) |
| Invariant 17 (no competing primary resource/progression economy) | Forces real design discipline; prevents the kind of resource-pool sprawl Wurm has (Stamina, Favor, multiple pools) | Directly blocks a literal Wurm-style Stamina-gated action economy without reinterpretation |
| Skill-Tier/24-attribute skill generation — DEC-005/012 | Mathematically elegant; skills emerge from play (failed Doubles) rather than being hand-authored one at a time | No native mechanism for Wurm-style sub-skill sprawl — a strength for elegance, but means crafting specialization must be expressed through Recipe-level skill tags, not dozens of named Advanced Skills |

---

## 5. Side-by-Side Comparison

| Dimension | Wurm Online | Tiwas | Compatible? |
|---|---|---|---|
| Output quality determinant | Continuous QL capped by weakest material/tool input | Discrete Tier capped by `min(Skill-Tier, max(input Tiers))` (proposed, this session) | **Compatible** — same underlying logic, different granularity |
| Tool's own quality as a cap | Yes — both material QL and tool QL independently cap output | Currently only input Tier is in the formula; tool Tier is not yet a formal input | **Compatible, and a genuine gap** — see Recommendation C, §6 |
| Failure outcome | Partial cost: byproduct, damage, or partial material loss | Binary: no item produced (DEC-128 Q2, Ruled) | **Partially compatible** — see Recommendation A, §6 |
| Improvement mechanic | Diminishing-returns asymptote toward a skill ceiling | Binary: success = Tier+1/Mag+1, failure = Tier+1/Mag+0 (DEC-128 Q3, Ruled) | **Partially compatible** — see Recommendation B, §8 |
| Time/duration | Real-time seconds, stamina-gated | No native clock; turn/scene-based | **Incompatible** — see §7 |
| Skill structure | ~100+ independently named, hand-authored skills | 24-attribute-derived Skills + emergent Advanced Skills | **Incompatible as a direct port** — see §7 |
| Material tracking precision | Fractional kg | Whole-unit quantity counts (this session's proposal) | **Incompatible at Wurm's granularity** — see §7 |
| Player economy | Server-wide player market | GM-run, session-scale; no established market subsystem (EQ-3A still open) | **Out of scope**, not strictly incompatible — see §7 |
| Failure's relationship to growth | Punitive — time/resource cost with no compensating benefit | Generative — Failure XP always awarded regardless of subsystem (Locked Priority 2) | **Tiwas is structurally stronger here** — see §9 |

---

## 6. Compatible Improvements — Recommended for Adoption

### 6.1 Recommendation A — Partial-Failure Byproduct Rule
*(Full mechanical specification already drafted in `tiwas-wurm-online-crafting-adaptation-session-report-v2-2026-09-17.md` §4; summarized here for the comparative record.)*

Directly grounded in Wurm's studded-leather and woodworking failure behavior. Proposes that a failed final Creation interval convert committed inputs into a lesser byproduct scaled by how close the attempt came to completion, rather than DEC-128 Q2's flat "no item." **Requires reopening DEC-128 Q2** — flagged, not silently applied.

### 6.2 Recommendation C — Tool Tier as a Formula Input (new this report)

Wurm's rule that *both* material QL and tool QL cap output QL (e.g., a stone brick's quality is capped by the shard's quality, and a higher-QL stone chisel separately increases both success chance and achievable quality) exposes a real gap in the parent proposal's Tier-determination formula (Option A), which only accounts for input materials/components:

- **Current (proposed) formula:** `Result Tier = min(Skill-Tier, max(input Tiers))`
- **Recommended revision:** `Result Tier = min(Skill-Tier, max(input Tiers), Tool Tier)`

This is a small, low-risk addition — it does not touch any Ruled material, only extends an already-non-canonical proposal formula — but it is the single cleanest, most directly-evidenced improvement this research surfaced. A crude Tier-1 knife should not be able to produce a Tier-3 result no matter how good the wood is, and Wurm's own rules agree.

### 6.3 Tool-Bootstrapping Dependency Chains

Already exploited across the primitive item catalog and both Wurm item catalogs. Wurm's own crude-knife-first, everything-else-built-from-something-earlier structure is a strong, well-tested validation of the mandatory Component pipeline already decided this session (§0 of the base crafting proposal) and directly serves Tiwas's Locked Priority 1 (granular physical simulation where warranted). No further action needed beyond what is already drafted — recorded here as a confirmed positive, not a new proposal.

### 6.4 Recipe-Based, Named Input/Output Crafting

Wurm's crafting-window model (activate a tool, select inputs, get a named output) validates the shape of the Recipe record already proposed (base proposal §9). No changes recommended; recorded as confirmation that the chosen shape is sound.

---

## 7. Incompatible Elements — Explicitly Not Recommended

| Wurm element | Why it is incompatible with Tiwas |
|---|---|
| **Real-time wall-clock action timers, stamina-gated** | Tiwas has no clock and is explicitly turn/scene-resolved; a real-time timer cannot exist in a system with no session-independent time unit. This is why the parent proposal defaulted to a number-of-actions convention instead (already resolved, not reopened here). |
| **A dedicated Stamina resource pool gating actions** | Would directly violate Invariant 17 (no competing primary resource or progression economy) unless folded into an existing pool (PE), which would then just be Cost = Roll under another name — i.e., Tiwas already has the mechanic this would reinvent. |
| **100+ hand-authored, narrowly-scoped sub-skills** | Conflicts with Tiwas's skill-generation philosophy (DEC-005/012): skills emerge from attribute combinations and failed Doubles, not from a hand-curated master list. Porting Wurm's skill sprawl would mean either (a) hand-authoring dozens of Advanced Skills outside the normal creation path, undermining DEC-012's origin rule, or (b) building a parallel skill-naming layer with no Tier/Cap grounding. Neither is recommended. |
| **Fractional-kg material-weight tracking** | Adds bookkeeping precision with no payoff at tabletop pace; this session's crafting proposal already deliberately abstracted this to whole-unit `quantity` counts (§7 of the base proposal), and that choice should stand. |
| **Grind-optimized skill-training meta (imp-to-skill+10, sleep-bonus doubling, dedicated cheap-material skill-trainer items)** | This is an artifact of Wurm's unlimited-real-time MMO economy, not a crafting mechanic per se. It actively conflicts with Locked Priority 3 (minimum resolution steps without sacrificing simulation) — Tiwas should not import a design pattern whose entire purpose is to absorb large amounts of real player time. |
| **Player-driven server market/economy** | No equivalent exists in a GM-run tabletop game; this is not so much incompatible as simply a different genre of system. Any Tiwas economy content belongs to the still-open EQ-3A fork (DEC-081.A Open 3), not to a crafting-mechanics import. |

---

## 8. Partially Compatible — Needs Careful Adaptation

### 8.1 Recommendation B — Diminishing-Returns Upgrade Ceiling
*(Full specification in the v2 session report §5.)* Wurm's asymptotic imp ceiling is a real strength in an MMO where hundreds of attempts are plausible — but Tiwas's own Priority 3 (minimum resolution steps) means the same idea, ported at Wurm's own pace, would be a mistake. If adopted, the constants (`k`, `c` in the proposed formula) must be tuned so the "hard zone near the ceiling" is reached in a handful of Upgrade attempts, not dozens. **This caution is itself part of the recommendation, not a separate caveat** — accepting Recommendation B without also constraining it to tabletop pace would import Wurm's weakness along with its strength.

### 8.2 Material/Component Decay Over Time

Flagged (not drafted) in the v2 report §8. Wurm's mortar/clay spoilage is a genuine piece of realism, but with no real-time clock, "decay" would need to be redefined as a per-scene or per-session-count mechanic rather than a literal timer. This report does not draft that formula — it is recorded here only so it is not lost, and is explicitly **not** among the recommendations in §10's punch list.

---

## 9. Where Tiwas Is Already Stronger Than Wurm

A comparative report should note this directly, since it is easy to read a "what can we borrow" exercise as one-directional:

- **Failure generates growth, universally.** Wurm's failure is a pure cost with no structural compensation beyond "you can retry." Tiwas's Failure XP (DEC-009) fires on *every* failed Core Test, crafting included, regardless of whether the item itself is lost. This is a genuine design advantage baked into Tiwas's Core that Wurm does not have, and no recommendation in this report should be read as weakening it — Recommendation A specifically preserves it by adding a *second, independent* consolation (the byproduct) on top of the Failure XP that already fires.
- **One resolution engine for everything.** Wurm's crafting, combat, and gathering systems are related but not identical subsystems with their own quirks. Tiwas's Invariant 18 (every subsystem builds on the same Core Test Transaction) means crafting inherits Cost/Overflow/Recovery/Failure-XP/Advanced-Skill-creation for free, with no separate crafting-specific economy to maintain.
- **Mathematically bounded skill/attribute system.** 24 fixed attributes with a formulaic Cap/Tier system is far more maintainable and internally consistent than an organically-grown 100+-skill list — a genuine structural advantage for a system that intends to stay "closed and authoritative" per its own design discipline.

---

## 10. Consolidated Recommendations Table

| ID | Recommendation | Disposition | Requires reopening a Ruled DEC? |
|---|---|---|---|
| A | Partial-Failure Byproduct Rule | Proposed — full spec in v2 §4 | Yes — DEC-128 Q2 |
| B | Diminishing-Returns Upgrade Ceiling, tabletop-paced | Proposed with an explicit pacing caveat — full spec in v2 §5 | No (adds a Skill-side penalty layer; DEC-128 Q3's outcome table untouched) |
| C | Tool Tier added to the output-Tier formula | Proposed, new this report | No (extends an already non-canonical proposal formula) |
| — | Tool-bootstrapping dependency chains | Confirmed positive, already in use | No |
| — | Recipe-based crafting shape | Confirmed positive, already in use | No |
| — | Real-time action timers | **Rejected** | N/A |
| — | Stamina resource pool | **Rejected** | N/A |
| — | 100+ hand-authored sub-skills | **Rejected** | N/A |
| — | Fractional-kg material precision | **Rejected** | N/A |
| — | Grind-optimized skill-training meta | **Rejected** | N/A |
| — | Player-driven market economy | **Out of scope** (belongs to EQ-3A, not this report) | N/A |
| — | Material/component decay over time | **Flagged, not drafted** | N/A |

---

## 11. Relationship to Prior Session Documents

| Document | Role relative to this report |
|---|---|
| `tiwas-crafting-system-proposal-v0.1-2026-09-12.md` | Base framework this report evaluates and, in §6.2, proposes one revision to (Recommendation C) |
| `tiwas-tier1-primitive-item-catalog-v0.1-2026-09-12.md` | Worked-example evidence for §6.3's tool-bootstrapping confirmation |
| `tiwas-wurm-online-crafting-adaptation-session-report-2026-09-17.md` (v1) | Source of the original ten-item Wurm research and the two tensions this report formalizes |
| `tiwas-wurm-online-crafting-adaptation-session-report-v2-2026-09-17.md` (v2) | Source of the full mechanical specs for Recommendations A and B, and the sixteen additional items grounding them |
| **This document** | System-level comparative analysis; does not repeat item catalogs, only synthesizes their findings into adopt/reject guidance |

---

## 12. Open Questions / Required Tiwa Rulings

1. Recommendation A (Partial-Failure Byproduct Rule) — accept, reject, or request revision; requires reopening DEC-128 Q2 if accepted.
2. Recommendation B (Diminishing-Returns Upgrade Ceiling) — accept, reject, or request revision; does not require reopening any Ruled DEC, but needs its own new ruling to exist at all.
3. Recommendation C (Tool Tier in the output formula) — accept, reject, or fold into the base proposal's still-open Tier-formula question (§5, Option A/B/C).
4. Whether any form of decay/spoilage (§8.2) is worth drafting as its own future recommendation.
5. All open items already carried from the base proposal and both Wurm session reports remain open and are not restated in full here — see those documents' own checklists.

---

## 13. Required OpenCode Actions

1. File this report under `investigations/` alongside the four documents it builds on.
2. Route Recommendations A, B, and C to Tiwa as three separately-rulable items, consistent with how A and B were already flagged in the v2 report.
3. Assign no DEC to anything in this document.
4. When/if any of A, B, or C is ruled on, update this report's §10 disposition column rather than silently superseding it.

---

## 14. Sources

All source material is carried from the prior session documents' research (Wurmpedia, Wurm Wikia/Fandom, and community guide sources cited in `tiwas-wurm-online-crafting-adaptation-session-report-2026-09-17.md` §11 and `tiwas-wurm-online-crafting-adaptation-session-report-v2-2026-09-17.md` §11). No new Wurm research was conducted for this report; it is a synthesis document.

---

## 15. Reconfirmation Checklist for Tiwa

- [ ] Recommendation A — accept / reject / revise
- [ ] Recommendation B — accept / reject / revise
- [ ] Recommendation C — accept / reject / fold into base proposal's open Tier-formula question
- [ ] §7's rejection list — confirm agreement, or flag any item you want reconsidered despite the stated incompatibility
- [ ] §8.2 (decay/spoilage) — confirm out of scope, or request a drafted proposal
- [ ] §9 — confirm the "Tiwas is already stronger here" claims are accurate framing, not overstated

---

**End of report.**

**Author:** Claude Sonnet 5 — LLM name: `claude-sonnet-5`, LLM version: `claude-sonnet-5`
**Date:** 2026-09-17
