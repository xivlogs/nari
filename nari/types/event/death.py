"""
Death
~~~~~
"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor


class Death(Event): # pylint: disable=too-few-public-methods
    """Represents the death of an actor

    :param timestamp: Timestamp of the event
    :type timestamp: Timestamp
    :param source_actor: The (actor) cause of the actor's death, if relevant
    :type source_actor: Actor
    :param target_actor: The actor that died
    :type target_actor: Actor
    """
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
