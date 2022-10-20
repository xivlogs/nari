"""
Markers and combat-related vfx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from enum import IntEnum

from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor


class OverheadVFX(Event): # pylint: disable=too-few-public-methods
    """Event representing content-applied markers

    :param timestamp: The timestamp of the event
    :type timestamp: Timestamp
    :param actor: The actor the VFX is being applied to
    :type actor: Actor
    :param marker_id: The id of the vfx
    :type marker_id: int
    """
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
    """The operation is unknown"""
    Add = 1
    """The marker is added"""
    Update = 2
    """The marker is updated"""
    Delete = 3
    """The marker is removed"""


# pylint: disable=invalid-name
class PlayerMarker(IntEnum):
    """Enums for player-applied markers, these IDs can be found in the Marker.exd client file"""
    Attack1 = 0
    """Places the (1) marker over the target"""
    Attack2 = 1
    """Places the (2) marker over the target"""
    Attack3 = 2
    """Places the (3) marker over the target"""
    Attack4 = 3
    """Places the (4) marker over the target"""
    Attack5 = 4
    """Places the (5) marker over the target"""
    Bind1 = 5
    """Places the chain marker (with a 1) over the target"""
    Bind2 = 6
    """Places the chain marker (with a 2) over the target"""
    Bind3 = 7
    """Places the chain marker (with a 3) over the target"""
    Ignore1 = 8
    """Places the ignore marker (with a 1) over the target"""
    Ignore2 = 9
    """Places the ignore marker (with a 2) over the target"""
    Square = 10
    """Places a square marker over the target"""
    Circle = 11
    """Places a circle marker over the target"""
    Plus = 12
    """Places a plus marker over the target"""
    Triangle = 13
    """Places a triangle marker over the target"""

    @classmethod
    def contains(cls, value: int) -> bool:
        """Returns true if the value is a valid PlayerMarkerType"""
        return value in cls._value2member_map_ # pylint: disable=no-member


class OverheadMarker(Event): # pylint: disable=too-few-public-methods
    """Event representing player-applied markers

    :param timestamp: The timestamp of the event
    :type timestamp: Timestamp
    :param source_actor: The actor that applied the marker
    :type source_actor: Actor
    :param target_actor: The target that receives the marker
    :type target_actor: Actor
    :param operator: If the marker is being added/removed/modified
    :type operator: MarkerOperation
    :param marker: The marker that goes over the head
    :type marker: PlayerMarker
    """
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
