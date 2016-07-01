import itertools

from units.characters import AbstractCharacter
from units.characters import classes as char_classes
from utils import dice
from decorators import enemy_exist


class Character(AbstractCharacter):
    """
    Abstract characters
    Strength   Dexterity  Constitution  Intelligence  Wisdom   Charisma
    """

    char_goal = 100

    char_race = "human"
    char_gender = "male"
    char_alignment = "true_neutral"

    action_list = {}
    items = []

    classes = {
        "Fighter": 1
    }

    @enemy_exist
    def action(self, world):
        command, *args = self.get_command(world)
        self.dispatch(command, world, *args)

    @classmethod
    def create(cls,
               name,
               start_class,
               str_modify=0,
               dex_modify=0,
               con_modify=0,
               int_modify=0,
               wis_modify=0,
               chr_modify=0,
               **kwargs
            ):
        char_class = getattr(char_classes, start_class)()
        char = Character(
                name = name,
                classes = {
                    start_class: 1},
                unit_str = 10+str_modify,
                unit_dex = 10+dex_modify,
                unit_con = 10+con_modify,
                unit_int = 10+int_modify,
                unit_wis = 10+wis_modify,
                unit_chr = 10+chr_modify,
                **kwargs,
        )
        hp_max = dice(char_class.hit_dice) + char.con_modifier
        print("%s created, hit dice get %d hp" % (name, hp_max))
        if hp_max < 1:
            hp_max = 1
        char.unit_hp_max = hp_max
        char.unit_hp = hp_max
        # if char.unit_level > 1:
        #     char.gain_level(char.ask_next_level_class())
        return char

    def gain_level(self, class_gain):
        """docstring for gain_level"""
        # raise NotImplementedError()
        # 1. Increase HP
        c = getattr(char_classes, class_gain)()
        gain_hp = dice(c.hit_dice) + self.con_modifier
        self.unit_hp_max += gain_hp
        self.unit_hp = self.unit_hp_max

        # 2. Increate base attack bonus
        # 3. Increate save throws
        self.unit_fortitude += c.fortitude_bonus[self.unit_level]
        self.unit_reflex += c.reflex_bonus[self.unit_level]
        self.unit_will += c.will_bonus[self.unit_level]
        # 4. gain ability score
        if c.ability_bonus[self.unit_level]:
            ability = self.ask_ability_bonus()
            ability_point = getattr(self, ability) + 1
            setattr(self, ability, ability_point)
        # 5. Allicate skill points
        # 6. add feats
        # 7. classes level + 1
        self.unit_level += 1
        if class_gain in self.classes:
            self.classes[class_gain] += 1
        else:
            self.classes[class_gain] = 1
        print("%s gain a level(LV %d):" % (self.name, self.unit_level))

    def get_base_attack_bonus(self):
        res = []
        for c, lv in self.classes.items():
            cl = getattr(char_classes, c)()
            res = list(map(sum, itertools.zip_longest(res, list(cl.attack_bonus[lv-1]), fillvalue=0)))
        return res

