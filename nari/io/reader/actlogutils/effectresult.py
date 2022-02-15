"""Parses effect results from logline"""
from typing import List
from struct import unpack

from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor
from nari.types.event.effectresult import EffectResult, EffectResultEntry

def effectresult_from_logline(timestamp: Timestamp, params: List[str]) -> Event:
    """Returns an effect result event from an act log line

    ACT Event ID (decimal): 37

    ## Param layout from act

    The first two params in every event is the act event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Actor ID|
    |1    |string|Actor name|
    |2    |uint32|Sequence ID|
    |3    |int|Actor current HP|
    |4    |int|Actor max HP|
    |5    |int|Actor current MP|
    |6    |int|Actor max MP|
    |7    |uint8|Shield|
    |8    |null|Blank field|
    |9    |float|Actor X position|
    |10   |float|Actor Y position|
    |11   |float|Actor Z position|
    |12   |float|Actor facing|
    |13   |int|Unknown|
    |14   |int|Unknown|
    |15   |int|Unknown|
    |16   |int|EffectResult entry count|
    |17-N |EffectResult(s)|Every four fields makes up one EffectResult entry, and there are up to four groups, meaning N <= 29.|

    Each EffectResult entry has the following four fields, in order:

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|BBH -> EffectIndex / Padding / EffectId|
    |1    |int|II -> padding / some kind of param|
    |2    |float|Effect duration (as hex)|
    |3    |int|Source actor ID|

    """
    target_actor = Actor(*params[0:2])
    sequence_id = int(params[2], 16)
    try:
        target_actor.resources.update(
            *[int(x) for x in params[3:7]]
        )
        target_actor.position.update(
            *[int(x) for x in params[9:13]]
        )
    except ValueError:
        pass
    try:
        shield_percent = int(params[7], 16)
    except ValueError:
        shield_percent = 0

    effect_result_entries = []
    for i in range(17, len(params)-1, 4): # len(params)-1 because the last param is always blank
        effect_hexdata = int(params[i].zfill(8), 16)
        effect_index, _, effect_id = unpack('>BBH', effect_hexdata.to_bytes(4, 'big'))
        effect_duration, *_ = unpack('<f', int(params[i+2].zfill(8), 16).to_bytes(4, 'little'))
        source_actor_id = int(params[i+3].zfill(4), 16)
        effect_result_entries.append(
            EffectResultEntry(
                effect_index=effect_index,
                effect_id=effect_id,
                effect_duration=effect_duration,
                source_actor_id=source_actor_id
            )
        )
    return EffectResult(
        timestamp=timestamp,
        target_actor=target_actor,
        sequence_id=sequence_id,
        shield_percent=shield_percent,
        effect_results=effect_result_entries,
    )
