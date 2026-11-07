#!/usr/bin/env python3
"""
Tiwas Your First Adventure v0.2 — Fresh Unattended Playtest Execution
Grok 4.5 — 2026-09-14
RNG: random.SystemRandom() only. No seed. New entropy.
"""
import random
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional
from copy import deepcopy
import json

rng = random.SystemRandom()

# ============================================================
# Helpers
# ============================================================
def d100() -> int:
    return rng.randint(1, 100)

def zero_step(natural: int) -> int:
    """Canonical §14.1 verbatim"""
    if natural == 100:
        return 100
    tens = natural // 10
    units = natural % 10
    return units * 10 + tens

def quartile(li: int) -> str:
    if 1 <= li <= 25: return "Legs"
    if 26 <= li <= 50: return "Arms"
    if 51 <= li <= 75: return "Torso"
    return "Head"

def side(li: int) -> str:
    return "Left" if (li % 2 == 1) else "Right"

# ============================================================
# Character
# ============================================================
@dataclass
class Char:
    name: str
    # Body 12
    bpp:int; bps:int; bpe:int; bpx:int
    bsp:int; bss:int; bse:int; bsx:int
    bep:int; bes:int; bee:int; bex:int
    # Mind 12
    mpp:int; mps:int; mpe:int; mpx:int
    msp:int; mss:int; mse:int; msx:int
    mep:int; mes:int; mee:int; mex:int
    # Derived (locked from module)
    hp: int
    max_hp: int
    mp: int
    max_mp: int
    pe: int
    max_pe: int
    speed: int
    er: int   # Body recovery
    mr: int   # Mind recovery
    movement: int
    skills: Dict[str, dict] = field(default_factory=dict)
    wounds: List[dict] = field(default_factory=list)
    conditions: List[dict] = field(default_factory=list)
    general_xp: int = 0
    tags: List[str] = field(default_factory=list)

    def body_wound(self, attr: str, mag: int, loc: str, side: str):
        old = getattr(self, attr)
        setattr(self, attr, max(1, old - mag))
        self.max_hp = max(1, self.max_hp - mag)
        self.hp = min(self.hp, self.max_hp)
        self.wounds.append({"domain":"Body","attr":attr,"mag":mag,"loc":loc,"side":side})
        # Cap updates for skills based on that attr are approximate; current stays

    def mind_wound(self, attr: str, mag: int, loc: str, side: str):
        old = getattr(self, attr)
        setattr(self, attr, max(1, old - mag))
        self.max_mp = max(1, self.max_mp - mag)
        self.mp = min(self.mp, self.max_mp)
        self.wounds.append({"domain":"Mind","attr":attr,"mag":mag,"loc":loc,"side":side})

# ============================================================
# Ledger
# ============================================================
LEDGER = []   # every d100 with mapping
TXNS = []     # full transaction rows

def log_roll(scene: str, rnd: str, actor: str, skill: str, roll: int, skill_val: int, note: str = ""):
    entry = f"{scene}|{rnd}|{actor}|{skill}|roll={roll}|vs={skill_val}|{note}"
    LEDGER.append(entry)
    return entry

