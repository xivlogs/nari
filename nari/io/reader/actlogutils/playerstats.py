"""Parses playerstats events from ACT log line"""
from datetime import datetime
from typing import List, Dict

from nari.types.job import Job
from nari.types.stats import Stats
from nari.types.event.playerstats import PlayerStats
from nari.util.exceptions import ActLineReadError


def playerstats_from_logline(timestamp: datetime, params: List[str]) -> PlayerStats:
    """Parses a PlayerStats event from an act log line

    ACT Event ID (decimal): 12

    ## Param layout from act

    The first two params in every event is the act event ID and the timestamp it was parsed; the following table documents all the other fields.

    Param 15 is blank so it is parsed out.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Class/Job ID|
    |1    |int|Strength|
    |2    |int|Dexterity|
    |3    |int|Vitality|
    |4    |int|Intelligence|
    |5    |int|Mind|
    |6    |int|Piety|
    |7    |int|Attack power|
    |8    |int|Direct hit|
    |9    |int|Critical hit|
    |10   |int|Attack magic potency|
    |11   |int|Heal magic potency|
    |12   |int|Determination|
    |13   |int|Skill speed|
    |14   |int|Spell speed|
    |15   |int|Blank (0)|
    |16   |int|Tenacity|
    
    """

    param_order: List[Stats] = [
        Stats.STR,
        Stats.DEX,
        Stats.VIT,
        Stats.INT,
        Stats.MND,
        Stats.PIE,
        Stats.ATK,
        Stats.DH,
        Stats.CRIT,
        Stats.MATK,
        Stats.HATK,
        Stats.DET,
        Stats.SKS,
        Stats.SPS,
        Stats.TEN,
    ]

    # to ensure the correct number of params are extracted
    param_count = 17

    param_ints = [int(param) for param in params[0:param_count] if param != "0"]

    # Malformed line check
    if len(param_ints) != 16:
        raise ActLineReadError("Params are unexpectedly short")

    job = Job(param_ints.pop(0))
    stats: Dict[Stats, int] = dict(zip(param_order, param_ints))

    return PlayerStats(timestamp, job, stats)
