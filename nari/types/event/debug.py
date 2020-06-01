from nari.types.event.base import Event
from nari.types.event import Type


class Debug(Event):
    """ID 251 is for debug data. Probably best to preserve as-is"""
    __id__ = Type.debug.value
    def handle_params(self):
        self.message = self.params[0]

    def __repr__(self):
        return f'<Debug ({self.message})>'