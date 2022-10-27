"""
DoTs and HoTs
~~~~~~~~~~~~~

Events that represents ticks of statuses with periodic effects
"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor


class DamageOverTime(Event): # pylint: disable=too-few-public-methods
    """Represents a damage tick

    :param timestamp: Timestamp of the event
    :type timestamp: Timestamp
    :param actor: Actor that receives the damage
    :type actor: Actor
    :param effect_id: The associated dot status id
    :type effect_id: int
    :param value: The amount of damage
    :type value: int
    """
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
    """Represents a heal tick

    :param timestamp: Timestamp of the event
    :type timestamp: Timestamp
    :param actor: The actor that receives the heal
    :type actor: Actor
    :param effect_id: The associated hot status id
    :type effect_id: int
    :param value: The amount of healing
    :type value: int
    """
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
