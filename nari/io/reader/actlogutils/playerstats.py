"""Parses playerstats events from ACT log line"""
from datetime import datetime
from typing import List, Dict

from nari.types.job import Job
from nari.types.stats import Stats
from nari.types.event.playerstats import PlayerStats
from nari.util.exceptions import ActLineReadError


def playerstats_from_logline(timestamp: datetime, params: List[str]) -> PlayerStats:
    """Parses playerstats event from logline.
    Param 15 is blank so it is parsed out.
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
