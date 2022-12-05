"""
Party
~~~~~
"""
from nari.types import Timestamp
from nari.types.event import Event


class PartyList(Event): # pylint: disable=too-few-public-methods
    """Represents changes to the party list

    :param timestamp: The timestamp of the event
    :type timestamp: Timestamp
    :param ids: The actor IDs for the actors in your party
    :type ids: list[int]
    :param other_ids: Actor IDs for actors in your alliance, defaults to []
    :type other_ids: list[int], optional
    """
    def __init__(self, *, # pylint: disable=dangerous-default-value
                 timestamp: Timestamp,
                 ids: list[int],
                 other_ids: list[int] = [],
                ):
        super().__init__(timestamp)
        self.ids = ids
        self.other_ids = other_ids

    def __repr__(self):
        return f'<PartyList f{len(self.ids)} (other: {len(self.other_ids)})>'
