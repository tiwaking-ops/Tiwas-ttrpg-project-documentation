---
document:
  title: "Adversarial Verifier Report — Seven Consuming Mechanics Fusion Synthesis (DEC-133.A R3)"
  version: "1.0"
  status: "Advisory working document (not canonical, not a ruling)"
provenance:
  author_llm: {name: "upstage", version: "solar-pro4:free"}
  assessor_llm:
    - {name: "not established", version: "not established"}
  last_modified_by_llm: {name: "opencode", version: "muse-spark-1.3-contributor-free"}
  created_date: "2026-09-19"
  last_modified_date: "2026-09-19"
  storage_note: "Moved from repo root to investigations/ on 2026-09-19 by opencode / muse-spark-1.3-contributor-free per the analyze-assess-record-store workflow. Authorship attributed to upstage / solar-pro4:free per the sibling summary investigations/tiwas-g5-seven-consuming-mechanics-fusion-synthesis-adversarial-verification-chat-results-2026-09-19.md §8 (written in the same session); no independent assessment of this report itself has been performed. Frontmatter added at storage time; body unaltered. Advisory-only, non-canonical, no DEC inferred; storage & assessment confer no authority."
---

# Adversarial Verifier Report — tiwas-g5-seven-consuming-mechanics-fusion-synthesis-2026-09-19.md

**Verifier role:** Independent adversarial verifier (NOT in drafter pool).  
**Scope:** Red-team the draft against (a) Core Invariants + locked invariant spec-card content, and (b) live `_consolidation/decision-register.md`.  
**Instruction followed:** Report only invariant violations, silent assumptions, contradictions with existing DECs, unresolved designer forks, and claims missing an evidence class. No rewrites.

---

## 0. Foundational note — spec card

- The draft's §0.1 "Locked constraints any candidate must survive" is a **self-constructed summary**, not a from-repo spec card. No stored spec-card file exists in the repository for this section (verified by search). The orchestration plan (`roadmap/tiwas-gdd-multi-llm-orchestration-plan-v0.1-2026-09-18.md`) describes spec cards as the *contract* a drafter must satisfy, with the Verifier "rejecting violations mechanically, not by taste."
- **Implication for this pass:** I do not treat §0.1 as a governed spec card. I independently re-derive the constraint set from Canonical §16 (DEC-016) + the live decision register, and I check the draft's own §0.1 table against that derivation. Where §0.1 mis-states something, that is itself a finding (evidence-class / citation-accuracy issue), not an invariant violation by the mechanics.

---

## 1. Invariant 6 (Cost = natural roll) — Canonical §16, DEC-016

**Outcome: no clear violation. Two soft spots.**

### 1.A — ZoC Z-A "2 hexes per 1 hex traversed" justification muddles Invariant 6 vs Invariant 17

- Draft §0.1 row for Invariant 6 says: "Distance multipliers are position accounting, not a second Cost channel that violates the invariant, but they interact with the open consumption fork."
- Invariant 6 is about **the natural d100 roll being unmodified as Cost**. No candidate proposes a roll modifier, so Invariant 6 is preserved in form across all options.
- **Problem:** the justification language talks about a "second Cost channel" for a *distance multiplier*. "Cost" in the Canonical sense (DEC-006) = natural roll paid from a resource pool. Distance accounting is not "Cost" in that sense. The draft's wording therefore conflates Invariant 6 (roll integrity) with Invariant 17 (no new pool) in a way that is more confusing than wrong.
- **Finding (precision, not violation):** the sentence should state plainly that distance multipliers touch movement-distance accounting only and do not touch the natural-roll Cost. As written, a reader could mis-read "not a second Cost channel" as implying distance allowance is part of the Cost system.

### 1.B — Repeated attribution of "no graded outcomes" to DEC-030 is a misattribution, not an invariant violation

- Draft §0.1 says: "DEC-024 / DEC-030 — One Effect per win; no graded outcomes."
- Draft §5 (Forced Movement) says: "Binary outcome (DEC-030): the win produces the full declared magnitude or it does not; Quality does not buy extra hexes."
- Draft §7 (Seize/Deny G-C) says: "Binary outcomes only (DEC-030)."
- **Live register:**
  - DEC-024 (line 217): "Flat one-Effect-per-win. No Quality-based scaling, no purchasing of additional Effects off a single win."
  - DEC-030 (line 224): "Partial Tag/Location match → fail-and-fall-back to Base-tier Inflict Injury (HP-only form)."
