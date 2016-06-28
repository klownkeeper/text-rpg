from skills.spells.divine.divine_spell import DivineSpell


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
            print("Cure Minor Wounds cures %s by 1 hp." % unit.name)
