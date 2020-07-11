"""You'll see this every time an actor is targeted by a hostile action"""

from nari.types.event.base import Event
from nari.types.event import Type

class NetworkEffectResult(Event):
    """Apparently, this is any time an actor is targeted by a hostile action"""
    __id__ = Type.networkeffectresult
    def __repr__(self):
        return f'<EffectResult ({self.params[1]})>'
