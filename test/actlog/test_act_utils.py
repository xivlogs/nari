import unittest

from nari.io.reader.actlogutils import validate_checksum


class TestLineChecksum(unittest.TestCase):

    def test_line(self):
        """
        Tests act checksum validation for lines
        """
        test_line = "253|2020-09-10T22:36:46.6756722-04:00|FFXIV PLUGIN VERSION: 2.0.6.8|4b16c21ba358b9543c75ad2f090cac53"
        self.assertEquals(validate_checksum(test_line, 1), True)


if __name__ == '__main__':
    unittest.main()