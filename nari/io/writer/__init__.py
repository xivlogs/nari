"""Collection of writing-related classes and utilities"""

from abc import ABCMeta, abstractmethod
from typing import List, Iterator, Optional

from nari.types.event.base import Event


class Writer(metaclass=ABCMeta):
    """Represents an abstract base for writer objects"""
    def __init__(self, stream: Iterator[Event]):
        self.stream = iter(stream)

    def write(self):
        """Prompts the writer to begin consuming events"""
        while True:
            # try to grab a single event
            try:
                new_event = next(self.stream)
                self.write_next(new_event)
            except StopIteration:
                break

    @abstractmethod
    def write_next(self, event: Event) -> None:
        """Implementing classes must implement this method to write the next event"""
