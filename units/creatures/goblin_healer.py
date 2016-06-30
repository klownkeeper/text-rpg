from units.creatures import Creature
from settings import *
from units.const import *
from units.creatures.tactics.heal_weakest import HealWeakestTactic
from encounter.const import *
from items.weapons import UNARMED_STRIKE_SMALL


class GoblinHealer(HealWeakestTactic, Creature):
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
