from nari.parser.event.base import Event
from nari.types.event import Type
from nari.types.director import DirectorUpdateType

class DirectorUpdate(Event):
    """Can apparently do several things:
    * change the music
    * reset zone on a wipe
    * limit gauge for bosses
    * updates on time remaining
    """
    __id__ = Type.directorupdate.value
    def handle_params(self):
        self.director_type = int(self.params[0][:4], 16)
        self.instance_id = int(self.params[0][4:], 16)
        # still not sure about these
        # param[1] - Command? Cactbot notes that 40000010 is a wipe, for example
        # param[2:6] - 4 bytes of arbitrary data 
    
    def __repr__(self):
        return f'<DirectorUpdate ({DirectorUpdateType.name_for_value(self.director_type)})>'