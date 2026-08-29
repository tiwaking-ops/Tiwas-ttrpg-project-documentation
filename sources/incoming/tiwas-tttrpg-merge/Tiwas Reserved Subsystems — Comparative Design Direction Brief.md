# **Tiwas Reserved Subsystems — Comparative Design Direction Brief**

*(Updated Synthesis: Internal, Perplexity, Gemini 3.1-pro, Grok 4.5 \+ Extended Test Framework)*

## **0\. Executive Posture**

All prior analyses agree on Tiwas’s identity and negative space. Two high-impact mechanical forks remain situation-dependent by designer ruling:

* **Opposed quality measure** (Margin vs Blackjack vs Hybrid) — situation-dependent (e.g., target shooting favors Margin; arm wrestling favors Blackjack).  
* **Hit-location default** — situation-dependent (e.g., formal duel favors locations on; chaotic brawl favors locations off).

This brief keeps both forks visible, ranks residual decisions by dependency and impact, and now incorporates a constrained Extended Test framework as a Universal Play Module for long-term tasks.

### **Locked Identity Statement**

> Tiwas is a high-consequence percentile universal RPG in which every attempt costs resources, every failure generates growth, and every meaningful success changes the tactical or narrative state.

### **Locked Priority Ranking**

1. Granular physical simulation (hit locations, wound states, long-term injury) where the situation warrants it.  
2. Heroic resilience / low permanent character loss rate.  
3. Minimize resolution steps per exchange without sacrificing Priority 1\.

---

## **1\. Core Convergence Across Analyses**

| Theme | Shared Conclusion | Source Weight |
| ----- | ----- | ----- |
| Combat philosophy | Opposed contest that produces state change (position, control, injury, equipment), not pure HP attrition | All prior |
| Opposed test primacy | Single universal contest procedure for combat and non-combat | All prior |
| Resource centrality | Physical Energy / MP remain the first endurance layer; Overflow-to-HP is identity | All prior |
| Magic model | Emergent from Advanced Skills \+ MP \+ overflow backlash; no fixed class/spell-list default | All prior |
| Architecture | Core engine ↔ Universal Play Modules ↔ Setting Modules | All prior |
| Negative space | Reject D\&D HP escalation \+ rest pacing; reject fixed spell lists as core; reject Fate narrative currency as primary engine | All prior |
| Failure stakes | Failure must never be consequence-free; stakes gate required | All prior |
| Effect menu size | Short universal list (≈ 8–12) gated by weapon/setting tags | Perplexity \+ Gemini \+ Grok 4.5 |
| Long-term tasks | Extended Tests (constrained) are a high-value addition for multi-interval work | New synthesis |

---

## **2\. Major Divergences Kept Open**

### **2.1 Opposed Quality Measure (Situation-Dependent)**

| Model | Core Formula | Strength for Tiwas | Weakness for Tiwas | Best Situational Fit |
| ----- | ----- | ----- | ----- | ----- |
| Pure Margin | Margin \= Skill − Roll; higher Margin wins | Low successful rolls \= efficient \+ high quality; redeems Skill \> 99 | Expensive high rolls penalized twice | Precision tasks (target shooting, lockpicking, stealth, research) |
| Pure Blackjack | Among successes, higher natural roll wins | Expensive commitment buys victory | Skill \> 99 needs Mastery patch; can feel swingy | Contests of force or commitment (arm wrestling, shoving) |
| Hybrid Committed | Committed \= Roll \+ max(0, Skill − 99); higher Committed wins | Satisfies both efficiency and commitment stories | Extra term; requires simulation | Mixed or unknown situations |

**Designer ruling**: Quality measure is selectable per contest type. Any implementation must preserve Cost \= Roll and the 100-Fumble rule.

### **2.2 Hit-Location Granularity (Situation-Dependent)**

| Tier | Model | Resolution Cost | Simulation Fidelity | Recommended Situational Use |
| ----- | ----- | ----- | ----- | ----- |
| 0 | No locations; Quality → global HP / conditions only | Lowest | Lowest | Mass brawls, cinematic fights, social-only scenes |
| 1 | Lightweight (units digit or reverse digits of the attack roll); no extra die | Near-zero extra steps | Medium-High | Standard simulation-grade play, formal duels |
| 2 | Full location armor \+ surgery trees | Higher | Highest | Optional gritty module only |

**Designer ruling**: Default on/off is situation-dependent. The core engine must support all three tiers as modules.

---

## **3\. Synthesized Architecture (Updated)**

text  
TIWAS CORE ENGINE (locked)  
├── d100 roll-under \+ mandatory 100-Fumble  
├── 24-attribute matrix, live derived stats  
├── Physical Energy / MP identity \+ Overflow → HP  
├── Failure XP / temporary Skill Roll Pool / Cap ceiling  
├── General XP, unbounded advancement  
└── Advanced Skill construction on failed doubles

