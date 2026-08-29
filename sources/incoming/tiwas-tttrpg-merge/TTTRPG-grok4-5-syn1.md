# Tiwas Design Direction — Comparative Synthesis

## My Analysis vs PerplexityAI’s Findings

Purpose: Merge both audits into one decision-ready brief.  
Sources:

* A \= my prior Tiwas work (Phase One–Two math audit \+ Reserved Subsystems Direction Brief)  
* P \= PerplexityAI’s comparative lean-toward document

No new full ruleset is proposed here. This is a synthesis of agreements, divergences, and a single recommended path.

---

# 1\. Executive Comparison

| Dimension | My Analysis (A) | Perplexity (P) | Synthesis |
| ----- | ----- | ----- | ----- |
| Core identity | Costly d100 tests; failure teaches; doubles branch skills; PE/MP → Overflow-HP; permanent 1% fumble | Same identity, stated more philosophically | Full agreement |
| Primary references | Mythras / BRP / GURPS discipline | Mythras / BRP / GURPS | Full agreement |
| Negative references | D\&D HP escalation, fixed spell lists, Fate currency | Same three | Full agreement |
| Opposed model preference | Blackjack ranked \#1; margin \#2 | Margin (Skill − Roll) preferred | Real conflict — must resolve |
| Combat philosophy | State-change \+ wounds; Special Effects as optional module | State-change via 8–12 Outcome Effects as central | Agree on philosophy; disagree on centrality/weight |
| Hit locations | Strongly recommended (units digit free channel) | Explicitly avoid full Mythras hit locations | Conflict — see §4 |
| Damage / HP role | Two-track: HP \= fatigue/collapse; location wounds \= injury/death | HP as survival reserve; Energy/MP first line; avoid HP sponge | Compatible if HP is not the kill track |
| Magic | Advanced Skills \+ effect grammar \+ MP \+ overflow backlash | Same structure | Full agreement |
| Architecture | Core / universal modules / setting modules | Nearly identical stack | Full agreement |
| Failure must have stakes | Stakes gate as hard rule (Pain Pump control) | Failure productive but never consequence-free | Full agreement |
| Depth of math | Quantitative (ceilings, exploit rates, steady-state drain) | Mostly qualitative with good mechanical intuition | A supplies numbers; P supplies design rhetoric — merge both |

Bottom line: P and A describe the same game. They diverge on one architectural fork (how opposed quality is measured) and one simulation fork (how granular injury is). Everything else can be unified cleanly.

---

# 2\. Where Both Analyses Strongly Agree

These are no longer open design questions unless the human designer rejects them.

## 2.1 Identity Statement (joint)

*Tiwas should be a high-consequence percentile universal RPG where every attempt costs something, every failure teaches something, and every major success changes the situation.*

P’s wording is excellent and should be retained as the north-star sentence. A’s audits prove that identity is already latent in v2 math.

## 2.2 Lean-Toward / Lean-Away Table (merged)

| Priority | Lean toward | Learn | Do not copy |
| ----: | ----- | ----- | ----- |
| 1 | Mythras | Opposed exchanges → tactical consequences, not mere HP subtraction | Full combat-style skill tree, long Special Effect catalogue as default mandatory menu |
| 2 | BRP | Clear opposed procedure; outcome quality before fiction translation | 1/5 special-success thresholds, resistance table as mandatory chassis |
| 3 | GURPS | Universal core \+ optional modules \+ setting packages; fatigue matters | Point-buy sprawl, huge skill lists, per-item microstats, lookup-heavy play |
| — | Avoid D\&D 5e | — | Abstract HP sponge, short-rest pacing, class chassis |
| — | Avoid fixed-list magic | — | Spell lists as universal default |
| — | Avoid Fate-primary | — | Narrative currency as main resolution/advancement |

## 2.3 Shared Structural Conclusions

1. Combat must be an opposed contest of control/injury, not attack roll → damage roll.  
2. Success quality must matter (both propose a quality channel; they disagree which).  
3. Resources stay central — PE/MP are identity, not chrome.  
4. Advanced Skills are the universal specialisation language (martial, social, magical, technical).  
5. Setting modules add permissions/content, not a second math engine.  
6. Failure XP without stakes is an exploit; adjudication must make failure costly in fiction.  
7. Magic \= skills \+ defined effects \+ MP \+ risk/overflow \+ failure consequences.  
8. Modularity is mandatory for universal/generic scope.

