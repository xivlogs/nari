from datetime import datetime
from typing import List
from nari.types.event.gauge import Gauge


def gauge_from_logline(timestamp: datetime, params: List[str]) -> Gauge:
    """Parses gauge event out from act log line"""
    actor_id = int(params[0], 16)

    # Unpacks the params into a tuple of four bytes type to be used later, since each job has data stored differently
    gauge_data = tuple((string_to_bytes(param) for param in params[1:5]))

    # TODO: add exceptions for IndexError

    return Gauge(timestamp=timestamp, actor_id=actor_id, fields=gauge_data)


def string_to_bytes(param: str) -> bytes:
    """Helper function to convert strings into bytes. Also changes the byte order."""

    param_expanded = param.zfill(8)
    bytes_data = int(param_expanded, 16).to_bytes(4, "little")

    # TODO: add exceptions for ValueError and Overflow Error
    return bytes_data
