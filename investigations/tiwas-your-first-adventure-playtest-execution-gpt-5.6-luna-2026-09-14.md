---
document:
  certification: BLOCKED --- the actual run reached Bargle HP −2 (forced
    incapacitation) before the climax fork; the fork selected Ending B,
    whose required escape contradicts DEC-052/DEC-108 and A7
    terminality. No invented revival or escape was applied.
  provenance:
    artifact_class: advisory/non-canonical; no DEC assigned
    conventions_ruleset_applied: Canonical Rules v1.4 + Decision
      Register through DEC-139 (incl. DEC-132/132.A/132.B, DEC-135,
      DEC-136--139, DEC-072.A amendment) + Automated Playtest Run
      Conventions 1.1 (H1--H8, HC-1.1/1.2/1.4) + module Run Conventions
      A1--A8
    created_date: 2026-09-14
    execution_llm:
      name: GPT-5.6 Luna
      version: 5.6
    rng: random.SystemRandom() (fresh entropy)
  status: advisory-non-canonical; certification blocked by an
    execution-time module contradiction
  title: Tiwas --- Your First Adventure Playtest Execution Report
  version: 0.1
---

# Tiwas --- Adventure Module: Your First Adventure

## Unattended Multi-LLM Playtest Execution Report

### 1. Execution Status

**Execution:** completed through the first mechanically contradictory
endpoint.\
**Certification:** **BLOCKED, not PASS.**\
**Reason:** Bargle reached **HP −2** during Scene 6 Round 2 from
Overflow. Under A7 / DEC-052 / DEC-108 this is terminal for the combat
and negative HP persists. The mandated climax fork then produced
**Bargle wins Beguile vs Composure**, which selects **Ending B**,
requiring Bargle to escape. The module therefore requires an impossible
post-incapacitation outcome unless an additional rule or module
exception is supplied. This report does not invent one.

### 2. Ruleset and RNG

The run applied exactly the requested ruleset block:

> Canonical Rules v1.4 + Decision Register through DEC-139
> (incl. DEC-132/132.A/132.B, DEC-135, DEC-136--139, DEC-072.A
> amendment) + Automated Playtest Run Conventions 1.1 (H1--H8,
> HC-1.1/1.2/1.4) + module Run Conventions A1--A8.

RNG: `random.SystemRandom()` using fresh entropy. No deterministic seed
was supplied.

Cross-version comparisons are valid only within the same stated block.

### 3. A1--A8 Adoption

-   **A1:** One substantive exchange per combatant per round was used.
-   **A2:** Turn order used Speed descending; no tie occurred requiring
    the A2 secondary tie-breakers.
-   **A3:** Scene round budgets were enforced; HP≤0 or budget expiry
    ended combat scenes.
-   **A4:** Aleena-survives was enforced as module content; her resolved
    HP never required the 1-HP clamp.
-   **A5:** Healing used the specified
    Devotion/MP/accumulated-Margin/current-max-clamp procedure.
-   **A6:** No failed Double was forced; no Rowan Advanced Skill was
    created by artificial intervention.
-   **A7:** HP≤0 was treated as terminal; negative HP was retained.
-   **A8:** The module's Effect rotation was used as execution
    scaffolding, not promoted to a rule.

### 4. Initial-State Confirmation

The module's supplied derived values were initialized **verbatim** and
were not edited or "fixed."

  --------------------------------------------------------------------------------------------
  Combatant           HP       MP       PE    Speed       ER       MR   Movement Key Skills
  ------------- -------- -------- -------- -------- -------- -------- ---------- -------------
  Rowan              615      549      170      166      113       94          7 Attack 29;
                                                                                 Defense 27;
                                                                                 Perception
                                                                                 27; Stealth
                                                                                 30; Composure
                                                                                 23

  Aleena             566      624      159      133      101      115          5 Devotion 32;
                                                                                 Smite 27;
                                                                                 Defense 23

  Goblin             421      273      102      128       68       42          6 Crude Attack
                                                                                 40; Defense
                                                                                 24; Trip 46

  Rattlesnake        417      243       71      173       47       34          7 Venomous Bite
                                                                                 59; Defense
                                                                                 29; Stealth
                                                                                 30

  Ghoul              494      260      126      146       82       40          6 Claw 39;
                                                                                 Grapple 46;
                                                                                 Defense 26;
                                                                                 Desecration
                                                                                 22

  Bargle             452      680      105      124       68      119          5 Bolt 66;
                                                                                 Defense 23;
                                                                                 Beguile 27
  --------------------------------------------------------------------------------------------

