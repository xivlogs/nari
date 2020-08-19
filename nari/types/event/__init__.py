"""Base event class that all other event types inherit from"""
from datetime import datetime

class Event(): # pylint: disable=too-few-public-methods
    """"Basically just contains the timestamp"""
    def __init__(self, timestamp: datetime):
        self.timestamp = timestamp

    def __repr__(self):
        return '<Event>'
