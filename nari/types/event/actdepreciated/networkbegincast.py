"""This event represents someone starting to cast"""

from nari.types.event.base import Event
from nari.types.event import Type
from nari.types.actor import Actor
from nari.types.ability import Ability

class NetworkBeginCast(Event):
    """NetworkBeginCast"""
    __id__ = Type.networkbegincast.value
    def handle_params(self):
        self.source_actor = Actor(self.params[0], self.params[1])
        self.ability = Ability(self.params[2], self.params[3])
        self.target_actor = Actor(self.params[4], self.params[5])
        # I *think* params[6] is the cast time

    def __repr__(self):
        return f'<NetworkBeginCast {self.source_actor.name} --({self.ability.name})--> {self.target_actor.name}>'
