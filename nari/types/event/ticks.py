"""Class that represents ticks of statuses with periodic effects"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor


class DamageOverTime(Event): # pylint: disable=too-few-public-methods
    """Represents a damage tick"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 actor: Actor,
                 effect_id: int,
                 value: int,
                ):
        super().__init__(timestamp)
        self.actor = actor
        self.effect_id = effect_id
        self.value = value

    def __repr__(self):
        return '<DoT>'


class HealOverTime(Event): # pylint: disable=too-few-public-methods
    """Represents a heal tick"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 actor: Actor,
                 effect_id: int,
                 value: int,
                ):
        super().__init__(timestamp)
        self.actor = actor
        self.effect_id = effect_id
        self.value = value

    def __repr__(self):
        return '<HoT>'
