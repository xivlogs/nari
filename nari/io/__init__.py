from nari.parser.event.base import Event
from nari.parser.event import IdEventMapping
from nari.util import timestamp_from_datestr
from nari.util.exceptions import EventNotFound

def event_from_str(event: str) -> Event:
    args = event.strip().split('|')
    id = int(args[0])
    timestamp = timestamp_from_datestr(args[1])
    if id in IdEventMapping:
        evt = IdEventMapping[id](timestamp, args[2:])
        return evt
    else:
        raise EventNotFound(f'ID {id} not found: {event}')
    return Event(id, timestamp, args[2:])

# TODO: It's probably valuable to create a Reader and Writer class so that you can do
# complicated scenarios like reading from a file (or another network stream or something?)
# and serialize to a file, or output to an API-bound service, etc
def log_reader(log_path: str, raise_on_unknown: bool=False):
    """Reads a file and returns a list of Event objects"""
    with open(log_path, 'r') as f:
        for line in f:
            yield event_from_str(line)