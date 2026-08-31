---
document:
  title: "S-6 Defense — Opening Design Brief"
  version: "1.4-draft"
  status: "Open — fully ruled at brief level (Forks 1–7); Promotion Rule steps 5–8 outstanding"
provenance:
  author_llm:
    name: "Claude Sonnet 5"
    version: "claude-sonnet-5"
  assessor_llm:
    - {name: "opencode", version: "big-pickle"}
  last_modified_by_llm:
    name: "opencode"
    version: "big-pickle"
  created_date: "2026-08-31"
  last_modified_date: "2026-08-31"
---

# S-6 Defense — Opening Design Brief

**Document Version:** 1.4-draft
**Document Status:** Open — all seven Forks (1–7) ruled at brief level (§1a); Promotion Rule steps 5–8 outstanding.
Contains no Canonical material; every ruling below is a **non-canonical designer ruling**.
**Rule Authority:** None — this document creates no Canonical mechanic and no ruling in it is Canonical.
**Prepared By:** Claude Sonnet 5 (`claude-sonnet-5`), Lead Systems Architect / Design Assistant role, working from
the 2026-08-31 curated session brief and conversational context — no live repository access this session.
**Assessed By:** OpenCode (`opencode`/`big-pickle`), documentarian, live repository access, 2026-08-31 — assessed
for factual/documentary consistency and provenance; corrected author-version field and reconciled the "Passive
Guard" verification flag against `proposals/` (see §4/§6). Assessment is review, not a ruling, and confers no
authority.
**Session Participants:**
- Tiwa — human designer, sole ruling authority
- OpenCode (`opencode`/`big-pickle`) — documentarian, live repository access; identified the OPEN-005
  sequencing question and produced the S-5–S-12 dependency grid this brief inherits
- ChatGPT (`ChatGPT-sonnet-5`, per its own self-report — version otherwise not established) — advisory pass on
  S-6, reassessed against the 2026-08-31 curated snapshot; source of the twelve-question framework this brief
  restructures
- Claude Sonnet 5 — this document

**Purpose:** Formally open S-6 (Defense) as the active OPEN-005 subsystem target, consolidate the prior advisory
material into a governance-compliant investigation frame, and state the open forks as questions — now each
resolved by explicit designer ruling (§1a) — pending formal documentation.

---

## 1. Status of this document

This is a **Draft** investigation-staging brief. All seven forks originally identified (§4) have now been
resolved by explicit designer ruling (§1a, below). Per Promotion Rule step 1 (`governance/status-model.md`
§"Promotion Rule"), the document exists to make design questions explicit before analysis/documentation; steps
5–8 (formal documentation, Canonical/Changelog update, source supersession, implementation docs) remain
outstanding for all rulings below. Nothing in this document is Canonical.

### 1a. Ruling record

| Fork | Ruling | Ruled by | Date | Notes |
|---|---|---|---|---|
| Fork 3 — Defense architecture | **Active Defense.** Defender makes a genuine Core Test in response to the incoming Effect. | Tiwa | 2026-08-31 | Full PE/MP cost, full Core consequences (DEC-006/007). Passive Defense, contest-participant, and resource-costed reaction are no longer live candidates. |
| Fork 4 — Who rolls | **The defender rolls.** | Tiwa | 2026-08-31 | Consistent with the working assumption carried in the original candidate framing. |
| Fork 5 — Voluntary decline | **Yes.** The defender may choose not to defend and accept the incoming Effect as applied. | Tiwa | 2026-08-31 | Confirms the candidate previously labeled S-6.2 in prior conversation, now ruled rather than merely carried as candidate. |
| Fork 7 — Roll/resolution-step ceiling | **Uncapped.** No per-action limit on Defense rolls. | Tiwa | 2026-08-31 | **Follow-up investigation flagged for later, unscoped:** whether repeated Defense rolls within a scene/encounter should trigger additional negative effects from fatigue/exhaustion. Explicitly deferred — **no fatigue/exhaustion system currently exists anywhere in the game**, so this cannot be scoped as a rule until such a system (if any) is designed. Not part of S-6's core architecture. Does not block current S-6 work. |
| Fork 2 — Timing vs. DEC-027 auto-apply | **Model B — preserve DEC-027 literally.** The Effect auto-applies exactly as DEC-027 rules; the Active Defense roll acts as post-hoc mitigation on the already-applied Effect, not as a gate preventing application. | Tiwa | 2026-08-31 | Stated reason: increases player agency. DEC-027 is not contradicted or reinterpreted — the Effect genuinely auto-applies in every case; Defense only affects its aftermath/magnitude. The Model A vs. hybrid alternatives (§4 Fork 2 as originally drafted) are no longer live. |
| Fork 6 — DEC-026 deferred defensive position | **Separate mitigation.** Each Effect (the primary Effect and any DEC-026 second Effect) receives its own independent Active Defense mitigation roll, rather than one Defense roll covering the combined outcome. | Tiwa | 2026-08-31 | Stated reason: increases player agency. Consistent with the Model B framing above — each auto-applied Effect is independently mitigable. Raises the roll-count implications of Fork 7's uncapped ruling: a single exchange producing two Effects can now generate two separate Defense rolls. |
| Fork 1 — Defensible-Effect scope | **Universal eligibility.** Any Effect that successfully auto-applies is eligible for Active Defense mitigation — no enumerated/gated list of "defensible" Effects. | Tiwa | 2026-08-31 | Stated reasons: (1) increases player agency; (2) the S-3 Effect menu is currently undefined, so an enumerated list is not yet buildable; (3) **the Effect menu includes positive Effects, not only negative ones** — this is new information not previously addressed in this brief (see note below). |

