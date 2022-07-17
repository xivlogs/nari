"""Class that represents version(s)"""
from nari.types import Timestamp
from nari.types.event import Event
from packaging import version as semver

class Version(Event): # pylint: disable=too-few-public-methods
    """Represents a version string found in the events"""
    def __init__(self, *,
                 timestamp: Timestamp,
                 version: str,
                ):
        super().__init__(timestamp)
        self.version = version

    def __repr__(self):
        return f'<Version> {self.version}'

    def after(self, ref: str) -> bool:
        """Returns true if reference version is less than class version"""
        return semver.parse(self.version) > semver.parse(ref)
