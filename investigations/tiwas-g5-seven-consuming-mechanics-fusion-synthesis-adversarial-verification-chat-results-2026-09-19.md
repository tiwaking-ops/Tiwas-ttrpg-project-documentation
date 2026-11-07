---
document:
  title: "Red-Team Verification of Fusion Synthesis — Seven Consuming Mechanics Draft (DEC-133.A R3): Complete Chat Results for OpenCode"
  version: "1.0"
  status: "Non-canonical advisory record — OpenCode chat-results report; no authority-changing action authorized; independent assessment recommended per governance/provenance.md"
  authority: "Verification record only"
  scope: "Complete results of the independent adversarial verification (red-team) of the non-canonical draft `tiwas-g5-seven-consuming-mechanics-fusion-synthesis-2026-09-19.md` against the Core Invariants and the live decision register. Produced for the OpenCode control plane as required by the Tiwas GDD Multi-LLM Orchestration Plan (roadmap/tiwas-gdd-multi-llm-orchestration-plan-v0.1-2026-09-18.md)."
provenance:
  author_llm: {name: "upstage", version: "solar-pro4:free"}
  assessor_llm: {name: "not established", version: "not established"}
  last_modified_by_llm: {name: "upstage", version: "solar-pro4:free"}
  created_date: "2026-09-19"
  last_modified_date: "2026-09-19"
  note: "Authored / assessed / last-modified by the same model in a single pass. Single-model self-assessment is a weaker form of review than an independent second pass; it is recorded honestly as such and confers no authority. Recommendation: a separate-model independent review before the designer gate (G1) consumes these findings."
reviewed_document:
  title: "Fusion Synthesis — Seven Consuming Mechanics Candidates (DEC-133.A R3)"
  file: "tiwas-g5-seven-consuming-mechanics-fusion-synthesis-2026-09-19.md"
  status: "Non-canonical advisory"
  decision_reference: "DEC-133.A R3"
  scope: "Candidate rules text for the seven consuming mechanics remaining open under DEC-133.A R3: Disengage, Zone of Control, Chase, generic movement contests, Forced Movement magnitude, Pin/Hold Position resolution, Seize/Deny Ground resolution."
---

# Red-Team Verification — Fusion Synthesis Draft (DEC-133.A R3): Complete Chat Results

**Author:** upstage (version: solar-pro4:free)
**Assessment date:** 2026-09-19
**Report status:** Non-canonical advisory record. **Nothing herein is Canonical; no DEC is inferred; no authority is changed; no recommendation is adopted by force of this record.**

**This report is the full formal deliverable for the OpenCode control plane.** It is generated from the complete turn-by-turn verification already performed in this chat: a single-model independent adversarial verification (red-team) of the draft `tiwas-g5-seven-consuming-mechanics-fusion-synthesis-2026-09-19.md` against (a) the project's Core Invariants and locked invariant spec-card content, and (b) the live decision register (`_consolidation/decision-register.md`, through DEC-145). The draft was **not** rewritten; the original verifier-only report (`verifier-report-tiwas-g5-fusion-synthesis-2026-09-19.md`) is the source truth for the detailed findings and should be read alongside this summary.

---

## 1. Purpose and positioning

This session was contracted as the **Adversarial Verifier** role from the orchestration plan (`roadmap/tiwas-gdd-multi-llm-orchestration-plan-v0.1-2026-09-18.md`, §2, §3 P2): a model **not in the drafter pool** red-teams a candidate draft against the spec card's locked invariants and the live decision register, produces a pass/fail + contradiction report, and surfaces but does not resolve open designer forks.

The task instruction said "Report only: invariant violations, silent assumptions, contradictions with existing DECs, and unresolved designer forks. Do not rewrite the draft. Also flag any claim missing an evidence class."

The report therefore contains **only** the five classes the instruction demanded:

1. invariant violations
2. silent assumptions
3. contradictions with existing DECs
4. unresolved designer forks
5. claims missing an evidence class

plus a compact positive-judgment summary and a consolidated OpenCode-facing finding list.

---

## 2. Documents examined

