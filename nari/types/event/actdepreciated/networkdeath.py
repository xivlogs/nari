"""This event generates when someone (player or npc) dies"""

from nari.types.event.base import Event
from nari.types.event import Type
from nari.types.actor import Actor

class Death(Event):
    """Someone made an oopsie"""
    __id__ = Type.networkdeath.value
    def handle_params(self):
        self.target_actor = Actor(self.params[0], self.params[1])
        self.source_actor = Actor(self.params[2], self.params[3])
        # there's a params[4], but it's empty??

    def __repr__(self):
        return f'<Death ({self.target_actor})>'
