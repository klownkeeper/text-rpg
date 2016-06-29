class AbstractClass(object):

    name = "abstract_class"
    description = None

    hit_dice = "1d10"

    feat_bonus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    attack_bonus = [
        [0], [0], [0], [0], [0],
        [0], [0], [0], [0], [0],
        [0], [0], [0], [0], [0],
        [0], [0], [0], [0], [0]
    ]

    fortitude_bonus = [
        2, 3, 3, 4, 4,
        5, 5, 6, 6, 7,
        7, 8, 8, 9, 9,
        10, 10, 11, 11, 12
    ]

    reflex_bonus = [
        0, 0, 1, 1, 1,
        2, 2, 2, 3, 3,
        3, 4, 4, 4, 5,
        5, 5, 6, 6, 6
    ]

    will_bonus = [
        0, 0, 1, 1, 1,
        2, 2, 2, 3, 3,
        3, 4, 4, 4, 5,
        5, 5, 6, 6, 6
    ]

    ability_bonus = [
        0, 0, 0, 1,
        0, 0, 0, 1,
        0, 0, 0, 1,
        0, 0, 0, 1,
        0, 0, 0, 1,
    ]

    enable_weapon_armor = []

    def feats_bonus_on_level(self, level):
        return self.feat_bonus[level]

    def attack_bonus_on_level(self, level):
        return self.attack_bonus[level]
    
    def saving_throw_bonus_on_level(self, level):
        return (
            self.fortitude_bonus[level],
            self.reflex_bonus[level],
            self.will_bonus[level])

    def ability_bonus_on_level(self, level):
        raise NotImplementedError

    def check_requirement(self):
        """
        check player requirements. before get level
        """
        return True

    def avaliable_weapon_armor(self):
        raise NotImplementedError

    def class_skills_list(self):
        raise NotImplementedError
