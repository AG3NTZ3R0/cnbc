"""
Test the APIWrapper class.
"""
import unittest
from unittest.mock import patch, MagicMock

from src.cnbc.api_wrapper import APIWrapper
from src.cnbc.endpoints import Endpoints
from src.cnbc.exceptions import InvalidParameterConfiguration


class TestAPIWrapper(unittest.TestCase):
    """
    Test the APIWrapper class.
    """

    def test_set_params(self):
        """
        Test the set_params method.
        :return: None
        """
        endpoint = APIWrapper("API_KEY", Endpoints.GET_FUNDAMENTALS)
        endpoint_params = {"issueIds": None}
        endpoint.params = endpoint_params
        self.assertEqual(endpoint_params, endpoint.params)

    def test_set_params_invalid_parameter_configuration(self):
        """
        Test the set_params method with an invalid parameter configuration.
        :return: None
        """
        endpoint = APIWrapper("API_KEY", Endpoints.GET_FUNDAMENTALS)
        with self.assertRaises(InvalidParameterConfiguration):
            endpoint.params = {"key": "value"}

    @patch('src.cnbc.api_wrapper.requests.request')
    def test_request(self, mock_request: MagicMock):
        """
        Test the request method.
        :param mock_request: The mock request.
        :return: None
        """
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}

        mock_request.return_value.__enter__.return_value = mock_response

        endpoint = APIWrapper("API_KEY", Endpoints.GET_METADATA)
        response = endpoint.request()

        mock_request.assert_called_once_with(
            "GET", endpoint.endpoint,
            headers=endpoint.headers, params=endpoint.params, timeout=endpoint.timeout
        )
        self.assertEqual({"key": "value"}, response)

    def test_request_translate_translation_table(self):
        """
        Test the request method with the translate endpoint with a translation table.
        :return: None
        """
        translation_table = {'AAPL': '123'}
        json_response_expected = {'issueId': '123', 'errorMessage': '', 'errorCode': ''}

        api_wrapper = APIWrapper('API_KEY', Endpoints.TRANSLATE)
        api_wrapper._translation_table = translation_table
        api_wrapper_params = api_wrapper.params
        api_wrapper_params['symbol'] = 'AAPL'
        json_response = api_wrapper.request()

        self.assertEqual(translation_table, api_wrapper.translation_table)
        self.assertEqual(json_response_expected, json_response)

    @patch('src.cnbc.api_wrapper.requests.request')
    def test_request_translate_translation_table_empty(self, mock_request: MagicMock):
        """
        Test the request method with the translate endpoint without a translation table.
        :param mock_request: The mock request.
        :return: None
        """
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'issueId': '123', 'errorMessage': '', 'errorCode': ''}

        mock_request.return_value.__enter__.return_value = mock_response

        translation_table = {'AAPL': '123'}

        api_wrapper = APIWrapper('API_KEY', Endpoints.TRANSLATE)
        api_wrapper_params = api_wrapper.params
        api_wrapper_params['symbol'] = 'AAPL'
        json_response = api_wrapper.request()

        mock_request.assert_called_once_with(
            "GET", api_wrapper.endpoint,
            headers=api_wrapper.headers, params=api_wrapper.params, timeout=api_wrapper.timeout
        )
        self.assertEqual(translation_table, api_wrapper.translation_table)
        self.assertEqual(mock_response.json.return_value, json_response)
