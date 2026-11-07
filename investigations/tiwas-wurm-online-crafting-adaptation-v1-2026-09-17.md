---
document:
  title: "Tiwas — Session Report: Wurm Online Crafting Research & Adaptation (OpenCode Handoff)"
  version: "v1.0"
  status: "Advisory / Non-canonical. Session report only. No DEC assigned or inferred. Nothing in this document is Canonical, Ruled, or binding until Tiwa reviews and acts on it."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-17"
  last_modified_date: "2026-09-17"
session_deliverables:
  - "tiwas-crafting-system-proposal-v0.1-2026-09-12.md"
  - "tiwas-tier1-primitive-item-catalog-v0.1-2026-09-12.md"
  - "tiwas-wurm-online-crafting-adaptation-session-report-2026-09-17.md (this document)"
---

**Author:** Claude Sonnet 5 — LLM name: `claude-sonnet-5`, LLM version: `claude-sonnet-5`
**Date:** 2026-09-17
**Classification:** Advisory / Non-canonical session report for OpenCode. No DEC assigned, none proposed as final by this document.

---

# Tiwas — Session Report: Wurm Online Crafting Adaptation

## 0. Governance Statement

- Assigns **no DEC number** and proposes none as settled.
- Every mechanic below is labelled **REUSED (Ruled)**, **REUSED (Proposed, this session)**, or **NEW (Proposed, this session)** — nothing is asserted as Canonical.
- Where a Wurm Online mechanic conflicts with an already-Ruled Tiwas decision, the conflict is flagged (§7) and the Ruled decision is **not** overridden.
- This document is a **session report**: its purpose is to hand the complete, consolidated output of this chat session to OpenCode for filing, in the same shape as prior session-report artifacts in this repository (e.g. the mirror-combat v2 session report).

---

## 1. Session Overview — Deliverables Produced

Three documents were produced in this session, in order:

| # | Document | Content |
|---|---|---|
| 1 | `tiwas-crafting-system-proposal-v0.1-2026-09-12.md` | Base crafting framework: unified Material/Component/Item record (extends DEC-128 Q1), mandatory Component pipeline, Tier-determination formula candidates, Extended-Test crafting procedure, quantity-vs-Invariant-17 reconciliation, Recipe schema |
| 2 | `tiwas-tier1-primitive-item-catalog-v0.1-2026-09-12.md` | Worked example content: a self-bootstrapping Tier-1 primitive (Stone-Age-equivalent) item catalog built on document #1's framework |
| 3 | **This document** | Wurm Online crafting-system research, its adaptation onto documents #1–#2's framework, ten Wurm-derived starter items, and this consolidated session recap |

§8 gives the full recap table (status, open items, file paths) for all three.

---

## 2. Research Process — Wurm Online Crafting System

Documented in the order performed, per your instruction:

