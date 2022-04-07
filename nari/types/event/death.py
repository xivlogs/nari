"""Class that represents an Actor dying"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor


class Death(Event): # pylint: disable=too-few-public-methods
    """Represents an Actor dying"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 source_actor: Actor,
                 target_actor: Actor,
                ):
        super().__init__(timestamp)
        self.source_actor = source_actor
        self.target_actor = target_actor

    def __repr__(self):
        return '<Death>'
