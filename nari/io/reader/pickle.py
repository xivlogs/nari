"""Reads pickle'd event files"""

from pickle import load
from typing import Optional

from nari.io.reader import Reader
from nari.types.event import Event


class PickleReader(Reader):
    """Opens up a pickle file with events and reads them out"""
    def __init__(self, filename: str):
        self.handle = open(filename, 'rb')

    def __del__(self):
        """Handles closing the file when the object undergoes garbage collection"""
        self.handle.close()

    def read_next(self) -> Optional[Event]:
        try:
            return load(self.handle)
        except EOFError:
            return None
