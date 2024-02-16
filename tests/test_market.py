import os
import unittest

from src.cnbc import list_indices


class TestMarketEndpoints(unittest.TestCase):
    def test_list_indices(self):
        """
        Test that get_metadata is communicating with the CNBC API.
        """
        json_resp = list_indices(api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)


if __name__ == '__main__':
    unittest.main()
