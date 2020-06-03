"""Different from a regular damage event, this Event represents an ability that hits multiple targets."""

from nari.types.event.base import Event
from nari.types.event import Type

class AoeAbility(Event):
    """AoeAbility"""
    __id__ = Type.networkaoeability.value
    def __repr__(self):
        return f'<AoeAbility ({self.params[3]})>'
