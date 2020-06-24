"""Collection of writing-related classes and utilities"""

from abc import ABCMeta, abstractmethod
from typing import List, Iterator, Optional

from nari.types.event.base import Event


class Writer(metaclass=ABCMeta):
    """Represents an abstract base for writer objects"""
    def __init__(self, stream: Iterator[Event]):
        self.stream = iter(stream)

    def write_one(self) -> bool:
        """Attempts to write one event. If it fails, return False. Otherwise, return True"""
        try:
            new_event = next(self.stream)
            self.write_next(new_event)
        except StopIteration:
            return False

        return True

    def write_batch(self, amount: int):
        """Writes a batch of events"""
        for i in range(amount): # pylint: disable=unused-variable
            response = self.write_one()
            if not response:
                # best to raise an exception, but I dunno
                return

    def write(self):
        """Prompts the writer to consume all events"""
        while True:
            response = self.write_one()
            if not response:
                return

    @abstractmethod
    def write_next(self, event: Event) -> None:
        """Implementing classes must implement this method to write the next event"""
