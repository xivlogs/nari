"""Type for when player stats change"""
from datetime import datetime
from typing import List

from nari.types.event import Event
from nari.types.job import Job
from nari.types.stats import Stats


class PlayerStats(Event): # pylint: disable=too-few-public-methods
    """Represents the event when the player's stats change. Also happens when
    zone/instance changes.
    """
    def __init__(self, timestamp: datetime,
                 job: Job,
                 stats: List[Stats],
                 ):
        super().__init__(timestamp)
        self.job = job
        self.stats = stats

    def __repr__(self):
        return '<PlayerStats>'
