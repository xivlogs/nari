"""This data is only relevant to the person parsing – Gauge events will only show up that player"""

from nari.types.event.base import Event
from nari.types.event import Type

class Gauge(Event):
    """ID 31 is a gauge event"""
    __id__ = Type.gauge.value
    def __repr__(self):
        return '<Gauge>'
