"""Represents 'cast' or ability usage events"""
from enum import IntEnum

from nari.types.event.base import Event
from nari.types.event import Type
from nari.types.actor import Actor
from nari.types.ability import Ability as AbilityType

class ActionEffectType(IntEnum):
    """Blah, need some docs"""
    applieseffect = 0x0e
    """The action applies a status effect"""


class Ability(Event):
    """A 'cast' event"""
    __id__: int = Type.networkability.value

    def handle_params(self):
        self.source_actor = Actor(self.params[0], self.params[1])
        self.ability = AbilityType(self.params[2], self.params[3])
        self.target_actor = Actor(self.params[4], self.params[5])
        # params[6] = ???
        # params[7] = ???
        # params[8] is upwards of 4 bytes
        # for example, 00AA220E breaks into AA (170, crit chance), 22 (34, low byte of true damage), and 0E (14, ???)
        # If the second and third are missing, then it's because it's not a dot/hot. The first byte is special metadata
        # about the action, and likely beyond the scope of this parser for now
        ability_info: int = int(self.params[8], 16)
        self.action_effect = ability_info & 0xFF
        self.damage_low_byte = (ability_info >> 8) & 0xFF
        self.crit_low_byte = (ability_info >> 16) & 0x0FF
        self.action_metadata = (ability_info >> 24) & 0xFF

    def __repr__(self):
        return f'<Ability ({self.ability.name})>'
