"""Events that representing updating actor resources"""
from datetime import datetime

from nari.types.event import Event
from nari.types.actor import Actor


class UpdateHpMp(Event): # pylint: disable=too-few-public-methods
    """Event represents the updating of resources on an actor"""
    def __init__(self, *,
                 timestamp: datetime,
                 actor: Actor):
        super().__init__(timestamp)
        self.actor = actor

    def __repr__(self):
        return '<UpdateHpMp>'
