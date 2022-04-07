"""Class that represents the Limit Break gauge state"""
from nari.types import Timestamp
from nari.types.event import Event


class LimitBreak(Event): # pylint: disable=too-few-public-methods
    """Represents changes to the value of the Limit Break bar"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 amount: int,
                 bars: int,
                ):
        super().__init__(timestamp)
        self.amount = amount
        self.bars = bars

    def __repr__(self):
        return '<LimitBreak>'
