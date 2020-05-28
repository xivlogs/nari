from nari.parser.event.base import Event
from nari.types.event import Type
from nari.util.byte import hexstr_to_byte, reverse_bytes

class Gauge(Event):
    """ID 31 is a gauge event"""
    __id__ = Type.gauge.value
    def __repr__(self):
        return f'<Gauge>'