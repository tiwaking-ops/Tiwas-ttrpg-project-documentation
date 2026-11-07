import csv
import json
from tiwas_bargle_playtest import (
    make_character, core_test, run_exchange, declare_effect_rowan,
    declare_effect_bargle, apply_prone_penalty, clear_prone_if_present, rng,
)

rolls_log = []
effects_log = []
healing_log = []

# --- Character construction (attributes exactly as in the written module) --

rowan = make_character(
    "Rowan",
    body_attrs=dict(bpp=58, bps=52, bpe=47, bpx=40, bsp=61, bss=55, bse=50, bsx=38,
                     bep=60, bes=53, bee=57, bex=44),
    mind_attrs=dict(mpp=42, mps=45, mpe=50, mpx=33, msp=48, mss=55, mse=40, msx=46,
                     mep=51, mes=43, mee=49, mex=47),
    skills={
        "Attack": {"tier": 1, "attrs": ["bpp"], "domain": "PE", "signature": False, "start_mode": "half"},
        "Defense": {"tier": 1, "attrs": ["bss"], "domain": "PE", "signature": False, "start_mode": "half"},
        "Perception": {"tier": 1, "attrs": ["mss"], "domain": "MP", "signature": False, "start_mode": "half"},
        "Stealth": {"tier": 1, "attrs": ["bsp"], "domain": "PE", "signature": False, "start_mode": "half"},
    },
    gear=[{"name": "Shortsword", "tags": ["slot:main_hand", "state:held", "offense:melee", "damage:slashing", "handling:light"]},
          {"name": "Leather Armor", "tags": ["slot:body", "state:worn", "defense:armor"]}],
    is_pc_like=True,
)

aleena = make_character(
    "Aleena",
    body_attrs=dict(bpp=45, bps=40, bpe=50, bpx=48, bsp=42, bss=47, bse=44, bsx=41,
                     bep=55, bes=46, bee=58, bex=50),
    mind_attrs=dict(mpp=50, mps=48, mpe=62, mpx=44, msp=46, mss=50, mse=43, msx=49,
                     mep=60, mes=55, mee=65, mex=52),
    skills={
        "Devotion": {"tier": 1, "attrs": ["mee"], "domain": "MP", "signature": False, "start_mode": "half"},
        "Smite": {"tier": 1, "attrs": ["bep"], "domain": "PE", "signature": False, "start_mode": "half"},
        "Defense": {"tier": 1, "attrs": ["bss"], "domain": "PE", "signature": False, "start_mode": "half"},
    },
    gear=[{"name": "Mace", "tags": ["slot:main_hand", "state:held", "offense:melee", "damage:bludgeoning", "handling:light"]},
          {"name": "Holy Vestments", "tags": ["slot:body", "state:worn"]}],
    is_pc_like=True,  # GM Fiat, DEC-130, per the written module's Round-1 Exchange-3 ruling
)

goblin = make_character(
    "Goblin",
    body_attrs=dict(bpp=40, bps=38, bpe=30, bpx=25, bsp=45, bss=48, bse=35, bsx=30,
                     bep=32, bes=36, bee=34, bex=28),
    mind_attrs=dict(mpp=22, mps=28, mpe=20, mpx=15, msp=25, mss=35, mse=24, msx=18,
                     mep=20, mes=22, mee=25, mex=19),
    skills={
        "Crude Attack": {"tier": 1, "attrs": ["bpp"], "domain": "PE", "signature": True, "start_mode": "full"},
        "Defense": {"tier": 1, "attrs": ["bss"], "domain": "PE", "signature": False, "start_mode": "half"},
        "Trip": {"tier": 2, "attrs": ["bsp", "bss"], "domain": "PE", "signature": True, "start_mode": "full"},
    },
    gear=[{"name": "Rusty Dagger", "tags": ["slot:main_hand", "state:held", "offense:melee", "damage:piercing", "handling:light"]}],
    is_pc_like=False,
)

bargle = make_character(
    "Bargle",
    body_attrs=dict(bpp=35, bps=32, bpe=30, bpx=44, bsp=40, bss=46, bse=38, bsx=42,
                     bep=33, bes=35, bee=37, bex=40),
    mind_attrs=dict(mpp=68, mps=65, mpe=60, mpx=55, msp=58, mss=52, mse=50, msx=48,
                     mep=62, mes=57, mee=55, mex=50),
    skills={
        "Bolt": {"tier": 2, "attrs": ["mpp", "mps"], "domain": "MP", "signature": True, "start_mode": "full"},
        "Defense": {"tier": 1, "attrs": ["bss"], "domain": "PE", "signature": False, "start_mode": "half"},
        "Beguile": {"tier": 1, "attrs": ["mpx"], "domain": "MP", "signature": False, "start_mode": "half"},
    },
    gear=[{"name": "Gnarled Wand", "tags": ["slot:main_hand", "state:held", "offense:ranged", "damage:electric"]},
          {"name": "Traveling Robes", "tags": ["slot:body", "state:worn"]}],
    is_pc_like=False,
)

