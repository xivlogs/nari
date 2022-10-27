"""
Visibility
~~~~~~~~~~
Classes for visibility state management
"""
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
    """Represents a change in visibility for an actor

    :param timestamp: The timestamp of the event
    :type timestamp: Timestamp
    :param actor: The actor which is undergoing a visibility change
    :type actor: Actor
    :param visibility_category: The type of visibility that is changing
    :type visibility_category: VisibilityCategory
    :param state: If the actor is becoming invisible or visible
    :type state: VisibilityState
    """
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
