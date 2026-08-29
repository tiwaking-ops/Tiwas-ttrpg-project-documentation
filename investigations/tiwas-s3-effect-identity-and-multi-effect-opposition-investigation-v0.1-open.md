---
document:
  title: "Tiwas S-3: Effect Identity & Multi-Effect Opposition — Investigation (Open)"
  version: "v0.1-open"
  status: "Non-canonical investigation thread — status Open, no rulings yet. No item herein is a Tiwas rule."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
---

# Tiwas S-3 — Effect Identity & Multi-Effect Opposition: Investigation (Open)

**Status: Open — no rulings yet.**

This is a dedicated non-canonical investigation thread, opened parallel to the S-3
Outcome Effects investigation (and to the earlier S-2 investigations D4/D5). It tracks
the design forks that surfaced from the S-3 discussion, most of which were *not* settled
by the first two S-3 rulings (see below). It compiles the open questions with their
evidence classes and the constraints already Canonical, and does **not** resolve any of
them — consistent with Roadmap §24 Rule 6 (never silently resolve an open designer fork)
and REQ-021.

Cross-reference: rulings and open items from this thread are recorded in
`_consolidation/decision-register.md` §D (DEC-025…DEC-030) and, for the ruled S-3 items,
in `proposals/` §3.4 and `investigations/tiwas-s3-outcome-effects-investigation-v0.1-draft.md`.

---

## 1. Context — the S-3 rulings already made on S-3

Before this thread's questions arise, the human has already ruled on four S-3 decisions
(recorded in `_consolidation/decision-register.md` §D, DEC-023, DEC-024, DEC-028,
DEC-029):

- **DEC-023 (Q-S3-1)** — Tiered Effect menu: base tier = **Inflict Injury (HP-only)** +
  **Open Retreat / Compel Yield**; five gated tiers keyed to their owning subsystem's
  lock status. **Disarm / Break Hold tier assignment is still pending**; it is placed
  via Q-S3-3's combined Tag+Location gating, with its specific tier and partial-match
  behaviour depending on Q-S3-3a below.
- **DEC-024 (Q-S3-2)** — **Flat one-Effect-per-win.** No Quality-based scaling, no
  purchasing additional Effects off a single win. A second/additional Effect requires a
  **separate opposed roll** — the mechanism for that roll is not yet designed and is
  deferred to this thread (Q-S3-2b).
- **DEC-028 (Q-S3-3)** — **Combined Location + Tag gating** for the in-scope S-3 Effects
  (**Disarm/Break Hold, Equipment Damage, Armor Bypass**): trigger requires both a
  matching Tag and a supporting Zero-Step Location Index (Tier 1+). **Function Impairment
  and Incapacitation are deferred OUT of S-3 scope** (Incapacitation → S-7; Function
  Impairment → S-4/Condition). This ruling spins off **Q-S3-3a** (below).
- **DEC-029 (Q-S3-4)** — S-3/S-4 boundary confirmed prototype-only; no interface work
  needed yet; the S-4 *direction* is a non-binding steer for a future S-4 investigation.

The effect of DEC-024 is significant: it removes the Proposals/WIP §3.2 purchasing model
(Quality/Net-Advantage bands) as the basis for *multiplicity*. A win yields exactly one
Effect; any further Effect on the same target/objective requires a new opposed roll. This
is the "multi-effect opposition" half of this thread's name.

---

## 2. Open design questions (no rulings yet)

### Q-S3-2a — Effect identity / naming gating

**Subject.** Named Effects (Disarm, Bleed, etc.) create a naming-collision risk. Because
**Advanced Skill names carry zero mechanical weight** (Canonical Rules §12.3 — the
resource-domain/advancement identity of an Advanced Skill is independent of its name),
nothing currently stops a player from naming a Skill after an Effect and arguing
entitlement to that Effect.

**Open fork (designer ruling required):**
- **(A)** Effects require a **formal tag/category system on Advanced Skills** —
  e.g., an Effect only triggers from a Skill carrying the relevant tag, closing the
  naming-collision.
- **(B)** Effects stay **purely declared intent, with no skill-gating at all** — the
  name does not entitle the player to anything mechanical; the effect follows the
  declared outcome, not the Skill's name.

**Evidence class:** Designer ruling (open). Related constraint: canonical §12.3 (Skill
names carry no mechanical weight) and REQ-017 (no competing economy — a tag system must
not become a second progression/advancement currency).

**Note:** the Disarm/Break Hold tier placement does **not** depend on this question; it
depends on Q-S3-3's combined Tag+Location gating (DEC-028) and Q-S3-3a below.

### Q-S3-2b — Second-Effect opposed-roll mechanism

**Subject.** Per DEC-024, an additional Effect beyond the free one requires a **separate
opposed roll**. What governs that roll is undecided.

**Open fork (designer ruling required):**
- What Skill / check the second roll uses: the **same Skill as the original contest**, a
  **different Skill**, or a **flat check**.
- Whether the target gets any **defensive roll** for the additional Effect, given
  **S-6 Defense is still Open** (Proposals/WIP §6; Roadmap §4 row S-6). Until S-6 is
  locked, a defensive roll cannot rely on a defined Defense system.

**Evidence class:** Designer ruling (open). Related constraints: REQ-018 (build on the
Core Test Transaction, not a parallel engine); REQ-017 (no competing economy).

### Q-S3-3a — Partial Tag / Location match behavior

