---
document:
  title: "G5 Seven Consuming Mechanics — Spec Card (DEC-133.A R3)"
  version: "P0-2026-09-19"
  status: "Proposal (non-canonical)"
  authority: "Non-canonical advisory material only; no DEC inferred; no authority-changing action authorized"
  scope: "Candidate rules text for the seven consuming mechanics left open by DEC-133.A R3: Disengage, Zone of Control, Chase, generic movement contests, Forced Movement magnitude, Pin/Hold Position resolution, Seize/Deny Ground resolution. This spec card is the contract a drafter agent must satisfy; no DEC is inferred or resolved hereby; nothing herein is promoted, demoted, or superseded."
  provenance:
    author_llm: {name: "opencode", version: "big-pickle"}
    assessor_llm:
      - {name: "not established", version: "not established"}
    last_modified_by_llm: {name: "opencode", version: "muse-spark-1.3-contributor-free"}
    created_date: "2026-09-19"
    last_modified_date: "2026-09-19"
    note: "This is a proposal spec card for the G5 seven-consuming-mechanics section (DEC-133.A R3). It establishes the locked constraints, open questions, and dependency chain for drafter agents. No DEC is inferred; all authority remains with the designer gate (G1) and formal promotion process (G2)."
    storage_note: "Stored in proposals/ as a draft spec card per the multi-LLM orchestration plan. Advisory-only; no DEC inferred; no authority conferred."
  ---

# G5 Seven Consuming Mechanics — Spec Card (DEC-133.A R3)

**Status:** Proposal (non-canonical advisory). Candidate rules text for the seven consuming mechanics left open by **DEC-133.A R3**. This spec card is the contract a drafter agent must satisfy; no DEC is inferred or resolved hereby; nothing herein is promoted, demoted, or superseded.

**Purpose.** Provide candidate implementations for: **Disengage, Zone of Control, Chase, generic movement contests, Forced Movement magnitude, Pin/Hold Position resolution, Seize/Deny Ground resolution**. Each candidate must (a) be expressible as rules text, (b) carry an evidence class per claim, (c) present open designer forks rather than silently collapsing them.

---

## 0. Locked constraints any candidate must survive

### 0.1 Core Invariants (Canonical §16)

| Invariant | Requirement | Implication for candidates |
|---|---|---|
| **Invariant 6** — Cost = natural roll | Every contested resolution is a full Core Test (DEC-006); natural d100 never modified. Distance multipliers are position accounting, not a second Cost channel that violates the invariant, but they interact with the open consumption fork. | No candidate may modify the natural d100 roll; all opposed contests must be full S-1 with normal Cost. |
| **Invariant 17** — no competing resource pools | No stored movement tokens, per-scene counters, or second progression channel. Only natural-roll Cost + ephemeral per-turn Movement Distance allowance. | Movement Distance allowance must remain ephemeral and per-turn; no new resource pools may be introduced. |
| **Invariant 18** — build on Core Test | No separate “movement engine.” Chase, ZoC contests, Disengage contests, etc. are S-1 (DEC-013). | All mechanics must be expressible as S-1 opposed contests or as Effect payloads under DEC-023.A Position tier; no parallel resolution engine. |

### 0.2 Locked Designer Rulings (DEC-133.A R3 + DEC-147/148)

| DEC | Subject | Decision | Implication for candidates |
|---|---|---|
| **DEC-133.A R3** | G5 seven consuming mechanics | Remain open as Position-tier Effects under DEC-023.A; not added to DEC-023.A alpha list. | Candidates must be Position-tier Effects (DEC-023.A) but not necessarily listed in DEC-023.A's alpha enumeration. |
| **DEC-147** | Movement Distance ephemerality | Movement Distance derived per turn from live effective MS; never stored/banked/tracked per scene. Mid-turn MS change: remaining = effective MS at query − hexes spent, floored at 0; no debt; rises grant movement. | Candidates must treat Movement Distance as ephemeral per-turn allowance; no per-scene tracking; mid-turn MS changes follow the formula. |
| **DEC-148** | Position-tier substrate clarification | "Consuming mechanics operating on the Position-tier substrate," not "added to the DEC-023.A alpha list." | Candidates operate on Position-tier substrate but do not need to be explicitly listed in DEC-023.A's alpha content. |

