"""Parses lb information from act log line"""

from datetime import datetime
from typing import List

from nari.types.event import Event
from nari.types.event.limitbreak import LimitBreak

def limitbreak_from_logline(timestamp: datetime, params: List[str]) -> Event:
    """Helper function to parse limit break"""
    # param layout from act
    # 0 - bar amount; 10,000 = 1 full bar
    # 1 - number of bars (3 for 3 full limit bars)
    amount = int(params[0], 16)
    bars = int(params[1])
    return LimitBreak(
        timestamp=timestamp,
        amount=amount,
        bars=bars
    )
