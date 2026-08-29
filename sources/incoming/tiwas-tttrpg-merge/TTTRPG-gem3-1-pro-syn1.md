# Tiwas Next-Phase Research & Direction Brief: Analysis, Contrast, and Synthesis

## 0\. Executive Synthesis & Architectural Posture

This document compares, contrasts, and synthesizes two distinct architectural analyses for the Tiwas TTRPG:

1. The Lead Systems Architect (Internal) Brief: Prioritized ultra-crunch simulation, granular hit locations, dual-layer wound/HP tracking, and zero-extra-step resolution mechanics.  
2. The Perplexity AI (External) Brief: Prioritized Mythras-style consequence generation, Basic Roleplaying (BRP) percentile margin contests, and GURPS-style modularity, while explicitly warning *against* the bloat of full hit locations and exhaustively detailed skill/equipment lists.

### Core Convergence (Where Both Analyses Agree)

Both analyses arrive at identical conclusions regarding the fundamental identity of Tiwas:

* Consequence-Driven Combat: Combat must not be a static HP-attrition gate. Successes and failures must change fictional positioning, resources, or capabilities (Mythras influence).  
* Opposed Test Primacy: Active conflicts must use a universal opposed-roll structure that rewards high skill and acknowledges the resource cost of the roll (BRP influence).  
* Modular Universalism: The core engine (d100, Overflow, Advanced Skills) must be rigorously separated from setting-specific permissions (magic, cybernetics) (GURPS influence).  
* Rejection of Modern Tropes: Both explicitly reject D\&D 5e-style hit point scaling/rest pacing, fixed class/spell-list Magic, and Fate-style meta-currencies.

### Core Divergence (The Granularity Tension)

* The Internal Brief mandated *granular physical simulation, hit locations, and wound states.*  
* The Perplexity Brief explicitly flagged *detailed hit locations and long Special Effect lists* as negative GURPS/Mythras elements to avoid.

### The Synthesized Solution

To satisfy the mandate for simulation-grade crunch without violating the warning against resolution bloat, Tiwas must employ Zero-Step Granularity. Hit locations and wound severities must be derived mathematically from the *existing* d100 attack roll and margin of success, requiring no secondary tables, location dice, or sub-system calculations.

The following sections provide the synthesized mechanical directives for future LLM design sessions.

---

## 1\. Opposed Tests: The Margin-of-Success Synthesis

### Contrast

* Internal Analysis: Proposed comparing Outcome Degrees (Fumble \< Failure \< Success \< Critical) to minimize arithmetic.  
* Perplexity Analysis: Strongly recommended a raw Margin of Success formula: Margin \= Skill \- Roll.

### Synthesis & Directional Advice

Adopt the Perplexity Margin equation: Margin \= Skill \- Roll.

This is mathematically superior for Tiwas because it seamlessly unifies the game's core contradiction (higher rolls cost more resources but are less likely to succeed).

If a character with Skill 65 rolls a 20:

* Cost: 20 (Highly efficient).  
* Margin: \+45 (Highly effective).

If they roll a 60:

* Cost: 60 (Exhausting).  
* Margin: \+5 (Barely effective).

The Margin equation elegantly maps *effort efficiency* to *outcome quality*.

The Synthesized Opposed Procedure:

1. Both active participants declare skill and resource domain.  
2. Both roll d100 and pay resource cost equal to their roll. (Overflow applies instantly).  
3. If both fail, the contest is a muddy stalemate, but both gain Failure XP (Roll \- Skill).  
4. If one succeeds and one fails, the successful party dictates the consequence.  
5. If both succeed, compare Margins. The highest Margin wins the exchange.  
6. The difference between the winning and losing Margin is the Net Advantage, which acts as currency to buy Combat Consequences / Special Effects.

### Compatibility Check

| Tiwas Core Element | Compatibility Verification |
| :---- | :---- |
| Cost \= Roll | Perfectly maintained. High-margin successes naturally cost less, simulating expert efficiency. |
| Failure XP | Maintained. The loser of an opposed roll only gets XP if they actually failed their own test. A successful roll that simply loses to a *better* successful roll does not grant XP (preventing XP farming on successes). |
| Overflow-to-HP | Maintained. A defender can overexert (roll 95, cost 95 MP), succeed, win the contest, but still take massive Overflow-to-HP. This creates gritty, Pyrrhic victories. |

---

## 2\. Combat Exchanges & Consequence Menus

### Contrast

* Internal Analysis: Suggested categorized Consequence Packages (Injury, Position, Control, Exposure) triggered by success.  
* Perplexity Analysis: Advocated for a curated Mythras-style "Outcome Effect" menu (8-12 options) where a successful roll *changes the tactical state* rather than just subtracting a number.

### Synthesis & Directional Advice

Implement a Margin-Driven Consequence Menu.

Combat is not a separate subsystem; it is merely an Opposed Test where the Net Advantage (the winner's margin minus the loser's margin) is spent to purchase consequences.

