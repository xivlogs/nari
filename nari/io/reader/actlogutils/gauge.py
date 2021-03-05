from datetime import datetime
from typing import List

from nari.types.event.gauge import Gauge


def gauge_from_logline(timestamp: datetime, params: List[str]) -> Gauge:
    """Parses gauge event out from act log line"""
    # Param layout from ACT
    # 0 - 'actor id' which is the player who is logging.
    # 1-4 - Most gauge data is stored in 1-3. Gauge data and data type is dependent on job so they are left as bytes for
    #       destructuring later. I have no idea what's in 4 and could not find documentation for it.

    actor_id = int(params[0], 16)
    gauge_data = tuple((string_to_bytes(param) for param in params[1:5]))

    # TODO: add exceptions for IndexError

    return Gauge(timestamp=timestamp, actor_id=actor_id, fields=gauge_data)


def string_to_bytes(param: str) -> bytes:
    """Helper function to convert strings into bytes. Also changes the byte order."""

    param_expanded = param.zfill(8)
    bytes_data = int(param_expanded, 16).to_bytes(4, "little")

    # TODO: add exceptions for ValueError and Overflow Error
    return bytes_data