exch_counter = [1]


def snapshot(char):
    return {
        "name": char["name"], "hp": char["hp"], "hp_max": char["derived"]["HP"],
        "pe": char["pools"]["PE"], "pe_max": char["derived"]["PE"],
        "mp": char["pools"]["MP"], "mp_max": char["derived"]["MP"],
        "skills": {n: {"tier": s["tier"], "cap": s["cap"], "current": s["current"]}
                   for n, s in char["skills"].items()},
        "wounds": char["wounds"], "conditions": char["conditions"],
        "advanced_skills_created": char["advanced_skills_created"],
        "general_xp": char["general_xp"], "incapacitated": char["incapacitated"],
    }


initial_state = {c["name"]: snapshot(c) for c in (rowan, aleena, goblin, bargle)}

# ---------------------------------------------------------------------------
# Scene 2 -- The Goblin's Trap
# DEC-095 turn order: Rowan(166) > Aleena(133) > Goblin(128)
# DEC-106: Goblin has two legal combat actions (Crude Attack, Trip) and no GM
# is present in this automated run -> fires BOTH each of its own turns.
# ---------------------------------------------------------------------------

rowan_powerstrike_hits = [0]

def rowan_offense_action(target, scene, rnd):
    skill_name = "Power Strike" if "Power Strike" in rowan["skills"] else "Attack"
    tier = rowan["skills"][skill_name]["tier"]
    if skill_name == "Power Strike":
        rowan_powerstrike_hits[0] += 1
        effect = declare_effect_rowan(rowan_powerstrike_hits[0], tier)
    else:
        effect = "injury"
    saved = apply_prone_penalty(rowan, skill_name)
    run_exchange(rowan, skill_name, target, "Defense", scene, rnd,
                 exch_counter, effect, rolls_log, effects_log)
    if saved is not None:
        rowan["skills"][skill_name]["current"] = saved
    clear_prone_if_present(rowan)


round_no = 0
while goblin["hp"] > 0 and rowan["hp"] > 0 and round_no < 60:
    round_no += 1
    # Rowan's turn
    if rowan["hp"] > 0 and goblin["hp"] > 0:
        rowan_offense_action(goblin, "Scene2", round_no)
    # Aleena's turn
    if aleena["hp"] > 0 and goblin["hp"] > 0:
        run_exchange(aleena, "Smite", goblin, "Defense", "Scene2", round_no,
                     exch_counter, "injury", rolls_log, effects_log)
    # Goblin's turn: DEC-106 multi-attack, highest Cap first (Trip 46 > Crude Attack 40)
    if goblin["hp"] > 0 and rowan["hp"] > 0:
        run_exchange(goblin, "Trip", rowan, "Defense", "Scene2", round_no,
                     exch_counter, "trip", rolls_log, effects_log)
    if goblin["hp"] > 0 and rowan["hp"] > 0:
        run_exchange(goblin, "Crude Attack", rowan, "Defense", "Scene2", round_no,
                     exch_counter, "injury", rolls_log, effects_log)

scene2_result = {
    "rounds": round_no,
    "goblin_hp_final": goblin["hp"],
    "rowan_hp_final": rowan["hp"],
    "outcome": "Goblin defeated" if goblin["hp"] <= 0 else (
        "Rowan incapacitated" if rowan["hp"] <= 0 else "Round cap reached, unresolved"),
}

# ---------------------------------------------------------------------------
# Interlude -- Aleena's Aid (S-11 Extended Test healing on Rowan)
# DEC-071/073/067/068/070: explicit Skill Test, Extended Test instance,
# Margin-accumulation, neutral failures, GM-set target (here: 40 Margin).
# ---------------------------------------------------------------------------

HEALING_TARGET = 40
running_margin = 0
interval = 0
while running_margin < HEALING_TARGET and interval < 30:
    interval += 1
    result = core_test(aleena, "Devotion", healing_log, "Interlude", interval, 0, "healer")
    if result["success"]:
        running_margin += result["margin"]

hp_restored = min(running_margin, aleena["derived"]["HP"])  # sanity clamp only
rowan["hp"] = min(rowan["derived"]["HP"], rowan["hp"] + running_margin)

