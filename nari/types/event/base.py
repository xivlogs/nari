from datetime import datetime
from hashlib import md5
from typing import List

class Event(object):
    """Represents a base event"""
    __id__: int = -1

    def __init__(self, timestamp: datetime, params: List[str] = [], index: int = 0, checksum: str = '', id: int = None):
        self.id = id or self.__id__
        self.timestamp = timestamp
        self.params = params
        self.checksum = checksum
        self.index = index

        self.handle_params()

    def handle_params(self):
        pass

    def valid_checksum(self) -> bool:
        """"""
        if self.index > 0:
            checkstr = f'{str(self.id).rjust(2, "0")}|{self.timestamp}|{"|".join(self.params)}|{self.index}'.encode('utf-8')
            return  md5(checkstr).hexdigest() == self.checksum
        return True

    def __repr__(self) -> str:
        return f'<Event {self.id} ({"|".join(self.params)})>'