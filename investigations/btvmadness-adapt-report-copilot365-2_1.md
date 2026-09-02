Tiwas Adventure Readiness Audit
Benchmark Adventure: Beyond-the-Vale-of-Madness-GURPS.pdf
Baseline Assessed Against: Tiwas-Alpha-Playtest-Corpus-2026-09-01.md

Sources: Beyond-the-Vale-of-Madness-GURPS.pdf; Tiwas-Alpha-Playtest-Corpus-2026-09-01.md

1. Executive Summary

Overall finding: Beyond the Vale of Madness is substantially playable in Tiwas today, but not fully playable as written without adaptation and several unresolved subsystem dependencies.

The adventure primarily exercises:

General task resolution
Environmental hazards
Exploration
Inventory and treasure acquisition
Combat
Stealth
Social/non-combat interactions
Healing
Death/incapacitation
Monster special abilities
Equipment and armor interactions
Fear/psychological effects
Tactical combat assumptions

Tiwas already possesses a functioning Core Test engine, Opposed Contest system, Location framework, Armor framework, Defense framework, Incapacitation framework, Difficulty framework, Extended Tests, and Healing architecture.

However, the adventure exposes several major gaps:

Gap	SeverityNo completed creature/NPC construction framework (S-12 content)	High
S-3 gated effect contents not enumerated	High
Wound consequence implementation not table-ready	High
Fear/terror condition mapping incomplete	Medium
Environmental hazard content layer missing	Medium
Equipment, weapon, armor, and treasure conversion content absent	Medium
Tactical combat positioning effect catalogue incomplete	Medium
Magic/spell adaptation content absent	Medium

Conclusion: A limited Tiwas playtest version could be run immediately. A complete mechanical adaptation covering all adventure branches cannot presently be executed without additional subsystem and content work.

2. Audit Objective and Method
Objective

Determine whether Tiwas can currently perform every mechanical function required by the adventure, regardless of route frequency or optimal play path.

Method

Every mechanical demand appearing in the adventure was extracted and classified as one of:

Core resolution demand
Combat demand
Exploration demand
Hazard demand
Character state demand
Resource demand
Equipment demand
Content demand

Each demand was mapped against:

Canonical Locked rules
Ruled non-canonical mechanisms
Open systems

Only established mechanics were considered available.

Any unresolved subsystem remained unavailable regardless of design direction.

3. Source Adventure Mechanical Inventory

The adventure uses or assumes the following systems.

Requirement	ExamplesGeneric skill/attribute tests	DX, IQ, ST, Will, Perception, Merchant, Search, Tracking, Climbing, Survival, etc.
Opposed tests	Stealth vs Perception
Difficulty modifiers	DX-5, ST-4, IQ-2, +2 Lockpicking, etc.
Environmental hazards	Hypothermia, cold exposure, cliff falls
Fatigue/resource depletion	FP loss from exertion
HP loss	Combat, falls, wounds, cold
Healing	First Aid, Physician
Death/incapacitation	Falling unconscious and dying
Monster combat	Ice Troll, Blood Man
Initiative/tactical combat assumptions	Battle maps, starting positions
Fear effects	Fright Checks
Stealth	Sneaking past troll
Search/discovery	Hidden treasure
Movement challenges	Climbing, traversal
Equipment usage	Shields, weapons, crossbow
Weapon differentiation	Mace, dagger, sword, shield, crossbow
Armor interaction	DR values
Monster special abilities	Regeneration, Blood Seep, Night Vision
Conditions	Ambushed, Darkness
Inventory/loot	Numerous treasure items
Merchant valuation	Sale values
Magic	Pregenerated spellcaster and enchanted items
NPC rescue	Injured hunter
Extended tasks	Digging through ice, searching areas

Sources throughout adventure.

4. System-by-System Tiwas Compatibility Assessment
4.1 General Skill Resolution
Adventure Requirement

Large number of ordinary skill and attribute tests.

Tiwas Capability

All are replaceable by ordinary Tiwas Core Tests.

Status
Assessment	ResultCapability exists	Yes
Authority	Canonical
Readiness	Playtestable Now

Relevant rules: DEC-006 Core Test, DEC-001 d100 resolution.

4.2 Difficulty Modifiers
Adventure Requirement

Frequent ± modifiers and attribute reductions.

Examples:

DX-5
ST-4
IQ-2
Lockpicking +2
Tiwas Capability

Difficulty grades with effective-Skill modification.

Status
Assessment	ResultCapability exists	Yes
Authority	Non-canonical ruling
Readiness	Playtestable Now

DEC-063 to DEC-066.

4.3 Opposed Resolution
Adventure Requirement

