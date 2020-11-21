from datetime import datetime
from typing import List
from struct import unpack

from nari.types.event import Event
from nari.types.event.version import Version
from nari.types.event.config import Config
from nari.types.actor import Actor

def version_from_logline(timestamp: datetime, params: List[str]) -> Event:
    # param layout from act
    # 0 the version string that's it pack it up and take it home
    return Version(timestamp=timestamp, version=params[0])

def config_from_logline(timestamp: datetime, params: List[str]) -> Event:
    # param layout from act
    # 0 a string with a bunch of configurations values separated by commas
    args = params[0].split(', ')
    values = {k:v for k,v in [s.split(': ') for s in args]}
    return Config(timestamp=timestamp, values=values)

def effect_result_from_logline(timestamp: datetime, params: List[str]) -> Event:
    # param layout from act
    # 0-1  ActorId / Name
    # 2    SequenceId (Hex)
    # 3-6  current/max hp and mp
    # 7    shield percent (decimal)
    # 8    null (cuuurse you)
    # 9-12 xyz/facing
    # 13   classjob (the upper byte, the lower byte is useless)
    # 14   fixed at 0 for some reason
    # 15   padding?
    # 16   number of 'in use effects' (decimal?)
    # The in-use effects have the following fields:
    # 1    BBH -> EffectIndex / Padding / EffectId
    # 2    II  -> padding / some kind of param
    # 3    effect duration (float as hex)
    # 4    source actor id
    target_actor = Actor(*params[0:2])
    sequence_id = int(params[2])
    target_actor.resources.update(
        *[int(x) for x in params[3:7]]
    )
    shield_percent = int(params[7], 16)
    target_actor.position.update(
        *[float(x) for x in params[9:13]]
    )
    cji_hexdata = int(params[13].rjust(4, '0'), 16)
    class_job_id, _ = unpack('>BB', cji_hexdata.to_bytes(2, 'big'))
    in_use_effects_amount = int(params[16])
