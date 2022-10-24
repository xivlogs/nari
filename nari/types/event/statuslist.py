"""
Status Effect Lists
~~~~~~~~~~~~~~~~~~~
"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.classjoblevel import ClassJobLevel
from nari.types.actor import Actor
from nari.types.status import StatusEffect


class StatusList(Event): # pylint: disable=too-few-public-methods
    """Represents a player Actor status list

    :param timestamp: The timestamp of the event
    :type timestamp: Timestamp
    :param class_job_level: The actor's class, job, and level
    :type class_job_level: ClassJobLevel
    :param target_actor: The target actor that has status effects
    :type target_actor: Actor
    :param status_effects: A list of status effects
    :type status_effects: list[StatusEffect]
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 class_job_level: ClassJobLevel,
                 target_actor: Actor,
                 status_effects: list[StatusEffect],
                ):
        super().__init__(timestamp)
        self.class_job_level = class_job_level
        self.target_actor = target_actor
        self.status_effects = status_effects

    def __repr__(self):
        return '<StatusList>'


class StatusListBasic(Event): # pylint: disable=too-few-public-methods
    """Represents a simplified status list as opposed to ``StatusList``

    :param timestamp: The timestamp of the event
    :type timestamp: Timestamp
    :param target_actor: The target actor that has status effects
    :type target_actor: Actor
    :param status_effects: A list of status effects
    :type status_effects: list[StatusEffect]
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 target_actor: Actor,
                 status_effects: list[StatusEffect],
                ):
        super().__init__(timestamp)
        self.target_actor = target_actor
        self.status_effects = status_effects

    def __repr__(self):
        return '<StatusListBasic>'
