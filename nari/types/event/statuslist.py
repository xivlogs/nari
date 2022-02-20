"""Stuff for the application of statuses"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.classjoblevel import ClassJobLevel
from nari.types.actor import Actor
from nari.types.status import StatusEffect


class StatusList(Event): # pylint: disable=too-few-public-methods
    """Whenever a status is applied"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 class_job_level: ClassJobLevel,
                 target_actor: Actor,
                 status_effects: list[StatusEffect]
                ):
        super().__init__(timestamp)
        self.class_job_level = class_job_level
        self.target_actor = target_actor
        self.status_effects = status_effects

    def __repr__(self):
        return '<StatusList>'
