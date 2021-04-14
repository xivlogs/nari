"""Class that maps jobs to jobID
Reference: https://github.com/xivapi/ffxiv-datamining/blob/master/csv/ClassJob.csv
"""

from enum import IntEnum


class Job(IntEnum):
    """
    Jobs and abbreviations in game.
    """
    ADV = 0
    adventurer = 0
    GLA = 1
    gladiator = 1
    PGL = 2
    pugilist = 2
    MRD = 3
    marauder = 3
    LNC = 4
    lancer = 4
    ARC = 5
    archer = 5
    CNJ = 6
    conjurer = 6
    THM = 7
    thaumaturge = 7
    CRP = 8
    carpenter = 8
    BSM = 9
    blacksmith = 9
    ARM = 10
    armorer = 10
    GSM = 11
    goldsmith = 11
    LTW = 12
    leatherworker = 12
    WVR = 13
    weaver = 13
    ALC = 14
    alchemist = 14
    CUL = 15
    culinarian = 15
    MIN = 16
    miner = 16
    BTN = 17
    botanist = 17
    FSH = 18
    fisher = 18
    PLD = 19
    paladin = 19
    MNK = 20
    monk = 20
    WAR = 21
    warrior = 21
    DRG = 22
    dragoon = 22
    BRD = 23
    bard = 23
    WHM = 24
    white_mage = 24
    BLM = 25
    black_mage = 25
    ACN = 26
    arcanist = 26
    SMN = 27
    summoner = 27
    SCH = 28
    scholar = 28
    ROG = 29
    rogue = 29
    NIN = 30
    ninja = 30
    MCH = 31
    machinist = 31
    DRK = 32
    dark_knight = 32
    AST = 33
    astrologian = 33
    SAM = 34
    samurai = 34
    RDM = 35
    red_mage = 35
    BLU = 36
    blue_mage = 36
    GNB = 37
    gunbreaker = 37
    DNC = 38
    dancer = 38
