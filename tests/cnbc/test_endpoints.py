"""
Test the Endpoints enum.
"""
import unittest

from src.cnbc.endpoints import Endpoints
from src.cnbc.exceptions import InvalidParameterConfiguration


class TestEndpoints(unittest.TestCase):
    """
    Test the Endpoints enum.
    """

    def test_parameters_set_item_invalid_parameter_configuration(self):
        """
        Test the __setitem__ method of the Parameters class for an invalid parameter configuration.
        :return: None
        """
        with self.assertRaises(InvalidParameterConfiguration):
            Endpoints.GET_FUNDAMENTALS.get_parameters()["key"] = "value"

    def test_get_endpoint_host(self):
        """
        Test the get_endpoint method of the Endpoints enum for the attributes which aren't endpoints.
        :return: None
        """
        self.assertEqual(None, Endpoints.HOST.get_endpoint())

    def test_get_endpoint(self):
        """
        Test the get_endpoint method of the Endpoints enum.
        :return: None
        """
        self.assertEqual("https://cnbc.p.rapidapi.com/symbols/get-fundamentals", Endpoints.GET_FUNDAMENTALS.get_endpoint())

    def test_get_parameters_host(self):
        """
        Test the get_parameters method of the Endpoints enum for the attributes which aren't endpoints.
        :return:
        """
        self.assertEqual(None, Endpoints.HOST.get_parameters())

    def test_get_parameters(self):
        """
        Test the get_parameters method of the Endpoints enum.
        :return:
        """
        self.assertEqual({"issueIds": None}, Endpoints.GET_FUNDAMENTALS.get_parameters())
