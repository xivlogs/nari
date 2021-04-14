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
    Strength = 1
    DEX = 2
    Dexterity = 2
    VIT = 3
    Vitality = 3
    INT = 4
    Intelligence = 4
    MND = 5
    Mind = 5
    PIE = 6
    Piety = 6
    ATK = 20
    Attack_Power = 20
    DH = 22
    Direct_Hit_Rate = 22
    CRIT = 27
    Critical_Hit = 27
    MATK = 33
    Attack_Magic_Potency = 33
    HATK = 34
    Healing_Magic_Potency = 34
    DET = 44
    Determination = 44
    SKS = 45
    Skill_Speed = 45
    SPS = 46
    Spell_Speed = 46
    TEN = 19
    Tenacity = 19
