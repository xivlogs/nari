"""Provides the Normaliser abstract base class"""

from abc import ABCMeta, abstractmethod
from typing import Union, List, Iterator, Optional

from nari.types.event.base import Event


class Normaliser(metaclass=ABCMeta):
    """Normalisers take in interable events and spit out iterable events"""
    def __init__(self, stream: Iterator[Event]):
        self.stream = iter(stream)
        self.buffer: List[Event] = []
        self.stream_finished = False

    def __iter__(self) -> Iterator[Event]:
        return self

    def __next__(self) -> Event:
        event: Union[Event, None] = self.handle_next()
        if event:
            return event
        raise StopIteration

    def grab_next_event(self) -> Union[List[Event], Event, None]:
        """Keeps iterating down the stream until it either has nothing left or it gets an event we're happy with"""
        while not self.stream_finished:
            # try to grab a single event
            try:
                new_event = next(self.stream)
                handled_event = self.on_event(new_event)
                if handled_event is None:
                    continue
                return handled_event
            except StopIteration:
                self.stream_finished = True
                return None
        return None

    def handle_next(self) -> Optional[Event]:
        """Handles the next event from the input stream, calling `on_event()` with each event"""
        if not self.stream_finished:
            handled_event = self.grab_next_event()
            if isinstance(handled_event, list):
                self.buffer.extend(handled_event)
            elif isinstance(handled_event, Event):
                self.buffer.append(handled_event)
            elif handled_event is None: # we might be done with the stream anyway
                pass
            else: # not a list or an Event?
                raise Exception('yell at nono to come up with a name for this screwup')

        # keep dumping that buffer
        if len(self.buffer) > 0:
            return self.buffer.pop(0)

        return None

    @abstractmethod
    def on_event(self, event: Event) -> Union[List[Event], Event]:
        """Takes an event and returns either a single event in turn, or a list of events

        A normaliser that does nothing would just implement the method to return the same
        event that it receives; conversely you could fabricate entirely new events to place
        in the resultant array.
        """
