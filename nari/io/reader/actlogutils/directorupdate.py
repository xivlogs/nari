"""Parses director events from act log lines"""
from typing import Optional

from nari.types import Timestamp
from nari.types.event import Event
from nari.types.event.instance import BarrierState, BarrierToggle
from nari.types.event.instance import InstanceComplete, InstanceFade, InstanceInit, Fade
from nari.types.director import DirectorUpdateCommand

def director_events_from_logline(timestamp: Timestamp, params: list[str]) -> Optional[Event]:
    """Parses a director event from an act log line

    ACT Event ID (decimal): 33

    ## Param layout from act

    The first two params in every event is the act event ID and the timestamp it was parsed; the following table documents all the other fields.

    This event will be one of `BarrierToggle`, `InstanceComplete`, `InstanceVote`, `InstanceFade`, or `InstanceInit`.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|The first two bytes are from the category, and the second two bytes make up the instance ID.|
    |1    |int|The director command ID.|
    |2-N  ||Depends on the command.|
    """
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
