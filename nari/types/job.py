"""Class that maps jobs to jobID
Reference: https://github.com/xivapi/ffxiv-datamining/blob/master/csv/ClassJob.csv
"""

from enum import IntEnum


class Job(IntEnum):
    """
    Jobs and abbreviations in game.
    """
    ADV = 0
    ADVENTURER = 0
    GLA = 1
    GLADIATOR = 1
    PGL = 2
    PUGILIST = 2
    MRD = 3
    MARAUDER = 3
    LNC = 4
    LANCER = 4
    ARC = 5
    ARCHER = 5
    CNJ = 6
    CONJURER = 6
    THM = 7
    THAUMATURGE = 7
    CRP = 8
    CARPENTER = 8
    BSM = 9
    BLACKSMITH = 9
    ARM = 10
    ARMORER = 10
    GSM = 11
    GOLDSMITH = 11
    LTW = 12
    LEATHERWORKER = 12
    WVR = 13
    WEAVER = 13
    ALC = 14
    ALCHEMIST = 14
    CUL = 15
    CULINARIAN = 15
    MIN = 16
    MINER = 16
    BTN = 17
    BOTANIST = 17
    FSH = 18
    FISHER = 18
    PLD = 19
    PALADIN = 19
    MNK = 20
    MONK = 20
    WAR = 21
    WARRIOR = 21
    DRG = 22
    DRAGOON = 22
    BRD = 23
    BARD = 23
    WHM = 24
    WHITE_MAGE = 24
    BLM = 25
    BLACK_MAGE = 25
    ACN = 26
    ARCANIST = 26
    SMN = 27
    SUMMONER = 27
    SCH = 28
    SCHOLAR = 28
    ROG = 29
    ROGUE = 29
    NIN = 30
    NINJA = 30
    MCH = 31
    MACHINIST = 31
    DRK = 32
    DARK_KNIGHT = 32
    AST = 33
    ASTROLOGIAN = 33
    SAM = 34
    SAMURAI = 34
    RDM = 35
    RED_MAGE = 35
    BLU = 36
    BLUE_MAGE = 36
    GNB = 37
    GUNBREAKER = 37
    DNC = 38
    DANCER = 38
