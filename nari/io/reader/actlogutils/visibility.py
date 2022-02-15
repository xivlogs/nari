"""Parses visibility data from act log data"""

from datetime import datetime
from typing import List

from nari.types.actor import Actor
from nari.types.event import Event
from nari.types.event.visibility import VisibilityChange, VisibilityState, VisibilityType

def visibility_from_logline(timestamp: datetime, params: List[str]) -> Event:
    """Parses a VisibilityChange event from an act log line

    ACT Event ID (decimal): 34

    ## Param layout from act

    The first two params in every event is the act event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Source actor ID|
    |1    |string|Source actor name|
    |2    |int|Target actor ID|
    |3    |string|Target actor name|
    |4    |int|0 for invisible, 1 for visible|
    
    """
    actor = Actor(*params[0:2])
    visibility = VisibilityState(int(params[4]))
    return VisibilityChange(
        timestamp=timestamp,
        actor=actor,
        visibility_type=VisibilityType.Nameplate,
        state=visibility
    )
