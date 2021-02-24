"""Fires when the zone is changed"""

from nari.types.event.base import Event
from nari.types.event import Type

class ZoneChange(Event):
    """ZoneChange"""
    __id__ = Type.zonechange.value
    def handle_params(self):
        self.zone_id = int(self.params[0], 16)
        self.zone_name = self.params[1]
    def __repr__(self):
        return f'<ZoneChange ({self.zone_name})>'
