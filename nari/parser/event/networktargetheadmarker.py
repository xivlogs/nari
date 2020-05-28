from nari.parser.event.base import Event
from nari.types.actor import Actor
from nari.types.event import Type

class NetworkTargetHeadMarker(Event):
    """Looks like it identifies the type of marker over someone's head iunno"""
    __id__ = Type.networktargetheadmarker
    def handle_params(self):
        self.targetActor = Actor(self.params[0], self.params[1])
    
    def __repr__(self):
        return f'<HeadMarker ({self.targetActor})>'