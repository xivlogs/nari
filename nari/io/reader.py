"""Collection of reading-related classes and utilities"""

from abc import ABCMeta, abstractmethod
from typing import List

from nari.types.event.base import Event

# pylint: disable=too-few-public-methods
class Reader(metaclass=ABCMeta):
    """Represents an abstract base for reader objects"""
    @abstractmethod
    def read(self) -> List[Event]:
        """Implementing classes must implement this method to return a list of events"""

# pylint: disable=unused-import,wrong-import-position
from .actlog import ActLogReader
