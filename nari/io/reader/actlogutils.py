"""Just a bunch of helper methods to spit out events from the act log"""
from datetime import datetime
from struct import unpack
from typing import Callable, Dict, List

from nari.types.event import Event
from nari.types.event.ability import Ability
from nari.types.event.act import Type as ActEventType
from nari.types.actioneffect import ActionEffect
from nari.types.actor import Actor
from nari.types.ability import Ability as AbilityType

DEFAULT_DATE_FORMAT: str = '%Y-%m-%dT%H:%M:%S.%f%z'
ActEventFn = Callable[[datetime, List[str]], Event]


def action_effect_from_logline(params: List[str]) -> ActionEffect:
    """Takes the eight bytes from an act log line and returns ActionEffect data"""
    if len(params) != 2:
        raise Exception('Yell at nono to come up with a specific exception just for you')
    hexdata = ''.join([x.rjust(8, '0') for x in params])
    intdata = int(hexdata, 16)
    parsed_params = unpack('>BBBBHBB', intdata.to_bytes(8, 'big'))
    param0, param1, param2, effect_type, value, flags, extended_value_high_bytes = parsed_params
    return ActionEffect(effect_type=effect_type, flags=flags, value=value, extended_value_high_bytes=extended_value_high_bytes, additional_params=[param0, param1, param2])


def ability_from_logline(timestamp: datetime, params: List[str]) -> Event:
    """Returns an ability event from a semi-parsed act logline"""
    # param layout from act
    # 0-1 source actor id/name
    # 2-3 ability id/name
    # 4-5 target actor id/name
    # 6-21 ActionEffect(s) (every 2 fields is 1 ActionEffect)
    # 22-23 source current/max hp
    # 24-25 source current/max mp
    # 26-27 source current/max tp/others?
    # 28-31 source actor x/y/z/facing
    # 32-33 target current/max hp
    # 34-35 target current/max mp
    # 36-37 target current/max tp/others?
    # 38-41 target actor x/y/z/facing
    # 42 globalsequence
    source_actor = Actor(*params[0:2])
    ability = AbilityType(*params[2:4])
    target_actor = Actor(*params[4:6])
    action_effects = []
    for i in range(8):
        n = i + 6
        action_effects.append(
            action_effect_from_logline(params[n:n+2])
        )
    source_actor.resources.update(
        *[int(x) for x in params[22:28]]
    )
    source_actor.position.update(
        *[float(x) for x in params[28:32]]
    )
    target_actor.resources.update(
        *[int(x) for x in params[32:38]]
    )
    target_actor.position.update(
        *[float(x) for x in params[38:42]]
    )
    return Ability(
        timestamp=timestamp,
        action_effects=action_effects,
        source_actor=source_actor,
        target_actor=target_actor,
        ability=ability
    )


def date_from_act_timestamp(datestr: str) -> datetime:
    """Parse timestamp from act log into a python datetime object
    Look, this is dirty. This is wrong. Please someone find a better way to do this.
    """
    return datetime.strptime(f'{datestr[:26]}{datestr[-6:]}', DEFAULT_DATE_FORMAT)


ID_MAPPINGS: Dict[int, ActEventFn] = {
    ActEventType.networkability.value: ability_from_logline,
}
