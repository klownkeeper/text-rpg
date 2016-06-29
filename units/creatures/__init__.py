from units import Unit
from encounter.exceptions import *
from encounter import const
from utils import dice


class Creature(Unit):
    """docstring for Abstract Creature"""

    unit_exp = 1

    creature_hit_dice = "1d4"

    def choose_action(self, world):
        if len(self.enemy_list(world)) == 0:
            raise NoEnemyException
        return "attack", self.enemy_list(world)[0]

    def action(self, world):
        action, *args = self.choose_action(world)
        self.dispatch(action, world, *args)

    @classmethod
    def create(cls, **kwargs):
        creature = cls(**kwargs)
        hp_max = 0
        for l in range(creature.unit_level):
            hp = dice(creature.creature_hit_dice) + creature.con_modifier
            if hp < 1:
                hp = 1
            hp_max += hp
        creature.unit_hp_max = hp_max
        creature.unit_hp = hp_max
        print("create %s with %d hp" % (creature.name, creature.unit_hp))
        return creature
        
