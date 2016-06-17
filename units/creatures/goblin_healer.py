from units.creatures import Creature
from settings import *


class GoblinHealer(Creature):
    """docstring for Goblin"""

    name = None
    initiative = 10.0
    team = "wild"

    unit_hp = 10
    unit_mp = 2
    unit_hp_max = 10
    unit_mp_max = 2
    unit_damage = "1d2"
    unit_attack = 0
    unit_defence = 0

    action_list = {
        "goblin_club":{
            'skill_attack': 0,
            'skill_damage': '1d2',
            'skill_cost': 0,
            'skill_cooldown': TURN_CONST,
            'skill_effect': None,
            },
        "cure_light_wounds":{
            'skill_attack': 0,
            'skill_damage': '1d8',
            'skill_cost': 2,
            'skill_cooldown': TURN_CONST,
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
            world.attack(world.unit_list.index(self), target_idx, action)
