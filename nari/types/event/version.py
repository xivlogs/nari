"""Class that represents version(s)"""
from dataclasses import dataclass
from nari.types import Timestamp
from nari.types.event import Event

@dataclass(order=True)
class SemanticVersion(object):
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
        self.version = SemanticVersion(*(int(v) for v in params[2].split('.')))

    def __repr__(self):
        return f'<Version> {self.version}'

    def after(self, ref: SemanticVersion) -> bool:
        """Returns true if reference version is less than class version"""
        return self.version > ref
