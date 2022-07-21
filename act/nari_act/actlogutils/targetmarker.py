"""Parse player-applied overhead marker data from ACT log line"""
from nari.types import Timestamp
from nari.types.actor import Actor
from nari.types.event import Event
from nari.types.event.markers import MarkerOperation, OverheadMarker, PlayerMarker
from nari_act.actlogutils.exceptions import InvalidMarkerID, InvalidMarkerOperation


def targetmarker_from_logline(timestamp: Timestamp, params: list[str]) -> Event:
    """Parses a target marker event from an ACT log line

    ACT Event ID (decimal): 29

    ## Param layout from ACT

    The first two params in every event is the ACT event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |str|Operation|
    |1    |int|Marker ID|
    |2    |int|Source Actor ID|
    |3    |str|Source Actor Name|
    |4    |int|Target Actor ID|
    |5    |str|Target Actor Name|
    """
    source_actor = Actor(*params[2:4])
    target_actor = Actor(*params[4:6])

    # pylint: disable=invalid-name,duplicate-code
    op = MarkerOperation.Unknown
    match params[0].title():
        case 'Add':
            op = MarkerOperation.Add
        case 'Update':
            op = MarkerOperation.Update
        case 'Del' | 'Delete':
            op = MarkerOperation.Delete
        case _ as value:
            raise InvalidMarkerOperation(value)

    marker_id = int(params[1])
    if not PlayerMarker.contains(marker_id):
        raise InvalidMarkerID(marker_id)

    return OverheadMarker(
        timestamp=timestamp,
        source_actor=source_actor,
        target_actor=target_actor,
        operator=op,
        marker=PlayerMarker(marker_id)
    )
