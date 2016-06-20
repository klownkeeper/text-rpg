from settings import TURN_CONST
from encounter.exceptions import SkillFailException
from utils import saving_throw_success


class Skill(object):
    """docstring for Skill"""

    skill_name = "abstract_skill" # used as command
    skill_description = "Abstract Skill"
    skill_type = None # damage, heal, effect
    skill_cost = 0
    skill_cooldown = TURN_CONST

    def cast(self, **kwargs):
        raise NotImplementedError
        
    def precondition_check(self, **kwargs):
        raise NotImplementedError


class DamageSkill(Skill):
    """docstring for DamageSkill"""
    skill_name = "abstract_skill" # used as command
    skill_description = "Abstract Skill"
    skill_type = None # damage, heal, effect
    skill_cost = 0
    skill_cooldown = TURN_CONST

    skill_attack_bonus = 0
    skill_damage = '1d8'

    def cast(self, world, from_id, to_id):
        """docstring for ca"""
        self.precondition_check(world)
        # reflex saving throw

    def precondition_check(self, world, from_id, to_id):
        self_mp = world.unit_list[from_id].unit_mp
        if self_mp < self.skill_cost:
            raise SkillFailException(
                "Skill %s need %d mp to cast, but only %d mp left",
                self.skill_name, self.skill_cost, self_mp)
        


class HealSkill(Skill):
    """docstring for DamageSkill"""
    skill_name = "abstract_skill" # used as command
    skill_description = "Abstract Skill"
    skill_type = None # damage, heal, effect
    skill_cost = 0
    skill_cooldown = TURN_CONST

    skill_attack_bonus = 0
    skill_damage = '1d8'
