"""Class that represents blahblahblah"""
from datetime import datetime

from nari.types.event import Event
from nari.types.actor import Actor


class ActorSpawn(Event): # pylint: disable=too-few-public-methods
    """Represents"""
    def __init__(self, *,
                 timestamp: datetime,
                 actor: Actor, # TODO: what to do with actor?
                ):
        super().__init__(timestamp)

    def __repr__(self):
        return '<EffectResult>'
