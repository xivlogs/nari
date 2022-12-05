"""
Ability
~~~~~~~

Refers to events emitted when abilities are used
"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor
from nari.types.ability import Ability as AbilityObj
from nari.types.actioneffect import ActionEffect

class Ability(Event): # pylint: disable=too-few-public-methods
    """A single target ability

    :param timestamp: Number of seconds since the unix epoch
    :type timestamp: Timestamp
    :param action_effects: `ActionEffect` entries that apply to this ability usage
    :type action_effects: list[ActionEffect]
    :param source_actor: The 'casting' actor
    :type source_actor: Actor
    :param target_actor: The target of the ability
    :type target_actor: Actor
    :param ability: The ability being used
    :type ability: AbilityObj
    :param sequence_id: The sequence id assigned to this usage
    :type sequence_id: int
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 action_effects: list[ActionEffect],
                 source_actor: Actor,
                 target_actor: Actor,
                 ability: AbilityObj,
                 sequence_id: int,
                ):
        super().__init__(timestamp)
        self.source_actor = source_actor
        self.target_actor = target_actor
        self.action_effects = action_effects
        self.ability = ability
        self.sequence_id = sequence_id

    def __repr__(self):
        return '<Ability>'

class AoeAbility(Event): # pylint: disable=too-few-public-methods
    """An ability that hits multiple actors"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 action_effects: list[ActionEffect],
                 source_actor: Actor,
                 target_actor: Actor,
                 ability: AbilityObj,
                 sequence_id: int,
                ):
        super().__init__(timestamp)
        self.source_actor = source_actor
        self.target_actor = target_actor
        self.action_effects = action_effects
        self.ability = ability
        self.sequence_id = sequence_id

    def __repr__(self):
        return '<AoEAbility>'
