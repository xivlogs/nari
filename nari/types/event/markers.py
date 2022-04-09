"""Classes for overhead markers"""
from enum import IntEnum

from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor


class OverheadVFX(Event): # pylint: disable=too-few-public-methods
    """Event representing content-applied markers"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 actor: Actor,
                 marker_id: int,
                ):
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
class PlayerMarker(IntEnum):
    """Enums for player-applied markers, these IDs can be found in the Marker.exd client file"""
    Attack1 = 0
    Attack2 = 1
    Attack3 = 2
    Attack4 = 3
    Attack5 = 4
    Bind1 = 5
    Bind2 = 6
    Bind3 = 7
    Ignore1 = 8
    Ignore2 = 9
    Square = 10
    Circle = 11
    Plus = 12
    Triangle = 13

    @classmethod
    def contains(cls, value: int) -> bool:
        """Returns true if the value is a valid PlayerMarkerType"""
        return value in cls._value2member_map_ # pylint: disable=no-member


class OverheadMarker(Event): # pylint: disable=too-few-public-methods
    """Event representing player-applied markers"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 source_actor: Actor,
                 target_actor: Actor,
                 operator: MarkerOperation,
                 marker: PlayerMarker,
                ):
        super().__init__(timestamp)
        self.source_actor = source_actor
        self.target_actor = target_actor
        self.operator = operator
        self.marker = marker

    def __repr__(self):
        return f'<PlayerMarker {self.operator.name} {self.marker.name}>'
