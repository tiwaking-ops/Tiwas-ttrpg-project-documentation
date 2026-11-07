---
document:
  title: "Fusion Synthesis — Seven Consuming Mechanics Candidates (DEC-133.A R3)"
  version: "v0.1-fusion"
  status: "Non-canonical advisory"
provenance:
  author_llm: {name: "grok-fusion", version: "multi-llm-synthesis-2026-09-19"}
  source_runs:
    - multi-llm-test1-opencode-big-pickle (primary structure + depth)
    - multi-llm-test1-opencode-muse-spark-1-3-contributor-free (primary options + evidence class discipline)
    - multi-llm-test2-google-gemini-3-1-flash-lite (compact framing notes)
    - multi-llm-test2-kilo-auto-free (dependency map + advisory direction)
    - multi-llm-test2-openrouter-free (context summary only)
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "muse-spark-1.3-contributor-free"}
  created_date: "2026-09-19"
  last_modified_date: "2026-09-19"
  note: "This document is a fusion of the strongest parts of the five multi-run candidates. It does not resolve open designer forks. Nothing herein is Canonical."
  storage_note: "Moved from repo root to investigations/ on 2026-09-19 by opencode / muse-spark-1.3-contributor-free per the analyze-assess-record-store workflow. Body unaltered; frontmatter updated to record the opencode/big-pickle red-team verification as assessor. Red-teamed twice (upstage solar-pro4:free verifier-only report + opencode/big-pickle chat report, both stored alongside); independently assessed (Nemotron 3 Ultra, stored alongside). Advisory-only, non-canonical, no DEC inferred; storage & assessment confer no authority."
---

> You are producing non-canonical advisory material only. Per this project's `governance/status-model.md` and the LLM Governance Rules, your output goes into `investigations/` or `proposals/`, is never Canonical, and must not silently resolve an open designer fork. Cite existing DEC IDs from `decision-register.md` where relevant. State your evidence class (mechanical fact / empirical finding / designer ruling / recommendation) for each claim.

# Fusion Synthesis — Seven Consuming Mechanics (DEC-133.A R3)

**Status:** Non-canonical advisory. Candidate rules text for the seven consuming mechanics left open by **DEC-133.A R3**. Fused from five independent multi-LLM runs; no DEC is inferred or resolved hereby; nothing here is promoted, demoted, or superseded.

**Purpose.** Provide candidate implementations for: **Disengage, Zone of Control, Chase, generic movement contests, Forced Movement magnitude, Pin/Hold Position resolution, Seize/Deny Ground resolution**. Each candidate must (a) be expressible as rules text, (b) carry an evidence class per claim, (c) present open designer forks rather than silently collapsing them.

---

## 0. Scope, constraints, and shared substrate

### 0.1 Locked constraints any candidate must survive

| Constraint | Source | Implication for candidates |
|---|---|---|
| **Invariant 6** — Cost = natural roll | Canonical §16 | Every contested resolution is a full Core Test (DEC-006); natural d100 is never modified. Distance multipliers are position accounting, not a second Cost channel that violates the invariant, but they interact with the open consumption fork. |
| **Invariant 17** — no competing resource pools | Canonical §16 | No stored movement tokens, per-scene counters, or second progression channel. Only natural-roll Cost + ephemeral per-turn Movement Distance allowance. |
| **Invariant 18** — build on Core Test | Canonical §16 | No separate “movement engine.” Chase, ZoC contests, Disengage contests, etc. are S-1 (DEC-013). |
| **DEC-024 / DEC-030** | Designer ruling | One Effect per win; no graded outcomes. Forced Movement, Pin/Hold, Seize/Deny are mutually exclusive selections unless DEC-026 cash-out is engaged. |
| **DEC-123** — “never total” | Designer ruling | Never veto action declaration. Express denial as Effective Movement Speed = 0 / −Y or as a contested roll that must be won. |
| **DEC-082.A R2** | Designer ruling | Movement-denial × Movement Speed question is closed. Pin/Hold must reuse existing Condition stack (DEC-122/123/124/126/131), not reopen it. |
| **DEC-095** | Designer ruling | Movement is free/bundled side-activity; one substantive action per turn. |
| **DEC-133 Hybrid** | Designer ruling | Movement Distance = Effective Movement Speed (1 MS = 1 hex/turn). Band model remains; band↔hex boundaries are content-authoring (DEC-077.A). |

