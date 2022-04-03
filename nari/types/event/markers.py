"""Events for markers"""
from enum import Enum

from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor

# pylint: disable=invalid-name
class PlayerMarkerType(Enum):
    """Enums for player-assigned markers, these IDs can be found in the Marker.exd client file"""
    Attack1 = 1
    Attack2 = 2
    Attack3 = 3
    Attack4 = 4
    Attack5 = 5
    Bind1 = 6
    Bind2 = 7
    Bind3 = 8
    Ignore1 = 9
    Ignore2 = 10
    Square = 11
    Circle = 12
    Plus = 13
    Triangle = 14

class ContentMarker(Event): # pylint: disable=too-few-public-methods
    """Event representing content-applied markers"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 actor: Actor,
                 marker_id: int):
        super().__init__(timestamp)
        self.actor = actor
        self.marker_id = marker_id

    def __repr__(self):
        return f'<ContentMarker {self.marker_id}>'
