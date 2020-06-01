from nari.types.event.base import Event
from nari.types.event import Type

class NetworkTargetMarker(Event):
    """The place I got my docs from didn't give good data for this one"""
    __id__ = Type.networktargetmarker.value
    def __repr__(self):
        return f'<TargetMarker>'