---
document:
  title: "Hierarchical Location Architecture — Open-Item Designer Options Brief (DEC-042 Secondary Roll & Location Ceiling)"
  version: "1.0"
  status: "Advisory options brief — Non-canonical. Not a ruling. No DEC inferred. Pending Tiwa's in-session ruling; if ruled, OpenCode records the ruling per standing governance before any register text changes."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-09-12"
  last_modified_date: "2026-09-12"
---

# Hierarchical Location Architecture — Open-Item Designer Options Brief

## 0. Governance Notice

This document is an **advisory options brief**, produced at Tiwa's request from the
2026-09-12 session. It:

- identifies and explains two unresolved decision items left open by the adoption of the
  hierarchical Location Address architecture (**DEC-112**, 2026-09-08);
- presents option sets with consequences;
- does **not** rule, assign a DEC, amend the decision register, or change any Canonical
  text.

**Tiwa** holds sole human ruling authority. **OpenCode** records rulings only after
Tiwa's explicit sign-off. None of the options below are operative until Tiwa picks one
and the ruling is formally recorded.

Source material: `investigations/Tiwas TTRPG — Proposed Hierarchical Location
Architecture Report.md` (GPT-5.6 Luna, 2026-09-08, **proposal / not canonical**);
`_consolidation/decision-register.md` (DEC-042, 100, 112, 113, 114, 030, 062, 107);
canonical rules v1.3 §5.1.

## 1. Purpose and Scope

The GPT-5.6 Luna hierarchical-architecture proposal was largely adopted in-session on
2026-09-08 via **DEC-112** (fourteen sub-rulings **L-001–L-014** mirroring the
proposal's §31 decision decomposition). Two items remain genuinely open or internally
contradictory and require a human ruling before the architecture is implementable:

- **Q1 — the DEC-042 secondary location roll**: DEC-112 L-011 removed it, but two later-
  established rulings still route **Armor Bypass** through it.
- **Q2 — the Location Tier ceiling**: the proposal specified a **12-tier architectural
  ceiling**; DEC-112 L-005 reads "**no cap** — Skill-Tier maps directly to Location
  Tier".

Both questions are dormant in effect today (only **Armor Bypass** is Tier-2-eligible,
and no Tier-2+ template or 100-state allocation has been authored yet — DEC-112
L-009/L-010 deferred to content-authoring), but the register cannot be made internally
consistent without resolving Q1, and Q2 decides how the still-unbuilt Tiers 3+ behave.

## 2. Background — What DEC-112 Established (Context, Unchanged Here)

Adopted 2026-09-08 (non-canonical designer ruling; supersedes the earlier flat Level 2–5
menu ruling and the DEC-042 secondary-roll mechanism "for Tier 2+ location resolution"):

- **L-001** hierarchical Location Address model replaces flat cumulative menus.
- **L-002** Location Index provider is the Zero-Step tens/units exchange (unchanged).
- **L-003** single-source deterministic resolution — the d100 Location Index determines
  the full address path; **no secondary roll**.
- **L-004** per-creature-type authored **Location Templates**.
- **L-005** Skill-Tier maps directly to Location Tier; **no cap**.
- **L-006** Location Tier = spatial precision depth (Tier 1 = Head/Torso/Arms/Legs).
- **L-007** parent/child matching (parent covers children; parent Armor covers child
  locations; parent Wound covers child locations).
- **L-009** Human template — deferred to content-authoring.
- **L-010** 100-state numerical allocation — deferred to content-authoring.
- **L-011** secondary roll removed.
- **L-012** Armor location-bound with parent coverage.
- **L-014** on location mismatch, fall back to the coarser parent location.

Chronology relevant to both questions:

| Date | Ruling / input | Content |
|---|---|---|
| 2026-08-31 | **DEC-042** | Tier-2+ subdivision via dedicated **secondary d6/d10 roll** (no cost, not a second Core Test); mismatch → DEC-030. |
| 2026-09-04 | **DEC-100** | Tier-1 quartiles: 1–25 Legs, 26–50 Torso, 51–75 Arms, 76–100 Head. |
| 2026-09-06 | **DEC-113** | Per-Effect tier assignment. **Armor Bypass is the only Tier-2 Effect, "resolved via the DEC-042 secondary roll"**; preserves "DEC-042 procedure (now exercised by Armor Bypass only)". |
| 2026-09-06 | **DEC-114** | Tag-trigger table. Armor Bypass: "location match evaluated at DEC-112 sub-zone level **via the DEC-042 secondary roll**". |
| 2026-09-08 | **Proposal stored** | GPT-5.6 Luna proposal (non-canonical; no DEC inferred; register rows for DEC-041/042/100/113 bracketed "formal human decision required before any amendment or supersession"). |
| 2026-09-08 | **DEC-112** | Hierarchical architecture adopted; **L-011 removes the DEC-042 secondary roll**; preserves DEC-113 "per-Effect tier assignment" without reconciling its secondary-roll clause. |

---

## 3. Q1 — Armor Bypass and the DEC-042 Secondary Roll

### 3.1 Evidence

- **DEC-042 (2026-08-31)** — Tier-2+ subdivision is resolved by a dedicated **secondary
  roll** (e.g. d10/d6), separate from the Zero-Step-derived number; no Energy/MP cost;
  explicitly not a second Core Test; location-mismatch falls back per **DEC-030**
  (fail-and-fall-back to Base `Inflict Injury`, HP-only).
- **DEC-113 R2 (2026-09-06)** — Armor Bypass is the only Tier-2 Effect, resolved "via
  the DEC-042 secondary roll". Tier-1 Effects (Wound, Trip, Disarm/Break Hold, Equipment
  Damage) use the DEC-100 quartile ranges with **no** secondary roll.
