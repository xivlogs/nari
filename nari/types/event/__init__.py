"""Base for event-related object code"""
from enum import IntEnum

# this should be renamed and moved up a module – perhaps EventType?
class Type(IntEnum):
    """List of Event types from the ACT network log"""
    logline = 0
    zonechange = 1
    changeplayer = 2
    addcombatant = 3
    removecombatant = 4
    partylist = 11
    playerstats = 12
    networkbegincast = 20
    networkability = 21
    networkaoeability = 22
    networkcancelability = 23
    networkdot = 24
    networkdeath = 25
    networkbuff = 26
    networktargetheadmarker = 27
    networktargetmarker = 29
    networkbuffremove = 30
    gauge = 31
    directorupdate = 33
    networknametoggle = 34
    networktether = 35
    limitbreak = 36
    networkeffectresult = 37
    networkstatuseffect = 38
    networkupdatehp = 39
    config = 249
    hook = 250
    debug = 251
    version = 253

    @classmethod
    def has_id(cls, id_: int) -> bool:
        """Returns True if the id is in the enum"""
        return id_ in cls.__members__.values()

    @classmethod
    def has_type(cls, name: str) -> bool:
        """Returns true if the name is in the enum"""
        return name in cls.__members__.keys()
