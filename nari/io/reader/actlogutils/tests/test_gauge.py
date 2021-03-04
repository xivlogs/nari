import unittest
from nari.io.reader.actlogutils import date_from_act_timestamp, gauge
from nari.types.event.gauge import Gauge


class GaugeTestCase(unittest.TestCase):
    def test_sch_aetherflow(self):
        test_string = "31|2021-02-04T21:51:04.3820000+09:00|1029BDAA|300001C|00|800|426E3855" \
                      "|083c7ec0220b2c890503f47c3f265078"
        test_params = test_string.split("|")[2:]
        test_timestamp = date_from_act_timestamp(test_string.split("|")[1])
        gauge_result = gauge.gauge_from_logline(test_timestamp, test_params)
        expected_bytes = tuple([bytes([0x1c, 0x00, 0x00, 0x03]),
                                bytes([0x00, 0x00, 0x00, 0x00]),
                                bytes([0x00, 0x08, 0x00, 0x00]),
                                bytes([0x55, 0x38, 0x6e, 0x42])])
        expected_gauge = Gauge(timestamp=test_timestamp, actor_id=int("1029BDAA", 16), fields=expected_bytes)
        self.assertEqual(gauge_result, expected_gauge)

    def test_sch_no_aetherflow(self):
        test_string = "31|2021-02-04T21:51:14.0590000+09:00|1029BDAA|1C|1E|300|414B0A28" \
                      "|202a8e1dd5aba0cc4fe83544d4fe34e1 "
        test_params = test_string.split("|")[2:]
        test_timestamp = date_from_act_timestamp(test_string.split("|")[1])
        gauge_result = gauge.gauge_from_logline(test_timestamp, test_params)
        expected_bytes = tuple([bytes([0x1c, 0x00, 0x00, 0x00]),
                                bytes([0x1e, 0x00, 0x00, 0x00]),
                                bytes([0x00, 0x03, 0x00, 0x00]),
                                bytes([0x28, 0x0a, 0x4b, 0x41])])
        expected_gauge = Gauge(timestamp=test_timestamp, actor_id=int("1029BDAA", 16), fields=expected_bytes)
        self.assertEqual(gauge_result, expected_gauge)

    def test_sch_dissipation(self):
        test_string = "31|2021-02-04T21:51:16.4640000+09:00|1029BDAA|300001C|600001E|00|00" \
                      "|95bd2835b76abb53b65fa45e81d44a4f "
        test_params = test_string.split("|")[2:]
        test_timestamp = date_from_act_timestamp(test_string.split("|")[1])
        gauge_result = gauge.gauge_from_logline(test_timestamp, test_params)
        expected_bytes = tuple([bytes([0x1c, 0x00, 0x00, 0x03]),
                                bytes([0x1e, 0x00, 0x00, 0x06]),
                                bytes([0x00, 0x00, 0x00, 0x00]),
                                bytes([0x00, 0x00, 0x00, 0x00])])
        expected_gauge = Gauge(timestamp=test_timestamp, actor_id=int("1029BDAA", 16), fields=expected_bytes)
        self.assertEqual(gauge_result, expected_gauge)

    def test_short_line(self):
        # TODO: implement with exception
        pass

    def test_long_line(self):
        # TODO: implement with exception
        pass


if __name__ == '__main__':
    unittest.main()
