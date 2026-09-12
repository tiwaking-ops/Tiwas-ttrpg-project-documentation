#!/usr/bin/env python3
"""
Tiwas TTRPG -- Mirror-Match Combat Stress Test v2 (Rotation Fix)

Addendum to tiwas-playtest-mirror-combat-design-brief-2026-09-10.md (v0.2).
Non-canonical. No DEC assigned. Advisory scaffolding only.

CHANGE FROM v1: offense-skill selection replaced with a fixed round-robin
rotation (Attack -> Grapple -> Trip -> Disarm -> Equipment Damage -> repeat),
advanced once per TURN (not per internal repeat-roll), to eliminate the
single-skill lock-in observed in the prior "highest current value" runs.
Everything else (combat procedure, DEC-103/104/105/014/100/114/030 logic,
combatant baseline) is unchanged from v1.
"""

import csv
import json
from collections import Counter
import random

rng = random.SystemRandom()
DOUBLES = {11, 22, 33, 44, 55, 66, 77, 88, 99, 100}
ROTATION_ORDER = ['Attack', 'Grapple', 'Trip', 'Disarm', 'EquipmentDamage']


def roll_d100():
    return rng.randint(1, 100)


def zero_step(roll):
    if roll == 100:
        return 100
    tens, units = roll // 10, roll % 10
    swapped = units * 10 + tens
    return swapped if swapped != 0 else 100


def zone_of(index):
    if 1 <= index <= 25:
        return 'Legs'
    if 26 <= index <= 50:
        return 'Torso'
    if 51 <= index <= 75:
        return 'Arms'
    if 76 <= index <= 100:
        return 'Head'
    return 'Unknown'


def laterality_of(index):
    return 'Left' if index % 2 == 1 else 'Right'


def resolve_effect_tier_magnitude(atk_tier, def_tier, defender_margin):
    base_mag = atk_tier
    tier = atk_tier
    if atk_tier == def_tier:
        mag = base_mag - 1
    elif def_tier > atk_tier:
        mag = base_mag - (def_tier - atk_tier)
    else:
        mag = base_mag + 1
    mag -= defender_margin
    if mag <= 0:
        tier -= 1
        if tier <= 0:
            return 0, 0
        mag = tier
    return tier, -tier


def inflict_injury_damage(atk_margin, defender_margin):
    dmg = atk_margin - defender_margin
    return dmg if dmg > 0 else 1


class Combatant:
    def __init__(self, name):
        self.name = name
        self.hp = 600
        self.hp_max = 600
        self.pe = 150
        self.pe_max = 150
        self.energy_regen = 100
        self.speed = 150
        self.movement_speed = 6
        self.skills = {
            'Attack':          {'value': 25, 'cap': 50, 'tier': 2},
            'Grapple':         {'value': 25, 'cap': 50, 'tier': 2},
            'Trip':            {'value': 25, 'cap': 50, 'tier': 2},
            'Disarm':          {'value': 25, 'cap': 50, 'tier': 2},
            'EquipmentDamage': {'value': 25, 'cap': 50, 'tier': 2},
            'Defense':         {'value': 25, 'cap': 50, 'tier': 2},
        }
        self.rotation_index = 0  # NEW in v2: round-robin pointer
        self.conditions = []
        self.advanced_skills = []
        self.general_xp = 0
        self.total_failure_xp = 0

    def select_offense_skill_rotation(self):
        """NEW in v2: fixed round-robin, ignores current skill value entirely."""
        skill = ROTATION_ORDER[self.rotation_index % len(ROTATION_ORDER)]
        self.rotation_index += 1
        return skill

    def pay_cost_and_recover(self, roll):
        overflow = 0
        if self.pe >= roll:
            self.pe -= roll
        else:
            overflow = roll - self.pe
            self.pe = 0
            self.hp -= overflow
        recover = self.energy_regen // 2
        self.pe = min(self.pe_max, self.pe + recover)
        return overflow

    def apply_failure_xp_and_pool(self, skill_name, roll, success):
        skill = self.skills[skill_name]
        failure_xp = max(0, roll - skill['value']) if not success else 0
        self.total_failure_xp += failure_xp
        pool = failure_xp
        while pool >= skill['value'] and skill['value'] < skill['cap']:
            pool -= skill['value']
            skill['value'] += 1
        self.general_xp += pool
        return failure_xp

    def check_failed_double(self, skill_name, roll, success):
        if roll in DOUBLES and not success:
            old = self.skills[skill_name]
            new_tier = old['tier'] + 1
            new_name = f"{skill_name}-Adv{len(self.advanced_skills) + 1}(T{new_tier})"
            self.skills[new_name] = {'value': 1, 'cap': 50, 'tier': new_tier}
            self.advanced_skills.append(new_name)
            return new_name
        return None