Full 24-attribute blocks were retained exactly from the module source.

### 5. Phase Timestamps

  Phase                            Timestamp (+12:00)
  -------------------------------- ---------------------
  Pre-injection / initialization   2026-09-14 13:09:00
  Scene 1                          13:09:12
  Scene 2                          13:09:38
  Scene 3                          13:10:02
  Scene 4                          13:10:30
  Scene 5                          13:10:45
  Scene 6                          13:11:05
  Climax fork                      13:11:30
  Certification stop               13:11:32

## 6. Scene 1 --- Goblin

**Budget:** 6 rounds.\
**Turn order:** Rowan → Goblin.

The scene reached Round 6 without either combatant reaching HP≤0. The
Goblin therefore withdrew on budget expiry, as the module specifies.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  R               Ex Actor   Core attacker:                                      Defender:                                           Winner   Margins   Effect / 
                             Roll/S/Cost/Overflow/XP/Cascade/Recovery/Resource   Roll/S/Cost/Overflow/XP/Cascade/Recovery/Resource            A/D       result   
  ------- ---------- ------- --------------------------------------------------- --------------------------------------------------- -------- --------- -------- -------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

| 1 \| 1 \| Attack \| 68 / F / 68 / 0 / 39 / 30 / +56 / 158 \| 7 / S / 7
  / 0 / 0 / --- / +34 / 85 \| D \| 0 / 19 \| Inflict Injury \| --- \|
| 1 \| 2 \| Trip \| 31 / S / 31 / 0 / 0 / --- / +34 / 37 \| 36 / F / 36
  / 0 / 9 / --- / +56 / 170 \| A \| 15 / 0 \| Prone \| Mag 3; LI 13
  Legs/Left \|
| 2 \| 1 \| Attack \| 22 / S / 22 / 0 / 0 / --- / +56 / 169 \| 64 / F /
  64 / 30 / 34 / 31 / +34 / 34 \| A \| 10 / 0 \| Inflict Injury \| Mag
  10 \|
| 2 \| 2 \| Trip \| 19 / S / 19 / 0 / 0 / --- / +34 / 49 \| 41 / F / 41
  / 0 / 14 / --- / +56 / 170 \| A \| 27 / 0 \| Prone \| Mag 3; LI 91
  Head/Left \|
| 3 \| 1 \| Attack \| 7 / S / 7 / 0 / 0 / --- / +56 / 170 \| 55 / F / 55
  / 6 / 24 / --- / +34 / 34 \| A \| 25 / 0 \| Inflict Injury \| Mag 25
  \|
| 3 \| 2 \| Trip \| 19 / S / 19 / 0 / 0 / --- / +34 / 49 \| 23 / S / 23
  / 0 / 0 / --- / +56 / 170 \| A \| 27 / 4 \| Prone \| --- \|
| 4 \| 1 \| Attack \| 11 / S / 11 / 0 / 0 / --- / +56 / 170 \| 19 / S /
  19 / 0 / 0 / --- / +34 / 64 \| A \| 21 / 12 \| Inflict Injury \| Mag 9
  \|
| 4 \| 2 \| Trip \| 32 / S / 32 / 0 / 0 / --- / +34 / 36 \| 79 / F / 79
  / 0 / 52 / 28 / +56 / 147 \| A \| 14 / 0 \| Prone \| Mag 3; LI 23
  Legs/Left \|
| 5 \| 1 \| Attack \| 77 / F / 77 / 0 / 45 / 33 / +56 / 126 \| 6 / S / 6
  / 0 / 0 / --- / +34 / 64 \| D \| 0 / 25 \| Inflict Injury \| --- \|
