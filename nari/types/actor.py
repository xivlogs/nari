"""Actor-related types and utilities"""

from nari.util.pair import IdNamePair

class Actor(IdNamePair):
    """Represents an Actor"""
    def __repr__(self) -> str:
        return f'<Actor ({self.name}|{self.id})>'
