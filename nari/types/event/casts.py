"""Class for cast bars"""
from enum import IntEnum, auto

from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor
from nari.types.ability import Ability


class CastStart(Event): # pylint: disable=too-few-public-methods
    """Represents the preparation towards a cast"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 source_actor: Actor,
                 ability: Ability,
                 target_actor: Actor,
                 duration: float,
                ):
        super().__init__(timestamp)
        self.source_actor = source_actor
        self.ability = ability
        self.target_actor = target_actor
        self.duration = duration

    def __repr__(self):
        return '<CastStart>'


# pylint: disable=invalid-name
class CastStopCategory(IntEnum):
    """Represents reasons a cast could be interrupted"""
    Interrupted = auto()
    Cancelled = auto()
    Unknown = auto()

    @classmethod
    def value_from_name(cls, name: str):
        """Shorthand class method to get the string name from a matching int"""
        return cls.__members__.get(name, cls.Unknown)
# pylint: enable=invalid-name


class CastStop(Event): # pylint: disable=too-few-public-methods
    """Represents a cast being stopped before completion"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 source_actor: Actor,
                 ability: Ability,
                 cause: CastStopCategory,
                ):
        super().__init__(timestamp)
        self.source_actor = source_actor
        self.ability = ability
        self.cause = cause

    def __repr__(self):
        return f'<CastStop {self.cause}>'
