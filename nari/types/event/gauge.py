"""Class that represents gauge events"""
from datetime import datetime
from typing import Tuple

from nari.types.event import Event


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

    def __repr__(self):
        return '<Gauge>'

