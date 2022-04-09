"""Information about jobs"""
from typing import NamedTuple
from enum import IntEnum

class Job(IntEnum):
    """A list of jobs"""
    GLA = 1
    PGL = 2
    LNC = 4
    ARC = 5
    CNJ = 6
    THM = 7
    PLD = 19
    MNK = 20
    DRG = 22
    BRD = 23
    WHM = 23
    BLM = 25
    ACN = 26
    SMN = 27
    SCH = 28
    ROG = 29
    NIN = 30
    MCH = 31
    DRK = 32
    AST = 33
    SAM = 34
    RDM = 35
    BLU = 36
    GNB = 37
    DNC = 38

class ClassJobLevel(NamedTuple):
    """A tuple containing data about a job"""
    sync_level: int
    job_level: int
    class_level: int
    job_id: Job
