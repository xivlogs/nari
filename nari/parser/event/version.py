from .base import Event
from nari.types.event import Type

class Version(Event):
    __id__ = Type.version.value
    def __repr__(self):
        return f'<Version {self.params[0]}>'