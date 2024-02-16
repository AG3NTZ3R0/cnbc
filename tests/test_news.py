import os
import unittest

from src.cnbc import list_trending_news, list_special_reports, list_symbol_news


class TestNewsEndpoints(unittest.TestCase):
    def test_list_trending_news(self):
        """
        Test that list_trending_news is communicating with the CNBC API.
        """
        json_resp = list_trending_news(count='25',
                                       api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_list_special_reports(self):
        """
        Test that list_special_reports is communicating with the CNBC API.
        """
        json_resp = list_special_reports(api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_list_symbol_news(self):
        """
        Test that list_symbol_news is communicating with the CNBC API.
        """
        json_resp = list_symbol_news(symbol='AAPL',
                                     api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)


if __name__ == '__main__':
    unittest.main()
