import unittest
from typing import Optional

from nari.io.reader.actlogutils.targetmarker import targetmarker_from_logline
from nari.types.event.markers import PlayerMarkerType, MarkerOperation, PlayerMarker
from nari.io.reader.actlogutils.exceptions import InvalidMarkerID


class TestLineChecksum(unittest.TestCase):

    def test_line(self):
        """
        Tests ACT validation for marker parsing
        """
        timestamp = 0000 # THE START OF TIME
        add_marker_attack_1 = "Add|0|10909B23|Danger Duckling|40001112|Striking Dummy".split('|')
        result: PlayerMarker = targetmarker_from_logline(timestamp, add_marker_attack_1)
        self.assertNotEqual(result, None)
        self.assertEqual(result.operator, MarkerOperation.Add)
        self.assertEqual(result.marker, PlayerMarkerType.Attack1)

    def test_raise(self):
        """
        Tests that we raise when providing an invalid marker id
        """
        timestamp = 0000 # THE START OF TIME
        add_invalid_marker = "Add|56|10909B23|Danger Duckling|40001112|Striking Dummy".split('|')
        with self.assertRaises(InvalidMarkerID):
            result = targetmarker_from_logline(timestamp, add_invalid_marker)


if __name__ == '__main__':
    unittest.main()
