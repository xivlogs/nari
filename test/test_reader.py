from typing import Optional
from unittest import TestCase
from unittest.mock import patch

from nari.io.reader import Reader
from nari.types.event import Event


class TestReader(Reader):
    def __init__(self):
        self.default_events = [
            Event(timestamp=1),
            Event(timestamp=2),
            Event(timestamp=3),
        ]

    def read_next(self) -> Optional[Event]:
        try:
            event = self.default_events.pop(0)
            return event
        except IndexError:
            return None

class TestBaseReader(TestCase):
    def test_read_next(self):
        test_reader = TestReader()
        events = iter(test_reader)
        self.assertEqual(next(events).timestamp, 1)
        self.assertEqual(next(events).timestamp, 2)
        self.assertEqual(next(events).timestamp, 3)
        with self.assertRaises(StopIteration):
            _event = next(events)

    def test_read_all(self):
        test_reader = TestReader()
        event_list = test_reader.read_all()
        self.assertEqual(len(event_list), 3)
        self.assertEqual(event_list[0].timestamp, 1)
        self.assertEqual(event_list[1].timestamp, 2)
        self.assertEqual(event_list[2].timestamp, 3)