- **DEC-114 R2 (2026-09-06)** — Armor Bypass trigger: `defense:armor`/`defense:shield`
  at the struck sub-location; "location match evaluated at DEC-112 sub-zone level via
  the DEC-042 secondary roll".
- **DEC-112 L-011 (2026-09-08)** — "**Secondary roll: removed** — DEC-042 secondary
  location roll is superseded by the single-source deterministic address resolution."

### 3.2 The contradiction

| Statement | Source |
|---|---|
| "Secondary roll: removed — DEC-042 secondary location roll is superseded by the single-source deterministic address resolution" | DEC-112 L-011 (2026-09-08) |
| Armor Bypass = Tier-2-eligible, "resolved via the DEC-042 secondary roll" | DEC-113 R2 (2026-09-06) |
| "DEC-042 procedure (now exercised by Armor Bypass only)" preserved | DEC-113 Preserves clause (2026-09-06) |
| Armor Bypass "location match evaluated at DEC-112 sub-zone level via the DEC-042 secondary roll" | DEC-114 R2 (2026-09-06) |

DEC-112 explicitly **preserves** DEC-113 ("per-Effect tier assignment") while **removing**
the mechanism that DEC-113 R2's Armor Bypass tier depends on. Either DEC-113 R2/DEC-114 R2
need amending to drop the DEC-042 reference, or DEC-112 L-011 needs amending to leave the
roll in place for Armor Bypass. The register currently says both things and cannot be
applied unambiguously. (The register's own 2026-09-08 brackets on DEC-042 require a
formal human decision before supersession — so this is Tiwa's call, not something an LLM
may silently resolve; REQ-022.)

### 3.3 Operational reality (why this matters now)

- DEC-112 L-010 (100-state allocation) and L-009 (Human template) are **deferred to
  content-authoring** — they do **not exist yet**.
- Consequently, **no deterministic Tier-2 address table currently exists** against which
  Armor Bypass can resolve under the single-source model. The proposal's stated pipeline
  (`Index → Template → Address`) is unimplementable at Tier 2 until that content is
  authored.
- The **only** existing, ruled mechanism for resolving Armor Bypass below a coarse zone
  is the DEC-042 secondary roll. A literal, immediate application of L-011 would leave
  Armor Bypass with **no resolvable Tier-2 path** — it would fall back to coarse Tier 1
  (the PC downgrade gate in DEC-113 R3), which contradicts R2's intent that a creature's
  promoted Armor Bypass "always resolves at Tier 2" (DEC-113 R4).
- **Invariant 18** (no parallel resolution engine) is preserved under every option — the
  DEC-042 roll was already scoped as "explicitly not a second Core Test".

### 3.4 Options

