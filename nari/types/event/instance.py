"""
Instance-specific events
~~~~~~~~~~~~~~~~~~~~~~~~

Classes that represent director commands to manage instance duty state.

TODO: talk about instance_id and how to turn it into an instance
"""
from enum import Enum, auto

from nari.types import Timestamp
from nari.types.event import Event


# pylint: disable=invalid-name
class Fade(Enum):
    """Enums for fade in/out"""
    In = auto()
    """Fade back in from black"""
    Out = auto()
    """Fade to black"""


class BarrierState(Enum):
    """Enums for barrier state"""
    down = auto()
    """The barrier holding actors in place disappears"""
    up = auto()
    """A barrier at the start of an instance keeps players from moving beyond a specified zone"""
# pylint: enable=invalid-name


class InstanceComplete(Event): # pylint: disable=too-few-public-methods
    """Represents an instance being complete

    :param timestamp: Timestamp that the event occurred at
    :type timestamp: Timestamp
    :param instance_id: The instance id
    :type instance_id: int
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 instance_id: int,
                ):
        super().__init__(timestamp)
        self.instance_id = instance_id


    def __repr__(self):
        return '<InstanceComplete>'


class InstanceVote(Event): # pylint: disable=too-few-public-methods
    """Represents the start of a vote

    :param timestamp: Timestamp the event occurred at
    :type timestamp: Timestamp
    :param instance_id: The instance id
    :type instance_id: int
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 instance_id: int,
                ):
        super().__init__(timestamp)
        self.instance_id = instance_id

    def __repr__(self):
        return '<InstanceVote>'


class InstanceFade(Event): # pylint: disable=too-few-public-methods
    """Represents fade out/in

    :param timestamp: Timestamp the event occurred at
    :type timestamp: Timestamp
    :param instance_id: The instance id
    :type instance_id: int
    :param state: Shows if the instance is fading in or out
    :type state: Fade
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 instance_id: int,
                 state: Fade,
                ):
        super().__init__(timestamp)
        self.instance_id = instance_id
        self.state = state

    def __repr__(self):
        return '<InstanceFade>'


class BarrierToggle(Event): # pylint: disable=too-few-public-methods
    """Represents a barrier changing state

    :param timestamp: Timestamp the event occurred at
    :type timestamp: Timestamp
    :param instance_id: the instance id
    :type instance_id: int
    :param state: The state of the barrier
    :type state: BarrierState
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 instance_id: int,
                 state: BarrierState,
                ):
        super().__init__(timestamp)
        self.instance_id = instance_id
        self.state = state

    def __repr__(self):
        return '<BarrierToggle>'


class InstanceInit(Event): # pylint: disable=too-few-public-methods
    """Represents entering an instance

    :param timestamp: Timestamp the event occurred at
    :type timestamp: Timestamp
    :param instance_id: The instance id
    :type instance_id: int
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 instance_id: int,
                ):
        super().__init__(timestamp)
        self.instance_id = instance_id

    def __repr__(self):
        return '<InstanceInit>'