| Document | Role in verification |
|---|---|
| `tiwas-g5-seven-consuming-mechanics-fusion-synthesis-2026-09-19.md` | Draft under review (339 lines; seven-machinery candidate rules text, §0–§11) |
| `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` | Canonical invariant source (§16; 18 invariants, especially 6, 17, 18) |
| `_consolidation/decision-register.md` | Live decision register, DEC-001 … DEC-145 (incl. DEC-023.A, DEC-024, DEC-026, DEC-030, DEC-082.A, DEC-095, DEC-107, DEC-122/124/126/131, DEC-132.A/B, DEC-133/A, DEC-138) |
| `roadmap/tiwas-gdd-multi-llm-orchestration-plan-v0.1-2026-09-18.md` | Pipeline definition + spec-card-as-contract framing for the verifier role |
| `governance/provenance.md` | Provenance block conventions (author_llm / assessor_llm / last_modified_by_llm / dates) |
| `governance/authority.md` | Authority boundary for Canonical vs non-canonical material |
| `governance/status-model.md` | Status lifecycle, evidence-class vocabulary, Promotion Rule, LLM Governance Rules |

No separate stored spec-card file exists in the repository for this section. The draft's own §0.1 "Locked constraints any candidate must survive" is a self-constructed summary, not a governed spec card, so this verification independently re-derived the constraint set from Canonical §16 + the live register rather than treating §0.1 as a contract.

---

## 3. Verification results

### 3.1 Invariant results

**Invariant 6 — Cost = natural roll (Canonical §16, DEC-016).**

- **Verdict:** No formal violation found. All seven candidate rule sets use full-Cost S-1 opposed contests (DEC-006/DEC-013) with no modification to the natural d100 roll.
- **Soft spot:** The Zone-of-Control Z-A option ("2 hexes of Movement Distance allowance per 1 hex traversed") is justified with language about "second Cost channel." In the Canonical taxonomy, "Cost" = natural roll paid from a resource pool; distance accounting is not "Cost" in that sense. The draft's language therefore muddles Invariant 6 with Invariant 17 framing rather than cleanly separating them. This is a precision issue in the justification, not a mechanics violation — recorded as contradiction **RC-1** and silent assumption **SA-4** in the detailed report.

**Invariant 17 — no competing resource/progression economy (Canonical §16, DEC-016).**

- **Verdict:** No formal violation found. No candidate creates a stored movement fund, per-scene movement counter, or second progression channel; movement remains described as ephemeral per-turn Movement Distance allowance.
- **Silent assumption flagged:** The draft treats Movement Distance allowance as definitively ephemeral and per-turn in its Invariant-17-compliance argument for Z-A and for the suite as a whole. The closest anchors (DEC-133(3) and DEC-095) establish the **size** of the allowance and that it does not cost a substantive action, but no DEC in the live register explicitly locks the statement "Movement Distance allowance is a purely ephemeral per-turn allowance and may not become a tracked per-scene resource." This is intended design and almost certainly correct, but per the project's AGENTS.md (evidence-before-interpretation principle) it should not be presented as if it is already locked. Recorded as silent assumption **SA-4** in the detailed report.

**Invariant 18 — build on the Core Test Transaction; no separate "movement engine" (Canonical §16, DEC-016).**

- **Verdict:** PASS. All seven mechanics are expressed as S-1 opposed contests (DEC-013) or as Effect payloads under DEC-023.A Position tier; no parallel resolution engine is introduced.

**Bottom line on invariants:** The draft is invariant-clean in shape. The issues are (a) justification-language precision, and (b) one silent assumption about the status of Movement Distance as a non-pool. There is no case here of a candidate candidate rule actually breaking Invariant 6, 17, or 18.

---

### 3.2 Contradictions with existing DECs and citation-accuracy issues

The verification found **two register contradictions**, **one citation-imprecision** that is not false but is misleading, and **several provenance/citation-accuracy problems** in the draft's own documentation layer.

#### RC-1 — "One Effect per win; no graded outcomes" misattributed to DEC-024/DEC-030

- **Where found:** Draft §0.1 table ("DEC-024 / DEC-030 — One Effect per win; no graded outcomes"); repeated in draft §5 (Forced Movement) "Binary outcome (DEC-030)"; repeated in draft §7 (Seize/Deny G-C) "Binary outcomes only (DEC-030)".
- **What the live register actually says:**
  - DEC-024 (line 217): "Flat one-Effect-per-win. No Quality-based scaling, no purchasing of additional Effects off a single win." That is the seat of "one Effect per win; no Quality scaling."
  - DEC-030 (line 224): "Partial Tag/Location match → fail-and-fall-back to Base-tier Inflict Injury (HP-only form)." DEC-030 is about partial-match fall-back, **not** about "Effect magnitude is binary / Quality does not buy extra hexes."