Confidence in joint agreement set: High.

---

# 3\. The Central Divergence — Opposed Quality Model

This is the only disagreement that rewrites downstream math.

## 3.1 Positions

|  | Perplexity (P) | My Analysis (A) |
| ----- | ----- | ----- |
| Preferred measure | Margin \= Skill − Roll (higher margin wins) | Blackjack: among successful rolls, higher roll wins |
| Why | Low successful rolls \= efficient *and* high quality; “most Tiwas-native triad”; respects skill and roll | High rolls already cost more; making them also win fuses exertion with victory; Speed tie-break uses existing stat; simpler comparison |
| Claimed triad | Skill→chance; Roll→cost; Skill−Roll→quality | Skill→chance; Roll→cost and quality; margin optional for damage |

## 3.2 Mathematical Contrast (same example P used)

Scout Skill 65 rolls 22; Guard Skill 50 rolls 47\. Both succeed.

| Model | Winner | Why | Resource story |
| ----- | ----- | ----- | ----- |
| P Margin | Scout (+43 vs \+3) | Lower roll \= more controlled success | Scout spent 22, won big — efficient mastery |
| A Blackjack | Guard (47 \> 22\) | Higher successful effort wins | Guard spent 47, won — costly commitment beats cheap caution |
| Hybrid (see below) | Depends on rule | e.g. compare rolls, break ties with margin/skill | Tunable |

## 3.3 Compatibility With Tiwas Invariants

| Invariant | Margin (P) | Blackjack (A) |
| ----- | ----- | ----- |
| Cost \= natural die (no roll mods) | ✓ | ✓ |
| Doubles read from natural die | ✓ | ✓ |
| High roll \= expensive | True, but high roll hurts quality | True, and high roll helps win |
| Skill \>99 needs a job | Natural — bigger Skill directly grows margin | Needs Mastery Surplus patch (Skill−99 → quality/damage) |
| Failure XP / fumble unchanged | ✓ | ✓ |
| Extra arithmetic | One subtraction per side | One comparison; damage may still subtract |

## 3.4 Design Tension (honest)

* Margin makes skilled characters win *cheaply*. That matches “mastery looks effortless,” and redeems unbounded Skill (§8.3) without a patch. It weakens the drama that expensive rolls are “going for it.”  
* Blackjack makes expensive rolls the way you dominate exchanges. That matches exertion-as-identity and the fiction of committing hard under pressure. It needs help for Skill \>99 and can feel swingy when a barely-skilled high roll beats a masterful low roll.

P is right that margin is elegant.  
A is right that blackjack is the only model where paying more buys a better contested result without new currencies.

## 3.5 Synthesized Recommendation — **Hybrid “Committed Margin” (default proposal)**

Do not pick pure P or pure A without simulation. Implement this hybrid as the primary candidate:

### Opposed resolution (proposed direction)

1. Both sides roll d100 under the normal v2 procedure (cost, fumble, recovery, XP rules unchanged).  
2. A side that fails loses to any side that succeeds.  
3. If both succeed, compare Committed Result:

text

Committed \= Roll \+ Mastery

Mastery   \= max(0, Skill − 99\)     // 0 for all normal characters

Highest Committed wins. Ties → Speed, then higher Skill.  
4\. Effect magnitude / damage basis:

text

Quality \= WinnerCommitted − LoserCommitted   // if loser succeeded

        \= WinnerCommitted                    // if loser failed (cap later in tuning)

or, alternatively for softer lethality:

text

Quality \= WinnerMargin \= WinnerSkill − WinnerRoll

Designer must pick one Quality formula in simulation (Decision S-1).

### Why this hybrid

