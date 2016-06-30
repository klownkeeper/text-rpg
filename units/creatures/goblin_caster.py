from units.creatures import Creature
from settings import *
from units.const import *
from encounter.const import *
from items.weapons import UNARMED_STRIKE_SMALL

class GoblinCaster(Creature):
    """docstring for Goblin Caster"""

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
        'ray_of_frost': 6
    }

    def choose_action(self, world):
        """
        Goblins are always attack most weak enemy.
        """
        enemy_list = self.enemy_list(world)
        if len(enemy_list) == 0:
            raise NoEnemyException
        
        for idx in enemy_list:
            unit = world.unit_list[idx]
            if not unit.is_dead:
                if self.creature_spells['ray_of_frost'] > 0:
                    self.creature_spells['ray_of_frost'] -= 1
                    return ("cast", "ray_of_frost", unit.id)
                else:
                    return ('attack', target_idx)
