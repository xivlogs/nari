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

from nari.types.event.version import Version
from nari.types.event.config import Config
from nari.types.event.debug import Debug
from nari.types.event.hook import Hook
from nari.types.event.gauge import Gauge
from nari.types.event.zonechange import ZoneChange
from nari.types.event.changeplayer import ChangePlayer
from nari.types.event.addcombatant import AddCombatant
from nari.types.event.playerstats import PlayerStats
from nari.types.event.logline import LogLine
from nari.types.event.removecombatant import RemoveCombatant
from nari.types.event.networkstatuseffect import NetworkStatusEffect
from nari.types.event.networkbuff import NetworkBuff
from nari.types.event.networkupdatehp import NetworkUpdateHP
from nari.types.event.networkbuffremove import NetworkBuffRemove
from nari.types.event.networkbegincast import NetworkBeginCast
from nari.types.event.ability import Ability
from nari.types.event.networknametoggle import NameToggle
from nari.types.event.limitbreak import LimitBreak
from nari.types.event.directorupdate import DirectorUpdate
from nari.types.event.partylist import PartyList
from nari.types.event.networkeffectresult import NetworkEffectResult
from nari.types.event.networktargetmarker import NetworkTargetMarker
from nari.types.event.aoeability import AoeAbility
from nari.types.event.networkdot import NetworkDot
from nari.types.event.networktether import NetworkTether
from nari.types.event.networktargetheadmarker import NetworkTargetHeadMarker
from nari.types.event.networkcancelability import CancelAbility
from nari.types.event.networkdeath import Death

IdEventMapping = {
    Type.version.value: Version,
    Type.config.value: Config,
    Type.debug.value: Debug,
    Type.hook.value: Hook,
    Type.gauge.value: Gauge,
    Type.zonechange.value: ZoneChange,
    Type.changeplayer.value: ChangePlayer,
    Type.addcombatant.value: AddCombatant,
    Type.playerstats.value: PlayerStats,
    Type.logline.value: LogLine,
    Type.removecombatant.value: RemoveCombatant,
    Type.networkstatuseffect.value: NetworkStatusEffect,
    Type.networkbuff.value: NetworkBuff,
    Type.networkupdatehp.value: NetworkUpdateHP,
    Type.networkbuffremove.value: NetworkBuffRemove,
    Type.networkbegincast.value: NetworkBeginCast,
    Type.networkability.value: Ability,
    Type.networknametoggle.value: NameToggle,
    Type.limitbreak.value: LimitBreak,
    Type.directorupdate.value: DirectorUpdate,
    Type.partylist.value: PartyList,
    Type.networkeffectresult.value: NetworkEffectResult,
    Type.networktargetmarker.value: NetworkTargetMarker,
    Type.networkaoeability.value: AoeAbility,
    Type.networkdot.value: NetworkDot,
    Type.networktether.value: NetworkTether,
    Type.networktargetheadmarker.value: NetworkTargetHeadMarker,
    Type.networkcancelability.value: CancelAbility,
    Type.networkdeath: Death,
}