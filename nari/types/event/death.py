"""Stuff for death of actors"""
from datetime import datetime

from nari.types.event import Event
from nari.types.actor import Actor


class Death(Event): # pylint: disable=too-few-public-methods
    """Event represents the death of an actor"""
    def __init__(self, *,
                 timestamp: datetime,
                 source_actor: Actor,
                 target_actor: Actor,
                ):
        super().__init__(timestamp)
        self.source_actor = source_actor
        self.target_actor = target_actor

    def __repr__(self):
        return '<StatusApply>'