| Goal | How hybrid serves it |
| ----- | ----- |
| P’s “quality matters” | Explicit Quality number drives effects/damage |
| A’s “cost buys power in contests” | Higher successful roll wins |
| I-4 Skill \>99 | Mastery term redeems unbounded advancement |
| I-1 no roll modification | Die face untouched; Mastery is skill-side |
| Universal contests | Same rule for stealth, debate, melee, hacking |
| Failures stay expensive fiction | Failed high rolls still drain PE/MP and can overflow |

### Simulation matrix required before lock-in

| Matchup | Pure Margin | Pure Blackjack | Hybrid Committed |
| ----- | ----- | ----- | ----- |
| 30 vs 30 |  |  |  |
| 50 vs 50 |  |  |  |
| 70 vs 50 |  |  |  |
| 99 vs 60 |  |  |  |
| 150 vs 99 |  |  |  |
| PE drained per exchange |  |  |  |
| Win rate vs skill gap |  |  |  |

Confidence: High that a hybrid or a simulated choice is needed; Medium on exact hybrid formula.

---

# 4\. Second Divergence — Hit Locations & Injury Granularity

## 4.1 Positions

|  | Perplexity (P) | My Analysis (A) |
| ----- | ----- | ----- |
| Hit locations | Lean away from Mythras full location detail | Lean into locations via units digit of winning roll (free channel) |
| Injury model | Implied: consequences \+ conditions \+ HP as reserve | Explicit two-track: HP collapse track \+ location wound track |
| Priority frame | Tactical state-change first | Human brief priorities: granular simulation \+ low permanent death \+ few steps |

## 4.2 Reconciliation

P’s warning is about Mythras load (separate location rolls, large effect lists, combat-style sprawl).  
A’s proposal was specifically not full Mythras: location from a digit already rolled, \~10 slots, thresholds, no extra die.

Those are compatible if framed as tiers of detail:

| Tier | Model | When |
| ----: | ----- | ----- |
| 0 | No locations; Quality → HP/conditions only | Narrative / mook / social-only games |
| 1 (default recommended) | Optional location via units digit; Serious/Major thresholds; HP ≠ death | Standard Tiwas simulation mode |
| 2 | Full location armor, crippling, surgery trees | Optional “gritty module” |

Synthesis:

* Adopt P’s caution: do not make Mythras-grade location bookkeeping mandatory.  
* Adopt A’s insight: HP math forces something other than pure global attrition (mean HP \~600 vs per-hit scale ≤ \~100).  
* Default \= Tier-1 lightweight locations \+ two-track damage, module-flagged so cinematic games can stay at tier-0.

### Two-track model retained (A), restated in P’s language

* Energy/MP \= first endurance line (agree with P).  
* HP \= survival reserve / collapse buffer from Overflow \+ residual trauma (agree with P’s “not a sponge”).  
* Wounds/conditions \= what actually changes the fight and threatens death (agree with P’s consequence combat).  
* Death from vital Major outcomes \+ failed tests, not from HP→0 (A detail; P leaves open — recommend A).

Confidence: High on two-track \+ modular locations; Medium on exact threshold formulas.

---

# 5\. Combat Consequences — Merging Mythras Lessons

Both want successes to change state. Difference is packaging.

|  | P | A | Synthesis |
| ----- | ----- | ----- | ----- |
| Menu size | 8–12 universal Outcome Effects | Special Effects mainly on success doubles (unused design space) \+ wound states | Core: 8–10 effects; trigger by Quality bands and/or success doubles |
| Always-on menu each hit? | Implied yes | Optional to save steps | Default: 1 free effect on win; extra effect on success-double or high Quality |
| Examples | disarm, pin, force move, break guard, impose condition, resource drain… | choose location, bleed, stun, trip… | Shared short list; weapons/settings gate availability (P’s best idea) |

### Recommended compact Effect list (universal)

1. Inflict Injury (apply Quality to wound/HP track)  
2. Impose Condition (staggered, prone, impaired…)  
3. Disarm / Break Hold  
4. Force Movement / Seize Position  
5. Seize Tempo (advantage on next contest)  
6. Guard Break (reduce defence options next action)  
7. Bleed / Ongoing Drain (Track A or condition)  
8. Open Retreat / Compel Yield check  
9. Damage Equipment (optional tag)  
10. Choose Location (if locations module on)