### 0.3 Locked Content (DEC-024, DEC-082.A R2, DEC-095, DEC-133)

| DEC | Subject | Decision | Implication for candidates |
|---|---|---|
| **DEC-024 / DEC-030** | One Effect per win; no graded outcomes | Forced Movement, Pin/Hold, Seize/Deny are mutually exclusive selections unless DEC-026 cash-out is engaged. | Each contest produces exactly one Effect; no Quality-based scaling of Effect magnitude. |
| **DEC-082.A R2** | Movement-denial × Movement Speed question closed | Pin/Hold must reuse existing Condition stack (DEC-122/123/124/126/131), not reopen it. | Pin/Hold must route to existing Condition machinery; cannot invent new Condition types. |
| **DEC-095** | Movement free/bundled side-activity | One substantive action per turn; movement is free/bundled. | Movement contests do not consume the substantive action; they are side-activities. |
| **DEC-133 Hybrid** | Movement Distance = Effective Movement Speed | 1 MS = 1 hex/turn; band model remains; band↔hex boundaries are content-authoring (DEC-077.A). | Movement Distance allowance is directly tied to Effective Movement Speed; hex conversion is content-authoring. |

---

## 1. Open questions (to be ruled by Tiwa at G1)

### 1.1 Seven mechanics shape forks

| Mechanic | Fork | Options | Status |
|---|---|---|---|
| **Disengage** | D-A vs D-B vs hybrid | D-A (contested S-1 gate), D-B (free exit + reaction), hybrid (contest only vs reaction-Tag holders) | Open (G1) |
| **Zone of Control** | Z-A vs Z-B vs Z-C | Z-A (cost-overlay), Z-B (pure reaction-enabler), Z-C (gated pass-through contest) | Open (G1) |
| **Chase** | K-A vs K-B | K-A (binary band steps), K-B (margin-accumulation track) | Open (G1) |
| **Forced Movement** | F-A vs F-B vs F-C | F-A (Tier-scaled hexes), F-B (fixed 1 hex), F-C (MS-referenced) | Open (G1) |
| **Pin/Hold** | P-A vs P-B | P-A (full existing Condition), P-B (lightweight leave-contest mark) | Open (G1) |
| **Seize/Deny** | G-A vs G-B vs G-C | G-A (denial-field), G-B (seize + displace), G-C (unified claim) | Open (G1) |

### 1.2 Cross-cutting forks

| Fork | Description | Status |
|---|---|---|
| **Fork C** (contested-movement consumption) | Does a failed movement contest consume the mover’s remaining Movement Distance allowance for the turn, only the distance already travelled, or nothing beyond the natural-roll Cost? | Open (G1) |
| **Fork G** (generic movement contest skill/payload) | Which Skill lineages and what payload selection rules apply to the shared primitive? | Open (G1) |
| **Fork T** (extra Skill-Tier gate on Position-tier Effects) | Does Position-tier require only the DEC-023.A unlock, or an extra Skill-Tier threshold? | Open (G1) |

### 1.3 Evidence-class discipline

| Evidence Class | Requirement | Status |
|---|---|---|
| **Mechanical fact** | Claims about invariant existence, DEC structure, mechanical primitives | Must be clearly labeled |
| **Designer ruling** | Claims about DEC content, locked constraints, evidence-class vocabulary | Must cite DEC IDs |
| **Recommendation** | Candidate shape options, design proposals, open forks | Must be marked as such |

---

## 2. Dependency chain

### 2.1 Precedence order (locked)

1. **DEC-133.A R3** — seven consuming mechanics remain open as Position-tier Effects
2. **DEC-147** — Movement Distance ephemerality lock
3. **DEC-148** — Position-tier substrate clarification
4. **DEC-023.A** — Position-tier Effect selection framework
5. **DEC-013** — S-1 opposed contest primitive
6. **DEC-006/007** — Core Test Transaction (Cost, Overflow, Failure XP)
7. **DEC-024/030** — One Effect per win, no graded outcomes
8. **DEC-095** — Movement as free/bundled side-activity

### 2.2 Content dependencies (open)

