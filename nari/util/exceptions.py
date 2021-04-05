"""Nari-related exceptions"""

class EventNotFound(Exception):
    """Thrown when events are not found"""

class InvalidChecksum(Exception):
    """Thrown when the checksum of an event doesn't match"""

class JobGaugeNotFound(Exception):
    """Thrown when gauge data is not found for job"""

class ActLineReadError(Exception):
    """Thrown when error reading a line from ACT log"""