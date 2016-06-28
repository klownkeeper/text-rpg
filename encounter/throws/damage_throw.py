from utils import dice, target_hit_print
from encounter import const


class DamageThrowMixin(object):
    """
    Tell how many points of damage target will get.
    """

    def damage_roll(self, attacker_id, target_id,
                    skill_name, skill_damage, bonus_ability,
                    is_critical=False, penalty=0):
        """
        skill_damage + related ability modifier
        if is_critical, twice die damage + 2 * all modifiers
        """
        attacker = self.unit_list[attacker_id]
        target = self.unit_list[target_id]
        base_damage = dice(skill_damage)
        modifier = attacker.ability_modifier(bonus_ability)
        if is_critical:
            base_damage += dice(skill_damage)
            modifier += modifier
        damage = base_damage + modifier - penalty
        if damage < const.MINIMUN_DAMAGE:
            damage = MINIMUN_DAMAGE
        self.unit_list[target_id].unit_hp -= damage
        msg = ""
        if is_critical:
            msg += "(Critical Hit)"
        if target.unit_hp <= 0:
            msg = "Target died."
        target_hit_print(
            player_name=attacker.name, action_name=skill_name,
            target_name=target.name, damage=damage,
            target_hp=target.unit_hp, message=msg)