Stealth vs troll perception.

Tiwas Capability

S-1 Universal Opposed Contest.

Status
Assessment	ResultCapability exists	Yes
Authority	Canonical
Readiness	Playtestable Now

DEC-013.

4.4 Physical Hazards
Adventure Requirement
Falls
Climbing failures
Ice
Environmental injuries
Tiwas Capability

Hazards can use ordinary Core Tests.

Non-attack location generation also exists.

Status
Assessment	ResultCapability exists	Mostly
Authority	Mixed
Readiness	Adaptation Mapping Required

Hazard resolution exists, but damage content values require conversion. DEC-037.

4.5 Combat
Adventure Requirement

Direct melee combat with multiple monsters.

Tiwas Capability

Combat supports:

Core Tests
Opposed contests
Effects
Defense
Armor
Injuries
Status
Assessment	ResultCapability exists	Partial
Authority	Mixed
Readiness	Design-Stage Dependency

Major blocker:

S-3 effect-content catalogue remains incomplete. Many combat outcomes depend on unspecified effects.

4.6 Armor
Adventure Requirement

DR, protection, armor interaction.

Tiwas Capability

Armor subsystem exists.

Status
Assessment	ResultCapability exists	Yes
Authority	Ruled
Readiness	Playtestable Now

DEC-058 to DEC-062.

4.7 Active Defense
Adventure Requirement

Combat implicitly assumes avoidance/parrying/dodging.

Tiwas Capability

S-6 Active Defense.

Status
Assessment	ResultCapability exists	Yes
Authority	Ruled
Readiness	Playtestable Now

DEC-044 to DEC-050.

4.8 Wounds and Injury
Adventure Requirement

Serious injury, long-term injury, monster attacks.

Tiwas Capability

Wounds exist.

Issue

Actual wound consequences remain non-table-ready.

Status
Assessment	ResultCapability exists	Incomplete
Authority	Partial
Readiness	Design-Stage Dependency

OPEN-007 remains non-table-ready.

4.9 Death and Incapacitation
Adventure Requirement

Many possible death routes.

Tiwas Capability

Directly supported.

Status
Assessment	ResultCapability exists	Yes
Authority	Ruled
Readiness	Playtestable Now

DEC-052 to DEC-057.

4.10 Healing
Adventure Requirement

First Aid and Physician recovery.

Tiwas Capability

S-11 Healing.

Status
Assessment	ResultCapability exists	Yes
Authority	Ruled
Readiness	Playtestable Now

DEC-071 to DEC-074.

4.11 Fear Effects
Adventure Requirement

Explicit Fright Checks.

Tiwas Capability

No complete fear subsystem appears in corpus.

Status
Assessment	ResultCapability exists	No complete subsystem
Authority	None
Readiness	Missing Subsystem

Adventure requires fear mechanics. Tiwas currently provides no identified fear-condition framework.

4.12 Conditions
Adventure Requirement

Darkness, fear, ambushed status, injuries.

Tiwas Capability

Condition concept exists.

Issue

Condition catalogue incomplete.

Status
Assessment	ResultCapability exists	Partial
Readiness	Design-Stage Dependency

S-3 condition-content enumeration unfinished.

4.13 Stealth
Adventure Requirement

Sneaking and detection.

Tiwas Capability

Core tests + S-1.

Status

Playtestable Now.

4.14 Extended Tasks
Adventure Requirement

Searching, digging, prolonged effort.

Tiwas Capability

S-9/S-10 Extended Tests.

Status

Playtestable Now.

4.15 Resource Exhaustion
Adventure Requirement

Fatigue expenditure.

Tiwas Capability

Physical Energy already exists as universal expenditure economy.

Status

Adaptation Mapping Required.

FP can map to Physical Energy, but adventure-specific conversion must be authored.

4.16 Monsters
Adventure Requirement

Ice Troll and Blood Man.

Tiwas Capability

No finalized creature implementation content.

Status
Assessment	ResultCapability exists	Not sufficiently
Readiness	Design-Stage Dependency

S-12 remains content-authoring work.

4.17 Magic
Adventure Requirement

Spells, enchanted dagger, magical effects.

Tiwas Capability

No finished magic subsystem in corpus.

Status
Assessment	ResultCapability exists	Not established
Readiness	Missing Subsystem

Adventure can be run without mage character, but the adventure itself assumes magical content exists.