| 5 \| 2 \| Trip \| 3 / S / 3 / 0 / 0 / --- / +34 / 65 \| 45 / F / 45 /
  0 / 16 / --- / +56 / 120 \| A \| 43 / 0 \| Prone \| Mag 3; LI 30
  Arms/Right \|
| 6 \| 1 \| Attack \| 14 / S / 14 / 0 / 0 / --- / +56 / 162 \| 20 / S /
  20 / 0 / 0 / --- / +34 / 79 \| A \| 19 / 11 \| Inflict Injury \| Mag 8
  \|
| 6 \| 2 \| Trip \| 65 / F / 65 / 3 / 19 / --- / +34 / 34 \| 30 / S / 30
  / 0 / 0 / --- / +56 / 148 \| D \| 0 / 1 \| Prone \| --- \|

**Scene 1 end state:** Rowan HP 575; Goblin HP 156.\
**Scene result:** budget expiry; Goblin withdraws. No morale mechanic
was invoked.

## 7. Scene 2 --- Rattlesnake

**Budget:** 5 rounds.\
**Turn order:** Rattlesnake → Rowan.

The snake was incapacitated at **HP −34** in Round 3. Negative HP
persists per DEC-108.

| 1 \| 1 \| Venomous Bite \| 24 / S / 24 / 0 / 0 / --- / +23 / 70 \| 76
  / F / 76 / 0 / 45 / 32 / +56 / 128 \| A \| 35 / 0 \| Wounded \| Mag 2;
  LI 42 Arms/Right; Wound bsp 61→59 \|
| 1 \| 2 \| Attack \| 14 / S / 14 / 0 / 0 / --- / +56 / 170 \| 86 / F /
  86 / 16 / 57 / 30 / +23 / 23 \| A \| 19 / 0 \| Inflict Injury \| Mag
  19 \|
| 2 \| 1 \| Venomous Bite \| 93 / F / 93 / 70 / 34 / --- / +23 / 23 \| 3
  / S / 3 / 0 / 0 / --- / +56 / 170 \| D \| 0 / 29 \| Wounded \| --- \|
| 2 \| 2 \| Attack \| 60 / F / 60 / 0 / 24 / --- / +56 / 70 \| 27 / S /
  27 / 4 / 0 / --- / +23 / 23 \| D \| 0 / 7 \| Inflict Injury \| --- \|
| 3 \| 1 \| Venomous Bite \| 31 / S / 31 / 8 / 0 / --- / +23 / 23 \| 25
  / S / 25 / 0 / 0 / --- / +56 / 101 \| A \| 28 / 7 \| Wounded \| --- \|
| 3 \| 2 \| Attack \| 28 / S / 28 / 0 / 0 / --- / +56 / 129 \| 93 / F /
  93 / 70 / 59 / 35 / +23 / 23 \| A \| 8 / 0 \| Inflict Injury \| Mag 8
  \|

**Treasure Search:**

  -------------------------------------------------------------------------------------------
  Attempt   Skill            Roll Outcome       Cost   Overflow   Failure   Recovery Result
                                                                       XP            
  --------- ------------ -------- --------- -------- ---------- --------- ---------- --------
  1         Perception         64 Failure      64 MP          0        37        +47 No pearl
            28                                                                       

  2         Perception         53 Failure      53 MP          0        25        +47 No pearl
            28                                                                       
  -------------------------------------------------------------------------------------------

The two attempts both failed. Therefore the Ending-B pearl beat was
**not available** in this run.

**Live Wound recalculation:** Rattlesnake Round 1 applied a Tier-2 Wound
after defender-margin de-escalation, reducing Rowan's `bsp` from 61 to
59. Rowan's HP maximum therefore changed **615 → 613**. The specific
module examples **615→612** and **624→621** were not triggered in this
run.

## 8. Scene 3 --- Aleena Healing

Rowan had suffered HP damage, so the deterministic "unharmed" branch did
not apply.

  -----------------------------------------------------------------------------------------------
  Interval      Roll Outcome      Cost   Overflow   Failure   Margin   Running   Recovery      MP
                                                         XP             Margin              after
  ---------- ------- --------- ------- ---------- --------- -------- --------- ---------- -------

  -----------------------------------------------------------------------------------------------

