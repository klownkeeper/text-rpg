from units.characters import Character
from settings import TURN_CONST
from decorators import enemy_exist
from units.const import *
from encounter.const import *

from items.weapons import SHORT_SWORD

class Fighter(Character):

    name = "Fighter"
    initiative = 10.0

    unit_hp = 10
    unit_mp = 10
    unit_hp_max = 10
    unit_mp_max = 10


    unit_main_weapon = SHORT_SWORD
