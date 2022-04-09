"""Classes for visibility state management"""
from enum import Enum, auto

from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor

# pylint: disable=invalid-name
class VisibilityCategory(Enum):
    """Enums for concepts that have visibility"""
    Nameplate = auto()


class VisibilityState(Enum):
    """Enum for the state of the visiblity change"""
    Invisibile = 0
    Visible = 1


class VisibilityChange(Event): # pylint: disable=too-few-public-methods
    """Represents a visibility change"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 actor: Actor,
                 visibility_category: VisibilityCategory,
                 state: VisibilityState,
                ):
        super().__init__(timestamp)
        self.actor = actor
        self.visibility_category = visibility_category
        self.state = state

    def __repr__(self):
        return f'<Visibility {self.visibility_category.name}>'
