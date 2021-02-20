"""Represents a buff being removed"""

from nari.types.event.base import Event
from nari.types.event import Type

class NetworkBuffRemove(Event):
    """NetworkBuffRemove"""
    __id__ = Type.networkbuffremove.value
    def __repr__(self):
        return f'<NetworkBuffRemove ({self.params[4]})>'
