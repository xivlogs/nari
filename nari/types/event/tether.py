"""
Tethers
~~~~~~~
"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor


class Tether(Event): # pylint: disable=too-few-public-methods
    """Represents a tether

    :param timestamp: The timestamp of the event
    :type timestamp: Timestamp
    :param source_actor: The actor that initiated the tether
    :type source_actor: Actor
    :param target_actor: The target actor of the tether
    :type target_actor: Actor
    :param tether_id: The id of the tether
    :type tether_id: int
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 source_actor: Actor,
                 target_actor: Actor,
                 tether_id: int,
                ):
        super().__init__(timestamp)
        self.source_actor = source_actor
        self.target_actor = target_actor
        self.tether_id = tether_id

    def __repr__(self):
        return f'<Tether {self.target_actor.name} with {self.tether_id}>'
