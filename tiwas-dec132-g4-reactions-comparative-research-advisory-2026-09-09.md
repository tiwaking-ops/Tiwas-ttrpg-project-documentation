---
document:
  title: "DEC-132 (G4 Reactions) — Comparative TTRPG Research & Options Advisory"
  version: "1.0"
  status: "Advisory session output — Non-canonical. Not a ruling. Pending Tiwa's review and, where applicable, the 8-step Promotion Rule (Proposals/WIP §21 / REQ-021)."
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm: []
  last_modified_by_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  created_date: "2026-09-09"
  last_modified_date: "2026-09-09"
---

# DEC-132 (G4 Reactions) — Comparative TTRPG Research & Options Advisory

## 0. Governance Notice

This document is an **advisory session output**, not a ruling. Per the project's standing
governance model (`governance/authority.md`, `governance/status-model.md`):

- Claude Sonnet 5 (this document's author) holds an **advisory role only** — it identifies
  options, surfaces conflicts, and drafts formal text, but never issues rulings or assigns
  DEC numbers.
- **Tiwa** holds sole human ruling authority over Tiwas TTRPG.
- **OpenCode ("big-pickle")** is the sole documentarian with live repository access; it
  formally records rulings only after Tiwa's explicit sign-off.

Nothing in this report should be recorded to `decision-register.md`, the canonical rules
file, or any other project document as-is. It is a research and options package awaiting
Tiwa's ruling on the three carried-open items under DEC-132.

## 1. Session Scope

DEC-132 (G4 — Reactions beyond Active Defense) was ruled 2026-09-07 as a **framework**
(Option C: structured tag-triggered reactions). Three items were explicitly carried open
at that time and are the subject of this session:

1. **Trigger menu content and exact reaction-granting Tag vocabulary** — what specific
   triggers exist, and what Tags grant reactions in response to them.
2. **Replace-vs-stack question** — whether a Reaction replaces or stacks with Active
   Defense (DEC-044–050) when both could apply to the same incoming Effect.
3. **Per-scene/frequency limits on Reactions** — whether any cap or throttle exists beyond
   normal resource cost.

A fourth, unprompted issue was surfaced during the session and is recorded here for
completeness even though it was not one of the three originally carried-open items:
whether a single trigger event can provoke Reactions from multiple party members
simultaneously (§4.4 below).

This report covers two linked deliverables produced in-session:

- **Part A** — an initial options brief (no external research), presenting concrete
  option sets for all three items.
- **Part B** — a comparative research pass across four published TTRPGs (D&D 5e,
  Pathfinder 2e, GURPS, Shadowrun 5e) plus a fifth partial comparator (World of Darkness/
  Chronicles of Darkness dice-pool splitting), used to pressure-test and refine Part A's
  options against real precedent.

## 2. Relevant Existing Rulings (Context, Unchanged by This Report)

The following locked/ruled material bounds every option considered below. None of it is
reopened or altered by this report.

| ID | Subject | Constraint imposed |
|---|---|---|
| DEC-082 | Time/Action economy | **No discrete action-point budget of any kind** — Skill-side/Movement-penalty expression only. Any option requiring a tracked "reaction slot" count conflicts with this locked ruling. |
| DEC-044–050 | Active Defense (S-6) | AD is a genuine, voluntary, uncapped (DEC-047) Core Test; post-hoc mitigation only (Model B, DEC-048); universal Effect eligibility including positive Effects (DEC-050 amendment). |
| DEC-006/007 | Core Test Transaction / Cost=Roll | Reactions, per DEC-132(2)(c), resolve as full S-1 combat exchanges — normal Cost, Overflow risk, Failure XP apply. |
| DEC-077.A | Content-authoring path | Trigger/Tag content for reactions is explicitly named as content-authoring in DEC-132(4), consistent with the project's general content-authoring-via-playtesting norm. |
| DEC-135 | Repeated-Defense fatigue (supersedes DEC-075) | Repeated Active Defense within a continuous defensive sequence escalates the existing `Fatigued` Condition (DEC-079) by one Tier per qualifying repeat, expressed via the unified StateRecord schema (DEC-115–117). Explicitly includes (F6) a clause covering "defensive reactions whose purpose is to mitigate the incoming Effect." |
| Invariant 17 | No competing resource/progression economy | Rules out any new pool, counter, or currency dedicated to reactions specifically. |

## 3. Part A — Initial Options Brief (Pre-Research)

### 3.1 Item 1 — Trigger menu content and Tag vocabulary

| Option | Description | Trade-off |
|---|---|---|
| A. Rule a starter vocabulary now | Author 3–6 concrete triggers and matching Tags immediately (e.g. `combat:opportunist`, `combat:guardian`), parallel to DEC-080's alpha 34-Tag list. | Table-ready immediately; some tension with content-via-playtesting norm, though DEC-080 is real precedent for framework-level Tag authoring. |
| B. Defer entirely to content-authoring | No baseline list ruled now; Tags authored per-creature/class/equipment as needed. | Matches current carried-open status; risk that Reactions go unexercised in the next playtest for lack of any granted Tag. |
| C. Rule trigger *categories*, defer exact wording | Lock a small taxonomy (movement-trigger, ally-targeted-trigger, HP-threshold-trigger, etc.) without locking specific Tags or phrasing. | Middle ground; gives content authors a template without pre-authoring specific combat content in a ruling session. |

### 3.2 Item 2 — Replace vs. stack with Active Defense

Underlying fork identified: DEC-132(2)(c) frames a Reaction as "a full S-1 combat
exchange" against the triggering combatant — structurally distinct from Active Defense,
which is post-hoc mitigation of an Effect already applied to the reactor (DEC-048). The
replace-vs-stack conflict is therefore narrower than it first appears — it only arises
where a Reaction-Tag is specifically authored to trigger on "an Effect is about to be
applied to me," the one case where Reaction and AD compete for the same moment.

| Option | Description | Trade-off |
|---|---|---|
| A. Always independent | AD and Reaction never compete; a defender may both AD and separately react to the same exchange if a Tag grants it. | Cleanest fit to DEC-132's literal text and DEC-044–050; risks two full Core Tests off one attacker action. |
| B. Exclusive per trigger-moment | Where a Reaction's trigger coincides with an incoming-Effect moment, the defender must choose AD or Reaction, not both. | Prevents double-response; but implies an "action slot" concept in tension with DEC-132(3)'s "no new action economy" clause. |
| C. Structural non-overlap | Reaction-Tags may never be authored with a trigger condition identical to "an Effect is being applied to me"; that trigger space stays reserved for AD only. | Avoids the conflict by restricting future content rather than ruling the conflict itself; cheapest to rule, constrains future reaction design. |

### 3.3 Item 3 — Per-scene/frequency limits

| Option | Description | Trade-off |
|---|---|---|
| A. Uncapped | No frequency limit; self-limited only by PE/MP cost and Overflow risk. | Mirrors DEC-047 (AD uncapped) and DEC-075's original rationale (no fatigue system existed at the time). |
| B. Explicit tracked cap | A new per-character counter (e.g., 1 reaction per round/scene). | No precedent elsewhere in the ruled corpus; DEC-047 explicitly rejected this pattern for AD; introduces new bookkeeping. |

## 4. Part B — Comparative TTRPG Research

### 4.1 Methodology

Web research was conducted across four published systems with distinct out-of-turn-action
architectures, chosen for structural diversity: a hard-slot economy (D&D 5e), a
confirmed-identical hard-slot economy with an explicit multi-actor clarification
(Pathfinder 2e), an uncapped-but-penalized economy (GURPS), and a resource-gated interrupt
economy (Shadowrun 5e). A fifth system (World of Darkness / Chronicles of Darkness
dice-pool splitting) was reviewed as a partial comparator per the requester's prior
familiarity with it, though it was found to be structurally a pre-declared resource-split
system rather than a triggered interrupt system, limiting its direct applicability.

This research is **empirical/comparative evidence**, not a designer ruling or an
architectural constraint per se (evidence-class distinctions per `governance/status-model.md`
§ Evidence classes). It informs the options below; it does not resolve them.

### 4.2 Comparative Findings Table

| System | Reaction/interrupt limit | Multiple triggers from one event? | Interaction with primary defense |
|---|---|---|---|
| D&D 5e | Hard cap: 1 reaction per round per creature; refreshes at the start of the creature's own turn. | Not applicable within one creature (single pool). | Single shared pool — Attack of Opportunity, Shield, Counterspell, etc. all draw from the same one reaction; forces a real trade-off between offense-flavored and defense-flavored uses. |
| Pathfinder 2e | Same hard cap: 1 reaction per round, refreshes on the creature's own turn. | **Explicitly confirmed**: the one-reaction-per-trigger limit is per creature; multiple different creatures may each use a reaction in response to the same single trigger event. | Same shared-pool pattern as D&D 5e. |
| GURPS | Uncapped in count. Repeated use of the *same* defense type within one turn accrues a cumulative penalty (typically −4 per additional use, halved for Weapon Master/fencing weapons), reset at the start of the defender's own turn. A "Double Defense" option explicitly allows two *different* defense types against one incoming attack. | Not turn-limited; a defender facing multiple attackers defends against each independently. | Different defense types are explicitly stackable against a single attack (Double Defense); the throttle is a cumulative penalty, not exclusivity. |
| Shadowrun 5e | Uncapped in count. Every Interrupt Action spends Initiative Score, the same resource that determines a character's remaining actions for the Combat Turn; going below 0 has consequences. | Not capped by rule; self-limits via shared resource depletion across all actors independently. | Interrupt Actions are gated by the same resource economy as ordinary actions — no separate "reaction currency" exists. |
| World of Darkness / Chronicles of Darkness | Dice pool is split across pre-declared actions (including defense) before the round resolves; each declared action after the first accrues a cumulative dice/difficulty penalty. | N/A — defense capacity is budgeted in advance, not triggered reactively after the fact. | Structurally a resource-split economy, not a triggered interrupt system; limited direct applicability to Tiwas's post-hoc, per-Effect Active Defense model (DEC-048). |

### 4.3 Analysis Against Locked Tiwas Architecture

Two structurally distinct design families emerged from the research:

1. **Hard-count economy** (D&D 5e, Pathfinder 2e): a fixed number of reaction "slots" per
   round, refilled on a timer. Requires a tracked action-point-style resource. **This
   family is foreclosed by DEC-082**, which locks "no discrete action budget or action
   points" for the Time/Action economy.
2. **Resource-self-limiting economy** (GURPS, Shadowrun 5e): no hard count; cost itself
   (cumulative penalty, or a shared spendable resource) throttles repeated use. This
   family is **already the default shape of Tiwas Reactions** per DEC-132(2)(c), which
   makes every Reaction a full Core Test subject to Cost = Roll, Overflow, and Failure XP
   (DEC-006/007/009).

The World of Darkness dice-pool-split model does not map cleanly onto Tiwas's
architecture: Tiwas's Active Defense is post-hoc mitigation (DEC-048), not a pre-round
budget allocation, so the split-pool mechanic's core assumption (defense capacity is
committed in advance) does not hold here.