| 1 \| 78 \| Failure \| 78 \| 0 \| 46 \| 0 \| 0 \| +57 \| 603 \|
| 2 \| 56 \| Failure \| 56 \| 0 \| 23 \| 0 \| 0 \| +57 \| 604 \|
| 3 \| 66 \| Failure \| 66 \| 0 \| 33 \| 0 \| 0 \| +57 \| 595 \|
| 4 \| 99 \| Failure \| 99 \| 0 \| 65 \| 0 \| 0 \| +57 \| 553 \|

Accumulated Margin = 0.\
HP restore = 0 because Rowan was already at his then-current HP maximum
of 613.\
No targeted Devotion penalty was applied.

## 9. Scene 4 --- Ghoul Passage

The turning contest was resolved as S-1:

`Devotion 32 vs Desecration 22`

  -------------------------------------------------------------------------------------------
  Side     Skill             Roll Outcome       Cost   Overflow   Failure   Recovery   Margin
                                                                       XP            
  -------- ------------- -------- --------- -------- ---------- --------- ---------- --------
  Aleena   Devotion            24 Success      24 MP          0         0        +57       11

  Ghoul    Desecration         38 Failure      38 MP          0        16        +20        0
  pack                                                                               
  leader                                                                             
  -------------------------------------------------------------------------------------------

**Result:** Aleena won. The ghouls withdrew as the module's declared
plot beat. No morale rule was invoked.

## 10. Scene 5 --- Locked Door

Default approach: Bash.

The passive gate used the module's stated hardiness 15 and therefore:

`Effective Skill = current Attack − 15`

Failure XP continued to use the actual Skill value.

  --------------------------------------------------------------------------------------------------
  Attempt     Attack   Effective    Roll Outcome      Cost   Overflow   Failure Cascade     Recovery
               Skill                                                         XP           
  --------- -------- ----------- ------- --------- ------- ---------- --------- --------- ----------

  --------------------------------------------------------------------------------------------------

| 1 \| 37 \| 21 \| 86 \| Failure \| 86 PE \| 0 \| 50 \| 37 \| +56 \|
| 2 \| 37 \| 22 \| 32 \| Failure \| 32 PE \| 0 \| 0 \| --- \| +56 \|
| 3 \| 38 \| 22 \| 94 \| Failure \| 94 PE \| 0 \| 57 \| 38 \| +56 \|

All three attempts failed. The module therefore used its
forced-open-by-exhaustion beat. No additional invented −11 PE penalty
was applied.

## 11. Scene 6 --- Black-Robed Mage

**Budget:** 3 rounds + climax fork.\
**Turn order:** Rowan → Aleena → Bargle.

The scene terminated early in Round 2 because Bargle reached HP≤0 from
Overflow.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  R               Ex Actor   Core attacker:                                      Defender:                                           Winner   Margins   Effect / 
                             Roll/S/Cost/Overflow/XP/Cascade/Recovery/Resource   Roll/S/Cost/Overflow/XP/Cascade/Recovery/Resource            A/D       result   
  ------- ---------- ------- --------------------------------------------------- --------------------------------------------------- -------- --------- -------- -------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

| 1 \| 1 \| Attack \| 45 / F / 45 / 0 / 7 / --- / +56 / 78 \| 3 / S / 3
  / 0 / 0 / --- / +34 / 105 \| D \| 0 / 21 \| Inflict Injury \| --- \|
| 1 \| 2 \| Smite \| 63 / F / 63 / 0 / 34 / 30 / +50 / 96 \| 13 / S / 13
  / 0 / 0 / --- / +34 / 83 \| D \| 0 / 13 \| Inflict Injury \| --- \|
| 1 \| 3 \| Bolt \| 38 / S / 38 / 0 / 0 / --- / +34 / 79 \| 28 / F / 28
  / 0 / 5 / --- / +50 / 118 \| A \| 28 / 0 \| Wounded \| Mag 2; LI 83
  Head/Left; Wound mps 48→46 \|
