"""Exceptions related to ACT log parsing"""

class ActLineParsingException(Exception):
    """Raised when an ACT log line cannot be parsed"""


class InvalidActChecksum(Exception):
    """Raised when a checksum is invalid"""


class InvalidMarkerID(Exception):
    """Raised when a marker ID not a known value"""


class InvalidMarkerOperation(Exception):
    """Raised when a marker operation is not known"""