**Note on Fork 1's third stated reason (positive Effects):** this brief, and the prior ChatGPT advisory pass it
drew on, discussed Defense throughout as resisting/mitigating negative outcomes (Injury, Wound, etc.) without
explicitly considering that the S-3 candidate Effect menu also contains positive Effects. Universal
eligibility as ruled would, on a literal reading, make Active Defense mitigation available against *any*
auto-applied Effect — positive ones included. Whether "mitigating" a positive Effect (e.g. an opponent's
successful advantageous Effect) is coherent, and whether it's actually desired, is not resolved by this
ruling and is flagged here as a follow-up question for whoever next works on the Effect menu or S-6
implementation — not a blocking issue for this brief, but worth surfacing before implementation.

**Authority:** All rulings above are **non-canonical designer rulings** — same status class as DEC-023 onward.
They govern candidate S-6 material only and are not Canonical. **DEC numbers are not assigned here** — per
provenance standard §4.3, numbering is left to OpenCode against the live register's actual next-available
sequence. Promotion Rule step 4 (designer acceptance) is satisfied for each fork above; step 3 (formal
simulation/analysis) was not run for any of these prior to ruling — designer authority is sufficient to rule
ahead of analysis; this is noted rather than corrected. Steps 5–8 remain outstanding for all seven rulings.

**Open status:** All seven forks originally identified in §4 are now ruled. No forks remain open at the level
this brief was scoped to. See §7 for the follow-up item this generates (positive-Effect mitigation) and the
unscoped fatigue/exhaustion item, neither of which blocks closing this brief.

## 2. Sequencing basis — why S-6 now

Per OpenCode's OPEN-005 dependency grid (this session), S-6 depends only on S-1 (Locked), so it is unblocked.
Two considerations were laid out, not recommended, by OpenCode:

- S-6 carries two S-3 rulings already waiting on its resolution: **DEC-026** (second-Effect roll — "target
  gets no defensive roll until S-6 locks") and **DEC-027** (auto-apply as the ruled default, with contested
  application deferred to S-6 as an optional modifier).
- S-5 (Armor) and part of S-11 (Rest/Healing) are lower-friction/momentum picks; S-7/S-8 are higher-leverage
  picks for getting ahead of a likely S-2 non-attack-deferral reopening.

**Designer selection:** Tiwa selected S-6 as the active OPEN-005 target (this session, 2026-08-31). This
satisfies Promotion Rule step 1 for the *sequencing* question only — it does not rule anything within S-6
itself. OPEN-005 remains open as a register; only the "which subsystem is under active investigation now" fact
is settled.

## 3. Upstream ruled/locked material S-6 must not contradict

