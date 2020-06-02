from abc import ABCMeta, abstractmethod
from typing import List

from nari.types.event.base import Event

class Reader(metaclass=ABCMeta):
    @abstractmethod
    def read(self) -> List[Event]:
        """Implementing classes must implement this method to return a list of events"""
        pass

from .actlog import ActLogReader