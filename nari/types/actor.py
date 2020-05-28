from nari.types import HexStr
from nari.util.pair import IdNamePair

class Actor(IdNamePair):
    def __repr__(self) -> str:
        return f'<Actor ({self.name}|{self.id})>'