from skills.spells.divine.divine_spell import DivineSpell
from skills.spells.spell import SingleTargetHealSpellMixin


class CureMinorWounds(SingleTargetHealSpellMixin, DivineSpell):
    """
    Cure Minor Wounds: Cures 1 point of damage.
    """
    level = 0
    name = "cure_minor_wounds"
    description = "Cure Minor Wounds: Cures 1 point of damage."

    heal_hp = 1
