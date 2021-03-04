from datetime import datetime
from typing import Tuple

from nari.types.event import Event
from nari.types.actor import Actor


class Gauge(Event):  # pylint: disable=too-few-public-methods
    """Represents the gauge status for any job"""

    def __init__(self, *,
                 timestamp: datetime,
                 actor_id: int,  # can only store gauge events of the user, name not in log line
                 fields: Tuple[bytes, ...],
                 ):
        super().__init__(timestamp)
        self.actor_id = actor_id
        self.fields = fields

    def __eq__(self, other):
        return all((self.timestamp == other.timestamp, self.actor_id == other.actor_id, self.fields == other.fields))

    def __repr__(self):
        return '<Gauge>'

