"""Parse waymark data from ACT log line"""
from nari.types import Timestamp
from nari.types.actor import Actor
from nari.types.event import Event
from nari.types.event.markers import MarkerOperation
from nari.types.event.waymark import Waymark, Waypoint, Position
from nari.io.reader.actlogutils.exceptions import InvalidMarkerID, InvalidMarkerOperation


def waymark_from_logline(timestamp: Timestamp, params: list[str]) -> Event:
    """Parses a waymark event from an ACT log line

    ACT Event ID (decimal): 28

    ## Param layout from ACT

    The first two params in every event is the ACT event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |str|Operation|
    |1    |int|Marker ID|
    |2    |int|Actor ID|
    |3    |str|Actor Name|
    |4    |float|Target waypoint X position|
    |5    |float|Target waypoint Y position|
    |6    |float|Target waypoint Z position|
    """
    actor = Actor(*params[2:4])

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

    position = Position(*[float(x) for x in params[4:7]])

    marker_id = int(params[1]) + 1 # IPC data sends this zero-indexed, adjust since game uses it one-indexed
    if not Waypoint.contains(marker_id):
        raise InvalidMarkerID(marker_id)

    return Waymark(
        timestamp=timestamp,
        actor=actor,
        operator=op,
        marker=Waypoint(marker_id),
        position=position
    )
