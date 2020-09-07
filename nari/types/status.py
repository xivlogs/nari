"""Status related container"""

from typing import NamedTuple

class Status(NamedTuple):
    status_id: int
    status_name: str = ''