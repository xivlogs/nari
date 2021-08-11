""""Parses partylist events from act log line"""
from datetime import datetime
from typing import List

from nari.types.event import Event
from nari.types.event.party import PartyList


def partylist_from_logline(timestamp: datetime, params: List[str]) -> Event:
    """Parses a partylist event out from act log line"""
    # Param layout from ACT
    # 0 - number of actor IDs
    # 1 - 0 or more actor IDs for the party. First entry is always your actor;
    #     subsequent actors are those of your party (up to the amount listed 
    #     in param 0). Any further actors are actors that are a part of your
    #     alliance
    amount = int(params[0])
    if amount == 0:
        return # TODO: perhaps send a 'PartyDisband' event?

    # amount is > 1; grab local party first
    ids = [int(i, 16) for i in params[1:amount+1]]
    other_ids = [int(i, 16) for i in params[amount+1:]]
    return PartyList(timestamp=timestamp, ids=ids, other_ids=other_ids)
