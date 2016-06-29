import unittest
from unittest.mock import MagicMock
from units.creatures.goblin import Goblin
from units.creatures.goblin_healer import GoblinHealer
from units.characters.character import Character
from units.characters.classes import Fighter
from encounter import Encounter
from encounter.exceptions import *
from items.weapons import SHORT_SWORD_MEDIUM


class TestEncounter(unittest.TestCase):

    def test_encounter(self):
        encounter = Encounter()

        char = Character.create_character(
            name="Player",
            start_class=Fighter,
            str_modify=6,
            dex_modify=2,
            con_modify=4,
            int_modify=2,
            wis_modify=0,
            chr_modify=0,
            init_weapon=SHORT_SWORD_MEDIUM,
            )
        char.team = "party"
        char.get_command = MagicMock(return_value=["attack", 1])
        encounter.add_unit(char)
        encounter.add_unit(Goblin('glblin a'))
        encounter.add_unit(Goblin('glblin b'))
        encounter.add_unit(GoblinHealer('glblin_healer a'))

        win_team = None
        try:
            encounter.run_until_exception()
        except BattleFinishedException as e:
            win_team = e.team_win
            print("team %s wins!" % win_team)
