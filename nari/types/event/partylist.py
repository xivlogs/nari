from nari.types.event.base import Event
from nari.types.event import Type

class PartyList(Event):
    """List of members in the party"""
    __id__ = Type.partylist.value
    def __repr__(self):
        return f'<Partylist ({self.params[0]})>'