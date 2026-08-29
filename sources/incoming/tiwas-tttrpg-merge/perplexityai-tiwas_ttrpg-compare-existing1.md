<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# I want you to tell me what I should lean towards for Tiwas TTRPG based on its hardcore roll mechanics. At least give me a comparative list

You should lean toward **Mythras-style opposed combat consequences**, **Basic Roleplaying’s percentile contest structure**, and **GURPS’s disciplined universal-systems thinking—but not its full complexity load**. You should actively avoid D\&D-style hit-point escalation, large fixed spell lists as the universal default, and any design that makes failed tests consequence-free or mechanically trivial.

For Tiwas specifically, the goal is not to imitate any of these systems. It is to borrow their strongest *design lessons* while preserving Tiwas’s distinctive engine: costly d100 tests, failure-generated growth, dynamic Advanced Skills, Body/Mind resource identity, and high-risk fumbles.

## Recommended lean-toward systems

| Priority | System / subsystem | What Tiwas should learn | Why it fits Tiwas | What not to copy |
| --: | :-- | :-- | :-- | :-- |
| 1 | **Mythras: opposed rolls and Special Effects** | Combat exchanges should produce tactical consequences, not merely “miss” or “lose HP” | Tiwas already makes failures costly and meaningful; combat should likewise turn success quality into positioning, disarm, retreat, pressure, injury, or control | Its full combat-skill structure, detailed hit locations, and long Special Effect lists |
| 2 | **Basic Roleplaying: percentile contests and graded outcomes** | Use a coherent roll-under contest procedure that compares outcome quality before comparing raw rolls | Tiwas is fundamentally percentile roll-under; a related contest framework can extend it without replacing its core mathematics | Directly importing BRP’s one-fifth special-success thresholds or resistance table |
| 3 | **GURPS: generic-system architecture and consequence-based fatigue** | Separate universal engine rules from setting modules; let equipment and abilities alter fictional permissions rather than replace the core resolution engine | Tiwas is intended to run fantasy, science fiction, horror, historical, and modern games; modularity is essential | GURPS’s exhaustive skill list, point-buy accounting, numerous exceptions, and equipment-detail burden |

### 1. Lean strongly toward Mythras’s consequence-oriented combat

**Recommendation:** Use Mythras as the strongest reference point for *combat philosophy*, especially opposed exchanges and meaningful outcomes beyond raw damage.

Mythras makes opposed rolls central to many combat interactions and uses success differences to determine who gains tactical leverage. Its Special Effects include options such as disarm, trip, force a failure, withdraw, pin, bleed, impale, press advantage, and compel surrender.[^1][^2]

Tiwas should not import that list wholesale. But the underlying principle aligns unusually well:

> A successful roll should change the tactical situation, not merely subtract a number.

That is highly compatible with Tiwas because Tiwas already says:

- every test commits resources;
- high rolls are expensive;
- failures generate learning;
- doubles create novel capabilities;
- Body and Mind are differentiated;
- resource exhaustion can become HP damage.

A Tiwas combat exchange should therefore create a **state change**. A successful defender might not simply “negate” damage; they might gain spacing, force the attacker off balance, redirect the attack, create an opening, protect an ally, or preserve a resource.

A successful attacker might choose between:

- inflicting damage;
- breaking guard;
- disarming;
- forcing movement;
- imposing a condition;
- creating a retreat opportunity;
- damaging equipment;
- pinning;
- gaining a positional advantage;
- forcing a resource drain;
- escalating a threat.

This would make combat feel like a hard, dynamic contest between people under pressure rather than a repetition of “roll to hit, roll damage.”

### Why it fits Tiwas mathematically

Tiwas has an unusual asymmetry:

$$
\text{Higher roll} \Rightarrow \text{higher resource cost}
$$

but:

$$
\text{Higher roll} \Rightarrow \text{more likely failure}
$$

That means Tiwas should avoid a combat design where a near-failed high roll is treated as indistinguishable from a harmless miss. A roll of 96 is not just unsuccessful—it may have cost 96 Energy or MP and could have caused HP overflow.

A consequence-based combat system can turn these events into fiction:

- A costly failed attack may overextend the attacker.
- A failed defence may consume guard, positioning, armour integrity, or movement options.
- A failed double may produce an Advanced Skill that reflects a painful lesson from the fight.
- A 100-Fumble can be a genuine crisis, not merely a numerical miss.

