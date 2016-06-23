from settings import *
from utils import dice, target_hit_print, target_heal_print
from encounter import const


class ActionManager(object):
    unit_list = []
    cooldown_list = []
    unit_ready_list = []
    ready = False

    def add_unit(self, unit, cooldown_init=TURN_CONST):
        """docstring for add_unit"""
        self.unit_list.append(unit)
        self.cooldown_list.append(cooldown_init)

    def del_unit(self, unit_id):
        for i in range(len(self.unit_list)):
            if self.unit_list[i].id == unit_id:
                del(self.unit_list[i])
                del(self.cooldown_list[i])

    def get_unit(self, unit_id):
        return self.unit_list[unit_id]

    def wait_unit(self):
        if not self.unit_list:
            raise "No Unit"
        if self.ready:
            return self.ready
        time_to_action = self._time_to_action()
        shortest_time = min(time_to_action)
        self._update_cooldown(shortest_time)
        self.ready = True
        return self.ready
    
    def act_unit(self):
        if not self.ready:
            return self.ready
        for idx in self.unit_ready_list:
            if self.unit_list[idx].is_dead:
                continue
            self.unit_list[idx].action(self)
            # self.cooldown_list[idx] = TURN_CONST
        for unit in self.unit_list:
            if unit.is_dead:
                idx = self.unit_list.index(unit)
                # print("removed dead unit", unit.name)
                del(self.unit_list[idx])
                del(self.cooldown_list[idx])
        self.unit_ready_list = []
        self.ready = False
        return self.ready

    def run_until_exception(self):
        for i in range(30):
            self.wait_unit()
            self.act_unit()

    def situation(self):
        """docstring for si"""
        return self.unit_list

    def _time_to_action(self):
        time_to_action = []
        for unit, cooldown in zip(self.unit_list, self.cooldown_list):
            time_to_action.append(cooldown / unit.initiative)
        return time_to_action

    def _update_cooldown(self, time):
        for unit, idx in zip(self.unit_list, range(len(self.unit_list))):
            self.cooldown_list[idx] -= time * unit.initiative
            if self.cooldown_list[idx] < 0.001:
                self.cooldown_list[idx] = 0
                self.unit_ready_list.append(idx)


class EncounterManager(ActionManager):

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

    def damage_roll(self, attacker_id, target_id, skill_name,
                    is_critical=False, penalty=0):
        """
        skill_damage + related ability modifier
        if is_critical, twice die damage + 2 * all modifiers
        """
        attacker = self.unit_list[attacker_id]
        target = self.unit_list[target_id]
        skill = attacker.action_list[skill_name]
        base_damage = dice(skill['skill_damage'])
        modifier = attacker.ability_modifier(skill['skill_bonus_ability'])
        if is_critical:
            base_damage += dice(skill['skill_damage'])
            modifiers += modifiers
        damage = base_damage + modifier - penalty
        if damage < const.MINIMUN_DAMAGE:
            damage = MINIMUN_DAMAGE
        self.unit_list[target_id].unit_hp -= damage
        self.unit_list[attacker_id].unit_mp -= skill['skill_cost']
        msg = ""
        if target.unit_hp <= 0:
            msg = "Target died."
        target_hit_print(
            player_name=attacker.name, action_name=skill_name,
            target_name=target.name, damage=damage,
            target_hp=target.unit_hp, message=msg)

    def heal(self, healer_id, target_id, skill_name):
        healer = self.unit_list[healer_id]
        target = self.unit_list[target_id]
        skill = healer.action_list[skill_name]
        cost = skill['skill_cost']
        if cost > healer.unit_mp:
            # print("* %s failed to heal %s by %s: MP(%d) not enough" % (
            #     healer.name, target.name, skill_name, healer.unit_mp))
            self.cooldown_list[healer_id] = TURN_CONST
            return
        damage = skill['skill_damage']
        attack = skill['skill_attack']
        damage_deal = dice(damage) + attack
        if damage_deal + target.unit_hp > target.unit_hp_max:
            damage_deal = target.unit_hp_max - target.unit_hp
        self.unit_list[target_id].unit_hp += damage_deal
        self.unit_list[healer_id].unit_mp -= cost
        self.cooldown_list[healer_id] = skill['skill_cooldown']
        target_heal_print(
            name=healer.name, action_name=skill_name,
            target_name=target.name, damage=damage_deal,
            target_hp=target.unit_hp, message="")
