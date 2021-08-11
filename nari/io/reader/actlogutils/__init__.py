"""Just a bunch of helper methods to spit out events from the act log"""
from datetime import datetime
from typing import Callable, Dict, List, Optional
from enum import IntEnum

from nari.types.event import Event
from nari.types.event.limitbreak import LimitBreak
# here we go
from nari.io.reader.actlogutils.metadata import version_from_logline, config_from_logline
from nari.io.reader.actlogutils.zone import zonechange_from_logline
from nari.io.reader.actlogutils.status import statuslist_from_logline, statusapply_from_logline
from nari.io.reader.actlogutils.limitbreak import limitbreak_from_logline
from nari.io.reader.actlogutils.ability import ability_from_logline, aoeability_from_logline
from nari.io.reader.actlogutils.directorupdate import director_events_from_logline
from nari.io.reader.actlogutils.updatehp import updatehp_from_logline
from nari.io.reader.actlogutils.actorspawn import actor_spawn_from_logline
from nari.io.reader.actlogutils.gauge import gauge_from_logline
from nari.io.reader.actlogutils.playerstats import playerstats_from_logline
from nari.io.reader.actlogutils.visibility import visibility_from_logline
from nari.io.reader.actlogutils.party import partylist_from_logline

DEFAULT_DATE_FORMAT: str = '%Y-%m-%dT%H:%M:%S.%f%z'
ActEventFn = Callable[[datetime, List[str]], Optional[Event]]

# pylint: disable=invalid-name
class ActEventType(IntEnum):
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
# pylint: enable=invalid-name

def date_from_act_timestamp(datestr: str) -> datetime:
    """Parse timestamp from act log into a python datetime object
    Look, this is dirty. This is wrong. Please someone find a better way to do this.
    """
    return datetime.strptime(f'{datestr[:26]}{datestr[-6:]}', DEFAULT_DATE_FORMAT)

# pylint: disable=unused-argument
def noop(timestamp: datetime, params: List[str]) -> Event:
    """Straight-up ignores things"""
    # print(f'Ignoring an event with timestamp {timestamp} and params: {"|".join(params)}')

ID_MAPPINGS: Dict[int, ActEventFn] = {
    ActEventType.version: version_from_logline,
    ActEventType.zonechange: zonechange_from_logline,
    ActEventType.changeplayer: noop,
    ActEventType.config: config_from_logline,
    ActEventType.debug: noop,
    ActEventType.hook: noop,
    ActEventType.addcombatant: actor_spawn_from_logline,
    ActEventType.playerstats: playerstats_from_logline,
    ActEventType.logline: noop,
    ActEventType.gauge: gauge_from_logline,
    ActEventType.networkstatuseffect: statuslist_from_logline,
    ActEventType.networkbuff: statusapply_from_logline,
    ActEventType.limitbreak: limitbreak_from_logline,
    ActEventType.partylist: partylist_from_logline,
    ActEventType.networknametoggle: visibility_from_logline,
    ActEventType.networkupdatehp: updatehp_from_logline,
    ActEventType.directorupdate: director_events_from_logline,
    ActEventType.networkability: ability_from_logline,
    ActEventType.networkeffectresult: noop, # TODO
}
