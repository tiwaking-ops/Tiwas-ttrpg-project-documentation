---
document:
  title: "Standardized Melee-Exchange Algorithm Design Ruling (OI-103)"
  version: "1.0"
  status: "Advisory recording of a designer ruling. Non-canonical. Assigns DEC-105 in the decision register."
provenance:
  author_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
  ruling_origin: "Human designer (Tiwa), in-session ruling, 2026-09-05, resolving open item OI-103 (v4 Cross-Report Synthesis 2026-09-05)"
  recorded_in: "_consolidation/decision-register.md DEC-105"
---

# Standardized Melee-Exchange Algorithm Design Ruling (OI-103)

## 1. Purpose

This document records Tiwa's designer ruling resolving **OI-103** — the standardized
melee-exchange algorithm. OI-103 was raised by the v4 Ice Troll Combat Playtest Cross-Report
Synthesis (2026-09-05, §6.2 / §10) because **no single DEC spells out the full combined
melee-exchange algorithm**: Claude Sonnet 5 explicitly reconstructed one (its §14
methodology note) and flagged it for human confirmation; Grok 4.5 implemented a
similar-but-not-identical version; GPT-5.6 Luna never reached the exchange (it aborted at the
Wound branch, OI-101/102).

The ruling was given in-session and is recorded in §3 and §4. It is recorded here as the
auditable source for the corresponding decision-register entry (**DEC-105**).

**Authority status:** This is a non-canonical designer ruling. It does not itself make
anything Canonical. Any promotion to Canonical would require the full 8-step Promotion Rule
(REQ-021 / Proposals/WIP §21).

## 2. Open item resolved

| ID | Issue | Source |
|---|---|---|
| OI-103 | Standardized melee-exchange algorithm (confirm/correct Claude's reconstruction) | v4 Cross-Report Synthesis (2026-09-05) §6.2, §10; Claude v4 Final Report §14 methodology note |

## 3. The ruling — verbatim (Tiwa, 2026-09-05)

> On Claude's step 1–2 (attacker-fail ends the exchange; defender rolls only on attacker
> success), Tiwa repeatedly corrected: **"I thought attacks were a contest?"** — the
> exchange is a single S-1 opposed contest in which **both participants always roll** and
> the DEC-013 outcome matrix decides. This supersedes Claude's gated construction.
>
> On potential rule items 4–5 (Effect-tier eligibility; Wound/Condition channel), Tiwa
> confirmed the existing rulings apply: base `Effect Tier Y Magnitude Y` with Y = Attack
> Skill Tier (OI-102 / DEC-103), and the Wound/Condition mitigation channel (DEC-103) is
> already resolved.
>
> On item 6 (mitigation on a lost defense): **"Resolved."** — under the contest model,
> mitigation arises only in the Both-Success row (defense succeeded AND attack landed).
>
> On item 7 (additional Effects): **"If there is a second Effect then it is contested, third
> Effect? Contested. But only if an Active Defense is selected by the Defender."**
>
> On declined Active Defense:
>
> > "For playtests defense is Mandatory. In real life play it would be rare for a player to
> > refuse an Active Defense roll, but it may be possible that the enemies are simply too
> > weak to either hit or affect them and actively defending may cause Overflow damage due
> > to lack of Energy Pool."
>
> And on what the attacker gets when defense is declined:
>
> > "Attacker gets a normal Core Skill Test. This is why a defender may decline as the
> > attackers Skill Level may be very low or its weapons too weak to cause any lasting
> > damage."

## 4. Clarifications — verbatim (Tiwa, 2026-09-05)

None beyond §3. All matters raised for OI-103 were answered in-session as recorded above.

## 5. Structured restatement (for execution)

### 5.1 The exchange IS one S-1 opposed contest

Both participants make their own Core Tests **always** — there is no defender roll once
the attacker succeeds (that was Claude's §14 error, now superseded). The defender's roll
is their Active Defense Core Test (DEC-044); it is simultaneously their S-1 "other
participant" roll (nested in the exchange per DEC-095).

### 5.2 Outcome matrix (DEC-013 §13.1 as applied to combat)

| Attacker roll | Defender roll | Result |
|---|---|---|
| Success | Failure | **Attacker wins** — Effect at the attacker's full Quality; mitigation 0 (DEC-097) |
| Failure | Success | **Defender wins** — attack fails entirely; no Effect, no counter-Effect (DEC-101) |
| Success | Success | Compare Quality (Margin, DEC-013 §13.2/13.3): higher wins; exact tie → repeat (§13.5) |
| Failure | Failure | Repeat contest (§13.4) |

### 5.3 Effect-channel split on an attacker win (Both-Success row, attacker Margin higher)

- **Inflict Injury (HP):** damage = Winner's Margin − Defender's Margin (contest-delta,
  DEC-104 = DEC-096 composed with DEC-097).
- **Wound/Condition Effect:** DEC-103 full machinery — Skill-Tier comparison shred
  (Atk=Def → Mag −1; Def>Atk → Mag − difference; Atk>Def → Mag +1), then margin
  de-escalation with the carry rule; survivor records natively (Z = −Y, DEC-035.A/DEC-079).
  **Wound Effects do not themselves remove HP** — HP loss comes only from Inflict Injury
  (DEC-104) and Overflow (DEC-007).

### 5.4 Effect-tier eligibility

Eligibility (Base vs gated, DEC-099: Quality ≥ 1 / ≥ 10) is judged on the **winner's raw,
pre-mitigation Quality** (DEC-031: Quality is computed at the winner's own successful
roll), not the defense-reduced net.

### 5.5 Overflow

Overflow (DEC-007) is independent of the exchange outcome and always lands on the roller's
own HP, on both the attacker's and the defender's individual Core Tests.

### 5.6 Voluntary vs mandatory defense

- **Playtests: defense is MANDATORY** — the defender always rolls their Active Defense
  Core Test.
- **Live play: defense is VOLUNTARY.** Refusal is rare but legitimate when the attacker's
  Skill Level is very low or its weapons too weak to cause lasting damage, or when
  defending risks self-Overflow from an empty Energy Pool.
- **Declined defense: the attacker gets a normal Core Skill Test only** — no contest, no
  margin comparison, no mitigation. (An unopposed attack does not auto-succeed.)

### 5.7 Additional (second and further) Effects

Any Effect beyond the single free one per win (DEC-024) requires its own **separate opposed
roll** (DEC-026: different Advanced Skill), each with its **own independent Active Defense
roll** (DEC-049) — second, third, etc., all contested identically, and only if the Defender
selects an Active Defense in each case (DEC-050: voluntary).

## 6. Register entry

Recorded in `_consolidation/decision-register.md` (Section B, Non-canonical designer
ruling):

| ID | Subject | Status |
|---|---|---|
| DEC-105 | Standardized melee-exchange algorithm (resolves OI-103) | Ruled (non-canonical) |

## 7. Status

**Status:** Advisory recording — not canonical
**Authority:** Non-canonical designer ruling (real decision; promotion requires the
8-step Promotion Rule)
**Assigns:** DEC-105 (next sequential ID after DEC-104)
**Resolves:** OI-103 (standardized melee-exchange algorithm)
**Supersedes for general play:** Claude v4 Final Report §14's gated exchange construction
(attacker-fail ends exchange; defender rolls only on attacker success) — the DEC-013 contest
model governs.
**Leaves open:** OI-104 (DEC-101 coverage — a matched or forced case to exercise
defender-wins), OI-105 (SC-XX action selection), OI-106 (Quality → Wound Tier table context),
OI-107 (HP floor convention)
**Canonical rule change:** None