from nari.types.event.base import Event
from nari.types.event import Type

class NetworkUpdateHP(Event):
    """NetworkUpdateHP"""
    __id__ = Type.networkupdatehp.value
    def __repr__(self):
        return f'<NetworkUpdateHP ({self.params[1]})>'