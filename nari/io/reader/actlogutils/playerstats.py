"""Parses playerstats events from ACT log line"""
from datetime import datetime
from typing import List

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

    param_ints = [int(param) for param in params if param != "0"]
    # Malformed line check
    if len(param_ints) != 16:
        raise ActLineReadError("Params are unexpectedly short")

    job = Job(param_ints.pop(0))
    stats = [Stats(param) for param in param_ints]

    return PlayerStats(timestamp, job, stats)
