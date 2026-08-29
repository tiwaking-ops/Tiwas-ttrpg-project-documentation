---
document:
  title: "Tiwas S-3: Effect Identity & Multi-Effect Opposition — Investigation (Closed)"
  version: "v0.1-closed"
  status: "Non-canonical investigation thread — status Closed; all items ruled 2026-08-29. No item herein is a Tiwas rule."
provenance:
  author_llm: {name: "opencode", version: "big-pickle"}
  assessor_llm: {name: "opencode", version: "big-pickle"}
  last_modified_by_llm: {name: "opencode", version: "big-pickle"}
  created_date: "2026-08-29"
  last_modified_date: "2026-08-29"
---

# Tiwas S-3 — Effect Identity & Multi-Effect Opposition: Investigation (Closed)

**Status: CLOSED — all items (Q-S3-2a / DEC-025, Q-S3-2b / DEC-026, Q-S3-5 / DEC-027,
Q-S3-3a / DEC-030) ruled 2026-08-29.**

This was a dedicated non-canonical investigation thread, opened parallel to the S-3
Outcome Effects investigation (and to the earlier S-2 investigations D4/D5). It tracked
the design forks that surfaced from the S-3 discussion, most of which were *not* settled
by the first two S-3 rulings. It compiled the open questions with their evidence classes
and the constraints already Canonical, and did **not** resolve them itself — consistent
with Roadmap §24 Rule 6 (never silently resolve an open designer fork) and REQ-021.
**All four of its open items have since been ruled by the human** (2026-08-29, per the
per-decision handoff reports): Q-S3-3a (DEC-030), Q-S3-5 (DEC-027), Q-S3-2a (DEC-025), and
Q-S3-2b (DEC-026). This thread is now **Closed**; no open forks remain in it.

Cross-reference: the rulings and formerly-open items from this thread are recorded in
`_consolidation/decision-register.md` §D (DEC-025…DEC-030) and, for the ruled S-3 items,
in `proposals/` §3.4 and `investigations/tiwas-s3-outcome-effects-investigation-v0.1-draft.md`.

---

## 1. Context — the S-3 rulings already made on S-3

Before this thread's questions arise, the human has already ruled on four S-3 decisions
(recorded in `_consolidation/decision-register.md` §D, DEC-023, DEC-024, DEC-028,
DEC-029):

- **DEC-023 (Q-S3-1)** — Tiered Effect menu: base tier = **Inflict Injury (HP-only)** +
  **Open Retreat / Compel Yield**; five gated tiers keyed to their owning subsystem's
  lock status. **Disarm / Break Hold tier assignment** was placed via Q-S3-3's combined
  Tag+Location gating and is now **determined** by DEC-030 (its specific tier and
  partial-match behaviour are resolved below).
- **DEC-024 (Q-S3-2)** — **Flat one-Effect-per-win.** No Quality-based scaling, no
  purchasing additional Effects off a single win. A second/additional Effect requires a
  **separate opposed roll** — the mechanism for that roll was deferred to this thread
  (Q-S3-2b) and is now **ruled** (DEC-026).
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

## 2. Design questions — all RULED

### Q-S3-2a — Effect identity / naming gating — **RULED: Pure declared intent (DEC-025)**

**Subject.** Named Effects (Disarm, Bleed, etc.) create a naming-collision risk. Because
**Advanced Skill names carry zero mechanical weight** (Canonical Rules §12.3 — the
resource-domain/advancement identity of an Advanced Skill is independent of its name),
nothing currently stops a player from naming a Skill after an Effect and arguing
entitlement to that Effect.

**Fork considered (see decision-register DEC-025):**
- **(A)** Effects require a **formal tag/category system on Advanced Skills** —
  e.g., an Effect only triggers from a Skill carrying the relevant tag, closing the
  naming-collision.
- **(B)** Effects stay **purely declared intent, with no skill-gating at all** — the
  name does not entitle the player to anything mechanical; the effect follows the
  declared outcome, not the Skill's name.

**RULED (Option B — pure declared intent, human, DEC-025):** Effects are granted solely
by the declared outcome of a successful S-1 contest, subject to the other gates already
ruled (gear/ability Tag + Location Index where required, DEC-028). The Skill name carries
**no mechanical weight** and does not entitle or gate any Effect. A formal tag/category
system on Advanced Skills is **rejected**. Designer rationale: formal tags and category
systems are exploitable and would lead players to limit their Skill choices to only those
carrying degenerate mechanical Effects.

**Consequences:** no Skill-side tags, categories, or Effect-entitlement vocabulary are
introduced; the name holds only fictional weight (reinforcing Canonical §12.3); REQ-017 is
satisfied (no competing classification economy on Skills); the existing DEC-028 gates are
unaffected (Tags remain on gear/ability, not on Skills).

