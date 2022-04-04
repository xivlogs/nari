"""Exceptions related to ACT log parsing"""

class InvalidActChecksum(Exception):
    """Raised when a checksum is invalid"""


class InvalidMarkerID(Exception):
    """Raised when a marker ID not a known value"""


class InvalidMarkerOperation(Exception):
    """Raised when a marker operation is not known"""
