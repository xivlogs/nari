"""Stuff for gauge of actors"""
from datetime import datetime

from nari.types.event import Event
from nari.types.actor import Actor


class Gauge(Event): # pylint: disable=too-few-public-methods
    """Event represents the gauge of an actor"""
    def __init__(self, *,
                 timestamp: datetime,
                 source_actor: Actor,
                ):
        super().__init__(timestamp)
        self.source_actor = source_actor

    def __repr__(self):
        return '<StatusApply>'