[EC: mechanical fact for Invariants; designer ruling for listed DECs]

### 0.2 Shared design substrate

- **Geometry:** All positional payloads stated in hexes with parenthetical band reading. Exact band names/widths = content. [EC: designer ruling — DEC-133 / 133.A R1]
- **Resolution:** Every meaningful contest is a full S-1 opposed contest (DEC-013) with normal Cost, Overflow, Failure XP, Doubles, Recovery. [EC: mechanical fact]
- **Effect selection:** Winner selects **one** Position-tier Effect their Skill-Tier permits (DEC-107: Effect Tier = causing Skill-Tier). Quality is success precondition / tie-break, not a magnitude dial. [EC: designer ruling]
- **Reactions:** Movement-triggers are a ruled category (DEC-132.A R1); exact Tags and eligibility are content-authoring (DEC-077.A).

### 0.3 Shared open forks (must NOT be resolved by this draft)

1. **Fork C — contested-movement consumption (DEC-133.A R2):** Does a failed movement contest consume the mover’s remaining Movement Distance allowance for the turn, only the distance already travelled, or nothing beyond the natural-roll Cost?
2. **Fork G — generic movement contest skill/payload:** Which Skill lineages and what payload selection rules apply to the shared primitive?
3. **Fork T — additional Skill-Tier gate on Position-tier Effects:** Does Position-tier require only the DEC-023.A unlock, or an extra Skill-Tier threshold?

These remain open. Candidates below present options without collapsing them.

---

## 1. Disengage (leaving Engagement)

### (a) Candidate rules text

> **D-0 Common shell.** A combatant that uses its per-turn movement (DEC-095 free side-activity; DEC-133 distance allowance) to leave the *Engagement* band relative to an engaged opponent declares **Disengage**. Distance moved debits the mover’s remaining Movement Distance allowance. Leaving Engagement is a *movement-trigger* (DEC-132.A R1); opponents with a matching `reaction:` Tag *may* be eligible to react — eligibility and Tag vocabulary remain content-authoring (DEC-077.A). All rolls are full Core Tests / S-1 contests at normal Cost. No roll modifier touches the natural d100 (Invariant 6).

> **Option D-A — Contested Disengage (S-1 gate).** Mover declares destination (band + hex path within allowance). Each engaged opponent that contests (GM Fiat or automation rule) resolves one S-1 opposed contest: mover rolls a movement/agility-lineage Skill; opponent rolls a holding/reactive Skill.  
> - **Mover wins:** departure succeeds; mover completes the declared move (consumption per Fork C).  
> - **Opponent wins:** mover’s exit is arrested at the Engagement edge; distance already travelled is still debited; mover retains unused allowance for non-exiting repositioning and may still take a non-movement action (DEC-095). Failed exit may be re-attempted (another full-Cost S-1).

> **Option D-B — Free exit + Reaction window.** Mover completes the declared move within allowance with **no gate contest**. Each engaged opponent with a matching `reaction:` Tag may resolve one Reaction (DEC-132, full S-1, full Cost). Reaction winner selects one Position-tier Effect they are entitled to (e.g. Forced Movement to re-engage, or Pin/Hold attempt) subject to one-Effect-per-win (DEC-024). If no opponent reacts, exit is unopposed.

> **Hybrid note (recommendation):** Contest only against opponents who hold a `reaction:` movement-trigger Tag; otherwise free exit. This preserves both pressure and table variance without forcing every Engagement to generate rolls.

### (b) Evidence class

- Movement free/bundled; one S-1 exchange per turn — **designer ruling (DEC-095)**
- Distance = effective MS hexes — **designer ruling (DEC-133)**
- Movement-trigger reaction category; Tags content-authored — **designer ruling (DEC-132.A R1, DEC-077.A)**
- S-1 matrix, full Cost — **mechanical fact (DEC-013, DEC-006/007)**
- Contested vs free shape (D-A / D-B / hybrid) — **recommendation** (fork preserved)

