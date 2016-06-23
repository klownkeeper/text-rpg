from units import TeamedUnit
from encounter.exceptions import *
from encounter import const


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
        # world.attack(world.unit_list.index(self), target_idx, action)
        attack_roll = world.attack_roll(
                world.unit_list.index(self), target_idx, action)
        if attack_roll == const.ATTACK_ROLL_HIT:
            world.damage_roll(
                world.unit_list.index(self), target_idx, action)
        elif attack_roll == const.ATTACK_ROLL_CRITICAL:
            world.damage_roll(
                world.unit_list.index(self), target_idx, action)
        else:
            pass
        attacker_id = world.unit_list.index(self)
        world.cooldown_list[attacker_id] = self.action_list[action]['skill_cooldown']

