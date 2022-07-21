"""Parse zone change data from ACT log line"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.event.zone import ZoneChange


def zonechange_from_logline(timestamp: Timestamp, params: list[str]) -> Event:
    """Parses a ZoneChange event from an ACT log line

    ACT Event ID (decimal): 1

    ## Param layout from ACT

    The first two params in every event is the ACT event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Zone ID|
    |1    |string|Zone name|
    """
    # param layout from act
    # 0 - zone id
    # 1 - zone name
    zone_id = int(params[0], 16)
    return ZoneChange(timestamp=timestamp, zone_id=zone_id)
