from ..types import HexStr

class IdNamePair(object):
    def __init__(self, id: HexStr, name: str):
        self.id = int(id, 16)
        self.name = name