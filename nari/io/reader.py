"""Collection of reading-related classes and utilities"""

from abc import ABCMeta, abstractmethod
from typing import List, Iterable, Union

from nari.types.event.base import Event


class Reader(metaclass=ABCMeta):
    """Represents an abstract base for reader objects"""
    def __iter__(self) -> Iterable[Event]:
        return self

    def __next__(self) -> Event:
        event: Event = self.read_next()
        if event:
            return event
        raise StopIteration

    @abstractmethod
    def read_next(self) -> Union[Event, None]:
        """Implementing classes must implement this method to return the next parsed event"""

    def read_all(self) -> List[Event]:
        """Iterates through all events and returns them as a list"""
        return list(self)