### (c) Designer questions left open

1. Gate, window, or hybrid (contest only vs `reaction:` Tag holders)?
2. Which Skill lineages may roll Disengage contests (content-authoring now, or framework-fixed)?
3. Does a failed D-A exit consume only movement allowance, or also the substantive action (DEC-095 interaction)?

*Sources fused: muse-spark D-0/D-A/D-B structure + big-pickle Option A permissive default + kilo advisory direction (reaction-gated).*

---

## 2. Zone of Control (ZoC)

### (a) Candidate rules text

> **Z-0 Common shell.** A Zone of Control is a **declarative, read-only area assertion**: while combatant C is in a stated posture (content-authored; e.g. wielding `handling:reach`, holding a lane, or maintaining a stance Tag), the Engagement-adjacent hexes/band around C are flagged as **controlled**. The flag itself rolls nothing, spends nothing, and creates no pool (Conditional-Trait-Binding grammar precedent). What the flag *enables* is the fork below. Posture declaration breadth is content-authoring (DEC-077.A).

> **Option Z-A — ZoC as Difficult-Ground overlay.** Entering, crossing, or exiting controlled hexes costs **2 hexes of Movement Distance allowance per 1 hex traversed** (multiplier on distance accounting, not a new currency). No contest is forced. GM Fiat may waive for allies/formation (DEC-130).

> **Option Z-B — ZoC as Reaction-enabler only.** Controlled status grants **no movement-cost change**. Movement through controlled space is a movement-trigger to which holders of a matching `reaction:` Tag may react (DEC-132; one Reaction per reactor per trigger event; each a full S-1 at full Cost). Without a reactor Tag + declared reaction, ZoC has no mechanical effect.

> **Option Z-C — Permissive default + gated pass-through denial (big-pickle preferred shape).** ZoC is declared freely. Movement into/through is normally permitted. The controller (or any ally with the relevant Tag) may contest a specific transit as a reaction (S-1). On controller win the mover is stopped at the controlled-edge (or pushed back 1 hex — payload choice). On mover win transit completes. This keeps ZoC “live” only when someone elects to spend a reaction.

### (b) Evidence class

- Declarative flag, no pool — **recommendation** (Invariant 17 hygiene)
- Distance multiplier vs reaction-enabler vs gated contest — **recommendation** (three live options; none locked)
- Reaction machinery — **designer ruling (DEC-132)**

### (c) Designer questions left open

1. Cost-overlay (Z-A), pure reaction (Z-B), or gated contest (Z-C)?
2. Does ZoC stack with Seize/Deny Ground, or are they mutually exclusive claims?
3. How many hexes / which bands does a single ZoC cover by default (content vs framework)?

*Sources fused: muse-spark Z-A/Z-B + big-pickle Z1 gated shape + gemini interrupt-action framing.*

---

## 3. Chase (pursuit over multiple turns)

### (a) Candidate rules text

> **K-0 Common shell.** A Chase is a sequence of movement contests across one or more turns while the pursued remains outside Engagement (or outside a declared capture band). There is **no** Speed-vs-Speed resolution without rolls; every interval is a full S-1 (Invariant 18 / Core Test identity).

> **Option K-A — Sequential S-1 movement contests, band-driven.** Each Chase interval (once per turn of the pursuing party, or on a shared clock): both parties roll an S-1 opposed contest using movement/agility-lineage Skills.  
> - **Pursuer wins:** reduces band separation by 1 (or by Margin-derived steps if designer elects graded chase — currently forbidden by DEC-030 unless a separate chase track is content-authored).  
> - **Pursued wins:** increases separation by 1 or holds.  
> - Capture occurs when pursuer reaches Engagement (or a declared capture band). Escape occurs when separation reaches a content-authored Far threshold or the pursued reaches a declared sanctuary.  
> Each contest is full Cost for both participants. Movement Distance allowance is still debited for actual hexes moved during the interval (Fork C applies).

