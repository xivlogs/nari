"""Provides the Normalizer abstract base class"""

from abc import ABCMeta, abstractmethod
from typing import Union, List, Iterable, Iterator

from nari.types.event.base import Event


class Normalizer(metaclass=ABCMeta):
    """Normalizers take in interable events and spit out iterable events"""
    def __init__(self, stream: Iterator[Event]):
        self.stream = iter(stream)
        self.buffer: List[Event] = []
        self.stream_finished = False

    def __iter__(self) -> Iterable[Event]:
        return self

    def __next__(self) -> Event:
        event: Event = self.handle_next()
        if event:
            return event
        raise StopIteration

    def handle_next(self) -> Union[Event, None]:
        """Handles the next event from the input stream, calling `on_event()` with each event"""
        if not self.stream_finished:
            # try to keep grabbing at least one event and process it into the buffer
            try:
                new_event = next(self.stream)
                handled_event = self.on_event(new_event)

                if isinstance(handled_event, list):
                    self.buffer.extend(handled_event)
                elif isinstance(handled_event, Event):
                    self.buffer.append(handled_event)
                else: # not a list or an Event?
                    raise Exception('yell at nono to come up with a name for this screwup')
            except StopIteration:
                self.stream_finished = True

        # keep dumping that buffer
        if len(self.buffer) > 0:
            return self.buffer.pop(0)

        return None

    @abstractmethod
    def on_event(self, event: Event) -> Union[List[Event], Event]:
        """Takes an event and returns either a single event in turn, or a list of events

        A normalizer that does nothing would just implement the method to return the same
        event that it recieves; conversely you could fabricate entirely new events to place
        in the resultant array.
        """


class PassthroughNormalizer(Normalizer):
    """Dumb way of passing through events to act like you're cool or something"""
    def on_event(self, event):
        return event

class DoubleNormalizer(Normalizer):
    """Even dumber thing to return a duplicate of every event like you're dumb or something"""
    def on_event(self, event):
        return [event, event]
