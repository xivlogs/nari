"""Just a bunch of helper methods to spit out events from the act log"""
from datetime import datetime
from struct import unpack
from typing import Callable, Dict, List

from nari.types.event import Event
from nari.types.event.act import Type as ActEventType
from nari.types.actioneffect import ActionEffect

DEFAULT_DATE_FORMAT: str = '%Y-%m-%dT%H:%M:%S.%f%z'
ActEventFn = Callable[[datetime, List[str]], Event]

# type ActionEffect struct {
#     EffectType  uint8
#     HitSeverity uint8
#     padding     uint8
#     Percentage  uint8
#     Multiplier  uint8 // Total Damage = 65535 * Multiplier * (Flags & 0x40) + Damage
#     Flags       uint8 // (Flags & 0xA0) means attacker receives damage instead
#     Damage      uint16
# }
def action_effect_from_logline(params: List[str]) -> ActionEffect:
    """Takes the eight bytes from an act log line and returns ActionEffect data"""
    if len(params) != 2:
        raise Exception('Yell at nono to come up with a specific exception just for you')
    hexdata = ''.join([x.rjust(8, '0') for x in params])
    intdata = int(hexdata, 16)
    parsed_params = unpack('>BBBBBBH', intdata.to_bytes(8, 'big'))
    effect_type, hit_severity, padding, percentage, multiplier, flags, damage = parsed_params
    return ActionEffect(effect_type=effect_type, hit_severity=hit_severity, padding=padding, percentage=percentage, multiplier=multiplier, flags=flags, damage=damage)


def ability_from_logline(timestamp: datetime, params: List[str]) -> Event:
    """Returns an ability event from a semi-parsed act logline"""
    ...

def date_from_act_timestamp(datestr: str) -> datetime:
    """Parse timestamp from act log into a python datetime object
    Look, this is dirty. This is wrong. Please someone find a better way to do this.
    """
    return datetime.strptime(f'{datestr[:26]}{datestr[-6:]}', DEFAULT_DATE_FORMAT)


ID_MAPPINGS: Dict[int, ActEventFn] = {
    ActEventType.networkability.value: ability_from_logline,
}
