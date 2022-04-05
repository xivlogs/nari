"""Parse content-specific overhead marker data from ACT log line"""
from nari.types import Timestamp
from nari.types.actor import Actor
from nari.types.event import Event
from nari.types.event.markers import ContentMarker


def targeticon_from_logline(timestamp: Timestamp, params: list[str]) -> Event:
    """Parses a target icon event from an ACT log line

    ACT Event ID (decimal): 27

    ## Param layout from ACT

    The first two params in every event is the ACT event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Target actor ID|
    |1    |string|Target actor name|
    |2    |int|padding|
    |3    |int|padding|
    |4    |int|Lockon ID|
    |5    |int|padding|
    |6    |int|padding|
    |7    |int|padding|
    """
    actor = Actor(*params[0:2])
    return ContentMarker(
        timestamp=timestamp,
        actor=actor,
        marker_id=int(params[4])
    )
