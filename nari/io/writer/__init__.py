"""Collection of writing-related classes and utilities"""

from abc import ABCMeta, abstractmethod
from typing import Iterator

from nari.types.event import Event


class Writer(metaclass=ABCMeta):
    """Represents an abstract base for writer objects"""
    def __init__(self, stream: Iterator[Event]):
        self.stream = iter(stream)

    def write(self, amount: int = 0):
        """Prompts the writer to consume an amount of events or all events"""
        index: int = 1
        while index != amount:
            try:
                next_event = next(self.stream)
                self.write_next(next_event)
                index += 1
            except StopIteration:
                self.cleanup()
                return

    @abstractmethod
    def write_next(self, event: Event) -> None:
        """Implementing classes must implement this method to write the next event"""

    def cleanup(self):
        """Override to provide any cleanup items you need to do after the last item was written"""
