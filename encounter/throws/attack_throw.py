from utils import dice
from encounter import const
from utils import target_attack_print, target_attack_failed_print
from items import armor_types


class AttackThrowMixin(object):
    """
    for attack throw
    example:
      player use a short sword to attack a goblin.
      if attack throw pass, it will give a hit.
    """

    def attack_roll(self,
                    attacker_id,
                    target_id,
                    ability_to_attack,
                    attack_time=0,
                    critical_dice=[20],
                    penalty=0):
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
        if d20 in critical_dice:
            maybe_critical = True
            # make a critical rool
        attacker = self.get_unit_by_idx(attacker_id)
        target = self.get_unit_by_idx(target_id)

        attack_bonus = (attacker.get_base_attack_bonus()[attack_time]
                + getattr(attacker, ability_to_attack.lower()+"_modifier")
                + attacker.size_modifier)
        target_ac = target.armor_class

        attack_beat_ac = (d20 + attack_bonus - penalty) >= target_ac

        target_attack_print(player_name=attacker.name,
                            target_name=target.name)
        if attack_beat_ac:
            if maybe_critical:
                return const.ATTACK_ROLL_CRITICAL
            else:
                return const.ATTACK_ROLL_HIT
        else:
            if maybe_critical:
                return const.ATTACK_ROLL_HIT
            else:
                target_attack_failed_print(player_name=attacker.name,
                                    target_name=target.name)
                return const.ATTACK_ROLL_FAILED

        
