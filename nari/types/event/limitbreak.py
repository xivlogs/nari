"""Stuff for limitbreak"""
from nari.types import Timestamp
from nari.types.event import Event


class LimitBreak(Event): # pylint: disable=too-few-public-methods
    """Event represents the gain towards the limit break far"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 amount: int,
                 bars: int):
        super().__init__(timestamp)
        self.amount = amount
        self.bars = bars

    def __repr__(self):
        return '<LimitBreak>'
