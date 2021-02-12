"""Analysers parse streams of data like Normalisers and Writers, but don't push out an event stream"""

from enum import IntEnum, auto
from typing import Iterable, Iterator, Callable, Tuple, Dict, Any, List, Optional
from nari.types.event import Event

# some useful typedefs
FilterFunc = Callable[[Event], bool]
CallbackFunc = Callable[[Event], Optional[bool]]
TopicCallbackFunc = Callable[[], None]
FilterCallbackBundle = Tuple[FilterFunc, CallbackFunc]
Hooks = Dict[int, FilterCallbackBundle]
Topics = Dict[int, List[TopicCallbackFunc]]

# The default for a hook is to just subscribe to everything. Be careful and define a predicate if you can
allow_all_events = lambda x: True
# Hook functions can return False to stop the analyzer entirely
STOP_PROCESSING = False

class AnalyserTopic(IntEnum):
    """List of topics"""
    stream_end = auto()


class Analyser():
    """Analyser base class"""
    def __init__(self, stream: Iterable[Event]):
        self.stream: Iterator[Event] = iter(stream)
        self.hooks: Hooks = {}
        self.hooks_to_remove: List[int] = []
        self.topics: Topics = {}
        self.init()

    def init(self):
        """Subclasses override this method to set up for their particular use case"""

    def add_event_hook(self, *, predicate: FilterFunc = allow_all_events, callback: CallbackFunc) -> int:
        """Adds an event hook that watches for certain types of events and calls a callback function on them"""
        filter_id = id(predicate)
        self.hooks[filter_id] = (predicate, callback)
        return filter_id

    def add_topic_hook(self, topic: AnalyserTopic, callback: TopicCallbackFunc):
        """Adds a set of 'topic hooks' that run at specified times"""
        topics = self.topics.get(topic, [])
        topics.append(callback)
        self.topics[topic] = topics

    def remove_event_hook(self, filter_id: int):
        """Removes an event hook"""
        self.hooks_to_remove.append(filter_id)

    def process_events(self):
        """The 'main' loop. Grabs every event, and calls all relevant callback functions on them"""
        # process the main stream
        for event in self.stream:
            for filter_fn, callback in self.hooks.values():
                if filter_fn(event):
                    if not callback(event):
                        break
            else:
                while len(self.hooks_to_remove) > 0:
                    del self.hooks[self.hooks_to_remove.pop()]
                continue
            break

        # call the 'stream_end' topic
        for callback in self.topics.get(AnalyserTopic.stream_end, []):
            callback()

        return self.results()

    def results(self) -> Any:
        """Override to provide results from your analyser. It's up to you to return what you want"""
