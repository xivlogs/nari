"""Parse tether data from ACT log line"""
from nari.types import Timestamp
from nari.types.actor import Actor
from nari.types.event import Event
from nari.types.event.tether import Tether


def tether_from_logline(timestamp: Timestamp, params: list[str]) -> Event:
    """Parses a tether event from an ACT log line

    ACT Event ID (decimal): 35

    ## Param layout from ACT

    The first two params in every event is the ACT event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Source Actor ID|
    |1    |str|Source Actor Name|
    |2    |int|Target Actor ID|
    |3    |str|Target Actor Name|
    |4    |int|padding|
    |5    |int|padding|
    |6    |int|Tether ID|
    |7    |int|padding|
    |8    |int|padding|
    |9    |int|padding|
    """
    source_actor = Actor(*params[0:2])
    target_actor = Actor(*params[2:4])

    return Tether(
        timestamp=timestamp,
        source_actor=source_actor,
        target_actor=target_actor,
        tether_id=int(params[6])
    )
