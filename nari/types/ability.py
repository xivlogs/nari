"""Ability-related types"""

from nari.util.pair import IdNamePair

class Ability(IdNamePair):
    """Represents an Ability in-game"""
    def __repr__(self) -> str:
        return f'<Ability ({self.name})>'