- **Why it matters:** The claim itself ("Quality does not buy extra hexes / magnitude is binary") is correct and well-anchored in DEC-024, DEC-107, and DEC-023.A content policy. The problem is that **DEC-030 is cited as if it rules that**. That is a contradiction with the register's own labeling. Repeated three times, so it is a pattern, not a typo.
- **Classification:** Contradiction with existing DEC labeling (correct outcome, wrong anchor). Not a canon violation, but a citation-accuracy defect that would mislead downstream readers.

#### RC-2 — DEC-082.A R2 presented as if it directly commands Pin/Hold to reuse the existing Condition stack

- **Where found:** Draft §0.1 ("DEC-082.A R2 — Movement-denial × Movement Speed question is closed. Pin/Hold must reuse existing Condition stack (DEC-122/123/124/126/131), not reopen it.")
- **What the live register actually says:** DEC-082.A R2 (line 113) closes the movement-denial × Movement Speed question using DEC-122/123/131. It does **not** name Pin/Hold. The step from "movement-denial × Movement Speed is closed" to "therefore Pin/Hold must reuse existing Condition stack" is a reasonable inference one could defend to a designer, but the draft writes it as if DEC-082.A R2 says exactly that. It does not.
- **Classification:** Inference presented with the appearance of a direct citation. Should be recorded as "designer ruling (DEC-082.A R2) + inference to Pin/Hold routing," not a bare DEC-082.A R2 citation. Evidence-class and citation-accuracy issue.

#### RC-3 — Pin P-A's description of Grappled denial is insufficiently accurate for the live Grappled state

- **Where found:** Draft §6 P-A — "That Condition already zeros or penalises Effective Movement Speed per the locked rules," and "Restrained or Grappled per DEC-122/124/126/131 stack" as options.
- **What the live register actually says:**
  - DEC-122 (line 157): uniform self-referential-Y total-lock overlay for Stunned / Incapacitated / Restrained / Grappled / Prone — but this is the **overlay** model, and DEC-122 itself is provisional.
  - DEC-124 (line 159): Grappled movement restriction = contested Break-Hold model; moving away from grappler requires breaking the Grapple; the fail-vs-relocate outcome was deferred.
  - DEC-131 (line 166): resolved the deferred item — Option A "Pure Break" adopted; fail = Grapple persists / mover locked / no relocation; success = stepwise Heal-Effect-System Grapple removal; "relocate both" branch **dropped**.
- **Why it matters:** "Zeroes or penalises Effective Movement Speed per the locked rules" fits Restrained cleanly. For Grappled, the operative denial mechanism is a contested Break-Hold check with stepwise removal and no relocation-on-fail — not simply an Effective-MS zero overlay. If Pin/Hold routes to Grappled, P-A's generic statement is inaccurate for that branch. The draft should describe Grappled's actual denial mechanism or qualify that the Grappled branch carries additional contested-break semantics per DEC-124/DEC-131.
- **Classification:** Contradiction with the live register on the Grappled branch of Pin/Hold. Substantial enough that a designer reading "Condition already zeros or penalises Effective Movement Speed" would mis-model Grappled denial if they never read DEC-124/DEC-131.

#### RC-4 — P-B and Seize record proposals invent new StateRecord types without anchoring to the unified-schema DECs

- **Where found:** Draft §6 P-B ("StateRecord(Type: Held-Position / Tier Y / Location = current hex…)"); draft §7 G-A/G-B/G-C (ground-control StateRecords with mandatory Location).
- **What the live register actually says:** DEC-115 (line 150) is the unified schema (`Type / Tier Y / Magnitude Z / optional Location X`) and DEC-117 (line 152) extends it to Tags and adds counter/removal machinery.
- **Why it matters:** P-B and the Seize record proposals are correctly labeled "recommendation" in most places, but they are **not anchored to any DEC** and do not engage the schema machinery that would govern a new record Type — whether a new record needs a governing Effect to create it, a removal route, or counter-rule interaction. This is an engineering gap in an otherwise-fine recommendation. §7(b) ZoC/Seize evidence classes use the informal phrase "DEC-115 style"; that is not a false claim, but it is weak documentation for a proposal to invent new record types.
- **Classification:** Missing evidence-class anchor + missing schema citation for a record-schema-level recommendation.

---

### 3.3 Silent assumptions

The verification found **six silent assumptions**.

