""""Parses partylist events from act log line"""
from typing import Optional

from nari.types import Timestamp
from nari.types.event import Event
from nari.types.event.party import PartyList


def partylist_from_logline(timestamp: Timestamp, params: list[str]) -> Optional[Event]:
    """Parses a PartyList event from an act log line

    ACT Event ID (decimal): 11

    ## Param layout from act

    The first two params in every event is the act event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Number of actor IDs|
    |1    |int|Zero or more actor IDs for the party. First entry is always your actor; subsequent actors are those of your party (up to the amount listed in param 0). Any further actors are actors that are a part of your alliance.|
    """
    amount = int(params[0])
    if amount == 0:
        return None

    # amount is > 1; grab local party first
    ids = [int(i, 16) for i in params[1:amount+1]]
    other_ids = [int(i, 16) for i in params[amount+1:]]
    return PartyList(timestamp=timestamp, ids=ids, other_ids=other_ids)
