"""
Status effects
~~~~~~~~~~~~~~
"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor
from nari.types.status import Status


class StatusApply(Event): # pylint: disable=too-few-public-methods
    """Represents the application of a status

    :param timestamp: The timestamp of the event
    :type timestamp: Timestamp
    :param status: The status effect being applied
    :type status: Status
    :param duration: The duration the status will be in effect for
    :type duration: float
    :param source_actor: The actor that applied the effect
    :type source_actor: Actor
    :param target_actor: The actor that is the recipient of the effect
    :type target_actor: Actor
    :param params: TODO:
    :type params: int
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 status: Status,
                 duration: float,
                 source_actor: Actor,
                 target_actor: Actor,
                 params: int,
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
    """Represents the removal of a status

    :param timestamp: The timestamp of the event
    :type timestamp: Timestamp
    :param status: The status effect being removed
    :type status: Status
    :param duration: TODO: why is there a duration when it's removed??
    :type duration: float
    :param source_actor: TODO: why do we care about a source actor when it's gone?
    :type source_actor: Actor
    :param target_actor: The actor that the effect is being removed from
    :type target_actor: Actor
    :param params: TODO:
    :type params: int
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 status: Status,
                 duration: float,
                 source_actor: Actor,
                 target_actor: Actor,
                 params: int,
                ):
        super().__init__(timestamp)
        self.status = status
        self.duration = duration
        self.source_actor = source_actor
        self.target_actor = target_actor
        self.params = params

    def __repr__(self):
        return '<StatusRemove>'
