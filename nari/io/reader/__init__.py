"""Collection of reading-related classes and utilities"""

from abc import ABCMeta, abstractmethod
from typing import Iterator, Optional

from nari.types.event import Event


class Reader(metaclass=ABCMeta):
    """Represents an abstract base for reader objects"""
    def __iter__(self) -> Iterator[Event]:
        return self

    def __next__(self) -> Event:
        event: Optional[Event] = self.read_next()
        if event:
            return event
        raise StopIteration

    @abstractmethod
    def read_next(self) -> Optional[Event]:
        """Implementing classes must implement this method to return the next parsed event.

        :return: A nari Event or ``None``; the latter of which will cause the reader to stop iterating.
        """

    def read_all(self) -> list[Event]:
        """Iterates through all events and returns them as a list"""
        return list(self)
