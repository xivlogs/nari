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