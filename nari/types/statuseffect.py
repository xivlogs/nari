from typing import NamedTuple, List

class StatusEffect(NamedTuple):
    status_id: int
    status_params: bytes
    duration: float
    source_actor_id: int