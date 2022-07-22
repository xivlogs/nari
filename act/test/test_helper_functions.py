import unittest

from nari.ext.act.actlogutils import date_from_act_timestamp
from nari.ext.act.actlogutils.playerstats import playerstats_from_logline
from nari.types.job import Job
from nari.types.stats import Stats
from nari.types.event.playerstats import PlayerStats


class TestPlayerStatsFromACTLogLine(unittest.TestCase):

    def test_base_case(self):
        """
        Tests the case from Luna
        """
        test_line = "33|115|226|3162|241|2276|610|115|364|2484|2276|2276|1949|364|1074|0|364|4000174AEA370F|8fb8294d68dd2159f694b8a975b43ee4"
        test_params = test_line.split("|")
        timestamp = date_from_act_timestamp("2020-09-11T00:13:57.7510000-04:00")

        asserted_event = PlayerStats(
            timestamp,
            Job(33),
            {
                Stats.STR: 115,
                Stats.DEX: 226,
                Stats.VIT: 3162,
                Stats.INT: 241,
                Stats.MND: 2276,
                Stats.PIE: 610,
                Stats.ATK: 115,
                Stats.DH: 364,
                Stats.CRIT: 2484,
                Stats.MATK: 2276,
                Stats.HATK: 2276,
                Stats.DET: 1949,
                Stats.SKS: 364,
                Stats.SPS: 1074,
                Stats.TEN: 364
            })
        self.addTypeEqualityFunc(PlayerStats, self.are_playerevents_equal)
        self.assertEqual(asserted_event, playerstats_from_logline(timestamp, test_params))

    def are_playerevents_equal(self, first_event, second_event, msg=None):
        """
        Sets equality for two playerstats events
        """
        self.assertEqual(type(first_event), type(second_event))
        self.assertEqual(first_event.timestamp, second_event.timestamp)
        self.assertEqual(first_event.strength, second_event.strength)
        self.assertEqual(first_event.dexterity, second_event.dexterity)
        self.assertEqual(first_event.intelligence, second_event.intelligence)
        self.assertEqual(first_event.mind, second_event.mind)
        self.assertEqual(first_event.piety, second_event.piety)
        self.assertEqual(first_event.attack, second_event.attack)
        self.assertEqual(first_event.direct_hit, second_event.direct_hit)
        self.assertEqual(first_event.critical_hit, second_event.critical_hit)
        self.assertEqual(first_event.magic_attack, second_event.magic_attack)
        self.assertEqual(first_event.heal_attack, second_event.heal_attack)
        self.assertEqual(first_event.determination, second_event.determination)
        self.assertEqual(first_event.skill_speed, second_event.skill_speed)
        self.assertEqual(first_event.spell_speed, second_event.spell_speed)
        self.assertEqual(first_event.tenacity, second_event.tenacity)


if __name__ == "__main__":
    unittest.main()
