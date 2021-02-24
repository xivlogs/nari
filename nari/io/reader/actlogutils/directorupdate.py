"""Parses director events from act log lines"""

from datetime import datetime
from typing import List, Optional

from nari.types.event import Event
from nari.types.event.barriertoggle import BarrierState, BarrierToggle
from nari.types.event.instance import InstanceComplete, InstanceFade, InstanceInit, Fade
from nari.types.director import DirectorUpdateCommand

def director_events_from_logline(timestamp: datetime, params: List[str]) -> Event:
    """Helper function to parse director events from act log lines"""
    # Param layout from act:
    # 0 - first 2 bytes are from category, second 2 bytes is instance_id
    # 1 - director 'command'
    # 2-N - depends on the command
    #
    # Basically, we're going to return one of BarrierToggle, InstanceComplete,
    # InstanceVote, InstanceFade, or InstanceInit from this event
    # category = int(params[0][:4], 16)
    instance_id = int(params[0][:4], 16)
    command = int(params[1], 16)

    event: Optional[Event] = None
    if command == DirectorUpdateCommand.barrierup:
        event = BarrierToggle(timestamp=timestamp, instance_id=instance_id, state=BarrierState.up)
    elif command == DirectorUpdateCommand.barrierdown:
        event = BarrierToggle(timestamp=timestamp, instance_id=instance_id, state=BarrierState.down)
    elif command == DirectorUpdateCommand.complete:
        event = InstanceComplete(timestamp=timestamp, instance_id=instance_id)
    elif command == DirectorUpdateCommand.fadein:
        event = InstanceFade(timestamp=timestamp, instance_id=instance_id, state=Fade.In)
    elif command == DirectorUpdateCommand.fadeout:
        event = InstanceFade(timestamp=timestamp, instance_id=instance_id, state=Fade.Out)
    elif command == DirectorUpdateCommand.init:
        event = InstanceInit(timestamp=timestamp, instance_id=instance_id)

    return event
