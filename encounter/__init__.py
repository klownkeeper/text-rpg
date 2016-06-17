from settings import *
from utils import dice


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
                print("removed dead unit", unit.name)
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

    def attack(self, attacker_id, target_id, skill_name):
        attacker = self.unit_list[attacker_id]
        target = self.unit_list[target_id]
        skill = attacker.action_list[skill_name]
        damage = skill['skill_damage']
        attack = skill['skill_attack']
        cost = skill['skill_cost']
        if cost > attacker.unit_mp:
            print("* %s failed to attack %s by %s: MP(%d) not enough" % (
                attacker.name, target.name, skill_name, attacker.unit_mp))
            self.cooldown_list[attacker_id] = TURN_CONST
            return
        defenc = target.unit_defence
        damage_deal = dice(damage) + attack - defenc
        if damage_deal < 0:
            damage_deal = 0
        self.unit_list[target_id].unit_hp -= damage_deal
        self.unit_list[attacker_id].unit_mp -= cost
        self.cooldown_list[attacker_id] = skill['skill_cooldown']
        print("* (%s) <%s> (%s), deal (%d) points damage: (%d)" % (
            attacker.name, skill_name, target.name, damage_deal, target.unit_hp))

    def heal(self, healer_id, target_id, skill_name):
        healer = self.unit_list[healer_id]
        target = self.unit_list[target_id]
        skill = healer.action_list[skill_name]
        cost = skill['skill_cost']
        if cost > healer.unit_mp:
            print("* %s failed to heal %s by %s: MP(%d) not enough" % (
                healer.name, target.name, skill_name, healer.unit_mp))
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
        print("* %s %s %s heal %d points damage: (%d)" % (
            healer.name, skill_name, target.name, damage_deal, target.unit_hp))
