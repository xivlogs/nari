"""Parses playerstats events from ACT log line"""
from datetime import datetime
from typing import List

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

    stats_definitions = ("JOB", "STR", "DEX", "VIT", "INT", "MND", "PIE", "ATTACK POWER", "DIRECT HIT", "CRITICAL HIT",
                         "ATTACK MAGIC POTENCY", "HEAL MAGIC POTENCY", "DETERMINATION", "SKILL SPEED", "SPELL SPEED",
                         "TENACITY")
    param_ints = (int(param) for param in params if param != "0")
    player_stats = dict(zip(stats_definitions, param_ints))

    # Malformed line check
    if len(player_stats) != 17:
        raise ActLineReadError("Params are unexpectedly short")

    # clear the blank field
    try:
        del player_stats["delete"]
    except KeyError as key_error:
        raise ActLineReadError("Missing delete field") from key_error

    return PlayerStats(timestamp, player_stats)
