from unittest import TestCase

from nari.types.event import Event


class TestBaseEvent(TestCase):
    def test_event_init(self):
        """The base event only carries a timestamp value and a default repr"""
        event = Event(timestamp=123)
        self.assertEqual(event.timestamp, 123)
        self.assertEqual(repr(event), '<Event>')
