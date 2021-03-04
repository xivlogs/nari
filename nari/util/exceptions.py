"""Nari-related exceptions"""

class EventNotFound(Exception):
    """Thrown when events are not found"""

class InvalidChecksum(Exception):
    """Thrown when the checksum of an event doesn't match"""