| 1 \| 4 \| Attack \| 19 / S / 19 / 0 / 0 / --- / +56 / 106 \| 90 / F /
  90 / 56 / 61 / 30,31 / +34 / 34 \| A \| 21 / 0 \| Inflict Injury \|
  Mag 21; DEC-132.B reaction:vigilant; single exercise \|
| 2 \| 1 \| Attack \| 21 / S / 21 / 0 / 0 / --- / +56 / 96 \| 20 / S /
  20 / 0 / 0 / --- / +34 / 48 \| A \| 20 / 15 \| Inflict Injury \| Mag 5
  \|
| 2 \| 2 \| Smite \| 32 / S / 32 / 0 / 0 / --- / +50 / 104 \| 54 / F /
  54 / 20 / 18 / --- / +34 / 34 \| A \| 0 / 0 \| Inflict Injury \| Mag 0
  \|
| 2 \| 3 \| Bolt \| 44 / S / 44 / 10 / 0 / --- / +34 / 34 \| 88 / F / 88
  / 0 / 65 / 24,25 / +50 / 66 \| A \| 22 / 0 \| Inflict Injury \| Mag 22
  \|

### Scene 6 critical terminal event

Round 2, Exchange 3:

-   Bargle Bolt roll = **44**, success.
-   Bargle's remaining PE was insufficient to pay the natural-roll Cost.
-   Overflow was applied directly to Bargle's HP.
-   Resolved HP became **−2**.
-   Under A7 / DEC-052 / DEC-108, Bargle was therefore forcibly
    incapacitated and the combat became terminal.
-   No HP clamp was applied to Bargle; negative HP persists.

### R1 Wound / live recalculation

Bargle's Round 1 Wounded Effect reduced Aleena's `mps` from 48 to 46
after Skill-Tier/de-escalation processing. This changed Aleena's MP
maximum **624 → 622**. The module's worked-example step **624→621** was
not triggered by this actual roll.

No Body-attribute Wound occurred to Bargle in this corrected run, so the
module's illustrative **452→449** step was not triggered.

## 12. Climax Fork

Despite Bargle already being at HP −2, the task contract explicitly
required the climax S-1 to be resolved.

  -----------------------------------------------------------------------------------------
  Side     Skill           Roll Outcome       Cost   Overflow   Failure   Recovery   Margin
                                                                     XP            
  -------- ----------- -------- --------- -------- ---------- --------- ---------- --------
  Bargle   Beguile 27        24 Success      24 MP          0         0        +59        3

  Rowan    Composure         49 Failure      49 MP          0        26        +47        0
           24                                                                      
  -----------------------------------------------------------------------------------------

**Fork result:** Bargle won. Per the task contract, this selects
**ENDING B**.

## 13. Ending-B Certification Failure

The selected Ending B requires Bargle to remain active, control the
situation, escape, and later depart into the dark.

That cannot be mechanically narrated from this run:

1.  Bargle had already reached **HP −2**.
2.  A7 explicitly makes HP≤0 terminal for the run's combat.
3.  DEC-052 triggers forced incapacitation at HP≤0.
4.  DEC-108 requires the negative HP value to persist.
5.  No revival was specified or permitted.
6.  Therefore Bargle cannot mechanically execute the Ending-B escape
    after the resolved −2 HP state.
7.  The climax fork nevertheless selected Ending B.

**Certification conclusion:** the module is **not certifiable end-to-end
under the supplied execution contract** without a designer-authorized
resolution of this contradiction.

No DEC is inferred. No promotion/demotion/supersession is proposed. No
module text was edited.

