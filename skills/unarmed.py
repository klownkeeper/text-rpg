from skills import DamageSkill
from settings import TURN_CONST


class UnarmedAttack(DamageSkill):

    skill_name = "unarmed_attack"
    skill_description = "unarmed attack"
    skill_type = "damage"
    skill_cost = 0
    skill_cooldown = TURN_CONST

    skill_attack_bonus = 0
    skill_damage = '1d8'
