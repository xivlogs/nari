"""Represents a buff being applied. Seen also with statuseffect"""
from nari.types.event.base import Event
from nari.types.event import Type

class NetworkBuff(Event):
    """NetworkBuff"""
    __id__ = Type.networkbuff.value
    def __repr__(self):
        return f'<NetworkBuff ({self.params[4]})>'