- DEC-030 does **not** rule that Effect magnitude is binary / not Quality-scaled. That property belongs to DEC-024 + DEC-107 + DEC-023.A content policy ("no Effect scaling by Quality; no additional Effect granted").
- **Finding (contradiction with live register):** the draft attributes "no graded outcomes" jointly to DEC-024/DEC-030 and cites DEC-030 for "Quality does not buy extra hexes." The correct anchors for that claim are DEC-024, DEC-107, and DEC-023.A. This is a citation-accuracy error repeated in three places.

---

## 2. Invariant 17 (no competing resource/progression economy) — Canonical §16, DEC-016

**Outcome: no clear violation. One silent assumption, one structural soft spot.**

### 2.A — ZoC Z-A "multiplier is accounting, not a pool" is correct in intent but rests on an un-locking assumption

- Draft §0.1 Invariant-17 row: "No stored movement tokens, per-scene counters, or second progression channel. Only natural-roll Cost + ephemeral per-turn Movement Distance allowance." Then ZoC Z-A is marked satisfied because "multiplier is accounting, not a pool."
- **Silent assumption:** the draft treats Movement Distance allowance as definitively ephemeral and per-turn, with no per-scene tracking beyond "what remains this turn." The closest Canonical/registered anchors are DEC-133(3) ("Movement Distance per combat turn = effective Movement Speed; 1 MS = 1 hex per combat turn") and DEC-095 (movement is free/bundled side-activity). Those establish the *size* of the allowance and that movement does not cost a substantive action, but the register does **not** contain an explicit locked statement that "Movement Distance allowance is a purely ephemeral per-turn allowance and may not become a tracked per-scene resource."
- **Finding (silent assumption):** Invariant-17 safety for Z-A is intended design, not a locked derivation from an explicit DEC. The repo has not locked that specific characteristic. This is a property the designer very likely intends, but per AGENTS.md ("determine what the repository explicitly establishes before deciding how material may be used"), the draft should not present it as if it is already locked. Flag as silent assumption, not as a violation.

### 2.B — Pin P-B and Seize G-A/G-B propose new StateRecord types without anchoring them to the unified schema DECs

- Pin P-B proposes a StateRecord `Type: Held-Position / Tier Y / Location = current hex`.
- Seize G-A/G-B/G-C propose ground-control records as StateRecords with mandatory Location.
- The unified StateRecord schema is **DEC-115** (Effect/Condition merged; `Type / Tier Y / Magnitude Z / optional Location X`), and **DEC-117** extends it to Tags and adds the counter/removal machinery.
- The draft's §7(b) ZoC/Seize evidence classes reference "DEC-115 style" (informal) but P-B's StateRecord proposal is not anchored to any DEC at all — it says only "StateRecord(...)" with no schema citation and no engagement with whether a new record Type needs a governing Effect to create it, a removal route, or counter-rule interaction.
- **Finding (missing evidence-class anchor + missing schema citation):** P-B and the Seize record proposals are recommendations (correctly labeled "recommendation" in §6(b)/§7(b) for the most part), but a recommendation that invents a new StateRecord Type should at minimum cite DEC-115/DEC-117 as the governing schema and state which fields it uses. The draft does not. That is an evidence-class gap for a record-schema claim.

---

## 3. Live-decision-register contradictions and citation-accuracy issues

### 3.A — DEC-024/DEC-030 "one Effect per win; no graded outcomes" (repeat of 1.B, listed here as a register contradiction)

See §1.B. The register places "one Effect per win, no Quality scaling" on DEC-024; DEC-030 is about partial-match fall-back. The draft's joint citation is a contradiction with the register's own labeling.

### 3.B — DEC-082.A R2 presented as directly requiring Pin/Hold to reuse the existing Condition stack

- Draft §0.1: "DEC-082.A R2 — Movement-denial × Movement Speed question is closed. Pin/Hold must reuse existing Condition stack (DEC-122/123/124/126/131), not reopen it."
- **Live register DEC-082.A R2 (line 113):** closes the movement-denial × Movement Speed question using DEC-122/123/131; it does **not** mention Pin/Hold by name.
- The step from "movement-denial × Movement Speed is closed" to "therefore Pin/Hold must reuse existing Condition stack" is a **reasonable inference**, but the draft presents it as if DEC-082.A R2 directly says "Pin/Hold must reuse existing Condition stack." It does not say that.
- **Finding (silent inference presented as direct citation):** evidence class should be "designer ruling (DEC-082.A R2) + inference to Pin/Hold routing," not a bare DEC-082.A R2 citation.