# ============================================================
# Core Test (9-step DEC-006 order)
# ============================================================
def core_test(c: Char, skill_name: str, scene: str, rnd: str, forced_roll: Optional[int] = None) -> dict:
    sk = c.skills[skill_name]
    val = sk["current"]
    domain = sk["domain"]
    roll = forced_roll if forced_roll is not None else d100()
    log_roll(scene, rnd, c.name, skill_name, roll, val)

    # 1-2 Cost
    cost = roll
    overflow = 0
    if domain == "PE":
        if c.pe < cost:
            overflow = cost - c.pe
            c.pe = 0
            c.hp = max(-999, c.hp - overflow)  # DEC-108 negative persists
        else:
            c.pe -= cost
    else:
        if c.mp < cost:
            overflow = cost - c.mp
            c.mp = 0
            c.hp = max(-999, c.hp - overflow)
        else:
            c.mp -= cost

    # 3-4 Outcome / Margin
    success = (roll <= val) and (roll != 100)  # 100 always fails
    margin = max(0, val - roll) if success else 0

    # 5 Failure XP + cascade
    fail_xp = 0
    cascade_log = ""
    if not success:
        fail_xp = roll - val
        pool = fail_xp
        steps = []
        while pool >= sk["current"] and sk["current"] < sk["cap"]:
            old = sk["current"]
            sk["current"] += 1
            pool -= old
            steps.append(f"{old}->{sk['current']}")
        c.general_xp += pool
        cascade_log = f"cascade[{','.join(steps)}] rem={pool}->GXP" if steps else f"rem={pool}->GXP"

    # 6 Recovery
    if domain == "PE":
        rec = c.er // 2
        c.pe = min(c.max_pe, c.pe + rec)
    else:
        rec = c.mr // 2
        c.mp = min(c.max_mp, c.mp + rec)

    txn = {
        "scene": scene, "rnd": rnd, "actor": c.name, "skill": skill_name,
        "roll": roll, "skill_val": val, "success": success, "margin": margin,
        "cost": cost, "overflow": overflow, "fail_xp": fail_xp,
        "cascade": cascade_log, "rec": rec,
        "post_pe": c.pe, "post_mp": c.mp, "post_hp": c.hp
    }
    TXNS.append(txn)
    return txn

# ============================================================
# S-1 Margin Contest
# ============================================================
def s1(attacker: Char, atk_sk: str, defender: Char, def_sk: str,
       scene: str, rnd: str, max_rerolls: int = 3) -> Tuple[bool, int, int, int]:
    """Returns (attacker_wins, atk_margin, def_margin, atk_natural_roll)"""
    attempts = 0
    while True:
        attempts += 1
        atk = core_test(attacker, atk_sk, scene, rnd)
        dfn = core_test(defender, def_sk, scene, rnd)
        if atk["margin"] > dfn["margin"]:
            return True, atk["margin"], dfn["margin"], atk["roll"]
        if dfn["margin"] > atk["margin"]:
            return False, atk["margin"], dfn["margin"], atk["roll"]
        # Tie
        if attempts > max_rerolls:
            return False, 0, 0, atk["roll"]  # defense holds
        # else reroll both

