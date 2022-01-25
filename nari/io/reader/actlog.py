"""Classes and functions for handling network logs from ACT"""
from typing import Optional

from nari.io.reader import Reader
from nari.io.reader.actlogutils import ID_MAPPINGS, date_from_act_timestamp
from nari.types.event import Event
from nari.util.exceptions import EventNotFound

class ActLogReader(Reader):
    """Implementation of the Reader class for parsing ACT network logs"""
    def __init__(self, actlog_path, *, raise_on_checksum_failure=False, raise_on_invalid_id=False):
        # might need a helper function, but eh.
        self.handle = open(actlog_path, 'r')
        # Let's talk about this. ACT network logs seem to use two different indexes – one for
        # network events, and one for other types of events. Without breaking the code too badly,
        # might be good to identify if an ID is based off network or 'other' (memory events only?)
        # and cycle through the correct indexes
        self.network_index = 1
        self.memory_index = 1
        self.raise_on_checksum_failure = raise_on_checksum_failure
        self.raise_on_invalid_id = raise_on_invalid_id

    def __del__(self):
        """Handles closing the file when the object undergoes garbage collection"""
        self.handle.close()

    def handle_line(self, line: str) -> Event:
        """Handles an act-specific line"""
        args = line.strip().split('|')
        id_ = int(args[0])
        # TODO: increment network_index or memory_index here, so we can do a checksum check here
        datestr = args[1]
        timestamp = date_from_act_timestamp(datestr)

        event: Optional[Event] = None

        if id_ in ID_MAPPINGS:
            event = ID_MAPPINGS[id_](timestamp, params=args[2:-1])
        elif self.raise_on_invalid_id:
            raise EventNotFound(f'No event found for id {id_}')
        else:
            event = Event(timestamp)

        return event


    def read_next(self) -> Optional[Event]:
        """Returns an array of all the act log events from the file"""
        # keep reading until we get a non-None response from handle_line
        while True:
            line: str = self.handle.readline()
            if len(line) == 0:
                return None
            if (event := self.handle_line(line)) is not None:
                return event
