"""Actor-related types and utilities"""
from dataclasses import dataclass

from nari.util.pair import IdNamePair


@dataclass
class Resources():
    """Holds resource values for an Actor"""
    hp: int = 0
    hp_max: int = 0
    mp: int = 0
    mp_max: int = 10000
    sp: int = 0
    sp_max: int = 0

    # I'm providing convenience here, leave me alone
    # pylint: disable=too-many-arguments
    def update(self, hp: int = None, hp_max: int = None, mp: int = None, mp_max: int = None, sp: int = None, sp_max: int = None):
        """Lets you batch update the resource values"""
        self.hp = hp or self.hp
        self.hp_max = hp_max or self.hp_max
        self.mp = mp or self.mp
        self.mp_max = mp_max or self.mp_max
        self.sp = sp or self.sp_max
        self.sp_max = sp_max or self.sp_max

@dataclass
class Position():
    """Holds position data for an Actor"""
    x: float = 0
    y: float = 0
    z: float = 0
    bearing: float = 0

    def update(self, x: float = None, y: float = None, z: float = None, bearing: float = None):
        """Lets you batch update the position via position or arguments"""
        self.x = x or self.x
        self.y = y or self.y
        self.z = z or self.z
        self.bearing = bearing or self.bearing


class Actor(IdNamePair):
    """Represents an Actor"""
    # pylint: disable=too-few-public-methods
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resources = Resources()
        self.position = Position()

    def __repr__(self) -> str:
        return f'<Actor ({self.name}|{self.id})>'