# ============================================================
# Init from module v0.2 verbatim
# ============================================================
def init():
    chars = {}
    # Rowan
    r = Char("Rowan",
        58,52,47,40, 61,55,50,38, 60,53,57,44,
        42,45,50,33, 48,55,40,46, 51,43,49,47,
        615,615, 549,549, 170,170, 166, 113,94, 7)
    r.skills = {
        "Attack":     {"tier":1,"cap":58,"start":29,"current":29,"domain":"PE"},
        "Defense":    {"tier":1,"cap":55,"start":27,"current":27,"domain":"PE"},
        "Perception": {"tier":1,"cap":55,"start":27,"current":27,"domain":"MP"},
        "Stealth":    {"tier":1,"cap":61,"start":30,"current":30,"domain":"PE"},
        "Composure":  {"tier":1,"cap":47,"start":23,"current":23,"domain":"MP"},
    }
    r.tags = ["reaction:vigilant"]
    chars["Rowan"] = r

    a = Char("Aleena",
        45,40,50,48, 42,47,44,41, 55,46,58,50,
        50,48,62,44, 46,50,43,49, 60,55,65,52,
        566,566, 624,624, 159,159, 133, 101,115, 5)
    a.skills = {
        "Devotion": {"tier":1,"cap":65,"start":32,"current":32,"domain":"MP"},
        "Smite":    {"tier":1,"cap":55,"start":27,"current":27,"domain":"PE"},
        "Defense":  {"tier":1,"cap":47,"start":23,"current":23,"domain":"PE"},
    }
    chars["Aleena"] = a

    g = Char("Goblin",
        40,38,30,25, 45,48,35,30, 32,36,34,28,
        22,28,20,15, 25,35,24,18, 20,22,25,19,
        421,421, 273,273, 102,102, 128, 68,42, 6)
    g.skills = {
        "Crude Attack": {"tier":1,"cap":40,"start":40,"current":40,"domain":"PE"},
        "Defense":      {"tier":1,"cap":48,"start":24,"current":24,"domain":"PE"},
        "Trip":         {"tier":2,"cap":46,"start":46,"current":46,"domain":"PE"},
    }
    chars["Goblin"] = g

    s = Char("Rattlesnake",
        30,28,24,20, 60,58,55,45, 22,25,24,26,
        15,18,14,12, 30,40,28,20, 16,18,15,17,
        417,417, 243,243, 71,71, 173, 47,34, 7)
    s.skills = {
        "Venomous Bite": {"tier":2,"cap":59,"start":59,"current":59,"domain":"PE"},
        "Defense":       {"tier":1,"cap":58,"start":29,"current":29,"domain":"PE"},
        "Stealth":       {"tier":1,"cap":60,"start":30,"current":30,"domain":"PE"},
    }
    chars["Rattlesnake"] = s

    gh = Char("Ghoul",
        42,36,40,30, 50,52,44,38, 40,42,44,36,
        20,25,18,16, 28,30,22,20, 18,22,20,21,
        494,494, 260,260, 126,126, 146, 82,40, 6)
    gh.skills = {
        "Claw":        {"tier":2,"cap":39,"start":39,"current":39,"domain":"PE"},
        "Grapple":     {"tier":2,"cap":46,"start":46,"current":46,"domain":"PE"},
        "Defense":     {"tier":1,"cap":52,"start":26,"current":26,"domain":"PE"},
        "Desecration": {"tier":2,"cap":22,"start":22,"current":22,"domain":"MP"},
    }
    chars["Ghoul"] = gh

    b = Char("Bargle",
        35,32,30,44, 40,46,38,42, 33,35,37,40,
        68,65,60,55, 58,52,50,48, 62,57,55,50,
        452,452, 680,680, 105,105, 124, 68,119, 5)
    b.skills = {
        "Bolt":    {"tier":2,"cap":66,"start":66,"current":66,"domain":"MP"},
        "Defense": {"tier":1,"cap":46,"start":23,"current":23,"domain":"PE"},
        "Beguile": {"tier":1,"cap":55,"start":27,"current":27,"domain":"MP"},
    }
    chars["Bargle"] = b
    return chars

