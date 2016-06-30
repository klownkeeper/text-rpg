from skills.spells.divine.divine_spell import DivineSpell
from skills.spells.spell import SingleTargetHealSpellMixin


class CureLightWounds(SingleTargetHealSpellMixin, DivineSpell):
    """
    Cure Minor Wounds: Cures 1 point of damage.
    """
    level = 0
    name = "cure_light_wounds"
    description = "Cure Light Wounds: Cures Cures 1d8 damage +1/level (max +5)."

    heal_hp_dice = "1d8"

    def get_heal_hp_modifier(self, world, *args):
        caster = self.get_caster(world)
        caster_level = 0
        if caster.unit_level > 5:
            caster_level = 5
        else:
            caster_level = caster.unit_level
        return caster_level
