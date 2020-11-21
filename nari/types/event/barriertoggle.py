"""Class that represents events around toggled barrier(s)"""
from datetime import datetime
from enum import Enum, auto

from nari.types.event import Event

class BarrierState(Enum):
    down = auto()
    up = auto()


class BarrierToggle(Event): # pylint: disable=too-few-public-methods
    """Represents a barrier changing state"""
    def __init__(self, *,
                 timestamp: datetime,
                 instance_id: int,
                 state: BarrierState,
                ):
        super().__init__(timestamp)
        self.instance_id = instance_id
        self.state = BarrierState

    def __repr__(self):
        return '<BarrierToggle>'