UNIVERSAL PLAY MODULES  
├── Difficulty grades (Skill-side only)  
├── Task adjudication \+ stakes gate  
├── Opposed contests (quality measure selectable)  
├── Outcome Effect menu (8–12 universal, gated)  
├── Extended Tests (long-term / multi-interval tasks)  
├── Time / turns / action economy  
├── Conditions / tags  
├── Two-track harm (resources/HP collapse vs wounds/conditions)  
├── Optional lightweight locations (Tier 0/1/2)  
├── Equipment traits \+ tags  
├── NPC compression packages  
└── Rest / healing / death thresholds

SETTING MODULES  
├── Fantasy / SF / Modern / Horror / Historical / Cinematic  
└── Each opens effect tags, creatures, tech, and which lineages count as powers

### **Two-Track Harm Model**

* **Track A – Resources / Global HP**: Physical Energy and MP are the primary endurance layer. Overflow and residual trauma deplete Global HP (sum of Body attributes). HP \= 0 triggers incapacitation checks, not automatic death.  
* **Track B – Localized Wounds / Conditions**: When Net Damage exceeds a threshold, a Wound is applied to a location (if locations are active). Wound states (Light / Serious / Critical) produce conditions, disability, or death checks.

---

## **4\. Outcome Effect Menu**

Universal list of ≈ 8–12 effects. Winner of an opposed contest may purchase 1 free effect; additional effects cost Net Advantage / Quality bands or require a success-double.

**Core candidate list**:

1. Inflict Injury (apply Quality to wound/HP track)  
2. Impose Condition (Stunned, Prone, Impaired…)  
3. Disarm / Break Hold  
4. Force Movement / Seize Position  
5. Seize Tempo (advantage on next contest)  
6. Guard Break  
7. Bleed / Ongoing Drain  
8. Open Retreat / Compel Yield  
9. Damage Equipment (tag-gated)  
10. Choose Location (only if locations module active)

Weapons, powers, and setting modules unlock or restrict subsets. Effects never modify the historical die face.

---

## **5\. Extended Tests Framework (New Synthesis)**

### **Design Rationale**

CODA-style Extended Tests address reserved scope in task adjudication, environmental hazards, crafting, research, travel, sieges, and prolonged social or technical work. They convert binary failure into ongoing pressure while remaining inside the existing engine.

### **Compatibility Verification**

| Tiwas Invariant | Extended Test Interaction | Verdict |
| ----- | ----- | ----- |
| Cost \= Roll | Every interval still costs its natural die face in PE or MP | Compatible |
| Failure XP | Each failed interval generates Failure XP normally | Compatible |
| 100-Fumble | Remains mandatory failure \+ Double on any interval | Compatible |
| Overflow-to-HP | High-cost failures on long tasks can still overflow | Compatible |
| Advanced Skill construction | Failed doubles during Extended Tests may still spawn Advanced Skills | Compatible |
| Automatic post-test recovery | Recovery occurs after every interval | Compatible (long tasks expose steady-state recovery math) |
| No parallel currencies | Progress is pure accumulation of existing test outcomes | Required constraint |

### **Tiwas-Native Form**

1. GM declares a task Extended and defines:  
   * Required total Quality / Margin sum (or number of successful intervals).  
   * Time increment per roll.  
   * Complication risk on failure (drawn from existing Condition / hazard list).  
2. Each interval is a normal skill test (unopposed or opposed). Cost, Overflow, Failure XP, recovery, and Advanced Skill rules apply unchanged.  
3. Accumulated successful Margins (or binary success count) are tracked until the threshold is reached or the situation ends.  
4. Failed doubles during the Extended Test may create or evolve Advanced Skills, reflecting learning under prolonged pressure.  
5. Optional conversion rule: any mundane or relaxed failed test may be reframed as the first interval of an Extended Test when the fiction supports ongoing effort (subject to the stakes-gate principle).

### **Constraints (Non-Negotiable)**

* Progress Points must never become a second resource economy. They are only a running total of existing test outcomes.  
* Complications map exclusively to existing tools (Conditions, resource drains, environmental hazard checks, temporary Cap reductions).  
* Time increments must be explicit so automatic recovery does not trivialize long tasks.  
* The conversion rule is gated by stakes: only convert when continued effort is narratively and mechanically meaningful.

---

## **6\. Magic & Special Abilities**

Magic and all special abilities are constructed exclusively through the Advanced Skill engine:

* Permission granted by setting module.  
* Test uses Mind-rooted (or Body-rooted) skill; cost \= roll; Overflow possible.  
* Quality dictates effect magnitude.  
* Failed double creates or evolves an Advanced Skill lineage.  
* Fixed spell lists exist only as optional setting curricula, never as core chassis.

