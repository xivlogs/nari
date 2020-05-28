from nari.parser.event.base import Event
from nari.types.event import Type
from nari.types.actor import Actor
from nari.types.ability import Ability as AbilityType

class Ability(Event):
    """A 'cast' event"""
    __id__: int = Type.networkability.value

    def handle_params(self):
        self.sourceActor = Actor(self.params[0], self.params[1])
        self.ability = AbilityType(self.params[2], self.params[3])
        self.targetActor = Actor(self.params[4], self.params[5])
        # I don't have enough data on the rest
    
    def __repr__(self):
        return f'<Ability ({self.ability.name})>'