| Step | Query | What it established |
|---|---|---|
| 1 | Wurm Online crafting system — skill, Quality Level (QL) mechanics | QL is a continuous 1–99(+) quality dial on every item; skill level, material QL, and tool QL jointly determine both success chance and the maximum QL achievable on a given attempt; an "improve" (imp) action can push an existing item's QL up over repeated attempts, but it approaches a skill-based asymptotic ceiling rather than climbing without bound |
| 2 | Wurm Online action timer mechanics — ticks, duration formula | Actions consume real-world time (seconds), not an abstract turn or action-point count; duration is reduced by higher relevant-skill level, sufficient stamina, and higher tool QL — there is no discrete "number of actions" currency in Wurm itself, it is a wall-clock system |
| 3 | Wurm Online new-player crafting guide — common early items | Confirmed the standard early bootstrap chain: a crude knife (rock shard + iron-bearing rock, no tool needed) is the first tool, required before any other tool can be shaped; wood items (shafts, planks) come from logs via carving knife/saw; iron items (nails, lumps) come from ore via a fire and an anvil; rope comes from plant fiber via a rope tool |
| 4 | Wurm Online rope-making, shingle, plank, carving-knife crafting steps | Confirmed exact input chains for rope (rope tool + wemp fiber, output QL capped at the fiber's own QL), and the carpentry chain (log → shaft/plank via carving knife or saw); also surfaced a concrete failure-handling detail: a failed Plank attempt does not destroy the log outright — it can be retried on the same log until the log's weight drops too low, and a failed attempt on some wood items yields a lesser byproduct (woodscrap) rather than nothing |

No content is reproduced verbatim from any source; all findings below are paraphrased and cited only by URL in §11.

---

## 3. Wurm Online Crafting System — Findings Summary

| Mechanic | Wurm behavior |
|---|---|
| Quality Level (QL) | Single continuous quality stat, roughly 1–99+, on every item |
| Success/output determinants | Crafter's skill level, the QL of the tool used, the QL of the input material, and the item's intrinsic difficulty jointly set both success chance and achievable output QL |
| Output QL ceiling | An item's output QL cannot exceed the QL of the material or tool that produced it — realism is enforced by capping quality at the weakest input, not by skill alone |
| Improvement ("imping") | Repeated attempts on an existing item can raise its QL further, but gains diminish and approach a skill-based asymptotic ceiling rather than climbing indefinitely |
| Failure behavior | Not uniformly "nothing happens" — some failed attempts consume part of the input material (retry until the source is too depleted) or produce a lesser byproduct instead of the intended item |
| Action/time system | Real-world seconds per action, not an abstract action-point or turn count; duration scales down with higher skill, adequate stamina, and better tool QL |
| Tool bootstrapping | The crude knife is the one tool built from nothing but raw materials and no tool; every other tool in the game is built using some earlier tool, forming a strict dependency chain |

---

## 4. Adaptation Mapping — Wurm Mechanic → Tiwas Mechanic

| Wurm mechanic | Tiwas equivalent | Status |
|---|---|---|
| Quality Level (QL), continuous 1–99 | Item Magnitude (within a Tier band) | REUSED (Ruled shape, DEC-129 base-equal-at-creation pattern) — Wurm has no Tier concept; Tiwas layers a discrete Tier band on top of a Wurm-style continuous quality value. This is a genuine structural difference, not a 1:1 mapping — flagged in §7. |
| Output QL capped by weakest material/tool input | `Result Tier = min(Skill-Tier, max(input Tiers))` (Option A) | REUSED (Proposed, session #1, §5) — this Wurm finding is direct real-world-game validation for recommending Option A over Options B/C in the parent proposal. |
| Success/fail roll | Tiwas's existing d100 Core Test (Roll ≤ Skill) | REUSED (Ruled) — no new roll mechanic is invented; Wurm's percentage-chance system and Tiwas's roll-under Skill Test already serve the identical function. |
| Imp/improvement asymptotic ceiling | Candidate soft ceiling on Magnitude gain per Upgrade attempt | NEW (Proposed, this session) — see §7 for why this does **not** override the already-Ruled DEC-128 Q3 Upgrade outcome (success = Tier+1/Mag+1; fail = Tier+1/Mag+0). |
| Byproduct-on-failure / partial material consumption | — | NOT adopted — flagged as a tension with Ruled material, §7. |
| Real-time action duration | Number-of-actions convention (§5) | NEW (Proposed, this session), per your explicit instruction that Tiwas has no time/action system yet. |
| Crude-knife-first tool bootstrapping | Mandatory Component pipeline (§3 of the parent proposal) + this session's Wurm item chain (§6) | REUSED (Proposed, session #1) — directly validated by Wurm's real bootstrap order. |

---

## 5. Time/Action System Resolution

**Finding:** Wurm Online's action system is a **real-world wall-clock timer** (seconds per action), gated by stamina, skill level, and tool QL. It is not a discrete "number of actions" system — Wurm's own mechanic does not directly transplant onto a turn-based, roll-driven tabletop game with no clock.

**Resolution, per your instruction to default to number-of-actions when a transplantable Wurm time system does not exist:**

- **1 Tiwas crafting action = 1 Extended Test interval** (one Core Test attempt on the relevant crafting Skill, per the parent proposal §6 and the already-Ruled DEC-067/068/070 Extended Test machinery).
- Wurm's "higher skill/better tool = faster" principle is preserved **as an action-count effect, not a time effect**: a higher Skill-Tier accumulates Margin faster per interval (already true under DEC-067's Margin-accumulation), and a higher-Tier tool is proposed (NEW, this session) to grant a flat discount to the Extended Test's completion threshold — e.g., `Effective Threshold = Base Threshold − (Tool Tier − 1)`, floored at a positive minimum. This is a candidate formula only, not a ruling.
- No wall-clock, stamina pool, or real-time value is introduced. This keeps Invariant 17 intact (no new resource pool) and Invariant 6 intact (natural roll never modified).

---

## 6. Ten Most Common Wurm Online Simple Items — Adapted to Tiwas

Selected as the ten items that most commonly recur across Wurm's own new-player bootstrap chain (crude tool → wood processing → iron processing → rope), rather than niche/late-game items. Each row shows the real Wurm crafting step (paraphrased) and its Tiwas equivalent using the Material/Component/Item schema and Recipe shape from `tiwas-crafting-system-proposal-v0.1-2026-09-12.md`.

| # | Wurm item | Real Wurm crafting step | Tiwas `type` | Tiwas Tier | Inputs | Tool required | Crafting Skill | Action count (proposed default) |
|---|---|---|---:|---:|---|---|---|---:|
| 1 | Crude Knife | Rock shard + iron-bearing rock, combined by hand; the game's true bootstrap tool, needs no other tool | Item | 1 | Material `rock_shard` + Material `iron_rock` | none | Improvisation/Survival | 2 |
| 2 | Shaft | Carving knife used on a log | Component | 1 | Material `log` | `crude_knife` (#1) | Woodcutting/Carpentry | 2 |
| 3 | Plank | Saw used on a log | Component | 1 | Material `log` | Saw *(external tool, not detailed this session — flagged §9)* | Carpentry | 2 |
| 4 | Mallet | Carving knife shapes a shaft into a mallet head, combined with a second shaft as the handle | Item | 1 | Component `shaft` ×2 | `crude_knife` (#1) | Carpentry | 3 |
| 5 | Small Anvil | Hot iron lumps combined, then shaped with a mallet | Item | 1 | Material `iron_lump` ×2 (combined) | `mallet` (#4) + fire *(via `kindling`, #10)* | Blacksmithing | 3 |
| 6 | Small Nail | Iron lump worked on an anvil | Component | 1 | Material `iron_lump` | `small_anvil` (#5) | Blacksmithing | 2 |
| 7 | Large Nail | Iron lump worked on an anvil, more material consumed than a Small Nail | Component | 1 | Material `iron_lump` ×2 | `small_anvil` (#5) | Blacksmithing | 3 |
| 8 | Rope Tool | Shaft or plank shaped by hand/carving knife into a dedicated ropemaking tool | Item | 1 | Component `shaft` or `plank` | `crude_knife` (#1) | Carpentry | 2 |
| 9 | Rope | Rope tool used on plant fiber; output quality is explicitly capped at the fiber's own quality in Wurm's own rules — direct real-world confirmation of the Option A Tier formula (§4) | Item | 1 | Material `plant_fiber` *(same subtype as the earlier primitive catalog — see §7 continuity note)* | `rope_tool` (#8) | Ropemaking | 3 |
| 10 | Kindling | Crude knife used on woodscrap; enables a campfire, itself a prerequisite for smelting the iron used in items #5–7 | Component | 1 | Material `woodscrap` *(byproduct-class Material; see §7)* | `crude_knife` (#1) | Woodcutting/Survival | 1 |

**Dependency order this table implies** (mirrors Wurm's own real progression): `crude_knife` → `shaft`, `plank`, `kindling` (all need only the knife) → `mallet`, `rope_tool` (need shafts/planks) → fire, via `kindling` → `small_anvil` (needs mallet + fire) → `small_nail`, `large_nail` (need the anvil) → `rope` (needs the rope tool + fiber).

**Continuity note:** items #2, #3, #10 reuse the `log`/`woodscrap` Material family already implied by the earlier primitive catalog's `wood_branch`; item #9's `plant_fiber` input is the **same subtype** already defined in `tiwas-tier1-primitive-item-catalog-v0.1-2026-09-12.md` §2 — this Wurm-derived set is designed to slot directly alongside that catalog rather than duplicate it. `log` and `woodscrap` are new subtypes this session adds to the Material list (a log being a larger/less-processed precursor to a branch, per Wurm's own distinction between the two).

---

## 7. Points of Tension With Already-Ruled/Proposed Material — Flagged, Not Resolved

| Tension | Wurm side | Tiwas side | Resolution this session |
|---|---|---|---|
| Failure output | A failed crafting attempt can consume part of the material and/or yield a lesser byproduct (e.g., woodscrap instead of a shaft) rather than producing nothing | DEC-128 Q2 is **Ruled**: a failed (first-time) Creation attempt produces **no item** | **Not adopted.** DEC-128 Q2 is Ruled and this document does not override it. The Wurm byproduct idea is recorded here only as a candidate refinement for Tiwa's own future consideration — it would need its own ruling and is not assumed anywhere in §6's table. |
| Continuous QL vs discrete Tier | QL is one continuous 1–99+ dial with no tier bands | Tiwas layers a discrete Tier ceiling on top of a continuous Magnitude, per the parent proposal | No numeric QL-to-Tier band mapping is proposed — that would be fabricated precision with no grounding. Wurm QL is treated as validating the *existence* of a quality dial (→ Magnitude) and the *capping* behavior (→ the Tier formula), not as a source of specific band cutoffs. |
| Improvement asymptote | Imping approaches a skill-based ceiling with diminishing returns per attempt | DEC-128 Q3 is **Ruled**: Upgrade success = Tier+1/Magnitude+1; failure = Tier+1/Magnitude+0 (imbalanced) | **Not adopted as a mechanic change.** DEC-128 Q3's binary success/imbalance-on-failure shape stands unmodified. The Wurm asymptote idea is recorded only as an optional *content* input (e.g., how a GM might narrate diminishing returns at high Tier), never as a proposed change to the roll outcome table. |
| Saw (tool) | Referenced in Wurm's own plank-making step | Not detailed in this session's ten-item set | Flagged, not invented — `tiwas-crafting-system-proposal-v0.1`'s Recipe schema can host it whenever it is authored. |

---

## 8. Complete Chat Session Deliverables — Recap for OpenCode

| Document | Status | Key open items |
|---|---|---|
| `tiwas-crafting-system-proposal-v0.1-2026-09-12.md` | Non-canonical proposal, pending review | Tier-determination formula choice (A/B/C — this session's Wurm research favors A); completion-threshold scaling; Material-acquisition scope (ties to EQ-3A, DEC-081.A Open 3); recipe-authorship confirmation; tool/facility requirement scope; Component-as-standalone-Item default |
| `tiwas-tier1-primitive-item-catalog-v0.1-2026-09-12.md` | Advisory example content, pending Tiwa's authorship review | `self_bow` and fired pottery flagged as possible Tier-2 stretch items; material-acquisition Skill-Test question inherited from the parent proposal |
| This document | Advisory session report, pending review | Byproduct-on-failure and imp-asymptote ideas explicitly **not** adopted, recorded only as future-consideration candidates (§7); action-count-per-Tool-Tier discount formula (§5) is a fresh candidate, unvalidated by playtest |

None of the three documents has been promoted, ruled on, or run through the 8-step Promotion Rule. All three remain fully non-canonical.

---

## 9. Consolidated Open Questions (all three documents)

1. Tier-determination formula: confirm Option A (`min(Skill-Tier, max(input Tiers))`), now with Wurm's own output-capping behavior as supporting precedent.
2. Extended Test completion-threshold formula, and whether a Tool-Tier discount (§5, this session) is adopted.
3. Material acquisition scope and its dependency on the still-open EQ-3A wealth/economy fork.
4. Recipe authorship: confirmed as pure content-authoring (no universal input-count formula) — still needs explicit sign-off.
5. Tool/facility requirements above Tier 1 (forge, workbench) — fully open.
6. Component-as-standalone-Item default (§3 of the parent proposal) — still needs confirm/override.
7. Whether `self_bow` and fired pottery should move to Tier 2.
8. Whether the Wurm-inspired byproduct-on-failure and imp-asymptote ideas (§7, this document) should ever be raised as their own separate ruling requests — recorded as declined-to-propose this session, not rejected outright.

---

## 10. Required OpenCode Actions

1. File all three documents from §1 as advisory storage under `investigations/`; assign no DEC to any of them.
2. Cross-reference this report against `_consolidation/decision-register.md`'s DEC-081.A Open 3 entry (Equipment subsystem, wealth/economy fork) since §9 item 3 depends on it.
3. Do not mark any content in any of the three documents Canonical, Ruled, or content-authored/blessed — all three await Tiwa's explicit review.
4. Preserve the §7 tension table verbatim in any future summary — it exists specifically so the Wurm-sourced ideas that were **not** adopted are not later mistaken for silently-adopted rulings.

---

## 11. Sources (Wurm Online Research)

- https://wurm.fandom.com/wiki/Rope_tool
- https://www.wurmpedia.com/index.php/Rope_tool
- https://saarith.com/how-to-build-a-ship-in-wurm-online/
- https://steemit.com/gaming/@enjar/why-i-enjoy-playing-wurm
- https://www.wurmpedia.com/index.php/Guides:Woodcutting(tutorial)
- https://www.wurmpedia.com/index.php/Ropemaking
- https://www.wurmpedia.com/index.php/Guides:Carpentry_and_subskills_guide_for_the_resource_conscious
- https://www.wurmpedia.com/index.php/Rope
- https://www.wurmpedia.com/index.php/Guides:Starting_with_Nothing
- Additional general Wurm Online QL/skill-check and action-timer mechanics pages (Wurmpedia/community wiki), consulted for §§2–3 findings

---

## 12. Reconfirmation Checklist for Tiwa

- [ ] Tier-determination formula confirmed (Option A recommended, now Wurm-validated)
- [ ] Tool-Tier action-count discount formula (§5) accepted, modified, or rejected
- [ ] Byproduct-on-failure idea (§7) — confirm it stays unadopted, or raise it as its own future ruling request
- [ ] Imp-asymptote idea (§7) — confirm it stays unadopted, or raise it as its own future ruling request
- [ ] Ten-item catalog (§6) reviewed for authorship/content-blessing per the DEC-077.A precedent
- [ ] Saw (and any other unlisted Wurm tool) flagged for future authoring, not silently assumed

---

**End of session report.**

**Author:** Claude Sonnet 5 — LLM name: `claude-sonnet-5`, LLM version: `claude-sonnet-5`
**Date:** 2026-09-17
