from skills.skill import AbstractSkill


class Spell(AbstractSkill):
    """
    Abstract class for Spell
    """

    level = 0

    def effect(self, world, **kwargs):
        raise NotImplementedError("Spell class need effect function")
        