**Note:** the Disarm/Break Hold tier placement does **not** depend on this question; it
depends on Q-S3-3's combined Tag+Location gating (DEC-028) and Q-S3-3a (DEC-030), both of
which are now ruled.

### Q-S3-2b — Second-Effect opposed-roll mechanism — **RULED: Different Advanced Skill; defensive roll deferred (DEC-026)**

**Subject.** Per DEC-024, an additional Effect beyond the free one requires a **separate
opposed roll**. What governs that roll was undecided.

**Fork considered (see decision-register DEC-026):**
- What Skill / check the second roll uses: the **same Skill as the original contest**, a
  **different Skill**, or a **flat check**.
- Whether the target gets any **defensive roll** for the additional Effect, given
  **S-6 Defense is still Open** (Proposals/WIP §6; Roadmap §4 row S-6). Until S-6 is
  locked, a defensive roll cannot rely on a defined Defense system.

**RULED (human, DEC-026):** The separate opposed roll for any Effect beyond the single
free one uses a **different Advanced Skill** that is **domain-appropriate** to the
declared second Effect. The actor accepts the risk of the additional roll. The **full
9-step Core Test Transaction applies** (REQ-018). The target receives **no defensive roll
until S-6 locks**; any provisional resistance used in the interim is **non-canonical
scaffolding only** and must be discarded when S-6 locks. **Same-Skill and flat-check
options are rejected.**

**Consequences:** the multi-Effect path is high-friction — it requires possession of (and
risk to) a second relevant Advanced Skill; resource economy (Cost / Overflow / Failure XP
/ Recovery) applies to the second Skill only; no parallel engine (REQ-018) and no
competing economy (REQ-017) are introduced; Skill-name weight is zero (Canonical §12.3,
"domain-appropriate" is a lineage/domain judgement). Sequencing: the Free Effect resolves
first; the second roll is a separate, subsequent transaction. No residual
Advantage/Margin/state carries from the first contest.

### Q-S3-3a — Partial Tag / Location match behavior — **RULED: Fail-and-fall-back (DEC-030)**

**Subject.** Spun off from the DEC-028 ruling (Q-S3-3): the three in-scope
Tag+Location-gated Effects (Disarm/Break Hold, Equipment Damage, Armor Bypass) require
*both* a matching Tag *and* a supporting Location Index. What happens on a **partial
match** — the Tag is present but the Location Index doesn't support the Effect, or the
Location Index supports it but the Tag is absent?

