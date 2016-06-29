from settings import *
from utils import turn_start_print, turn_end_print


class TurnManager(object):
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
            turn_start_print(name=self.unit_list[idx].name)
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
        # Main Loop
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

