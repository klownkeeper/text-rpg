from skills.spells.divine.divine_spell import DivineSpell
from utils import cast_spell_success_print, dice


class CureLightWounds(DivineSpell):
    """
    Cure Minor Wounds: Cures 1 point of damage.
    """
    level = 0
    name = "cure_light_wounds"
    description = "Cure Light Wounds: Cures Cures 1d8 damage +1/level (max +5)."

    def effect(self, world, target_unit_id):
        caster = world.unit_list[world.current_act_unit_id]
        target = world.unit_list[target_unit_id]
        cure_hp = dice("1d8")
        modifier = caster.unit_level
        if caster.unit_level > 5:
            modifier = 5
        cure_hp += modifier

        if target.unit_hp + cure_hp > target.unit_hp_max:
            cure_hp = target.unit_hp_max - target.unit_hp

        world.unit_list[target_unit_id].unit_hp += cure_hp
        cast_spell_success_print(
            spell_name=self.name,
            target_name=target.name,
            message="cure \033[91m%s\033[0m by %d hp" % (target.name, cure_hp))

