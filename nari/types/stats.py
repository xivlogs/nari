"""Class that maps stats to the statID.
Note: Abbreviations are not official.

Reference: https://github.com/xivapi/ffxiv-datamining/blob/master/csv/ActionParam.csv
"""

from enum import IntEnum


class Stats(IntEnum):
    """
    Stats and abbreviations in game.
    """
    STR = 1
    STRENGTH = 1
    DEX = 2
    DEXTERITY = 2
    VIT = 3
    VITALITY = 3
    INT = 4
    INTELLIGENCE = 4
    MND = 5
    MIND = 5
    PIE = 6
    PIETY = 6
    ATK = 20
    ATTACK_POWER = 20
    DH = 22
    DIRECT_HIT_RATE = 22
    CRIT = 27
    CRITICAL_HIT = 27
    MATK = 33
    ATTACK_MAGIC_POTENCY = 33
    HATK = 34
    HEALING_MAGIC_POTENCY = 34
    DET = 44
    DETERMINATION = 44
    SKS = 45
    SKILL_SPEED = 45
    SPS = 46
    SPELL_SPEED = 46
    TEN = 19
    TENACITY = 19
