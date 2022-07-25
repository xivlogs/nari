"""Types for ACT"""

from typing import Callable, Optional

from nari.types import Timestamp
from nari.types.event import Event


ActEventFn = Callable[[Timestamp, list[str]], Optional[Event]]
ActIdMapping = dict[int, ActEventFn]
