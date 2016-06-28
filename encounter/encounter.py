from encounter.turn_manager import TurnManager
from encounter.throws import AttackThrowMixin, DamageThrowMixin

class Encounter(AttackThrowMixin, DamageThrowMixin, TurnManager):
    pass
