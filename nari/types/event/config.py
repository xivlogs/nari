from nari.types.event.base import Event
from nari.types.event import Type

class Config(Event):
    """Represents ACT config options"""
    __id__ = Type.config.value
    def handle_params(self):
        self.options = self.params[0].split(', ')
    
    def __repr__(self):
        return f'<Config ({";".join(self.options)})>'