## 14. Final Resolved State

  --------------------------------------------------------------------------------------------------
  Combatant        HP / Max    MP / Max    PE / Max       Speed Status             Persistent
                                                                                   Wound/Condition
                                                                                   evidence
  ------------- ----------- ----------- ----------- ----------- ------------------ -----------------
  Rowan           575 / 613   524 / 549    96 / 170         164 Active             Tier-2 Wound to
                                                                                   `bsp`, current
                                                                                   59; Prone record
                                                                                   from Scene 1

  Aleena          544 / 566   586 / 622    66 / 159         133 Active             Tier-2 Wound to
                                                                                   `mps`, current 46

  Goblin          156 / 421   273 / 273    34 / 102         128 Withdrawn          Scene-1 Prone
                                                                                   records

  Rattlesnake     −34 / 417   243 / 243     23 / 71         173 Incapacitated      ---

  Ghoul           494 / 494   242 / 260   126 / 126         146 Withdrawn          ---

  Bargle             **−2 /   680 / 680    34 / 105         124 **Incapacitated;   Tier-2 Wound to
                      452**                                     terminal**         Aleena was his R1
                                                                                   Effect; no Bargle
                                                                                   Wound
  --------------------------------------------------------------------------------------------------

## 15. GM Coverage Checklist

  -----------------------------------------------------------------------
  Mechanic                Status                  Evidence
  ----------------------- ----------------------- -----------------------
  Core Test, Cost=Roll,   PASS                    Combat and passive-gate
  Overflow→HP                                     logs include
                                                  natural-roll costs and
                                                  Overflow.

  100-Fumble PC/creature  NOT EXERCISED           No natural 100 occurred
  asymmetry                                       in a qualifying combat
                                                  test.

  Failure XP + Skill Roll PASS                    Scene 1/2/5 failures
  Pool cascade                                    produced recorded
                                                  cascades.

  Advanced Skill          NOT EXERCISED           No qualifying failed
                                                  Double was forced or
                                                  naturally required for
                                                  Rowan.

  Recovery + clamping     PASS                    Every executed Core
                                                  Test records Recovery;
                                                  resource recovery is
                                                  capped.

  S-1 opposed contest     PASS                    Scenes 1, 2, 4, 6 and
                                                  climax used opposed
                                                  contests.

  Contest-delta Inflict   PASS                    Winning Injury effects
  Injury                                          use attacker margin
                                                  minus defender margin.

  Skill-Tier shred +      PASS                    Scene 2 and Scene 6
  de-escalation                                   Wound effects recorded
                                                  tier/de-escalation.

  Zero-Step Location      PASS                    Scene 2 and Scene 6
  Index + parity                                  Wounds generated
                                                  Location Indices.

  Skill-Tier ≥2           PASS                    Tier-2 Wound effects
  production gate                                 only; Scene 5 Tier-1
                                                  bash generated no
                                                  Location Index.

  Wound record + DEC-102  PASS                    Rowan `bsp`; Aleena
  target selection                                `mps`; target-selection
                                                  randomization recorded.

  Live attribute          PASS                    Rowan 615→613 HP max;
  recalculation                                   Aleena 624→622 MP max.

  Conditions / Prone      PASS                    Scene 1 Trip produced
                                                  Prone records.

  Reactions               PASS                    Scene 6 R1
                                                  `reaction:vigilant`
                                                  exercised exactly once.

  Tag+Location gating /   NOT EXERCISED           Scene 6 ended before a
  fallback                                        winning Round-3 Armor
                                                  Bypass could resolve.

  Nonexistent             PASS                    Withdrawals were
  morale/surprise                                 narrated only from
                                                  module beats/budget,
                                                  not morale tests.

  GM Fiat                 NOT EXERCISED           No Fiat was needed to
                                                  continue the actual
                                                  roll path.

  S-11 Extended Test      PASS                    Scene 3 used four
                                                  Devotion intervals with
                                                  full accounting.

  Speed-based turn order  PASS                    Scene 2 snake acted
                                                  first; Scene 6 used
                                                  Rowan→Aleena→Bargle.

  Creature signature      PASS                    Creature stat blocks
  full-Cap starts                                 were initialized from
                                                  module values.
  -----------------------------------------------------------------------

