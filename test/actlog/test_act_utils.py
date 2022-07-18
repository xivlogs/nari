import unittest

from nari.io.reader.actlogutils import ActLogChecksumType, validate_checksum
from nari.io.reader.actlogutils.exceptions import InvalidActChecksumAlgorithm


class TestLineChecksum(unittest.TestCase):

    def test_md5_line(self):
        """
        Tests ACT MD5 checksum validation for lines
        """
        test_line = "253|2020-09-10T22:36:46.6756722-04:00|FFXIV PLUGIN VERSION: 2.0.6.8|4b16c21ba358b9543c75ad2f090cac53"
        self.assertEqual(validate_checksum(test_line, 1, ActLogChecksumType.MD5), True)

    def test_sha256_line(self):
        """
        Tests ACT SHA256 checksum validation for lines
        """
        test_line = "253|2022-02-09T20:09:52.6303877-06:00|FFXIV_ACT_Plugin Version: 2.6.4.1 (50BCD605C50A749F)|5401dc333f466389"
        self.assertEqual(validate_checksum(test_line, 1, ActLogChecksumType.SHA256), True)

    def test_invalid_checksum(self):
        """
        Tests ACT checksum validation against an unknown algorithm
        """
        test_line = "253|2020-09-10T22:36:46.6756722-04:00|FFXIV PLUGIN VERSION: 2.0.6.8|4b16c21ba358b9543c75ad2f090cac53"
        with self.assertRaises(InvalidActChecksumAlgorithm):
            validate_checksum(test_line, 1, "crc32")


if __name__ == '__main__':
    unittest.main()
