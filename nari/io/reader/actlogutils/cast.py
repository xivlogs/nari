"""Parses cast information from act log line"""
from datetime import datetime
from typing import List

from nari.types.actor import Actor
from nari.types.ability import Ability as AbilityType
from nari.types.event import Event
from nari.types.event.startcast import StartCast
from nari.types.event.stopcast import StopCast, StopCastType

def startcast_from_logline(timestamp: datetime, params: List[str]) -> Event:
    """Parses a start cast event from an act log line

    ACT Event ID (decimal): 20

    ## Param layout from act

    The first two params in every event is the act event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Source actor ID|
    |1    |string|Source actor Name|
    |2    |int|Ability ID|
    |3    |string|Ability name|
    |4    |int|Target actor ID|
    |5    |string|Target actor Name|
    |6    |float|Duration?|
    |7    |int|Blank field?|
    
    """
    source_actor = Actor(*params[0:2])
    ability = AbilityType(*params[2:4])
    target_actor = Actor(*params[4:6])
    return StartCast(
        timestamp=timestamp,
        source_actor=source_actor,
        ability=ability,
        target_actor=target_actor,
        duration=int(params[6]),
    )

def stopcast_from_act_timestamp(timestamp: datetime, params: List[str]) -> Event:
    """Parses stop cast event from act log line"""
    # param layout from act
    # 0-1 Source Actor
    # 2-3 Ability
    # 4 Interrupted or Cancelled
    # 5 blank field ???
    source_actor = Actor(*params[0:2])
    ability = AbilityType(*params[2:4])
    stop_type = StopCastType.value_from_name(params[4])
    return StopCast(
        timestamp=timestamp,
        source_actor=source_actor,
        ability=ability,
        cast_type=stop_type,
    )