**Option A — Pure single-source (strict DEC-112).** Armor Bypass resolves at Tier 2
through the deterministic Location Index / template address only; the DEC-042 secondary
roll is removed for all Effects, including Armor Bypass.
- Register edits required: amend DEC-113 R2 (strike "resolved via the DEC-042 secondary
  roll") and DEC-114 R2 (strike "via the DEC-042 secondary roll"); clarify DEC-113 R3's
  PC-downgrade rationale (its "drops the DEC-042 secondary roll and thereby the DEC-030
  location-mismatch risk" justification loses its subject matter).
- Consequences: cleanest single-source architecture; but **Armor Bypass at Tier 2 is not
  actually resolvable today** (no template/allocation), so the ruling is latent until
  L-009/L-010 content exists; in the interim Armor Bypass resolves at Tier 1 (coarse) —
  effectively making Tier-2 Armor Bypass a State-2 "anchored but not yet resolvable"
  classification in the DEC-019/§14.7 sense.

**Option B — Keep the DEC-042 secondary roll for Armor Bypass only.** Reverse part of
L-011: the secondary roll is removed for Tier-1 Effects but retained as the Armor Bypass
Tier-2 sub-resolution mechanism (matching DEC-113/114 as written).
- Register edits required: amend DEC-112 L-011 to scope the removal to non-Armor-Bypass
  (Tier-1) resolution or to "until the 100-state allocation exists"; keep DEC-113/114
  unchanged.
- Consequences: immediately operational Armor Bypass at Tier 2; preserves the DEC-030
  mismatch-fallback path; retains the proposal's single-source model as the long-term
  target, with the secondary roll as an interim provider — conceptually parallel to the
  existing "interim content" precedents. Cost: the architecture is temporarily dual-
  mechanism (deterministic for coarse, secondary roll for Armor Bypass detail).

**Option C — Latency hold (State-2 classification).** Armor Bypass remains Tier-2-
eligible per DEC-113 R2, but with no authored Tier-2 address content it resolves at
Tier 1 coarse **until** the L-010 allocation / L-009 template are authored; the DEC-042
secondary roll is removed now (Option A's removal) and nothing replaces it until the
content lands. No secondary roll and no deterministic Tier-2 table in the interim.
- Register edits required: add an interim-resolution annotation to DEC-113 R2/R4 (Tier-2
  Armor Bypass "anchored, not yet resolvable" while allocation is unauthored); amend
  DEC-114 R2's "via the DEC-042 secondary roll" to "pending 100-state allocation".
- Consequences: mirrors the DEC-019 State-2 precedent instead of inventing an interim
  roll; puts the entire Tier-2 pathway behind the same content dependency as everything
  else in the hierarchy. Matches the practical drift of the current playtests, which have
  exercised only coarse-zone location records so far.

### 3.5 Decision for Tiwa

> Which treatment of the DEC-042 secondary roll for **Armor Bypass** should the register
> reflect: **(A)** removed entirely — deterministic-only, latent until allocation exists;
> **(B)** retained as the interim Tier-2 Armor Bypass mechanism until the 100-state
> allocation/template are authored; or **(C)** removed now and Tier-2 Armor Bypass held
> as "anchored, not yet resolvable" until content lands?

---

## 4. Q2 — Location Tier Ceiling: 12 vs "No Cap"

### 4.1 Evidence

- **Proposal §6.2 / §28 / LOC-I15** — `L_max = min(S, 12)`: Skill-Tier maps to maximum
  Location Tier subject to an **architectural ceiling of 12** ("Terminal substructure").
  Rationale (§28): a fixed engine boundary, predictable content-authoring requirements,
  controlled maximum complexity — not a claim that real anatomy has exactly twelve
  layers. The proposal's semantic ladder (§7) defines Tiers 1–12 and stops there.
- **DEC-112 L-005** — "**no cap** — Skill-Tier maps directly to Location Tier (higher
  Skill-Tier = deeper resolution)".
- **Canonical §5.1** — Skill-Tier = number of distinct attributes in the Cap formula;
  "The theoretical maximum Tier is therefore **24**."
- Prior flat architecture capped resolution at **Level 5** (old DEC-112; "no granularity
  above Level 5 is currently reachable").

### 4.2 The ambiguity

L-005's "no cap" was written against the old flat **Level-5** ceiling (removing it), but
read literally it also declines the proposal's separate **12-tier** architectural ceiling.
Nothing in DEC-112 mentions 12. Because the canonical Skill-Tier maximum is 24, the two
readings diverge materially for Skills above Tier 12 — which are theoretical but legal.

Practical bounding that reduces the stakes:

- Effective resolution is already bounded per target by **authored depth**:
  `L_actual = min(S, D)` (proposal §6.3). Most creatures will author 3–8 meaningful
  levels; the ceiling mainly constrains hypothetical very-high-resolution templates.
- Only **Armor Bypass** is Tier-2-eligible today; Tiers 3+ are dormant pending content.
- Location **depth ≠ number of states**: a single 100-state Index encodes one
  variable-length path, so deep addresses do not consume extra probability mass —
  the ceiling is an authoring/engine boundary, not a d100-representation constraint.

### 4.3 Options

**Option A — Adopt the explicit 12-tier ceiling (proposal as written).** Location Tier is
capped at 12; Skill-Tiers 13+ simply resolve at Tier 12.
- Register edits: add a ceiling clause to DEC-112 (L-005 or L-006) and adopt
  proposal LOC-I15 ("max architectural Location Tier is 12 unless a future formal
  decision changes it").
- Consequences: fixed engine boundary; bounded content-authoring; the finished 1–12
  semantic ladder is usable as-is; matches the proposal. Minor cost: future-proofing
  requires a formal change if 12 ever binds.

**Option B — Unbounded (literal "no cap").** Location Tier = Skill-Tier, no ceiling.
- Consequences: simplest mapping; requires a semantic ladder beyond Tier 12
  (the proposal defines none — Tier 12 is already "Terminal substructure"), plus
  unbounded authoring expectations; effectively the "no cap" L-005 reading. Since
  authored depth D usually binds first, the practical difference vs Option A is small
  and only shows on exotic high-Tier templates.

**Option C — "No cap" on mapping + content-driven bound (no normative ceiling).**
Location Tier tracks Skill-Tier without a rule ceiling, but effective resolution is
bounded by authored template depth (`L = min(S, D)`), and 12 is adopted as a
**content-authoring convention** (template depth cap target), not a rule.
- Consequences: preserves L-005 wording exactly; avoids inventing a ceiling while
  keeping content bounded by convention; may revisit if a beastie genuinely needs
  Tier 13+. Least register churn; closest to the system's existing "content, not
  engine" philosophy (cf. DEC-110, DEC-133 content-boundary precedents).

### 4.4 Decision for Tiwa

> How should Location Tier scale above the reached tiers: **(A)** a hard architectural
> ceiling of 12 (proposal LOC-I15), **(B)** unbounded Skill-Tier→Location-Tier mapping
> with no ceiling, or **(C)** no rule ceiling, but 12 as a content-authoring depth cap
> (`L = min(S, D)` governs effective resolution)?

---

## 5. Interaction and Sequencing Note

Q1 and Q2 interact through the still-unbuilt L-009/L-010 content:

- Under **Q1 = A/C**, the Tier-2 path is latent until the 100-state allocation is
  authored; under **Q1 = B**, an operational interim mechanism exists today.
- Under **Q2 = A**, Tier 3+ content boundaries are fixed at 12 for all future templates;
  under **B/C** they are open (B globally, C by authoring convention).
- Either way, the proposal's remaining recommendation — the **100-state information-
  capacity / allocation investigation** (§9, §25, LOC-I16) — is the natural next piece
  of design work and is untouched by this brief's two options.

The proposal's separate recommendation to **re-investigate the DEC-100 Tier-1 quartile
ranges** is recorded in the register as unperformed; DEC-112 opted to keep the quartiles
unchanged. That is a third, lower-priority item and is deliberately **not** opened here —
flag for a future content/playtest pass rather than this ruling session.

## 6. Explicit Non-Decisions

This brief does not:

- assign a DEC or alter the decision register;
- promote anything (the hierarchical architecture remains a non-canonical designer
  ruling; any Canonical entry still requires the 8-step Promotion Rule, REQ-021);
- create Location Template content, a 100-state allocation, or Tier-1–12 semantics as
  canonical;
- re-open DEC-100 quartiles, DEC-062, DEC-030, DEC-107, or DEC-014.

If Tiwa rules, the ruling (with chosen option and exact register-amendment set) will be
recorded to `_consolidation/decision-register.md` in a follow-up step after explicit
sign-off, and the affected DEC cells (DEC-112 L-005/L-011; DEC-113 R2/R3/R4; DEC-114 R2)
updated as amendments per the existing amendment-row precedent.