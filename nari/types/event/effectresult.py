"""
EffectResult
~~~~~~~~~~~~

Encapsulates classes that show the result of an action being confirmed by the server
"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor

class EffectResultEntry(): # pylint: disable=too-few-public-methods
    """Represents a single effect result

    :param effect_index: TODO:
    :type effect_index: int
    :param effect_id: TODO:
    :type effect_id: int
    :param effect_duration: The length of the effect in seconds
    :type effect_duration: float
    :param source_actor_id: The source actor who generated the effect
    :type source_actor_id: int
    """
    def __init__(self, *,
                 effect_index: int,
                 effect_id: int,
                 effect_duration: float,
                 source_actor_id: int,
                ):
        self.effect_index = effect_index
        self.effect_id = effect_id
        self.effect_duration = effect_duration
        self.source_actor_id = source_actor_id

    def __repr__(self):
        return '<EventResultEntry>'


class EffectResult(Event): # pylint: disable=too-few-public-methods
    """Represents a list of effect results

    :param timestamp: Timestamp of event
    :type timestamp: Timestamp
    :param target_actor: The target of the `effect_results` list
    :type target_actor: Actor
    :param sequence_id: The sequence id that links an action to their final effects - for every `Ability` use, there should be a corresponding `EffectResult`
    :type sequence_id: int
    :param shield_percent: The percentage of the actor's health which is a shield
    :type shield_percent: int
    :param effect_results: A list of singular EffectResults
    :type effect_results: list[EffectResultEntry]
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 target_actor: Actor,
                 sequence_id: int,
                 shield_percent: int,
                 effect_results: list[EffectResultEntry],
                ):
        super().__init__(timestamp)
        self.target_actor = target_actor
        self.sequence_id = sequence_id
        self.shield_percent = shield_percent
        self.effect_results = effect_results

    def __repr__(self):
        return '<EffectResult>'