**SA-1 — Disengage as a movement-trigger eligible to provoke a reaction (D-B).**
Draft §1 D-B assumes leaving Engagement is a movement-trigger episode under the DEC-132.A R1 trigger taxonomy. The movement-trigger **category** is ruled (DEC-132.A R1); whether a specific case like "leaving Engagement" counts as a movement-trigger is content-authoring/DEFINITIONAL (DEC-077.A). The draft cites DEC-132.A R1 + DEC-077.A for the reaction category, but does not flag that the **application** of the category to Disengage is an assumption. Should be surfaced as fork/assumption, not stated as given.

**SA-2 — Chase can run on bands alone without a separate track (K-A).**
Draft §3 K-A rules text runs Chase purely in band terms and says "once per turn of the pursuing party" without resolving whether the Chase interval **is** the pursuer's substantive action for the turn. The note that DEC-030 forbids graded chase unless a separate chase track is content-authored is the right protection, but K-A's rules text itself leans on an unresolved action-economy answer and only raises it later in §3(c). The rules text presupposes an action-economy outcome it has not resolved.

**SA-3 — "Moving through controlled space is a movement-trigger" (Z-B).**
Same class as SA-1: applies the movement-trigger category to a specific case not expressly locked. Reasonable, not established. Flagged.

**SA-4 — Movement Distance allowance is definitively ephemeral/per-turn (no pool).**
Cross-referenced in §3.1 as the Invariant-17-compliance foundation for Z-A and the whole suite. Intended, but not explicitly locked by any DEC the draft cites. The draft should not present "Movement Distance allowance is a per-turn ephemeral allowance that cannot become a tracked resource" as an already-locked property. Recorded also as the basis for RC-1's soft spot.

**SA-5 — Provenance frontmatter author_llm "grok-fusion" does not match §11 source-run list.**
The draft's frontmatter says `author_llm: {name: "grok-fusion", version: "multi-llm-synthesis-2026-09-19"}`. The draft's §11 "Provenance & fusion notes" attributes primary structural depth/constraint analysis to **big-pickle**, primary multi-option rules text + evidence-class discipline to **muse-spark**, compact alternative framings to **gemini-3.1-flash-lite**, dependency map + advisory direction to **kilo-auto-free**, and context hand-off to **openrouter-free**. The named author model "grok-fusion" does **not appear** in the §11 source-run list. The actual authoring/fusion model is therefore ambiguous. Per the orchestration plan and governance/provenance.md, the `author_llm` field should identify the model that **produced this fused document**, and the source runs should be reflected consistently. This is a provenance-record defect — not a mechanics issue, but a real defect for a document that relies heavily on provenance discipline.

**SA-6 — M-0 "or simply succeeds at the declared movement objective if no Effect is required" embeds an open sub-question as if decided.**
Draft §4(a) M-0 rules text says the winner "selects one Position-tier Effect they are entitled to (or simply succeeds at the declared movement objective if no Effect is required)." Fork T (Position-tier gate) is listed as open, and §9 #2 explicitly asks whether "pure 'I get the hex' win still requires selecting a Position-tier Effect, or is objective success sufficient?" The parenthetical is embedded inside the candidate rules text without a fork marker or EC tag, even though the question is explicitly open. This is a soft narrowing risk — comparable to the draft's own annotation discipline in §6 P-0.

---

### 3.4 Unresolved designer forks — preservation check and soft-narrowing risks

#### Forks correctly preserved

The draft **does** preserve the major carried-open forks and does **not** collapse them:

- **Fork C (contested-movement consumption):** preserved in §0.3, §8, and §9 #7.
- **Fork G (generic contest skill/payload):** preserved in §0.3 and §9 #8.
- **Fork T (extra Skill-Tier gate on Position-tier Effects):** preserved in §0.3 and §9 #9.
- **Per-mechanic shape forks:** Disengage D-A/D-B/hybrid; ZoC Z-A/Z-B/Z-C; Chase K-A/K-B; Forced Movement F-A/F-B/F-C; Pin P-A/P-B; Seize G-A/G-B/G-C — all preserved in their sections and consolidated in §9.

That is the right structural behavior for a fusion draft and is a genuine positive.

#### Soft-narrowing risks where candidate rules text presupposes one fork outcome

Even where forks are preserved at the section level, some candidate rules text leans into one fork outcome inside the rules text itself:

