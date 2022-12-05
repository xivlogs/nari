"""
Config
~~~~~~
"""
from nari.types import Timestamp
from nari.types.event import Event

class Config(Event): # pylint: disable=too-few-public-methods
    """Represents a version string found in the events

    This is a metadata event that doesn't represent an event happening in the
    game, but may contain useful contextual information (parser being used,
    network information, etc)

    :param timestamp: Timestamp of the event
    :type timestamp: Timestamp
    :param values: A dictionary of configuration items
    :type values: dict[str, str]
    """
    def __init__(self, *,
                 timestamp: Timestamp,
                 values: dict[str, str],
                ):
        super().__init__(timestamp)
        self.values = values

    def __repr__(self):
        return f'<Config {self.values.items()}>'
