"""
Zone
~~~~
"""
from nari.types import Timestamp
from nari.types.event import Event

class ZoneChange(Event): # pylint: disable=too-few-public-methods
    """Represents a change in zone

    :param timestamp: The timestamp of the event
    :type timestamp: Timestamp
    :param zone_id: The zone being transitioned into
    :type zone_id: int
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 zone_id: int,
                ):
        super().__init__(timestamp)
        self.zone_id = zone_id

    def __repr__(self):
        return '<ZoneChange>'
