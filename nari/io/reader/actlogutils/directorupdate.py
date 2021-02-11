"""Parses director events from act log lines"""

from datetime import datetime
from typing import List

from nari.types.event import Event
from nari.types.event.barriertoggle import BarrierState, BarrierToggle
from nari.types.event.instance import InstanceComplete, InstanceFade, InstanceInit, Fade
from nari.types.event.act.directorupdate import DirectorUpdateCommand

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
    # pylint: disable=too-many-return-statements
    instance_id = int(params[0][:4], 16)
    command = int(params[1], 16)

    if command == DirectorUpdateCommand.barrierup:
        return BarrierToggle(timestamp=timestamp, instance_id=instance_id, state=BarrierState.up)
    if command == DirectorUpdateCommand.barrierdown:
        return BarrierToggle(timestamp=timestamp, instance_id=instance_id, state=BarrierState.down)
    if command == DirectorUpdateCommand.complete:
        return InstanceComplete(timestamp=timestamp, instance_id=instance_id)
    if command == DirectorUpdateCommand.fadein:
        return InstanceFade(timestamp=timestamp, instance_id=instance_id, state=Fade.In)
    if command == DirectorUpdateCommand.fadeout:
        return InstanceFade(timestamp=timestamp, instance_id=instance_id, state=Fade.Out)
    if command == DirectorUpdateCommand.init:
        return InstanceInit(timestamp=timestamp, instance_id=instance_id)

    return None