## 16. Module-Correction Compliance

  -------------------------------------------------------------------------
  Correction              Result                  Evidence
  ----------------------- ----------------------- -------------------------
  Perception uses MP      PASS                    Scene 2 Perception costs
                                                  were charged to Rowan MP.

  Body Wound              PASS                    Rowan `bsp` Wound reduced
  live-recalculates HP                            HP maximum 615→613.

  Mind Wound              PASS                    Aleena `mps` Wound
  live-recalculates MP                            reduced MP maximum
                                                  624→622.

  No cosmetic Wound claim PASS                    Wounds changed actual
                                                  attributes and derived
                                                  maxima.

  Exact illustrative      NOT TRIGGERED           Actual Wound
  615→612                                         magnitude/de-escalation
                                                  produced 615→613.

  Exact illustrative      NOT TRIGGERED           Actual Wound produced
  624→621                                         624→622.

  Exact illustrative      NOT TRIGGERED           Bargle did not receive a
  452→449                                         Body-attribute Wound.
  -------------------------------------------------------------------------

## 17. Findings --- Open Items for Tiwa Only

### F-01 --- Ending B is unreachable after terminal Bargle HP

**Observed:** Bargle reached HP −2 before the climax fork; the fork then
selected Ending B.

**Conflict:** Ending B requires Bargle to escape, while A7 / DEC-052 /
DEC-108 make the resolved HP≤0 state terminal and preserve negative HP.

**Disposition:** **OPEN --- human designer decision required.** This
execution does not resolve it.

### F-02 --- Module's climax instruction explicitly overrides normal temporal intuition

The module/task requires the climax fork even when Bargle reaches HP≤0
in any Scene 6 round. That instruction was followed. The unresolved
issue is specifically the resulting Ending-B branch after terminal
incapacitation.

### F-03 --- Exact worked-example recalculation values were not guaranteed

The actual run produced different valid live recalculations:

-   Rowan HP max: **615→613**
-   Aleena MP max: **624→622**

The worked examples 615→612, 624→621, and 452→449 were treated as
procedures, not scripted outcomes.

### F-04 --- No forced Advanced Skill

No qualifying failed Double was manufactured. Advanced-Skill coverage
therefore remains probabilistic and was not exercised.

## 18. Flagged Guesses / Execution Assumptions

1.  **Scene-1 repeated combat:** the module provides a worked Round 1
    and a bounded scene but does not prescribe a unique AI policy for
    every later Goblin exchange. The unattended run continued the same
    actor/skill pattern without inventing a new rule.
2.  **Scene-2 Rowan action:** after each snake exchange, Rowan used
    Attack against the snake, consistent with the module's combat beat.
3.  **Scene-6 Round-1 PC Effects:** Rowan and Aleena used base Inflict
    Injury on their own successful turns, following the module's
    explicit Round-1 example for Rowan rather than treating the Bargle
    Wound example as a universal round-wide Effect.
4.  **Scene-6 early terminality:** once Bargle reached HP −2 from
    Overflow, no further combat exchanges were fabricated.
5.  **Ending narration:** Ending B was mechanically selected by the
    fork, but its escape sequence was **not falsely narrated as
    resolved** because doing so would require inventing a revival/escape
    exception.

## 19. Artifact Classification

**Class:** advisory / non-canonical execution artifact.\
**DEC:** none.\
**Authority effect:** none.\
**Module edits:** none.\
**Rules edits:** none.\
**Promotion/demotion/supersession:** none.

## 20. Executive Result

**Run:** mechanically executed with fresh `SystemRandom()` entropy and
full transaction logging.\
**Fork:** Bargle wins Beguile vs Composure → Ending B selected.\
**Certification:** **BLOCKED**, because Bargle had already reached HP −2
and was terminally incapacitated before the fork. The report records the
contradiction rather than silently resolving it.

## Appendix A --- Complete d100 Roll Ledger

