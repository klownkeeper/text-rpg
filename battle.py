TURN_CONST = 10.0


class Unit(object):
    id = None
    name = None
    initiative = 10.0

    unit_hp = 10
    unit_mp = 10
    unit_attack = 1
    unit_defence = 1

    def action(self, situation):
        # print("Action", self.name, situation)
        print("unit %s, HP:%d" % (self.name, self.unit_hp))


class TeamedUnit(Unit):
    team = None

    def action(self, situation):
        # print("Action", self.name, situation)
        enemy_list = []
        for idx in range(len(situation)):
            print(situation, idx)
            if situation[idx].team != self.team:
                enemy_list.append(idx)
        if not enemy_list:
            print("enemy_list empty")
            return
        situation[enemy_list[0]].unit_hp -= 1
        print("unit %s, HP:%d" % (self.name, self.unit_hp))


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
            self.unit_list[idx].action(self.situation())
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


if __name__ == '__main__':
    u1 = TeamedUnit()
    u1.initiative = 9.0
    u1.name = "u1"
    u1.team = "1"
    u2 = TeamedUnit()
    u2.name = "u2"
    u2.team = "2"

    manager = ActionManager()
    manager.add_unit(u1)
    manager.add_unit(u2)

    for i in range(20):
        manager.wait_unit()
        manager.act_unit()

