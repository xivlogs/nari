"""Class that represents gauge events"""
from typing import Tuple

from nari.types import Timestamp
from nari.types.event import Event


class Gauge(Event):  # pylint: disable=too-few-public-methods
    """Represents the gauge state of any job"""

    def __init__(self, *,
                 timestamp: Timestamp,
                 actor_id: int,
                 fields: Tuple[bytes, ...],
                ):
        super().__init__(timestamp)
        self.actor_id = actor_id
        self.fields = fields

    def __repr__(self):
        return '<Gauge>'
