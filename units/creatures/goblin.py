from units.creatures import Creature
from units import const
from settings import *
from decorators import enemy_exist
from items.weapons import UNARMED_STRIKE_SMALL


class Goblin(Creature):
    """docstring for Goblin"""

    name = None
    initiative = 10.0
    team = "wild"

    unit_hp = 5
    unit_mp = 1
    unit_hp_max = 5
    unit_mp_max = 1

    unit_exp = 5

    unit_main_weapon = UNARMED_STRIKE_SMALL

    @enemy_exist
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
        return ('attack', target_idx)

