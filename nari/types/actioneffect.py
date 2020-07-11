"""Stores data about ActionEffects"""

from enum import IntEnum, IntFlag

# POTENTIALLY OUTDATED INFORMATION:
# Type 1 - Dodge/Miss.
# Type 2 - Fully resisted.
# Type 3 - Normal damage, P4 is damage
#   - P1 is a bitfield. 0 is normal, 1 is crit hit, 2 is direct hit, 3 is both.
# Type 4 - HP recover message (P1: 1, P4: HP recovered)
# Type 5 - Blocked damage. P3 is blocked percentage. P4 is damage.
# Type 6 - Parried damage. P3 is blocked percentage. P4 is damage.
# Type 7 - Invulnerable
# Type 8 - Has no effect.
# Type 9 - Bane spreading DoTs
# Type 10 - You lose MP (P4: MP lost).
# Type 11 - MP recover message (P4: MP recovered).
# Type 12 - You lose TP (P4: TP lost).
# Type 13 - TP recover message (P4: TP recovered).
# Type 14 - GP recover message (P4: TP recovered)
# Type 15(or 16) - Inflicted status effect
#   - P1 is base damage
#   - P2 is crit % * 10. For damage debuff, it indicates percent modifier.
#   - P4 is status ID
# Type 17-19 - Recovered from the effect of P4 status ID
# Type 21 - Status P4 has no effect.
# Type 25-26 - Enmity increases message
# Type 28 - Used Skill ID, P4 is skill ID
# Type 38 - Mounting a chocobo/mount.
# Type 46 - Suffer bad breath statuses (poison, blind, slow, heavy, damage down)
# Type 48 - Mounting a turret.
# Type 51 - Fully resist status P4
# Type 53 - Sentenced to death message.
# Type 55 - Lost the effect of sheltron. Recovered P4 MP.
# Type 57 - Player teleport.
# Type 58 - ??
# Type 61 - Reflected! You cast back the attack.
class EffectType(IntEnum):
    """The different effect types an ability can have"""
    Dodge = 0x1
    Resisted = 0x2
    NormalDamage = 0x3
    HPRecover = 0x4
    Blocked = 0x5
    Parried = 0x6
    Invulnerable = 0x7
    NoEffect = 0x8
    BaneSpread = 0x9
    LoseMP = 0xa
    RecoverMP = 0xb
    LoseTP = 0xc
    GainTP = 0xd
    GainGP = 0xe
    InflictStatus = 0xf


class EffectFlag(IntFlag):
    """Extra bitwise flags that modify the ability"""
    ExtraDamage = 0x40


class ActionEffect(): # pylint: disable=too-few-public-methods
    """Properties that modify an ability use"""
    def __init__(self, *,
                 effect_type: EffectType,
                 hit_severity: int,
                 padding: int,
                 percentage: int,
                 multiplier: int,
                 damage: int):
        self.effect_type = effect_type
        self.hit_severity = hit_severity
        self.padding = padding
        self.percentage = percentage
        self.multiplier = multiplier
        self.damage = damage
