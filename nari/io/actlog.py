from typing import List

from nari.io.reader import Reader
from nari.types.event import IdEventMapping, Type as EventType
from nari.types.event.base import Event
from nari.util.exceptions import InvalidChecksum, EventNotFound

class ActLogReader(Reader):
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
        id = int(args[0])
        datestr = args[1]

        event = None

        if id in IdEventMapping:
            if id in [EventType.config.value]:
                # special handling - this one doesn't have a checksum
                event = IdEventMapping[id](datestr, args[2:])
            else:
                event = IdEventMapping[id](datestr, args[2:-1], index=self.index, checksum=args[-1])
            if self.raise_on_checksum_failure and not event.valid_checksum():
                raise InvalidChecksum(f'Checksum is invalid for event: {line} (index {self.index})')
        elif self.raise_on_invalid_id:
            raise EventNotFound(f'No event found for id {id}')
        else:
            event = Event(datestr, args[2:-1], index=self.index, checksum=args[-1], id=id)

        self.index += 1
        return event
        

    def read(self) -> List[Event]:
        """Returns an array of all the act log events from the file"""
        for line in self.handle:
            yield self.handle_line(line)
        # return [self.handle_line(line) for line in self.handle]