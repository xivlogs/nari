"""Base event that all other event types inherit from"""
from nari.types import Timestamp

class Event(): # pylint: disable=too-few-public-methods
    """Represents a barebones event in nari.

    The only real thing this event records is the timestamp the event occurs at.
    """
    def __init__(self, timestamp: Timestamp):
        """Initializes a barebones event with a timestamp

        :param timestamp: Number of milliseconds since the unix epoch
        """
        self.timestamp = timestamp

    def __repr__(self):
        return '<Event>'
