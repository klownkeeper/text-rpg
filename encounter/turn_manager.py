from settings import *
from utils import turn_start_print, turn_end_print


class WorldMixin(object):

    def get_unit_by_idx(self, unit_id):
        return self.unit_list[unit_id]

    def get_unit_by_uuid(self, unit_uuid):
        for u in self.unit_list:
            if u.id == unit_uuid:
                return u
        
    def get_unit_idx_by_uuid(self, unit_uuid):
        for u in self.unit_list:
            if u.id == unit_uuid:
                return self.unit_list.index(u)
        

class TurnManager(WorldMixin):
    unit_list = []
    unit_dead_list = []
    cooldown_list = []
    unit_ready_list = []
    ready = False

    current_act_unit_id = None # keep current in turn unit idx

    def add_unit(self, unit, cooldown_init=TURN_CONST):
        """docstring for add_unit"""
        self.unit_list.append(unit)
        self.cooldown_list.append(cooldown_init)

    def kill_unit(self, unit_id):
        """docstring for kill_unit"""
        unit = self.unit_list[unit_id]
        self.unit_dead_list.append(unit)
        del(self.unit_list[unit_id])
        del(self.cooldown_list[unit_id])

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
            self.current_act_unit_id = idx
            turn_start_print(name=self.unit_list[idx].name)
            self.unit_list[idx].action(self)
        for unit in self.unit_list:
            if unit.is_dead:
                idx = self.unit_list.index(unit)
                self.kill_unit(idx)
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
