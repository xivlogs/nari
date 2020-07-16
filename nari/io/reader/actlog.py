"""Classes and functions for handling network logs from ACT"""
from typing import Optional

from nari.io.reader import Reader
import nari.io.reader.actlogutils as actutils
# from nari.types.event.act import Type as EventType
# from nari.types.event.mappings import IdEventMapping
from nari.types.event import Event
# from nari.util.exceptions import InvalidChecksum, EventNotFound

# class ActLogReader(Reader):
#     """Implementation of the Reader class for parsing ACT network logs"""
#     def __init__(self, actlog_path, *, raise_on_checksum_failure=False, raise_on_invalid_id=False):
#         # might need a helper function, but eh. Also TODO: close file at some point to be nice
#         self.handle = open(actlog_path, 'r')
#         # Let's talk about this. ACT network logs seem to use two different indexes – one for
#         # network events, and one for other types of events. Without breaking the code too badly,
#         # might be good to identify if an ID is based off network or 'other' (memory events only?)
#         # and cycle through the correct indexes
#         self.index = 1
#         self.raise_on_checksum_failure = raise_on_checksum_failure
#         self.raise_on_invalid_id = raise_on_invalid_id

#     def handle_line(self, line: str) -> Event:
#         """Handles an act-specific line"""
#         args = line.strip().split('|')
#         id_ = int(args[0])
#         datestr = args[1]

#         event = None

#         if id_ in IdEventMapping:
#             if id_ in [EventType.config.value]:
#                 # special handling - this one doesn't have a checksum
#                 event = IdEventMapping[id_](datestr, params=args[2:])
#             else:
#                 event = IdEventMapping[id_](datestr, params=args[2:-1], index=self.index, checksum=args[-1])
#             if self.raise_on_checksum_failure and not event.valid_checksum():
#                 raise InvalidChecksum(f'Checksum is invalid for event: {line} (index {self.index})')
#         elif self.raise_on_invalid_id:
#             raise EventNotFound(f'No event found for id {id}')
#         else:
#             event = Event(datestr, params=args[2:-1], index=self.index, checksum=args[-1], id_=id_)

#         self.index += 1
#         return event


#     def read_next(self) -> Union[Event, None]:
#         """Returns an array of all the act log events from the file"""
#         line: str = self.handle.readline()
#         if len(line) == 0:
#             return None
#         return self.handle_line(line)

class ActLogReader(Reader):
    """Translate ACT log events to nari event types"""
    def __init__(self, actlog_path: str, *, raise_on_checksum_failure: bool = False, raise_on_invalid_id: bool = False):
        self.handle = open(actlog_path, 'r')

    def handle_line(self, line: str) -> Event:
        """Handles an act-specific line"""
        args = line.strip().split('|')
        id_ = int(args[0])
        timestamp = actutils.date_from_act_timestamp(args[1])
        

    def read_next(self) -> Optional[Event]:
        line: str = self.handle.readline()
        if len(line) == 0:
            return None
