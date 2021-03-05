"""Classes that represent events around instance state"""
from datetime import datetime
from enum import Enum, auto

from nari.types.event import Event


# pylint: disable=invalid-name
class Fade(Enum):
    """Enums for fade in/out"""
    In = auto()
    Out = auto()


class BarrierState(Enum):
    """Enums for barrier state"""
    down = auto()
    up = auto()
# pylint: enable=invalid-name


class InstanceComplete(Event): # pylint: disable=too-few-public-methods
    """Represents an instance being complete"""
    def __init__(self, *,
                 timestamp: datetime,
                 instance_id: int,
                ):
        super().__init__(timestamp)
        self.instance_id = instance_id

    def __repr__(self):
        return '<InstanceComplete>'


class InstanceVote(Event): # pylint: disable=too-few-public-methods
    """Represents voting mechanics"""
    def __init__(self, *,
                 timestamp: datetime,
                instance_id: int,
                ):
        super().__init__(timestamp)
        self.instance_id = instance_id

    def __repr__(self):
        return '<InstanceVote>'


class InstanceFade(Event): # pylint: disable=too-few-public-methods
    """Represents fade out/in"""
    def __init__(self, *,
                 timestamp: datetime,
                 instance_id: int,
                 state: Fade
                ):
        super().__init__(timestamp)
        self.instance_id = instance_id
        self.state = state

    def __repr__(self):
        return '<InstanceFade>'


class BarrierToggle(Event): # pylint: disable=too-few-public-methods
    """Represents a barrier changing state"""
    def __init__(self, *,
                 timestamp: datetime,
                 instance_id: int,
                 state: BarrierState,
                ):
        super().__init__(timestamp)
        self.instance_id = instance_id
        self.state = state

    def __repr__(self):
        return '<BarrierToggle>'


class InstanceInit(Event): # pylint: disable=too-few-public-methods
    """Represents entering an instance"""
    def __init__(self, *,
                 timestamp: datetime,
                 instance_id: int,
                ):
        super().__init__(timestamp)
        self.instance_id = instance_id

    def __repr__(self):
        return '<InstanceInit>'
