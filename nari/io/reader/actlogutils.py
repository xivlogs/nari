"""Just a bunch of helper methods to spit out events from the act log"""
from datetime import datetime
from typing import Callable, Dict, List

from nari.types.event import Event
from nari.types.event.startcast import StartCast
from nari.types.event.act import Type as ActEventType
from nari.types.event.stopcast import StopCastType, StopCast
from nari.types.event.limitbreak import LimitBreak
from nari.types.event.death import Death
from nari.types.actor import Actor

DEFAULT_DATE_FORMAT: str = '%Y-%m-%dT%H:%M:%S.%f%z'
ActEventFn = Callable[[datetime, List[str]], Event]

def limitbreak_from_logline(timestamp: datetime, params: List[str]) -> Event:
    # param layout from act
    # 0 - bar amount; 10,000 = 1 full bar
    # 1 - number of bars (3 for 3 full limit bars)
    amount = int(params[0], 16)
    bars = int(params[1])
    return LimitBreak(
        timestamp=timestamp,
        amount=amount,
        bars=bars
    )

def date_from_act_timestamp(datestr: str) -> datetime:
    """Parse timestamp from act log into a python datetime object
    Look, this is dirty. This is wrong. Please someone find a better way to do this.
    """
    return datetime.strptime(f'{datestr[:26]}{datestr[-6:]}', DEFAULT_DATE_FORMAT)


ID_MAPPINGS: Dict[int, ActEventFn] = {
}
