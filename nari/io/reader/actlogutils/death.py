"""Parses death information from act log line"""
from typing import List

from nari.types import Timestamp
from nari.types.actor import Actor
from nari.types.event import Event
from nari.types.event.death import Death

def death_from_logline(timestamp: Timestamp, params: List[str]) -> Event:
    """Parses a death event from an act log line

    ACT Event ID (decimal): 25

    ## Param layout from act

    The first two params in every event is the act event ID and the timestamp it was parsed; the following table documents all the other fields.

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
