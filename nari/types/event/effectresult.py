"""Class that represents blahblahblah"""
from typing import List

from nari.types import Timestamp
from nari.types.event import Event
from nari.types.actor import Actor

class EffectResultEntry(): # pylint: disable=too-few-public-methods
    """Specific effect result data"""
    def __init__(self, *,
                 effect_index: int,
                 effect_id: int,
                 effect_duration: float,
                 source_actor_id: int):
        self.effect_index = effect_index
        self.effect_id = effect_id
        self.effect_duration = effect_duration
        self.source_actor_id = source_actor_id


class EffectResult(Event): # pylint: disable=too-few-public-methods
    """Represents"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 target_actor: Actor,
                 sequence_id: int,
                 shield_percent: int,
                 effect_results: List[EffectResultEntry]
                ):
        super().__init__(timestamp)
        self.target_actor = target_actor
        self.sequence_id = sequence_id
        self.shield_percent = shield_percent
        self.effect_results = effect_results

    def __repr__(self):
        return '<EffectResult>'
