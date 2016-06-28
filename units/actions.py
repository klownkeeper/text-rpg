"""
For dispatcher action
Mixins for Unit class
"""
from units import const
from skills import spells
from encounter.const import ATTACK_ROLL_CRITICAL, ATTACK_ROLL_FAILED, ATTACK_ROLL_HIT
from settings import TURN_CONST

from utils import cast_spell_print, cast_spell_success_print

class AttackMixin(object):

    ability_to_attack = const.STRENGTH

    def attack(self, world, target_idx, **kwargs):
        """
        Normal attack action
        All units should have it.
        """
        weapon = self.get_weapon(world)
        attacker_idx = self.get_self_idx(world)
        attack_roll = world.attack_roll(
                attacker_idx, target_idx, self.ability_to_attack)
        if attack_roll == ATTACK_ROLL_HIT:
            world.damage_roll(
                attacker_idx, target_idx,
                weapon['name'], weapon['damage'],
                self.ability_to_attack)
        elif attack_roll == ATTACK_ROLL_CRITICAL:
            world.damage_roll(
                attacker_idx, target_idx,
                weapon['name'], weapon['damage'],
                self.ability_to_attack,
                is_critical=True)
        else:
            pass
        world.cooldown_list[attacker_idx] = TURN_CONST

    def get_weapon(self, world):
        idx = self.get_self_idx(world)
        return world.unit_list[idx].unit_main_weapon

        
class CastSpellMixin(object):

    spell_list = []
    spell_casting = None
    spell_args = ()

    def check_spell_casting(self, world):
        if self.spell_casting:
            self.spell_casting.effect(world, *self.spell_args)

    def cast(self, world, spell_name, *args):
        # 1. put spell to spell_casting.
        spell_cls = "".join(
            list(map(lambda s: s.capitalize(), spell_name.split('_'))))
        self.spell_casting = getattr(spells, spell_cls)()
        self.spell_args = args

        # 2. reset cooldown.
        caster_idx = world.unit_list.index(self)
        world.cooldown_list[caster_idx] = self.spell_casting.cooldown

        cast_spell_print(
            name=world.unit_list[caster_idx].name,
            spell_name=spell_name)
        

class ActionDispatcherMixin(AttackMixin, CastSpellMixin):
    """
    Dispatch action name to functions
    """

    action_name_list = ["attack", "cast"]

    def dispatch(self, name, world, *args):
        self.check_spell_casting(world)
        action_func_name = name
        getattr(self, name)(world, *args)

