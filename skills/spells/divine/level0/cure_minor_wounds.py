from skills.spells.divine.divine_spell import DivineSpell
from utils import cast_spell_success_print


class CureMinorWounds(DivineSpell):
    """
    Cure Minor Wounds: Cures 1 point of damage.
    """
    level = 0
    name = "cure_minor_wounds"
    description = "Cure Minor Wounds: Cures 1 point of damage."

    def effect(self, world, target_unit_id):
        unit = world.unit_list[target_unit_id]
        if unit.unit_hp_max - unit.unit_hp >= 1:
            world.unit_list[target_unit_id].unit_hp += 1
            cast_spell_success_print(
                spell_name=self.name,
                target_name=unit.name,
                message="cure \033[91m%s\033[0m by 1 hp" % unit.name)