### 3.C — Pin P-A's description of Grappled denial is insufficiently accurate for the live Grappled state

- Draft §6 P-A: "That Condition already zeros or penalises Effective Movement Speed per the locked rules."
- P-A lists "Restrained or Grappled per DEC-122/124/126/131 stack" as options.
- **Live register:**
  - DEC-122 (line 157): uniform self-referential-Y zeroing for Stunned/Incapacitated/Restrained/Grappled/Prone — but this is the *overlay* model, and DEC-122 itself is provisional.
  - DEC-124 (line 159): Grappled movement restriction = contested Break-Hold model; moving away from grappler requires breaking the Grapple; fail-vs-relocate outcome was **deferred**.
  - DEC-131 (line 166): resolved the deferred item — Option A "Pure Break" adopted; fail = Grapple persists/mover locked/no relocation; success = stepwise Heal-Effect-System Grapple removal; "relocate both" branch **dropped**.
- **Finding (contradiction with live register on the Grappled branch):** "zeros or penalises Effective Movement Speed per the locked rules" matches Restrained (uniform zero) better than Grappled. For Grappled, the denial mechanism is a contested Break-Hold check with stepwise removal and no relocation-on-fail — not simply an Effective-MS zero overlay. If Pin/Hold can route to Grappled, P-A's generic description is inaccurate for that branch. The draft should either describe Grappled's actual denial mechanism, or qualify that the Grappled branch carries additional contested-break semantics per DEC-124/131.

---

## 4. Silent assumptions

### SA-1 — Disengage as a movement-trigger eligible to provoke a reaction

- Draft §1 D-B: mover completes declared move with no gate contest; each engaged opponent with a matching `reaction:` Tag may resolve one Reaction.
- This presupposes that **leaving Engagement is a movement-trigger episode** under the DEC-132.A R1 trigger taxonomy.
- The movement-trigger **category** exists (DEC-132.A R1); whether a specific concrete case like "leaving Engagement" counts as a movement-trigger is content-authoring / definitional (DEC-077.A). The draft cites DEC-132.A R1 + DEC-077.A for "reaction category; Tags content-authored," but does not flag that the *application* of the category to Disengage is an assumption.
- **Finding (silent assumption):** Disengage being a movement-trigger is not a locked DEC; it is a reasonable application of the category, but should be flagged as fork/assumption, not stated as given.

### SA-2 — Chase can run on bands alone without a separate track

- Draft §3 K-A describes capture/escape purely in band terms. §3(c) question #2 asks who spends the Chase interval's action economy.
- The draft's note that DEC-030 forbids graded chase unless a separate chase track is content-authored is the right protection. But K-A rules text says "once per turn of the pursuing party" without resolving whether the Chase interval **is** the pursuer's substantive action for the turn.
- **Finding (silent assumption):** K-A presupposes an action-economy answer (Chase interval = substantive action? free side-activity? both?) that is not resolved in the rules text and only raised later in §3(c). The rules text itself leans on an unresolved action-economy decision.

### SA-3 — "Moving through controlled space is a movement-trigger" (Z-B)

- Draft §2 Z-B: "Movement through controlled space is a movement-trigger to which holders of a matching `reaction:` Tag may react."
- Same class as SA-1: applies the movement-trigger category to a specific case not expressly locked. Reasonable; not established. Flag.

### SA-4 — Movement Distance allowance is definitively ephemeral/per-turn (no pool)

- Cross-referenced in §2.A. The draft's Invariant-17 compliance argument for Z-A and for the whole suite depends on this. It is intended, but not explicitly locked by any DEC the draft cites.
- **Finding (silent assumption):** the draft should not present "Movement Distance allowance is a per-turn ephemeral allowance that cannot become a tracked resource" as an already-locked property. It is a property the candidates rely on.

### SA-5 — Provenance frontmatter author_llm "grok-fusion" does not match the §11 source-run list

- Frontmatter: `author_llm: {name: "grok-fusion", version: "multi-llm-synthesis-2026-09-19"}`.
- §11 "Provenance & fusion notes" attributes: primary structural depth/constraint analysis = big-pickle; primary multi-option rules text + evidence-class discipline = muse-spark; compact alternative framings = gemini-3.1-flash-lite; dependency map + advisory direction = kilo-auto-free; context hand-off = openrouter-free.
- **Finding (provenance inconsistency):** the named author model "grok-fusion" does **not appear** in the §11 source-run list, while the listed source runs are not reflected in the frontmatter author field. The actual authoring/fusion model is ambiguous. Per the orchestration plan + AGENTS.md provenance discipline, the author_llm field should identify the model that produced *this fused document*, and the source runs should be reflected consistently. This is a provenance-record defect, not a mechanics issue.