**Suggested Tiwas design direction:** develop a small universal “Outcome Effect” menu with perhaps 8–12 options, then let weapons, magic, vehicles, and settings modify which effects are available. This preserves tactical depth without forcing every setting to use medieval weapon manoeuvres.

**Confidence:** High that this philosophy fits Tiwas; Medium on the final size and exact contents of the effect list.

***

### 2. Lean toward Basic Roleplaying’s contest clarity

**Recommendation:** Use Basic Roleplaying as the main reference point for an intelligible percentile-based opposed-test procedure.

BRP’s opposed skill procedure has both participants roll the relevant percentile skill. If only one succeeds, that side wins; if both succeed, outcomes are compared through success quality and then the successful rolls; ties can be resolved by higher skill.  BRP also uses special successes at one-fifth of the relevant success chance, making unusually low rolls meaningfully better than ordinary successes.[^3][^4][^5]

This is useful to Tiwas because it addresses a major reserved system: **what happens when two active agents oppose one another?**

Examples include:

- Stealth versus Perception.
- Grappling versus escape.
- Deception versus Cunning.
- Negotiation versus Composure.
- Hacking versus countermeasures.
- Piloting versus pursuit.
- Psychic influence versus Resolve.
- Sword strike versus parry.
- Aim versus evasive movement.

Tiwas needs a procedure that works across genres and does not require inventing a separate mini-game for every contest.

### What Tiwas should borrow

Borrow the *ordering principle*, not the exact BRP rule:

1. Did each side succeed?
2. If both succeeded, who succeeded more convincingly?
3. If outcomes remain tied, use a transparent tie-breaker.
4. Translate the result into an outcome appropriate to the fiction.

### What Tiwas should develop instead

Tiwas should test a **margin-based contest model** rather than immediately adopting BRP’s success grades.

A natural Tiwas measure is:

$$
Margin = Skill - Roll
$$

For a successful roll:

$$
Margin \ge 0
$$

A higher Margin means the character succeeded by more.

For example:


| Character | Skill | Roll | Result | Margin |
| :-- | --: | --: | :-- | --: |
| Scout | 65 | 22 | Success | +43 |
| Guard | 50 | 47 | Success | +3 |

The Scout wins decisively.

This fits Tiwas better than raw low-roll comparison because it respects both:

- the character’s skill;
- the actual roll.

It also naturally supports the existing system’s resource logic. A skilled character who rolls 22 spent only 22 resource points and achieved a strong margin. A barely successful result at 47 cost more and achieved less.

That creates a coherent triad:

$$
\text{Skill} \rightarrow \text{chance of success}
$$

$$
\text{Roll} \rightarrow \text{resource cost}
$$

$$
\text{Skill} - \text{Roll} \rightarrow \text{quality of success}
$$

This may be the most “Tiwas-native” extension discovered so far.

**Confidence:** High that Tiwas needs a single generic contest procedure; Medium that margin should be the final measure, because it needs comparative simulation against raw-roll and outcome-tier alternatives.

***

### 3. Lean toward GURPS’s modular universal architecture

**Recommendation:** Use GURPS as an architectural reference, not a mechanical template.

GURPS is relevant because it is designed as a generic, universal framework. Its broad lesson is that a rules engine can support many genres when it distinguishes:

- core universal rules;
- optional complexity modules;
- setting assumptions;
- campaign-level power expectations;
- equipment and technology packages;
- supernatural or cinematic subsystems.

GURPS also treats fatigue as a finite energy resource and links it to exertion and capability.[^6][^7]

Tiwas should adopt the **modularity principle** because its own core is already generic:

- Body skills can model athletics, fighting, piloting, surgery, stealth, driving, crafting, and survival.
- Mind skills can model investigation, technical work, social influence, hacking, magic, psionics, command, and research.
- Advanced Skills can represent specialised techniques, professions, spell forms, martial styles, technologies, cybernetic routines, or psychic disciplines.

This is a powerful foundation for a universal game.

### A suitable Tiwas architecture

