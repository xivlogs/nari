"""
Gauge Event(s)
~~~~~~~~~~~~~~
"""
from typing import Tuple

from nari.types import Timestamp
from nari.types.event import Event


class Gauge(Event):  # pylint: disable=too-few-public-methods
    """Represents the gauge state of any job

    :param timestamp: The timestamp of the event
    :type timestamp: Timestamp
    :param actor_id: The actor id that this gauge event corresponds to
    :type actor_id: int
    :param fields: An array of bytes that correspond to the gauge event
    :type fields: Tuple[bytes, ...]
    """

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