- **UF-1 (Fork T):** M-0 "Winner selects one Position-tier Effect they are entitled to" uses "entitled to" as if the gate is already defined. Should be qualified as fork-dependent.
- **UF-2 (Fork G):** M-0 "Skills: content-authored movement/agility/strength lineages (Fork G)" leans toward the content-authoring side of an open fork inside rules text, rather than neutrally stating "Skill lineages per Fork G (open)."
- **UF-3 (ZoC ↔ Seize/Deny relationship):** §9 #10 preserves the open relationship, but Seize G-B's parenthetical "or facing ZoC machinery if a movement-trigger Tag applies" presupposes ZoC and Seize/Deny can coexist as distinct layers — one open option, not the decided answer. Should be flagged fork-dependent.
- **UF-4 (Chase action economy):** see SA-2. K-A presupposes the Chase interval's action-economy role without resolving it.
- **UF-5 (Fork-C-adjacent distance-debit embedded inline without Fork-C annotation):** G-A "distance to edge still debited" and similar inline distance-debit consequences appear in candidate rules text without the Fork-C label the draft applies in §8. These should carry a Fork-C annotation or be marked fork-dependent, consistent with the draft's own §8 house style. The clearest case is G-A.

---

### 3.5 Claims missing an evidence class, or with a mismatched class

The verification found **six evidence-class defects**:

- **EC-1 (§0.1 global tag):** The §0.1 tag `[EC: mechanical fact for Invariants; designer ruling for listed DECs]` lumps invariant-interpretation reasoning under "mechanical fact." The **existence** of the invariants is mechanical fact (DEC-016 is Canonical/locked). But the **justification** (e.g. "Distance multipliers are position accounting, not a second Cost channel that violates the invariant") is the author's analysis/recommendation, not a mechanical fact. The tag should separate "invariant exists — mechanical fact" from "candidate satisfies it — recommendation/analysis."
- **EC-2 (§4(a) M-0 Cost claim):** §4(a) M-0 rules text states "Cost: full natural-roll Cost for each participant (Invariant 6)" without its own EC tag. §4(b) tags S-1-as-universal-primitive, one-Effect-per-win, and Skill lineage, but does not restate the Cost claim individually. The draft's house style elsewhere tags substantive claims individually; this one is left to block inference.
- **EC-3 (§5(b) Forced Movement):** "No graded Quality magnitude — designer ruling (DEC-030)" cites the wrong DEC. Correct anchors: DEC-024, DEC-107, DEC-023.A. Evidence class "designer ruling" is correct for the claim; the cited DEC is wrong. Same root as RC-1.
- **EC-4 (§6(a) Pin P-A duration/removal):** "Duration / removal follows the Condition's normal rules (opposed contest to break, end of Effect duration, etc.)" lacks its own EC tag and DEC citation. The Break-Hold contest existence for Grappled is established by DEC-124/DEC-131; the general duration/removal rules for Conditions are established by DEC-079 alpha vocabulary + DEC-135.A removal routes. The claim cites neither.
- **EC-5 (§7(b) Seize/Deny):** "StateRecord with Location — recommendation (DEC-115 style)" is an informal citation. The governing schema is DEC-115 (and DEC-117 for extension/counter/removal). Should cite DEC-115 directly rather than "DEC-115 style."
- **EC-6 (§3(b) Chase "No roll-less Speed contest — mechanical fact / recommendation"):** Dual-labeled. Acceptable as capturing both the invariant grounding and the design interpretation. Noted for transparency, not a defect.

---

## 4. What the verification found that is correct

For OpenCode's benefit, the substantive positives are:

- The draft carries the project's mandatory governance preamble.
- It labels evidence classes per claim in most of the body.
- It preserves Forks C, G, and T as open and does not collapse them.
- It presents multiple candidate shapes per mechanic rather than silently picking one.
- It cites DEC IDs throughout.
- It keeps status `Non-canonical advisory`.
- It does not resolve open designer forks or promote anything.
- The §10 invariant audit table is a useful summary structure, even where individual justifications are loose.

The draft is **fit for purpose as non-canonical advisory material** in structure and intent. The defects are in the documentation/precision layer, not in the candidate mechanics themselves.

---

## 5. Decisions and conclusions