### 4.4 Additional Item Surfaced In-Session (Not One of the Three Original Carried-Open Items)

Because Reactions fire on other combatants' turns, a single trigger event (e.g., an
attacker moving through a chokepoint occupied by multiple party members) could provoke
Reactions from every eligible party member simultaneously. DEC-132 does not address this.
Pathfinder 2e's rule text directly confirms this is normal, expected behavior in a
comparable system ("more than one creature can use a reaction... in response to a given
trigger") rather than an edge case requiring special handling. This is flagged for Tiwa's
awareness; it is not resolved by this report and is not one of the three items DEC-132
carried open. Tiwa may wish to fold it into the Item 1 ruling, treat it as a fourth
carried-open item, or explicitly rule it "confirmed non-issue" per the Pathfinder 2e
precedent.

## 5. Findings Applied to Each Carried-Open Item

### 5.1 Item 1 — Trigger vocabulary

**Research finding:** every system surveyed (D&D 5e, Pathfinder 2e, GURPS, Shadowrun 5e)
enumerates specific, named triggers per granted ability — none operates on a general
"react to anything" grant. This corroborates Options A and C from Part A (§3.1) over
Option B; no comparator system supports pure indefinite deferral as viable for actual
play. All comparators ship at least a minimal concrete trigger set before the table needs
one.

### 5.2 Item 2 — Replace vs. stack with Active Defense

**Research finding:** GURPS's "Double Defense" rule is direct precedent for applying two
*different* defense mechanisms to a single incoming attack without exclusivity — directly
supporting **Option A (always independent)** from Part A (§3.2). D&D 5e/Pathfinder 2e's
single-shared-reaction-pool pattern is the counter-example, but that pattern is an
artifact of those systems' scarce generic reaction currency — a currency Tiwas does not
have and, per DEC-082, is not permitted to create. Option B (exclusive per trigger-moment)
would require introducing an action-slot concept that has no precedent among the
resource-gated comparators and sits in tension with DEC-132(3)'s "no new action economy"
clause.

### 5.3 Item 3 — Frequency limits

**Research finding:** this is the strongest result of the session. GURPS's cumulative
same-type-defense penalty (reset each turn) is functionally what **DEC-135**, ruled
earlier in this session, already implemented independently for Active Defense — repeated
AD within a continuous defensive sequence escalates the `Fatigued` Condition Tier
(DEC-079) rather than applying a raw stat penalty. DEC-135(F6) already contemplates
extending this to "defensive reactions whose purpose is to mitigate the incoming Effect."

The comparative research suggests this extension could plausibly be broadened from
"defensive reactions" specifically to Reactions generally (per DEC-132), giving a
GURPS-equivalent self-limiting throttle using **already-existing, already-ruled
machinery** (DEC-135, DEC-079, DEC-115–117) rather than a new counter or new pool. This
would satisfy Invariant 17 (no new pool — reuses the existing Condition architecture) and
DEC-082 (no action-point budget — the throttle is a Skill-side penalty via Condition
Tier, consistent with DEC-082's locked expression method) without requiring any new
mechanism.

This finding is offered as an option for Tiwa's consideration, not a ruling — extending
DEC-135's scope is itself a decision only Tiwa can make.

## 6. Summary of Options for Tiwa's Ruling

| Item | Options identified | Research-informed lean (advisory only, not a recommendation to be treated as settled) |
|---|---|---|
| 1. Trigger vocabulary | A (rule starter list now) / B (defer entirely) / C (rule categories, defer wording) | A or C both have full precedent across every comparator; B is the only option with no comparator support for viability in actual play. |
| 2. Replace vs. stack with AD | A (always independent) / B (exclusive per trigger-moment) / C (structural non-overlap, restrict content) | A has direct GURPS precedent (Double Defense) and requires no new machinery; B would introduce an action-slot concept in tension with DEC-082/DEC-132(3). |
| 3. Frequency limits | A (uncapped) / B (explicit tracked cap) / A-extended (uncapped, throttled via DEC-135 Fatigued-Condition extension) | A-extended reuses already-ruled machinery (DEC-135/DEC-079/DEC-115-117) and has the closest real-system analog (GURPS cumulative defense penalty); B has no precedent in the ruled corpus and DEC-047 explicitly rejected the analogous cap for Active Defense. |

**Additional flagged item (not one of the three original carried-open items):** whether one
trigger event may provoke reactions from multiple party members (§4.4). Pathfinder 2e
precedent suggests this is unproblematic by default; no ruling is proposed here.

## 7. Required OpenCode Actions

**None at this time.** This document is an advisory research package. Per standing
governance, OpenCode should take no recording action until:

1. Tiwa selects among the options in §6 (or directs alternative options not listed here);
2. Claude (or another advisory LLM) drafts formal rule text reflecting Tiwa's selections;
3. Tiwa reviews and explicitly approves that formal text;
4. OpenCode verifies the draft against the live register and records the resulting DEC(s).

If and when Tiwa rules on these items, the resulting entries should be recorded as
amendments/closures against DEC-132's carried-open list, following the same pattern used
for prior G-series closures (DEC-122–127, DEC-131 for G2; this document's own predecessor
items for G4).

## 8. Open Questions for Tiwa

1. Which option (A/B/C) do you select for Item 1 (trigger vocabulary)? If A or C, do you
   want to author the starter trigger list now, or defer authorship to a follow-up
   session?
2. Do you accept Option A (always independent) for Item 2, informed by the GURPS Double
   Defense precedent? Or do you see a reason specific to Tiwas's design goals to prefer
   exclusivity (Option B) or content-restriction (Option C) despite the precedent?
3. For Item 3: do you want to extend DEC-135's Fatigued-Condition escalation mechanism to
   cover Reactions generally (not just Active Defense), or keep Item 3 as a separate,
   uncapped-with-no-throttle ruling (Option A, unmodified)?
4. Do you want the multi-party-simultaneous-reaction question (§4.4) folded into this
   ruling package, left as a distinct future carried-open item, or explicitly closed as
   "no issue" per the Pathfinder 2e precedent?

## 9. Sources

Web research conducted 2026-09-09, current as of that date. All sources are third-party
published-game documentation/community reference material, cited for comparative design
analysis only — no game text is reproduced verbatim in this report.

- Opportunity Attacks in D&D 5e — Arcane Eye (arcaneeye.com)
- D&D 5e Reactions: What is a Reaction & How Do They Work? — FandomSpot
- Reactions In D&D 5e — Dungeon Mister
- Multiple Attacks of Opportunity — GameQuery.blog
- DnD 5e: How Reactions Work — CBR
- How Reactions Work in D&D 5e — Roll for Two
- Reactions in Encounters — Archives of Nethys (Pathfinder 2e, 2e.aonprd.com)
- Reactions — Archives of Nethys (Pathfinder 2e)
- Actions — Pathfinder 2e SRD (pathfinder2.dragonlash.com)
- GURPS Combat Chart — Saga of Westmarch Wiki (Fandom)
- Dodge — GURPS Wiki (Fandom)
- GURPS Combat - Newbie Question — RPGnet Forums
- All-Out Defense — GURPS Wiki (Fandom)
- Combat Maneuvers — GURPSworld Wiki
- Dungeon Fantastic: GURPS Combat Skill/Defense Caps Part II — Defense (blog)
- Let's GURPS: Fundamental — How to Not Die: Active Defenses and Quick Contests (blog)
- Shadowrun 5E: Quick Reference (gogorikska.github.io)
- Shadowrun Fifth Edition — Combat Rules (dungeonsanddecimals.com)
- SR5:Combat Actions — Shadowrun Wiki
- Action Economy & the Combat Round — Shadowrun (caithegm.com)
- How to Split Dice? — Onyx Path Forums (World of Darkness)
- Multiple Actions - A simple houserule — Onyx Path Forums
- Revising Multiple Actions — Onyx Path Forums
- So how do reactions work? — Onyx Path Forums (Vampire: The Masquerade)

---

**End of report.** This document is advisory only and creates no canonical or
non-canonical designer ruling by its own existence. It awaits Tiwa's review per §8.
