"""
Resource updates
~~~~~~~~~~~~~~~~
"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor


# pylint: disable=duplicate-code
class UpdateHpMp(Event): # pylint: disable=too-few-public-methods
    """Represents the updating of resources on an actor

    :param timestamp: The timestamp of the event
    :type timestamp: Timestamp
    :param actor: The actor for which resources are updating
    :type actor: Actor
    :param hp: The current hp value of the actor
    :type hp: int
    :param mp: The current mp value of the actor
    :type mp: int
    :param sp: The current "sp" value of the actor
    :type sp: int
    """
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
