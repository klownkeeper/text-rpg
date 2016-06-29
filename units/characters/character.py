from units.characters import AbstractCharacter
from units.characters import classes
from utils import dice
from decorators import enemy_exist


class Character(AbstractCharacter):
    """
    Abstract characters
    Strength   Dexterity  Constitution  Intelligence  Wisdom   Charisma
    """

    char_level = 1
    char_goal = 100

    char_race = "human"
    char_gender = "male"
    char_alignment = "true_neutral"

    action_list = {}
    items = []

    classes = [[classes.Fighter, 1]]

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
               init_weapon=None,
            ):
        char_class = start_class()
        char = Character(
                name = name,
                classes = [[start_class(), 1]],
                unit_str = 10+str_modify,
                unit_dex = 10+dex_modify,
                unit_con = 10+con_modify,
                unit_int = 10+int_modify,
                unit_wis = 10+wis_modify,
                unit_chr = 10+chr_modify,
                unit_main_weapon = init_weapon
        )
        hp_max = dice(char_class.hit_dice) + char.con_modifier
        print("%s created, hit dice get %d hp" % (name, hp_max))
        if hp_max < 1:
            hp_max = 1
        char.unit_hp_max = hp_max
        char.unit_hp = hp_max
        return char

    def gain_level(self, class_gain):
        """docstring for gain_level"""
        pass
