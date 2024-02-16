import os
import unittest

from src.cnbc import get_earnings_chart, get_profile, get_chart, translate, get_summary, get_fundamentals, get_priceline_chart, get_peers


class TestSymbolEndpoints(unittest.TestCase):
    def test_get_earnings_chart(self):
        """
        Test that get_earnings_chart is communicating with the CNBC API.
        """
        json_resp = get_earnings_chart(issue_id='36276',
                                       num_of_years='3',
                                       api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_profile(self):
        """
        Test that get_profile is communicating with the CNBC API.
        """
        json_resp = get_profile(issue_id='36276',
                                api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_chart(self):
        """
        Test that get_chart is communicating with the CNBC API.
        """
        json_resp = get_chart(issue_id='36276',
                              interval='1d',
                              api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_translate(self):
        """
        Test that get_summary is communicating with the CNBC API.
        """
        json_resp = translate(symbol='TSLA',
                              api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_summary(self):
        """
        Test that get_summary is communicating with the CNBC API.
        """
        json_resp = get_summary(issue_ids='36276,24812378',
                                api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_fundamentals(self):
        """
        Test that get_fundamentals is communicating with the CNBC API.
        """
        json_resp = get_fundamentals(issue_ids='36276,24812378',
                                     api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_priceline_chart(self):
        """
        Test that get_priceline_chart is communicating with the CNBC API.
        """
        json_resp = get_priceline_chart(issue_id='24812378',
                                        num_of_days='1',
                                        api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_peers(self):
        """
        Test that get_peers is communicating with the CNBC API.
        """
        json_resp = get_peers(symbol='36276',
                              api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)


if __name__ == '__main__':
    unittest.main()
