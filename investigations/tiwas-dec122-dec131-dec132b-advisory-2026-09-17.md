---
document:
  title: "Advisory Session Report — DEC-122 Status Verification, DEC-131 Non-Escape Grappled Movement Options Brief, and DEC-132.B Comparative Research on Granular Tag-to-Reaction Matching"
  version: "1.0"
  status: "Advisory working document (not canonical, not a ruling)"
provenance:
  author_llm: {name: "Claude Sonnet 5", version: "claude-sonnet-5"}
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-17"
  last_modified_date: "2026-09-17"
---

## Purpose and Origin

Advisory material produced by Claude Sonnet 5 (`claude-sonnet-5`) in a chat session on 2026-09-17 and handed over for intake. Stored via the analyze-assess-record-store workflow (assessed and stored by OpenCode / big-pickle): advisory-only, non-canonical, no DEC inferred — storage and assessment confer no authority. Source file as received: `tiwas-dec122-dec131-dec132b-advisory-session-report-2026-09-17.md` (repo root). Body preserved verbatim below; only this frontmatter block and this opener were normalised at storage time (original author preserved as `author_llm`). Assessment note: §1 (DEC-122 Items 2–4 verification) and §3 (DEC-132.B survey) are consistent with the live register; §2's "carried open" framing of the DEC-131 non-escape-drag item predates Tiwa's same-day DEC-143 ruling closing that item and must be read as advisory record only — the operative rule is DEC-143, whose authority rests on Tiwa's ruling alone.

# Advisory Session Report — DEC-122, DEC-131, and DEC-132.B

**Author:** Claude Sonnet 5 — LLM name: `claude-sonnet-5`, LLM version: `claude-sonnet-5`
**Assessor:** OpenCode — LLM name: `opencode`, LLM version: `big-pickle` (in-session cross-verification of Part 1 only; see §1.3)
**Date:** 2026-09-17
**Document class:** Advisory session report. Records the complete results of a single chat session covering three items: a register-status verification, a non-canonical options brief, and a comparative-research summary. **No DEC number is assigned or proposed by this document.** Nothing herein is a ruling; all rulings remain Tiwa's.

---

## 0. Governance Statement

This document:

- Assigns **no DEC number** and proposes none.
- Contains one (1) **status verification** (§1), independently cross-checked by OpenCode against the live decision register with line-level citations.
- Contains one (1) **non-canonical options brief** (§2) addressing an explicitly open, carried-forward design fork (DEC-131's non-escape Grappled movement item). This is advisory content only, offered for Tiwa's eventual ruling — it is not adopted, not content-authored under DEC-077.A, and creates no operative rule.
- Contains one (1) **comparative research summary** (§3) surveying external TTRPG and video-game reaction/trigger systems, requested in connection with the DEC-132.B "granular Tag-to-Reaction matching system deferred" item. This is reference material only; DEC-132.B's deferral stands unless and until Tiwa rules otherwise.
- Follows the LLM Governance Rules (`governance/status-model.md`), in particular Rule 6 ("Never silently resolve an open designer fork") and Rule 10 ("State clearly when an answer depends on a proposal rather than a Canonical rule").
- Confers no authority by virtue of being written, stored, or cross-verified.

---

## 1. Status Verification — DEC-122 Items 2–4

### 1.1 Question Presented

Whether the following characterization is current:

> `| DEC-122 | Movement-denial Conditions (self-referential-Y) | **Items 2–4 still open** |`

### 1.2 Finding

**False as a statement of current status.** The "Pending (not ruled, this package)" language for Items 2–4 appears inside DEC-122's own register cell and describes the state of the G2 advisory package **at the moment DEC-122 itself was ruled** (2026-09-07) — it is a historical snapshot, not a live status field. All three items were resolved within the same design session via separate, explicitly-cited follow-up DECs.

| Item | Subject | Resolution | Closing DEC(s) |
|---|---|---|---|
| 2 | Action declaration under Stunned / Incapacitated / Restrained | **"Never total."** The three Conditions no longer categorically prohibit declaring an action. Effective Skill is forced to 0 by DEC-122's self-referential-Y (`Y` = the target stat's own current value; `Z = −Y`), guaranteeing failure, but the full 9-step Core Test Transaction still runs (Cost paid, Overflow risk, Failure XP, qualifying failed-Double Advanced Skill creation). Whether the attempt is **permitted at all** is GM Fiat (DEC-130). | **DEC-123** |
| 3 | Grappled directional movement gate | The DEC-059-pattern relational gate was rejected. Moving away from a Grapple requires a **contested Break Hold / Break Free Skill Check** (full Core Test). Fail → Grapple persists, mover locked, no relocation. Success → the Grapple StateRecord steps down one Tier via the Heal Effect System (`Tier Y → Y−1`; `Z = −Y` recalculated); `Y = 0` removes the record and the mover is free. The "relocate both" outcome was explicitly dropped. | **DEC-124** (contest model) → **DEC-131** (resolves the fail-vs-relocate deferred sentence) |
| 4 | Prone crawl-speed fraction | `crawl = max(1, floor(Movement Speed / 2))`. The `max(1, …)` floor-of-1 guarantee is the ruled component; the base fraction (½) is content-authoring under DEC-077.A and may be re-authored per creature without a new design decision. | **DEC-125** |

