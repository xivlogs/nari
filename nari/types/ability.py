"""Ability-related types"""

from nari.util.pair import IdNamePair

# pylint: disable=too-few-public-methods
class Ability(IdNamePair):
    """Represents an Ability in-game"""
    def __repr__(self) -> str:
        return f'<Ability ({self.name})>'
