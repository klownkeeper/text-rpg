import random

from encounter.exceptions import NoEnemyException
from skills import spells


class HealWeakestTactic(object):

    heal_threshold = 0.7

    def choose_action(self, world):
        """
        """
        enemy_list = self.enemy_list(world)
        if not enemy_list:
            raise NoEnemyException
        teammate_list = self.teammate_list(world)

        choose_spell = None
        for spell_name, times in self.creature_spells.items():
            if times < 1:
                continue
            spell = getattr(spells, "".join(list(map(lambda x:x.capitalize(), spell_name.split("_")))))()
            if (spell.spell_type == spells.const.HEAL_SPELL and
                spell.spell_target_type == spells.const.SINGLE_TARGET_SPELL):
                choose_spell = spell_name

        if choose_spell:
            for idx in teammate_list:
                unit = world.get_unit_by_idx(idx)
                if (float(unit.unit_hp) / float(unit.unit_hp_max)) < self.heal_threshold:
                    self.creature_spells[choose_spell] -= 1
                    return ("cast", choose_spell, unit.id)
        target_idx = random.choice(enemy_list)
        return ('attack', target_idx)
