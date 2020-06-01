from nari.types.event.base import Event
from nari.types.event import Type

class ChangePlayer(Event):
    """Changes the main player. Apparently only shows up after zone transitions."""
    __id__ = Type.changeplayer.value

    def __repr__(self):
        return f'<ChangePlayer ({self.params[1]})>'