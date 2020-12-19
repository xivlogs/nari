"""Classes that represent events around instance state"""
from datetime import datetime
from enum import Enum, auto

from nari.types.event import Event

class Fade(Enum):
    In = auto()
    Out = auto()

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
