"""Class to manage updates to Actor resources"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor


# pylint: disable=duplicate-code

class UpdateHpMp(Event): # pylint: disable=too-few-public-methods
    """Represents the updating of resources on an actor"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 actor: Actor,
                 hp: int,
                 mp: int,
                 sp: int,
                ):
        super().__init__(timestamp)
        self.actor = actor
        self.hp = hp
        self.mp = mp
        self.sp = sp

    def __repr__(self):
        return '<UpdateHpMp>'
