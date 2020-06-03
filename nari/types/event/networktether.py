"""Represents a tether from one actor to another"""

from nari.types.event.base import Event
from nari.types.actor import Actor
from nari.types.event import Type

class NetworkTether(Event):
    """Network tether event"""
    __id__ = Type.networktether.value
    def handle_params(self):
        self.source_actor = Actor(self.params[0], self.params[1])
        self.target_actor = Actor(self.params[2], self.params[3])

    def __repr__(self):
        return f'<Tether ({self.source_actor.name} -> {self.target_actor.name})>'
