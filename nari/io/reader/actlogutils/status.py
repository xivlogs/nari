"""Parse status data from ACT log line"""
from struct import unpack

from nari.types import Timestamp
from nari.types.event.statuslist import StatusList
from nari.types.event.status import StatusApply, StatusRemove
from nari.types.status import Status, StatusEffect
from nari.types.actor import Actor
from nari.types.event import Event
from nari.types.classjoblevel import ClassJobLevel

def classjoblevel_from_logline(param: str) -> ClassJobLevel:
    """Takes a classjoblevel field (From status packets) and parses it"""
    intdata = int(param, 16)
    parsed_params = unpack('>BBBB', intdata.to_bytes(4, 'big'))
    return ClassJobLevel(
        sync_level=parsed_params[0],
        job_level=parsed_params[1],
        class_level=parsed_params[2],
        job_id=parsed_params[3],
    )

def status_effect_from_logline(param0, param1, param2):
    """Helper function to parse a status effect from log line data"""
    # Assuming some input of 0A0168|41F00000|E0000000
    # 000A0168 is the status id (last 4 bytes), and status params (first 4 bytes)
    # 41F00000 is the duration as a float (30s, in this case)
    # E0000000 is the source actor id (E0000000 = no source actor)
    param0_int = int(param0.zfill(8), 16)
    status_params, status_id = unpack(
        '>HH',
        param0_int.to_bytes(4, 'big')
    )
    duration = unpack(
        '>f',
        int(param1.zfill(8), 16).to_bytes(4, 'big'),
    )[0]
    source_actor_id = int(param2, 16)
    return StatusEffect(
        status_id=status_id,
        status_params=status_params,
        duration=duration,
        source_actor_id=source_actor_id
    )

def statuslist_from_logline(timestamp: Timestamp, params: list[str]) -> Event:
    """Parses a StatusList event from an ACT log line

    ACT Event ID (decimal): 38

    ## Param layout from ACT

    The first two params in every event is the ACT event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Target actor ID|
    |1    |string|Target actor name|
    |2    |ClassJobLevel|Target actor ClassJob level|
    |3    |int|Target current HP|
    |4    |int|Target max HP|
    |5    |int|Target current MP|
    |6    |int|Target max MP|
    |7    |int|Target current TP|
    |8    |int|Target max TP|
    |9    |float|Target actor X position|
    |10   |float|Target actor Y position|
    |11   |float|Target actor Z position|
    |12   |float|Target actor bearing|
    |13-N |StatusEffect(s)|List of StatusEffects, in sets of 3|
    """
    target_actor = Actor(*params[0:2])
    class_job_level = classjoblevel_from_logline(params[2])
    try:
        target_actor.resources.update(
            *[int(x) for x in params[3:9]]
        )
    except ValueError:
        pass
    if '' not in params[9:13]:
        target_actor.position.update(
            *[float(x) for x in params[9:13]]
        )
    remaining_params = len(params) - 1
    status_effects: list[StatusEffect] = []
    for i in range(13, remaining_params, 3):
        status_effects.append(
            status_effect_from_logline(*params[i:i+3])
        )

    return StatusList(
        timestamp=timestamp,
        class_job_level=class_job_level,
        target_actor=target_actor,
        status_effects=status_effects
    )

def statusapply_from_logline(timestamp: Timestamp, params: list[str]) -> Event:
    """Parse status apply from ACT log line"""
    # param layout from act
    # 0-1 - Status ID / Name
    # 2 - Status Duration
    # 3-4 - Source Actor
    # 5-6 - Target Actor
    # 7 - param(s)
    # 8-9 - Source Actor HP/Max HP
    status = Status(int(params[0], 16), params[1])
    duration = float(params[2])
    source_actor = Actor(*params[3:5])
    target_actor = Actor(*params[5:7])
    status_params = int(params[7], 16)
    # source_actor.resources.update(*[int(x) for x in params[8:10]])
    return StatusApply(
        timestamp=timestamp,
        status=status,
        duration=duration,
        source_actor=source_actor,
        target_actor=target_actor,
        params=status_params,
    )

def statusremove_from_logline(timestamp: Timestamp, params: list[str]) -> Event:
    """Parse status remove from ACT log line"""
    # param layout from act
    # 0-1 - Status ID / Name
    # 2 - Status Duration
    # 3-4 - Source Actor
    # 5-6 - Target Actor
    # 7 - status params
    # 8-9 - Target / Source max hp
    status = Status(int(params[0]), params[1])
    duration = float(params[2])
    source_actor = Actor(*params[3:5])
    target_actor = Actor(*params[5:7])
    status_params = int(params[7])
    target_actor.resources.hp_max = int(params[8])
    source_actor.resources.hp_max = int(params[9])
    return StatusRemove(
        timestamp=timestamp,
        status=status,
        duration=duration,
        source_actor=source_actor,
        target_actor=target_actor,
        params=status_params
    )
