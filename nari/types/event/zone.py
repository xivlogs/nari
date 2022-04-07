"""Class that represents zone transitions"""
from nari.types import Timestamp
from nari.types.event import Event

class ZoneChange(Event): # pylint: disable=too-few-public-methods
    """Represents a change in zone"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 zone_id: int,
                ):
        super().__init__(timestamp)
        self.zone_id = zone_id

    def __repr__(self):
        return '<ZoneChange>'
