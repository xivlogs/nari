"""Class that represents an Actor spawning"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor


class ActorSpawn(Event): # pylint: disable=too-few-public-methods,duplicate-code
    """Represents an Actor spawning"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 actor: Actor,
                ):
        super().__init__(timestamp)
        # we might need to do more with this actor
        self.actor = actor

    def __repr__(self):
        return '<ActorSpawn>'
