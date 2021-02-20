"""Status effects applied to actors"""

from nari.types.event.base import Event
from nari.types.event import Type

class NetworkStatusEffect(Event):
    """NetworkStatusEffect"""
    __id__ = Type.networkstatuseffect.value
    def __repr__(self):
        return f'<NetworkStatusEffect ({self.params[1]})>'
