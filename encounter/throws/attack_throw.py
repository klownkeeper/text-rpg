from utils import dice
from encounter import const


class AttackThrowMixin(object):
    """
    for attack throw
    example:
      player use a short sword to attack a goblin.
      if attack throw pass, it will give a hit.
    """

    def attack_roll(self, attacker_id, target_id, skill_name, penalty=0):
        """
        1d20. when get 1, always MISS.
              when get 20, maybe critical.
              when Base attack bonus + ability modifier + size modifier > target AC, HIT.
                   if also critical, then CRITICAL_HIT
              else if maybe critical, HIT.
                   else MISS
        """
        d20 = dice("1d20")
        maybe_critical = False
        if d20 == 1:
            return const.ATTACK_ROLL_FAILED
        if d20 == 20:
            maybe_critical = True
            # make a critical rool
        attacker = self.get_unit(attacker_id)
        target = self.get_unit(target_id)
        skill = attacker.get_action(skill_name)

        attack_bonus = (attacker.base_attack_bonus
                + attacker.ability_modifier(skill['skill_bonus_ability'])
                + attacker.size_modifier)
        target_ac = target.armor_class

        attack_beat_ac = (d20 + attack_bonus - penalty) >= target_ac

        if attack_beat_ac:
            if maybe_critical:
                print("  %s critical hit %s!" % (attacker.name, target.name))
                return const.ATTACK_ROLL_CRITICAL
            else:
                print("  %s hit %s!" % (attacker.name, target.name))
                return const.ATTACK_ROLL_HIT
        else:
            if maybe_critical:
                print("  %s hit %s!" % (attacker.name, target.name))
                return const.ATTACK_ROLL_HIT
            else:
                print("  %s failed to hit %s!" % (attacker.name, target.name))
                return const.ATTACK_ROLL_FAILED

        