Weapons, powers, and genres enable subsets — GURPS modularity \+ Mythras consequences without catalogue bloat.

Cross-check: Effects must not modify the historical die face; they apply after resolution (I-1 safe).

---

# 6\. Resources, Exhaustion, and Why P’s Intuition Needs A’s Numbers

P correctly notes:

text

Higher roll ⇒ higher cost

Higher roll ⇒ more likely failure

A quantified the operational consequence under v2 recovery:

text

Long-run HP drain/test ≈ max(0, 50.5 − floor(Regen/2))

≈ 0 for \~half of characters at average Regen

### Joint implication (critical synthesis)

P says resources must stay strategically central.  
A shows per-test recovery makes long-run PE attrition weak.

Therefore both are only true if combat ends via wounds, conditions, and decision pressure, not via running out of PE. PE remains a burst/tactical constraint (multiple defences per round, declined parries, magic spikes), not the campaign clock.

Design rule to lock:

*Fights are decided by Outcome Effects and wound states. Resources shape options per round, not win by empty pool alone.*

Also retain A’s exploit warning (Pain Pump): P’s “failure never consequence-free” becomes the stakes gate rule, not advice.

---

# 7\. Magic, Advancement, Architecture — Unified Model

No material disagreement. Consolidated:

text

TIWAS CORE ENGINE (v2, locked)  
├─ d100 roll-under \+ 100-Fumble  
├─ 24-attribute matrix, live derived stats  
├─ PE / MP, Overflow → HP  
├─ Failure XP, temp Skill Roll Pool, Cap ceiling  
├─ General XP, unbounded attr/skill  
└─ Advanced Skills on failed doubles

UNIVERSAL PLAY MODULES  
├─ Difficulty (skill-side grades only; never edit die)  
├─ Task adjudication \+ stakes gate  
├─ Opposed contests (hybrid pending sim)  
├─ Outcome Effects (8–10)  
├─ Time / turns / action economy  
├─ Conditions  
├─ Two-track damage, healing, Rest  
├─ Equipment traits (flat adders \+ tags)  
├─ NPC compression  
└─ GM pacing / XP award bands

SETTING MODULES  
├─ Fantasy / SF / Modern / Horror / Historical / Cinematic

└─ Each opens effect tags, creatures, tech, and which lineages count as “powers”

Magic default:  
Advanced Skill \+ effect definition \+ MP cost (die) \+ opposed resist when needed \+ overflow backlash \+ failure XP/epiphany  
Spell lists optional as *setting curricula*, never core chassis.

---

# 8\. Comparative Shortlist — Final Lean Table

| Rank | Direction | Source weight | Notes |
| ----: | ----- | ----- | ----- |
| 1 | Consequence-first opposed combat (Mythras philosophy) | P+A | Shared |
| 2 | Single generic contest procedure for all genres (BRP clarity) | P+A | Shared |
| 3 | Quality measure: simulate Margin vs Blackjack vs Hybrid; default Hybrid Committed | Split → synthesized | Top open mechanical decision |
| 4 | Modular universal architecture (GURPS discipline, low load) | P+A | Shared |
| 5 | Lightweight optional hit locations \+ two-track injury | A primary, P-compatible as modular | Default on for “simulation-grade” mode |
| 6 | Short Outcome Effect menu gated by weapon/setting | P primary, A compatible | Default on |
| 7 | Advanced Skill as universal specialisation/magic language | P+A | Shared |
| 8 | Stakes-gated tests as exploit control | A quantified, P principled | Hard rule |
| — | Avoid D\&D HP/rest chassis | P+A | Shared |
| — | Avoid fixed-class magic default | P+A | Shared |
| — | Avoid Fate as primary engine | P+A | Shared |

---

# 9\. What Each Document Contributed That the Other Lacked

## From Perplexity (adopt into canon language)

* Clean identity sentence and priority list for non-math readers.  
* Strong argument that near-fail high rolls must mean something in fiction (overextend, crisis, not “whiff”).  
* Margin triad framing (even if not adopted pure, Quality must be first-class).  
* Explicit negative examples table (D\&D / spell lists / Fate).  
* Emphasis on 8–12 effect menu over full Mythras catalogue.  
* Reminder that BRP special-success thresholds are optional, not sacred.

