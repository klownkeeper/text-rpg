from skills.spells.arcane.arcane_spell import ArcaneSpell
from skills.spells.spell import SingleTargetDamageSpellMixin
from skills.spells import const


class RayOfFrost(SingleTargetDamageSpellMixin, ArcaneSpell):
    """
    Ray of frost:
      A ray of freezing air and ice projects from your pointing finger.
      You must succeed on a ranged touch attack with the ray to deal damage to a target.
      The ray deals 1d3 points of cold damage.
    """
    level = 0
    name = "ray_of_frost"
    description = "Ray of frost: deal 1d3 point of damages."

    damage = 0
    damage_dice = "1d3"

    spell_type = const.DAMAGE_SPELL
    spell_target_type = const.SINGLE_TARGET_SPELL
