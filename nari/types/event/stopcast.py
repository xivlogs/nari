"""Class that represents a cast being interrupted or cancelled"""

from datetime import datetime
from enum import IntEnum, auto

from nari.types.event import Event
from nari.types.actor import Actor
from nari.types.ability import Ability as AbilityObj


class StopCastType(IntEnum):
    Interrupted = auto()
    Cancelled = auto()
    Unknown = auto()

    @classmethod
    def value_from_name(cls, name: str):
        return cls.__members__.get(name, cls.Unknown)


class StopCast(Event): # pylint: disable=too-few-public-methods
    """An ability that hits multiple people"""
    def __init__(self, *,
                 timestamp: datetime,
                 source_actor: Actor,
                 ability: AbilityObj,
                 cast_type: StopCastType):
        super().__init__(timestamp)
        self.source_actor = source_actor
        self.ability = ability
        self.cast_type = cast_type

    def __repr__(self):
        return '<AoEAbility>'
