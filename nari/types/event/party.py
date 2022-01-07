"""Classes that represent changes to your parties"""
from datetime import datetime
from typing import List

from nari.types.event import Event


class PartyList(Event): # pylint: disable=too-few-public-methods
    """Represents changes to the party list"""
    def __init__(self, *, # pylint: disable=dangerous-default-value
                 timestamp: datetime,
                 ids: List[int],
                 other_ids: List[int] = [],
                ):
        super().__init__(timestamp)
        self.ids = ids
        self.other_ids = other_ids

    def __repr__(self):
        return f'<PartyList f{len(self.ids)} (other: {len(self.other_ids)})>'