DEC-079.A (2026-09-10) additionally closed the adjacent DEC-079 "carried open" tracker covering the same territory: R1 ties Condition Tier to DEC-107; R2 confirms the C5 overlay model plus DEC-122/125/133 as complete; R3 confirms DEC-123/126 as complete, with the explicit caveat that **no cross-Condition −Y stacking rule is established** (recorded as genuinely open, not closed-by-omission).

### 1.3 Independent Cross-Verification (OpenCode)

OpenCode independently verified this finding against `_consolidation/decision-register.md` with line-level citations:

| Citation | Content |
|---|---|
| `decision-register.md:157` | DEC-122 itself: "**Pending (not ruled, this package):** Item 2 … Item 3 … Item 4 …" — confirmed as package-scope language, not current-status language |
| `decision-register.md:158` | DEC-123: "Tiwa, ruling G2 **Item 2**" — Option B "never total" adopted; Item 2 closed |
| `decision-register.md:159` | DEC-124: "Tiwa, ruling G2 **Item 3**" — Option B contested Break-Hold adopted; DEC-059 gate rejected; one sentence flagged "To be decided (deferred)"; same row annotated "**[RESOLVED 2026-09-07 via DEC-131 …]**" |
| `decision-register.md:160` | DEC-125: "ruling G2 **Item 4**" — "**Closes G2 Item 4.**" |
| `decision-register.md:166` | DEC-131: "RESOLVES DEC-124's deferred sentence" — Option A "Pure Break" adopted; "**Closes G2 Item 3 fully**." |

All five citations trace to the same source session, `investigations/tiwas-g2-movement-denial-condition-advisory-session-2026-09-07.md`, dated 2026-09-07.

**Authority caveat (OpenCode, per `governance/authority.md` and `governance/status-model.md`):** DEC-122, DEC-123, DEC-124, DEC-125, and DEC-131 are all recorded as **Non-canonical designer ruling**; DEC-122's own adoption is explicitly **provisional**. None has completed the 8-step Promotion Rule (REQ-021), so none is Canonical. The finding in §1.2 concerns register-status accuracy only and makes no claim about Canonical status.

### 1.4 Conclusion

The row should read Items 2–4 **Closed** (DEC-123 / DEC-124→DEC-131 / DEC-125 respectively), not "still open." Per LLM Governance Rule 6, no LLM should treat this cell's historical wording as license to silently reopen a closed non-canonical fork. Any downstream document (roadmap, playtest packet, router-cached summary) currently repeating the stale "Items 2–4 still open" framing should be corrected by pointer/citation to this section rather than by re-derivation.

### 1.5 Genuinely Open Adjacent Items (for contrast, not addressed by this correction)

| Item | Status |
|---|---|
| Non-escape Grappled movement (holder dragging the victim; movement not away-from-grappler) | Carried open by DEC-131 — addressed in §2 below |
| Cross-Condition stacking interaction (e.g., Stunned + Restrained simultaneously) | Explicitly unruled per DEC-079.A R3 ("remains unruled, not ruled-against") |
| G3 — duration/time-unit scale | Open per DEC-133/DEC-133.A |

---

## 2. Options Brief — Non-Escape Grappled Movement (Holder Dragging Victim)

**Status: Advisory options brief. No DEC. This is not content-authoring under DEC-077.A and is not adopted.** Addresses the item carried open by DEC-131: "non-escape Grappled movement interactions (movement not away-from-grappler; holder initiating movement / dragging the victim)."

### 2.1 Constraint Baseline (already-ruled elements this brief must not contradict)

