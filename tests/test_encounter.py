import unittest
from unittest.mock import MagicMock
from units.creatures.goblin import Goblin
from units.creatures.goblin_healer import GoblinHealer
from units.creatures.goblin_caster import GoblinCaster
from units.characters.character import Character
from units.characters.classes import Fighter
from encounter import Encounter
from encounter.exceptions import *
from items.weapons import SHORT_SWORD_MEDIUM
from items.armors import SPLINT_MAIL_MEDIUM, LIGHT_WOOD_SHIELD_MEDIUM


class TestEncounter(unittest.TestCase):

    def test_encounter(self):
        encounter = Encounter()

        char1 = Character.create(
            name="Player A",
            start_class="Fighter",
            str_modify=6,
            dex_modify=2,
            con_modify=4,
            int_modify=2,
            wis_modify=0,
            chr_modify=0,
            unit_main_hand_weapon=SHORT_SWORD_MEDIUM,
            unit_off_hand_weapon=LIGHT_WOOD_SHIELD_MEDIUM,
            unit_armor=SPLINT_MAIL_MEDIUM,
            )
        char1.team = "party"
        char1.ask_ability_bonus = MagicMock(return_value="unit_str")
        
        char1.gain_level("Fighter")
        char1.gain_level("Fighter")
        char1.gain_level("Fighter")
        print("Char stats: HP:%d/%d %s" % (char1.unit_hp, char1.unit_hp_max, char1.get_base_attack_bonus()))
        char1.get_command = MagicMock(return_value=["attack", "1"])

        # char2 = Character.create(
        #     name="Player B",
        #     start_class="Fighter",
        #     str_modify=6,
        #     dex_modify=2,
        #     con_modify=4,
        #     int_modify=2,
        #     wis_modify=0,
        #     chr_modify=0,
        #     init_weapon=SHORT_SWORD_MEDIUM,
        #     )
        # char2.team = "party"
        # char2.gain_level("Fighter")
        # char2.gain_level("Fighter")
        # char2.gain_level("Fighter")
        # print("Char stats: HP:%d/%d %s" % (char2.unit_hp, char2.unit_hp_max, char2.get_base_attack_bonus()))
        # char2.get_command = MagicMock(return_value=["attack", "2"])

        gob1 = Goblin.create(name='goblin', unit_level=5)
        gob2 = GoblinCaster.create(name='goblin caster', unit_level=5)
        gob3 = GoblinHealer.create(name='goblin header', unit_level=7)
        encounter.add_unit(char1)
        # encounter.add_unit(char2)
        encounter.add_unit(gob1)
        encounter.add_unit(gob2)
        encounter.add_unit(gob3)

        win_team = None
        try:
            encounter.run_until_exception()
        except BattleFinishedException as e:
            win_team = e.team_win
            print("team %s wins!" % win_team)
            print("unit dead:", encounter.unit_dead_list)
