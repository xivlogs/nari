from nari.parser.event.base import Event
from nari.types.event import Type

class ActorControl(Event):
    """Can apparently do several things:
    * change the music
    * reset zone on a wipe
    * limit gauge for bosses
    * updates on time remaining
    """
    __id__ = Type.actorcontrol.value
    # Looks like the params work out like this:
    # param[0] - ZoneId
    # param[1] - Command
    # param[2:] - Data to change?
    
    def __repr__(self):
        return f'<ActorControl ({self.params[2]})>'