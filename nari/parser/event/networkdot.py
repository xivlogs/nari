from nari.parser.event.base import Event
from nari.types.actor import Actor
from nari.types.event import Type

class NetworkDot(Event):
    """Represents Dot AND Hot values"""
    __id__ = Type.networkdot.value
    def handle_params(self):
        self.actor = Actor(self.params[0], self.params[1])
        self.ticktype = self.params[2]
        # not sure about the rest of the params
    
    def __repr__(self):
        return f'<{self.ticktype} ({self.actor})>'