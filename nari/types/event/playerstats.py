"""Type for when player stats change"""
from datetime import datetime
from typing import Dict
from nari.types.event import Event

class PlayerStats(Event): # pylint: disable=too-few-public-methods
    """Represents the event when the player's stats change. Also happens when
    zone/instance changes.
    """
    def __init__(self, timestamp: datetime,
                 stats: Dict[str, int],
                 ):
        super().__init__(timestamp)
        self.stats = stats

    def __repr__(self):
        return '<PlayerStats>'
