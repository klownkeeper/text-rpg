import random

from encounter.exceptions import NoEnemyException


class RandomNormalAttackTactic(object):
    """docstring for RandomNormalAttackTactic"""

    def choose_action(self, world):
        """
        Always random attack enemy tactic.
        """
        enemy_list = self.enemy_list(world)
        if not enemy_list:
            raise NoEnemyException
        target_idx = random.choice(enemy_list)
        return ('attack', target_idx)
