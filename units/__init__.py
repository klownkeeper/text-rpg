from settings import TURN_CONST
from encounter.exceptions import BattleFinishedException

class Unit(object):
    id = None
    name = None
    initiative = 10.0

    unit_hp = 10
    unit_mp = 10
    unit_hp_max = 10
    unit_mp_max = 10
    unit_damage = "1d2"
    unit_attack = 0
    unit_defence = 0

    unit_fortitude = 1
    unit_reflex = 1
    unit_will = 1

    unit_ac = 0

    action_list = {
        "normal_attack":{
            'skill_attack': 0,
            'skill_damage': '1d2',
            'skill_cost': 0,
            'skill_cooldown': TURN_CONST,
            'skill_effect': None,
            },
    }

    def __init__(self, name, **kwargs):
        self.name = name
        for k, v in kwargs.items():
            setattr(self, k, v)

    def action(self, world):
        raise NotImplementedError

    @property
    def is_dead(self):
        return self.unit_hp <= 0


class TeamedUnit(Unit):
    team = None

    def enemy_list(self, world, include_dead=False):
        enemy_list = []
        for idx in range(len(world.unit_list)):
            if world.unit_list[idx].team != self.team and \
               not world.unit_list[idx].is_dead:
                enemy_list.append(idx)
        if not enemy_list:
            raise BattleFinishedException(team_win=self.team)
        return enemy_list

    def teammate_list(self, world, include_dead=False):
        teammate_list = []
        for idx in range(len(world.unit_list)):
            if world.unit_list[idx].team == self.team and \
               not world.unit_list[idx].is_dead:
                teammate_list.append(idx)
        return teammate_list

    def action(self, world):
        raise NotImplementedError