Extended Tests interact cleanly with magic: prolonged ritual or research tasks become Extended Tests that still risk Overflow and can generate Advanced Skills on failed doubles.

---

## **7\. Ranked Residual Designer Decision Points**

Ordered by dependency and impact.

| Rank | ID | Decision | Impact | Dependency | Recommended Approach |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 1 | S-1 | Opposed quality measure selection rules (when Margin vs Blackjack vs Hybrid) | Rewrites all contest math | None | Per-contest-type guidance; simulate win rates \+ PE drain |
| 2 | S-2 | Hit-location default policy (when Tier 0/1/2) | Controls step count and lethality feel | S-1 | Situation tags or GM table |
| 3 | S-3 | Effect trigger thresholds | Controls combat pacing | S-1 | Simulate exchange length |
| 4 | S-4 | Wound threshold formula | Controls when Track B activates | S-2 | Prefer derived (e.g. floor(HP/10)) |
| 5 | S-5 | Armor interaction (Bypass vs permanent Sunder) | Bookkeeping load | S-3 | Default Bypass; Sunder tag-gated |
| 6 | S-6 | Passive vs Active defense cost | Resource tactics | S-1 | Passive Guard at half-skill, zero PE cost |
| 7 | S-7 | Death path exact triggers | Permanent loss rate (Priority 2\) | S-4 | Major vital \+ failed opposed survival check |
| 8 | S-8 | Difficulty-grade interaction with Failure XP | Exploit control | Core | Failure XP always uses raw Skill |
| 9 | S-9 | Extended Test Progress method (Margin sum vs success count) | Long-task pacing | S-1 | Simulate both; prefer Margin sum for consistency with quality measure |
| 10 | S-10 | Extended Test Progress loss on failure | Risk profile of long tasks | S-9 | Default stall only; loss as optional complication |
| 11 | S-11 | Rest / healing timelines | Attrition clock | S-4, S-7 | Time \+ skill-based; no short-rest full resets |
| 12 | S-12 | NPC compression grades | Encounter design speed | All above | Package templates from same rules |

---

## **8\. Implementation Sequence for Future LLM Sessions**

1. Freeze core invariants and stakes-gate wording.  
2. Implement selectable opposed quality measures (Margin / Blackjack / Hybrid) behind a situation flag.  
3. Attach 8–12 Outcome Effects \+ Quality → Injury mapping.  
4. Implement two-track harm; confirm PE empty ≠ auto-loss and Global HP ≠ primary kill track.  
5. Add optional location modules (Tier 0/1/2) with Zero-Step or digit derivation.  
6. Implement Extended Tests as repeated normal tests with Progress accumulation (no new currency).  
7. Difficulty grades \+ Failure XP interaction test.  
8. Magic grammar as Mind-rooted Advanced Skills using the same opposed primitive.  
9. Rest, healing, death thresholds.  
10. NPC packages and encounter curves.  
11. Full regression suite against Cost \= Roll, 100-Fumble, Overflow, Failure XP, Advanced Skill rules, and Extended Test resource drain over multiple intervals.

---

## **9\. Contribution Summary**

| Source | Distinctive Contribution Retained |
| ----- | ----- |
| Internal / Prior Grok | Quantitative invariants, Pain Pump magnitude, steady-state recovery math, two-track HP necessity |
| Perplexity | Margin triad framing, identity sentence, short Effect menu emphasis, negative-examples table |
| Gemini 3.1-pro | Zero-Step reverse-digit location method, Dual-Layer HP \+ localized wounds separation, Net Advantage as Effect currency |
| Grok 4.5 | Hybrid Committed candidate, explicit simulation matrix requirement, ranked residual decisions |
| New synthesis | Constrained Extended Test framework that preserves all core invariants while covering long-term task adjudication |

---

## **10\. Final Directional Summary for LLMs**

* Build one opposed contest primitive that can accept different quality measures.  
* Keep hit locations modular and situation-gated.  
* Drive combat with a short, gated Outcome Effect menu.  
* Maintain two-track harm so resources shape options while wounds and conditions decide fights.  
* Express all special abilities (martial, magical, technical, social) as Advanced Skill lineages.  
* Implement Extended Tests as multi-interval applications of the existing test procedure with Progress as pure accumulation of outcomes; never introduce a parallel Progress Point economy.  
* Never violate Cost \= Roll, 100-Fumble, Overflow-to-HP, or Failure XP rules.  
* Leave S-1 and S-2 open for designer or situational adjudication; rank all other decisions behind them.

*Residual guess*: Exact numerical thresholds for Quality bands, wound severity, Effect costs, and Extended Test Progress targets will require simulation once S-1 and S-2 are provisionally chosen for a given campaign mode. No numerical values are locked here.