| Element | Ruled by | Relevance |
|---|---|---|
| Grapple = Location or global StateRecord, `Tier-Y Grappled Value Z` (`Z = −Y`) | DEC-079 | The record any drag mechanic would act on |
| Escape (mover moving away from grappler) = contested Break Hold, fail→no relocation, success→stepwise Tier reduction | DEC-124 / DEC-131 | Explicitly does **not** cover this case (holder-initiated, not mover-escape) |
| No action-point pool; Time/Action expressed only via Skill-side/Movement penalty overlays | DEC-082 | Any drag mechanic must be a penalty overlay, not a new resource |
| Movement = effective Movement Speed per combat turn; abstract distance bands (Engagement/Short/Medium/Far) | DEC-133 | Presumed unit of measure for any drag distance |
| Self-referential-Y overlay pattern (`Y` = target's own stat) | DEC-122 | One of three currently-named Y-source patterns; reusable if desired |
| Invariant 17 (no new resource pools); Invariant 6 (natural roll never modified) | Canonical | Hard constraints on all options below |

### 2.2 Candidate Options

**Option A — Automatic drag, no roll.**
The holder moves and the grappled victim moves with them at the holder's effective Movement Speed. No check. A Movement Speed penalty overlay (reusing the existing `−Y` Encumbered/Slowed mechanism, DEC-078 / DEC-079 C5) reduces the holder's effective Speed while dragging.

- *Consistent with:* DEC-082 (no action-point pool); Priority 3 (minimum resolution steps); the project's repeated "Simplification. Can be expanded on later." pattern (DEC-136, DEC-138, DEC-141, DEC-142).
- *Cost:* the victim has zero agency in the interaction, asymmetric with the escape side's contested roll.

**Option B — Movement Speed penalty scaled to Grapple Tier (no roll, reuses existing schema).**
Identical to A, but the overlay magnitude is `−Y` where `Y` = the **Grapple record's own current Tier**, not a self-referential target-stat pull. This is a third Y-source pattern (alongside the already-named causing-Skill-Tier [DEC-107] and target-stat-value [DEC-122 Item 5] patterns).

- *Consistent with:* reuses the existing `Tier-Y … Z=−Y` StateRecord shape (DEC-115) with zero new fields; ties drag friction to an already-tracked number.
- *Cost:* one additional named Y-source pattern to document (documentation overhead only, no new mechanic).

**Option C — Contested check per drag attempt.**
The holder makes an opposed Skill Check against the victim's resistance each time they attempt to drag; success = victim moves with them, failure = the holder's movement fizzles that action.

- *Consistent with:* symmetry with the DEC-124/DEC-131 escape model.
- *Cost:* works against Priority 3 and against DEC-082's no-action-point-pool spirit — every drag becomes a full 9-step Core Test in an already roll-heavy combat loop, the pattern Tiwa has been actively trimming (DEC-136/DEC-138/DEC-141/DEC-142).

### 2.3 Recommendation

**Option B**, with Option A as a lower-documentation-overhead fallback. Rationale: zero new mechanical surface (reuses an existing record shape and overlay pattern); gives dragging a meaningful cost without a roll; and is consistent with the project's dominant recent design trajectory of preferring the simpler mechanical surface when both a simple and a symmetric/contested option are on the table. **Option C is not recommended** given that trajectory.

### 2.4 Disposition

This options brief should be stored as a separate, citable, non-canonical advisory document (mirroring the shape of `tiwas-g2-movement-denial-condition-advisory-session-2026-09-07.md` or the DEC-141/DEC-142 P4/P6 proposal) if OpenCode elects to persist it, explicitly flagged as addressing the DEC-131 carried-open item. No LLM should write "Item resolved" into the decision register on the strength of this brief; that determination is Tiwa's.

---

## 3. Comparative Research — Granular Tag-to-Reaction Matching Systems

**Requested in connection with:** `| DEC-132.B | G4 Reactions | **Granular Tag-to-Reaction matching system deferred** |`

**Status: Reference material only.** DEC-132.B's deferral is explicit and self-explanatory in its own text ("a matching Tag to Reaction system may be implemented later... Tiwas TTRPG is currently to[o] primitive to support or test these systems at this time" — Tiwa, verbatim, 2026-09-13). This section does not propose reopening that deferral; it supplies comparative evidence for whenever Tiwa chooses to revisit it.

### 3.1 Systems Surveyed

| System | Trigger-matching model | Granularity | Key mechanism |
|---|---|---|---|
| **D&D 5e — Opportunity Attack** | One universal trigger ("hostile creature leaves your reach"), extended by discrete named exceptions | Coarse base trigger; exceptions individually authored (Polearm Master: entering reach; Mage Slayer: spellcasting in reach; Sentinel: any move in reach) | No tag ontology — each exception is a bespoke rules-text carve-out on the base trigger, not a matched Tag pair |
| **Pathfinder 2e — Reactions** | Each reaction defines its own free-text trigger; overlapping/near-identical triggers resolved by **GM judgment** | Fully granular but unstructured — no tag vocabulary, no matching engine | Rules text explicitly states: "If two triggers are similar, but not identical, the GM determines whether you can use one action in response to each" — ambiguity is *designed* to route to GM Fiat, not resolved mechanically |
| **GURPS — Active Defenses / Double Defense** | No trigger-matching; defenses (Dodge/Parry/Block) are available up to a per-turn count; "Double Defense" allows two different defense types to stack against one incoming attack | N/A — count-gated, not trigger-gated | Already the cited precedent underlying DEC-132.A(R2)'s "Reactions and Active Defense never compete" ruling |
| **XCOM (Overwatch)** | One universal trigger (hostile unit enters LoS / movement range), extended by named abilities adding new trigger conditions (Covering Fire: fires on enemy attacks; Suppression: fires on target movement; Kill Zone: fires on cone-entry) | Coarse base + short enumerated list of ability-specific trigger variants | Each variant is its own discrete named ability, not a matched Tag pair — structurally identical in shape to the D&D 5e / XCOM exception-list pattern |

### 3.2 Extracted Pattern

None of the four surveyed systems implement a generalized, combinatorial Trigger-Tag × Reaction-Tag matching engine. Notably, the two most mechanically dense systems surveyed (GURPS, Pathfinder 2e) **actively avoid** building one:

- Pathfinder 2e explicitly routes ambiguous/overlapping trigger cases to GM judgment as a stated design choice, not an oversight.
- D&D 5e and XCOM both achieve granularity through a "one base trigger + a short enumerated list of named exceptions" pattern — granularity is purchased by **authoring more named reactions/abilities**, not by building a matching table.

### 3.3 Relevance to Tiwas's Current State

This pattern corroborates the shape already adopted in DEC-132.A(R1) / DEC-132.B: a **coarse three-category taxonomy** (movement-trigger / ally-targeted-trigger / HP-state-threshold-trigger) with **one Tag per category**, exact menus deferred to content-authoring (DEC-077.A). No system surveyed exceeds this granularity in mature, played form before falling back to GM adjudication for edge cases.

### 3.4 Forward-Looking Options (for a future options brief only — not proposed for adoption now)

| Option | Shape | Nearest precedent |
|---|---|---|
| A — Named exceptions per Tag, not a matching engine | Retain the 3 coarse Tags; allow content-authoring (DEC-077.A) to attach creature/class-specific exception clauses to a Tag's trigger definition | D&D 5e, XCOM |
| B — Explicit GM-adjudication clause for near-identical triggers | Formalize what DEC-132.B already implies: ambiguous trigger overlap resolves via GM Fiat (DEC-130) | Pathfinder 2e |
| C — Full granular Tag-matching engine | **Not recommended** by this survey; no comparator system uses this in mature, tested form | — |

### 3.5 Disposition

This research should not be read as recommending that DEC-132.B be reopened now. It is offered so that, when Tiwa judges the base systems sufficiently mature, an options brief can be assembled quickly against precedent rather than from a blank slate.

---

## 4. Summary Table

| # | Item | This document's contribution | Authority |
|---|---|---|---|
| 1 | DEC-122 Items 2–4 register-status wording | Verified stale; corrected to "Closed" with DEC citations | Finding only — confers no authority; register itself remains non-canonical |
| 2 | DEC-131 non-escape Grappled dragging | Options brief (A/B/C), Option B recommended | Advisory only — no DEC, no adoption |
| 3 | DEC-132.B granular Tag-to-Reaction matching | Four-system comparative survey; options catalogued for future use | Reference material only — deferral (DEC-132.B) unchanged |

---

## 5. Hard Boundaries (restated)

- No DEC inferred or assigned by this document.
- No promotion, demotion, or supersession language used or implied.
- No rule invented, edited, or silently reopened.
- §1's finding is a citation-verified factual correction to register-cell interpretation, not a new ruling.
- §2 and §3 are advisory-only; nothing in either section is adopted, and neither is content-authored under DEC-077.A.
- All open items remain open until Tiwa rules; all closed items remain closed unless Tiwa reopens them through formal governance.

**End of report.**
