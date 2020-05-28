from nari.types.event import Type

from nari.parser.event.version import Version
from nari.parser.event.config import Config
from nari.parser.event.debug import Debug
from nari.parser.event.hook import Hook
from nari.parser.event.gauge import Gauge
from nari.parser.event.zonechange import ZoneChange
from nari.parser.event.changeplayer import ChangePlayer
from nari.parser.event.addcombatant import AddCombatant
from nari.parser.event.playerstats import PlayerStats
from nari.parser.event.logline import LogLine
from nari.parser.event.removecombatant import RemoveCombatant
from nari.parser.event.networkstatuseffect import NetworkStatusEffect
from nari.parser.event.networkbuff import NetworkBuff
from nari.parser.event.networkupdatehp import NetworkUpdateHP
from nari.parser.event.networkbuffremove import NetworkBuffRemove
from nari.parser.event.networkbegincast import NetworkBeginCast
from nari.parser.event.ability import Ability
from nari.parser.event.networknametoggle import NameToggle
from nari.parser.event.limitbreak import LimitBreak
from nari.parser.event.actorcontrol import ActorControl
from nari.parser.event.partylist import PartyList
from nari.parser.event.networkeffectresult import NetworkEffectResult
from nari.parser.event.networktargetmarker import NetworkTargetMarker
from nari.parser.event.aoeability import AoeAbility
from nari.parser.event.networkdot import NetworkDot
from nari.parser.event.networktether import NetworkTether
from nari.parser.event.networktargetheadmarker import NetworkTargetHeadMarker
from nari.parser.event.networkcancelability import CancelAbility
from nari.parser.event.networkdeath import Death

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
    Type.actorcontrol.value: ActorControl,
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