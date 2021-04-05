""""Parses gauge events from act log line"""
from datetime import datetime
from typing import List

from nari.types.event.gauge import Gauge
from nari.util.byte import hexstr_to_bytes
from nari.util.exceptions import ActLineReadError

def gauge_from_logline(timestamp: datetime, params: List[str]) -> Gauge:
    """Parses gauge event out from act log line"""
    # Param layout from ACT
    # 0 - 'actor id' which is the player who is logging.
    # 1-4 - Gauge data is from a C-style union type stored with fields depending on job. ACT represents this as four
    #       32-bit unsigned ints so they're left as bytes for destructuring later.

    try:
        actor_id = int(params[0], 16)
        gauge_data = tuple((hexstr_to_bytes(param) for param in params[1:]))
        return Gauge(timestamp=timestamp, actor_id=actor_id, fields=gauge_data)

    except IndexError as e:
        raise ActLineReadError('Error when splitting Gauge ACT Line') from e