| ID | Subject | Constraint on S-6 |
|---|---|---|
| DEC-006 | Core Test Transaction | If S-6 invokes a Skill Test, it must be the existing 9-step Core Test Transaction — no parallel resolution engine (Invariant 11). |
| DEC-007 | Cost & Overflow | If S-6 is a Core Test, cost = natural roll; Overflow → direct HP; no second resource pool. |
| DEC-013 | S-1 Opposed Contest | Canonical and complete. S-6 must not modify the S-1 outcome matrix to implement Defense. |
| DEC-016 | Core Architectural Invariants (esp. #17, #18) | No new primary resource or progression currency without explicit designer approval; no competing resource economy. |
| DEC-023–031 | S-3 Outcome Effects | Governs what Effects exist and how they apply; S-6's job is to determine which Effects are defensible and how, not to redefine Effects. |
| DEC-026 | S-3 second-Effect Advanced-Skill roll | Explicitly defers the defensive position on the second Effect to S-6 — this deferral must be resolved by whatever S-6 decides, not bypassed. |
| DEC-027 | S-3 auto-apply default | Auto-apply is the ruled default; contested application is an **optional modifier** deferred to S-6, not the default S-6 must reintroduce. |

## 4. Open forks — stated as questions, then ruled

Per LLM Governance Rule 6 ("never silently resolve an open designer fork") and Rule 4 ("never promote a
proposal because it appears repeatedly"), the four candidate Defense models were carried at **equal standing**
pending the rulings in §1a. All are now ruled; original framing is retained below for the record.

### Fork 1 — What does Defense do? — **RULED: Universal eligibility (see §1a)**

*Original framing retained for the record.*

Two framings were surfaced:
- **Narrow framing:** Defense determines whether a character can resist an Effect that has successfully
  reached them, where the relevant Effect is designated as defensible by S-6.
- **Broad framing (rejected as premature at drafting time, later effectively adopted via universal
  eligibility):** Defense limits/prevents every successful Effect.

**Ruled:** any auto-applied Effect is eligible for Active Defense mitigation; no enumerated defensible-Effect
list is maintained. See §1a for the follow-up flag on positive Effects raised by this ruling.

### Fork 2 — When does Defense occur, relative to S-3 Effect resolution? — **RULED: Model B (see §1a)**

*Original comparison retained for the record.*

| Model | Sequence | Note |
|---|---|---|
| A | S-1 → Effect eligibility → Defense → Effect application | Risks functionally converting every defended Effect into a second contest — needs explicit justification against DEC-027 if selected. |
| B | S-1 → Effect auto-applies (DEC-027) → Defense modifies/mitigates the applied Effect | Preserves auto-apply as literally as possible. |

**Ruled:** Model B — preserve DEC-027 literally (§1a).

### Fork 3 — Defense architecture — **RULED: Active Defense (see §1a)**

*Table retained below for the record of what was compared; Active Defense is no longer open.*

| Candidate | Rolls? | Additional Core Test? | Resource cost | Notes |
|---|---|---|---|---|
| Passive Defense | No roll, or a static value | No | Candidate framing includes a "no PE cost" variant — **verified against `proposals/` as candidate-only (not a Tiwas rule)** (see §6) | Attractive for controlling roll proliferation |
| Active Defense | Defender rolls | Yes, likely | Normal PE/MP per Core Test | Gives defender agency; raises roll-count/resolution-step cost |
| Contest participant (folds into S-1) | Uses existing Core Test as part of the contest | Uses Core Test as part of contest, not necessarily "additional" | Normal Core Test costs | Architecturally clean but risks altering how the S-1 primitive is invoked — must not modify S-1 itself (§3) |
| Resource-costed reaction | Model-dependent | Model-dependent | Explicit resource cost not yet defined | Needs its own resource definition before it can be evaluated against Invariant 17/18 |

**Evaluation axes specified by the project for this comparison:** resource drain, number of rolls,
survivability, tactical choice, resolution-step count.

**Ruled:** Active Defense (§1a). The other three candidates are no longer live.

### Fork 4 — Who rolls, if a roll exists? — **RULED: Defender rolls (see §1a)**

**Ruled:** the defender makes the Active Defense roll (§1a). Not applicable to Passive Defense (no longer live).

### Fork 5 — Voluntary participation — **RULED: Yes, defender may decline (see §1a)**

**Ruled:** the defender may choose not to defend and accept the incoming Effect as applied (§1a).

### Fork 6 — Resolution of the DEC-026 deferred defensive position — **RULED: Separate mitigation (see §1a)**

*Original framing retained for the record.*

**Original question:** Does S-6 introduce a Defense Test after DEC-026's second-Effect roll succeeds, or does
Defense become part of the opposition DEC-026 already represents? **Ruled:** each Effect — the primary Effect
and any DEC-026 second Effect — receives its own independent Active Defense mitigation roll (§1a).

### Fork 7 — Roll/resolution-step ceiling — **RULED: Uncapped (see §1a)**

**Ruled:** no per-action ceiling on Active Defense rolls (§1a).

**Follow-up item generated by this ruling — deferred, unscoped:** whether repeated Defense rolls within a
scene/encounter should carry additional negative consequences from fatigue/exhaustion. Explicitly deferred:
**no fatigue/exhaustion system currently exists anywhere in the game.** This cannot be scoped as a design
question, let alone ruled, until such a system (if one is ever designed) exists to attach it to. Not part of
current S-6 architecture; does not block S-6 work in progress.

## 5. What is firm regardless of which fork resolution is chosen

- **Full Core Test consequences apply whenever Defense is implemented as a Skill Test:** natural d100 roll,
  roll-under, natural-roll cost, Overflow → HP, Failure XP, failed-Double Advanced Skill creation, and normal
  recovery (DEC-006, DEC-007, DEC-012). This is not a candidate — it follows directly from the Canonical Core
  transaction being mandatory for every Skill Test, and is now the operative basis of the ruled Active Defense.
- **No new primary resource or parallel resolution engine** may be introduced regardless of architecture
  selected (Invariants 11, 17, 18).
- **S-1's outcome matrix is not modified** to implement any Defense model (DEC-013).
- **DEC-027's auto-apply default is not overturned by this investigation — and is now further reinforced by
  the Fork 2 ruling (§1a):** the Effect auto-applies exactly as DEC-027 states in every case; Active Defense
  never gates or prevents application, only mitigates its aftermath. This closes off any future drift toward
  a de facto contested-application model.

## 6. Advisory input received (pointer, not inline ruling)

An advisory pass by ChatGPT (session-scoped, working from the 2026-08-31 curated brief) proposed Active
Defense as the strongest candidate for further investigation and proposed carrying "voluntary
non-participation" forward as a candidate rule tied to that model. That ranking was **not adopted** in this
brief before ruling — all four candidates were carried at equal standing until Tiwa selected Active Defense
(§1a, Fork 3).

**OpenCode verification (2026-08-31):** the same pass referenced a "Passive Guard (half-Skill, no PE cost)"
candidate. This **is confirmed to exist** in
`proposals/tiwas-proposals-wip-and-design-direction-v1.4.3.md:523`, explicitly stated as **candidate-only, not
a Tiwas rule** (line 525), alongside the same four candidate Defense models and the same five evaluation axes
(lines 515–533). The verification flag is therefore **resolved**. (Independent of this, the Fork 3 ruling in
favour of Active Defense makes the "Passive Guard" framing moot for current S-6 work; it is retained on record
as a candidate only.)

## 7. Next steps (sequencing only — not rulings)

1. ~~OpenCode: confirm "Passive Guard" candidate status in `proposals/`~~ — **resolved (§6): exists as
   candidate-only.** Moot for Fork 3 following the Active Defense ruling; retained on record.
2. ~~Designer ruling on Fork 2 (timing Model A vs. B)~~ — **RULED: Model B, §1a.**
3. ~~Designer ruling on Fork 4 (who rolls)~~ — **RULED: defender rolls, §1a.**
4. ~~Designer ruling on Fork 5 (voluntary decline)~~ — **RULED: yes, §1a.**
5. ~~Designer ruling on Fork 7 (roll/resolution-step ceiling)~~ — **RULED: uncapped, §1a.**
6. ~~Designer ruling on Fork 6 (DEC-026 deferred defensive position)~~ — **RULED: separate mitigation per
   Effect, §1a.**
7. ~~Designer ruling on Fork 1 (defensible-Effect scope)~~ — **RULED: universal eligibility, §1a.**
8. **OpenCode: assign the actual DEC number(s) for the seven rulings above against the live register's
   next-available sequence** (see §1a Authority note; done as DEC-044–050).**
9. **New follow-up, not blocking:** positive-Effect mitigation question raised by the Fork 1 ruling (§1a) —
   does Active Defense mitigating a positive Effect make sense, and is it desired? Needs attention once the
   S-3 Effect menu is actually defined (it is currently undefined per the Fork 1 ruling's own stated reason).
10. **Deferred, not blocking:** fatigue/exhaustion-from-repeated-rolls investigation flagged under Fork 7.
    Cannot be scoped until a fatigue/exhaustion system exists elsewhere in the game — none currently does.
    Revisit if/when such a system is proposed.
11. Formal documentation, Canonical/Changelog update (if promoted beyond candidate status), source-proposal
    supersession, and implementation-doc updates — Promotion Rule steps 5–8 — remain the outstanding work to
    fully close this brief.

---

*End of brief. All seven forks originally identified in §4 have been ruled (§1a). Promotion Rule steps 5–8
remain outstanding before any of this is Canonical. Nothing in this document is Canonical.*
