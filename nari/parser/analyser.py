"""Analysers parse streams of data like Normalisers and Writers, but don't push out an event stream"""

from typing import Iterable, Iterator, Callable, Tuple, Dict, Any
from nari.types.event.base import Event

# some useful typedefs
FilterFunc = Callable[[Event], bool]
CallbackFunc = Callable[[Event], None]
FilterCallbackBundle = Tuple[FilterFunc, CallbackFunc]
Hooks = Dict[int, FilterCallbackBundle]

class Analyser():
    """Analyser base class"""
    def __init__(self, stream: Iterable[Event]):
        self.stream: Iterator[Event] = iter(stream)
        self.hooks: Hooks = {}
        self.init()

    def init(self):
        """Subclasses override this method to set up for their particular use case"""

    def add_event_hook(self, filter_fn: FilterFunc, callback: CallbackFunc) -> int:
        """Adds an event hook that watches for certain types of events and calls a callback function on them"""
        filter_id = id(filter_fn)
        self.hooks[filter_id] = (filter_fn, callback)
        return filter_id

    def remove_event_hook(self, filter_id: int):
        """Removes an event hook"""
        del self.hooks[filter_id]

    def process_events(self):
        """The 'main' loop. Grabs every event, and calls all relevant callback functions on them"""
        for event in self.stream:
            for filter_fn, callback in self.hooks.values():
                if filter_fn(event):
                    callback(event)

        return self.results()

    def results(self) -> Any:
        """Override to provide results from your analyzer. It's up to you to return what you want"""
