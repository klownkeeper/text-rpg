import unittest
from unittest.mock import MagicMock
from units.creatures.goblin import Goblin
from units.creatures.goblin_healer import GoblinHealer
from units.characters.fighter import Fighter
from encounter import EncounterManager
from encounter.exceptions import *


class TestEncounter(unittest.TestCase):

    def test_encounter(self):
        manager = EncounterManager()

        char = Fighter("Player", team="party")
        char.get_command = MagicMock(return_value=["short_sword", 1])
        manager.add_unit(char)
        manager.add_unit(Goblin('glblin a'))
        manager.add_unit(Goblin('glblin b'))
        manager.add_unit(GoblinHealer('glblin_healer a'))

        win_team = None
        try:
            manager.run_until_exception()
        except BattleFinishedException as e:
            win_team = e.team_win
            print("team %s wins!" % win_team)
