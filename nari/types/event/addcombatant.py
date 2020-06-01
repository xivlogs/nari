from nari.types.event.base import Event
from nari.types.event import Type
from nari.types.actor import Actor

class AddCombatant(Event):
    """Adding an actor to the field"""
    __id__ = Type.addcombatant.value
    def handle_params(self):
        self.actor = Actor(self.params[0], self.params[1])
    
    def __repr__(self):
        return f'<AddCombatant ({self.actor})>'