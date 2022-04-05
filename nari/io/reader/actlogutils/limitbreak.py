"""Parses LB bar state data from ACT log line"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.event.limitbreak import LimitBreak

def limitbreak_from_logline(timestamp: Timestamp, params: list[str]) -> Event:
    """Parses a limit break event from an act log line

    ACT Event ID (decimal): 36

    ## Param layout from act

    The first two params in every event is the act event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Bar amount; 10,000 = 1 full bar.|
    |1    |int|Number of bars (3 for 3 full limit bars).|
    """
    amount = int(params[0], 16)
    bars = int(params[1])
    return LimitBreak(
        timestamp=timestamp,
        amount=amount,
        bars=bars
    )
