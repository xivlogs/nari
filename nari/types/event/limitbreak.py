from nari.types.event.base import Event
from nari.types.event import Type

class LimitBreak(Event):
    """Event when limit break is gained"""
    __id__ = Type.limitbreak.value
    # looks like it has two params:
    # 0000|1
    # I think the first one is the state of the bar.
    # Not sure what the second one is.

    def __repr__(self):
        return f'<LimitBreak>'