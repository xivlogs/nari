"""Literally lines from the in-game log"""

from nari.types.event.base import Event
from nari.types.event import Type

class LogLine(Event):
    """Logline"""
    __id__ = Type.logline.value

    def __repr__(self):
        return f'<LogLine ({self.params[2]})>'
