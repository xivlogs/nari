"""Class that represents configuration value(s)"""
from typing import Dict

from nari.types import Timestamp
from nari.types.event import Event

class Config(Event): # pylint: disable=too-few-public-methods
    """Represents a version string found in the events"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 values: Dict[str, str]
                ):
        super().__init__(timestamp)
        self.values = values

    def __repr__(self):
        return f'<Config {self.values.items()}>'
