from enum import IntEnum

class DirectorUpdateType(IntEnum):
    BattleLeve = 0x8001,
    GatheringLeve = 0x8002,
    InstanceContent = 0x8003,
    PublicContent = 0x8004,
    QuestBattle = 0x8006,
    CompanyLeve = 0x8007,
    TreasureHunt = 0x8009,
    GoldSaucer = 0x800A,
    CompanyCraftDirector = 0x800B,
    DpsChallange = 0x800D,
    Fate = 0x801A

    @classmethod
    def name_for_value(cls, value):
        if value in cls.__members__.values():
            return cls(value).name
        return 'Unknown'

class DirectorUpdateCommand(IntEnum):
    init = 0x40000001 # params: 3: duty length in seconds, eg 0xE10 is 3600 or 1 hour, 4-6: unused
    complete = 0x40000002 # params: 3 unused, 4: passed to director, 5-6: unused
    clear = 0x40000003 # params: 3: fadeout seq if 0x1, otherwise return immediately (ie first clear cutscene flag), 4-6: unused
    timer = 0x40000004 # params: 3: duty time in seconds, 4-6: unused
    fadeout = 0x40000005 # params: unused
    barrierdown = 0x40000006 # restart, show "forward!", puts barrier down – params: 3: duty time left in seconds, 4-6: unused
    noclue = 0x40000007 # params: examples, no clue tho (0x6, 0x0, 0x0, 0x0, 0x0, 0x0), (0x6, 0x1, 0x0, 0x0, 0x0, 0x0)
    initvote = 0x40000008 # init vote (ie abandon, kick, etc) – params: 3: vote type, 4: unused, 5-6: unknown
    concludevote = 0x40000009 # conclude vote – params: 3: vote type, 4: 1 for succeed/0 for fail, 5-6: unknown
    partyinvite = 0x4000000A # "you invite x to a party" – params: 3: log message id?, 4: log message param?, 5-6: unused
    newtoduty = 0x4000000D # "one or more party members are new to this duty, a bonus will be awarded for swift completion of objectives" – params: seems all unused
    fadein = 0x40000010 # fade in for reset - params: 3: time left in seconds, 4-6: unused?
    barrierup = 0x40000012 # puts the barrier up – params: seems all unused?

    @classmethod
    def name_for_value(cls, value):
        if value in cls.__members__.values():
            return cls(value).name
        return 'Unknown'