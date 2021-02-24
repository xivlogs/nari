"""Parses HP data from act log line"""

from datetime import datetime
from typing import List

from nari.types.event.updatehpmp import UpdateHpMp
from nari.types.actor import Actor

def updatehp_from_logline(timestamp: datetime, params: List[str]) -> UpdateHpMp:
    """Helper function to parse hp data from act log data"""
    # Param layout from act:
    # 0-1 - Actor ID/Name
    # 2-3 - hp/max hp
    # 4-5 - mp/max mp
    # 6-7 - tp/max tp
    # 8-11 - x/y/z/facing
    # 12 - blank because ACT

    actor = Actor(*params[0:2])
    try:
        actor.resources.update(
            *[int(x) for x in params[2:8]]
        )
    except ValueError:
        pass

    return UpdateHpMp(timestamp=timestamp, actor=actor)