## From My Analysis (retain as engineering constraints)

* Invariants I-1…I-6 (especially do not modify the die).  
* Natural advancement ceiling min(Cap,51) and two-phase progression.  
* Pain Pump magnitude (\~48 General XP/test at low cap).  
* Steady-state recovery math → PE cannot be sole combat clock.  
* HP scale argument → global HP cannot be primary kill track.  
* Success-double as unused channel for excellence effects.  
* Mastery Surplus need if blackjack-like models win.  
* Concrete implementation sequence \+ regression suite requirement.  
* NPC compression and encounter benchmark approach.

---

# 10\. Unified Design Priorities (replace both lists)

1. One opposed contest primitive for combat and non-combat.  
2. Quality is first-class and drives injury magnitude and/or Outcome Effects.  
3. Every test keeps v2 cost, fumble, recovery, XP order — combat is not a second engine.  
4. State change \> raw attrition; short Effect menu mandatory.  
5. Two-track harm: resources/HP collapse vs wounds/conditions death path.  
6. Locations optional module, lightweight if on (digit mapping, not extra dice).  
7. Advanced Skills express techniques, professions, and powers.  
8. Difficulty only on Skill side; stakes gate controls farming.  
9. Setting modules grant content/permissions only.  
10. Simulate before locking Quality formula, lethality thresholds, and XP-vs-grade interaction.

---

# 11\. Open Decisions After Synthesis

| ID | Decision | P’s lean | A’s lean | Synthesized default to simulate first |
| ----- | ----- | ----- | ----- | ----- |
| S-1 | Opposed quality measure | Margin | Blackjack | Hybrid Committed \+ Quality from differential |
| S-2 | Hit locations default on/off | Off / avoid full | On lightweight | On as default in simulation-grade rules; off-switch for cinematic |
| S-3 | Effect triggers | Common on wins | Prefer success-double gating | 1 effect on win; \+1 on success double or high Quality band |
| S-4 | HP \= 0 | Unspecified | Collapse, not death | Collapse / incapacitation |
| S-5 | Death path | Unspecified | Major vital \+ tests | Keep A |
| S-6 | Failure XP under difficulty grades | Not covered | True vs effective skill fork | Still must simulate (A’s D-8) |
| S-7 | Declining defence allowed? | Implicit in resource tactics | Yes | Yes |
| S-8 | Mastery above 99 | Automatic if pure margin | Needs surplus if blackjack | Hybrid includes Mastery term |

---

# 12\. Recommended Next Implementation Order (joint)

1. Freeze v2 invariants and stakes-gate wording.  
2. Code three opposed models (Margin, Blackjack, Hybrid) \+ PE drain \+ win rates.  
3. Pick S-1 from data, not taste.  
4. Attach 8–10 Outcome Effects \+ Quality→Injury mapping.  
5. Add two-track harm; tune so PE empty ≠ auto-loss and HP sponge ≠ win condition.  
6. Add optional locations as module; verify step count still low.  
7. Difficulty grades \+ D-8/S-6 XP interaction test.  
8. Magic grammar as Mind-rooted Advanced Skills \+ same opposed primitive.  
9. NPC grades \+ encounter curves from the same simulator.  
10. Rest/healing parameters last.

Every step re-runs core regressions: natural skill terminus, fumble floor, Pain Pump throughput, overflow steady-state.

---

# 13\. Final Synthesis Judgment

Perplexity and I are aligned on what Tiwas is and what it must not become.

Perplexity is strongest on design philosophy, modularity rhetoric, and consequence-first combat language.  
I am strongest on engine invariants, quantitative exploits, and injury architecture forced by the math.

The only hard fork is how to measure contested success quality.  
Treat that as an empirical choice between:

* pure Margin (P),  
* pure Blackjack (A),  
* Hybrid Committed (recommended synthesis default).

Everything else collapses into one stack:

BRP-clear contests \+ Mythras-style consequences (small menu) \+ GURPS modularity (low load) \+ Tiwas-native cost/failure/epiphany engine \+ two-track harm with optional lightweight locations.

That is the lean.  
