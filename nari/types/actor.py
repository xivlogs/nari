"""Actor-related types and utilities"""

from nari.util.pair import IdNamePair

# pylint: disable=too-few-public-methods
class Actor(IdNamePair):
    """Represents an Actor"""
    def __repr__(self) -> str:
        return f'<Actor ({self.name}|{self.id})>'