> **Option K-B — Margin-accumulation track (extended-test flavour).** Same S-1 rolls, but Margin is accumulated toward a target number (content-authored or derived from initial band distance). First to the target captures or escapes. Still full Core Tests; no new resource pool.

> **Default recommendation:** K-A (binary band steps) for alpha simplicity; K-B only if the table wants longer multi-round chases with clearer “closing the gap” theatre.

### (b) Evidence class

- No roll-less Speed contest — **mechanical fact / recommendation** (Invariant 18 + progression economy)
- Sequential S-1 — **recommendation**
- Band-driven vs Margin track — **recommendation** (open)

### (c) Designer questions left open

1. Binary band steps (K-A) or Margin accumulation (K-B)?
2. Who spends the Chase interval’s action economy (pursuer only, both, or free side-activity)?
3. Interaction with terrain / ZoC during a Chase?

*Sources fused: big-pickle K1 sequential + muse-spark chase structure + kilo/gemini Margin notes.*

---

## 4. Generic movement contests (shared primitive)

### (a) Candidate rules text

> **M-0 Shared primitive.** Whenever two (or more) combatants compete for the same movement objective — same hex, same band threshold, same chokepoint, same Disengage/ZoC/Chase contest, etc. — resolve as a **single S-1 opposed contest** (DEC-013).  
> - Winner selects one Position-tier Effect they are entitled to (or simply succeeds at the declared movement objective if no Effect is required).  
> - Loser is blocked, displaced, or fails the objective per the specific mechanic that invoked M-0.  
> - Skills: content-authored movement/agility/strength lineages (Fork G).  
> - Cost: full natural-roll Cost for each participant (Invariant 6).  
> - Consumption of Movement Distance on failure: Fork C (open).

> This primitive is the single resolution engine under Disengage (D-A), ZoC (Z-C), Chase intervals, Seize/Deny entry contests, and any ad-hoc “who gets there first” situation. No second movement resolution system is introduced.

### (b) Evidence class

- S-1 as universal opposed primitive — **designer ruling (DEC-013)**
- One Effect per win — **designer ruling (DEC-024)**
- Skill lineage & payload details — **recommendation** (Fork G preserved)

### (c) Designer questions left open

1. Default Skill families for M-0 (framework list vs pure content)?
2. Does a pure “I get the hex” win still require selecting a Position-tier Effect, or is objective success sufficient?
3. Multi-party contests (3+ actors) — sequential pairwise or simultaneous?

*Sources fused: muse-spark M-0 + big-pickle M4 + gemini “Gain Position” framing.*

---

## 5. Forced Movement magnitude

### (a) Candidate rules text

> **F-0 Common shell.** Forced Movement is a Position-tier Effect (DEC-023.A). On selection after a winning contest, the target is displaced.

> **Option F-A — Tier-scaled hexes (preferred default).** Magnitude = **Effect Tier** (which equals causing Skill-Tier per DEC-107) in hexes. Example: Skill-Tier 2 → push/pull/slide 2 hexes. Direction is chosen by the victor (or by the effect’s authored vector). Occupied destination hexes may trigger further contests or stop the move at the last legal hex (content or GM Fiat).

> **Option F-B — Fixed small magnitude.** Always 1 hex (or 1 band step). Simpler for alpha; Tier instead gates *availability* of the Effect rather than distance.

> **Option F-C — MS-referenced.** Magnitude = target’s or actor’s Effective Movement Speed (or a fraction). Rejected as default because it couples Forced Movement to a derived stat in a way that can create swingy or opaque results; kept only as a designer alternative.

> **Binary outcome (DEC-030):** the win produces the full declared magnitude or it does not; Quality does not buy extra hexes.

### (b) Evidence class

- Position-tier Effect, one per win — **designer ruling (DEC-023.A, DEC-024)**
- Effect Tier = Skill-Tier — **designer ruling (DEC-107)**
- Magnitude formula (F-A / F-B / F-C) — **recommendation**
- No graded Quality magnitude — **designer ruling (DEC-030)**

