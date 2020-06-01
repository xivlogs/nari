from nari.types.event.base import Event
from nari.types.event import Type

class ZoneChange(Event):
    """ZoneChange"""
    __id__ = Type.zonechange.value
    def __repr__(self):
        return f'<ZoneChange ({self.params[1]})>'