Directional Mechanics:

* Base Attack: Winning the opposed test allows the attacker to inflict Base Weapon Damage.  
* Special Effects (Mythras influence): If the winner's Net Advantage exceeds certain thresholds (e.g., \+20, \+40), they may purchase additional effects from a universal, restricted list of \~10 options.  
* Effect Categories to implement:  
  * *Disarm/Sunder:* Damage or remove equipment.  
  * *Trip/Push:* Alter spatial positioning.  
  * *Bypass Armor:* Use accuracy (Margin) to negate physical DR.  
  * *Choose Location:* Override the random hit location (see Section 3).  
  * *Pin/Grapple:* Restrain using opposed Body skills.  
  * *Bleed/Stun:* Impose a universal Condition Tag.

By capping the universal list at \~10 options and allowing weapon tags (e.g., *Hook, Flexible*) to unlock 1-2 specific effects, Tiwas achieves Mythras-level tactical depth without the cognitive overload Perplexity warns against.

### Compatibility Check

| Tiwas Core Element | Compatibility Verification |
| :---- | :---- |
| Advanced Skills | Advanced Skills (e.g., *Zweihander Mastery*) can simply reduce the Margin cost of specific Special Effects, or grant access to exclusive ones. |
| 100 \= Fumble | A 100 is an automatic failure, meaning Margin is highly negative, granting the opponent massive Net Advantage to spend on devastating counter-effects. |
| Action Economy | Resolving attack, defense, and special effects in a *single roll pairing* satisfies the mandate to minimize resolution steps per exchange. |

---

## 3\. Granular Injury: Hit Locations & Wound States

### Contrast

* Internal Analysis: Demanded ultra-crunch simulation, hit locations, wound tracking, and heroic resilience.  
* Perplexity Analysis: Explicitly warned against "detailed hit locations" and "D\&D-style HP escalation."

### Synthesis & Directional Advice

Implement Dual-Layer HP/Wounds with "Zero-Step" Hit Locations.

To satisfy the crunch mandate without causing the slowdown Perplexity fears, hit locations must not require a separate roll.

1\. Zero-Step Hit Locations:  
When an attack succeeds and inflicts a wound, read the d100 attack roll's digits in reverse to determine the location on a static d100 chart.

* *Example:* An attacker rolls a 37 (Success). The hit location is 73 (e.g., Right Leg).  
* If the attacker buys the *Choose Location* consequence using their Margin, they ignore the reverse-digits and pick the location.

2\. Dual-Layer Damage System:

* Global HP (The Buffer): As mandated by the core rules, HP is the sum of all 12 Body attributes. In combat, weapon damage acts as *Shock and Blood Loss*, depleting global HP. When HP reaches 0, the character is not dead, but must make a Body test (e.g., Toughness) every round to remain conscious.  
* Localized Wounds (The Simulation): If the Net Damage (Damage \- Armor DR) exceeds a mathematical threshold (e.g., 20% of Max HP, or a static number based on Toughness), it inflicts a Wound to the derived hit location.  
* Wound States:  
  * *Light:* Imposes an Effective Test Value (ETV) penalty.  
  * *Serious:* Disables the location (e.g., drop weapon, fall prone).  
  * *Critical:* Permanent injury/dismemberment, forces immediate death check.

This resolves the tension perfectly: it provides granular, simulation-grade hit locations and crippling wounds, but keeps resolution fast and preserves Tiwas's large HP pools as a heroic exhaustion/shock buffer rather than an abstract meat-sponge.

### Compatibility Check

| Tiwas Core Element | Compatibility Verification |
| :---- | :---- |
| HP / Overflow | Overflow from PE/MP exertion deals direct Global HP damage (exhaustion/shock) but *cannot* cause Localized Wounds. This beautifully separates combat trauma from exhaustion trauma. |
| Skill Rules | Localized wounds apply negative modifiers to the ETV (Effective Test Value) of associated Body skills, looping back into the core mechanics. |

---

## 4\. Magic & Advanced Skills: The Universal Framework

### Contrast

* Internal Analysis: Magic should be a skill-based, effect-construction layer using MP and PE, emergent from Advanced Skills.  
* Perplexity Analysis: "Fixed-class/fixed-spell-list magic as the default universal model" must be actively avoided. Setting modules should define fictional permissions, not core mechanics.

### Synthesis & Directional Advice

Implement Magic exclusively through the Advanced Skill engine and Condition Tags.

Tiwas already has the perfect engine for universal, setting-agnostic magic: the Failed Double. Magic should not exist as a separate subsystem. It should be a fictional permission applied to the existing mechanics.

Directional Mechanics:

