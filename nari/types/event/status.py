"""Stuff for application of statuses"""
from datetime import datetime

from nari.types.event import Event
from nari.types.actor import Actor
from nari.types.status import Status


class StatusApply(Event): # pylint: disable=too-few-public-methods
    """Event represents the application of a status"""
    def __init__(self, *,
                 timestamp: datetime,
                 status: Status,
                 duration: float,
                 source_actor: Actor,
                 target_actor: Actor,
                 params: int
                ):
        super().__init__(timestamp)
        self.status = status
        self.duration = duration
        self.source_actor = source_actor
        self.target_actor = target_actor
        self.params = params

    def __repr__(self):
        return '<StatusApply>'


class StatusRemove(Event): # pylint: disable=too-few-public-methods
    """Event represents the application of a status"""
    def __init__(self, *,
                 timestamp: datetime,
                 status: Status,
                 duration: float,
                 source_actor: Actor,
                 target_actor: Actor,
                 params: int
                ):
        super().__init__(timestamp)
        self.status = status
        self.duration = duration
        self.source_actor = source_actor
        self.target_actor = target_actor
        self.params = params

    def __repr__(self):
        return '<StatusRemove>'