### (c) Designer questions left open

1. Tier-scaled (F-A), fixed (F-B), or MS-referenced (F-C)?
2. What happens when the forced path is blocked (stop, divert, contest the blocker)?
3. Does Forced Movement through a ZoC or Seized ground trigger those mechanics?

*Sources fused: big-pickle F1 Tier-scaled + muse-spark magnitude options + gemini MS note (retained as alternative only).*

---

## 6. Pin / Hold Position resolution

### (a) Candidate rules text

> **P-0 Common shell.** Pin/Hold Position is a Position-tier Effect (DEC-023.A). It must **not** reopen the movement-denial × Movement Speed question (DEC-082.A R2 complete). Therefore it routes to the existing Condition machinery.

> **Option P-A — Route to existing Restrained / Grappled stack (preferred).** On winning the contest and selecting Pin/Hold:  
> - Target gains (or has applied) the appropriate existing Condition record (Restrained or Grappled per DEC-122/124/126/131 stack).  
> - That Condition already zeros or penalises Effective Movement Speed per the locked rules.  
> - Duration / removal follows the Condition’s normal rules (opposed contest to break, end of Effect duration, etc.).  
> - No new “Pinned” Condition is invented; the Position-tier Effect is the *application vector* into the existing record.

> **Option P-B — Lightweight positional mark.** A StateRecord (`Type: Held-Position / Tier Y / Location = current hex`) that forces the target to win an M-0 contest to leave the hex, without applying the full Restrained package. Use only if the designer wants a lighter touch than full Condition application.

> **Never-total discipline (DEC-123):** even under Pin/Hold the target may still declare actions; only movement is constrained via the Condition or the leave-contest.

### (b) Evidence class

- Must reuse existing denial stack — **designer ruling (DEC-082.A R2, DEC-122/123/124/126/131)**
- Position-tier application vector — **recommendation**
- Lightweight alternative — **recommendation** (open)

### (c) Designer questions left open

1. Full Condition application (P-A) or lightweight leave-contest mark (P-B)?
2. Which existing Condition is the default target (Restrained vs Grappled)?
3. Does the pin require continued Engagement, or can it persist after the pin-ner moves away?

*Sources fused: big-pickle P1 route-to-Condition + muse-spark + kilo “reuse Restrained” direction.*

---

## 7. Seize / Deny Ground resolution

### (a) Candidate rules text

> **G-0 Common shell.** Seize / Deny Ground is a Position-tier Effect (DEC-023.A) that contests *control of ground* rather than *possession of a body* (contrast with Pin/Hold). Imposition requires an S-1 win with the Effect selected (DEC-024). Effect Tier = causing Skill-Tier (DEC-107). The record marks **ground**, not the character: a StateRecord with mandatory Location (contested hexes or band). Control confers no HP, no XP, no pool — only movement consequences.

> **Option G-A — Denial-field (entry contest).** While the record persists, any opponent entering the marked ground must first win an M-0 movement contest against the record holder (or against the record’s Tier as passive difficulty — sub-fork). Failure → entry refused at the field edge (distance to edge still debited). Allies of the holder pass freely unless the holder declares otherwise (GM Fiat).

> **Option G-B — Seize with displacement.** Victor declares a ground claim. Target is displaced out of that area by **Y hexes** (same magnitude convention as Forced Movement §5), and the victor occupies it. The loser may not re-enter without winning a new M-0 contest (or facing ZoC machinery if a movement-trigger Tag applies).

> **Option G-C — Unified claim with two intents.** One resolution, two declared intents:  
> - **Seize** = displace + occupy.  
> - **Deny** = prohibit entry (no displacement).  
> Same record type; payload differs only by declared intent at selection time.

> **Binary outcomes only (DEC-030):** a single win either establishes the claim or it does not.

### (b) Evidence class

- Position-tier, ground-not-body — **recommendation** grounded in DEC-023.A list
- StateRecord with Location — **recommendation** (DEC-115 style)
- Entry-contest vs displace-and-occupy vs unified — **recommendation** (open)
- No new resource — **mechanical fact / recommendation** (Invariant 17)

