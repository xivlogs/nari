"""RemoveCombatant fires when an actor is removed"""

from nari.types.event.base import Event
from nari.types.event import Type

class RemoveCombatant(Event):
    """RemoveCombatant"""
    __id__ = Type.removecombatant.value
    def __repr__(self):
        return f'<RemoveCombatant ({self.params[1]})>'