def core_test(combatant, skill_name):
    roll = roll_d100()
    skill_val = combatant.skills[skill_name]['value']
    success = (roll <= skill_val) and (roll != 100)
    margin = skill_val - roll if success else None
    overflow = combatant.pay_cost_and_recover(roll)
    failure_xp = combatant.apply_failure_xp_and_pool(skill_name, roll, success)
    adv = combatant.check_failed_double(skill_name, roll, success)
    return {'roll': roll, 'skill_val_at_roll': skill_val, 'success': success,
            'margin': margin, 'overflow': overflow, 'failure_xp': failure_xp,
            'advanced_skill_created': adv}


EFFECT_NAME = {'Trip': 'Prone', 'Disarm': 'Disarmed',
               'EquipmentDamage': 'EquipmentDamaged', 'Grapple': 'Grappled'}
DECLARED_NAME = {'Attack': 'Inflict Injury', 'Grapple': 'Impose Condition: Grappled',
                  'Trip': 'Knock Prone', 'Disarm': 'Disarm/Break Hold',
                  'EquipmentDamage': 'Equipment Damage'}


def resolve_exchange(actor, defender, log, ctr, round_num, replicate, max_repeats=50):
    # v2 CHANGE: skill selected ONCE per turn, reused across any internal repeats
    offense_skill = actor.select_offense_skill_rotation()
    repeats = 0
    while True:
        repeats += 1
        ctr[0] += 1
        exch_id = ctr[0]

        atk_res = core_test(actor, offense_skill)
        def_res = core_test(defender, 'Defense')

        if not atk_res['success'] and not def_res['success']:
            outcome = 'repeat-bothfail'
        elif atk_res['success'] and not def_res['success']:
            outcome = 'attacker-wins'
        elif not atk_res['success'] and def_res['success']:
            outcome = 'defender-wins'
        else:
            if atk_res['margin'] > def_res['margin']:
                outcome = 'attacker-wins'
            elif def_res['margin'] > atk_res['margin']:
                outcome = 'defender-wins'
            else:
                outcome = 'repeat-tie'

        effect_declared = ''
        location_index = zone = laterality = ''
        tag_check = ''
        resulting_staterecord = ''

        if outcome == 'attacker-wins':
            mitigation = def_res['margin'] if def_res['success'] else 0
            effect_declared = DECLARED_NAME[offense_skill]

            if offense_skill == 'Attack':
                dmg = inflict_injury_damage(atk_res['margin'], mitigation)
                defender.hp -= dmg
                resulting_staterecord = f"HP -{dmg}"
            else:
                loc_referencing = offense_skill in ('Trip', 'Disarm', 'EquipmentDamage')
                if loc_referencing:
                    location_index = zero_step(atk_res['roll'])
                    zone = zone_of(location_index)
                    laterality = laterality_of(location_index)

                if offense_skill == 'Disarm':
                    match = (zone == 'Arms')
                    tag_check = 'pass' if match else 'fail-and-fall-back'
                elif offense_skill == 'EquipmentDamage':
                    match = zone in ('Arms', 'Torso')
                    tag_check = 'pass' if match else 'fail-and-fall-back'
                else:
                    match = True
                    tag_check = 'n/a'

                if not match:
                    dmg = inflict_injury_damage(atk_res['margin'], mitigation)
                    defender.hp -= dmg
                    resulting_staterecord = f"Fallback HP -{dmg} (Base Inflict Injury, DEC-030)"
                    effect_declared += ' -> FAIL-AND-FALL-BACK -> Inflict Injury'
                else:
                    atk_tier = actor.skills[offense_skill]['tier']
                    def_tier = defender.skills['Defense']['tier']
                    tier, mag = resolve_effect_tier_magnitude(atk_tier, def_tier, mitigation)
                    if tier == 0:
                        resulting_staterecord = 'Negated (Tier reduced to 0)'
                    else:
                        loc_str = f"Location {location_index}({zone}/{laterality}) " if loc_referencing else ''
                        cond_name = EFFECT_NAME[offense_skill]
                        resulting_staterecord = f"{loc_str}Tier-{tier} {cond_name} Magnitude {mag}"
                        defender.conditions.append({
                            'type': cond_name, 'tier': tier, 'magnitude': mag,
                            'location': location_index if loc_referencing else None,
                            'zone': zone if loc_referencing else None,
                            'source_exchange': exch_id,
                        })

        row = {
            'replicate': replicate, 'exchange_#': exch_id, 'round': round_num, 'repeat_seq': repeats,
            'actor': actor.name, 'defender': defender.name,
            'offense_skill_chosen': offense_skill,
            'offense_skill_value_at_roll': atk_res['skill_val_at_roll'],
            'atk_roll': atk_res['roll'], 'def_roll': def_res['roll'],
            'atk_success': atk_res['success'], 'def_success': def_res['success'],
            'atk_margin': atk_res['margin'], 'def_margin': def_res['margin'],
            'outcome': outcome, 'effect_declared': effect_declared,
            'location_index': location_index, 'zone': zone, 'laterality': laterality,
            'tag_check': tag_check, 'resulting_staterecord': resulting_staterecord,
            'hp_alpha_after': alpha.hp, 'hp_beta_after': beta.hp,
            'pe_alpha_after': alpha.pe, 'pe_beta_after': beta.pe,
            'atk_overflow': atk_res['overflow'], 'def_overflow': def_res['overflow'],
            'atk_failure_xp': atk_res['failure_xp'], 'def_failure_xp': def_res['failure_xp'],
            'atk_advanced_skill_created': atk_res['advanced_skill_created'] or '',
            'def_advanced_skill_created': def_res['advanced_skill_created'] or '',
        }
        log.append(row)

        if outcome in ('attacker-wins', 'defender-wins'):
            return outcome
        if repeats >= max_repeats:
            row['outcome'] = outcome + ' [SAFETY-CAP-FORCED-END]'
            return 'defender-wins'


