from units.characters import Character
from settings import TURN_CONST
from decorators import enemy_exist
from units.const import *
from encounter.const import *


class Fighter(Character):

    name = "Fighter"
    initiative = 10.0

    unit_hp = 10
    unit_mp = 10
    unit_hp_max = 10
    unit_mp_max = 10

    action_list = {
        "short_sword": {
            'skill_attack': 1,
            'skill_damage': '1d8',
            'skill_cost': 0,
            'skill_cooldown': TURN_CONST,
            'skill_bonus_ability': STRENGTH,
            'skill_effect': None,
        },
        "rest": {
            'skill_attack': 0,
            'skill_damage': '1d4',
            'skill_cost': 0,
            'skill_cooldown': TURN_CONST,
            'skill_bonus_ability': STRENGTH,
            'skill_effect': None,
        }
    }

    @enemy_exist
    def action(self, world):
        command, target_idx = self.get_command(world)
        if command == "short_sword":
            attack_roll = world.attack_roll(
                    world.unit_list.index(self), target_idx, command)
            if attack_roll == ATTACK_ROLL_HIT:
                world.damage_roll(
                    world.unit_list.index(self), target_idx, command)
            elif attack_roll == ATTACK_ROLL_CRITICAL:
                world.damage_roll(
                    world.unit_list.index(self), target_idx, command)
            else:
                pass
            attacker_id = world.unit_list.index(self)
            world.cooldown_list[attacker_id] = self.action_list[command]['skill_cooldown']

        elif command == "rest":
            world.heal(
                world.unit_list.index(self),
                world.unit_list.index(self),
                command)
