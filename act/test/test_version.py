import unittest
from typing import Optional

from nari.ext.act.actlogutils.metadata import version_from_logline
from nari.types.event.version import SemanticVersion, Version
from nari.util.exceptions import CannotParseVersion


class TestVersionFromACTLogLine(unittest.TestCase):

    def test_old_line(self):
        """
        Tests ACT version parsing in older versions (2.2.1.6 or older)
        """
        timestamp = 0000 # THE START OF TIME
        version_string = "FFXIV PLUGIN VERSION: 2.2.1.6".split('|')
        result: Version = version_from_logline(timestamp, version_string)
        self.assertIsInstance(result.version, SemanticVersion)
        self.assertEqual(result.version, SemanticVersion(2,2,1,6))

    def test_new_line(self):
        """
        Tests ACT version parsing in newer versions
        """
        timestamp = 0000 # THE START OF TIME
        version_string = "FFXIV_ACT_Plugin Version: 2.6.4.1 (50BCD605C50A749F)".split('|')
        result: Version = version_from_logline(timestamp, version_string)
        self.assertIsInstance(result.version, SemanticVersion)
        self.assertEqual(result.version, SemanticVersion(2,6,4,1))

    def test_raise(self):
        """
        Test ACT version parsing failure throws expected exception
        """
        timestamp = 0000 # THE START OF TIME
        version_string = "FFXIV PLUGIN VERSION 6.9.4.20".split('|')
        with self.assertRaises(CannotParseVersion):
            version_from_logline(timestamp, version_string)

if __name__ == '__main__':
    unittest.main()