# ============================================================
# MAIN RUN
# ============================================================
def main():
    chars = init()
    rowan = chars["Rowan"]
    aleena = chars["Aleena"]
    goblin = chars["Goblin"]
    snake = chars["Rattlesnake"]
    ghoul = chars["Ghoul"]
    bargle = chars["Bargle"]

    print("=== FRESH RUN START ===")
    print(f"RNG identity: SystemRandom, first 3 rolls probe: {[d100() for _ in range(3)]}")

    # ---------------------------------------------------------
    # SCENE 1 — Goblin (budget 6)
    # ---------------------------------------------------------
    print("\n=== SCENE 1: Goblin on the Road ===")
    # Mandatory fixed Perception teaching beat
    print("--- Fixed Perception Teaching Beat (roll=100) ---")
    # Manual fixed because core_test would roll
    sk = rowan.skills["Perception"]
    roll = 100
    log_roll("Sc1", "Pre", "Rowan", "Perception", 100, 27, "FIXED teaching beat")
    cost = 100
    rowan.mp -= 100  # 549 -> 449
    # Advanced Skill creation (DEC-012 / DEC-140)
    new_cap = (rowan.mss + rowan.mps) // 2  # 50
    rowan.skills["Perception (Advanced)"] = {
        "tier":2, "cap":50, "start":1, "current":1, "domain":"MP"
    }
    # Failure XP 73 cascade on original Perception
    fail_xp = 73
    pool = 73
    steps = []
    while pool >= sk["current"] and sk["current"] < sk["cap"]:
        old = sk["current"]
        sk["current"] += 1
        pool -= old
        steps.append(f"{old}->{sk['current']}")
    rowan.general_xp += pool
    # Recovery
    rec = rowan.mr // 2  # 47
    rowan.mp = min(rowan.max_mp, rowan.mp + rec)  # 496
    TXNS.append({
        "scene":"Sc1","rnd":"Pre","actor":"Rowan","skill":"Perception",
        "roll":100,"skill_val":27,"success":False,"margin":0,
        "cost":100,"overflow":0,"fail_xp":73,
        "cascade":f"cascade[{','.join(steps)}] rem={pool}->GXP",
        "rec":47,"post_pe":rowan.pe,"post_mp":rowan.mp,"post_hp":rowan.hp
    })
    print(f"  Advanced Skill created: Perception (Advanced) T2 Cap50 Start1")
    print(f"  Perception current now {sk['current']}, MP={rowan.mp}")

    # Combat
    for r in range(1, 7):
        print(f"-- Sc1 Round {r} --")
        # Rowan Attack -> Inflict Injury
        wins, am, dm, aroll = s1(rowan, "Attack", goblin, "Defense", "Sc1", f"R{r}")
        if wins:
            injury = am
            goblin.hp -= injury
            print(f"  Rowan wins Injury {injury} -> Goblin HP {goblin.hp}")
        else:
            print(f"  Rowan Attack fails (M{am} vs M{dm})")
        if goblin.hp <= 0:
            print("  Goblin HP<=0 -> incapacitated (secondary end)")
            break
        # Goblin Trip -> Knock Prone
        wins, am, dm, aroll = s1(goblin, "Trip", rowan, "Defense", "Sc1", f"R{r}")
        if wins:
            li = zero_step(aroll)
            loc = quartile(li)
            sd = side(li)
            mag = 3  # T2 shred +1 over T1
            print(f"  Goblin Trip win -> Prone {sd} {loc} Mag{mag} (LI={li})")
            # free stand later (DEC-082)
        else:
            print(f"  Goblin Trip fails")
        if goblin.hp <= 0:
            break
    else:
        print(f"  Round 6 expiry -> Goblin WITHDRAWS (primary D5). HP={goblin.hp}")

    # ---------------------------------------------------------
    # SCENE 2 — Rattlesnake (budget 5, Snake first)
    # ---------------------------------------------------------
    print("\n=== SCENE 2: Rattlesnake ===")
    for r in range(1, 6):
        print(f"-- Sc2 Round {r} (Snake first) --")
        # Snake Venomous Bite -> Wounded
        wins, am, dm, aroll = s1(snake, "Venomous Bite", rowan, "Defense", "Sc2", f"R{r}")
        if wins:
            li = zero_step(aroll)
            loc = quartile(li)
            sd = side(li)
            attr = rng.choice(["bsp", "bss"])
            mag = 3
            rowan.body_wound(attr, mag, loc, sd)
            print(f"  Snake Wounded {sd} {loc} {attr}-{mag} -> Rowan maxHP={rowan.max_hp} HP={rowan.hp}")
        # Rowan Attack
        wins, am, dm, aroll = s1(rowan, "Attack", snake, "Defense", "Sc2", f"R{r}")
        if wins:
            injury = am
            snake.hp -= injury
            print(f"  Rowan Injury {injury} -> Snake HP {snake.hp}")
        if snake.hp <= 0:
            print("  Snake HP<=0")
            break
    else:
        print(f"  Round 5 expiry -> Snake withdraws. HP={snake.hp}")

    # Treasure search (Perception Advanced if present)
    print("--- Treasure Search ---")
    skname = "Perception (Advanced)" if "Perception (Advanced)" in rowan.skills else "Perception"
    # Use original Perception for better chance; Advanced is Start 1
    txn = core_test(rowan, "Perception", "Sc2", "Search")
    pearl = txn["success"]
    print(f"  Search success={pearl} (pearl={'found' if pearl else 'not found'})")

    # ---------------------------------------------------------
    # SCENE 3 — Aleena S-11
    # ---------------------------------------------------------
    print("\n=== SCENE 3: Aleena Healing ===")
    if rowan.hp < rowan.max_hp or rowan.wounds:
        total_m = 0
        for i in range(1, 5):
            txn = core_test(aleena, "Devotion", "Sc3", f"I{i}")
            if txn["success"]:
                total_m += txn["margin"]
        restore = min(total_m, rowan.max_hp - rowan.hp)
        rowan.hp += restore
        print(f"  S-11 total Margin {total_m}, restore {restore} -> Rowan HP {rowan.hp}/{rowan.max_hp}")
        # Wounds remain (separate action)
    else:
        print("  Rowan unharmed at current max -> declined")

    # ---------------------------------------------------------
    # SCENE 4 — Ghoul Turning
    # ---------------------------------------------------------
    print("\n=== SCENE 4: Ghoul Passage ===")
    wins, am, dm, aroll = s1(aleena, "Devotion", ghoul, "Desecration", "Sc4", "Turn")
    if wins:
        print(f"  Turning SUCCESS (M{am} vs M{dm}) -> ghouls withdraw (narrated)")
        fight = False
    else:
        print(f"  Turning FAIL -> fight budget 3")
        fight = True
        for r in range(1, 4):
            print(f"  -- Fight R{r} --")
            # Simplified: Rowan + Aleena vs one Ghoul representative
            wins, am, dm, _ = s1(rowan, "Attack", ghoul, "Defense", "Sc4", f"FR{r}")
            if wins:
                ghoul.hp -= am
                print(f"    Rowan Injury {am} -> Ghoul {ghoul.hp}")
            wins, am, dm, _ = s1(aleena, "Smite", ghoul, "Defense", "Sc4", f"FR{r}")
            if wins:
                ghoul.hp -= am
                print(f"    Aleena Injury {am} -> Ghoul {ghoul.hp}")
            if ghoul.hp <= 0:
                print("    Ghoul pack driven")
                break
        else:
            print("  Round 3 expiry -> pack breaks, party slips past")

    # ---------------------------------------------------------
    # SCENE 5 — Locked Door (bash default)
    # ---------------------------------------------------------
    print("\n=== SCENE 5: Locked Door ===")
    opened = False
    for att in range(1, 4):
        roll = d100()
        effective = rowan.skills["Attack"]["current"] - 15
        log_roll("Sc5", f"Bash{att}", "Rowan", "Attack", roll, effective, "passive-gate")
        cost = roll
        if rowan.pe < cost:
            overflow = cost - rowan.pe
            rowan.pe = 0
            rowan.hp -= overflow
        else:
            rowan.pe -= cost
        rec = rowan.er // 2
        rowan.pe = min(rowan.max_pe, rowan.pe + rec)
        success = roll <= effective
        print(f"  Bash{att}: roll={roll} vs effective {effective} -> {'PASS' if success else 'FAIL'}")
        if success:
            opened = True
            break
    if not opened:
        print("  3 fails -> forced open by exhaustion (narrated)")

    # ---------------------------------------------------------
    # SCENE 6 — Bargle (budget 3 + fork)
    # ---------------------------------------------------------
    print("\n=== SCENE 6: Bargle ===")
    reaction_fired = False
    ending = None
    for r in range(1, 4):
        print(f"-- Sc6 Round {r} --")
        # Rowan Attack
        effect = "Injury" if r < 3 else "ArmorBypass"
        wins, am, dm, aroll = s1(rowan, "Attack", bargle, "Defense", "Sc6", f"R{r}")
        if wins:
            if effect == "ArmorBypass":
                # no-match fallback DEC-030
                injury = am
                bargle.hp -= injury
                print(f"  Rowan ArmorBypass -> fallback Injury {injury} -> Bargle HP {bargle.hp}")
            else:
                bargle.hp -= am
                print(f"  Rowan Injury {am} -> Bargle HP {bargle.hp}")
        # Aleena Smite
        wins, am, dm, aroll = s1(aleena, "Smite", bargle, "Defense", "Sc6", f"R{r}")
        if wins:
            bargle.hp -= am
            print(f"  Aleena Injury {am} -> Bargle HP {bargle.hp}")
        # Bargle Bolt -> Aleena (Wounded)
        wins, am, dm, aroll = s1(bargle, "Bolt", aleena, "Defense", "Sc6", f"R{r}")
        if wins:
            li = zero_step(aroll)
            loc = quartile(li)
            sd = side(li)
            attr = rng.choice(["mpp", "mps"])
            mag = 3
            aleena.mind_wound(attr, mag, loc, sd)
            print(f"  Bargle Wounded {sd} {loc} {attr}-{mag} -> Aleena maxMP={aleena.max_mp}")
            # reaction:vigilant once
            if not reaction_fired and "reaction:vigilant" in rowan.tags:
                reaction_fired = True
                print("  ** reaction:vigilant (DEC-132.B) fires **")
                wins_r, am_r, dm_r, _ = s1(rowan, "Attack", bargle, "Defense", "Sc6", f"R{r}-React")
                if wins_r:
                    bargle.hp -= am_r
                    print(f"  Reaction Injury {am_r} -> Bargle HP {bargle.hp}")
                else:
                    print("  Reaction fails")
        # A4 check
        if aleena.hp <= 0:
            print("  A4: Aleena would cross 0 -> clamp to 1, narrate collapse")
            aleena.hp = 1
        if bargle.hp <= 0:
            print("  Bargle HP<=0 -> ENDING A immediately (D1), fork SKIPPED")
            ending = "A"
            break
    if ending is None:
        # Climax fork
        print("--- Climax Fork: Beguile vs Composure ---")
        wins, am, dm, aroll = s1(bargle, "Beguile", rowan, "Composure", "Sc6", "Fork")
        if wins:
            ending = "B"
            print(f"  Beguile wins (M{am} vs M{dm}) -> ENDING B")
        else:
            ending = "A"
            print(f"  Composure holds -> ENDING A")
            # Decisive exchange
            print("  Decisive exchange:")
            wins, am, dm, aroll = s1(rowan, "Attack", bargle, "Defense", "Sc6", "Decisive")
            if wins:
                bargle.hp = max(0, bargle.hp - am)
                print(f"  Decisive Injury {am} -> Bargle HP {bargle.hp}")
            if bargle.hp <= 0:
                print("  Bargle incapacitated (DEC-052)")
            else:
                print("  Residual / fail -> Bargle escapes wounded (still Ending A)")

    # Final states
    print("\n=== FINAL STATES ===")
    print(f"Rowan: HP={rowan.hp}/{rowan.max_hp} PE={rowan.pe}/{rowan.max_pe} MP={rowan.mp}/{rowan.max_mp}")
    print(f"  Attack={rowan.skills['Attack']['current']} Defense={rowan.skills['Defense']['current']} Perception={rowan.skills['Perception']['current']}")
    print(f"  Wounds={len(rowan.wounds)} GXP={rowan.general_xp}")
    print(f"Aleena: HP={aleena.hp}/{aleena.max_hp} PE={aleena.pe} MP={aleena.mp}/{aleena.max_mp}")
    print(f"Bargle: HP={bargle.hp}/{bargle.max_hp}")
    print(f"Goblin final HP={goblin.hp} Snake={snake.hp}")
    print(f"ENDING = {ending}")
    print(f"reaction_fired = {reaction_fired}")
    print(f"pearl_found = {pearl}")

    # Write artifacts
    with open("/tmp/tiwas_yfa_v02_fresh_ledger.txt", "w") as f:
        f.write("\n".join(LEDGER))
    with open("/tmp/tiwas_yfa_v02_fresh_txns.json", "w") as f:
        json.dump(TXNS, f, indent=2)
    with open("/tmp/tiwas_yfa_v02_fresh_summary.txt", "w") as f:
        f.write(f"ENDING={ending}\n")
        f.write(f"Rowan HP={rowan.hp}/{rowan.max_hp} PE={rowan.pe} MP={rowan.mp}\n")
        f.write(f"Aleena HP={aleena.hp} MP={aleena.mp}/{aleena.max_mp}\n")
        f.write(f"Bargle HP={bargle.hp}\n")
        f.write(f"reaction={reaction_fired} pearl={pearl}\n")
        f.write(f"Ledger lines={len(LEDGER)} Txns={len(TXNS)}\n")

    print(f"\nLedger entries: {len(LEDGER)}")
    print(f"Transactions: {len(TXNS)}")
    print("Files written under /tmp/")

if __name__ == "__main__":
    main()