### (c) Designer questions left open

1. Denial-field (G-A), seize-with-displace (G-B), or unified claim (G-C)?
2. Duration of the ground claim (end of turn, until broken, scene, etc.)?
3. Interaction / stacking with ZoC (mutually exclusive, layered, or ZoC is the “soft” version of Seize/Deny)?

*Sources fused: muse-spark G-A/G-B + big-pickle S1 position-ownership + gemini cost-increase note (not adopted as primary).*

---

## 8. Cross-cutting consumption (Fork C preserved)

The DEC-133.A R2 fork remains open. For every mechanic above that can fail a movement contest (Disengage D-A, ZoC Z-C, Chase intervals, M-0, Seize entry):

- **C1** — Failure consumes the entire remaining Movement Distance allowance for the turn.  
- **C2** — Failure consumes only the distance already travelled; remaining allowance may be used for other movement.  
- **C3** — Failure consumes nothing beyond the natural-roll Cost of the contest; distance accounting is independent.

No candidate in this synthesis selects among C1/C2/C3. Designers must rule before promotion.

[EC: designer ruling that the fork exists (DEC-133.A R2); recommendation that it stay open here]

---

## 9. Consolidated designer question list (G1 / human gate)

1. **Disengage shape:** D-A (contested gate), D-B (free + reaction), or hybrid (contest only vs reaction-Tag holders)?
2. **ZoC shape:** cost-overlay (Z-A), pure reaction (Z-B), or gated contest (Z-C)?
3. **Chase shape:** binary band steps (K-A) or Margin accumulation (K-B)?
4. **Forced Movement magnitude:** Tier-scaled (F-A), fixed 1 hex (F-B), or MS-referenced (F-C)?
5. **Pin/Hold vector:** full existing Condition (P-A) or lightweight leave-contest mark (P-B)?
6. **Seize/Deny shape:** denial-field (G-A), seize+displace (G-B), or unified claim (G-C)?
7. **Fork C (consumption):** C1 full allowance, C2 travelled-only, or C3 cost-only?
8. **Fork G (generic contest skills):** framework-fixed lineages or pure content-authoring?
9. **Fork T (extra Skill-Tier gate on Position Effects):** yes or no?
10. **ZoC ↔ Seize/Deny relationship:** exclusive, layered, or soft/hard versions of the same idea?
11. **Default Skill families** for movement contests (Disengage, Chase, M-0)?
12. **Duration defaults** for ground claims and pins?

---

## 10. Invariant 6 / 17 audit (summary)

| Mechanic | Invariant 6 (natural-roll Cost) | Invariant 17 (no competing pool) |
|---|---|---|
| Disengage | Satisfied (full S-1 Cost) | Satisfied (distance is ephemeral allowance) |
| ZoC | Satisfied (reactions are full S-1) | Satisfied (multiplier is accounting, not a pool) |
| Chase | Satisfied (every interval is S-1) | Satisfied (no chase-point pool) |
| Generic M-0 | Satisfied | Satisfied |
| Forced Movement | N/A (Effect payload, not a roll) | Satisfied |
| Pin/Hold | Satisfied (application via contest) | Satisfied (reuses Condition records) |
| Seize/Deny | Satisfied (entry contests are S-1) | Satisfied (ground record is not a pool) |

---

## 11. Provenance & fusion notes

- **Primary structural depth and constraint analysis:** big-pickle run.  
- **Primary multi-option rules text and evidence-class discipline:** muse-spark run.  
- **Compact alternative framings:** gemini-3.1-flash-lite.  
- **Dependency map and prior advisory direction:** kilo-auto-free.  
- **Context hand-off only:** openrouter-free (did not produce full candidate rules text).  

This fusion deliberately keeps every major fork open, labels every substantive claim with an evidence class, and stays inside the Core Invariants and the locked DECs listed in §0.1. It is ready for human (Tiwa) review and for a subsequent assessor pass; it is **not** a promotion candidate until the open questions in §9 are ruled.

---

*End of fusion synthesis.*
