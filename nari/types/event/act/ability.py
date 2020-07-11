"""Ability represents actions performed by Actors to Actors

Anything that does an action in-game, from ninjitsu use to abilities used by bosses, should
generate one of these events.
"""
from enum import IntEnum

from nari.types.event.base import Event
from nari.types.event import Type
from nari.types.actor import Actor
from nari.types.ability import Ability as AbilityObject

class AbilityType(IntEnum):
    """AbilityEffectTypes lists all the different effects that an ability can be marked with"""
    none = 0x0
    """Ability has no special effects"""
    applieseffect = 0x0E
    """The ability applies a status effect"""


class Ability(Event):
    """Represents an ability use

    The Ability event has 43 parameters, some of which are known:

    1. The source actor ID
    2. The source actor name
    3. The ability ID
    4. The ability name
    5. The target actor ID
    6. The target actor name
    7. effect_data1 (*4 bytes of data, unknown purpose*)
    8. effect_data1, part 2 (*4 bytes of data, unknown purpose*)
    9. effect_data2

        effect_data2 has 4 bytes with different characteristics:

        | byte | description                                                                                                   |
        | :--: | :------------------------------------------------------------------------------------------------------------ |
        | 1    | Action metadata. For example, Fuma Shuriken's metadata shows which of Ten/Chi/Jin button was used to cast it. |
        | 2    | Crit chance. For example, `0xAA` turns into 17% crit chance (value / 10)                                      |
        | 3    | Low byte of true damage. If this and byte 2 are non-zero, this is likely a dot of some kind                   |
        | 4    | Action type, see AbilityType for more information                                                             |

    10. effect_data2, part 2 (*4 bytes of data, unknown purpose*)
    11. effect_data3 (*4 bytes of data, unknown purpose*)
    12. effect_data3, part 2 (*4 bytes of data, unknown purpose*)
    13. effect_data4 (*4 bytes of data, unknown purpose*)
    14. effect_data4, part 2 (*4 bytes of data, unknown purpose*)
    15. effect_data5 (*4 bytes of data, unknown purpose*)
    16. effect_data5, part 2 (*4 bytes of data, unknown purpose*)
    17. effect_data6 (*4 bytes of data, unknown purpose*)
    18. effect_data6, part 2 (*4 bytes of data, unknown purpose*)
    19. effect_data7 (*4 bytes of data, unknown purpose*)
    20. effect_data7, part 2 (*4 bytes of data, unknown purpose*)
    21. effect_data8 (*4 bytes of data, unknown purpose*)
    22. effect_data8, part 2 (*4 bytes of data, unknown purpose*)
    23. Source actor hp
    24. Source actor max hp
    25. Source actor mp
    26. Source actor max mp
    27. Source actor tp
    28. Source actor max tp
    29. Source actor x position
    30. Source actor y position
    31. Source actor z position
    32. Source actor facing
    33. Target actor hp
    34. Target actor max hp
    35. Target actor mp
    36. Target actor max mp
    37. Target actor tp
    38. Target actor max tp
    39. Target actor x position
    40. Target actor y position
    41. Target actor z position
    42. Target actor facing
    43. Global sequence – apparently seems to increment on every ability cast
    """
    __id__: int = Type.networkability.value

    def handle_params(self):
        # param[0] and param[1] - source Actor ID/name
        self.source_actor = Actor(self.params[0], self.params[1])
        # param[2] and param[3] - Ability ID/name
        self.ability = AbilityObject(self.params[2], self.params[3])
        # param[4] and param[5] - target Actor ID/name
        self.target_actor = Actor(self.params[4], self.params[5])
        # params[6] = effect_data1
        # params[7] = effect_data1, part 2
        # params[8] = effect_data2
        # effect_data2 has 4 bytes with different characteristics:
        # 1 - action metadata. For example, Fuma Shuriken's metadata shows which of Ten/Chi/Jin button was used.
        #     There's enough data here that documenting it is best left to other documentation.
        # 2 - crit chance. 0xAA turns into a ~17% crit chance (value / 10)
        # 3 - low byte of true damage. If this and byte 2 are present, this is likely a dot of some kind
        # 4 - action type. See the ActionEffectType enum above for documentation
        ability_info: int = int(self.params[8], 16)
        self.action_effect = ability_info & 0xFF
        self.damage_low_byte = (ability_info >> 8) & 0xFF
        self.crit_low_byte = (ability_info >> 16) & 0xFF
        self.action_metadata = (ability_info >> 24) & 0xFF
        # params[9] = effect_data2, part 2
        # params[10] = effect_data3
        # params[11] = effect_data3, part 2
        # params[12] = effect_data4
        # params[13] = effect_data4, part 2
        # params[14] = effect_data5
        # params[15] = effect_data5, part 2
        # params[16] = effect_data6
        # params[17] = effect_data6, part 2
        # params[18] = effect_data7
        # params[19] = effect_data7, part 2
        # params[20] = effect_data8
        # params[21] = effect_data8, part 2
        #
        # source actor parameters
        # params[22] = current hp
        # params[23] = max hp
        # params[24] = current mp
        # params[25] = max mp
        # params[26] = current tp
        # params[27] = max tp
        # params[28] = x position
        # params[29] = y position
        # params[30] = z position
        # params[31] = facing in radians (facing east is 0)

        # sometimes these values are blank... why not provide 0s tho?
        if '' not in self.params[22:31]:
            self.source_actor.resources.update(*map(int, self.params[22:28]))
            self.source_actor.resources.update(*map(float, self.params[28:31]))

        # target actor parameters
        # params[32] = current hp
        # params[33] = max hp
        # params[34] = current mp
        # params[35] = max mp
        # params[36] = current tp
        # params[37] = max tp
        # params[38] = x position
        # params[39] = y position
        # params[40] = z position
        # params[41] = facing in radians (facing east is 0)
        if '' not in self.params[32:41]:
            self.target_actor.resources.update(*map(int, self.params[32:38]))
            self.target_actor.position.update(*map(float, self.params[38:41]))

        # params[42] = global sequence

    def __repr__(self):
        return f'<Ability ({self.ability.name})>'