**Fork considered (see decision-register DEC-030):**
- **(A) Fail-and-fall-back** — the Effect simply fails and falls back to plain damage
  (consistent with the flat one-Effect-per-win ruling: the win's Effect is the declared
  one, and if it can't trigger, only the base damage path remains).
- **(B) Partial/reduced outcome** — some reduced or different effect applies on a
  partial match.

**RULED (Option A, human, post-handoff confirm — DEC-030):** On a partial Tag/Location
match, the declared Effect fails entirely and the successful S-1 contest applies the
Base-tier Effect **Inflict Injury (HP-only form)**. No residual Advantage, magnitude,
duration, or secondary state is generated from the partial match. Designer clarification
extends DEC-024: any further Effect beyond the single free Effect requires a **separate
opposed roll using an appropriate Advanced Skill**, accepting the risk of that additional
roll.

**Consequences:** partial-match behaviour is closed to binary fail/success only; Disarm /
Break Hold's tier is now fully determined (Tag+Location-gated, DEC-028) with its failure
behaviour identical to Equipment Damage and Armor Bypass (fall back to Base Inflict
Injury). Graded/residual Effects are explicitly rejected for S-3 gated Effects.

### Q-S3-5 — Auto-apply vs. contested application — **RULED: Auto-apply (DEC-027)**

**Subject.** When S-1 is won with a declared Effect, does the Effect apply
automatically, or does it itself require passing a further check against the target?

**Fork considered (see decision-register DEC-027):**
- **(A) Auto-apply** — winning S-1 with a declared Effect applies it directly. This is
  the only option **buildable today**, because S-6 Defense is not locked and there is no
  defined resistance mechanic for a contested application.
- **(B) Contested application** — the Effect requires a further check/roll against the
  target before it takes hold. Cannot be fully specified until S-6 (and/or Defensive
  mechanics) is designed.

**RULED (Option A — auto-apply, human, DEC-027):** Winning an S-1 opposed contest with a
declared Effect applies that Effect **directly**; no secondary application contest is
required. Gate checks (Tag + Location Index where required per DEC-028; fail-and-fall-back
per DEC-030) remain in force and are evaluated **once, post-win**.

**Designer clarification:** S-6 (Defense) remains free to introduce Tags or equipment
options that counter or prevent specific Effects after they would otherwise auto-apply
(e.g., locked gauntlets prevent Disarm). Contested application is **rejected as the S-3
default**; any future contested-application mechanic is deferred to **S-6 as an optional
modifier**, not an S-3 default rule.

**Consequences:** the default application path is auto-apply (buildable against the locked
Core + S-1 + Zero-Step); extra resolution steps are none; S-6 extensibility is additive;
REQ-018 is preserved. The one-Effect-per-win path is now fully specified for all currently
unlocked Effects.

### Carried forward — Disarm / Break Hold tier placement — **CLOSED by DEC-030**

From DEC-023 (Q-S3-1) and DEC-028 (Q-S3-3), the Disarm / Break Hold Effect is placed in
the combined Tag+Location-gated category. With Q-S3-3a ruled (DEC-030), its **specific
tier** and **failure behaviour** are now determined and this item is closed: it sits in
the Tag+Location-gated category, and on a partial Tag/Location match its declared Effect
fails and falls back to Base Inflict Injury (HP-only) — identical to Equipment Damage and
Armor Bypass.

---

## 3. Already-Ruled S-3 decisions (reference — not open)

These are recorded for completeness and are not re-opened by this thread. **All eight
S-3 session decisions (DEC-023…DEC-030) are ruled.**

- **DEC-023 — Tiered Effect menu** (base tier: Inflict Injury HP-only, Open
  Retreat/Compel Yield; five gated tiers; Disarm/Break Hold placed via Q-S3-3 gating).
- **DEC-024 — Flat one-Effect-per-win** (no Quality scaling; second effect = new opposed
  roll).
- **DEC-025 — Effect identity / naming** pure declared intent (Option B); Skill name
  never entitles or gates an Effect; formal tag/category system on Advanced Skills
  rejected.
- **DEC-026 — Second-Effect opposed-roll mechanism** different Advanced Skill
  (domain-appropriate), full 9-step Core Test Transaction; no target defensive roll until
  S-6; same-Skill and flat-check rejected.
- **DEC-027 — Effect application** auto-apply; gate checks evaluated once post-win;
  contested application rejected as S-3 default, deferred to S-6 as optional modifier.
- **DEC-028 — Combined Location + Tag gating** for Disarm/Break Hold, Equipment Damage,
  Armor Bypass; Function Impairment and Incapacitation deferred out of S-3.
- **DEC-029 — S-3/S-4 boundary** prototype-only; S-4 direction recorded non-binding.
- **DEC-030 — Partial Tag/Location match** fail-and-fall-back (Option A); partial match
  falls back to Base Inflict Injury (HP-only); further Effects require a separate opposed
  roll using an appropriate Advanced Skill.

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

## 5. Resolution of this thread

All four open items in this thread have been ruled by the human (2026-08-29):
Q-S3-3a (DEC-030), Q-S3-5 (DEC-027), Q-S3-2a (DEC-025), and Q-S3-2b (DEC-026) — see §2
above and `_consolidation/decision-register.md` §D. No pending human rulings remain in
this thread.

The resolved items return to the main S-3 investigation
(`tiwas-s3-outcome-effects-investigation-v0.1-draft.md`) for incorporation into the S-3
proposal and, ultimately, the formal promotion process and any later S-6 revisit of the
deferred defensive half of the second-effect roll.

---

## 6. Known limitations of this thread

- **No simulation or playtest data.** None of these forks has empirical support; they are
  architectural/design questions resolved by designer ruling rather than measurement.
- **S-6 Defense is Open.** Resolved here via deferral: DEC-026 gives the target **no**
  defensive roll until S-6 locks (any interim resistance is non-canonical scaffolding),
  and DEC-027 rejects contested application and defers it to S-6 as an optional modifier.
- **Single-model, single-session analysis.** Authored and assessed by the same LLM
  session; an independent second review is recommended per `governance/provenance.md`.
- **Provenance of underlying S-3 content (Proposals/WIP §3) is not established** per the
  original consolidation.

---

## 7. Status of this document

- Status: **Non-canonical investigation thread — Closed. All four items (Q-S3-3a /
  DEC-030, Q-S3-5 / DEC-027, Q-S3-2a / DEC-025, Q-S3-2b / DEC-026) ruled 2026-08-29.**
- It does **not** alter Canonical Rules.
- It resolves none of these items by its own judgement — each was ruled by the human
  designer and recorded in `_consolidation/decision-register.md` §D and `proposals/` §3.4.
- Placed in `investigations/` as evidentiary/analytical work product feeding the
  Proposals/WIP layer, parallel to the S-2 investigations (D4/D5).
