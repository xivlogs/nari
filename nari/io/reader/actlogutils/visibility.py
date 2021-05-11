"""Parses visibility data from act log data"""

from datetime import datetime
from typing import List

from nari.types.actor import Actor
from nari.types.event import Event
from nari.types.event.visibility import VisibilityChange, VisibilityState, VisibilityType

def visibility_from_logline(timestamp: datetime, params: List[str]) -> Event:
    """Parses networknametoggle from act log line"""
    # param layout from act
    # 0-1 source actor name/id
    # 2-3 target actor name/id
    # 4 0 for invisible, 1 for visible
    actor = Actor(*params[0:2])
    visibility = VisibilityState(int(params[4]))
    return VisibilityChange(
        timestamp=timestamp,
        actor=actor,
        visibility_type=VisibilityType.Nameplate,
        state=visibility
    )
