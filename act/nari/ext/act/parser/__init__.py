"""Just a bunch of helper methods to spit out events from the ACT log"""
from enum import IntEnum

from nari.types.event import Event
from nari.types import Timestamp

from nari.ext.act.parser.metadata import version_from_logline, config_from_logline
from nari.ext.act.parser.zone import zonechange_from_logline
from nari.ext.act.parser.status import statuslist_from_logline, statuslist3_from_logline, statusapply_from_logline
from nari.ext.act.parser.limitbreak import limitbreak_from_logline
from nari.ext.act.parser.ability import ability_from_logline, aoeability_from_logline
from nari.ext.act.parser.tick import tick_from_logline
from nari.ext.act.parser.directorupdate import director_events_from_logline
from nari.ext.act.parser.updatehpmp import updatehpmp_from_logline
from nari.ext.act.parser.actorspawn import actor_spawn_from_logline
from nari.ext.act.parser.gauge import gauge_from_logline
from nari.ext.act.parser.playerstats import playerstats_from_logline
from nari.ext.act.parser.visibility import visibility_from_logline
from nari.ext.act.parser.targeticon import targeticon_from_logline
from nari.ext.act.parser.targetmarker import targetmarker_from_logline
from nari.ext.act.parser.tether import tether_from_logline
from nari.ext.act.parser.waymark import waymark_from_logline
from nari.ext.act.parser.party import partylist_from_logline
from nari.ext.act.parser.effectresult import effectresult_from_logline
from nari.ext.act.parser.cast import startcast_from_logline, stopcast_from_logline
from nari.ext.act.types import ActIdMapping


# pylint: disable=invalid-name
class ActEventType(IntEnum):
    """List of Event types from the ACT network log"""
    memorychatlog = 0
    memoryzonechange = 1
    memorychangeprimaryplayer = 2
    memoryaddcombatant = 3
    memoryremovecombatant = 4
    memorypartylist = 11
    memoryplayerstats = 12
    networkstartscasting = 20
    networkability = 21
    networkaoeability = 22
    networkcancelability = 23
    networkdothot = 24
    networkdeath = 25
    networkstatusadd = 26
    networktargeticon = 27
    networkwaymarkmarker = 28
    networksignmarker = 29
    networkstatusremove = 30
    networkgauge = 31
    unusedworld = 32
    networkdirector = 33
    networknametoggle = 34
    networktether = 35
    networklimitbreak = 36
    networkeffectresult = 37
    networkstatuslist = 38
    networkupdatehpmp = 39
    memorychangemap = 40
    memorysystemlogmessage = 41
    networkstatuslist3 = 42
    config = 249
    hook = 250
    debug = 251
    packetdump = 252
    version = 253
    error = 254

    @classmethod
    def has_id(cls, id_: int) -> bool:
        """Returns True if the id is in the enum"""
        return id_ in cls.__members__.values()

    @classmethod
    def has_type(cls, name: str) -> bool:
        """Returns True if the name is in the enum"""
        return name in cls.__members__.keys() # pylint: disable=consider-iterating-dictionary
# pylint: enable=invalid-name

# pylint: disable=unused-argument
def noop(timestamp: Timestamp, params: list[str]) -> Event:
    """Straight-up ignores things"""
    # print(f'Ignoring an event with timestamp {timestamp} and params: {"|".join(params)}')

ID_MAPPINGS: ActIdMapping = {
    # Internal events
    ActEventType.config: config_from_logline,
    ActEventType.debug: noop,
    ActEventType.error: noop,
    ActEventType.hook: noop,
    ActEventType.packetdump: noop,
    ActEventType.version: version_from_logline,
    # Memory events
    ActEventType.memorychatlog: noop,
    ActEventType.memoryzonechange: zonechange_from_logline,
    ActEventType.memorychangemap: noop,
    ActEventType.memorychangeprimaryplayer: noop,
    ActEventType.memoryaddcombatant: actor_spawn_from_logline,
    ActEventType.memoryremovecombatant: noop,
    ActEventType.memorysystemlogmessage: noop,
    ActEventType.memoryplayerstats: playerstats_from_logline,
    ActEventType.memorypartylist: partylist_from_logline,
    # Network events
    ActEventType.networkgauge: gauge_from_logline,
    ActEventType.networkdeath: noop,
    ActEventType.networknametoggle: visibility_from_logline,
    ActEventType.networkupdatehpmp: updatehpmp_from_logline,
    ActEventType.networkdirector: director_events_from_logline,
    ActEventType.networkstartscasting: startcast_from_logline,
    ActEventType.networkcancelability: stopcast_from_logline,
    ActEventType.networkability: ability_from_logline,
    ActEventType.networkaoeability: aoeability_from_logline,
    ActEventType.networkeffectresult: effectresult_from_logline,
    ActEventType.networkstatuslist: statuslist_from_logline,
    ActEventType.networkstatuslist3: statuslist3_from_logline,
    ActEventType.networkstatusadd: statusapply_from_logline,
    ActEventType.networkstatusremove: noop,
    ActEventType.networkdothot: tick_from_logline,
    ActEventType.networklimitbreak: limitbreak_from_logline,
    ActEventType.networksignmarker: targetmarker_from_logline,
    ActEventType.networktargeticon: targeticon_from_logline,
    ActEventType.networkwaymarkmarker: waymark_from_logline,
    ActEventType.networktether: tether_from_logline,
    # Defined by ACT but unused events
    ActEventType.unusedworld: noop,
}
