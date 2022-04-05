"""Parses cast data from ACT log line"""
from nari.types import Timestamp
from nari.types.actor import Actor
from nari.types.ability import Ability as AbilityType
from nari.types.event import Event
from nari.types.event.startcast import StartCast
from nari.types.event.stopcast import StopCast, StopCastType

def startcast_from_logline(timestamp: Timestamp, params: list[str]) -> Event:
    """Parses a start cast event from an act log line

    ACT Event ID (decimal): 20

    ## Param layout from act

    The first two params in every event is the act event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Source actor ID|
    |1    |string|Source actor name|
    |2    |int|Ability ID|
    |3    |string|Ability name|
    |4    |int|Target actor ID|
    |5    |string|Target actor name|
    |6    |float|Duration (ms)|
    |7    |float|Source actor X position|
    |8    |float|Source actor Y position|
    |9    |float|Source actor Z position|
    |10   |float|Source actor bearing|
    """
    source_actor = Actor(*params[0:2])
    ability = AbilityType(*params[2:4])
    target_actor = Actor(*params[4:6])
    try:
        source_actor.position.update(
            *[int(x) for x in params[7:11]]
        )
    except ValueError:
        pass
    duration = float(params[6])
    return StartCast(
        timestamp=timestamp,
        source_actor=source_actor,
        ability=ability,
        target_actor=target_actor,
        duration=duration,
    )


def stopcast_from_logline(timestamp: Timestamp, params: list[str]) -> Event:
    """Parses stop cast event from act log line

    ACT Event ID (decimal): 20

    ## Param layout from act

    The first two params in every event is the act event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Source actor ID|
    |1    |string|Source actor name|
    |2    |int|Ability ID|
    |3    |string|Ability name|
    |4    |int|Type of interrupt|
    |5    |null|Blank field|
    """
    source_actor = Actor(*params[0:2])
    ability = AbilityType(*params[2:4])
    stop_type = StopCastType.value_from_name(params[4])
    return StopCast(
        timestamp=timestamp,
        source_actor=source_actor,
        ability=ability,
        cast_type=stop_type,
    )
