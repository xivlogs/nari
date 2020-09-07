"""Stuff for limitbreak"""
from datetime import datetime

from nari.types.event import Event


class LimitBreak(Event): # pylint: disable=too-few-public-methods
    """Event represents the gain towards the limit break far"""
    def __init__(self, *,
                 timestamp: datetime,
                 amount: int,
                 bars: int):
        super().__init__(timestamp)
        self.amount = amount
        self.bars = bars

    def __repr__(self):
        return '<LimitBreak>'
