from units.creatures import Creature
from settings import *
from units.const import *
from encounter.const import *


class GoblinHealer(Creature):
    """docstring for Goblin"""

    name = None
    initiative = 10.0
    team = "wild"

    unit_hp = 4
    unit_mp = 2
    unit_hp_max = 4
    unit_mp_max = 2

    unit_str = 11
    unit_dex = 13
    unit_con = 12
    unit_int = 10
    unit_wis = 9
    unit_chr = 6

    action_list = {
        "goblin_club":{
            'skill_attack': 0,
            'skill_damage': '1d2',
            'skill_cost': 0,
            'skill_cooldown': TURN_CONST,
            'skill_bonus_ability': STRENGTH,
            'skill_effect': None,
            },
        "cure_light_wounds":{
            'skill_attack': 0,
            'skill_damage': '1d8',
            'skill_cost': 2,
            'skill_cooldown': TURN_CONST,
            'skill_bonus_ability': INTELLIGENCE,
            'skill_effect': None,
            },
    }
    unit_exp = 5

    def choose_action(self, world):
        """
        Goblins are always attack most weak enemy.
        """
        teammate_list = self.teammate_list(world)
        for idx in teammate_list:
            unit = world.unit_list[idx]
            if (float(unit.unit_hp) / float(unit.unit_hp_max)) < 0.4 and \
                    self.unit_mp >= 2:
                return "cure_light_wounds", idx
        enemy_list = self.enemy_list(world)
        if len(enemy_list) == 0:
            raise NoEnemyException
        target_idx = enemy_list[0]
        for idx in range(len(enemy_list)):
            if world.unit_list[enemy_list[idx]].unit_hp < \
                    world.unit_list[target_idx].unit_hp:
                target_idx = idx
        # print(self.name, target_idx)
        return ('goblin_club', target_idx)

    def action(self, world):
        action, target_idx = self.choose_action(world)
        if action == "cure_light_wounds":
            world.heal(world.unit_list.index(self), target_idx, action)
        else:
            attack_roll = world.attack_roll(
                    world.unit_list.index(self), target_idx, action)
            if attack_roll == ATTACK_ROLL_HIT:
                world.damage_roll(
                    world.unit_list.index(self), target_idx, action)
            elif attack_roll == ATTACK_ROLL_CRITICAL:
                world.damage_roll(
                    world.unit_list.index(self), target_idx, action)
            else:
                pass
            attacker_id = world.unit_list.index(self)
            world.cooldown_list[attacker_id] = self.action_list[action]['skill_cooldown']
