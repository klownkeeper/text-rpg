import random

TURN_CONST = 10.0

def dice(dice_str):
    n, d = map(int, dice_str.split('d'))
    res = 0
    for i in range(n):
        res += random.choice(range(1, d+1))
    return res
    

class Unit(object):
    id = None
    name = None
    initiative = 10.0

    unit_hp = 10
    unit_mp = 10
    unit_damage = "1d2"
    unit_attack = 0
    unit_defence = 0

    action_list = {
        "normal_attack":{
            'unit_attack': 0,
            'unit_damage': '1d2',
            'unit_cooldown': TURN_CONST,
            },
    }

    def action(self, world):
        print("unit %s, HP:%d" % (self.name, self.unit_hp))


class TeamedUnit(Unit):
    team = None

    def action(self, situation):
        raise NotImplementedError
        # print("Action", self.name, situation)
        enemy_list = []
        for idx in range(len(situation)):
            if situation[idx].team != self.team:
                enemy_list.append(idx)
        if not enemy_list:
            return
        damage = dice(self.unit_damage) + self.unit_attack - situation[enemy_list[0]].unit_defence
        print(damage)
        situation[enemy_list[0]].unit_hp -= damage
        print("unit %s, HP:%d" % (self.name, self.unit_hp))


class Creature(TeamedUnit):
    """docstring for Abstract Creature"""

    def enemy_list(self, world):
        enemy_list = []
        for idx in range(len(world.unit_list)):
            if world.unit_list[idx].team != self.team:
                enemy_list.append(idx)
        if not enemy_list:
            raise "Battle is already finished!"
        return enemy_list

    def choose_action(self, world):
        return "normal_attack", self.enemy_list(world)[0]

    def action(self, world):
        action, target_idx = self.choose_action(world)
        world.attack(world.unit_list.index(self), target_idx, action)


class Situation(object):
    pass


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
            self.unit_list[idx].action(self)
            self.cooldown_list[idx] = TURN_CONST
        self.unit_ready_list = []
        self.ready = False
        return self.ready

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


class DamageManager(ActionManager):

    def attack(self, attacker_id, defencer_id, attack_name):
        attacker = self.unit_list[attacker_id]
        defencer = self.unit_list[defencer_id]
        damage = attacker.action_list[attack_name]['unit_damage']
        attack = attacker.action_list[attack_name]['unit_attack']
        defenc = defencer.unit_defence
        damage_deal = dice(damage) + attack - defenc
        if damage_deal < 0:
            damage_deal = 0
        self.unit_list[defencer_id].unit_hp -= damage_deal
        print("* %s %s %s deal %d points damage: (%d)" % (
            attacker.name, attack_name, defencer.name, damage_deal, self.unit_list[defencer_id].unit_hp))


if __name__ == '__main__':
    u1 = Creature()
    u1.initiative = 9.0
    u1.name = "u1"
    u1.team = "1"
    u2 = Creature()
    u2.name = "u2"
    u2.team = "2"

    manager = DamageManager()
    manager.add_unit(u1)
    manager.add_unit(u2)

    for i in range(20):
        manager.wait_unit()
        manager.act_unit()