5. Playtestability Matrix
Requirement	StatusCore resolution	Playtestable Now
Difficulty	Playtestable Now
Opposed contests	Playtestable Now
Search	Playtestable Now
Climbing	Playtestable Now
Social interactions	Playtestable Now
Extended tasks	Playtestable Now
Armor	Playtestable Now
Defense	Playtestable Now
Incapacitation	Playtestable Now
Healing	Playtestable Now
Hazard resolution	Adaptation Mapping Required
Resource exhaustion mapping	Adaptation Mapping Required
Treasure conversion	Adaptation Mapping Required
Monster construction	Design-Stage Dependency
Combat effects	Design-Stage Dependency
Wound consequences	Design-Stage Dependency
Tactical positioning effects	Design-Stage Dependency
Fear mechanics	Missing Subsystem
Magic subsystem	Missing Subsystem
6. Missing / Design-Stage Dependencies
High-Severity
Dependency	ImpactS-3 effect content enumeration	Central combat functionality
OPEN-007 wound consequences	Injury meaning unclear
Creature implementation content	Monsters cannot be authored consistently
Medium-Severity
Dependency	ImpactFear subsystem	Multiple scenes require it
Magic subsystem	Adventure assumes magical artifacts/spells
Environmental hazard content	Cold exposure not fully mapped
7. Adventure Path Dependency Analysis
Minimal Viable Route

A player can:

Travel
Search
Climb
Sneak
Fight
Heal
Collect treasure

using existing Tiwas systems.

Therefore a reduced adventure playtest is presently feasible.

Full Mechanical Coverage Route

Requires:

Troll combat
Blood Man combat
Fear checks
Monster special abilities
Wound effects
Location interactions
Armor interactions
Enchanted items
Spellcasting assumptions

This route encounters unresolved dependencies.

8. Tiwas Readiness Assessment
Area	ReadinessExploration	High
Task resolution	High
Opposed actions	High
Difficulty framework	High
Survival challenges	Medium
Combat	Medium
Injury system	Medium-Low
Creature support	Low
Fear mechanics	Low
Magic support	Low

Overall readiness:

Partially Ready.

The adventure successfully stress-tests many mature Tiwas systems but also reveals that combat content and creature support are less complete than the underlying engine architecture.

9. Development Priorities Exposed by the Adventure
Priority 1
Complete S-3 Effect Catalogue

This is the single largest combat blocker.

Without a complete effect inventory, many combat outcomes remain undefined.

Priority 2
Complete OPEN-007 Wound Consequences

The adventure repeatedly tests injury and recovery loops.

Wounds exist; consequences do not yet have table-ready implementation.

Priority 3
Establish Practical Creature Authoring Framework

The adventure immediately requires:

Ice Troll
Blood Man
Injured NPC
Potential future creatures

S-12 content capability is therefore directly exposed.

Priority 4
Fear / Horror Condition System

The adventure contains explicit fright events and horror encounters.

Priority 5
Magic and Special Ability Architecture

Not required for a stripped-down playtest, but required for full benchmark parity.

10. Conclusions

Beyond the Vale of Madness is a useful readiness benchmark because it exercises considerably more than simple dungeon exploration. It stresses combat, hazards, injuries, healing, creatures, special abilities, fear, inventory, and environmental survival.

What Tiwas can already do:

Core task resolution
Difficulty handling
Opposed contests
Exploration
Search
Climbing
Healing
Armor interactions
Active defense
Incapacitation/death
Extended tasks

What still blocks a full adaptation:

Complete combat effect catalogue
Finished wound-consequence implementation
Creature content framework
Fear subsystem
Magic subsystem

Therefore:

The adventure is partially playtestable now, but not fully benchmark-playtestable across all mechanical branches without additional Tiwas subsystem completion and adaptation-content work.

11. Source and Evidence Register
Source	UsageBeyond-the-Vale-of-Madness-GURPS.pdf	Adventure mechanical inventory, encounters, hazards, monsters, fear checks, combat assumptions.
Tiwas-Alpha-Playtest-Corpus-2026-09-01.md	Canonical and ruled subsystem status, readiness classification, dependency identification.
12. Explicit Assumptions / Unresolved Questions
Every GURPS skill and attribute check was treated as a Tiwas Core Test per audit instructions.
No attempt was made to preserve GURPS-specific procedures.
The audit assumes adventure monster abilities must be represented mechanically, not abstracted away.
Fear mechanics were treated as requiring a dedicated system because the adventure explicitly invokes Fright Checks.
Magic was treated as required because the adventure includes magical characters, enchanted equipment, and GURPS Magic support.
OPEN-007 remains non-table-ready and therefore unavailable for dependable benchmark play.
S-3 gated effect contents remain incompletely enumerated and were therefore treated as unavailable.
S-12 creature-content authoring remains unresolved enough that specific monster implementations were treated as adaptation blockers.