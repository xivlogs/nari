"""
Waymarks
~~~~~~~~
Classes for waymarks
"""
from dataclasses import dataclass
from enum import IntEnum

from nari.types import Timestamp
from nari.types.event import Event
from nari.types.event.markers import MarkerOperation
from nari.types.actor import Actor


# pylint: disable=invalid-name
class Waypoint(IntEnum):
    """Enums for waymarks, these IDs can be found in the FieldMarker.exd client file"""
    WaypointA = 1
    WaypointB = 2
    WaypointC = 3
    WaypointD = 4
    Waypoint1 = 5
    Waypoint2 = 6
    Waypoint3 = 7
    Waypoint4 = 8
    Clear = 9

    @classmethod
    def contains(cls, value: int) -> bool:
        """Returns true if the value is a valid Waypoint"""
        return value in cls._value2member_map_ # pylint: disable=no-member


@dataclass
class Position(): # pylint: disable=duplicate-code
    """Holds position data for a Waymark"""
    x: float = 0
    y: float = 0
    z: float = 0


class Waymark(Event): # pylint: disable=too-few-public-methods
    """Represents a waymark placement

    :param timestamp: The timestamp of the event
    :type timestamp: Timestamp
    :param actor: The actor placing the marker
    :type actor: Actor
    :param operator: If the marker is being added/removed/moved/etc
    :type operator: MarkerOperation
    :param marker: The marker being placed
    :type marker: Waypoint
    :param position: The position of the placed marker
    :type position: Position
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 actor: Actor,
                 operator: MarkerOperation,
                 marker: Waypoint,
                 position: Position,
                ):
        super().__init__(timestamp)
        self.actor = actor
        self.operator = operator
        self.marker = marker
        self.position = position

    def __repr__(self):
        return f'<Waymark {self.operator.name} {self.marker.name}>'
