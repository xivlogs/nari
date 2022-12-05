"""
ActorSpawn
~~~~~~~~~~
"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor


class ActorSpawn(Event): # pylint: disable=too-few-public-methods,duplicate-code
    """Represents an actor spawning

    :param timestamp: Timestamp of the event
    :type timestamp: Timestamp
    :param actor: The actor that spawned
    :type actor: Actor
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 actor: Actor,
                ):
        super().__init__(timestamp)
        # we might need to do more with this actor
        self.actor = actor

    def __repr__(self):
        return '<ActorSpawn>'