interlude_result = {
    "intervals": interval, "final_margin_total": running_margin,
    "target": HEALING_TARGET, "hp_restored_to_rowan": running_margin,
    "rowan_hp_after": rowan["hp"],
}

# ---------------------------------------------------------------------------
# Scene 3 -- Bargle's Ambuscade
# DEC-095 turn order: Rowan(166) > Aleena(133) > Bargle(124)
# Bargle has one legal combat action (Bolt) -> no multi-attack (DEC-106(5)/(1)).
# Targeting convention: Bargle alternates targets by round parity.
# ---------------------------------------------------------------------------

bargle_hits = [0]
round_no3 = 0
while bargle["hp"] > 0 and (rowan["hp"] > 0 or aleena["hp"] > 0) and round_no3 < 80:
    round_no3 += 1
    if rowan["hp"] > 0 and bargle["hp"] > 0:
        rowan_offense_action(bargle, "Scene3", round_no3)
    if aleena["hp"] > 0 and bargle["hp"] > 0:
        run_exchange(aleena, "Smite", bargle, "Defense", "Scene3", round_no3,
                     exch_counter, "injury", rolls_log, effects_log)
    if bargle["hp"] > 0:
        target = aleena if (round_no3 % 2 == 0 and aleena["hp"] > 0) else rowan
        if target["hp"] <= 0:
            target = aleena if target is rowan and aleena["hp"] > 0 else rowan
        if target["hp"] > 0:
            def_skill = "Iron Faith" if ("Iron Faith" in target["skills"] and
                                          target["skills"]["Iron Faith"]["current"] >
                                          target["skills"]["Defense"]["current"]) else "Defense"
            bargle_hits[0] += 1
            effect = declare_effect_bargle(bargle_hits[0])
            run_exchange(bargle, "Bolt", target, def_skill, "Scene3", round_no3,
                         exch_counter, effect, rolls_log, effects_log)

scene3_result = {
    "rounds": round_no3,
    "bargle_hp_final": bargle["hp"],
    "rowan_hp_final": rowan["hp"],
    "aleena_hp_final": aleena["hp"],
    "outcome": "Bargle incapacitated (DEC-052)" if bargle["hp"] <= 0 else (
        "Party incapacitated" if rowan["hp"] <= 0 and aleena["hp"] <= 0 else
        "Round cap reached, unresolved"),
}

final_state = {c["name"]: snapshot(c) for c in (rowan, aleena, goblin, bargle)}

# ---------------------------------------------------------------------------
# Write logs
# ---------------------------------------------------------------------------

roll_fields = ["scene", "round", "exch_id", "actor", "role", "skill", "skill_tier",
               "skill_value_at_roll", "roll", "success", "margin", "cost", "overflow",
               "failure_xp", "skill_value_after", "is_double", "advanced_skill_created",
               "pool_domain", "pool_after_recovery", "hp_after"]

effect_fields = ["scene", "round", "exch_id", "attacker", "defender", "atk_skill",
                  "def_skill", "declared_effect", "location_index", "zone", "laterality",
                  "effect_tier", "effect_magnitude", "wound_attribute", "hp_change", "notes"]

with open("/home/claude/tiwas_playtest/tiwas_bargle_playtest_rolls.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=roll_fields)
    w.writeheader()
    for row in rolls_log:
        w.writerow(row)
    for row in healing_log:
        w.writerow(row)

with open("/home/claude/tiwas_playtest/tiwas_bargle_playtest_effects.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=effect_fields)
    w.writeheader()
    for row in effects_log:
        w.writerow(row)

summary = {
    "initial_state": initial_state,
    "scene2_goblin_fight": scene2_result,
    "interlude_healing": interlude_result,
    "scene3_bargle_fight": scene3_result,
    "final_state": final_state,
    "totals": {
        "total_core_tests": len(rolls_log) + len(healing_log),
        "total_exchanges": exch_counter[0] - 1,
        "total_100_fumbles": sum(1 for r in rolls_log + healing_log if r["roll"] == 100),
        "total_doubles": sum(1 for r in rolls_log + healing_log if r["is_double"]),
        "total_advanced_skills_created": sum(1 for r in rolls_log + healing_log
                                              if r["advanced_skill_created"]),
        "total_overflow_events": sum(1 for r in rolls_log + healing_log if r["overflow"] > 0),
        "total_wounds_recorded": len(rowan["wounds"]) + len(aleena["wounds"]) +
                                  len(goblin["wounds"]) + len(bargle["wounds"]),
    },
}

with open("/home/claude/tiwas_playtest/tiwas_bargle_playtest_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print(json.dumps(summary, indent=2))
