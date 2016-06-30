import random

from encounter.exceptions import NoEnemyException
from skills import spells


class RandomSpellAttackTactic(object):
    """docstring for RandomNormalAttackTactic"""

    def choose_action(self, world):
        """
        Always random attack enemy tactic.
        """
        enemy_list = self.enemy_list(world)
        if not enemy_list:
            raise NoEnemyException

        choose_spell = None
        for spell_name, times in self.creature_spells.items():
            if times < 1:
                continue
            spell = getattr(spells, "".join(list(map(lambda x:x.capitalize(), spell_name.split("_")))))()
            if (spell.spell_type == spells.const.DAMAGE_SPELL and
                spell.spell_target_type == spells.const.SINGLE_TARGET_SPELL):
                choose_spell = spell_name
               
        target_idx = random.choice(enemy_list)
        target = world.get_unit_by_idx(target_idx)
        if choose_spell:
            self.creature_spells[choose_spell] -= 1
            return ('cast', choose_spell, target.id)
        else:
            return ('attack', target_idx)

