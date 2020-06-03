"This event fires when a nameplate 'toggles' (becomes visible or invisible)"

from nari.types.event.base import Event
from nari.types.event import Type

class NameToggle(Event):
    """When a nameplate toggles"""
    __id__ = Type.networknametoggle.value
    def __repr__(self):
        return f'<NameToggle ({self.params[2]})>'
