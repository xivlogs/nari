"""Parsing act data about abilities"""
from struct import unpack
from typing import List
from datetime import datetime

from nari.types.actioneffect import ActionEffect
from nari.types.event.ability import Ability, AoeAbility
from nari.types.actor import Actor
from nari.types.ability import Ability as AbilityType
from nari.types.event import Event

def action_effect_from_logline(params: List[str]) -> ActionEffect:
    """Takes the eight bytes from an act log line and returns ActionEffect data"""
    if len(params) != 2:
        raise Exception('Yell at nono to come up with a specific exception just for you')
    hexdata = ''.join([x.zfill(8) for x in params])
    intdata = int(hexdata, 16)
    parsed_params = unpack('>BBBBHBB', intdata.to_bytes(8, 'big'))
    param0, param1, severity, effect_type, value, flags, multiplier = parsed_params
    return ActionEffect(effect_type=effect_type, severity=severity, flags=flags, value=value, multiplier=multiplier, additional_params=[param0, param1])

def ability_from_logline(timestamp: datetime, params: List[str]) -> Event:
    """Returns an ability event from an act logline

    ACT Event ID (decimal): 21

    ## Param layout from act

    The first two params in every event is the act event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Source Actor ID|
    |1    |string|Source Actor Name|
    |2    |int|Ability id|
    |3    |string|ability name|
    |4    |int|Target Actor ID|
    |5    |string|Target Actor Name|
    |6-21 |ActionEffect(s)|Every two fields make up 1 ActionEffect. See `action_effect_from_logline` for more info on parsing this.|
    |22   |int|Source current HP|
    |23   |int|Source max MP|
    |24   |int|Source current HP|
    |25   |int|Source max HP|
    |26   |int|Source current TP/others?|
    |27   |int|Source max TP/others?|
    |28   |float|Source actor X position|
    |29   |float|Source actor Y position|
    |30   |float|Source actor Z position|
    |31   |float|Source actor facing|
    |32   |int|Target current HP|
    |33   |int|Target max MP|
    |34   |int|Target current HP|
    |35   |int|Target max HP|
    |36   |int|Target current TP/others?|
    |37   |int|Target max TP/others?|
    |38   |float|Target actor X position|
    |39   |float|Target actor Y position|
    |40   |float|Target actor Z position|
    |41   |float|Target actor facing|
    |42   |int|Sequence ID|

    """
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
    for i in range(0, 16, 2):
        index = i + 6
        action_effects.append(
            action_effect_from_logline(params[index:index+2])
        )
    # apparently when the target actor is 'none', then the *source* actor's resources will be empty will also be empty
    # also apparently, other time(s) it will be blank just because /shrug
    try:
        source_actor.resources.update(
            *[int(x) for x in params[22:28]]
        )
        source_actor.position.update(
            *[float(x) for x in params[28:32]]
        )
    except ValueError:
        pass

    try:
        target_actor.resources.update(
            *[int(x) for x in params[32:38]]
        )
        target_actor.position.update(
            *[float(x) for x in params[38:42]]
        )
    except ValueError:
        pass
    sequence_id = int(params[42], 16)

    return Ability(
        timestamp=timestamp,
        action_effects=action_effects,
        source_actor=source_actor,
        target_actor=target_actor,
        ability=ability,
        sequence_id=sequence_id,
    )

def aoeability_from_logline(timestamp: datetime, params: List[str]) -> Event:
    """Parses an aoe ability from logline"""
    # see ability_from_logline above for field definitions
    source_actor = Actor(*params[0:2])
    ability = AbilityType(*params[2:4])
    target_actor = Actor(*params[4:6])
    action_effects = []
    for i in range(0, 16, 2):
        index = i + 6
        action_effects.append(
            action_effect_from_logline(params[index:index+2])
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
    sequence_id = int(params[42], 16)
    return AoeAbility(
        timestamp=timestamp,
        action_effects=action_effects,
        source_actor=source_actor,
        target_actor=target_actor,
        ability=ability,
        sequence_id=sequence_id,
    )
