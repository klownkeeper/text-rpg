from units.creatures import Creature
from settings import *


class Goblin(Creature):
    """docstring for Goblin"""

    name = None
    initiative = 10.0
    team = "wild"

    unit_hp = 10
    unit_mp = 1
    unit_hp_max = 10
    unit_mp_max = 1
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
    }
    unit_exp = 5

    def choose_action(self, world):
        """
        Goblins are always attack most weak enemy.
        """
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

