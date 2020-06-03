"""Represents an ability being cancelled for one reason or another"""

from nari.types.event.base import Event
from nari.types.actor import Actor
from nari.types.ability import Ability
from nari.types.event import Type

class CancelAbility(Event):
    """Represents an ability that was cancelled for one reason or another"""
    __id__ = Type.networkcancelability
    def handle_params(self):
        self.actor = Actor(self.params[0], self.params[1])
        self.ability = Ability(self.params[2], self.params[3])

    def __repr__(self):
        return f'<AbilityCancelled ({self.actor.name} X {self.ability.name})>'
