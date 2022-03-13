import os
import unittest

from src.cnbc.default import *


class TestDefaultEndpoints(unittest.TestCase):
    def test_get_metadata(self):
        """
        Test that get_metadata is communicating with the CNBC API.
        """
        json_resp = get_metadata(api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_auto_complete(self):
        """
        Test that auto_complete is communicating with the CNBC API.
        """
        json_resp = auto_complete(query='tesla',
                                  api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)


if __name__ == '__main__':
    unittest.main()
