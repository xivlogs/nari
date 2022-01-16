"""Parses effect results from logline"""
from datetime import datetime
from typing import List
from struct import unpack

from nari.types.event import Event
from nari.types.actor import Actor
from nari.types.event.effectresult import EffectResult, EffectResultEntry

def effectresult_from_logline(timestamp: datetime, params: List[str]) -> Event:
    """Helper function to parse effect result data from act log line"""
    # param layout from act
    # 0-1 Actor ID/Name
    # 2 Sequence ID (uint32)
    # 3-4 Actor HP/Max HP
    # 5-6 Actor MP/Max MP
    # 7 Shield (uint8)
    # 8 Blank?
    # 9-12 X/Y/Z/Facing
    # 13 unknown
    # 14 unknown
    # 15 unknown
    # 16 effect result entry count
    # 17-(N-1) Effect Result Entries (up to 4 groups, meaning N <= 29)
    # These have the following 4 fields in order
    #     1. BBH -> EffectIndex / Padding / EffectId
    #     2. II -> padding / some kind of param
    #     3. effect duration (float as hex)
    #     4. source actor id
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
    shield_percent = int(params[7], 16)

    effect_result_entries = []
    for i in range(17, len(params)-1, 4): # len(params)-1 because the last param is always blank
        effect_hexdata = int(params[i].zfill(8), 16)
        effect_index, _, effect_id = unpack('>BBH', effect_hexdata.to_bytes(4, 'big'))
        effect_duration = unpack('<f', int(params[i+2].zfill(8), 16).to_bytes(4, 'little'))
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

