from datetime import datetime
from typing import List

from nari.types.actor import Actor
from nari.types.event import Event
from nari.types.event.death import Death

def death_from_logline(timestamp: datetime, params: List[str]) -> Event:
    # param layout from act
    # 0-1 - 'target actor' (the thing that died)
    # 2-3 - 'source actor' (the thing that did the killing)
    # 3 can be blank because 2 might be 'E0000000' (no actor)
    target_actor = Actor(*params[0:2])
    source_actor = Actor(*params[2:4])
    return Death(timestamp=timestamp, source_actor=source_actor, target_actor=target_actor)