"""Class that represents ability usages"""
from datetime import datetime

from nari.types.actor import Actor
from nari.types.ability import Ability as AbilityObj

class Ability(Event): # pylint: disable=too-few-public-methods
    """Represents an ability use"""
    def __init__(self, *, timestamp: datetime, source_actor: Actor, target_actor: Actor, ability: AbilityObj, damage: int):
        super().__init__(timestamp)
        self.source_actor = source_actor
        self.target_actor = target_actor
        self.ability = ability
        self.damage = damage

    def __repr__(self):
        return '<Ability>'