**Subject.** Spun off from the DEC-028 ruling (Q-S3-3): the three in-scope
Tag+Location-gated Effects (Disarm/Break Hold, Equipment Damage, Armor Bypass) require
*both* a matching Tag *and* a supporting Location Index. What happens on a **partial
match** — the Tag is present but the Location Index doesn't support the Effect, or the
Location Index supports it but the Tag is absent?

**Open fork (designer ruling required):**
- **(A) Fail-and-fall-back** — the Effect simply fails and falls back to plain damage
  (consistent with the flat one-Effect-per-win ruling: the win's Effect is the declared
  one, and if it can't trigger, only the base damage path remains).
- **(B) Partial/reduced outcome** — some reduced or different effect applies on a
  partial match.

**Evidence class:** Designer ruling (open). Consistency note: option (A) is the simpler
reading and aligns with DEC-024's flat-one-Effect framing; option (B) introduces a
gradation the current rulings do not otherwise provide. This forks the specific
Disarm/Break Hold tier and failure behaviour.

### Q-S3-5 — Auto-apply vs. contested application

**Subject.** When S-1 is won with a declared Effect, does the Effect apply
automatically, or does it itself require passing a further check against the target?

**Open fork (designer ruling required):**
- **(A) Auto-apply** — winning S-1 with a declared Effect applies it directly. This is
  the only option **buildable today**, because S-6 Defense is not locked and there is no
  defined resistance mechanic for a contested application.
- **(B) Contested application** — the Effect requires a further check/roll against the
  target before it takes hold. Cannot be fully specified until S-6 (and/or Defensive
  mechanics) is designed.

**Evidence class:** Designer ruling (open). Note the current asymmetry: only auto-apply
can be implemented now; contested application would need an S-6 dependency.

### Carried forward — Disarm / Break Hold tier placement

From DEC-023 (Q-S3-1) and DEC-028 (Q-S3-3), the Disarm / Break Hold Effect is placed in
the combined Tag+Location-gated category. Its **specific tier** and its **failure
behaviour** remain pending, depending on how Q-S3-3a (partial Tag/Location match)
resolves. This is tracked here so it is not lost.

---

## 3. Already-Ruled S-3 decisions (reference — not open)

These are recorded for completeness and are not re-opened by this thread:

- **DEC-023 — Tiered Effect menu** (base tier: Inflict Injury HP-only, Open
  Retreat/Compel Yield; five gated tiers; Disarm/Break Hold placed via Q-S3-3 gating).
- **DEC-024 — Flat one-Effect-per-win** (no Quality scaling; second effect = new opposed
  roll).
- **DEC-028 — Combined Location + Tag gating** for Disarm/Break Hold, Equipment Damage,
  Armor Bypass; Function Impairment and Incapacitation deferred out of S-3.
- **DEC-029 — S-3/S-4 boundary** prototype-only; S-4 direction recorded non-binding.

---

## 4. Constraints binding all of the above (Canonical / process)

- **Canonical §13.2 / §12.3** — Quality only compares successful tests; Quality never
  modifies the historical roll/Cost/Failure XP/Double eligibility/Recovery; Advanced
  Skill names carry no mechanical weight.
- **REQ-017** — no competing primary resource or progression economy (a tag system or a
  second-effect mechanism must not become one).
- **REQ-018** — Universal Play modules build on the Core Test Transaction, not a
  parallel resolution engine.
- **REQ-021 / Roadmap §24 Rule 6** — no promotion, and no silent resolution of these
  open forks, without the formal promotion process and designer ruling.
- **REQ-020** — the Roadmap may not independently decide these unresolved designer
  decisions.

---

## 5. Recommended next steps (not performed — require human rulings)

1. **Human ruling on Q-S3-2a** (Effect naming/gating: tag system vs. declared intent).
2. **Human ruling on Q-S3-5** (auto-apply vs. contested application) — auto-apply is the
   only currently-buildable option; contested application depends on S-6.
3. **Human ruling on Q-S3-2b** (second-effect opposed-roll basis: same skill / different
   skill / flat check; and target defensive roll, gated on S-6 being Open).
4. **Human ruling on Q-S3-3a** (partial Tag/Location match: fail-and-fall-back vs.
   partial outcome) — this resolves the carried-forward Disarm/Break Hold tier and
   failure behaviour.
5. Once ruled, the resolved items return to the main S-3 investigation
   (`tiwas-s3-outcome-effects-investigation-v0.1-draft.md`) for incorporation into the
   S-3 proposal and, ultimately, the formal promotion process.

---

## 6. Known limitations of this thread

- **No simulation or playtest data.** None of these forks yet has empirical support; they
  are architectural/design questions pending designer ruling.
- **S-6 Defense is Open.** Both Q-S3-2b (target defensive roll) and Q-S3-5 (contested
  application) are constrained by the absence of a locked Defense subsystem.
- **Single-model, single-session analysis.** Authored and assessed by the same LLM
  session; an independent second review is recommended per `governance/provenance.md`.
- **Provenance of underlying S-3 content (Proposals/WIP §3) is not established** per the
  original consolidation.

---

## 7. Status of this document

- Status: **Non-canonical investigation thread — Open, no rulings yet.**
- It does **not** alter Canonical Rules.
- It does **not** resolve Q-S3-2a, Q-S3-2b, Q-S3-5, or Q-S3-3a, nor the carried-forward
  Disarm / Break Hold tier and failure behaviour.
- Placed in `investigations/` as evidentiary/analytical work product feeding the
  Proposals/WIP layer, parallel to the S-2 investigations (D4/D5).
