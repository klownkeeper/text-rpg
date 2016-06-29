from units.charaters.classes.abstract_class import AbstractClass
from items.weapon_types import *

        
class Fighter(AbstractClass):
    """
    docstring for Fighter
    """

    name = "fighter"
    description = "fighter class"

    hit_dice = "1d10"

    feat_bonus = (1, 1, 0, 1, 0, 1, 0, 1, 0, 1,
                  0, 1, 0, 1, 0, 1, 0, 1, 0, 1)

    attack_bonus = (
        (1),
        (2),
        (3),
        (4),
        (5),
        (6, 1),
        (7, 2),
        (8, 3),
        (9, 4),
        (10, 5),
        (11, 6, 1),
        (12, 7, 2),
        (13, 8, 3),
        (14, 9, 4),
        (15, 10, 5),
        (16, 11, 6, 1),
        (17, 12, 7, 2),
        (18, 13, 8, 3),
        (19, 13, 9, 4),
        (20, 15, 10, 5)
    )

    fortitude_bonus = (
        2, 3, 3, 4, 4,
        5, 5, 6, 6, 7,
        7, 8, 8, 9, 9,
        10, 10, 11, 11, 12
    )

    reflex_bonus = (
        0, 0, 1, 1, 1,
        2, 2, 2, 3, 3,
        3, 4, 4, 4, 5,
        5, 5, 6, 6, 6
    )

    will_bonus = (
        0, 0, 1, 1, 1,
        2, 2, 2, 3, 3,
        3, 4, 4, 4, 5,
        5, 5, 6, 6, 6
    )

    enable_weapon_armor = [SIMPLE, MARTIAL]

    def feats_bonus_on_level(self, level):
        """
        return list of feats on level
        """
        raise NotImplementedError

    def attack_bonus_on_level(self, level):
        """
        return list of attack_bonus on level
        """
        raise NotImplementedError
    
    def saving_throw_bonus_on_level(self, level):
        """
        return list of attack_bonus on level
        """
        raise NotImplementedError

    def ability_bonus_on_level(self, level):
        """
        return list of feats on level
        """
        raise NotImplementedError

    def check_requirement(self):
        """
        check player requirements. before get level
        """
        raise NotImplementedError

    def avaliable_weapon_armor(self):
        raise NotImplementedError

    def class_skills_list(self):
        raise NotImplementedError
