from enum import IntEnum

class Type(IntEnum):
    """List of Event types from the ACT network log"""
    version = 253
    config = 249
    debug = 251
    hook = 250
    gauge = 31
    zonechange = 1
    changeplayer = 2
    addcombatant = 3
    playerstats = 12
    logline = 0
    removecombatant = 4
    networkstatuseffect = 38
    networkbuff = 26
    networkupdatehp = 39
    networkbuffremove = 30
    networkbegincast = 20
    networkability = 21
    networknametoggle = 34
    limitbreak = 36
    directorupdate = 33
    partylist = 11
    networkeffectresult = 37
    networktargetmarker = 29
    networkaoeability = 22
    networkdot = 24
    networktether = 35
    networktargetheadmarker = 27
    networkcancelability = 23
    networkdeath = 25

    @classmethod
    def has_id(cls, id: int) -> bool:
        return id in cls.__members__.values()

    @classmethod
    def has_type(cls, name: str) -> bool:
        return name in cls.__members__.keys()
