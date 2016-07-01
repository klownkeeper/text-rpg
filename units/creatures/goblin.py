from units.creatures import Creature
from units import const
from settings import *
from decorators import enemy_exist
from items.weapons import UNARMED_STRIKE_SMALL
from units.creatures.tactics.random_normal_attack import RandomNormalAttackTactic


class Goblin(RandomNormalAttackTactic, Creature):
    """docstring for Goblin"""

    name = None
    initiative = 10.0
    team = "wild"

    unit_hp = 5
    unit_mp = 1
    unit_hp_max = 5
    unit_mp_max = 1

    unit_exp = 5

    unit_main_hand_weapon = UNARMED_STRIKE_SMALL
