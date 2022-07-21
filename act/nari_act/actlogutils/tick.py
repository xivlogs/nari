"""Parse effect-over-time data from ACT log line"""
from nari.types import Timestamp
from nari.types.event.ticks import DamageOverTime, HealOverTime
from nari.types.actor import Actor
from nari.types.event import Event
from nari_act.actlogutils.exceptions import ActLineParsingException


def tick_from_logline(timestamp: Timestamp, params: list[str]) -> Event:
    """Parses a DoT/HoT tick event from an ACT log line

    ACT Event ID (decimal): 24

    ## Param layout from ACT

    The first two params in every event is the ACT event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Actor ID|
    |1    |string|Actor name|
    |2    |str|DoT or HoT|
    |3    |int|Effect ID, seemingly only applies to ground effects|
    |4    |int|Effect Amount|
    """
    actor = Actor(*params[0:2])
    category = params[2]
    match category.lower():
        case 'dot':
            return DamageOverTime(
                timestamp=timestamp,
                actor=actor,
                effect_id=int(params[3], 16),
                value=int(params[4], 16)
            )

        case 'hot':
            return HealOverTime(
                timestamp=timestamp,
                actor=actor,
                effect_id=int(params[3], 16),
                value=int(params[4], 16)
            )

        case _:
            raise ActLineParsingException(f'Expected DoT or HoT for effect over time category, got {category}')