### SA-6 — M-0 "or simply succeeds at the declared movement objective if no Effect is required" presupposes a fork outcome

- Draft §4(a) M-0 rules text: "Winner selects one Position-tier Effect they are entitled to (or simply succeeds at the declared movement objective if no Effect is required)."
- Fork T (Position-tier gate) is listed as open; whether "objective success alone" is sufficient without Effect selection is an open sub-question (§9 #2).
- **Finding (soft silent narrowing):** the parenthetical "if no Effect is required" is presented inside the candidate rules text without a fork marker or EC tag, even though the question is explicitly open. Compare with §6 P-0's "Never-total discipline (DEC-123)" annotation discipline. The M-0 text should mark the "objective-success-without-Effect" path as fork-dependent, not embed it as if decided.

---

## 5. Unresolved designer forks — preservation check and soft narrowing risks

### 5.A — Forks correctly preserved

- Fork C (contested-movement consumption): preserved in §0.3, §8, and §9 #7. Good.
- Fork G (generic contest skill/payload): preserved in §0.3 and §9 #8. Good.
- Fork T (extra Skill-Tier gate on Position-tier Effects): preserved in §0.3 and §9 #9. Good.
- Per-mechanic shape forks (Disengage D-A/D-B/hybrid; ZoC Z-A/Z-B/Z-C; Chase K-A/K-B; Forced Movement F-A/F-B/F-C; Pin P-A/P-B; Seize G-A/G-B/G-C): all preserved in their sections and consolidated in §9. Good.

### 5.B — Soft narrowing risks where candidate rules text presupposes one fork outcome

- **UF-1 (Fork T):** M-0 "Winner selects one Position-tier Effect they are entitled to" uses "entitled to" as if the gate is already defined. Should qualify as fork-dependent.
- **UF-2 (Fork G):** M-0 "Skills: content-authored movement/agility/strength lineages (Fork G)" leans toward the content-authoring side of an open fork inside rules text, rather than neutrally stating "Skill lineages per Fork G (open)."
- **UF-3 (ZoC ↔ Seize/Deny relationship):** §9 #10 preserves the open relationship. But Seize G-B's parenthetical "or facing ZoC machinery if a movement-trigger Tag applies" presupposes ZoC and Seize/Deny can coexist as distinct layers — one open option, not the decided answer. Should be flagged fork-dependent.
- **UF-4 (Chase action economy):** see SA-2.
- **UF-5 (Fork-C-adjacent distance-debit embedded inline without Fork-C annotation):** Z-A "distance to edge still debited" (G-A) and similar inline distance-debit consequences appear in candidate rules text without the Fork-C label the draft applies in §8. The clearest case is G-A "distance to edge still debited." These should carry a Fork-C annotation or be marked fork-dependent, consistent with the draft's own §8 house style.

---

## 6. Claims missing an evidence class, or with a mismatched class

### 6.A — §0.1 global tag lumps invariant-interpretation reasoning under "mechanical fact"

- Line 45: `[EC: mechanical fact for Invariants; designer ruling for listed DECs]`.
- The *existence* of the invariants is mechanical fact (DEC-016 is Canonical/locked). But the row's *justification* ("Distance multipliers are position accounting, not a second Cost channel that violates the invariant") is the author's analysis/recommendation, not a mechanical fact. The tag should separate "invariant exists — mechanical fact" from "candidate satisfies it — recommendation/analysis."

### 6.B — §4(a) M-0 "Cost: full natural-roll Cost for each participant (Invariant 6)" not individually EC-tagged

- §4(a) M-0 rules text states Cost = full natural-roll Cost for each participant and references Invariant 6, but does not carry its own EC tag on that line.
- §4(b) evidence-class block tags S-1-as-universal-primitive (designer ruling DEC-013), one-Effect-per-win (designer ruling DEC-024), Skill lineage (recommendation). It does not restate the Cost claim with a class.
- **Finding (missing evidence-class label for a specific claim):** the M-0 Cost claim should either carry its own EC tag or be explicitly covered by a block tag. The draft's house style elsewhere tags substantive claims individually; this one is left to block inference.

### 6.C — §5(b) Forced Movement "No graded Quality magnitude — designer ruling (DEC-030)" cites the wrong DEC

- See §1.B / §3.A. Correct anchors: DEC-024, DEC-107, DEC-023.A. Evidence class "designer ruling" is correct for the claim; the cited DEC is wrong.

### 6.D — §6(a) Pin P-A "Duration / removal follows the Condition's normal rules (opposed contest to break, end of Effect duration, etc.)" lacks its own EC tag and DEC citation

- §6(b) tags "Must reuse existing denial stack — designer ruling (DEC-082.A R2, DEC-122/123/124/126/131)" and "Position-tier application vector — recommendation," but the specific claim about duration/removal mechanics is not individually tagged.
- The Break-Hold contest existence is established by DEC-124/131 for Grappled; the general duration/removal rules for Conditions are established by DEC-079 alpha vocabulary + DEC-135.A removal routes. The claim cites neither.
- **Finding (missing EC + missing DEC citation for a specific claim).**

### 6.E — §7(b) Seize/Deny "StateRecord with Location — recommendation (DEC-115 style)"

- "DEC-115 style" is informal. The governing schema DEC is DEC-115 (and DEC-117 for extension/counter/removal). Should cite DEC-115 directly rather than "DEC-115 style."
- **Finding (informal citation; not a class error per se, but weakens the evidence-class rigor the draft otherwise claims).**

### 6.F — §3(b) Chase "No roll-less Speed contest — mechanical fact / recommendation (Invariant 18 + progression economy)"

- Dual-labeled. Acceptable as capturing both the invariant grounding (mechanical fact) and the design interpretation (recommendation). Not a defect; noted for transparency.

---

## 7. What the draft does correctly (for balance)

- Carries the governance preamble.
- Labels evidence classes per claim in most places.
- Preserves Forks C/G/T as open and does not collapse them.
- Presents multiple candidate shapes per mechanic rather than silently picking one.
- Cites DEC IDs throughout.
- Keeps status Non-canonical advisory.
- Does not resolve the open designer forks or promote anything.
- §10 audit table is a useful summary structure, even where individual justifications are loose.

---

## 8. Consolidated red-team findings (compact)

**Invariant violations:** none clear-cut. Invariant 6 and Invariant 17 are preserved in form across all candidates.

**Silent assumptions:**
- Disengage is a movement-trigger eligible to provoke a reaction (SA-1).
- Moving through controlled space is a movement-trigger (Z-B) (SA-3).
- Movement Distance allowance is definitively ephemeral/per-turn with no per-scene tracking (SA-4 / §2.A).
- Chase can run on bands alone without a separate track, and the Chase interval's action-economy role is presupposed in K-A rules text (SA-2 / UF-4).
- M-0 "or simply succeeds if no Effect required" embeds an open sub-question as if decided (SA-6 / UF-1).
- Provenance frontmatter author_llm "grok-fusion" does not match the §11 source-run list; the actual fusion-authoring model is ambiguous (SA-5).

**Contradictions with existing DECs:**
- C-1: "One Effect per win; no graded outcomes" attributed to DEC-024/DEC-030; DEC-030 does not rule that. Repeated in §0.1, §5, §7.
- C-2: DEC-082.A R2 presented as directly requiring Pin/Hold to reuse existing Condition stack; it closes movement-denial × MS, not Pin/Hold routing specifically.
- C-3: Pin P-A describes Grappled denial as "zeros or penalises Effective Movement Speed," which is insufficiently accurate for the live Grappled state under DEC-124/131.

**Unresolved designer forks with soft-narrowing risk:**
- UF-1: M-0 "entitled to" presupposes Fork T.
- UF-2: M-0 "content-authored movement/agility/strength lineages" leans toward one Fork G outcome in rules text.
- UF-3: Seize G-B parenthetical presupposes ZoC + Seize/Deny can coexist as layers.
- UF-4: Chase K-A presupposes an action-economy answer not resolved in rules text.
- UF-5: G-A "distance to edge still debited" and similar inline distance-debit consequences are Fork-C-adjacent but not annotated as Fork-C-dependent.

**Claims missing or mis-matching an evidence class:**
- EC-1: §0.1 global tag lumps invariant-interpretation reasoning under "mechanical fact."
- EC-7: §4(a) M-0 Cost claim not individually EC-tagged.
- EC-8: §5(b) "No graded Quality magnitude — designer ruling (DEC-030)" cites the wrong DEC.
- EC-9: §6(a) Pin P-A duration/removal claim lacks its own EC tag and DEC citation.
- EC-10: §7(b) "DEC-115 style" is an informal citation for the unified-schema claim.

---

*End of adversarial verifier report. No draft text was rewritten.*
