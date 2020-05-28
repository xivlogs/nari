from nari.parser.event.base import Event
from nari.types.event import Type

class PlayerStats(Event):
    """Id 12"""
    __id__ = Type.playerstats.value
    def __repr__(self):
        return f'<PlayerStats>'