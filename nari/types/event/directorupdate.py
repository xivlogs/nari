from nari.types.event.base import Event
from nari.types.event import Type
from nari.types.director import DirectorUpdateType, DirectorUpdateCommand

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
        self.director_command = int(self.params[1], 16)
        # param[2:6] - 4 bytes of arbitrary data, dependant on the director command
    
    def __repr__(self):
        dtype = DirectorUpdateType.name_for_value(self.director_type)
        dcomm = DirectorUpdateCommand.name_for_value(self.director_command)
        return f'<DirectorUpdate ({dtype}|{dcomm})>'