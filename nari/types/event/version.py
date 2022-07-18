"""Class that represents version(s)"""
from dataclasses import dataclass
from nari.types import Timestamp
from nari.types.event import Event

@dataclass(order=True)
class SemanticVersion():
    """Represents a semantic version string that can compare versions"""
    major: int
    minor: int
    patch: int
    build: int


class Version(Event): # pylint: disable=too-few-public-methods
    """Represents a version string found in the events"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 version: str,
                ):
        super().__init__(timestamp)
        # "FFXIV PLUGIN VERSION: 2.2.1.6"
        self.version = SemanticVersion(*(int(v) for v in version[22:].split('.')))

    def __repr__(self):
        return f'<Version> {self.version}'