1. The Permission: A setting module states that certain characters can use Mind attributes (e.g., *Willpower, Cunning*) to manipulate reality.  
2. The Test: To cast a "spell," the character makes a standard Tier 1 Mind test. The d100 roll dictates the MP cost and the success/failure.  
3. The Consequence: Margin of Success dictates the magnitude of the supernatural effect (using the same universal Consequence Menu as combat, re-flavored).  
4. The Evolution (Advanced Skills): If a pyromancer fails a spell with a Double 66, they create an Advanced Skill. They add an attribute, recalculate the cap, and name it *Directed Plasma Arc*. This ability now has a higher cap, greater stability, and specific effects.  
5. Backlash: Because Magic uses MP, and high rolls cost high MP, a difficult spell that rolls an 85 will drain 85 MP. If this exceeds the caster's pool, the Overflow deals direct HP damage. *Magic backlash is already built into the core physics of Tiwas.*

### Compatibility Check

| Tiwas Core Element | Compatibility Verification |
| :---- | :---- |
| Failure-Generated Growth | Spells are learned by attempting and failing. Grimoires are merely narrative tools; mechanics strictly enforce learning by doing. |
| Body/Mind Identity | Differentiates Psionics/Magic (MP drain) from Ki/Martial Arts (Physical Energy drain) strictly by which attribute tier they stem from. |

---

## 5\. Negative Space: What Must Be Explicitly Excluded

Based on the synthesized analysis, future LLM sessions must strictly reject the following mechanics if they attempt to introduce them:

| Excluded Mechanic | Source of Rejection | Reasoning for Tiwas |
| :---- | :---- | :---- |
| Hit Point Bloat / Escalation | Both Briefs | HP is a fixed sum of 12 Attributes (\~600 avg). It must not increase via "levels." It represents a finite, non-scaling threshold for shock and exertion. |
| Abstract Combat (No hit locations) | Internal Brief | Opposed tests without location/consequence outputs turn a 600 HP pool into a tedious slog. High HP requires granular wounds to maintain lethal tension. |
| Short-Rest Full Recovery | Perplexity Brief | Tiwas recovers floor(Regen/2) after *every* test. A D\&D-style "Rest" that instantly refills 600 HP/MP bypasses the attrition simulation. Rest must be defined by time and long-term care rules. |
| Fate Points / Narrative Rerolls | Both Briefs | Meta-currencies dilute the brutal reality of the 100-Fumble and the exact mapping of Cost=Roll. Modifiers must apply to the ETV, not grant rerolls. |

---

## 6\. Updated Implementation Sequence Ranking

To optimize the workflow for subsequent LLM design sessions, implement systems in this exact order to prevent circular dependencies.

| Rank | Subsystem | Design Directives (Synthesized) |
| :---: | :---- | :---- |
| 1 | Task Adjudication & Modifiers | Define ETV (Skill \+/- Mods). Lock in the rule: Failure XP always uses *Current Skill*, not ETV, to prevent modifier abuse. |
| 2 | Margin & Opposed Tests | Implement Margin \= Skill \- Roll. Define how Net Advantage resolves ties and buys success outcomes. |
| 3 | Combat Exchanges | Build the Mythras-lite Consequence Menu (Disarm, Trip, Bypass Armor). Map them to Margin costs. |
| 4 | Wounds & Hit Locations | Implement the Zero-Step hit location rule (reverse d100 digits). Define the Wound Severity thresholds (Light, Serious, Critical). |
| 5 | Armor & Weapons | Define Armor as localized DR. Define weapons as having Base Damage \+ Margin Scaling \+ Special Tags. |
| 6 | Conditions & Tags | Standardize penalites (e.g., *Bleeding, Stunned, Terrified*) as modifiers to ETV, Resource Max, or Regen rates. |
| 7 | Rest & Death | Define HP=0 as Incapacitation Checks, not instant death. Define Rest timelines vs. Immediate Recovery. |
| 8 | Magic / Tech Permissions | Write the guidelines for mapping Advanced Skills to supernatural or high-tech setting modules. |

---

## 7\. Residual Ambiguities & Designer Decision Points

Before an LLM can write the mathematical code for the above systems, the human designer must provide rulings on the following variables:

1. Wound Threshold Math: Does a localized wound occur when Net Damage exceeds a flat number (e.g., 20), a derived stat (e.g., Toughness / 2), or a percentage of Global HP (e.g., 10%)? *(Recommendation: Use a derived stat threshold like floor(HP/10) to keep math static during combat).*  
2. Armor Degradation: Does purchasing a *Sunder* special effect permanently reduce armor DR, or just bypass it for that attack? *(Recommendation: Bypass only, to reduce bookkeeping, unless the weapon possesses a specific 'Armor Piercing' tag).*  
3. Passive vs. Active Defense: In an opposed combat exchange, if a defender chooses *not* to spend a major action defending, do they still roll to resist (spending PE), or do they take a static ETV of 0? *(Recommendation: Implement a "Passive Guard" rule where undefended attacks roll against half-skill and cost the defender no PE, simulating taking a hit while preserving stamina).*

*End of Brief. The core Tiwas engine is now structurally prepared to accept universal, simulation-grade combat and resolution modules.*  