def run_scenario(replicate, max_rounds=500):
    global alpha, beta
    alpha = Combatant('Alpha')
    beta = Combatant('Beta')
    log = []
    ctr = [0]
    round_num = 0
    terminated = False
    victor = cause = None

    while round_num < max_rounds and not terminated:
        round_num += 1
        if alpha.speed == beta.speed:
            while True:
                a_r, b_r = roll_d100(), roll_d100()
                if a_r != b_r:
                    break
            order = [alpha, beta] if a_r > b_r else [beta, alpha]
        else:
            order = sorted([alpha, beta], key=lambda c: -c.speed)

        for actor in order:
            defender = beta if actor is alpha else alpha
            if actor.hp <= 0 or defender.hp <= 0:
                terminated = True
                break
            resolve_exchange(actor, defender, log, ctr, round_num, replicate)
            if alpha.hp <= 0 or beta.hp <= 0:
                terminated = True
                if alpha.hp <= 0 and beta.hp <= 0:
                    victor = 'Simultaneous (both HP<=0)'
                elif alpha.hp <= 0:
                    victor = 'Beta'
                else:
                    victor = 'Alpha'
                cause = 'HP <= 0 (DEC-052 forced incapacitation)'
                break

    if not terminated:
        victor = 'None (round cap reached)'
        cause = f'MAX_ROUNDS safety cap ({max_rounds}) reached'

    outcome_counts = Counter(r['outcome'] for r in log)
    effect_counts = Counter(r['effect_declared'] for r in log if r['effect_declared'])
    tagcheck_counts = Counter(r['tag_check'] for r in log if r['tag_check'])
    skill_choice_counts = Counter(r['offense_skill_chosen'] for r in log)
    adv_created = len(alpha.advanced_skills) + len(beta.advanced_skills)

    # objective coverage flags for this replicate
    obj = {
        '1_melee_exchange': True,
        '2_contest_delta_hp': outcome_counts.get('attacker-wins', 0) > 0,
        '3_effect_tier_magnitude': any(k not in ('Inflict Injury',) and 'FAIL-AND-FALL-BACK' not in k
                                        for k in effect_counts if k != 'Inflict Injury'),
        '4_skill_tier_shred': None,  # same trigger as (3); filled below
        '5_zero_step_location': any(r['location_index'] != '' for r in log),
        '6_tag_location_gating': len(tagcheck_counts) > 0 and ('pass' in tagcheck_counts or 'fail-and-fall-back' in tagcheck_counts),
        '7_grappled_imposition': 'Impose Condition: Grappled' in effect_counts,
        '7_breakhold_escape': False,  # structurally excluded, per this scenario's scope
        '8_wound_target_selection': False,  # structurally unreachable, no Wound pairing exists
        '9_advanced_skill_creation': adv_created > 0,
        '10_armor_bypass': None,  # intentionally out of scope
    }
    obj['4_skill_tier_shred'] = obj['3_effect_tier_magnitude']

    summary = {
        'replicate': replicate, 'total_rounds': round_num, 'total_exchanges_logged': len(log),
        'victor': victor, 'termination_cause': cause,
        'alpha_final_hp': alpha.hp, 'beta_final_hp': beta.hp,
        'alpha_final_pe': alpha.pe, 'beta_final_pe': beta.pe,
        'alpha_skills': {k: v['value'] for k, v in alpha.skills.items()},
        'beta_skills': {k: v['value'] for k, v in beta.skills.items()},
        'alpha_advanced_skills': alpha.advanced_skills, 'beta_advanced_skills': beta.advanced_skills,
        'alpha_conditions_ever': alpha.conditions, 'beta_conditions_ever': beta.conditions,
        'alpha_total_failure_xp': alpha.total_failure_xp, 'beta_total_failure_xp': beta.total_failure_xp,
        'alpha_general_xp': alpha.general_xp, 'beta_general_xp': beta.general_xp,
        'outcome_counts': dict(outcome_counts), 'effect_counts': dict(effect_counts),
        'tagcheck_counts': dict(tagcheck_counts), 'skill_choice_counts': dict(skill_choice_counts),
        'objective_coverage': obj,
    }
    return log, summary


# ---------------------------------------------------------------------------
# Execute 3 independent replicate runs (SystemRandom has no reproducible seed;
# 3 replicates check the fix is robust, not a one-off lucky roll sequence)
# ---------------------------------------------------------------------------

all_log = []
all_summaries = []
for rep in (1, 2, 3):
    log, summary = run_scenario(rep)
    all_log.extend(log)
    all_summaries.append(summary)

fieldnames = list(all_log[0].keys())
with open('/home/claude/mirror_playtest/exchange_log_v2_rotation.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(all_log)

with open('/home/claude/mirror_playtest/summary_v2_rotation.json', 'w') as f:
    json.dump(all_summaries, f, indent=2, default=str)

print(json.dumps(all_summaries, indent=2, default=str))