- **DEC-122/123/124/126/131** — Condition stack for Pin/Hold
- **DEC-132.A R1** — Movement-trigger reaction category
- **DEC-107** — Effect Tier = causing Skill-Tier
- **DEC-041** — Location Index generation (Skill-Tier ≥ 2 gate)
- **DEC-130** — GM Fiat universality (bounded)

---

## 3. DEC+line links (Select-String numbering)

Based on the decision register analysis, the following DEC IDs contain relevant content for G5:

- **DEC-023.A** — line 219 (S-3 Gated-Tier Effect Content Enumeration)
- **DEC-024** — line 220 (S-3 Effect purchasing / multiplicity)
- **DEC-024.A** — line 221 (closure of second-Effect mechanism)
- **DEC-013** — line 37 (S-1 Opposed Contest)
- **DEC-079** — line 106 (Encumbrance Model) + line 107 (Conditions subsystem)
- **DEC-082.A R2** — line 111 (Equipment state model closure)
- **DEC-095** — line 127 (Combat sequencing / initiative)
- **DEC-133.A R3** — line 170 (G5 Movement confirmation)
- **DEC-148** — line 194 (G5 clarification)

**Note:** Line numbers are based on Select-String counting; Get-Content undercounts. All DEC+line links should be verified by reading the decision register with Select-String.

---

## 4. Governance preamble (verbatim from fusion synthesis)

> You are producing non-canonical advisory material only. Per this project's `governance/status-model.md` and the LLM Governance Rules, your output goes into `investigations/` or `proposals/`, is never Canonical, and must not silently resolve an open designer fork. Cite existing DEC IDs from `decision-register.md` where relevant. State your evidence class (mechanical fact / empirical finding / designer ruling / recommendation) for each claim.

---

## 5. Evidence-class per claim rule

Every substantive claim in the candidate draft must be explicitly labeled with one of the following evidence classes:

- **Mechanical fact** — describes invariant existence, DEC structure, or mechanical primitives
- **Designer ruling** — cites DEC IDs, locked constraints, or evidence-class vocabulary
- **Recommendation** — presents candidate shape options, design proposals, or open forks
- **Empirical finding** — reports findings from verification, assessment, or independent review

---

## 6. Designer question list (unresolved forks — NOT resolved by this spec card)

The following open designer questions must be ruled by Tiwa at gate G1 before any candidate can be promoted:

1. **Disengage shape** — D-A (contested gate), D-B (free + reaction), or hybrid (contest only vs reaction-Tag holders)?
2. **Zone of Control shape** — Z-A (cost-overlay), Z-B (pure reaction), or Z-C (gated contest)?
3. **Chase shape** — K-A (binary band steps) or K-B (margin-accumulation)?
4. **Forced Movement magnitude** — F-A (Tier-scaled), F-B (fixed 1 hex), or F-C (MS-referenced)?
5. **Pin/Hold vector** — P-A (full Condition) or P-B (lightweight mark)?
6. **Seize/Deny shape** — G-A (denial-field), G-B (seize+displace), or G-C (unified)?
7. **Fork C (consumption)** — C1 (full allowance), C2 (travelled-only), or C3 (cost-only)?
8. **Fork G (generic contest skills)** — framework-fixed lineages or pure content-authoring?
9. **Fork T (extra Skill-Tier gate)** — yes or no?
10. **ZoC ↔ Seize/Deny relationship** — exclusive, layered, or soft/hard versions?
11. **Default Skill families** for movement contests (Disengage, Chase, M-0)?
12. **Duration defaults** for ground claims and pins?

**Note:** The 14 mechanics questions from the verification chain reports (big-pickle §3.3) remain agenda material and are not resolved by this spec card.

---

## 7. Storage and provenance

- **Location:** `proposals/tiwas-g5-seven-consuming-mechanics-spec-card-p0-2026-09-19.md`
- **Status:** Proposal (non-canonical advisory)
- **Provenance:** opencode/big-pickle (author), no assessor, last-modified by opencode/muse-spark-1.3-contributor-free
- **Authority:** Non-canonical advisory material only; no DEC inferred; no authority-changing action authorized
- **Note:** This spec card is a proposal for the G5 seven-consuming-mechanics section; it establishes the locked constraints and open questions for drafter agents. No DEC is inferred; all authority remains with the designer gate (G1) and formal promotion process (G2).