```text
TIWAS CORE ENGINE
├── d100 roll-under resolution
├── Attributes and derived statistics
├── Skill caps and tiers
├── Physical Energy and MP
├── Overflow into HP
├── Failure XP and General XP
└── Advanced Skill creation

UNIVERSAL PLAY MODULES
├── Difficulty and task adjudication
├── Opposed tests
├── Time, turns, and action economy
├── Consequence framework
├── Conditions
├── Damage, healing, and recovery
├── Equipment traits
├── NPC construction
└── Encounter and GM procedures

SETTING MODULES
├── Fantasy: magic, creatures, cultures
├── Science fiction: vehicles, hacking, psionics, biotech
├── Modern: firearms, law, surveillance, wealth
├── Horror: fear, corruption, sanity-like pressures
├── Historical: social rank, logistics, warfare
└── Superhero/cinematic: powers, collateral effects, scale
```

The important point is that magic should not become mandatory in the base game. It should be a **setting capability framework** built from the same Skill, resource, consequence, and Advanced Skill architecture.

### What Tiwas should avoid copying from GURPS

Do not adopt:

- hundreds of narrow, separately purchased skills;
- heavy point-buy character accounting;
- high granularity by default;
- extensive per-item equipment statistics;
- a core experience that requires frequent table lookup;
- a universal system so broad that ordinary play becomes slow.

Tiwas’s 24-attribute matrix already gives it a large mechanical footprint. It should seek **depth through interaction**, not through an ever-growing catalogue of subrules.

**Confidence:** High that modularity is essential for Tiwas as a universal game; High that GURPS-scale bookkeeping should be avoided.

***

## Systems to treat as negative examples

These are not bad games. They are negative examples **for this project’s stated identity**.


| Avoid leaning toward | Why it clashes with Tiwas | Specific risk |
| :-- | :-- | :-- |
| D\&D 5e-style HP, healing, and rest pacing | Tiwas already has HP, Energy, MP, overflow, and automatic partial recovery | HP becomes a long-duration damage sponge and undermines exertion risk |
| Fixed-class/fixed-spell-list magic as the default universal model | Tiwas already supports dynamic skills and emergent Advanced Skills | Magic becomes a disconnected exception system |
| Fate-style broad narrative currency as the main resolution layer | Tiwas is explicitly hardcore, quantitative, resource-linked, and simulation-minded | The game’s existing mathematical identity is diluted |

### Avoid D\&D-style hit-point escalation and rest pacing

D\&D-style combat often treats hit points as a broad abstraction of endurance, luck, minor wounds, morale, and survivability. It also commonly relies on powerful recovery cycles tied to rests.

Tiwas already has a clearer and harsher resource chain:

$$
Skill\ Test
\rightarrow
Resource\ Cost
\rightarrow
Resource\ Depletion
\rightarrow
Overflow
\rightarrow
HP\ Damage
$$

Importing D\&D-like high HP scaling or large healing resets risks making that chain irrelevant.

If HP becomes too large relative to weapon damage and overflow, then:

- exhaustion becomes cosmetic;
- 100-Fumbles lose threat;
- armour becomes difficult to balance;
- attrition disappears;
- combat becomes long and repetitive;
- “hardcore roll mechanics” become numerically present but strategically weak.

Tiwas should instead lean toward **HP as a meaningful survival reserve**, with Energy and MP serving as the first line of endurance.

This does not require gritty instant-death simulation. It means the system should preserve the fact that resource collapse is dangerous.

**Confidence:** High.

***

### Avoid fixed classes and fixed spell lists as Tiwas’s default magic model

Tiwas’s Advanced Skill mechanic is unusually compatible with emergent abilities.

A failed double already says:

> A difficult attempt teaches the character a new, more specialised way to act.

That can naturally support:

- a sword technique;
- a firearm trick;
- a magical practice;
- an alchemical method;
- a hacking routine;
- a psychic discipline;
- a leadership manoeuvre;
- a vehicle stunt;
- a survival technique;
- a social manipulation.

A fixed spell list can still exist in a setting module as a reference catalogue, teaching curriculum, religious tradition, corporate technology suite, or military manual. But it should not be the mechanical foundation of Tiwas magic.

A Tiwas-native magic framework should likely make spells or powers:

$$
\text{Advanced Skills}
+
\text{defined effects}
+
\text{MP expenditure}
+
\text{risk / overflow}
+
\text{failure consequences}
$$

That would preserve genericity. A fantasy “fire spell,” a sci-fi “plasma discharge,” a psychic “telekinetic push,” and a superhero “kinetic blast” could all be different fictional expressions of the same underlying effect architecture.

**Confidence:** High.

***

### Avoid Fate-style narrative currency as the primary engine

Fate is excellent for narrative-authorial play, flexible aspects, and player-driven story permission. But its core assumptions conflict with Tiwas’s existing foundation.