- **No DEC was inferred, ruled, promoted, demoted, or superseded in this chat.** All seven consuming mechanics remain carried-open as Position-tier Effects under DEC-023.A / DEC-133.A R3, exactly as the register establishes.
- **The draft passes the Core Invariants in shape** for Invariant 6, 17, and 18. There is no case in which a candidate rule actually breaks an invariant.
- **The draft is not yet clean enough to consume without attention to the documentation/precision layer.** The issues are: one register contradiction-pattern (RC-1), one register over-read (RC-2), one Grappled-denial inaccuracy (RC-3), one schema-anchoring gap (RC-4), six silent assumptions, several soft-narrowing risks inside candidate rules text, and six evidence-class defects. None of these change authority; all of them are worth fixing before the next sprint or before the designer gate (G1) consumes the draft.
- **Storage recommendation:** Consistent with `governance/status-model.md` and the draft's own header instruction, the draft and this report remain non-canonical; placement in `proposals/` or `investigations/` is appropriate. Neither storage nor assessment confers authority.
- **Independent-assessment recommendation:** Per the project's healthy review discipline (`audits/README.md`; single-model self-assessment caveat in `governance/provenance.md`), a **separate-model independent review** of this verification is recommended before G1 consumes its findings.

---

## 6. Unresolved issues / next steps (for OpenCode)

1. **Designer (Tiwa) ruling requests derived from this verification:**
   - RC-1/UF-3 zone: Does the Z-A "2 hexes per 1 hex" distance multiplier require its own designer ruling to be Invariant 6/17-safe, or is the accounting-vs-currency framing sufficient (perhaps sharpened)?
   - RC-2/C2 zone: Should P-0 cite DEC-079's alpha vocabulary for the Condition stack rather than / alongside DEC-122/123/124/126/131?
   - RC-3 zone: Should P-A describe the Grappled branch's actual denial mechanism (contested Break-Hold + stepwise removal + no relocation-on-fail per DEC-124/DEC-131), or explicitly limit itself to the Restrained branch?
   - SA-4 zone: Should the project explicitly lock that Movement Distance allowance is per-turn ephemeral and non-poolable, so later designs can depend on it without silent assumption?

2. **Drafting corrections before the next sprint (if the drafter pool re-works the file):**
   - Fix the DEC-024/DEC-030 misattribution for "no graded outcomes" throughout §0.1, §5, §7.
   - Recast the DEC-082.A R2 Pin/Hold citation as "designer ruling (DEC-082.A R2) + inference."
   - Anchor P-B and the Seize record proposals to DEC-115/DEC-117 and state which fields they use.
   - Tag the M-0 Cost claim individually, or make the block tag explicit.
   - Reconcile the frontmatter `author_llm` with §11 source-run attribution.

3. **Designer-question list not resolved by this chat:**
   - The 14 designer questions consolidated in the detailed verifier report (`verifier-report-tiwas-g5-fusion-synthesis-2026-09-19.md` §9) remain agenda material. None are answerable by any LLM under current governance.

4. **Wiring for OpenCode's pipeline:**
   - According to the orchestration plan, this adversarial-verification result feeds P2 (Verify) → P3 (Merge/fusion) → P4 (Human gate G1). The verifier report should travel with the draft until Tiwa rules on the C/RC/SA/UF items.
   - Pending verifier-model selection per orchestration plan §9 item 2 — requirement is only that it is not in the drafter pool; recorded open.

5. **No repository governance item was reopened or resolved** as part of this chat.

---

## 7. Appendix — operational notes from this chat

For future OpenCode sessions working in this repository:

- The project is **Windows / PowerShell 5.1** under git-bash/MSYS for terminal calls, so command syntax matters: `&&` chaining and some PowerShell builtins behave differently than the docs sometimes imply. Verify shell behaviour before chaining.
- Large files (`decision-register.md`, the draft, JSON candidates) truncate at ~2000 lines per read; re-read with `offset` or use targeted content search of DEC rows before drawing conclusions.
- File reads returning partial content should be re-issued with an offset before concluding. In this session the draft's frontmatter was confirmed at first read, but the body required a second read.

---

## 8. Sources and provenance of this report

- Primary source of findings: the detailed verifier-only report `verifier-report-tiwas-g5-fusion-synthesis-2026-09-19.md` (written in this session), which contains the full justification, line references, and classification for every item summarized here.
- Governing documents referenced inline: `canonical/rules/tiwas-canonical-rules-and-changelog-v1.3.md` §16; `_consolidation/decision-register.md` DEC-001…DEC-145; `governance/provenance.md`; `governance/authority.md`; `governance/status-model.md`; `roadmap/tiwas-gdd-multi-llm-orchestration-plan-v0.1-2026-09-18.md`.
- This report itself is **non-canonical advisory material**. It does not create game mechanics, does not close any open designer fork, and does not promote any draft or finding.

---

**End of report.** This record is non-canonical advisory material. It confers no authority and changes no document status. The substantive findings are in `verifier-report-tiwas-g5-fusion-synthesis-2026-09-19.md`; this file is the OpenCode-facing formal summary.
