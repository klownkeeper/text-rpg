from encounter.turn_manager import TurnManager
from encounter.throws import AttackThrowMixin, DamageThrowMixin

class Encounter(AttackThrowMixin, DamageThrowMixin, TurnManager):

    def heal(self, healer_id, target_id, skill_name):
        healer = self.unit_list[healer_id]
        target = self.unit_list[target_id]
        skill = healer.action_list[skill_name]
        cost = skill['skill_cost']
        if cost > healer.unit_mp:
            # print("* %s failed to heal %s by %s: MP(%d) not enough" % (
            #     healer.name, target.name, skill_name, healer.unit_mp))
            self.cooldown_list[healer_id] = TURN_CONST
            return
        damage = skill['skill_damage']
        attack = skill['skill_attack']
        damage_deal = dice(damage) + attack
        if damage_deal + target.unit_hp > target.unit_hp_max:
            damage_deal = target.unit_hp_max - target.unit_hp
        self.unit_list[target_id].unit_hp += damage_deal
        self.unit_list[healer_id].unit_mp -= cost
        self.cooldown_list[healer_id] = skill['skill_cooldown']
        target_heal_print(
            name=healer.name, action_name=skill_name,
            target_name=target.name, damage=damage_deal,
            target_hp=target.unit_hp, message="")
        
