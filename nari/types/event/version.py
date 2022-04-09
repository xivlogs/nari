"""Class that represents version(s)"""
from nari.types import Timestamp
from nari.types.event import Event

class Version(Event): # pylint: disable=too-few-public-methods
    """Represents a version string found in the events"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 version: str,
                ):
        super().__init__(timestamp)
        self.version = version

    def __repr__(self):
        return '<Version>'
