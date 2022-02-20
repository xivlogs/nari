"""Parse actor spawn data from act log line"""
from nari.types import Timestamp
from nari.types.actor import Actor
from nari.types.event import Event
from nari.types.event.actorspawn import ActorSpawn

def actor_spawn_from_logline(timestamp: Timestamp, params: list[str]) -> Event:
    """Returns an actor spawn event from an act logline

    ACT Event ID (decimal):

    ## Param layout from act

    The first two params in every event is the act event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Source actor ID|
    |1    |string|Source actor name|
    |2    |int|Source current HP|
    |3    |int|Source max HP|
    |4    |int|Source current MP|
    |5    |int|Source max MP|
    |6    |int|Source current TP/others?|
    |7    |int|Source max TP/others?|
    |8    |float|Source actor X position|
    |9    |float|Source actor Y position|
    |10   |float|Source actor Z position|
    |11   |float|Source actor facing|

    """
    source_actor = Actor(*params[0:2])
    try:
        source_actor.resources.update(
            *[int(x) for x in params[2:8]]
        )
        source_actor.position.update(
            *[float(x) for x in params[8:12]]
        )
    except ValueError:
        pass

    return ActorSpawn(
        timestamp=timestamp,
        actor=source_actor
    )
