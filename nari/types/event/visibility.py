"""Events for visibility"""
from enum import Enum, auto

from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor

# pylint: disable=invalid-name
class VisibilityType(Enum):
    """Enums for concepts that have visibility"""
    Nameplate = auto()


class VisibilityState(Enum):
    """Enum for the state of the visiblity change"""
    Invisibile = 0
    Visible = 1


class VisibilityChange(Event): # pylint: disable=too-few-public-methods
    """Event representing visibility changes"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 actor: Actor,
                 visibility_type: VisibilityType,
                 state: VisibilityState):
        super().__init__(timestamp)
        self.actor = actor
        self.visibility_type = visibility_type
        self.state = state

    def __repr__(self):
        return f'<Visibility {self.visibility_type.name}>'