Tiwas already has:

- 24 independently rolled attributes;
- derived pools;
- skill caps;
- tier mathematics;
- d100 probabilities;
- failure-generated XP;
- automatic recovery;
- overflow damage;
- permanent fumbles;
- emergent skill creation.

A primary resolution layer based on broad narrative aspects, player currency, and negotiated fictional permissions would compete with rather than reinforce this machinery.

Tiwas may still benefit from a **light narrative layer**, such as:

- tags;
- affiliations;
- motives;
- background traits;
- setting descriptors;
- faction reputation;
- narrative permissions for tools and contacts.

But those should alter the *fictional availability* of actions, not replace d100 resolution.

**Confidence:** Medium-high.

***

## Recommended comparative shortlist

If you want a concise answer to the earlier preference question, I recommend this:

```text
Lean toward:
1. Mythras — opposed combat and consequence-driven Special Effects,
   but not full hit locations or its complete effect catalogue.

2. Basic Roleplaying — clear percentile contests and outcome-quality comparison,
   but not its exact special-success thresholds or resistance table.

3. GURPS — universal modular architecture and meaningful exertion,
   but not its point-buy complexity, huge skill list, or equipment granularity.

Avoid / treat as negative examples:
1. D&D 5e — large HP pools, rapid rest recovery, and combat as repeated hit-point subtraction.

2. Class-and-spell-list-first fantasy design — magic should emerge from Tiwas skills,
   MP, risk, and Advanced Skill creation rather than sit outside them.

3. Fate as a primary rules chassis — narrative currency should not replace Tiwas’s
   hardcore d100/resource/failure engine.
```


## Best-fit design identity

The strongest direction for Tiwas is:

> **A high-consequence percentile universal RPG where every attempt costs something, every failure teaches something, and every major success changes the situation.**

That suggests the following design priorities:

1. **Combat should be an opposed contest of position, control, and injury**, not a simple attack-roll gate followed by damage.
2. **Success quality should matter**, most likely through a Tiwas-specific margin or outcome-band system.
3. **Resources should remain strategically central**, because Physical Energy and MP are a core identity feature rather than secondary bookkeeping.
4. **Advanced Skills should become the universal language of specialisation**, covering martial arts, professional expertise, vehicles, science, magic, psionics, technology, and social manoeuvres.
5. **Setting modules should add content and permissions**, not replace the core mathematical engine.
6. **Failure must remain productive but never consequence-free**, otherwise XP farming overwhelms the intended risk loop.

The next research phase should use Mythras, BRP, and GURPS as the main comparative references while building Tiwas-native simulations for opposed contests, tactical outcomes, exhaustion, and Advanced Skill lineages.
<span style="display:none">[^10][^11][^12][^13][^14][^15][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://rpol.net/display.cgi?gi=78495\&ti=1

[^2]: https://www.scribd.com/document/934968441/MythWrack-5d

[^3]: https://www.chaosium.com/content/FreePDFs/BRP/CHA2021 - Basic RolePlaying Quick-Start.pdf

[^4]: https://www.chaosium.com/content/FreePDFs/BRP/BRP SRD - V1.0.pdf

[^5]: https://www.chaosium.com/content/orclicense/BasicRoleplaying-ORC-Content-Document.pdf

[^6]: https://www.scribd.com/document/459015317/GURPS-Lite-Fourth-Edition-pdf

[^7]: https://www.scribd.com/doc/46933794/GURPS-4th-Edition-Lite

[^8]: https://www.sjgames.com/ill/img/retailerimages/Munchkin OTD/Game Support/GURPS/GURPS_Lite_Interlingua_Fourth_Edition.pdf

[^9]: https://www.scribd.com/document/356300106/TDM110-Mythras-Imperative

[^10]: https://www.scribd.com/document/691853706/TDMORC002-Mythras-Imperative-071223

[^11]: https://www.tapatalk.com/groups/designmechanism/mythras-imperative-3e-errata-rules-clarifications-t3885.html

[^12]: https://www.scribd.com/document/976457177/GURPS-Lite-Fourth-Edition-pdf

[^13]: https://rpol.net/display.cgi?gi=76885\&ti=4\&date=1653663364

[^14]: https://www.scribd.com/document/949608362/GURPS-4e-Lite

[^15]: https://mdhughes.tech/2020/03/27/chaosiums-system-reference-document/

