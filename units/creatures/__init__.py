from units import TeamedUnit
from encounter.exceptions import *


class Creature(TeamedUnit):
    """docstring for Abstract Creature"""

    unit_exp = 1
    unit_level = 1

    def choose_action(self, world):
        if len(self.enemy_list(world)) == 0:
            raise NoEnemyException
        return "normal_attack", self.enemy_list(world)[0]

    def action(self, world):
        action, target_idx = self.choose_action(world)
        world.attack(world.unit_list.index(self), target_idx, action)
