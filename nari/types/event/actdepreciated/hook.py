"""When ACT successfully 'hooked' into FFXIV, it generates this event."""

from nari.types.event.base import Event
from nari.types.event import Type

class Hook(Event):
    """ID 250 is the notification that the plugin has 'hooked' into the XIV process ID"""
    __id__ = Type.hook.value
    def __repr__(self):
        return '<Hook>'
