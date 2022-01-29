"""Classes and functions for handling network logs from ACT"""
from typing import Optional

from nari.io.reader import Reader
from nari.io.reader.actlogutils import ID_MAPPINGS, ActEventType, date_from_act_timestamp, validate_checksum
from nari.types.event import Event
from nari.util.exceptions import EventNotFound


class InvalidActChecksum(Exception):
    """Raised when a checksum is invalid"""


class ActLogReader(Reader):
    """Implementation of the Reader class for parsing ACT network logs"""
    def __init__(self, actlog_path, *, raise_on_checksum_failure=False, raise_on_invalid_id=False):
        # might need a helper function, but eh.
        self.handle = open(actlog_path, 'r')
        self.index = 1
        self.raise_on_checksum_failure = raise_on_checksum_failure
        self.raise_on_invalid_id = raise_on_invalid_id

    def __del__(self):
        """Handles closing the file when the object undergoes garbage collection"""
        self.handle.close()

    def handle_line(self, line: str) -> Optional[Event]:
        """Handles an act-specific line"""
        args = line.strip().split('|')
        id_ = int(args[0])

        if self.raise_on_invalid_id and id_ not in ID_MAPPINGS:
            raise EventNotFound(f"ACT id: {id_}")

        if self.raise_on_checksum_failure:
            if id_ in (ActEventType.zonechange, ActEventType.version):
                self.index = 1

            if validate_checksum(line.strip(), self.index) is False:
                raise InvalidActChecksum(f'Invalid checksum for line {line.strip()} with index {self.index})')

            self.index += 1

        datestr = args[1]
        timestamp = date_from_act_timestamp(datestr)

        event: Optional[Event] = None

        if id_ in ID_MAPPINGS:
            event = ID_MAPPINGS[id_](timestamp, args[2:-1])
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
