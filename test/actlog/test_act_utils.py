import unittest

from nari.io.reader.actlogutils import validate_checksum


class TestLineChecksum(unittest.TestCase):

    def test_line(self):
        """
        Tests act checksum validation for lines
        """
        test_line = "253|2022-02-09T20:09:52.6303877-06:00|FFXIV_ACT_Plugin Version: 2.6.4.1 (50BCD605C50A749F)|5401dc333f466389"
        self.assertEquals(validate_checksum(test_line, 1), True)


if __name__ == '__main__':
    unittest.main()
