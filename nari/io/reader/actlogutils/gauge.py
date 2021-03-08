from datetime import datetime
from typing import List

from nari.types.event.gauge import Gauge


def gauge_from_logline(timestamp: datetime, params: List[str]) -> Gauge:
    """Parses gauge event out from act log line"""
    # Param layout from ACT
    # 0 - 'actor id' which is the player who is logging.
    # 1-4 - Gauge data is from a C-style union type stored with fields depending on job. ACT represents this as four
    #       32-bit unsigned ints so they're left as bytes for destructuring later.

    actor_id = int(params[0], 16)
    gauge_data = tuple((string_to_bytes(param) for param in params[1:]))

    # TODO: add exceptions for IndexError

    return Gauge(timestamp=timestamp, actor_id=actor_id, fields=gauge_data)


def string_to_bytes(param: str) -> bytes:
    """Helper function to convert strings into bytes. Also changes the byte order."""

    param_expanded = param.zfill(8)
    bytes_arr = bytearray.fromhex(param_expanded)
    bytes_arr.reverse()  # switch the endianness

    return bytes(bytes_arr)
