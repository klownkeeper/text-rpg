from units.creatures import Creature
from settings import *
from units.const import *
from encounter.const import *
from items.weapons import UNARMED_STRIKE_SMALL


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

    unit_exp = 5

    unit_main_weapon = UNARMED_STRIKE_SMALL

    creature_spells = {
        'cure_light_wounds': 2
    }

    def choose_action(self, world):
        """
        Goblins are always attack most weak enemy.
        """
        teammate_list = self.teammate_list(world)
        if self.creature_spells['cure_light_wounds'] > 0:
            for idx in teammate_list:
                unit = world.unit_list[idx]
                if (float(unit.unit_hp) / float(unit.unit_hp_max)) < 0.4 and \
                        self.unit_mp >= 2:
                    print("%%%%%", self.creature_spells)
                    self.creature_spells['cure_light_wounds'] -= 1
                    return ("cast", "cure_light_wounds", idx)
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
