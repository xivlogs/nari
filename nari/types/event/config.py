"""Class that represents configuration value(s)"""
from datetime import datetime
from typing import Dict

from nari.types.event import Event

class Config(Event): # pylint: disable=too-few-public-methods
    """Represents a version string found in the events"""
    def __init__(self, *,
                 timestamp: datetime,
                 values: Dict[str, str]
                ):
        super().__init__(timestamp)
        self.values = values

    def __repr__(self):
        return f'<Config {self.values.items()}>'
