---
document:
  title: "Tiwas — G3 Duration / Time-Unit Scale: Comprehensive Options Research Report"
  version: "0.1"
  status: "Advisory / Non-canonical. No DEC assigned. Research and options catalog only — resolves nothing, rules nothing, promotes nothing."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-17"
  last_modified_date: "2026-09-18"
---

## Purpose and Origin

Advisory design-research material produced by Claude Sonnet 5 (`claude-sonnet-5`) on 2026-09-17 and handed over for intake. Stored via the analyze-assess-record-store workflow (assessed and stored by OpenCode / big-pickle): advisory-only, non-canonical, no DEC inferred — storage and assessment confer no authority. It is a comprehensive catalog and categorized comparison of candidate architectures for the **G3 duration / time-unit-scale gap** (open per DEC-133/DEC-133.A; explicitly left untouched by DEC-138's G1 closure), assembled across a multi-turn design-research session for handoff into the documentation pipeline ahead of any formal Tiwa ruling. Body preserved verbatim below; only this frontmatter block and this opener were normalised at storage time (original author preserved as `author_llm`). Assessment note: the report's load-bearing citations to the live register were verified accurate (DEC-082/DEC-082.A, DEC-095, DEC-133/DEC-133.A, DEC-138, DEC-067/068/070/073, DEC-089–DEC-093); one citation nuance is flagged — `Option O` describes DEC-117 R2's `duration` field as a four-value enum `instant / scene / session / permanent`, whereas the live register records only `permanent` (Tag), `instant`/`scene` (Effect) and "varies" (Condition); the `session` value is not established in the register and must not be treated as ruled (see the register annotation on DEC-133.A).

# Tiwas — G3 Duration / Time-Unit Scale: Comprehensive Options Research Report

**Prepared by (Author):** Claude — LLM name: `claude-sonnet-5`, LLM version: Claude Sonnet 5

**Date:** 2026-09-17

**Document class:** Advisory design-research report. Not a Decision Record. Not a proposal draft in the Proposals/WIP sense. A structured options catalog intended to give Tiwa (and OpenCode, as documentarian) a single reference document to rule from.

---

## 0. Governance Statement

This document:

- Assigns **no DEC number** and proposes none.
- **Makes no ruling.** Every option below remains a candidate until Tiwa selects, rejects, combines, or scopes one or more of them via the normal Status Lifecycle (`governance/status-model.md` §"Status lifecycle").
- **Resolves nothing about G3.** DEC-133 / DEC-133.A / DEC-138 remain exactly as recorded; this report does not narrow, imply, or presuppose an outcome for any of them.
- Is a **research consolidation**, not a fresh single-session brainstorm graded for internal consistency against itself only — each option is checked against Invariant 17 (no new resource/progression pool), Invariant 18 (no parallel resolution engine), and DEC-082/DEC-082.A (no action-point economy) as a baseline compatibility filter, not as a scoring mechanism that picks a winner.
- Carries no authority by virtue of thoroughness. A well-argued option is not a ruled option (Promotion Rule, Proposals/WIP §21; `governance/status-model.md`).

---

## 1. Purpose and Scope

### 1.1 Purpose

Tiwas has no ruled answer to a question every other subsystem eventually depends on: **how much real or narrative time does a resolved action, interval, or turn actually consume?** This report exists to give Tiwa a single, comprehensive, side-by-side reference of every architecture surfaced during design research, so that a ruling (or a scoped set of rulings) can be made deliberately rather than by whichever option happened to be discussed first.

### 1.2 Scope

In scope: all candidate mechanisms for assigning, scaling, or deliberately declining to assign a duration to (a) a combat turn/exchange, (b) an Extended Test interval, (c) a hazard-exposure tick, (d) a crafting or downtime task, and (e) travel between distance bands. Out of scope: any actual numeric constants (base durations, conversion tables, tuning coefficients) — those are content-authoring (DEC-077.A) or implementation detail that follows *after* an architecture is chosen, not before.

### 1.3 Why This Matters More Than a Typical Reserved Item

Tiwas's own stated identity (`canonical/rules/...` §1) is that *every meaningful attempt uses the common resolution engine* and *every test costs resources*. Skill Tests are not one subsystem among many in Tiwas — they are the substrate every other subsystem is built on (Core Test Transaction, S-1 Opposed Contest, Extended Tests, Hazards, Crafting). A duration model that gets bolted onto Skill Tests therefore touches more surface area than almost any other open item in the register. Getting G3 wrong — or leaving it silently unresolved while automated runners quietly invent their own answers — has more downstream blast radius than most Reserved subsystems.

---

## 2. Problem Statement — The G3 Gap

| Ruled item | What it settles | What it explicitly does *not* settle |
|---|---|---|
| DEC-095 | Combat turn = one S-1 exchange; Speed-based turn order; round structure | No real-world seconds/minutes assigned to a "turn" |
| DEC-082 / DEC-082.A | Time/Action expressed only via Skill-side or Movement-penalty overlays; **explicitly no action-point pool** | Never converts an "action" into elapsed time — the whole subsystem is about *penalties*, not *clocks* |
| DEC-133 / DEC-133.A | Canonical spatial model = four abstract Distance Bands (Engagement/Short/Medium/Far); Movement Distance per combat turn = effective Movement Speed; band↔hex conversion deferred to content-authoring | **Explicitly and by name declines to define real-world duration per turn** — this is the direct textual origin of the G3 gap |
| DEC-067 / DEC-068 / DEC-070 / DEC-073 | Extended Test intervals accumulate Margin; failure is neutral; completion target = GM discretion, no formula; S-11 healing is a literal Extended Test instance | An "interval" has no defined real-world length in any of these rulings |
| DEC-089–DEC-093 | Hazards resolve via the existing Core Test + Cost/Overflow machinery; Intensity is a lookup key into pre-set parameters | Duration of hazard exposure per resolution tick is undefined |
| DEC-117 R2 | Every StateRecord (Effect/Condition/Tag) already carries a `duration` field — currently the enum `instant / scene / session / permanent` | The enum's buckets are not defined in real time or in relation to a turn/interval — they are placeholders with no numeric or comparative meaning yet |

**Net effect:** Tiwas resolves *what happens* on virtually every roll in the game, and resolves it with unusual rigor — but nothing in the Locked Core or the Ruled non-canonical layer resolves *how long it took*. At a human table this is invisible, because a GM fills the gap by intuition every time (exactly the behavior described as the status quo). In an unattended automated run (the Claude/GPT/Grok playtest runners already in the corpus), there is no GM to intuit anything — the gap becomes a visible, blocking omission rather than an invisible convenience.

---

## 3. Research Methodology and Sources

Two research passes were run against external precedent before the options were drafted:

1. **Video-game action-timer systems**, with Wurm Online as the primary named reference: real-time action-duration formulas gated by skill level, tool quality, and stamina; a secondary derived stat (Mind Logic) gating action-queue depth rather than a bespoke action-point pool; server-side tuning multipliers kept separate from the base formula.
2. **Tabletop precedent across the full abstraction spectrum**: GURPS (concrete, logarithmic Time-Spent ladder and a man-hours labor model), D&D-lineage systems (flat non-scaling durations per category — the 6-second round, the 10-minute dungeon turn), Blades in the Dark / Forged in the Dark (Clocks — explicitly *not* a timekeeping mechanic, a consequence-proximity tracker), and Torchbearer (abstract, unitless "Turns" whose only defined property is what they consume, not how long they last).

These two poles — **simulate real time precisely** (Wurm, GURPS) versus **never define real time at all** (Torchbearer, Blades) — turned out to be the organizing axis for the entire option catalog below, which is why Category III exists as a legitimate architectural family and not a placeholder for "didn't answer the question."

---

## 4. Complete Option Catalog

Fifteen options were generated across the session (labeled A–O for stable cross-reference). Each entry includes its mechanism, its precedent, an explicit compatibility check against Tiwas's binding invariants, and an extended positives/negatives analysis.

---

### Option A — Fixed Category Lookup

**Mechanism:** Every action *category* (combat exchange, craft interval, travel interval, hazard tick, social/investigation beat) has one hard-coded duration drawn from a table. The duration does not vary with the roll, the Skill, or the outcome — only with which category the action belongs to.

**Precedent:** D&D-lineage fixed abstraction (6-second combat round; 10-minute dungeon exploration turn), independent of any roll result.

**Invariant/precedent fit:** No new resource, pool, or roll. Directly mirrors the already-ruled DEC-093 pattern ("Intensity is a lookup key only, never a roll or a second transaction").

**Positives**
- Zero computation overhead at the table — a GM or automated runner reads one number and moves on.
- Perfectly predictable; players can plan around known durations (a torch lasts N combat rounds, a rest period is always the same length).
- Trivial to automate: a lookup table needs no formula engine at all.
- Cannot desynchronize from the fiction — every actor's turn is the same length by definition, so "who finished first" is never an emergent question requiring adjudication.
- Matches Tiwas's Priority 3 (minimum resolution steps) almost perfectly for high-frequency, low-stakes categories.

**Negatives**
- Actively contradicts Priority 1 (granular physical simulation) for any category where duration *should* vary with competence — a Tier-5 master and a Tier-1 novice take identically long to do anything.
- No mechanical reward for skill investment in the time dimension at all, which sits oddly in a system that ties nearly everything else (Effect Tier, Location depth, Wound severity, crafting gates) to Skill-Tier.
- Requires an ever-growing table as new action categories are authored — maintenance burden scales with content, not with rules.
- Cannot represent "I rushed this" or "I took my time" as a meaningful player choice without bolting on a separate modifier (see Option M).

**Best-fit domain:** High-frequency, low-stakes categories where rolling for duration would slow the table down for no payoff — explicitly identified in-session as the right fit for something like Gather Information, where a per-roll time cost would be pure friction.

---

### Option B — Margin/Quality-Scaled Duration

**Mechanism:** `Duration = BaseDuration × 2^(−Margin / K)`, reusing the Margin or Quality value the S-1 Opposed Contest (or a solo Core Test) already computes every time it resolves. A larger Margin (a more decisive success) compresses the duration; a bare success or a near-miss failure stretches it. `K` is a tuning constant requiring its own ruling.

**Precedent:** GURPS's Time-Spent ladder (each doubling/halving of time taken is worth a flat ±1 to the roll), repurposed to run in the opposite direction — instead of spending extra time to buy a bonus, the roll's own quality determines how much time was spent.

**Invariant/precedent fit:** No new roll, no new stat — Margin/Quality already exists post-resolution for every contested and most uncontested tests (DEC-013 §13.2). Fits Invariant 17/18 cleanly.

**Positives**
- Free in the literal sense: the input value is already sitting on the table before this option does anything with it.
- Rewards competence directly and continuously, not just at pass/fail — a narrow success and a dominant success feel mechanically different, which reinforces Priority 1.
- Creates a natural "critical success = did it in a flash" and "scraped by = took forever" narrative texture without any new subsystem.
- Composable with almost every other option in this catalog as a *modifier* layer (e.g., combine with A's base duration).

**Negatives**
- Needs a tuning constant (`K`) authored and validated — get it wrong and either every task feels instant or every task feels glacial; this is exactly the kind of numeric threshold the LLM Governance Rules (Rule 5) forbid inferring without explicit locking.
- Does nothing for actions with no opposed/quality dimension (a flat, uncontested lookup-table hazard tick, for instance) — needs a fallback for those cases.
- Margin is a *contest*-scoped value; using it to drive duration for non-contested Extended Test intervals (DEC-067's Margin-accumulation) risks conflating "progress toward a goal" with "how long this step took," which are conceptually different numbers currently sharing one name.
- Exponential/logarithmic scaling is elegant on paper but can produce unintuitive results at the tails (a Skill-Tier-5 master finishing something in a fraction of a second) unless clamped.

**Best-fit domain:** Contested or Quality-bearing tests where "how well you did it" should visibly change "how long it took" — combat exchanges and skill-vs-skill social contests are the natural home.

---

### Option C — Skill-Tier-Scaled Duration

**Mechanism:** `Duration = BaseDuration / SkillTier` (or another monotonic decreasing function of Skill-Tier), keying duration to the same Skill-Tier axis that already governs Effect Tier (DEC-107), Location-resolution depth (DEC-112/DEC-136), and the Crafting Tier-combination/gate rules (DEC-141/DEC-142).

**Precedent:** Wurm Online's principle that higher effective skill shortens an action's real-time cost, translated into Tiwas's own already-load-bearing Tier axis instead of a raw skill number.

**Invariant/precedent fit:** No new stat. Reuses the single variable Tiwas keeps reaching for every time it needs a universal scaling dial — this is the option with the strongest "this is obviously how Tiwas would do it" argument, since the designer has independently converged on Skill-Tier as *the* scaling axis at least four separate times (DEC-041, DEC-107, DEC-112, DEC-141/142).

**Positives**
- Highest internal-consistency score of any option in this catalog — it doesn't introduce a new idiom, it extends an existing one that Tiwa has already ruled on repeatedly.
- Rewards the *investment* dimension of skill (advancing through Advanced Skill Tiers) rather than the *luck* dimension (a single good roll) — complementary to Option B rather than redundant with it.
- Stable and predictable per-character: a given character's crafting speed doesn't fluctuate roll-to-roll, which suits long-form Extended Test planning (how many intervals will this realistically take?).
- Simple integer/rational-function math, easy to implement in an automated runner.

**Negatives**
- Tier is a coarse variable (integer steps) — duration compression happens in large discrete jumps rather than smoothly, which can feel lumpy compared to a continuous formula.
- Divorces duration entirely from the specific roll result — two attempts at the same Tier take the same time regardless of how well or badly either one actually went, which loses the "critical success felt instant" texture Option B provides.
- At very high Tiers the function risks producing near-zero or degenerate durations unless floored (mirrors the real problem GURPS's own Takes-Extra-Time doubling ladder ran into at extreme levels).
- Does not by itself address hazard exposure, travel, or any action with no clear "acting Skill-Tier" (e.g., waiting, resting, passive perception).

**Best-fit domain:** Crafting and Extended Test planning, where a character's *build* (not their luck on a given roll) should determine throughput — directly complements the already-ruled DEC-141/142 crafting Tier machinery.

---

### Option D — Roll/Cost-Coupled Duration

**Mechanism:** `Duration = NaturalRoll × k`, reusing the exact d100 result that is already spent as Cost (DEC-006 step 4/DEC-007). No second number is computed; duration is a linear function of the same value already on the table.

**Precedent:** No single direct external precedent — this is Tiwas-native, extrapolating the system's own recurring pattern (Zero-Step, Cost, Failure XP all already derive everything from the one natural roll) into the time dimension.

**Invariant/precedent fit:** Cheapest possible option in this entire catalog — literally zero new computation, since the value already exists by the time Duration would be needed (step 4 of the 9-step Core Test Transaction).

**Positives**
- Free of charge, more so than any other option — there is nothing left to compute.
- Ties Duration to the same unforgiving randomness that already governs Cost, which gives travel and unknown-environment scenarios a genuine "you don't know how long this will take until you commit to it" texture — you don't find out the real cost of the attempt (in either resource or time) until the die is already cast.
- Extremely easy to automate; an unattended runner already has this number in hand for every single Core Test resolved.
- Thematically apt specifically for **unknown or hostile environments**, where real unpredictability (not skill, not narrative pacing) should govern how long something takes — a scouting run through unmapped terrain is exactly the kind of task where "you don't get to know in advance" is the point.

**Negatives**
- Directly inverts the competence relationship: a low roll (which succeeds more cheaply and safely under Tiwas's own Cost model) also *finishes fastest*, meaning skilled characters rolling conservatively low numbers are both cheaper *and* faster than a roll that barely scrapes by — this can read as backwards for tasks where mastery should mean speed, not luck.
- Provides no signal that competence matters at all for the time dimension — a Tier-1 novice and a Tier-5 master rolling the same number take identically long, same flaw as Option A but for the opposite reason (randomness instead of flatness).
- The tuning constant `k` still needs authoring and needs separate calibration per action category (a roll-driven combat exchange and a roll-driven three-day trek cannot share one `k`).
- Can produce jarring outliers: a 100-Fumble (which is guaranteed on every character regardless of Skill) would, under a naive reading, always produce the longest possible duration — appropriate for a botched action, but needs explicit ruling to confirm that's the intended outcome rather than an accident of the formula.

**Best-fit domain:** Travel and exploration through unknown or hostile environments, where the uncertainty of "how long will this actually take" is itself part of the danger — explicitly identified in-session as the strongest fit for this option.

---

### Option E — Canonical Abstract Time Bands

**Mechanism:** Define an ordered, qualitative set of Time Bands (e.g., Instant / Short / Medium / Long / Extended) with no canonical real-world value attached to any of them — only their relative ordering is locked. This is the direct structural twin of DEC-133's four Distance Bands (Engagement/Short/Medium/Far), applied to the time axis instead of the space axis.

**Precedent:** Torchbearer's unitless Turn concept, formalized into an explicit ordered enum the way Tiwas already formalized abstract distance.

**Invariant/precedent fit:** No new resource, no new roll, no numeric commitment at all — the safest possible ruling in terms of surface area, since it only locks an *ordering*, not a *value*.

**Positives**
- Near-perfect structural mirror of an architecture Tiwa has already ruled and accepted (DEC-133) — minimizes the risk of the ruling feeling inconsistent with the rest of the corpus.
- Never forces a real-world number that later evidence might contradict — bands can be re-anchored to different real-world values later (exactly as DEC-133 deferred hex-count boundaries to content-authoring) without reopening the Core ruling itself.
- Gives every subsystem (combat, Extended Tests, hazards, crafting) a shared vocabulary to reference ("this takes a Long interval") without requiring any of them to agree on what a "Long" actually is in seconds.
- Extremely low ruling-surface risk — a single ordered list is close to impossible to get wrong in a way that requires later walking back.

**Negatives**
- By itself, solves nothing for automation — an unattended runner still cannot compute anything from "this took a Medium amount of time" without a second, separate conversion layer (which is exactly what Option F is for).
- Risks becoming exactly the kind of ornamental vocabulary DEC-133 warns against if the bands are never actually consumed by any rule (a Distance Band that never gates anything is just flavor text).
- Requires every consuming subsystem (Extended Tests, Hazards, Crafting) to be individually retrofitted to reference the band system, which is a broader content-authoring lift than a single formula.
- Ordering-only locks can still generate table disputes about *where* a given action sits in the ordering, even without a numeric fight — "is lockpicking a Short or a Medium task?" is still a live question this option doesn't answer.

**Best-fit domain:** The canonical Core-layer answer, if Tiwa wants a rules-text-level architecture rather than a formula — pairs naturally with Option F to become usable by automated runners.

---

### Option F — Automation-Only Conversion Convention

**Mechanism:** Leave the table-play/Core layer abstract (per Option E, or per GM discretion generally), but author a **scoped, non-canonical** conversion table (band → real seconds, or turn → real seconds) that applies *only* to unattended automated runs. Exact structural precedent: the Automated Playtest Run Conventions (H1–H8), which already solved an identical class of problem for S-11 healing amounts (DEC-072.A) without touching DEC-070/DEC-074's table-level GM discretion.

**Precedent:** Tiwas's own H-block conventions, applied to a new domain.

**Invariant/precedent fit:** Explicitly scoped to exclude table play — cannot conflict with DEC-070/DEC-074/DEC-130 (GM Fiat, bounded universality) because it never claims to bind a human GM in the first place.

**Positives**
- Directly and completely solves the stated automation problem, which none of the table-facing options (A–D, G, L, M, N) do on their own without this layer or something functionally identical to it.
- Zero risk to table play — a human GM's discretion is completely untouched, exactly the same non-interference guarantee the existing H1–H8 block already provides for healing.
- Can be iterated on independently and rapidly (it's a convention document, not a Core Rules change) — if the conversion numbers turn out to feel wrong in playtesting, revising them doesn't require reopening any Canonical or Ruled non-canonical text.
- Precedent-proven: this exact pattern already shipped successfully once (DEC-072.A) for a structurally similar "automated runs need a number that table play deliberately declined to fix" problem.

**Negatives**
- Does not, by itself, answer G3 as a design question — it is a workaround for the *symptom* (automated runners need a number) rather than the underlying question (what should time mean in Tiwas at all), so Tiwa may reasonably want a Core answer eventually regardless.
- Introduces a second, parallel "meaning" of duration — one for humans (unspecified, GM's call) and one for automation (a specific authored number) — which risks the two drifting apart if either is revised without the other being checked.
- Requires *something* upstream to convert from (a band, a category, a formula) — Option F is not self-sufficient; it is explicitly a layer that sits on top of another option, not a standalone answer.
- If automated-run results are ever meant to validate or inform table-play tuning (as several existing playtest reports already do), a purely automation-scoped convention risks producing numbers that don't actually reflect intended table pacing.

**Best-fit domain:** Unattended automated/unattended runs specifically (the Claude/GPT/Grok runner packets) — the single most directly-requested use case in this research.

---

### Option G — Full Wurm-Style Derived Action-Duration Formula

**Mechanism:** `Duration = BaseDuration × f(EffectiveSkill, Cap) − ToolQualityBonus − StaminaFactor` — a genuine port of Wurm Online's actual formula shape: effective skill and tool quality reduce the base time, current stamina/resource level further modifies it, and the result is floored near some minimum.

**Precedent:** Wurm Online directly and explicitly, as named in the original request.

**Invariant/precedent fit:** Does not create a new resource *pool*, but does introduce a new *derived value* (an Action-Duration output) with more moving parts than any other option — the largest surface area for accidental Invariant 18 friction ("a parallel resolution engine") if implemented carelessly, though a purely output-only formula (no independent roll, no independent resource spend) should not actually cross that line.

**Positives**
- Highest fidelity to the named reference system — if "make it feel like Wurm" is a design goal for crafting specifically, this is the only option that actually delivers that texture rather than approximating it.
- Captures three genuinely distinct inputs (skill, equipment quality, current exertion) in one formula, giving crafting content authors multiple levers to differentiate recipes and tools meaningfully.
- Naturally produces the "steady, measurable progress" feel explicitly praised about Wurm's system in this research — a character's crafting throughput becomes a tangible, trackable resource in its own right.
- Directly usable by the Crafting subsystem work already in progress (the Wurm-adaptation documents, DEC-141/DEC-142), since it's the same lineage of content already being ported.

**Negatives**
- By far the largest ruling and implementation surface of any option in this catalog — multiple sub-questions (what counts as EffectiveSkill here, how Tool Quality is sourced from the Item Tier/Magnitude record, how Stamina/current-resource level factors in) each need their own sub-ruling, mirroring the multi-DEC sprawl the Wurm crafting adaptation already generated (DEC-141, DEC-142, and the still-open P5 tool/fixture-Tag precondition item).
- Highest risk of feeling over-engineered for anything outside crafting — applying a four-variable formula to "how long does this combat exchange take" would badly violate Priority 3 (minimum resolution steps).
- The floor/minimum-time problem Wurm itself struggles with (action times bottoming out at a hard few-second minimum regardless of skill) is a known rough edge in the source material, not a solved problem being imported cleanly.
- Highest content-authoring burden: every recipe, tool, and Extended Test category needs its own BaseDuration authored before this formula does anything, front-loading a large amount of work before any payoff is visible.

**Best-fit domain:** Crafting specifically, where the granular, multi-input simulation texture is a genuine design goal — not recommended as a universal answer for combat or simple downtime tasks.

---

### Option H — Formally Leave Reserved (No Answer)

**Mechanism:** Rule explicitly that G3 does not require resolution at this time — an intentional, documented non-decision rather than silent neglect. Time is only tracked mechanically when something is actually *consumed* by its passage (light, food, a Clock-style countdown); absent such a consumable, no duration answer is needed at all.

**Precedent:** Torchbearer and Blades in the Dark both operate this way at the Core level — neither game defines "how long a Turn is" as a first-class rule, because neither game's core loop actually requires that number to function.

**Invariant/precedent fit:** Trivially compliant with everything — a non-decision cannot violate an invariant.

**Positives**
- Costs literally nothing to implement and cannot be "wrong" in the way a numeric ruling can be.
- Consistent with the corpus's own explicit governance discipline (Roadmap §24 Rule 6: "never silently resolve an open designer fork") — this option is the *deliberate*, on-the-record version of that discipline rather than a violation of it.
- Keeps the door open for a narrower, better-informed ruling later, once actual play data shows which domains genuinely need a duration answer and which don't.
- Avoids over-committing Tiwas to a universal formula before the Crafting, Hazards, and Time/Action subsystems (all still partially open) have matured enough to reveal what they actually need from a duration model.

**Negatives**
- Does not solve the stated problem — an automated runner still has nothing to compute with, so this option alone leaves the original motivating issue (unattended systems need *some* answer) completely unaddressed.
- Risks becoming a permanent non-answer by default, the way several other "flagged, not ruled" items in the corpus have lingered for many sessions once nothing forces the question back onto the table.
- Undersells how central Skill Tests already are to the game (per the design brief's own emphasis) — a system this granular deferring the *time* dimension indefinitely sits somewhat awkwardly next to how precisely everything else is specified.

**Best-fit domain:** Not a standalone recommendation for Tiwas given the stated automation requirement — included for completeness and because it is the only option that is unambiguously safe to fall back on if none of the others survive scrutiny.

---

### Option I — Resource-Attrition Timekeeping

**Mechanism:** Do not measure time in minutes or turns at all. Instead, define time operationally as "however long it takes to consume one unit of a tracked resource" — a torch, a ration, an ammunition count. The passage of time is entirely inferred from resource depletion; no independent clock exists.

**Precedent:** Torchbearer's light/rations-driven dungeon-turn pressure, where the *only* thing that must stay consistent turn-to-turn is the consumable countdown, not an actual elapsed-time figure.

**Invariant/precedent fit:** Does not create a new resource pool by itself — it *reuses* whatever consumables a scene already tracks (light sources, rations, ammunition, charges) rather than inventing a duration-specific one, so Invariant 17 is not implicated.

**Positives**
- Produces genuine mechanical stakes for time passing without ever needing to answer "how many minutes was that" — the pressure is real (your torch is running out) even though the underlying clock is never stated in real units.
- Extremely well-suited to survival/dungeon-crawl pacing, which is exactly the genre this technique comes from and excels at.
- Composable with almost any other option as the "why does duration matter" layer sitting on top of whichever option answers "how long did it take."
- Naturally self-balancing: if resources are scarce, time pressure is high; if resources are abundant, time pressure organically relaxes, without any GM needing to hand-tune a numeric clock.

**Negatives**
- Only meaningful in scenes that actually have a trackable consumable — combat exchanges, social contests, and most Extended Tests have no natural "torch" to burn, so this option has a narrow domain of applicability on its own.
- Does not answer the automation problem at all by itself — an unattended runner still needs to know *how many actions per consumable unit*, which just relocates the original unanswered question rather than resolving it.
- Can feel disconnected from genuine simulation fidelity (Priority 1) if the resource-burn rate itself is arbitrary rather than grounded in an actual duration model underneath it.
- Doesn't interact cleanly with Tiwas's existing resource economy (PE/MP/Overflow) without care — needs to be a clearly separate tracked consumable, not accidentally folded into the Core resource pools, to avoid Invariant 17 friction.

**Best-fit domain:** Dungeon-crawl and wilderness-survival downtime scenes specifically, as a stakes layer rather than a universal time-unit answer.

---

### Option J — Time-as-Interval-Count

**Mechanism:** Formalize the Extended Test interval (already ruled, DEC-067/DEC-073) as the atomic unit of time, full stop. "How long did this take?" is answered entirely in intervals ("four intervals"), and any real-world translation is optional flavor text that never becomes load-bearing on any rule.

**Precedent:** A direct extension of Tiwas's own already-Ruled Extended Test machinery — not an import from an external system, but a formalization of what DEC-067/070/073 are already implicitly doing.

**Invariant/precedent fit:** Zero new mechanics — this option adds a *label*, not a *system*, to something already fully specified.

**Positives**
- The cheapest possible ruling that still gives players and content authors a concrete, comparable unit ("this recipe takes about twice as many intervals as that one") without inventing anything new.
- Naturally scales with whatever progress model governs the interval (Margin-accumulation, DEC-067) — a faster character reaches the completion target in fewer intervals automatically, without a separate duration formula being needed at all.
- Sidesteps the entire real-world-time debate for the specific domain (crafting, healing, research) where Extended Tests already dominate.
- Trivially automatable — an unattended runner already counts intervals as part of resolving an Extended Test; no new value needs to be computed.

**Negatives**
- Explicitly does not answer "how long is an interval" — which means it solves nothing for combat, single-roll hazards, or any domain that isn't already structured as an Extended Test.
- Risks becoming indistinguishable from Option H (a non-answer) in practice if no real-world anchor is ever attached to an interval, since two campaigns could implicitly run "an interval" as anything from a minute to a week with no rule catching the inconsistency.
- Narrative pacing suffers if a GM or a written adventure needs to say something concrete ("they arrive back in three days") and the only available unit is an abstract interval count with no declared real-world size.

**Best-fit domain:** Extended Test-governed content specifically (crafting, healing, research, long-form travel-as-Extended-Test) — the natural native unit for exactly the subsystem it's drawn from.

---

### Option K — Movement-Speed-Derived Travel Time

**Mechanism:** `Time-per-Band = Band-hex-count ÷ effective Movement Speed`, running DEC-133's own canonical relationship (`1 Movement Speed = 1 hex per combat turn`) in reverse to derive a travel duration instead of a travel distance, reusing the already-canonical derived statistic rather than a flat lookup table or a raw roll.

**Precedent:** No external system directly; this is a refinement of Option D specifically, engineered to reuse DEC-133's canonical formula instead of the raw natural roll, so that a faster character (higher Movement Speed) genuinely travels faster rather than a luckier one.

**Invariant/precedent fit:** No new stat, no new formula shape — Movement Speed and the hex-per-turn relationship are both already Canonical (DEC-133). This option is close to a "free" extension in the same sense Option D is, but grounded in competence rather than randomness.

**Positives**
- Directly answers the travel-in-unknown-terrain use case the same way Option D does, but ties the outcome to a *stable, canonical character stat* rather than a single roll — a scout with high Movement Speed reliably covers ground faster, which matches player intuition better than a roll-driven outcome would.
- Reuses a formula and a stat that are both already Ruled and Locked (DEC-004's Movement Speed formula, DEC-133's hex/turn relationship) — essentially zero new ruling surface.
- Naturally interacts with existing Movement-penalty overlays (DEC-138's uniform `Tier-Y Condition Value Z` formula for Encumbered/Slowed/etc.) without any extra work, since those overlays already modify *effective* Movement Speed, which this option consumes directly.
- Scales cleanly across all four Distance Bands using the exact same formula, with per-band hex counts as the only content-authored input needed (already flagged as deferred content in DEC-133 R1).

**Negatives**
- Inherits DEC-133's own still-open item: the hex-count-per-band boundaries remain content-authoring, so this option cannot produce a real number until that content is authored regardless of whether the formula itself is ruled.
- Removes the "you don't know how long this will take" uncertainty that made Option D specifically well-suited to unknown/hostile terrain — a Movement-Speed-based formula is fully predictable in advance, which may undersell the danger of unmapped or adversarial environments.
- Only answers *movement* duration — does nothing for combat exchanges, crafting, or hazard exposure, so it is narrowly scoped by design rather than a universal candidate.
- Does not account for terrain difficulty, obstacles, or narrative complications on its own — would likely need to be paired with a difficulty-grade modifier (DEC-063's Skill-side penalty architecture, applied to effective Movement Speed) to feel complete for genuinely hostile terrain.

**Best-fit domain:** A direct refinement/alternative to Option D for the same travel use case — recommended specifically where *predictable, competence-driven* travel time is wanted (known or partially-known routes) rather than *stakes-driven uncertainty* (Option D's better fit for truly unknown terrain).

---

### Option L — Per-Task Authored Duration

**Mechanism:** Every individual recipe, spell, hazard, or task carries its own explicit, hand-authored `duration` value set at content-creation time (DEC-077.A content-authoring), exactly the same way each already carries its own Skill-Tier gate (DEC-142) or Tier-combination rule (DEC-141). There is no universal formula at all — a content author simply writes "Forge a Steel Longsword: 6 intervals" once.

**Precedent:** Traveller-style per-task authored time requirements, and directly parallel to Tiwas's own already-ruled pattern of per-recipe authored gates (DEC-142's `min_skill_tier` field).

**Invariant/precedent fit:** No formula, no new mechanic — purely a content-authoring convention layered onto records that already support arbitrary authored fields.

**Positives**
- The cheapest way to get *concrete, usable numbers* into the game immediately, without waiting on a universal G3 formula to be designed, argued over, and ruled first — directly unblocks the in-progress Tier-1 crafting catalog work.
- Maximum content-author control: a legendary, dramatically-important recipe can simply be authored to take longer than a mundane one, with no formula fighting that intent.
- Zero risk of a universal formula producing a degenerate or silly result for some edge-case task nobody anticipated — each task's duration is a deliberate, individually-reviewed choice.
- Matches the "simplification, can be expanded on later" philosophy Tiwa has explicitly used to close both DEC-141 and DEC-142 — this option is the natural third leg of that same design posture applied to time.

**Negatives**
- Provides zero systemic consistency — nothing stops two structurally identical tasks from being authored with wildly different, unjustified durations unless a human author is disciplined about it, and there's no formula to catch the inconsistency.
- Doesn't scale with player choices at all (no Skill-Tier, no Margin, no roll influences it) — a Tier-5 master and a Tier-1 novice take the same authored duration for the same recipe unless a *second* mechanism (Options B/C/D/G) is layered on top.
- Front-loads a large, ongoing authoring burden onto every future piece of content — every new recipe, spell, or hazard now needs an explicit duration decision, which is easy to forget or under-specify.
- Does nothing for player-facing or improvised actions that were never pre-authored (a GM invents an action on the spot) — has no fallback for anything outside a curated content catalog.

**Best-fit domain:** Crafting/recipe catalogs specifically, where content is already being individually authored with per-recipe fields — the natural extension of work already underway.

---

### Option M — Time–Energy Tradeoff

**Mechanism:** A player may deliberately overspend Energy or MP beyond the Core Test's normal Cost (accepting the associated Overflow risk, DEC-007) in exchange for compressing whatever Duration value another option (A/B/C/D/G/L) would otherwise produce. This is not a competing duration model — it is a *modifier layer* that sits on top of any of the others, giving the player agency over the dial rather than the system dictating it unilaterally.

**Precedent:** GURPS's Hurrying penalty (a flat roll penalty for compressing a task's time), reframed through Tiwas's own existing Overflow mechanic instead of a new penalty type.

**Invariant/precedent fit:** Reuses Overflow exactly as already Ruled and Locked (DEC-007, DEC-007.A's immutability clause is respected — this option never modifies Overflow's magnitude or calculation, it only changes the *player's decision* to accept more of it) — no new resource pool, no new roll type.

**Positives**
- Directly answers the stated design value of player agency and flexibility — this is the one option in the entire catalog that is explicitly *about* giving players a meaningful choice over the time dimension rather than the system imposing one outcome.
- Creates a genuine tactical tradeoff (push yourself and risk more HP damage via Overflow, versus play it safe and take longer) using machinery that already exists in its entirety — nothing new needs to be built, only a rule connecting an existing mechanic (Overflow) to a new consequence (Duration).
- Composable with essentially every other option in the catalog without conflict, since it modifies an *output* of whichever base model is chosen rather than replacing that model.
- Thematically consistent with Tiwas's stated Priority 2 (heroic resilience / low permanent loss) paired against Priority 1 (granular simulation) — pushing through Overflow to save time is exactly the kind of "risk resources, not the character's life" tension the design priorities already ask for elsewhere (Overflow damages HP, but HP=0 is only incapacitation, not death, per DEC-052).
- Low ruling surface: the only genuinely new content is the conversion rate between "extra Energy/MP spent" and "Duration reduced," which is a single tunable relationship, not a whole subsystem.

**Negatives**
- Is not a standalone answer to G3 — it presupposes a base Duration model already exists to compress, meaning it must always be paired with at least one of A/B/C/D/G/L, adding to total ruling surface rather than reducing it.
- Risks becoming the dominant strategy if the tradeoff is tuned too generously (every task gets rushed via Overflow every time), which would flatten whatever texture the base Duration model was trying to create.
- Needs an explicit ruling on whether NPCs/creatures can access this tradeoff the same way PCs can, mirroring the PC/creature symmetry questions the corpus has repeatedly had to resolve elsewhere (DEC-140's universal-Advanced-Skill ruling being the most recent precedent for "don't assume PC-only without saying so").
- Overflow already damages HP directly and immutably (DEC-007.A) — stacking a deliberate "spend more, take Overflow, go faster" incentive on top of an already-punishing mechanic needs careful balancing to avoid making rushing simply too costly to ever be worth it in practice, which would make the option exist on paper but never get used at the table.

**Best-fit domain:** A universal *modifier* layer, not a domain-specific base model — recommended as an add-on to whichever base Duration option(s) Tiwa selects, specifically to preserve player agency across all of them.

---

### Option N — Independent Duration Roll

**Mechanism:** A dedicated die roll, separate from the Core Test's d100, made once per task category, determines how long the task takes — success/failure of the *task itself* remains entirely on the normal d100 roll-under check, while Duration is resolved by its own independent probabilistic roll.

**Precedent:** GURPS's own community-extension "5d for Takes-Extra-Time" model (a dice roll producing a randomized but centrally-tendencied duration, distinct from the success/failure roll).

**Invariant/precedent fit:** The one option in this catalog most likely to draw scrutiny under Invariant 18 ("no Universal Play subsystem may introduce a competing primary resolution transaction") — a second, independent roll type sits closer to "a parallel resolution engine" than any reuse-based option does, even though it doesn't touch Cost/Overflow/Failure XP and so may survive review if scoped narrowly and explicitly flagged for Tiwa's attention.

**Positives**
- Keeps "how long did this take" genuinely uncertain and interesting in its own right, for the specific cases where that uncertainty is dramatically valuable — building a keep, brewing a legendary potion, or any other rare, high-stakes undertaking where the answer shouldn't be fully derivable in advance from Skill-Tier alone.
- Decouples duration uncertainty from the success/failure uncertainty entirely — a task can be guaranteed to succeed eventually while still being genuinely unpredictable in how long it takes, which none of the roll-reuse options (B, D) can represent cleanly since they tie duration directly to the same roll that determined success.
- Can be scoped very narrowly (rare/unique undertakings only) to minimize its Invariant 18 exposure, rather than being proposed as a universal mechanic.

**Negatives**
- Highest process risk of any option in this catalog — explicitly flagged here as needing direct Invariant 18 review before Tiwa treats it as a live candidate, given the corpus's consistent, repeated rejection of "a second roll type" wherever it has come up elsewhere (Extended Tests deliberately reuse the ordinary Core Test rather than inventing a progress-roll, DEC-067/073).
- Adds table-time overhead exactly where Priority 3 (minimum resolution steps) argues against it — an extra roll per task, however occasional, is still literally the opposite of minimizing resolution steps.
- Needs its own die-size, target-curve, and modifier design from scratch — unlike every reuse-based option in this catalog, there is no existing value to repurpose, so this is genuinely new subsystem work, not an extension of something already Ruled.
- Redundant with Option B for most practical purposes (both produce a probabilistic duration distinct from a flat lookup) while carrying strictly higher implementation and governance risk than Option B does — hard to justify choosing this over B unless the specific goal of decoupling duration-luck from success-luck is a deliberate design priority in its own right.

**Best-fit domain:** Rare, dramatically significant undertakings only, if Tiwa specifically wants duration-luck and success-luck to be independent variables — not recommended as a general-purpose answer given its governance risk and redundancy with Option B.

---

### Option O — Reuse the Existing StateRecord `duration` Field

**Mechanism:** DEC-117 R2 already defines a `duration` field on every unified StateRecord (Effect, Condition, Tag alike), currently populated with the enum `instant / scene / session / permanent`. Rather than building any new time-unit architecture, extend that already-shipped enum with a small number of additional coarse buckets (e.g., `interval`, `downtime-block`) and let the field that already touches every Effect/Condition/Wound/Tag in the game carry G3's entire weight.

**Precedent:** No external system — this is a pure internal-reuse option, spotting dormant capacity already sitting in the Unified StateRecord schema rather than importing anything new.

**Invariant/precedent fit:** The lowest-surface-area option of the entire catalog for anyone wanting an actual *ruling* rather than a deferral — it is literally editing one enum's value list on a field that already exists everywhere, not introducing a new mechanic, pool, formula, or roll of any kind.

**Positives**
- Genuinely the cheapest possible *positive* ruling (as opposed to Option H's cheapest *non*-ruling) — a single amendment to DEC-117's enum, not a new DEC family.
- Immediately and retroactively applies to every Effect, Condition, Wound, and Tag already in the game, since all of them already carry this field — no retrofitting of existing content is required at all.
- Naturally pairs with Option E (bands) or Option J (interval-count) as the controlled vocabulary those options would write their values *into* — this option is best understood as the plumbing that other options would use, not a competitor to them.
- Minimizes the risk of the ruling ever needing to be walked back, since widening an enum is close to strictly additive and unlikely to conflict with anything already built on the narrower version.

**Negatives**
- By itself, still doesn't produce a real-world duration number any more than Option E does — it only gives the vocabulary a home, not a meaning; automation still needs Option F (or something like it) layered on top regardless.
- The existing enum values (`scene`, `session`) were authored with a *narrative* pacing intent (how long does this Condition persist in the story), not necessarily a *mechanical* duration intent (how long did the action that created it take) — conflating the two purposes inside one field risks muddying what the field means going forward, and may need its own clarifying sub-ruling to keep the two uses distinct.
- Solves the vocabulary problem but leaves every actual numeric or comparative question (is `interval` longer or shorter than `scene`?) completely open, meaning it functions more as an infrastructure decision than as an answer to G3 in the sense the user originally asked about.
- Easy to under-value in a ruling discussion precisely because it's so cheap — there's a risk Tiwa treats it as "too small to be the real G3 answer" and looks past it in favor of a more visible option, even though it may be the most efficient piece of the eventual solution.

**Best-fit domain:** Infrastructure — the recommended first move regardless of which other option(s) Tiwa selects, since it costs almost nothing and every other option benefits from having a shared vocabulary field to write into.

---

## 5. Categorization Taxonomy

The fifteen options sort cleanly into five functional families, grouped by *design philosophy* rather than by use case:

| Category | Options | Defining trait |
|---|---|---|
| **I — Deterministic Fixed-Value Systems** | A, L | One flat, pre-set duration per category or per task. No formula, no roll, no scaling variable of any kind. |
| **II — Roll/Skill-Derived Scaling Systems** | B, C, D, G, K, N | Duration is *computed* from some existing or new variable (Margin, Skill-Tier, the natural roll, a multi-input formula, Movement Speed, or a dedicated new roll). |
| **III — Abstract / Non-Real-Time Systems** | E, H, I, J | Deliberately decline to commit to a real-world numeric meaning for time; time is represented ordinally, operationally (via consumption), or not represented at all. |
| **IV — Automation & Infrastructure Layer** | F, O | Not competing duration *models* at all — scoped conventions and schema plumbing that other options depend on to actually function, especially for unattended play. |
| **V — Player-Agency Modifier Layer** | M | A tradeoff mechanic that sits on top of any base model from Categories I–III rather than replacing one. |

---

## 6. Cross-Category Comparison

The user's own suggested comparison axes — **fastest**, **simplest resolution**, **most realistic**, **most granular** — are used below alongside three additional axes identified as decision-relevant during this research: **automatability without a GM**, **player agency**, and **ruling/implementation cost**.

### 6.1 Comparison Matrix

| Axis | I — Fixed | II — Roll/Skill-Scaled | III — Abstract/Non-Real-Time | IV — Automation/Infra | V — Player-Agency Modifier |
|---|---|---|---|---|---|
| **Table speed (fastest to resolve)** | Very High | Medium | High (E/H/J) to Medium (I) | N/A (not table-facing) | Low overhead (single extra decision) |
| **Simplicity of ruling** | Very High | Low–Medium (varies widely: D is nearly free, G is the most complex ruling in the entire catalog) | High | Very High (F: proven pattern; O: near-trivial) | Medium |
| **Realism / simulation fidelity** | Low | High (especially C, G) | Low–Medium | N/A | Medium (adds a realistic risk/speed tradeoff) |
| **Granularity** | Very Low | Very High | Low | N/A | N/A (modifies granularity of whatever it's layered on) |
| **Automatable without a human GM** | Yes, trivially | Yes for B/C/D/K; No (needs Fiat) for N without extra scoping | No, unless paired with IV | Yes — this is the category's entire purpose | Yes, if the base model it modifies is automatable |
| **Player agency / flexibility** | Very Low | Low–Medium (the system decides, not the player) | Low–Medium | N/A | Very High — this is the category's entire purpose |
| **Implementation / ruling cost** | Very Low | Medium (B/C/D/K) to High (G, N) | Very Low (E/H/J) | Very Low | Low (assuming a base model already exists) |
| **Consistency with existing Tiwas idiom** | Medium (mirrors DEC-093) | High (C, K explicitly reuse ruled Tiwas variables; D extends the "everything derives from the roll" idiom) | Very High (E mirrors DEC-133 almost exactly) | Very High (F mirrors the H1–H8 block precedent exactly; O reuses an existing field) | High (reuses Overflow exactly as ruled) |

### 6.2 Narrative Comparison by Axis

**Fastest at the table:** Category I (A, L) wins outright — a lookup or an authored value requires zero computation. Category III's E, H, and J are close seconds since they require no math either, only a categorical judgment. Category II is the slowest of the base-model categories, since every option in it requires at least one arithmetic step after the roll resolves; Option G is the slowest of all, requiring three separate inputs to be gathered and combined.

**Simplest resolution (fewest new rules/steps):** Categories I and IV tie for simplest in terms of raw rule-count, but for different reasons — Category I is simple because it commits to almost nothing (a flat table), while Category IV is simple because it deliberately reuses machinery that already exists in full (F reuses the H-block pattern; O reuses a field that's already on every record in the game). Category II's D is nearly as simple as either, since it reuses the natural roll with zero new computation — the simplicity of an option in Category II depends entirely on *which* input it reuses, which is why this category has the widest internal spread of any of the five.

**Most realistic:** Category II wins clearly, and within it, C and G are the strongest — C because it ties duration to the same competence axis (Skill-Tier) the rest of Tiwas already uses to represent mastery, and G because it's the most direct port of an actual real-world-feeling simulation (Wurm's own formula). Category I is the weakest performer on this axis by design — flat categories cannot represent competence differences at all.

**Most granular:** Category II again, decisively — every option in it produces a continuously (or near-continuously) varying output rather than a small fixed set of buckets. Option G is the single most granular option in the entire catalog, since it has the most independent inputs feeding the result. Category III is the *least* granular by design — E's entire purpose is to collapse duration into a small ordered set of bands rather than a precise number.

**Best for automation:** Category IV is purpose-built for this and is the clear winner — it is, definitionally, the category that exists to solve exactly this problem. Within Category II, B, C, D, and K are all fully automatable on their own since every input they need already exists mechanically; N is the weak link in the category because it requires inventing an entirely new roll mechanism, which is more implementation work for an automated runner to support than any of the others. Category III cannot be automated on its own at all — it requires a Category IV layer (specifically F) bolted on before an unattended runner can do anything with it.

**Most player agency / flexibility:** Category V is the only category built specifically around this axis, and nothing else in the catalog comes close on this dimension — every other category either hands the player a fixed number (I, III) or computes one algorithmically without the player choosing anything (II, IV). This directly matches the design value explicitly named as important: flexibility and player choice as one of Tiwas's best qualities. Notably, Category V cannot deliver this value *by itself* — it only exists as a modifier on top of one of the other four categories, meaning "maximum flexibility" in practice requires *combining* Category V with something else, not choosing Category V in isolation.

**Cheapest ruling / implementation surface:** Category IV again, with O as the single cheapest positive ruling in the whole catalog (editing an existing enum) and F as the cheapest way to solve automation specifically (a scoped convention document, proven pattern). Category III's H is cheaper still in an absolute sense, but only because it rules nothing at all — it is free precisely because it produces no value.

**Most consistent with existing Tiwas idiom:** This is close between Category III (E's direct mirror of DEC-133) and Category IV (F's direct mirror of DEC-072.A, and O's direct reuse of DEC-117), with Category II's C and K close behind due to their reuse of Skill-Tier and Movement Speed respectively. Category I is the least consistent with Tiwas's broader design idiom — the rest of the system is built almost entirely around variable, competence-driven outcomes, and a flat lookup table is the one architecture in this catalog that runs most against that grain.

---

## 7. Domain-Assignment Recommendation (Non-Binding)

Precedent exists in the corpus for exactly this shape of ruling — DEC-013 §13.3 already lets the GM select which Quality mode (Margin/Blackjack/Hybrid) governs a given contest rather than locking S-1 to one universal mode. G3 could plausibly be ruled the same way: not "Tiwas uses one Option for all time," but "different domains declare which Option(s) govern them," with Category V (M) available everywhere as an optional overlay. A possible non-binding mapping, informed entirely by the per-axis analysis above and by the specific use cases raised in-session:

| Domain | Suggested governing option(s) | Rationale (cross-referenced to §6) |
|---|---|---|
| Combat exchange | **A** (Category I) | Table speed is paramount mid-fight; DEC-095's turn structure already assumes uniform turn length |
| Gather Information / low-stakes social checks | **A** (Category I) | Explicitly identified as needing to avoid per-roll time overhead |
| Crafting | **L + G** (Category I base, Category II refinement) or **C** alone | Matches the in-progress Wurm-adaptation content lineage (DEC-141/142); G for full fidelity, C for a lighter-weight version |
| Travel, known/mapped route | **K** (Category II) | Predictable, competence-driven, reuses canonical Movement Speed |
| Travel, unknown/hostile environment | **D** (Category II) | Stakes-driven unpredictability is the explicit design goal here |
| Healing / Extended Tests generally | **J** (Category III) | Interval-count is already the native unit per DEC-067/073 |
| Dungeon/survival downtime | **I** (Category III) | Consumption-based stakes without needing a real clock |
| Any domain, as an overlay | **M** (Category V) | Preserves player agency regardless of which base model governs the domain |
| All domains, as infrastructure | **O**, then **F** for automated runs specifically | Lowest-cost prerequisites that every other choice benefits from |

---

## 8. Open Questions for Tiwa

1. Should G3 be ruled as a **single universal architecture** (one Option for everything) or a **per-domain assignment** (§7's model), mirroring the DEC-013 Quality-mode precedent?
2. If Option G (full Wurm-style formula) is pursued for Crafting, does it warrant its own DEC family the way the Wurm crafting adaptation already has (DEC-141/142, plus the still-open P5 tool/fixture-Tag precondition), or should it be folded into the existing crafting ruling chain directly?
3. Does Option N (independent duration roll) require an explicit Invariant 18 compatibility ruling before it can be considered a live candidate at all, given the corpus's consistent prior rejection of "a second roll type" (Extended Tests deliberately reusing the ordinary Core Test being the clearest precedent)?
4. If Option O is adopted, should the widened `duration` enum stay unified with DEC-117's existing narrative-pacing values (`scene`, `session`), or does it need a documented split between "narrative persistence" and "mechanical action duration" to avoid the two meanings colliding on one field?
5. Should Option F's automated-run conversion table be authored once G3's table-facing answer is chosen, or does the automation need unblocking *now*, independently, the same way the H1–H8 healing conventions were authored ahead of a full S-11 GM-discretion resolution?

---

## 9. Appendix — Source Reference List

### 9.1 In-corpus decisions referenced

DEC-004, DEC-006, DEC-007, DEC-007.A, DEC-013 (§13.2/§13.3), DEC-041, DEC-052, DEC-063, DEC-067, DEC-068, DEC-070, DEC-072.A, DEC-073, DEC-077.A, DEC-082, DEC-082.A, DEC-089–DEC-093, DEC-095, DEC-107, DEC-112, DEC-117 (R2), DEC-130, DEC-133, DEC-133.A, DEC-136, DEC-138, DEC-140, DEC-141, DEC-142; Roadmap §24 Rule 6; `governance/status-model.md` Status Lifecycle and Promotion Rule.

### 9.2 External precedent referenced (research pass, this session)

- **Wurm Online** (Wurmpedia: *Action*, *Action queue*, *Mind logic*, *Skills*, *Timers*) — real-time action-duration formula gated by skill/tool-QL/stamina; Mind Logic as a reused-stat queue-depth gate.
- **GURPS** (GURPS Wiki: *Time Spent*, *Takes Extra Time*, *Task Difficulty*, *Skills*) — logarithmic doubling/halving Time-Spent ladder; man-hours labor-task model; Hurrying penalty.
- **Blades in the Dark / Forged in the Dark** (RPGnet review; Mythcreants; The Angry GM; CBR; The RPG Study; Wikipedia) — Progress Clocks as a consequence-proximity tracker, explicitly not a timekeeping mechanic.
- **Torchbearer** (Mythcreants; The Angry GM) — abstract, unitless Turns; light/rations-driven downtime pressure.
- **D&D-lineage systems** — fixed, non-scaling real-world durations per category (background knowledge; not independently re-verified this session).

---

**End of report.**
