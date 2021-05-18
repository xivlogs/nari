"""Parses playerstats events from ACT log line"""
from datetime import datetime
from typing import List, Dict

from nari.types.job import Job
from nari.types.stats import Stats
from nari.types.event.playerstats import PlayerStats
from nari.util.exceptions import ActLineReadError


def playerstats_from_logline(timestamp: datetime, params: List[str]) -> PlayerStats:
    """Parses playerstats event from logline.
    Format is as follows:

    0: JOB
    1: STR
    2: DEX
    3: VIT
    4: INT
    5: MND
    6: PIE
    7: ATTACK POWER
    8: DHIT
    9: CRIT
    10: ATTACK MAGIC POTENCY
    11: HEAL MAGIC POTENCY
    12: DET
    13: SKILL SPEED
    14: SPELL SPEED
    15: Blank (0)
    16: TENACITY
    """

    # param to stat dict
    param_to_stat = {
        0: 0,
        1: Stats.STR,
        2: Stats.DEX,
        3: Stats.VIT,
        4: Stats.INT,
        5: Stats.MND,
        6: Stats.PIE,
        7: Stats.ATK,
        8: Stats.DH,
        9: Stats.CRIT,
        10: Stats.MATK,
        11: Stats.HATK,
        12: Stats.DET,
        13: Stats.SKS,
        14: Stats.SPS,
        15: Stats.TEN,
    }

    # to ensure the correct number of params are extracted
    param_count = 17

    param_ints = [int(param) for param in params[0:param_count] if param != "0"]
    # Malformed line check
    if len(param_ints) != 16:
        raise ActLineReadError("Params are unexpectedly short")

    job = Job(param_ints[0])
    stats: Dict[Stats, int] = {param_to_stat[i]: param for i, param in enumerate(param_ints)}

    return PlayerStats(timestamp, job, stats)
