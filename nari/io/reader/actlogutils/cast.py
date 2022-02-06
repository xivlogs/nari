"""Parses cast information from act log line"""
from datetime import datetime
from typing import List

from nari.types.actor import Actor
from nari.types.ability import Ability as AbilityType
from nari.types.event import Event
from nari.types.event.startcast import StartCast
from nari.types.event.stopcast import StopCast, StopCastType

def startcast_from_logline(timestamp: datetime, params: List[str]) -> Event:
    """Parses start cast event from act log line"""
    # param layout from act
    # 0-1 Source Actor
    # 2-3 Ability
    # 4-5 Target Actor
    # 6 duration ???
    # 7 blank field ???
    source_actor = Actor(*params[0:2])
    ability = AbilityType(*params[2:4])
    target_actor = Actor(*params[4:6])
    duration = float(params[6])
    return StartCast(
        timestamp=timestamp,
        source_actor=source_actor,
        ability=ability,
        target_actor=target_actor,
        duration=duration,
    )

def stopcast_from_logline(timestamp: datetime, params: List[str]) -> Event:
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
