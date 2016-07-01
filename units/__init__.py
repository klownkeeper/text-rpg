import math
import uuid

from settings import TURN_CONST
from encounter.exceptions import BattleFinishedException
from units import const
from units.actions import  ActionDispatcherMixin, AttackMixin, CastSpellMixin

class AbstractUnit(object):
    id = None
    name = None
    initiative = 10.0
    unit_size = const.UNIT_SIZE_MEDIUM

    unit_level = 1

    unit_hp = 10
    unit_mp = 10
    unit_hp_max = 10
    unit_mp_max = 10

    unit_str = 10
    unit_dex = 10
    unit_con = 10
    unit_int = 10
    unit_wis = 10
    unit_chr = 10

    unit_fortitude = 1
    unit_reflex = 1
    unit_will = 1

    unit_ac = 0

    unit_main_hand_weapon = None
    unit_off_hand_weapon = None
    unit_armor = None

    base_attack_bonus = [0]

    # Ability modifiers
    @property
    def size_modifier(self):
        return getattr(const, self.unit_size + "_SIZE_MODIFIER")

    @property
    def str_modifier(self):
        return self._ability_modifier('str')

    @property
    def dex_modifier(self):
        dex_modifier = self._ability_modifier('dex')
        if self.armor_dex_cap:
            if dex_modifier > self.armor_dex_cap:
                dex_modifier = self.armor_dex_cap
        if self.shield_dex_cap:
            if dex_modifier > self.shield_dex_cap:
                dex_modifier = self.armor_dex_cap
        return dex_modifier

    @property
    def armor_dex_cap(self):
        cap = None
        if self.unit_armor:
            if self.unit_armor['max_dex_bonus']:
                cap = self.unit_armor['max_dex_bonus']
        return cap

    @property
    def shield_dex_cap(self):
        cap = None
        if self.unit_off_hand_weapon:
            if hasattr(self.unit_off_hand_weapon, 'max_dex_bonus'):
                cap = self.unit_off_hand_weapon['max_dex_bonus']
        return cap

    @property
    def con_modifier(self):
        return self._ability_modifier('con')

    @property
    def int_modifier(self):
        return self._ability_modifier('int')

    @property
    def wis_modifier(self):
        return self._ability_modifier('wis')

    @property
    def chr_modifier(self):
        return self._ability_modifier('chr')

    def get_base_attack_bonus(self):
        return self.base_attack_bonus

    @property
    def attack_times(self):
        return math.floor((self.base_attack_bonus - 1) / 5)

    def _ability_modifier(self, ability):
        ability_point = getattr(self, "unit_" + ability.lower())
        return math.floor((ability_point - 10) / 2)

    # Other modifiers

    @property
    def armor_bonus(self):
        if self.unit_armor:
            return self.unit_armor['armor_bonus']
        else:
            return 0

    @property
    def shield_bonus(self):
        if (self.unit_off_hand_weapon and
            hasattr(self.unit_off_hand_weapon, 'armor_type') and
            self.unit_off_hand_weapon['armor_type'] == armor_types.SHIELD):
            return self.unit_off_hand_weapon['armor_bonus']
        else:
            return 0

    @property
    def armor_class(self):
        return (10 + self.armor_bonus + self.shield_bonus
                + self.dex_modifier + self.size_modifier)

    def __init__(self, name, **kwargs):
        self.id = str(uuid.uuid4())
        self.name = name
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def get_action(self, action_name):
        return self.action_list[action_name]

    def action(self, world):
        raise NotImplementedError

    @property
    def is_dead(self):
        return self.unit_hp <= 0

    def get_self_idx(self, world):
        return world.unit_list.index(self)


class TeamedUnit(AbstractUnit):
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


class Unit(ActionDispatcherMixin,
           TeamedUnit):
    """
    Player/Creature should implement this class
    """

    def action(self, world):
        raise NotImplementedError

    @classmethod
    def create(cls, **kwargs):
        raise NotImplementedError()
