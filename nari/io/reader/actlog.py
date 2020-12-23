"""Classes and functions for handling network logs from ACT"""
from typing import Optional

from nari.io.reader import Reader
from nari.io.reader.actlogutils import ID_MAPPINGS, date_from_act_timestamp
# from nari.types.event.act import Type as EventType
# from nari.types.event.mappings import IdEventMapping
from nari.types.event import Event
from nari.util.exceptions import EventNotFound

class ActLogReader(Reader):
    """Implementation of the Reader class for parsing ACT network logs"""
    def __init__(self, actlog_path, *, raise_on_checksum_failure=False, raise_on_invalid_id=False):
        # might need a helper function, but eh. Also TODO: close file at some point to be nice
        self.handle = open(actlog_path, 'r')
        # Let's talk about this. ACT network logs seem to use two different indexes – one for
        # network events, and one for other types of events. Without breaking the code too badly,
        # might be good to identify if an ID is based off network or 'other' (memory events only?)
        # and cycle through the correct indexes
        self.index = 1
        self.raise_on_checksum_failure = raise_on_checksum_failure
        self.raise_on_invalid_id = raise_on_invalid_id

    def handle_line(self, line: str) -> Event:
        """Handles an act-specific line"""
        args = line.strip().split('|')
        id_ = int(args[0])
        datestr = args[1]
        timestamp = date_from_act_timestamp(datestr)

        event: Optional[Event] = None

        if id_ in ID_MAPPINGS:
            # if id_ in [EventType.config.value]:
            #     # special handling - this one doesn't have a checksum
            #     event = IdEventMapping[id_](datestr, params=args[2:])
            # else:
            event = ID_MAPPINGS[id_](timestamp, params=args[2:-1])
            # if self.raise_on_checksum_failure and not event.valid_checksum():
            #     raise InvalidChecksum(f'Checksum is invalid for event: {line} (index {self.index})')
        elif self.raise_on_invalid_id:
            raise EventNotFound(f'No event found for id {id_}')
        else:
            event = Event(timestamp)

        self.index += 1
        return event


    def read_next(self) -> Optional[Event]:
        """Returns an array of all the act log events from the file"""
        # keep reading until we get a non-None response from handle_line
        while True:
            line: str = self.handle.readline()
            if len(line) == 0:
                return None
            event = self.handle_line(line)
            if event is not None:
                return self.handle_line(line)
