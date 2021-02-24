"""parses zone change information from act log line"""

from datetime import datetime
from typing import List

from nari.types.event import Event
from nari.types.event.zone import ZoneChange

def zonechange_from_logline(timestamp: datetime, params: List[str]) -> Event:
    """Helper function to parse zone information from act log line"""
    # param layout from act
    # 0 - zone id
    # 1 - zone name
    zone_id = int(params[0], 16)
    return ZoneChange(timestamp=timestamp, zone_id=zone_id)
