"""Class for player stats"""
from nari.types import Timestamp
from nari.types.event import Event
from nari.types.job import Job
from nari.types.stats import Stats


class PlayerStats(Event):  # pylint: disable=too-few-public-methods,too-many-instance-attributes
    """Represents the event when the player's stats change. Also happens when zone/instance changes."""
    def __init__(self,
                 timestamp: Timestamp,
                 job: Job,
                 stats: dict[Stats, int],
                ):
        super().__init__(timestamp)
        self.job = job
        self.strength = stats[Stats.STR]
        self.dexterity = stats[Stats.DEX]
        self.vitality = stats[Stats.VIT]
        self.intelligence = stats[Stats.INT]
        self.mind = stats[Stats.MND]
        self.piety = stats[Stats.PIE]
        self.attack = stats[Stats.ATK]
        self.direct_hit = stats[Stats.DH]
        self.critical_hit = stats[Stats.CRIT]
        self.magic_attack = stats[Stats.MATK]
        self.heal_attack = stats[Stats.HATK]
        self.determination = stats[Stats.DET]
        self.skill_speed = stats[Stats.SKS]
        self.spell_speed = stats[Stats.SPS]
        self.tenacity = stats[Stats.TEN]

    def __repr__(self):
        return '<PlayerStats>'
