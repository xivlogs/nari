from datetime import datetime
from typing import List

from nari.types.actor import Actor
from nari.types.event import Event
from nari.types.event.actorspawn import ActorSpawn

def actor_spawn_from_logline(timestamp: datetime, params: List[str]) -> Event:
    # param layout from act
    # 0-1 actor id/name
    # 2-3 source current/max hp
    # 4-5 source current/max mp
    # 6-7 source current/max tp/others?
    # 8-11 source actor x/y/z/facing
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