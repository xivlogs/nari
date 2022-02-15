"""Class that represents a cast being interrupted or cancelled"""
from enum import IntEnum, auto

from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor
from nari.types.ability import Ability as AbilityObj


# pylint: disable=invalid-name
class StopCastType(IntEnum):
    """Represents reasons a cast could be interrupted"""
    Interrupted = auto()
    Cancelled = auto()
    Unknown = auto()

    @classmethod
    def value_from_name(cls, name: str):
        """Shorthand class method to get the string name from a matching int"""
        return cls.__members__.get(name, cls.Unknown)
# pylint: enable=invalid-name


class StopCast(Event): # pylint: disable=too-few-public-methods
    """An event that gets stopped by movement, death, or other reasons"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 source_actor: Actor,
                 ability: AbilityObj,
                 cast_type: StopCastType):
        super().__init__(timestamp)
        self.source_actor = source_actor
        self.ability = ability
        self.cast_type = cast_type

    def __repr__(self):
        return '<AoEAbility>'
