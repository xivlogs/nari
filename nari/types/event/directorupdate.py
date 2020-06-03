"""DirectorUpdate represents changes from the 'director' to content. For example, in instanced raid content, doing a fade-out is a common director event"""

from enum import IntEnum

from nari.types.event.base import Event
from nari.types.event import Type


class DirectorUpdateType(IntEnum):
    """These are related to the first param in the DirectorUpdate event"""
    BattleLeve = 0x8001
    GatheringLeve = 0x8002
    InstanceContent = 0x8003
    PublicContent = 0x8004
    QuestBattle = 0x8006
    CompanyLeve = 0x8007
    TreasureHunt = 0x8009
    GoldSaucer = 0x800A
    CompanyCraftDirector = 0x800B
    DpsChallange = 0x800D
    Fate = 0x801A

    @classmethod
    def name_for_value(cls, value):
        """Helper class method to return the name of the enum when you already have the value"""
        if value in cls.__members__.values():
            return cls(value).name
        return 'Unknown'


class DirectorUpdateCommand(IntEnum):
    """These are the 'command' portion of a director update"""
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
        """Helper class method to return the name of the enum when you already have the value"""
        if value in cls.__members__.values():
            return cls(value).name
        return 'Unknown'


class DirectorUpdate(Event):
    """Can apparently do several things:
    * change the music
    * reset zone on a wipe
    * limit gauge for bosses
    * updates on time remaining
    """
    __id__ = Type.directorupdate.value
    def handle_params(self):
        self.director_type = int(self.params[0][:4], 16)
        self.instance_id = int(self.params[0][4:], 16)
        self.director_command = int(self.params[1], 16)
        # param[2:6] - 4 bytes of arbitrary data, dependant on the director command

    def __repr__(self):
        dtype = DirectorUpdateType.name_for_value(self.director_type)
        dcomm = DirectorUpdateCommand.name_for_value(self.director_command)
        return f'<DirectorUpdate ({dtype}|{dcomm})>'
