from unittest import TestCase

from nari.types import HexStr
from nari.util.byte import hexstr_to_bytes, hexstr_to_int
from nari.util.pair import IdNamePair


class TestHexStr(TestCase):
    def test_hextstr_to_int(self):
        result = hexstr_to_int("0F123")
        self.assertEqual(result, 61731)

    def test_hextstr_to_bytes(self):
        result = hexstr_to_bytes("0F123")
        self.assertEqual(result, b'\x00\x00\xf1#')

    def test_hextstr_to_bytes_reverse(self):
        result = hexstr_to_bytes("0F123", reverse=True)
        self.assertEqual(result, b'#\xf1\x00\x00')

    def test_hexstr_to_bytes_intsize(self):
        result = hexstr_to_bytes("0F123", byte_size=8)
        self.assertEqual(result, b'\x00\x00\x00\x00\x00\x00\xf1#')


class TestIdNamePair(TestCase):
    def test_idnamepair_from_tuple_dec(self):
        params = [10, "YoshiP Sampo"]
        result = IdNamePair(*params[0:2])

        self.assertIsInstance(result, IdNamePair)
        self.assertEqual(result.id, 10)
        self.assertEqual(result.name, "YoshiP Sampo")
        self.assertEqual(repr(result), "<Pair 10:YoshiP Sampo>")

    def test_idnamepair_from_tuple_hex(self):
        params = ["A", "YoshiP Sampo"]
        result = IdNamePair(*params[0:2])

        self.assertIsInstance(result, IdNamePair)
        self.assertEqual(result.id, 10)
        self.assertEqual(result.name, "YoshiP Sampo")
        self.assertEqual(repr(result), "<Pair 10:YoshiP Sampo>")
