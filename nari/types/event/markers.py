"""Events for markers"""
from enum import IntEnum

from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor


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


# pylint: disable=invalid-name
class MarkerOperation(IntEnum):
    """Enums for marker operations"""
    Unknown = 0
    Add = 1
    Update = 2
    Delete = 3


# pylint: disable=invalid-name
class PlayerMarkerType(IntEnum):
    """Enums for player-applied markers, these IDs can be found in the Marker.exd client file"""
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

    @classmethod
    def contains(cls, value: int) -> bool:
        """Returns true if the value is a valid PlayerMarkerType"""
        return value in cls._value2member_map_ # pylint: disable=no-member


class PlayerMarker(Event): # pylint: disable=too-few-public-methods
    """Event representing player-applied markers"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 source_actor: Actor,
                 target_actor: Actor,
                 operator: MarkerOperation,
                 marker: PlayerMarkerType):
        super().__init__(timestamp)
        self.source_actor = source_actor
        self.target_actor = target_actor
        self.operator = operator
        self.marker = marker

    def __repr__(self):
        return f'<PlayerMarker {self.operator.name} {self.marker.name}>'
