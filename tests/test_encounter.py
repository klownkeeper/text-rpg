import unittest
from units.creatures.goblin import Goblin
from units.creatures.goblin_healer import GoblinHealer
from encounter import EncounterManager
from encounter.exceptions import *


class TestEncounter(unittest.TestCase):

    def test_encounter(self):
        manager = EncounterManager()

        manager.add_unit(Goblin('holy glblin a', team="holy"))
        manager.add_unit(Goblin('glblin a'))
        manager.add_unit(Goblin('holy glblin b', team="holy"))
        manager.add_unit(Goblin('glblin b'))
        manager.add_unit(GoblinHealer('holy glblin c', team="holy"))
        manager.add_unit(Goblin('glblin c'))

        win_team = None
        try:
            manager.run_until_exception()
        except BattleFinishedException as e:
            win_team = e.team_win
            print("team %s wins!" % win_team)
