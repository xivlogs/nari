"""Defines a helper class to bundle string hex IDs with an associated name"""

from ..types import HexStr
from typing import Union

# pylint: disable=too-few-public-methods,redefined-builtin
class IdNamePair():
    """Represents a tuple where there's a hex or an int id and a string name; automatically converts the hex string to an int"""
    def __init__(self, id: Union[HexStr, int], name: str):
        if(isinstance(id, int)):
            self.id = id
        else:
            self.id = int(id, 16)
        self.name = name

    def __repr__(self):
        return f'<Pair {self.id}:{self.name}>'
