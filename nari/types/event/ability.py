"""Class that represents ability usages"""
from datetime import datetime
from typing import List

from nari.types.event import Event
from nari.types.actor import Actor
from nari.types.ability import Ability as AbilityObj
from nari.types.actioneffect import ActionEffect

class Ability(Event): # pylint: disable=too-few-public-methods
    """Represents an ability use"""
    def __init__(self, *,
                 timestamp: datetime,
                 action_effects: List[ActionEffect],
                 source_actor: Actor,
                 target_actor: Actor,
                 ability: AbilityObj,):
        super().__init__(timestamp)
        self.source_actor = source_actor
        self.target_actor = target_actor
        self.action_effects = action_effects
        self.ability = ability

    def __repr__(self):
        return '<Ability>'
