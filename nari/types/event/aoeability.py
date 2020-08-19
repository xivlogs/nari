"""Class that represents ability uses that affect multiple people"""

from datetime import datetime

from nari.types.event import Event

class AoeAbility(Event): # pylint: disable=too-few-public-methods
    """An ability that hits multiple people"""
    def __init__(self, *
                 timestamp: datetime):
        super().__init__(timestamp)

    def __repr__(self):
        return '<AoEAbility>'
