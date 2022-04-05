"""Parse HP and MP updates from ACT log line"""
from nari.types import Timestamp
from nari.types.event.updatehpmp import UpdateHpMp
from nari.types.actor import Actor

def updatehp_from_logline(timestamp: Timestamp, params: list[str]) -> UpdateHpMp:
    """Parses an UpdateHpMp event from an act log line

    ACT Event ID (decimal): 39

    ## Param layout from act

    The first two params in every event is the act event ID and the timestamp it was parsed; the following table documents all the other fields.

    |Index|Type|Description|
    |----:|----|:----------|
    |0    |int|Actor ID|
    |1    |string|Actor name|
    |2    |int|Current HP|
    |3    |int|Max HP|
    |4    |int|Current MP|
    |5    |int|Max MP|
    |6    |int|Current TP|
    |7    |int|Max TP|
    |8    |float|Actor X position|
    |9    |float|Actor Y position|
    |10   |float|Actor Z position|
    |11   |float|Actor bearing|
    |12   |string|Blank because ACT|
    """
    actor = Actor(*params[0:2])
    try:
        actor.resources.update(
            *[int(x) for x in params[2:8]]
        )
    except ValueError:
        pass

    return UpdateHpMp(timestamp=timestamp, actor=actor)
