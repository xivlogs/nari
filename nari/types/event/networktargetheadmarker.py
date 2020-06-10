"""This event triggers an 'effect marker' to appear over an actor's head"""

from nari.types.event.base import Event
from nari.types.actor import Actor
from nari.types.event import Type

class NetworkTargetHeadMarker(Event):
    """Sets the model to use for the marker over a player's head"""
    __id__ = Type.networktargetheadmarker.value
    def handle_params(self):
        self.target_actor = Actor(self.params[0], self.params[1])
        # there's 6 other bytes afterwards:
        # params[2]: junk, literally padding from the Message IPC header
        # params[3]: padding
        # params[4]: model ID
        # params[5]: unused
        # params[6]: unused
        # params[7]: unused

    def __repr__(self):
        return f'<HeadMarker ({self.target_actor})>'
