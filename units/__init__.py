from settings import TURN_CONST

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

    def action(self, world):
        raise NotImplementedError

