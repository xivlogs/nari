"""Parses death data from ACT log line"""
from nari.types import Timestamp
from nari.types.actor import Actor
from nari.types.event import Event
from nari.types.event.death import Death


def death_from_logline(timestamp: Timestamp, params: list[str]) -> Event:
    """Parses a death animation event from an ACT log line

    ACT Event ID (decimal): 25

    ## Param layout from ACT

    The first two params in every event is the ACT event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Target actor ID - The thing that died.|
    |1    |string|Target actor name|
    |2    |int|Source actor ID - The thing that did the killing.|
    |3    |string|Source actor name - This field will be blank if field 2 is 'E0000000' (no actor).|
    """
    target_actor = Actor(*params[0:2])
    source_actor = Actor(*params[2:4])
    return Death(timestamp=timestamp, source_actor=source_actor, target_actor=target_actor)
