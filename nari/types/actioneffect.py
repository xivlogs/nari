"""Stores data about ActionEffects"""

from enum import IntEnum, IntFlag
from typing import List

class EffectType(IntEnum):
    """The different effect types an ability can have"""
    Nothing = 0
    Miss = 1
    FullResist = 2
    Damage = 3
    Heal = 4
    BlockedDamage = 5
    ParriedDamage = 6
    Invulnerable = 7
    NoEffectText = 8
    Unknown_0 = 9
    MpLoss = 10
    MpGain = 11
    TpLoss = 12
    TpGain = 13
    GpGain = 14
    ApplyStatusEffectTarget = 15
    ApplyStatusEffectSource = 16 # effect entry on target but buff applies to source, like storm's eye
    StatusNoEffect = 20
    StartActionCombo = 27
    ComboSucceed = 28
    Knockback = 33
    Mount = 40
    VFX = 59 # links to VFX sheet


class EffectResultFlag(IntFlag):
    """Extra bitwise flags that modify the ability"""
    NoEffect = 0x0
    Absorbed = 0x04
    ExtendedValue = 0x40
    EffectOnSource = 0x80
    Reflected = 0xA0


class HitSeverity(IntFlag):
    """Determines how hard the ability 'hit'"""
    NormalDamage = 0
    NormalHeal = 0
    CritDamage = 1
    CritHeal = 1
    DirectHitDamage = 2
    CritDirectHitDamage = 3


class ActionEffect(): # pylint: disable=too-few-public-methods
    """Properties that modify an ability use"""
    def __init__(self, *,
                 effect_type: EffectType, # IntEnum type in python
                 flags: int,
                 value: int,
                 extended_value_high_bytes: int,
                 additional_params: List[int]):
        self.effect_type = effect_type
        self.flags = flags
        self.value = value
        self.extended_value_high_bytes = extended_value_high_bytes
        self.additional_params = additional_params
