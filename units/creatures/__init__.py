from units import TeamedUnit
from encounter.exceptions import *


class Creature(TeamedUnit):
    """docstring for Abstract Creature"""

    unit_exp = 1
    unit_level = 1

    def enemy_list(self, world, include_dead=False):
        enemy_list = []
        for idx in range(len(world.unit_list)):
            if world.unit_list[idx].team != self.team and \
               not world.unit_list[idx].is_dead:
                enemy_list.append(idx)
        if not enemy_list:
            raise BattleFinishedException(team_win=self.team)
        return enemy_list

    def teammate_list(self, world, include_dead=False):
        teammate_list = []
        for idx in range(len(world.unit_list)):
            if world.unit_list[idx].team == self.team and \
               not world.unit_list[idx].is_dead:
                teammate_list.append(idx)
        return teammate_list

    def choose_action(self, world):
        if len(self.enemy_list(world)) == 0:
            raise NoEnemyException
        return "normal_attack", self.enemy_list(world)[0]

    def action(self, world):
        action, target_idx = self.choose_action(world)
        world.attack(world.unit_list.index(self), target_idx, action)
