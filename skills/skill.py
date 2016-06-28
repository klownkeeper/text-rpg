from settings import TURN_CONST


class AbstractSkill(object):
    """
    Abstract class for all unit skills.
    including:
    attack,
    feat,
    cast spell,
    use item,
    etc
    """

    name = None
    description = None
    cooldown = TURN_CONST
