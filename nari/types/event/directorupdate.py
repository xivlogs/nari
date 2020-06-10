"""DirectorUpdate represents changes from the 'Director' to the 'scene' in-game

When something more global than the actor scope happens, it's likely initiated by the director.
For example, on a wipe, the director will prompt fade to black, fade back in, and raising/lowering
the barrier.
"""

from enum import IntEnum

from nari.types.event.base import Event
from nari.types.event import Type


class DirectorUpdateType(IntEnum):
    """Relates to the type of content that's being 'directed'"""
    BattleLeve = 0x8001
    """Content is a combat leve duty"""
    GatheringLeve = 0x8002
    """Content is a gathering leve duty"""
    InstanceContent = 0x8003
    """Any type of content that is an instance

    Instanced content include:

    * Raid arenas
    * Dungeons
    * Alliance areas
    * Trials
    """
    PublicContent = 0x8004
    """Not sure what this is. Just regular stuff?"""
    QuestBattle = 0x8006
    """Not sure what this is. Perhaps instanced content like job quests?"""
    CompanyLeve = 0x8007
    """Need a better description."""
    TreasureHunt = 0x8009
    """Content that involves treasure maps with adds; perhaps also the 'dungeon' area afterwards?"""
    GoldSaucer = 0x800A
    """Probably related to GATEs"""
    CompanyCraftDirector = 0x800B
    """I'm assuming this is the 'group craft' actions like when you make an airship"""
    DpsChallange = 0x800D
    """Stone, Sea, Sky content"""
    Fate = 0x801A
    """FATE-related content"""

    @classmethod
    def name_for_value(cls, value):
        """Helper class method to return the name of the enum when you already have the value"""
        if value in cls.__members__.values():
            return cls(value).name
        return 'Unknown'


class DirectorUpdateCommand(IntEnum):
    """These are the 'command' portion of a director update"""
    init = 0x40000001 # params: 3: duty length in seconds, eg 0xE10 is 3600 or 1 hour, 4-6: unused
    """When a piece of content is initialized

    Params that follow the command:

    | Index | Description        |
    | ----: | -----------------: |
    | 3     | *unused*           |
    | 4     | passed to director |
    | 5-6   | *unused*           |
    """
    complete = 0x40000002 # "Duty Complete" flying text
    """When a piece of content ends

    Params that follow the command:

    | Index | Description        |
    | ----: | -----------------: |
    | 3     | *unused*           |
    | 4     | passed to director |
    | 5-6   | *unused*           |
    """
    clear = 0x40000003
    """Emits when a piece of content is 'cleared'

    Params that follow the command:

    | Index | Description                                           |
    | ----: | ----------------------------------------------------: |
    | 3     | `0x1` if a first-time clear (causes fadeout sequence) |
    | 4-6   | *unused*                                              |
    """
    timer = 0x40000004
    """The duty time in seconds

    Params that follow the command:

    | Index | Description            |
    | ----: | ---------------------: |
    | 3     | Duty time (in seconds) |
    | 4-6   | *unused*               |
    """
    fadeout = 0x40000005
    """Instructs the screen to fade to black"""
    barrierdown = 0x40000006
    """Takes the 'instance' barrier down"""
    noclue = 0x40000007 # params: examples, no clue tho (0x6, 0x0, 0x0, 0x0, 0x0, 0x0), (0x6, 0x1, 0x0, 0x0, 0x0, 0x0)
    initvote = 0x40000008 # init vote (ie abandon, kick, etc) – params: 3: vote type, 4: vote initiator, 5-6: unknown
    """Promps a vote to be held

    Params that follow the command:

    | Index | Description             |
    | ----: | ----------------------: |
    | 3     | vote type               |
    | 4     | vote initiator actor ID |
    | 5     | *unknown*               |
    | 6     | *unknown*               |
    """
    concludevote = 0x40000009 # conclude vote – params: 3: vote type, 4: 1 for succeed/0 for fail, 5: vote initiator, 6: unknown
    """Concludes the vote and shows the result

    Params that follow the command:

    | Index | Description                  |
    | ----: | ---------------------------: |
    | 3     | vote type                    |
    | 4     | 1 for success; 0 for failure |
    | 5     | vote initiator actor ID      |
    | 6     | unknown                      |
    """
    partyinvite = 0x4000000A # "you invite x to a party" – params: 3: log message id?, 4: log message param?, 5-6: unused
    """Sent when you invite someone to the party

    Params that follow the command:

    | Index | Description        |
    | ----: | -----------------: |
    | 3     | log message id?    |
    | 4     | log message param? |
    | 5-6   | unusued            |
    """
    newtoduty = 0x4000000D
    """This command comes in when one or more members in the instance are new to the duty"""
    levelup = 0x4000000E
    """This command comes in when a player levels up in the duty

    Params that follow the command:

    | Index | Description |
    | ----: | ----------: |
    | 3     | Actor ID    |
    | 4     | Old level   |
    | 5     | New level   |
    | 6     | *unused*    |
    """
    fadein = 0x40000010
    """Causes a fade-in to happen

    Params that follow the command:

    | Index | Description            |
    | ----: | ---------------------: |
    | 3     | Time left (in seconds) |
    | 4-6   | Unused                 |
    """
    barrierup = 0x40000012
    """Puts an 'instance' barrier up"""
    instancesynctime = 0x80000002
    """A periodic packet sent to indicate the remaining time in an instance

    Params that follow the command:
    | Index | Description            |
    | ----: | ---------------------: |
    | 3     | Time left (in seconds) |
    | 4-6   | Unused                 |
    """
    @classmethod
    def name_for_value(cls, value):
        """Helper class method to return the name of the enum when you already have the value"""
        if value in cls.__members__.values():
            return cls(value).name
        return 'Unknown'


class DirectorUpdate(Event):
    """Director events control the flow in different types of content

    It consists of two 'primary' parameters – the 'type' of content and the
    'command' to execute in that content. After the command, there are up to
    four additional bytes that can optionally give further information.

    The structure of a DirectorUpdate looks somewhat similar to the following:

    ```c
    struct directorUpdate {
        uint32_t category;
        uint32_t command;
        uint32_t params[4];
    }
    ```

    The upper 16 bits of category is the actual category, while the lower 16 bits
    are the instance_id.
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
