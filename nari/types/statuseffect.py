"""Types revolving around status effects"""

from typing import NamedTuple

class StatusEffect(NamedTuple):
    """Container for parameters for status effects"""
    status_id: int
    status_params: bytes
    duration: float
    source_actor_id: int
