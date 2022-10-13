"""
Event
~~~~~

Base event that all other event types inherit from.
"""
from nari.types import Timestamp

class Event(): # pylint: disable=too-few-public-methods
    """Initializes a base event with a timestamp

    :param timestamp: Number of milliseconds since the unix epoch
    :type timestamp: Timestamp
    """
    def __init__(self, timestamp: Timestamp):
        """Constructor method
        """
        self.timestamp = timestamp

    def __repr__(self):
        return '<Event>'
