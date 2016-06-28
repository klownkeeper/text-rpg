from units import Unit
from encounter.exceptions import *
from encounter import const


class Creature(Unit):
    """docstring for Abstract Creature"""

    unit_exp = 1
    unit_level = 1

    def choose_action(self, world):
        if len(self.enemy_list(world)) == 0:
            raise NoEnemyException
        return "attack", self.enemy_list(world)[0]

    def action(self, world):
        action, *args = self.choose_action(world)
        self.dispatch(action, world, *args)
