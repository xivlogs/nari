from datetime import datetime
from typing import List

from nari.types.event import Event

def director_events_from_logline(timestamp: datetime, params: List[str]) -> Event:
    # Param layout from act:
    # 0 - first 2 bytes are from category, second 2 bytes is instance_id
    # 1 - director 'command'
    # 2-N - depends on the command
    #
    # Basically, we're going to return one of BarrierToggle, InstanceComplete, 
    # InstanceVote, InstanceFade, or InstanceInit from this event
    return Event(timestamp)
