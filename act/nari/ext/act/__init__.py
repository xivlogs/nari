"""Classes and functions for handling network logs from ACT"""
from typing import Optional

from nari.io.reader import Reader
from nari.types.event import Event
from nari.types.event.version import SemanticVersion, Version
from nari.util.exceptions import EventNotFound

from nari.ext.act.parser import ID_MAPPINGS, ActEventType, ActLogChecksumType, date_from_act_timestamp, validate_checksum
from nari.ext.act.exceptions import InvalidActChecksum

# The last version of ACT to use MD5 checksums
# We default to SHA256, but if the version is <= 2.2.1.6 we switch to MD5
LAST_MD5_VERSION = SemanticVersion(2,2,1,6)


class ActLogReader(Reader):
    """Implementation of the Reader class for parsing ACT network logs"""
    def __init__(self, actlog_path, *, raise_on_checksum_failure=False, raise_on_invalid_id=False):
        # might need a helper function, but eh.
        self.handle = open(actlog_path, 'r', encoding='utf-8') # pylint: disable=consider-using-with
        self.index = 1
        self.raise_on_checksum_failure = raise_on_checksum_failure
        self.raise_on_invalid_id = raise_on_invalid_id
        self.algo = ActLogChecksumType.SHA256

    def __del__(self):
        """Handles closing the file when the object undergoes garbage collection"""
        self.handle.close()

    def handle_line(self, line: str) -> Optional[Event]:
        """Handles an ACT-specific line"""
        args = line.strip().split('|')
        id_ = int(args[0])

        if self.raise_on_invalid_id and id_ not in ID_MAPPINGS:
            raise EventNotFound(f"ACT id: {id_}")

        datestr = args[1]
        timestamp = date_from_act_timestamp(datestr)

        if self.raise_on_checksum_failure:
            if id_ in (ActEventType.memoryzonechange, ActEventType.version):
                self.index = 1

            if id_ == ActEventType.version:
                version_event = ID_MAPPINGS[id_](timestamp, args[2:-1])
                if isinstance(version_event, Version) and version_event.version <= LAST_MD5_VERSION:
                    self.algo = ActLogChecksumType.MD5

            if validate_checksum(line.strip(), self.index, self.algo) is False:
                raise InvalidActChecksum(f'Invalid checksum for line {line.strip()} with algo {self.algo} and index {self.index})')

            self.index += 1

        event: Optional[Event] = None

        if id_ in ID_MAPPINGS:
            event = ID_MAPPINGS[id_](timestamp, args[2:-1])
        else:
            event = Event(timestamp)

        return event

    def read_next(self) -> Optional[Event]:
        """Returns an array of all the ACT log events from the file"""
        # keep reading until we get a non-None response from handle_line
        while True:
            line: str = self.handle.readline()
            if len(line) == 0:
                return None
            if (event := self.handle_line(line)) is not None:
                return event
