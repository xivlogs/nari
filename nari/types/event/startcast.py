"""Stuff for preparecast"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor
from nari.types.ability import Ability


class StartCast(Event): # pylint: disable=too-few-public-methods
    """Event represents the preparation towards a cast"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 source_actor: Actor,
                 ability: Ability,
                 target_actor: Actor,
                 duration: float):
        super().__init__(timestamp)
        self.source_actor = source_actor
        self.ability = ability
        self.target_actor = target_actor
        self.duration = duration

    def __repr__(self):
        return '<PrepareCast>'
