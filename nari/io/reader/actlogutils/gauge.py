""""Parses gauge events from act log line"""
from typing import List

from nari.types import Timestamp
from nari.types.event.gauge import Gauge
from nari.util.byte import hexstr_to_bytes
from nari.util.exceptions import ActLineReadError

def gauge_from_logline(timestamp: Timestamp, params: List[str]) -> Gauge:
    """Parses a gauge event from an act log line

    ACT Event ID (decimal): 31

    ## Param layout from act

    The first two params in every event is the act event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Actor ID - The player who is logging.|
    |1-4  |uint32|Gauge data is from a C-style union type stored with fields depending on job. ACT represents this as four 32-bit unsigned ints so they're left as bytes for destructuring later.|
    """

    try:
        actor_id = int(params[0], 16)
        gauge_data = tuple((hexstr_to_bytes(param) for param in params[1:5]))
        return Gauge(timestamp=timestamp, actor_id=actor_id, fields=gauge_data)

    except IndexError as index_error:
        raise ActLineReadError('Error when splitting Gauge ACT Line') from index_error
