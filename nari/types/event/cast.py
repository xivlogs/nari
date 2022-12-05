"""
Cast
~~~~

Events and enums related to starting and stopping a cast.
"""
from enum import IntEnum, auto

from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor
from nari.types.ability import Ability


class CastStart(Event): # pylint: disable=too-few-public-methods
    """Represents the preparation towards a cast

    :param timestamp: Timestamp of the event
    :type timestamp: Timestamp
    :param source_actor: The actor that is starting to cast
    :type source_actor: Actor
    :param ability: The ability being casted
    :type ability: Ability
    :param target_actor: The target of the action
    :type target_actor: Actor
    :param duration: The expected duration of the cast
    :type duration: float
    """
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
    """The cast was interrupted because the actor died, was knocked back, etc"""
    Cancelled = auto()
    """The cast was interrupted because it was cancelled (the actor moved)"""
    Unknown = auto()
    """The reason the cast ended is unknown"""

    @classmethod
    def value_from_name(cls, name: str):
        """Shorthand class method to get the string name from a matching int

        :param name: The string name of the category
        :type name: str
        :return: The enum of the matching key name
        :rtype: CastStopCategory
        """
        return cls.__members__.get(name, cls.Unknown)
# pylint: enable=invalid-name


class CastStop(Event): # pylint: disable=too-few-public-methods
    """Represents a cast being stopped before completion

    :param timestamp: Timestamp of the event
    :type timestamp: Timestamp
    :param source_actor: The actor the cast stopped on
    :type source_actor: Actor
    :param ability: The ability that was interrupted
    :type ability: Ability
    :param cause: The reason the cast stopped
    :type cause: CastStopCategory
    """
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
