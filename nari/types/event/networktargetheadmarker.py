from nari.types.event.base import Event
from nari.types.actor import Actor
from nari.types.event import Type

class NetworkTargetHeadMarker(Event):
    """Looks like it identifies the type of marker over someone's head iunno"""
    __id__ = Type.networktargetheadmarker.value
    def handle_params(self):
        self.targetActor = Actor(self.params[0], self.params[1])
        # there's 6 other bytes afterwards:
        # params[2]: dunno
        # params[3]: dunno
        # params[4]: I think this is the type of marker
        # params[5]: dunno
        # params[6]: dunno
        # params[7]: dunno
    
    def __repr__(self):
        return f'<HeadMarker ({self.targetActor})>'