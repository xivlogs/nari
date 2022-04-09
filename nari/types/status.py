"""Types revolving around status effects"""

from typing import NamedTuple


class Status(NamedTuple):
    """Container for a status id with a name. Only really useful in ACT logs"""
    status_id: int
    status_name: str = ''


class StatusEffect(NamedTuple):
    """Container for status effects parameters"""
    status_id: int
    status_params: bytes
    duration: float
    source_actor_id: int
