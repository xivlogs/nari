"""Base event class that all other event types inherit from"""
from nari.types import Timestamp

class Event(): # pylint: disable=too-few-public-methods
    """"Basically just contains the timestamp"""
    def __init__(self, timestamp: Timestamp):
        self.timestamp = timestamp

    def __repr__(self):
        return '<Event>'
