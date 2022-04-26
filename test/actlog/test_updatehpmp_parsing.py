import unittest

from nari.io.reader.actlogutils.updatehpmp import updatehpmp_from_logline
from nari.types.event.updatehpmp import UpdateHpMp


class TestLineChecksum(unittest.TestCase):
    def test_line_when_sp_is_empty(self):
        timestamp = 0000
        show_default_hpmp = '106652C6||50875||10000|||||||'.split('|')
        result: UpdateHpMp = updatehpmp_from_logline(timestamp, show_default_hpmp)
        self.assertEqual(result.sp, 0)


if __name__ == '__main__':
    unittest.main()
