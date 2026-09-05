---
document:
  title: "Active Defense Effect Mitigation Design Ruling (OI-102)"
  version: "1.0"
  status: "Advisory recording of a designer ruling. Non-canonical. Assigns DEC-103 in the decision register."
provenance:
  author_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  assessor_llm: []
  last_modified_by_llm: {name: "opencode/big-pickle", version: "opencode/big-pickle"}
  created_date: "2026-09-05"
  last_modified_date: "2026-09-05"
  ruling_origin: "Human designer (Tiwa), in-session ruling, 2026-09-05, resolving open item OI-102 (v4 Cross-Report Synthesis 2026-09-05)"
  recorded_in: "_consolidation/decision-register.md DEC-103 (and DEC-104, same session)"
---

# Active Defense Effect Mitigation Design Ruling (OI-102)

## 1. Purpose

This document records Tiwa's designer ruling resolving **OI-102** — how Active Defense's
Defender's Margin modifies an incoming Effect's Tier/magnitude — raised by the v4 Ice
Troll Combat Playtest Cross-Report Synthesis (2026-09-05; Gap B / Finding F-07) and
first escalated by GPT-5.6 Luna ("does not specify ... how Active Defense's Defender's
Margin modifies a Wound Tier/magnitude").

The ruling was given in-session and is recorded in §3 and §4. It is recorded here as the
auditable source for the corresponding decision-register entry (**DEC-103**) and for the
Inflict Injury contest-delta refinement ruled in the same session (**DEC-104**).

**Authority status:** This is a non-canonical designer ruling. It does not itself make
anything Canonical. Any promotion to Canonical would require the full 8-step Promotion
Rule (REQ-021 / Proposals/WIP §21).

## 2. Open items resolved

| ID | Issue | Source |
|---|---|---|
| OI-102 | How Active Defense's Defender's Margin modifies an Effect (Wound/Condition) Tier/magnitude | v4 Cross-Report Synthesis (2026-09-05) §10 OI-102, Gap B / Finding F-07; GPT-5.6 Luna v4 Finding F-07 |
| — | Inflict Injury HP magnitude missing the Defender's-Margin mitigation (DEC-096 × DEC-097 composition) | Same OI-102 design session; contest-delta resolution |

## 3. The ruling — verbatim (Tiwa, 2026-09-05)

> **Case table (designer's corrected, final version):**
>
> | Case | Shred (initial reduction) |
> |---|---|
> | AtkTier = DefTier | Effect Tier-1 |
> | DefTier > AtkTier | Effect Tier-Difference, Magnitude-Difference |
> | AtkTier > DefTier | Effect Tier-1, Magnitude+1 |
>
> Examples: AtkTier 5 vs DefTier 5 → Effect Tier 4. AtkTier 4 vs DefTier 5 → Effect
> Tier 4, Magnitude 3. AtkTier 5 vs DefTier 4 → Effect Tier 4, Magnitude 5.
>
> **Simplified table (designer's final preference):**
>
> | Case | Transform | Examples |
> |---|---|---|
> | Atk = Def | Magnitude −1 | Atk 5/Def 5 → Tier 5, Mag 4 |
> | Def > Atk | Mag − (Def−Atk), cycling | Atk 4/Def 5 → Tier 4, Mag 3; Atk 3/Def 6 → 3−3=0 → cycle → Tier 2, Mag 2 |
> | Atk > Def | Mag +1 (gap irrelevant) | Atk 5/Def 4 → Tier 5, Mag 6; Atk 6/Def 4 → Tier 6, Mag 7 |
>
> "At first glance this looks really bad for Atk > Def. However, a successful defence
> roll allows anyone to reduce the magnitude of the Effect by the Margin of success. This
> gives an opportunity to negate an Effect, but it is slightly more difficult."
>
> **Carry/floor rule:** "Effect Magnitude Floor is 0 which then reduces Effect Tier by 1
> and then Magnitude = Effect Tier. Effect Tier Floor is Tier 0 which negates."
>
> "Yes it can be instantly negated. This may be a problem. It is only a problem if the
> defender is successful though."
>
> On `Atk 3 / Def 6`: "3-3 = 0. Skill Tier reduces by 1. Becomes Effect Tier 2 Magnitude 2."
>
> On the strong/equal threshold: "Initially I wanted it to be 'greatly reduces', but this
> system works better and is more fair." (Defense advantage pays off from +2 difference
> on; the +1 case equals Atk = Def.)
>
> On Tier-1 attackers: "Tier-1 attackers can only ever land an effect when the defender
> fails the roll. Remember, you choose. The attacker could choose to cause Injury / damage
> instead. If they want to choose an Effect which is immediately negated then that is not
> up to the system to prevent."

## 4. Clarifications — verbatim (Tiwa, 2026-09-05)

> 1. Order: "Yes fully resolves." — the Skill-Tier comparison shred fully resolves first
>    (including its cascades), then the Margin de-escalation cycle runs on the survivor.
> 2. Base values: "Base Y = Attack Skill Tier ... yes approved" for both Effect Tier and
>    Magnitude.
> 3. Defense roll: "Defense roll = Active Defense Skill, roll-under, Margin = Skill −
>    Roll. yes approved. Same system. If Attacker wants to apply an Effect then the
>    opponent can choose to make an Active Defense roll."
> 4. Reading 1: "Reading 1 — Magnitude is only a negation buffer." Reasoning: "Technically
>    it is a strict numerical amount, compounded by Tier. Tier 2 magnitude 2 requires 3
>    margin to negate, but Tier 5 Magnitude 5 requires 15 margin to negate. But this is
>    only for Effect and not damage. Tier denotes the difficulty to remove the Effect.
>    This system has never been mentioned before because I just made it today."
> 5. Inflict Injury resolution: "Contest-delta: damage = Winner's Margin − Defender's
>    Margin. ... This is exactly what Grok converged on in v4, so it has playtest evidence
>    behind it."
> 6. HP channel: "Confirmed" fully separate from the Effect negation table.

## 5. Structured restatement (for execution)

### 5.1 Definitions

- **Base Effect:** applying an Effect yields `Effect Tier Y, Magnitude Y`, where
  `Y = Attack Skill Tier` (Interpretation A; overridable by content-authored Effect/
  weapon tiers per DEC-087/085).
- **Defender choice:** on effect application, the opponent **may** make an Active Defense
  roll (Active Defense Skill, roll-under; Defense Margin = Skill − natural d100, the same
  economy as DEC-096/DEC-097). This supplies the defensive response DEC-024/DEC-026 left
  deferred and S-6-locked via DEC-044 (nested in the S-1 exchange per DEC-095).

### 5.2 Step 1 — Skill-Tier comparison shred (only on a successful Defense roll)

Failed Defense → mitigation 0 (DEC-097 preserved).

| Case | Transform |
|---|---|
| Atk = Def | Magnitude −1 |
| Def > Atk | Magnitude − (DefTier − AtkTier), cascading (advantage pays from +2 on) |
| Atk > Def | Magnitude +1 (gap irrelevant) |

### 5.3 Step 2 — Margin de-escalation

The survivor's Magnitude is reduced by the Defender's Margin. After each carry, remaining
margin continues draining. If the Effect survives to a Defense-Margin-exhausted state at
Tier ≥ 1, the leftover margin is lost (overprotection / luck).

### 5.4 Unified carry rule (single rule for both steps)

- Magnitude floor = 0 → Effect Tier −1 → Magnitude resets to the new Tier.
- Effect Tier floor = Tier 0 → **Effect negated**.
- **Instant negation** is permitted: a successful Defense alone can wholly erase an Effect
  before any margin is spent.

### 5.5 Reading 1 — consequences (Magnitude as negation buffer only)

- Magnitude is a strict numerical amount, compounded by Tier, used **only** as a negation
  buffer for Effects.
- **Tier = difficulty to remove the Effect:** negation cost is triangular in Tier when
  Magnitude = Tier (Y(Y+1)/2: Tier-2/Mag-2 → 3 margin; Tier-5/Mag-5 → 15 margin).
  Applies to **Effects only; never HP damage**.
- A surviving Effect records natively at the surviving tier
  (`Location X Tier-Y <Effect> Z`, Z = −Y; DEC-035.A / DEC-079). Decoupled intermediate
  magnitudes never enter records — **no amendment to DEC-035.A/DEC-079 required**.

### 5.6 Worked examples

| Exchange | Result | Full-negation margin cost |
|---|---|---|
| Atk 5 / Def 5 | Tier 5, Mag 4 | 4+4+3+2+1 = 14 |
| Atk 4 / Def 5 | Tier 4, Mag 3 | 3+3+2+1 = 9 |
| Atk 3 / Def 6 | Tier 2, Mag 2 | 2+1 = 3 |
| Atk 5 / Def 4 | Tier 5, Mag 6 | 6+4+3+2+1 = 16 |
| Atk 6 / Def 4 | Tier 6, Mag 7 | 7+5+4+3+2+1 = 22 |

### 5.7 Inflict Injury (HP) channel — contest-delta

`Inflict Injury` (Base-tier S-3 Effect, DEC-023) removes target HP equal to
**Winner's Margin − Defender's Margin** from the successful S-1 opposed contest. Recorded
as **DEC-104**: a refinement making explicit the composition of DEC-096 (Winner's Margin)
and DEC-097 (Defender's Margin mitigation). Never zero on a win. This channel is fully
separate from the Effect negation table above.

## 6. Register entries

Recorded in `_consolidation/decision-register.md` (Section B, Non-canonical designer
ruling):

| ID | Subject | Status |
|---|---|---|
| DEC-103 | S-4/S-6 Active Defense Effect mitigation — Skill-Tier shred + margin de-escalation (resolves OI-102) | Ruled (non-canonical) |
| DEC-104 | C-01/C-02 refinement — Inflict Injury contest-delta magnitude | Ruled (non-canonical) |

## 7. Status

**Status:** Advisory recording — not canonical
**Authority:** Non-canonical designer ruling (real decision; promotion requires the
8-step Promotion Rule)
**Assigns:** DEC-103 (next sequential ID after DEC-102) and DEC-104 (same session)
**Resolves:** OI-102 (Active Defense vs Effect — Defender's Margin modification of an
Effect Tier/magnitude)
**Leaves open:** OI-103 (exchange algorithm confirmation) remains open
**Canonical rule change:** None