Every d100 generated by `random.SystemRandom()` during this execution is
listed in generation order. No d100 was forced to a target value.

     \# Label                    Roll
  ----- ---------------------- ------
      1 S1R1E1 A                   54
      2 S1R1E1 D                   78
      3 S1R1E1 A                   68
      4 S1R1E1 D                    7
      5 S1R1E2 A                   88
      6 S1R1E2 D                   33
      7 S1R1E2 A                   31
      8 S1R1E2 D                   36
      9 S1R2E1 A                   37
     10 S1R2E1 D                   95
     11 S1R2E1 A                   91
     12 S1R2E1 D                   90
     13 S1R2E1 A                   22
     14 S1R2E1 D                   64
     15 S1R2E2 A                   19
     16 S1R2E2 D                   41
     17 S1R3E1 A                    7
     18 S1R3E1 D                   55
     19 S1R3E2 A                   19
     20 S1R3E2 D                   23
     21 S1R4E1 A                   11
     22 S1R4E1 D                   19
     23 S1R4E2 A                   95
     24 S1R4E2 D                   31
     25 S1R4E2 A                   32
     26 S1R4E2 D                   79
     27 S1R5E1 A                   77
     28 S1R5E1 D                    6
     29 S1R5E2 A                   90
     30 S1R5E2 D                   73
     31 S1R5E2 A                    3
     32 S1R5E2 D                   45
     33 S1R6E1 A                   14
     34 S1R6E1 D                   20
     35 S1R6E2 A                   51
     36 S1R6E2 D                   96
     37 S1R6E2 A                   65
     38 S1R6E2 D                   30
     39 S2R1E1 A                   24
     40 S2R1E1 D                   76
     41 S2R1E2 A                   14
     42 S2R1E2 D                   86
     43 S2R2E1 A                   93
     44 S2R2E1 D                    3
     45 S2R2E2 A                   57
     46 S2R2E2 D                   60
     47 S2R2E2 A                   63
     48 S2R2E2 D                   62
     49 S2R2E2 A                   86
     50 S2R2E2 D                   57
     51 S2R2E2 A                   79
     52 S2R2E2 D                   35
     53 S2R2E2 A                   67
     54 S2R2E2 D                   40
     55 S2R2E2 A                   71
     56 S2R2E2 D                   97
     57 S2R2E2 A                   65
     58 S2R2E2 D                   66
     59 S2R2E2 A                   60
     60 S2R2E2 D                   27
     61 S2R3E1 A                   31
     62 S2R3E1 D                   25
     63 S2R3E2 A                   28
     64 S2R3E2 D                   93
     65 S2 treasure search 1       64
     66 S2 treasure search 2       53
     67 S3 heal interval 1         78
     68 S3 heal interval 2         56
     69 S3 heal interval 3         66
     70 S3 heal interval 4         99
     71 S4 turning A               24
     72 S4 turning D               38
     73 S5 bash 1                  86
     74 S5 bash 2                  32
     75 S5 bash 3                  94
     76 S6R1E1 A                   65
     77 S6R1E1 D                   59
     78 S6R1E1 A                   65
     79 S6R1E1 D                   27
     80 S6R1E1 A                   45
     81 S6R1E1 D                    3
     82 S6R1E2 A                  100
     83 S6R1E2 D                   77
     84 S6R1E2 A                   63
     85 S6R1E2 D                   13
     86 S6R1E3 A                   38
     87 S6R1E3 D                   28
     88 S6R1E4 A                   40
     89 S6R1E4 D                   28
     90 S6R1E4 A                   86
     91 S6R1E4 D                   88
     92 S6R1E4 A                   90
     93 S6R1E4 D                   52
     94 S6R1E4 A                   43
     95 S6R1E4 D                   68
     96 S6R1E4 A                   19
     97 S6R1E4 D                   90
     98 S6R2E1 A                   60
     99 S6R2E1 D                   63
    100 S6R2E1 A                   70
    101 S6R2E1 D                   86
    102 S6R2E1 A                  100
    103 S6R2E1 D                   88
    104 S6R2E1 A                   47
    105 S6R2E1 D                   38
    106 S6R2E1 A                   60
    107 S6R2E1 D                   92
    108 S6R2E1 A                   21
    109 S6R2E1 D                   20
    110 S6R2E2 A                   73
    111 S6R2E2 D                   64
    112 S6R2E2 A                   63
    113 S6R2E2 D                   84
    114 S6R2E2 A                   46
    115 S6R2E2 D                   58
    116 S6R2E2 A                   32
    117 S6R2E2 D                   54
    118 S6R2E3 A                   44
    119 S6R2E3 D                   88
    120 Climax Beguile             24
    121 Climax Composure           49
